"""Mapping complex traits: Manhattan and QQ plots, linkage-disequilibrium triangles, LOD profiles of interval
mapping, and the simulations behind them (haplotypes with recombination hotspots, case-control association
scans, backcross QTL crosses) together with the standard power and prediction formulas.

All drawing functions draw on an ordinary matplotlib axes (``plt.subplots`` or ``charts.axes_at``) in the
palette colours; all simulations are deterministic for a given ``rng`` (default seed 0).

    from wikibio import gwas
    rng = np.random.default_rng(1)
    H, pos = gwas.simulate_haplotypes(300, 40, hotspots=[0.35, 0.7], rng=rng)   # (haplotypes, SNPs), positions
    gwas.ld_triangle(ax, gwas.ld_r2(H), pos=pos)                                 # Haploview-style r^2 diamonds
    d = gwas.simulate_case_control(2000, 2000, causal=[(3, 120, 1.3)], rng=rng)  # dict of chrom, pos, p, ...
    gwas.manhattan(ax, d["chrom"], d["pos"], d["p"])
    gwas.qq(ax, d["p"])                                                           # with lambda_GC and 95 % band
    m = gwas.backcross_scan(200, qtl=45.0, effect=0.6, rng=rng)                  # Haley-Knott interval mapping
    gwas.lod_profile(ax, m["x"], m["lod"], threshold=m["threshold"], markers=m["markers"], qtl=45.0)

Models: ``allelic_test`` is the 1-df chi-square test on the 2 x 2 table of allele counts; ``lambda_gc`` the
median chi-square divided by its null median 0.4549; ``power_quantitative(N, maf, beta, ...)`` uses the
noncentrality N 2pq beta^2 / sigma^2 of the 1-df test; ``pgs_r2(N, h2, Me)`` is the expected accuracy of a
polygenic score, h2 / (1 + Me / (N h2)) (Daetwyler et al. 2008).
"""

import math

import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.patches import Polygon, Rectangle

from . import palette as P
from .core import FONT


def _line(token):
    if token in (None, "ink"):
        return P.ink()
    if token == "muted":
        return P.muted()
    return P.fill(token) if P.is_dark() else P.edge(token)


def _scipy_stats():
    from scipy import stats  # imported lazily: only the plots that need quantiles pay for it

    return stats


# ------------------------------------------------------------------ simulations


def simulate_haplotypes(n_hap, n_snp, length=1.0, hotspots=(), founders=8, rho_bg=0.4, rho_hot=60.0,
                        hot_width=0.02, mutation=0.004, maf_min=0.05, rng=None):
    """Haplotypes as mosaics of a few founder haplotypes (a Li-Stephens style copying model).

    ``n_snp`` SNPs lie at sorted uniform positions on ``[0, length]``. Along each sampled haplotype the
    copied founder switches between adjacent SNPs with probability ``1 - exp(-rho * gap)``, where ``rho`` is
    ``rho_bg`` (per unit length) in the background and ``rho_bg + rho_hot`` inside a hotspot (a window of half-width
    ``hot_width`` around each position in ``hotspots``); copying errors flip an allele with probability
    ``mutation``. LD therefore stays high within the blocks between hotspots and breaks down across them.
    Returns ``(H, pos)``: an int8 array (n_hap, n_snp) of 0/1 alleles and the SNP positions.
    """
    rng = rng or np.random.default_rng(0)
    pos = np.sort(rng.uniform(0, length, n_snp))
    # founder alleles: within each block between hotspots the SNPs reuse a few founder partitions (as
    # SNPs on the same branch of a local genealogy do), so that r^2 is high inside blocks
    edges = np.concatenate([[-np.inf], np.sort(np.asarray(hotspots, float)), [np.inf]])
    block = np.searchsorted(edges, pos) - 1

    def partition():
        while True:
            col = (rng.random(founders) < rng.uniform(0.15, 0.6)).astype(np.int8)
            if 0 < col.sum() < founders:
                return col

    F = np.zeros((founders, n_snp), dtype=np.int8)
    for bk in np.unique(block):
        parts = [partition() for _ in range(3)]
        for j in np.where(block == bk)[0]:
            F[:, j] = parts[int(rng.integers(3))] if rng.random() < 0.8 else partition()
    weights = rng.dirichlet(np.full(founders, 2.0))
    gaps = np.diff(pos)
    mids = (pos[:-1] + pos[1:]) / 2
    rho = np.full(n_snp - 1, rho_bg)
    for h in hotspots:
        rho = rho + rho_hot * (np.abs(mids - h) < hot_width + gaps / 2)
    switch = 1 - np.exp(-rho * gaps)
    H = np.empty((n_hap, n_snp), dtype=np.int8)
    for i in range(n_hap):
        f = rng.choice(founders, p=weights)
        H[i, 0] = F[f, 0]
        for j in range(1, n_snp):
            if rng.random() < switch[j - 1]:
                f = rng.choice(founders, p=weights)
            H[i, j] = F[f, j]
    flips = rng.random(H.shape) < mutation
    H = np.where(flips, 1 - H, H).astype(np.int8)
    # keep the minor allele frequency above maf_min by flipping too-rare columns into common ones
    freq = H.mean(0)
    rare = np.minimum(freq, 1 - freq) < maf_min
    for j in np.where(rare)[0]:
        k = int(rng.integers(n_hap // 5, n_hap // 2))
        H[rng.choice(n_hap, k, replace=False), j] = 1 - H[0, j]
    return H, pos


def ld_r2(H):
    """Matrix of r^2 between the columns (SNPs) of a 0/1 haplotype array; monomorphic SNPs give 0."""
    X = np.asarray(H, dtype=float)
    X = X - X.mean(0)
    sd = np.sqrt((X**2).mean(0))
    ok = sd > 0
    R = np.zeros((X.shape[1], X.shape[1]))
    Z = X[:, ok] / sd[ok]
    R[np.ix_(ok, ok)] = (Z.T @ Z) / X.shape[0]
    return np.clip(R**2, 0, 1)


def ld_dprime(H):
    """Matrix of |D'| between the columns of a 0/1 haplotype array."""
    X = np.asarray(H, dtype=float)
    n, m = X.shape
    p = X.mean(0)
    pab = (X.T @ X) / n
    D = pab - np.outer(p, p)
    q = 1 - p
    dmax = np.where(D >= 0, np.minimum(np.outer(p, q), np.outer(q, p)), np.minimum(np.outer(p, p), np.outer(q, q)))
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(dmax > 0, np.abs(D) / dmax, 0.0)
    return np.clip(out, 0, 1)


def allelic_test(case_alt, case_n, ctrl_alt, ctrl_n):
    """Pearson chi-square (1 df) on the 2 x 2 table of allele counts; vectorized. Returns (chi2, p, OR).

    ``case_alt`` alternative alleles among ``case_n`` case chromosomes, likewise for controls.
    The odds ratio has 0.5 added to every cell (Haldane-Anscombe) so that it is always finite."""
    a = np.asarray(case_alt, float)
    b = np.asarray(case_n, float) - a
    c = np.asarray(ctrl_alt, float)
    d = np.asarray(ctrl_n, float) - c
    n = a + b + c + d
    num = n * (a * d - b * c) ** 2
    den = (a + b) * (c + d) * (a + c) * (b + d)
    with np.errstate(divide="ignore", invalid="ignore"):
        chi2 = np.where(den > 0, num / den, 0.0)
    p = _scipy_stats().chi2.sf(chi2, 1)
    OR = ((a + 0.5) * (d + 0.5)) / ((b + 0.5) * (c + 0.5))
    return chi2, p, OR


def simulate_case_control(n_case, n_control, n_chrom=10, snps_per_chrom=600, causal=(), ld_decay=0.8,
                          ld_reach=12, fst=0.0, case_share=0.5, control_share=0.5, maf=(0.05, 0.5), rng=None):
    """A genome scan of a case-control study under the allelic (multiplicative) model.

    Chromosome ``c`` (1-based) has ``snps_per_chrom`` SNPs at positions 1..n (unit: SNP index; chromosomes
    get lengths proportional to ``1.2 - 0.04 c`` so that they look like a karyotype). ``causal`` lists
    ``(chrom, index, odds_ratio)``; SNPs within ``ld_reach`` of a causal SNP carry the log odds ratio scaled
    by ``ld_decay ** distance`` (the tag-SNP effect of linkage disequilibrium). Population stratification:
    with ``fst > 0`` the sample is a mixture of two subpopulations whose allele frequencies differ by
    ``Normal(0, fst p (1 - p))`` and which contribute ``case_share`` of the cases and ``control_share`` of
    the controls. Returns a dict with ``chrom``, ``pos``, ``p``, ``chi2``, ``OR``, ``freq`` and ``causal``
    (the flat indices of the causal SNPs).
    """
    rng = rng or np.random.default_rng(0)
    sizes = [max(50, int(round(snps_per_chrom * (1.2 - 0.04 * c)))) for c in range(1, n_chrom + 1)]
    chrom = np.concatenate([np.full(s, c) for c, s in enumerate(sizes, start=1)])
    pos = np.concatenate([np.arange(1, s + 1) for s in sizes]).astype(float)
    m = chrom.size
    f = rng.uniform(*maf, m)
    logor = np.zeros(m)
    flat_causal = []
    starts = np.concatenate([[0], np.cumsum(sizes)[:-1]])
    for c, idx, orr in causal:
        k = int(starts[c - 1] + idx)
        flat_causal.append(k)
        lo, hi = max(int(starts[c - 1]), k - ld_reach), min(int(starts[c - 1] + sizes[c - 1]) - 1, k + ld_reach)
        for j in range(lo, hi + 1):
            logor[j] += math.log(orr) * ld_decay ** abs(j - k) * (1 if j == k else rng.uniform(0.6, 1.0))
    delta = rng.normal(0, np.sqrt(fst * f * (1 - f))) if fst > 0 else np.zeros(m)
    f1, f2 = np.clip(f + delta, 0.01, 0.99), np.clip(f - delta, 0.01, 0.99)

    def case_freq(q):
        o = np.exp(logor)
        return o * q / (1 - q + o * q)

    def draw(n, share_pop1, case):
        n1 = int(round(n * share_pop1))
        n2 = n - n1
        q1, q2 = (case_freq(f1), case_freq(f2)) if case else (f1, f2)
        return rng.binomial(2 * n1, q1) + rng.binomial(2 * n2, q2)

    a = draw(n_case, case_share, True)
    c = draw(n_control, control_share, False)
    chi2, p, OR = allelic_test(a, 2 * n_case, c, 2 * n_control)
    return {"chrom": chrom, "pos": pos, "p": np.maximum(p, 1e-300), "chi2": chi2, "OR": OR, "freq": f,
            "causal": flat_causal}


def lambda_gc(p):
    """Genomic inflation factor: median observed 1-df chi-square over the null median (0.4549)."""
    st = _scipy_stats()
    return float(np.median(st.chi2.isf(np.asarray(p, float), 1)) / st.chi2.ppf(0.5, 1))


def haldane_r(d_cm):
    """Recombination fraction for a map distance in centimorgans (Haldane, no interference)."""
    return 0.5 * (1 - np.exp(-2 * np.asarray(d_cm, float) / 100))


def backcross_scan(n, length=100.0, spacing=10.0, qtl=45.0, effect=0.5, sd=1.0, step=1.0, n_perm=200,
                   alpha=0.05, rng=None):
    """Simulate a backcross F1 x P and map one QTL by Haley-Knott regression interval mapping.

    Markers every ``spacing`` cM on a chromosome of ``length`` cM; each backcross individual is
    heterozygous (1) or homozygous (0) along the chromosome, switching state at crossovers (Poisson,
    Haldane). The trait is ``effect`` x (QTL genotype) + Normal(0, sd). At every test position the
    conditional probability of the heterozygote given the flanking markers is regressed on the trait, and
    LOD = (n/2) log10(RSS0 / RSS1). The genome-wide threshold is the (1 - alpha) quantile of the maximum
    LOD over ``n_perm`` permutations of the trait (Churchill and Doerge 1994).
    Returns a dict with ``x`` (cM), ``lod``, ``threshold``, ``markers`` (positions), ``marker_lod``
    (single-marker LOD), ``y``, ``G`` (marker genotypes) and ``qtl_genotype``.
    """
    rng = rng or np.random.default_rng(0)
    markers = np.arange(0, length + 1e-9, spacing)
    loci = np.sort(np.concatenate([markers, [qtl]]))
    r = haldane_r(np.diff(loci))
    geno = np.empty((n, loci.size), dtype=np.int8)
    geno[:, 0] = rng.integers(0, 2, n)
    for j in range(1, loci.size):
        flip = rng.random(n) < r[j - 1]
        geno[:, j] = np.where(flip, 1 - geno[:, j - 1], geno[:, j - 1])
    qi = int(np.searchsorted(loci, qtl))
    qg = geno[:, qi]
    G = np.delete(geno, qi, axis=1)
    y = effect * qg + rng.normal(0, sd, n)
    x = np.arange(0, length + 1e-9, step)
    prob = _hk_probabilities(G, markers, x)

    def lods(yy):
        rss0 = ((yy - yy.mean()) ** 2).sum()
        out = np.empty(x.size)
        for k in range(x.size):
            g = prob[:, k]
            gc = g - g.mean()
            b = (gc * (yy - yy.mean())).sum() / max((gc**2).sum(), 1e-12)
            rss1 = (((yy - yy.mean()) - b * gc) ** 2).sum()
            out[k] = n / 2 * math.log10(rss0 / rss1)
        return out

    lod = lods(y)
    perm = np.array([lods(rng.permutation(y)).max() for _ in range(n_perm)])
    thr = float(np.quantile(perm, 1 - alpha))
    mk = np.array([lod[int(round(m / step))] for m in markers])
    return {"x": x, "lod": lod, "threshold": thr, "markers": markers, "marker_lod": mk, "y": y, "G": G,
            "qtl_genotype": qg, "perm_max": perm}


def _hk_probabilities(G, markers, x):
    """P(heterozygote) at positions x given flanking backcross marker genotypes (no interference)."""
    n = G.shape[0]
    out = np.empty((n, x.size))
    for k, xx in enumerate(x):
        j = int(np.clip(np.searchsorted(markers, xx, side="right") - 1, 0, markers.size - 2))
        a, b = markers[j], markers[j + 1]
        if abs(xx - a) < 1e-9:
            out[:, k] = G[:, j]
            continue
        if abs(xx - b) < 1e-9:
            out[:, k] = G[:, j + 1]
            continue
        r1, r2, r = haldane_r(xx - a), haldane_r(b - xx), haldane_r(b - a)
        gl, gr = G[:, j], G[:, j + 1]
        # P(Q = 1 | left, right) for the four flanking classes
        p_same1 = (1 - r1) * (1 - r2) / (1 - r)
        p_recomb = np.where(gl == 1, (1 - r1) * r2, r1 * (1 - r2)) / r
        out[:, k] = np.where(gl == gr, np.where(gl == 1, p_same1, 1 - p_same1), p_recomb)
    return out


# ------------------------------------------------------------------ formulas


def power_quantitative(N, maf, beta, sd=1.0, alpha=5e-8):
    """Power of the 1-df additive test of a SNP with allele frequency ``maf`` and per-allele effect
    ``beta`` (trait SD ``sd``) in ``N`` individuals: noncentral chi-square with lambda = N 2pq beta^2 / sd^2."""
    st = _scipy_stats()
    lam = np.asarray(N, float) * 2 * maf * (1 - maf) * beta**2 / sd**2
    crit = st.chi2.isf(alpha, 1)
    return st.ncx2.sf(crit, 1, lam)


def pgs_r2(N, h2, Me):
    """Expected R^2 of a polygenic score from a GWAS of N individuals (Daetwyler et al. 2008)."""
    N = np.asarray(N, float)
    return h2 / (1 + Me / (N * h2))


# ------------------------------------------------------------------ drawing


def _style(ax, xlabel=None, ylabel=None):
    for name, sp in ax.spines.items():
        if name in ("top", "right"):
            sp.set_visible(False)
        else:
            sp.set_color(P.muted())
            sp.set_linewidth(0.8)
    ax.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=FONT["tiny"], width=0.7, length=3)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=FONT["small"], color=P.ink())
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=FONT["small"], color=P.ink())


def manhattan(ax, chrom, pos, p, tokens=("dna", "dna2"), threshold=5e-8, suggestive=1e-5, highlight=(),
              highlight_token="negative", gap=0.02, size=5, labels=True):
    """Manhattan plot: -log10 p against genome position, chromosomes in alternating colours.

    ``threshold`` (solid) and ``suggestive`` (dotted) lines are drawn when not None; SNPs in
    ``highlight`` (flat indices) are drawn larger in ``highlight_token``. Returns a dict with the x
    coordinate of every SNP (``x``) and the centre of every chromosome (``centers``)."""
    chrom = np.asarray(chrom)
    pos = np.asarray(pos, float)
    y = -np.log10(np.asarray(p, float))
    ids = list(dict.fromkeys(chrom.tolist()))
    total = sum(pos[chrom == c].max() for c in ids)
    off, x, centers = 0.0, np.empty(pos.size), {}
    for k, c in enumerate(ids):
        sel = chrom == c
        x[sel] = off + pos[sel]
        centers[c] = off + pos[sel].max() / 2
        ax.scatter(x[sel], y[sel], s=size, color=_line(tokens[k % len(tokens)]), lw=0, zorder=3)
        off += pos[sel].max() + gap * total
    hl = np.asarray(list(highlight), int)
    if hl.size:
        ax.scatter(x[hl], y[hl], s=size * 3, color=_line(highlight_token), lw=0, zorder=4)
    if threshold is not None:
        ax.axhline(-math.log10(threshold), color=_line("negative"), lw=0.9, zorder=2)
    if suggestive is not None:
        ax.axhline(-math.log10(suggestive), color=P.muted(), lw=0.8, ls=":", zorder=2)
    ax.set_xlim(-gap * total, off)
    ax.set_ylim(0, max(y.max() * 1.08, -math.log10(threshold or 1e-8) + 1))
    if labels:
        ax.set_xticks([centers[c] for c in ids], [str(c) for c in ids])
    _style(ax, "chromosome" if labels else None, "$-\\log_{10} p$")
    return {"x": x, "centers": centers}


def qq(ax, p, token="dna", band=True, show_lambda=True, size=5, lim=None):
    """QQ plot of p-values on the -log10 scale with the null diagonal, a pointwise 95 % band from the
    Beta(i, n - i + 1) distribution of order statistics, and lambda_GC in the corner. Returns lambda_GC."""
    p = np.sort(np.asarray(p, float))
    n = p.size
    i = np.arange(1, n + 1)
    e = -np.log10((i - 0.5) / n)
    o = -np.log10(p)
    if band:
        st = _scipy_stats()
        lo = -np.log10(st.beta.ppf(0.975, i, n - i + 1))
        hi = -np.log10(st.beta.ppf(0.025, i, n - i + 1))
        ax.fill_between(e, lo, hi, color=P.mix(P.surface(), P.muted(), 0.25), lw=0, zorder=1)
    top = lim or max(e.max(), o.max()) * 1.05
    ax.plot([0, e.max()], [0, e.max()], color=P.muted(), lw=0.9, zorder=2)
    ax.scatter(e, o, s=size, color=_line(token), lw=0, zorder=3)
    ax.set_xlim(0, e.max() * 1.04)
    ax.set_ylim(0, top)
    lam = lambda_gc(p)
    if show_lambda:
        ax.text(0.04, 0.95, f"$\\lambda_{{\\mathrm{{GC}}}} = {lam:.2f}$", transform=ax.transAxes, ha="left",
                va="top", fontsize=FONT["small"], color=P.ink())
    _style(ax, "expected $-\\log_{10} p$", "observed $-\\log_{10} p$")
    return lam


def ld_triangle(ax, r2, pos=None, token="negative", track=0.12, colorbar=True, labels=None, label_every=None):
    """Haploview-style LD plot: one diamond per SNP pair (i < j), shaded from the page surface (r^2 = 0)
    to the token colour (r^2 = 1), with the SNPs in order along the top. With ``pos`` (physical
    positions) a top track maps each SNP to its true position. Coordinates: SNP i sits at x = i, the
    triangle hangs below y = 0. Returns the axes."""
    r2 = np.asarray(r2, float)
    m = r2.shape[0]
    base, full = P.surface(), _line(token)
    verts, cols = [], []
    for i in range(m):
        for j in range(i + 1, m):
            cx, cy = (i + j) / 2, -(j - i) / 2
            verts.append([(cx - 0.5, cy), (cx, cy + 0.5), (cx + 0.5, cy), (cx, cy - 0.5)])
            cols.append(P.mix(base, full, float(r2[i, j])))
    pc = PolyCollection(verts, facecolors=cols, edgecolors=P.mix(base, P.muted(), 0.25), linewidths=0.2, zorder=2)
    ax.add_collection(pc)
    top = 0.5
    if pos is not None:
        pos = np.asarray(pos, float)
        h = track * m
        y0 = top + 0.3 * h
        ax.plot([-0.5, m - 0.5], [y0 + h, y0 + h], color=P.muted(), lw=1.2)
        lo, hi = pos.min(), pos.max()
        for k, xx in enumerate(pos):
            px = -0.5 + (xx - lo) / max(hi - lo, 1e-12) * m
            ax.plot([px, k], [y0 + h, y0], color=P.muted(), lw=0.45)
        top = y0 + h
    if labels is not None:
        step = label_every or 1
        for k in range(0, m, step):
            ax.text(k, 0.6, labels[k], rotation=90, ha="center", va="bottom", fontsize=FONT["tiny"], color=P.ink())
    if colorbar:
        w = max(m * 0.25, 2.0)
        x0, y0 = m - 0.5 - w, -m / 2 - 0.2
        nb = 20
        for k in range(nb):
            ax.add_patch(Rectangle((x0 + k * w / nb, y0), w / nb, 0.035 * m, facecolor=P.mix(base, full, (k + 0.5) / nb),
                                   edgecolor="none", zorder=2))
        ax.add_patch(Rectangle((x0, y0), w, 0.035 * m, facecolor="none", edgecolor=P.muted(), lw=0.5, zorder=3))
        for v, t in ((0, "0"), (0.5, "0.5"), (1, "1")):
            ax.text(x0 + v * w, y0 - 0.015 * m, t, ha="center", va="top", fontsize=FONT["tiny"], color=P.ink())
        ax.text(x0 - 0.3, y0 + 0.0175 * m, "$r^2$", ha="right", va="center", fontsize=FONT["small"], color=P.ink())
    ax.set_xlim(-1, m)
    ax.set_ylim(-m / 2 - 0.12 * m, top + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax


def lod_profile(ax, x, lod, threshold=None, markers=None, qtl=None, token="dna", support=1.5, marker_lod=None):
    """LOD profile of interval mapping: the curve, the permutation threshold (dashed), marker positions
    as a rug, the true QTL position (triangle) and the ``support``-LOD interval around the peak (shaded).
    Returns (peak position, (left, right) support interval)."""
    x = np.asarray(x, float)
    lod = np.asarray(lod, float)
    k = int(np.argmax(lod))
    peak = float(x[k])
    inside = lod >= lod[k] - support
    left = k
    while left > 0 and inside[left - 1]:
        left -= 1
    right = k
    while right < x.size - 1 and inside[right + 1]:
        right += 1
    top = max(lod.max(), threshold or 0) * 1.15 + 0.2
    ax.axvspan(x[left], x[right], color=P.mix(P.surface(), P.fill("highlight"), 0.22 if P.is_dark() else 0.45), lw=0, zorder=1)
    ax.plot(x, lod, color=_line(token), lw=1.8, zorder=3)
    if marker_lod is not None and markers is not None:
        ax.scatter(markers, marker_lod, s=14, color=P.ink(), zorder=4, lw=0)
    if threshold is not None:
        ax.axhline(threshold, color=_line("negative"), lw=1.0, ls="--", zorder=2)
    if markers is not None:
        for m in markers:
            ax.plot([m, m], [0, top * 0.04], color=P.muted(), lw=1.0, zorder=2)
    if qtl is not None:
        ax.add_patch(Polygon([(qtl - 0.012 * (x[-1] - x[0]), top * 0.97), (qtl + 0.012 * (x[-1] - x[0]), top * 0.97),
                              (qtl, top * 0.9)], closed=True, facecolor=_line("highlight"), edgecolor="none", zorder=4))
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, top)
    _style(ax, "map position / cM", "LOD")
    return peak, (float(x[left]), float(x[right]))
