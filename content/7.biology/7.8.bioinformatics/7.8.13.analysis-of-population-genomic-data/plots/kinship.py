# Relationship inference from genotypes (simulated). Pairs of individuals are typed at 20 000 independent SNPs
# (allele frequencies uniform on 0.05-0.5); at each SNP the pair shares 0, 1 or 2 alleles identical by descent
# with the probabilities (k0, k1, k2) of its relationship. For each pair we compute the KING-robust kinship
# estimate (N_het,het - 2 N_IBS0) / (N_het(i) + N_het(j)) and the fraction of SNPs at which the two are
# opposite homozygotes (IBS0). Dashed lines: the KING thresholds 2^(-3/2), 2^(-5/2), 2^(-7/2), 2^(-9/2) that
# separate duplicates, first-, second- and third-degree relatives and unrelated pairs. Parent-offspring and
# full-sib pairs have the same kinship (1/4) but differ in IBS0 (k0 = 0 against 1/4). Real chromosomes share
# IBD in long segments, which spreads each cloud more than here.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
m = 20000
p = rng.uniform(0.05, 0.5, m)
rels = [("unrelated", (1, 0, 0), 300, "neutral"), ("third degree (first cousins)", (0.75, 0.25, 0), 40, "plant"),
        ("second degree (half-sibs)", (0.5, 0.5, 0), 40, "enzyme"), ("full sibs", (0.25, 0.5, 0.25), 40, "protein"),
        ("parent-offspring", (0, 1, 0), 40, "dna"), ("duplicate / MZ twins", (0, 0, 1), 12, "negative")]


def pair(k):
    state = rng.choice(3, m, p=k)
    a = rng.random((4, m)) < p                       # allele = True for the A allele
    x1, x2, y1, y2 = a
    y1 = np.where(state >= 1, x1, y1)                # one allele shared IBD
    y2 = np.where(state == 2, x2, y2)                # both shared
    gx, gy = x1.astype(int) + x2, y1.astype(int) + y2
    hx, hy = gx == 1, gy == 1
    hethet = np.sum(hx & hy)
    ibs0 = np.sum(np.abs(gx - gy) == 2)
    return (hethet - 2 * ibs0) / (hx.sum() + hy.sum()), ibs0 / m


fig, ax = bio.canvas(20.0, 11.0)
a = C.axes_at(ax, (2.4, 1.6, 12.2, 8.8))
for name, k, num, tok in rels:
    v = np.array([pair(k) for _ in range(num)])
    a.scatter(v[:, 1], v[:, 0], s=10, color=C.line(tok), lw=0, alpha=0.85, label=name)
for e in (1.5, 2.5, 3.5, 4.5):
    a.axhline(2 ** -e, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.set_xlim(-0.002, 0.082)
a.set_ylim(-0.06, 0.56)
C.style_axes(a, "fraction of SNPs with IBS0 (opposite homozygotes)", "KING-robust kinship")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center left",
         bbox_to_anchor=(1.02, 0.5), markerscale=1.6)
bio.label(ax, (17.4, 3.2), "dashed: 0.354, 0.177,\n0.088, 0.044", size="tiny")
