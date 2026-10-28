"""Transmission genetics: crossovers among four chromatids, three-point crosses, linkage maps, asci
and tetrads, circular Hfr maps; and the standard quantitative models of the chapters on mapping.

    from wikibio import transmission as T

    T.chromatid_bar(ax, 1, 7, 3, [(0, 0.5, "dna"), (0.5, 1, "receptor")], loci=[(0.2, "a"), (0.8, "b+")])
    prod = T.four_chromatids(ax, 1, 7, 5, crossovers=[(0.5, 1, 2)], loci=[(0.2, ("A", "a")), (0.8, ("B", "b"))])
    T.chromatid_set(ax, 9, 14, 5, prod)                      # the four products of that meiosis
    T.three_point(ax, (1, 9), parents=(("v", "cv", "ct+"), ("v+", "cv+", "ct")), loci=[...], classes=[...])
    T.linkage_map(ax, 3, 9, [("y", 0.0), ("w", 1.0), ("v", 30.7)], scale=0.12, name="X")
    T.link_maps(ax, left_anchors, right_anchors)            # connect the same genes on two maps
    T.ascus(ax, (5, 4), ["dna", "dna", "receptor", ...])     # 8 spores in a linear (ordered) ascus
    T.tetrad(ax, (8, 4), ["AB", "AB", "ab", "ab"])           # unordered tetrad (yeast), genotypes in spores
    T.hfr_map(ax, (5, 5), 3, markers=[(0, "thr"), ...], hfrs=[(10, -1, "HfrH"), ...])

Allele text: a trailing ``+`` is written as a superscript (``"v+"`` -> v⁺), always italic.

Models (numpy; distances ``d`` in morgans unless noted):
``haldane(d)``, ``haldane_inv(r)``, ``kosambi(d)``, ``kosambi_inv(r)``; ``tetrad_freqs(d)`` returns
(PD, NPD, T) without interference; ``mii_freq(d)`` the second-division segregation frequency;
``chiasma_process(n, L, nu, rng)`` crossover positions on a chromosome of ``L`` morgans under the
chi-square (gamma renewal) model of interference (``nu = 1``: no interference, Poisson);
``interrupted_mating(t, entry, ...)`` and ``wu_cotransduction(d, L)``.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

from . import palette as P
from .core import LINE, arrow, label

# ---------------------------------------------------------------------------------------------
# text


def allele(text):
    """Italic mathtext for an allele or haplotype; a trailing '+' (or a lone '+') becomes a superscript."""
    if not text or "$" in text:
        return text
    parts = []
    for tok in text.split(" "):
        if tok == "+":
            parts.append(r"+")
        elif tok.endswith("+"):
            parts.append(r"\mathit{" + tok[:-1] + r"}^{+}")
        elif "^" in tok:
            base, sup = tok.split("^", 1)
            parts.append(r"\mathit{" + base + r"}^{\mathit{" + sup + "}}")
        else:
            parts.append(r"\mathit{" + tok + "}")
    return "$" + r"\ ".join(parts) + "$"


# ---------------------------------------------------------------------------------------------
# chromatids drawn as horizontal bars (centromere on the left unless placed elsewhere)


def chromatid_bar(ax, x0, x1, y, segments, height=0.26, loci=(), centromere=None, label_pos="above",
                  label_size="small", zorder=8):
    """One chromatid as a rounded horizontal bar from ``x0`` to ``x1`` at height ``y``.

    ``segments`` [(f0, f1, token)] colour it (f = fraction of the length from the left end, e.g. the
    parts inherited from each parent after crossing over). ``loci`` [(f, text)] draw a locus stripe
    and an italic allele label above (``label_pos="above"``), below, or none (``None``).
    ``centromere`` f draws a centromere (small dark oval). Returns {text: (x, y)} of the loci.
    """
    w = x1 - x0
    h = height
    box = FancyBboxPatch((x0, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h / 2}",
                         transform=ax.transData)
    for f0, f1, tok in segments:
        r = Rectangle((x0 + f0 * w, y - h), (f1 - f0) * w, 2 * h, facecolor=P.fill(tok), edgecolor="none",
                      zorder=zorder)
        ax.add_patch(r)
        r.set_clip_path(box)
        o = FancyBboxPatch((x0, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h / 2}", fill=False,
                           edgecolor=P.edge(tok), lw=LINE * 0.75, zorder=zorder + 0.2)
        ax.add_patch(o)
        clip = Rectangle((x0 + f0 * w - (0.02 if f0 <= 0 else 0), y - h), (f1 - f0) * w + (0.04 if f1 >= 1 else 0), 2 * h,
                         transform=ax.transData)
        o.set_clip_path(clip)
    out = {}
    for f, text in loci:
        x = x0 + f * w
        ax.plot([x, x], [y - h / 2, y + h / 2], color=P.edge("highlight"), lw=1.6, zorder=zorder + 0.3,
                solid_capstyle="butt")
        if label_pos == "above":
            label(ax, (x, y + h / 2 + 0.05), allele(text), size=label_size, va="bottom")
        elif label_pos == "below":
            label(ax, (x, y - h / 2 - 0.05), allele(text), size=label_size, va="top")
        out[text] = (x, y)
    if centromere is not None:
        cx = x0 + centromere * w
        ax.add_patch(Ellipse((cx, y), h * 1.15, h * 1.25, facecolor=P.edge("neutral"), edgecolor=P.ink(),
                             lw=0.6, zorder=zorder + 0.4))
    return out


def crossover_products(crossovers, tokens=("dna", "receptor")):
    """Colour segments of the four chromatids after the given crossovers.

    Chromatids 0 and 1 are the sisters of the first homologue (``tokens[0]``), 2 and 3 of the second.
    ``crossovers`` [(f, i, j)]: an exchange at fraction f between chromatids i and j; the parts to the
    right of f are swapped. Returns a list of four segment lists [(f0, f1, token)].
    """
    segs = [[(0.0, 1.0, tokens[0])], [(0.0, 1.0, tokens[0])], [(0.0, 1.0, tokens[1])], [(0.0, 1.0, tokens[1])]]

    def split(seg, f):
        left, right = [], []
        for a, b, t in seg:
            if b <= f:
                left.append((a, b, t))
            elif a >= f:
                right.append((a, b, t))
            else:
                left.append((a, f, t))
                right.append((f, b, t))
        return left, right

    for f, i, j in sorted(crossovers):
        li, ri = split(segs[i], f)
        lj, rj = split(segs[j], f)
        segs[i], segs[j] = li + rj, lj + ri
    # merge neighbouring segments of the same colour
    out = []
    for seg in segs:
        m = []
        for a, b, t in seg:
            if m and m[-1][2] == t and abs(m[-1][1] - a) < 1e-9:
                m[-1] = (m[-1][0], b, t)
            else:
                m.append((a, b, t))
        out.append(m)
    return out


def _token_at(seg, f):
    for a, b, t in seg:
        if a - 1e-9 <= f <= b + 1e-9:
            return t
    return seg[-1][2]


def four_chromatids(ax, x0, x1, y, crossovers=(), loci=(), tokens=("dna", "receptor"), spacing=0.36, height=0.22,
                    centromere=0.04, label_alleles=True, numbers=False, zorder=8):
    """A bivalent drawn as four horizontal chromatids (top two: sisters of homologue 1; bottom two:
    homologue 2), centromere near the left end, with each crossover ``(f, i, j)`` marked by an X
    joining chromatids i and j at fraction f. ``loci`` [(f, (allele1, allele2))].

    Returns a dict: ``segments`` (the four products, see ``crossover_products``), ``genotypes`` (the
    alleles each product carries at the loci) and ``ys`` (the four rows)."""
    ys = [y + 1.5 * spacing, y + 0.5 * spacing, y - 0.5 * spacing, y - 1.5 * spacing]
    w = x1 - x0
    for k, yy in enumerate(ys):
        tok = tokens[0] if k < 2 else tokens[1]
        pos = "above" if k == 0 else ("below" if k == 3 else None)
        al = [(f, a[0] if k < 2 else a[1]) for f, a in loci] if label_alleles else []
        if not label_alleles:
            al = [(f, "") for f, _ in loci]
        chromatid_bar(ax, x0, x1, yy, [(0, 1, tok)], height=height, loci=al, label_pos=pos, zorder=zorder)
        if numbers:
            label(ax, (x0 - 0.25, yy), str(k + 1), size="tiny", color=P.muted(), ha="right")
    for top in (0, 2):  # sister chromatids joined at the centromere
        cx = x0 + centromere * w
        ax.add_patch(Ellipse((cx, (ys[top] + ys[top + 1]) / 2), height * 1.2, spacing + height * 1.1,
                             facecolor=P.edge("neutral"), edgecolor=P.ink(), lw=0.6, zorder=zorder + 0.5))
    for f, i, j in crossovers:
        x = x0 + f * w
        dx = 0.16
        for (xa, ya), (xb, yb) in (((x - dx, ys[i]), (x + dx, ys[j])), ((x - dx, ys[j]), (x + dx, ys[i]))):
            ax.plot([xa, xb], [ya, yb], color=P.surface(), lw=3.6, zorder=zorder + 0.6, solid_capstyle="round")
            ax.plot([xa, xb], [ya, yb], color=P.ink(), lw=1.4, zorder=zorder + 0.7, solid_capstyle="round")
    segs = crossover_products(crossovers, tokens)
    geno = []
    for seg in segs:
        g = []
        for f, a in loci:
            g.append(a[0] if _token_at(seg, f) == tokens[0] else a[1])
        geno.append(tuple(g))
    return {"segments": segs, "genotypes": geno, "ys": ys}


def chromatid_set(ax, x0, x1, y, products, loci_f=None, spacing=0.36, height=0.22, tags=None, tag_x=None,
                  genotype_x=None, centromere=0.04, zorder=8):
    """Draw the four products returned by ``four_chromatids`` as separate chromatids (rows like the
    input), each with its genotype written to the right (``genotype_x``) and an optional tag
    (e.g. "P" / "R"). ``loci_f``: the locus fractions (stripes)."""
    ys = [y + 1.5 * spacing, y + 0.5 * spacing, y - 0.5 * spacing, y - 1.5 * spacing]
    segs, geno = products["segments"], products["genotypes"]
    gx = genotype_x if genotype_x is not None else x1 + 0.25
    for k, yy in enumerate(ys):
        chromatid_bar(ax, x0, x1, yy, segs[k], height=height, loci=[(f, "") for f in (loci_f or [])], label_pos=None,
                      centromere=centromere, zorder=zorder)
        label(ax, (gx, yy), allele(" ".join(geno[k])), size="small", ha="left")
        if tags:
            label(ax, (tag_x if tag_x is not None else gx + 1.3, yy), tags[k], size="tiny", ha="left",
                  color=P.ink() if tags[k].startswith("R") or tags[k].startswith("N") or tags[k].startswith("T") else P.muted())
    return ys


# ---------------------------------------------------------------------------------------------
# three-point testcross


def _origins(hap, parents):
    return [0 if a == parents[0][k] else 1 for k, a in enumerate(hap)]


def classify(hap, parents):
    """Class of a gamete haplotype from a triple heterozygote with parental haplotypes ``parents``
    (loci in map order): 'P' (parental), 'SCO 1', 'SCO 2' (single crossover in interval 1 or 2) or 'DCO'."""
    o = _origins(hap, parents)
    s1, s2 = o[0] != o[1], o[1] != o[2]
    return "P" if not (s1 or s2) else "DCO" if (s1 and s2) else "SCO 1" if s1 else "SCO 2"


def three_point(ax, origin, parents, loci, classes, tokens=("dna", "receptor"), width=4.2, row=0.62, height=0.24,
                count_x=None, type_x=None, header=True, zorder=8):
    """The eight gamete classes of a three-point testcross as chromatids, in rows from ``origin``
    (top-left). ``parents``: the two parental haplotypes of the F1 (allele tuples in map order);
    ``loci``: the three locus fractions; ``classes`` [(haplotype, count)]. Each chromatid is coloured
    by parental origin (the colour changes in the interval where a crossover occurred), followed by
    its count and class. Returns [(haplotype, count, class)]."""
    x0, y0 = origin
    cx = count_x if count_x is not None else x0 + width + 2.3
    tx = type_x if type_x is not None else cx + 0.9
    out = []
    if header:
        label(ax, (x0 + width / 2, y0 + 0.45), "Gamete from F1 (chromatid)", size="small", color=P.muted())
        label(ax, (cx, y0 + 0.45), "Number", size="small", color=P.muted(), ha="right")
        label(ax, (tx, y0 + 0.45), "Class", size="small", color=P.muted(), ha="left")
    for k, (hap, n) in enumerate(classes):
        y = y0 - k * row
        o = _origins(hap, parents)
        segs, start = [], 0.0
        for m in range(1, 3):
            if o[m] != o[m - 1]:
                cut = (loci[m - 1] + loci[m]) / 2
                segs.append((start, cut, tokens[o[m - 1]]))
                start = cut
        segs.append((start, 1.0, tokens[o[2]]))
        chromatid_bar(ax, x0, x0 + width, y, segs, height=height, loci=[(f, "") for f in loci], label_pos=None,
                      zorder=zorder)
        for f, a in zip(loci, hap):
            label(ax, (x0 + f * width, y + height / 2 + 0.04), allele(a), size="tiny", va="bottom")
        c = classify(hap, parents)
        label(ax, (cx, y), f"{n}", size="small", ha="right")
        names = {"P": "parental", "SCO 1": "single crossover, interval 1", "SCO 2": "single crossover, interval 2",
                 "DCO": "double crossover"}
        label(ax, (tx, y), names[c], size="tiny", ha="left", color=P.muted() if c == "P" else P.ink())
        out.append((hap, n, c))
    return out


# ---------------------------------------------------------------------------------------------
# linkage maps


def linkage_map(ax, x, y_top, loci, scale=0.1, width=0.32, token="chromatin", name=None, side="right",
                positions=True, length=None, unit="", size="small", zorder=8):
    """A vertical linkage map: a bar with a tick for each locus at ``y_top - position * scale``.

    ``loci`` [(gene, position in cM)]; gene names in italic on ``side``, positions (with ``unit``)
    on the other side. ``length`` (cM) sets the bar length (default: last locus). Returns
    {gene: (x of the bar edge on the gene side, y)} for ``link_maps``."""
    L = length if length is not None else max(p for _, p in loci)
    y_bot = y_top - L * scale
    ax.add_patch(FancyBboxPatch((x - width / 2, y_bot - 0.1), width, y_top - y_bot + 0.2,
                                boxstyle=f"round,pad=0,rounding_size={width / 2}", facecolor=P.fill(token),
                                edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder))
    if name:
        label(ax, (x, y_top + 0.45), name, size=size, bold=True)
    sg = 1 if side == "right" else -1
    ys = [y_top - p * scale for _, p in loci]
    # spread labels that would overlap (minimum gap 0.32 units)
    lab = list(ys)
    for _ in range(50):
        moved = False
        for k in range(1, len(lab)):
            if lab[k - 1] - lab[k] < 0.32:
                mid = (lab[k - 1] + lab[k]) / 2
                lab[k - 1], lab[k] = mid + 0.16, mid - 0.16
                moved = True
        if not moved:
            break
    out = {}
    for (g, p), yy, yl in zip(loci, ys, lab):
        ax.plot([x - width / 2, x + width / 2], [yy, yy], color=P.ink(), lw=1.1, zorder=zorder + 0.2)
        xe = x + sg * width / 2
        ax.plot([xe, xe + sg * 0.25, xe + sg * 0.45], [yy, yl, yl], color=P.muted(), lw=0.6, zorder=zorder)
        label(ax, (xe + sg * 0.5, yl), allele(g), size=size, ha="left" if sg > 0 else "right")
        if positions:
            xo = x - sg * width / 2
            ax.plot([xo, xo - sg * 0.25, xo - sg * 0.45], [yy, yl, yl], color=P.muted(), lw=0.6, zorder=zorder)
            label(ax, (xo - sg * 0.5, yl), f"{p:g}{unit}", size="tiny", ha="right" if sg > 0 else "left",
                  color=P.muted())
        out[g] = (xe, yy)
    return out


def link_maps(ax, left, right, color=None, dashed=True):
    """Connect the same genes on two maps (dicts returned by ``linkage_map``; the left map should be
    labelled on its right side and the right map on its left side or without names)."""
    for g, (xa, ya) in left.items():
        if g in right:
            xb, yb = right[g]
            ax.plot([xa + 0.95, xb - 0.95], [ya, yb], color=color or P.muted(), lw=0.8,
                    ls=(0, (2.5, 2)) if dashed else "-", zorder=5)


# ---------------------------------------------------------------------------------------------
# asci and tetrads


def ascus(ax, xy, spores, angle=90.0, spore=0.34, gap=0.04, wall="neutral", labels=None, zorder=8):
    """A linear (ordered) ascus with spores in a row, e.g. eight ascospores of *Neurospora*.
    ``spores``: a token per spore (colour = genotype, e.g. "ink" for black and "bone" for white
    spores); ``angle`` 90 draws it upright. ``labels``: optional text per spore beside it.
    Returns the spore centres (top first for an upright ascus)."""
    n = len(spores)
    a = math.radians(angle)
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    c = np.asarray(xy, float)
    step = spore * 1.25 + gap
    Ltot = n * step + 0.25
    t = np.linspace(0, 2 * np.pi, 120)
    outline = c + np.outer(Ltot / 2 * np.cos(t), u) + np.outer(spore * 0.95 * np.sin(t), v)
    ax.add_patch(Polygon(outline, closed=True, facecolor=P.fill(wall) if not P.is_dark() else P.mix(P.fill(wall), P.surface(), 0.7),
                         edgecolor=P.edge(wall), lw=LINE * 0.8, zorder=zorder))
    centres = []
    for k, tok in enumerate(spores):
        p = c + u * ((n - 1) / 2 - k) * step
        if tok == "ink":
            fc, ec = ("#1f2937", "#111827") if not P.is_dark() else ("#0b1020", "#cbd5e1")
        else:
            fc, ec = P.fill(tok), P.edge(tok)
        ax.add_patch(Ellipse(p, spore * 1.25, spore * 0.95, angle=angle, facecolor=fc, edgecolor=ec, lw=0.8,
                             zorder=zorder + 0.2))
        centres.append(tuple(p))
        if labels:
            label(ax, p + v * -(spore * 0.95 + 0.12), allele(labels[k]), size="tiny", ha="right")
    return centres


def tetrad(ax, xy, genotypes, tokens=None, r=0.36, spread=0.46, wall="neutral", size="tiny", zorder=8):
    """An unordered tetrad (e.g. a yeast ascus): four round spores in a diamond, each with its
    genotype written inside. ``tokens``: optional colour per spore (default neutral)."""
    c = np.asarray(xy, float)
    t = np.linspace(0, 2 * np.pi, 120)
    R = spread + r + 0.12
    ax.add_patch(Polygon(np.c_[c[0] + R * np.cos(t), c[1] + R * np.sin(t)], closed=True,
                         facecolor=P.fill(wall) if not P.is_dark() else P.mix(P.fill(wall), P.surface(), 0.7),
                         edgecolor=P.edge(wall), lw=LINE * 0.8, zorder=zorder))
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    out = []
    for k, (g, (px, py)) in enumerate(zip(genotypes, pos)):
        p = c + spread * np.array([px, py])
        tok = (tokens or ["bone"] * 4)[k]
        ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=zorder + 0.2))
        label(ax, p, allele(g), size=size, color=P.on_fill(), zorder=zorder + 0.5)
        out.append(tuple(p))
    return out


# ---------------------------------------------------------------------------------------------
# circular Hfr map


def hfr_map(ax, center, radius, markers=(), hfrs=(), total=100.0, ticks=10, token="dna", size="small",
            hfr_radius=None, zorder=8):
    """A circular bacterial chromosome with minute coordinates (0 at the top, clockwise).

    ``markers`` [(minute, gene)] are written outside in italic; ``hfrs`` [(minute, direction, name)]
    draw the integrated F (origin of transfer) inside the circle with an arrow in the direction of
    transfer (+1 clockwise, -1 anticlockwise), i.e. the order in which genes enter a recipient.
    Returns {gene: angle}."""
    cx, cy = center
    R = radius

    def ang(m):
        return math.pi / 2 - 2 * math.pi * m / total

    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(cx + R * np.cos(t), cy + R * np.sin(t), color=P.edge(token), lw=LINE * 2.6, zorder=zorder,
            solid_capstyle="round")
    ax.plot(cx + R * np.cos(t), cy + R * np.sin(t), color=P.fill(token), lw=LINE * 1.4, zorder=zorder + 0.1)
    if ticks:
        for m in np.arange(0, total, ticks):
            a = ang(m)
            ax.plot([cx + (R - 0.12) * math.cos(a), cx + (R + 0.12) * math.cos(a)],
                    [cy + (R - 0.12) * math.sin(a), cy + (R + 0.12) * math.sin(a)], color=P.muted(), lw=0.8,
                    zorder=zorder + 0.2)
            label(ax, (cx + (R - 0.42) * math.cos(a), cy + (R - 0.42) * math.sin(a)), f"{m:g}", size="tiny",
                  color=P.muted())
    out = {}
    for m, g in markers:
        a = ang(m)
        ax.add_patch(Circle((cx + R * math.cos(a), cy + R * math.sin(a)), 0.09, facecolor=P.ink(), edgecolor="none",
                            zorder=zorder + 0.4))
        lr = R + 0.38
        ha = "left" if math.cos(a) > 0.2 else "right" if math.cos(a) < -0.2 else "center"
        label(ax, (cx + lr * math.cos(a), cy + lr * math.sin(a)), allele(g), size=size, ha=ha)
        out[g] = a
    hr = hfr_radius if hfr_radius is not None else R * 0.55
    for k, (m, direction, name) in enumerate(hfrs):
        a = ang(m)
        p = np.array([cx + R * math.cos(a), cy + R * math.sin(a)])
        q = np.array([cx + hr * math.cos(a), cy + hr * math.sin(a)])
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("highlight"), lw=1.0, zorder=zorder - 0.1)
        # arc arrow inside, in the direction of transfer
        span = 0.32 * direction
        arc = np.linspace(a, a - span, 30)
        rr = R - 0.25
        pts = np.c_[cx + rr * np.cos(arc), cy + rr * np.sin(arc)]
        ax.plot(pts[:-3, 0], pts[:-3, 1], color=P.edge("highlight"), lw=1.8, zorder=zorder + 0.3)
        arrow(ax, pts[-4], pts[-1], kind="process", color=P.edge("highlight"), lw=1.8, head=0.2, zorder=zorder + 0.3)
        ax.add_patch(Circle(p, 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9,
                            zorder=zorder + 0.5))
        label(ax, (q[0], q[1]), name, size="tiny")
    return out


# ---------------------------------------------------------------------------------------------
# models


def haldane(d):
    """Haldane mapping function: recombination frequency for map distance d (morgans), no interference."""
    return 0.5 * (1 - np.exp(-2 * np.asarray(d, float)))


def haldane_inv(r):
    """Inverse Haldane function: map distance (morgans) from recombination frequency r < 1/2."""
    return -0.5 * np.log(1 - 2 * np.asarray(r, float))


def kosambi(d):
    """Kosambi mapping function r = tanh(2d) / 2 (d in morgans)."""
    return 0.5 * np.tanh(2 * np.asarray(d, float))


def kosambi_inv(r):
    """Inverse Kosambi function d = ln[(1 + 2r)/(1 - 2r)] / 4."""
    r = np.asarray(r, float)
    return 0.25 * np.log((1 + 2 * r) / (1 - 2 * r))


def tetrad_freqs(d):
    """(PD, NPD, T) frequencies of unordered tetrads for two loci d morgans apart, with crossovers a
    Poisson process (no chiasma interference) and random chromatid involvement."""
    d = np.asarray(d, float)
    t = 2 / 3 * (1 - np.exp(-3 * d))
    npd = (1 - 3 * np.exp(-2 * d) + 2 * np.exp(-3 * d)) / 6
    return 1 - t - npd, npd, t


def mii_freq(d):
    """Frequency of second-division segregation for a locus d morgans from its centromere (no interference)."""
    return 2 / 3 * (1 - np.exp(-3 * np.asarray(d, float)))


def chiasma_process(n, L, nu=1, rng=None):
    """Crossover positions on a bivalent of genetic length ``L`` morgans in ``n`` meioses under the
    chi-square model (Zhao, Speed and McPeek 1995): chiasmata are every ``nu``-th point of a Poisson
    process of rate 2*nu per morgan started in equilibrium (``nu = 1`` is the no-interference Poisson
    model). Returns a list of arrays of positions (bivalent level: mean 2L per meiosis)."""
    rng = rng or np.random.default_rng(0)
    out = []
    for _ in range(n):
        start = rng.integers(nu)  # stationary phase of the renewal process
        pts = []
        x, k = 0.0, 0
        while True:
            x += rng.exponential(1 / (2 * nu))
            if x > L:
                break
            if k % nu == start:
                pts.append(x)
            k += 1
        out.append(np.array(pts))
    return out


def chromatid_recombinant(chiasmata, a, b, rng):
    """For each meiosis (chiasma positions), whether a random chromatid is recombinant between
    positions a < b (no chromatid interference: each chiasma involves the chromatid with prob 1/2)."""
    res = []
    for ch in chiasmata:
        k = int(np.sum((ch > a) & (ch < b)))
        involved = rng.binomial(k, 0.5) if k else 0
        res.append(involved % 2 == 1)
    return np.array(res)


def interrupted_mating(t, entry, plateau=1.0, lam=0.0, rise=4.0):
    """Recombinant frequency of a donor marker at time t (min) in an Hfr x F- cross: zero before the
    marker's entry time, then rising (over about ``rise`` minutes, the spread of mating start times)
    to a plateau ``plateau * exp(-lam * entry)`` that falls with entry time because mating pairs
    break at rate ``lam`` per minute."""
    t = np.asarray(t, float)
    top = plateau * math.exp(-lam * entry)
    x = np.clip((t - entry) / rise, 0, None)
    return top * (1 - np.exp(-x))


def wu_cotransduction(d, L=2.0):
    """Wu (1966) cotransduction frequency of two markers d minutes apart for a transducing fragment
    of length L minutes (random fragment ends, both markers must be inside): (1 - d/L)^3."""
    d = np.asarray(d, float)
    return np.where(d < L, (1 - d / L) ** 3, 0.0)
