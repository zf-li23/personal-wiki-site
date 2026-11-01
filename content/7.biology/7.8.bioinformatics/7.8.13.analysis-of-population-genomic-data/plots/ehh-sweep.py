# Extended haplotype homozygosity around a recent sweep (simulated). 401 SNPs every 5 kb cover 1 Mb on each side
# of a core SNP. Background haplotypes are mosaics of 40 ancestral haplotypes (switch probability 0.05 per
# SNP interval, so linkage disequilibrium decays over about 100 kb). The 100 haplotypes carrying the derived
# core allele descend from one haplotype that rose to frequency 0.5 in t = 300 generations: on each side,
# each keeps that haplotype up to a recombination point at an exponential distance with mean 1/(t r) = 333 kb
# (r = 1e-8 per bp per generation) and continues as a background haplotype beyond it. The 100 ancestral-allele
# haplotypes are background haplotypes. A: EHH against distance for the two core alleles; the areas under the
# curves (integrated EHH, down to EHH = 0.05) give the unstandardized iHS = ln(iHH_A / iHH_D). B: the
# haplotypes, sorted by core allele and by the extent of the sweep haplotype; dark cells differ from the
# haplotype that swept, so the white block around the core is the shared sweep haplotype.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
pos = np.arange(-200, 201) * 5.0                       # kb
m, nf = pos.size, 40
fp = rng.uniform(0.05, 0.95, m)
found = (rng.random((nf, m)) < fp).astype(np.int8)


def background(n):
    h = np.empty((n, m), np.int8)
    for i in range(n):
        src = rng.integers(nf)
        for j in range(m):
            if rng.random() < 0.05:
                src = rng.integers(nf)
            h[i, j] = found[src, j]
    return h


sweep = background(1)[0]
nD = nA = 100
anc = background(nA)
der = background(nD)
mean_kb = 1 / (300 * 1e-8) / 1000
ext = np.zeros((nD, 2))
for i in range(nD):
    left, right = rng.exponential(mean_kb, 2)
    keep = (pos >= -left) & (pos <= right)
    der[i, keep] = sweep[keep]
    ext[i] = left, right
core = m // 2
der[:, core], anc[:, core] = 1, 0                      # the core SNP itself: derived 1, ancestral 0
sweep[core] = 1


def ehh(h):
    out = np.empty(m)
    n = len(h)
    for j in range(m):
        lo, hi = (j, core) if j <= core else (core, j)
        seg = h[:, lo:hi + 1]
        _, counts = np.unique(seg, axis=0, return_counts=True)
        out[j] = np.sum(counts * (counts - 1)) / (n * (n - 1))
    return out


eD, eA = ehh(der), ehh(anc)


def ihh(e):
    tot = 0.0
    for side in (slice(core, None), slice(core, None, -1)):
        x, y = np.abs(pos[side]), e[side]
        stop = np.argmax(y < 0.05) if np.any(y < 0.05) else len(y)
        tot += np.trapezoid(y[:stop + 1], x[:stop + 1])
    return tot


iD, iA = ihh(eD), ihh(eA)
ihs = np.log(iA / iD)

fig, ax = bio.canvas(30.0, 10.4)
a = C.axes_at(ax, (2.0, 1.6, 12.6, 7.8))
a.plot(pos, eD, color=C.line("negative"), lw=1.6, label="derived core allele")
a.plot(pos, eA, color=C.line("dna"), lw=1.6, label="ancestral core allele")
a.axhline(0.05, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.set_xlim(-1000, 1000)
a.set_ylim(0, 1.03)
a.text(-980, 0.62, f"iHH_D = {iD:.0f} kb\niHH_A = {iA:.0f} kb\nunstandardized iHS = {ihs:.2f}",
       fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(a, "distance from core SNP (kb)", "EHH")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
b = C.axes_at(ax, (18.0, 1.6, 11.4, 7.8))
o = np.argsort(ext.sum(1))[::-1]
hap = np.r_[der[o], anc] ^ sweep
b.imshow(hap, aspect="auto", cmap="Greys", vmin=0, vmax=1.6, interpolation="nearest",
         extent=(pos[0] - 2.5, pos[-1] + 2.5, nD + nA - 0.5, -0.5))
b.axhline(nD - 0.5, color=C.line("negative"), lw=1.2)
b.axvline(0, color=C.line("negative"), lw=0.8)
b.set_yticks([nD / 2, nD + nA / 2])
b.set_yticklabels(["derived", "ancestral"])
C.style_axes(b, "position (kb)", None, box=True)
bio.panel(ax, "A", (0.2, 10.0))
bio.panel(ax, "B", (16.2, 10.0))
