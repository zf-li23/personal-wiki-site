"""Partitioning variation in the ToothGrowth experiment (60 guinea pigs, Crampton 1947; R datasets::ToothGrowth).
A: odontoblast length by daily vitamin C dose (both delivery methods pooled; 20 animals per dose), group
means (short lines) and grand mean (dashed): the between-group part is the spread of the group means
around the grand mean, the within-group part the spread of animals around their group mean. B: the total
sum of squares split by one-way ANOVA (dose) and by two-way ANOVA (dose, delivery, interaction): the
residual part shrinks when the second factor and the interaction are modelled.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("toothgrowth.csv") as fh:
    rows = list(csv.DictReader(fh))
y = np.array([float(r["len"]) for r in rows])
dose = np.array([float(r["dose"]) for r in rows])
supp = np.array([r["supp"] for r in rows])
doses = [0.5, 1.0, 2.0]
gm = y.mean()
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6), gridspec_kw=dict(width_ratios=[1.3, 1]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.3)
ax = axs[0]
rng = np.random.default_rng(0)
for k, d in enumerate(doses):
    yy = y[dose == d]
    xs = k + rng.uniform(-0.18, 0.18, yy.size)
    m = yy.mean()
    for xv, yv in zip(xs, yy):
        ax.plot([xv, xv], [m, yv], color=P.muted(), lw=0.5, alpha=0.7)
    ax.scatter(xs, yy, s=12, color=P.fill("enzyme"), edgecolor=charts.line("enzyme"), lw=0.6, zorder=3)
    ax.plot([k - 0.3, k + 0.3], [m, m], color=P.ink(), lw=2)
    ax.annotate("", (k + 0.36, m), (k + 0.36, gm), arrowprops=dict(arrowstyle="->", color=charts.line("rna"), lw=1.2))
ax.axhline(gm, color=P.ink(), lw=0.9, ls="--")
ax.text(2.45, gm + 0.5, "grand mean", fontsize=FT["tiny"], color=P.ink(), ha="right")
ax.set_xticks(range(3))
ax.set_xticklabels([f"{d:g} mg/d" for d in doses], fontsize=FT["tiny"])
ax.set_xlim(-0.5, 2.6)
charts.style_axes(ax, "vitamin C dose", "odontoblast length")
charts.title(ax, "A  Between and within groups")

ax = axs[1]
sst = ((y - gm) ** 2).sum()
ssd = sum((dose == d).sum() * (y[dose == d].mean() - gm) ** 2 for d in doses)
sss = sum((supp == s).sum() * (y[supp == s].mean() - gm) ** 2 for s in ("OJ", "VC"))
cells = [(d, s) for d in doses for s in ("OJ", "VC")]
sse2 = sum(((y[(dose == d) & (supp == s)] - y[(dose == d) & (supp == s)].mean()) ** 2).sum() for d, s in cells)
ssi = sst - ssd - sss - sse2
bars = [("one-way", [(ssd, "dose", "enzyme"), (sst - ssd, "residual", "neutral")]),
        ("two-way", [(ssd, "dose", "enzyme"), (sss, "delivery", "rna"), (ssi, "dose x delivery", "protein"),
                     (sse2, "residual", "neutral")])]
for k, (nm, parts) in enumerate(bars):
    bottom = 0
    for v, lab, tok in parts:
        ax.bar(k, v, 0.55, bottom=bottom, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
        ax.text(k + 0.31, bottom + v / 2, f"{lab} {v:.0f}", fontsize=FT["tiny"], color=P.ink(), va="center")
        bottom += v
ax.set_xticks([0, 1])
ax.set_xticklabels(["one-way", "two-way"], fontsize=FT["tiny"])
ax.set_xlim(-0.5, 2.0)
charts.style_axes(ax, None, "sum of squares")
charts.title(ax, f"B  Total SS = {sst:.0f}")
