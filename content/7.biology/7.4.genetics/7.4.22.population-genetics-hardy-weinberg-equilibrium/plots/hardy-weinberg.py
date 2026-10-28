"""Hardy-Weinberg proportions. A: genotype frequencies p^2, 2pq and q^2 as functions of the allele
frequency q; the heterozygote frequency peaks at 1/2 when p = q = 1/2, and a rare allele is carried
almost entirely by heterozygotes. B: De Finetti diagram. Every population is a point in the triangle whose
distances from the sides are its three genotype frequencies; the parabola H = 2pq contains the populations in
Hardy-Weinberg proportions. Points: the MN sample of Example 22.2.2 (on the curve), the same allele
frequency with inbreeding F = 0.3 and F = 0.7 (below the curve, toward the base), a population of
self-fertilizing plants (near the base) and the pooled sample of two subpopulations with p = 0.2 and 0.8
(Wahlund effect)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3), gridspec_kw={"width_ratios": [1, 1.15]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.9, wspace=0.18)
a = axs[0]
q = np.linspace(0, 1, 300)
p = 1 - q
for y, lab, tok in ((p**2, "$AA$: $p^2$", "dna"), (2 * p * q, "$Aa$: $2pq$", "enzyme"), (q**2, "$aa$: $q^2$", "rna")):
    a.plot(q, y, color=charts.line(tok), lw=2, label=lab)
a.set_xlim(0, 1)
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(a, "allele frequency $q$ of $a$", "genotype frequency")
charts.title(a, "A  Genotype frequencies at equilibrium")

b = axs[1]
s3 = np.sqrt(3) / 2


def xy(PAA, H, Qaa):
    return Qaa + H / 2, H * s3


tri = np.array([(0, 0), (1, 0), (0.5, s3), (0, 0)])
b.plot(tri[:, 0], tri[:, 1], color=P.muted(), lw=1)
for f in (0.2, 0.4, 0.6, 0.8):
    b.plot([f / 2, 1 - f / 2], [f * s3, f * s3], color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5)
    b.text(1 - f / 2 + 0.02, f * s3, f"{f:g}", fontsize=FT["tiny"], color=P.muted(), va="center")
hx, hy = xy(p**2, 2 * p * q, q**2)
b.plot(hx, hy, color=charts.line("enzyme"), lw=2)
b.text(0.84, 0.33, "$H = 2pq$", ha="left", fontsize=FT["small"], color=charts.line("enzyme"))
pm = 0.5425
pts = [((pm**2, 2 * pm * (1 - pm), (1 - pm) ** 2), "MN sample", "dna")]
for F in (0.3, 0.7):
    H = 2 * pm * (1 - pm) * (1 - F)
    pts.append(((pm**2 + F * pm * (1 - pm), H, (1 - pm) ** 2 + F * pm * (1 - pm)), f"$F = {F}$", "negative"))
pts.append(((0.62, 0.04, 0.34), "selfing", "protein"))
pts.append(((0.5 * 0.04 + 0.5 * 0.64, 0.32, 0.5 * 0.64 + 0.5 * 0.04), "pooled subpopulations", "highlight"))
for (fr, lab, tok) in pts:
    X, Y = xy(*fr)
    b.scatter([X], [Y], s=34, color=charts.line(tok), zorder=4)
    dy = -0.055 if lab.startswith("pooled") else 0.02
    b.text(X + 0.025, Y + dy, lab, fontsize=FT["tiny"], color=P.ink())
b.text(-0.02, -0.05, "$AA$", ha="center", va="top", fontsize=FT["small"], color=P.ink())
b.text(1.02, -0.05, "$aa$", ha="center", va="top", fontsize=FT["small"], color=P.ink())
b.text(0.5, s3 + 0.03, "$Aa$", ha="center", va="bottom", fontsize=FT["small"], color=P.ink())
b.text(1.0, 0.45, "heterozygote\nfrequency", fontsize=FT["tiny"], color=P.muted(), ha="left")
b.annotate("", xy=(0.25, -0.1), xytext=(0.75, -0.1), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
b.text(0.5, -0.13, "allele frequency $q$", ha="center", va="top", fontsize=FT["tiny"], color=P.muted())
b.set_xlim(-0.08, 1.2)
b.set_ylim(-0.2, 0.95)
b.set_aspect("equal")
b.axis("off")
charts.title(b, "B  De Finetti diagram")
