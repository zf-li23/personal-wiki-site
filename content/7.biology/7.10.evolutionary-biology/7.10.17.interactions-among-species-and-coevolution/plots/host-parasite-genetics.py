"""Gene-for-gene and matching-alleles models.

A, B: infection matrices for haploid two-locus hosts (A1B1 ... A2B2) and parasites (a1b1 ... a2b2), after
Futuyma and Kirkpatrick (2017), Fig. 13.13. Gene-for-gene: infection fails if the host has A2 and the
parasite a2, or the host has B2 and the parasite b2. Matching alleles: infection only if alleles match at
both loci. C: one-locus matching-alleles recursion (Example 17.2.2), s_h = 0.3, s_p = 0.5, symmetric
mutation 1e-3 per generation in both species, start h = 0.6, q = 0.5.
"""

import numpy as np
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(34.0, 11.0)
hosts = ["A₁B₁", "A₁B₂", "A₂B₁", "A₂B₂"]
paras = ["a₁b₁", "a₁b₂", "a₂b₁", "a₂b₂"]
H = [(1, 1), (1, 2), (2, 1), (2, 2)]


def gfg(h, p):
    return not ((h[0] == 2 and p[0] == 2) or (h[1] == 2 and p[1] == 2))


def mat(h, p):
    return h == p


for j, (fn, title, x0) in enumerate(((gfg, "Gene-for-gene", 2.6), (mat, "Matching alleles", 11.4))):
    s = 1.3
    for pi in range(4):
        for hi in range(4):
            inf = fn(H[hi], H[pi])
            ax.add_patch(Rectangle((x0 + hi * s, 1.8 + (3 - pi) * s), s, s,
                                   facecolor=P.fill("virus") if inf else P.surface(), edgecolor=P.muted(), lw=0.7))
    for i in range(4):
        bio.label(ax, (x0 + (i + 0.5) * s, 1.4), hosts[i], size="tiny")
        bio.label(ax, (x0 - 0.15, 1.8 + (3.5 - i) * s), paras[i], size="tiny", ha="right")
    bio.label(ax, (x0 + 2 * s, 0.7), "host genotype", size="tiny", color=P.muted())
    bio.label(ax, (x0 - 1.7, 1.8 + 2 * s), "parasite genotype", size="tiny", color=P.muted(), rotation=90)
    bio.panel(ax, "AB"[j], (x0 - 2.4, 10.8))
    bio.label(ax, (x0, 10.4), title, size="small", bold=True, ha="left")
ax.add_patch(Rectangle((2.6, 9.0), 0.5, 0.5, facecolor=P.fill("virus"), edgecolor=P.muted(), lw=0.7))
bio.label(ax, (3.3, 9.25), "infection succeeds", size="tiny", ha="left")
sh, sp, mu = 0.3, 0.5, 1e-3
h, q = 0.6, 0.5
hs, qs = [], []
for _ in range(400):
    hs.append(h)
    qs.append(q)
    wh1, wh2 = 1 - sh * q, 1 - sh * (1 - q)
    wp1, wp2 = 1 - sp * (1 - h), 1 - sp * h
    h, q = h * wh1 / (h * wh1 + (1 - h) * wh2), q * wp1 / (q * wp1 + (1 - q) * wp2)
    h, q = h * (1 - mu) + (1 - h) * mu, q * (1 - mu) + (1 - q) * mu
pc = C.axes_at(ax, (21.6, 1.8, 11.4, 7.4))
g = np.arange(400)
pc.plot(g, hs, color=C.line("dna"), lw=1.7, label="host allele H₁, h")
pc.plot(g, qs, color=C.line("virus"), lw=1.7, ls=(0, (4, 2)), label="parasite allele P₁, q")
pc.set_xlim(0, 400)
pc.set_ylim(0, 1.18)
pc.set_yticks([0, 0.25, 0.5, 0.75, 1])
C.style_axes(pc, "generation", "allele frequency")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center", ncol=2)
bio.panel(ax, "C", (20.0, 10.8))
bio.label(ax, (21.6, 10.4), "Matching-alleles cycles", size="small", bold=True, ha="left")
