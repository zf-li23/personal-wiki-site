"""John Snow's map of the 1854 Broad Street cholera outbreak, redrawn from the digitized coordinates
(578 deaths and 13 pumps; HistData package, after Tobler). A: each dot is one death, triangles are the
pumps. B: deaths classified by their nearest pump (straight-line distance); 359 of the 578 deaths lie closer
to the Broad Street pump than to any other.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def read(name):
    with open(name) as fh:
        return list(csv.DictReader(fh))


deaths = np.array([[float(r["x"]), float(r["y"])] for r in read("snow_deaths.csv")])
pumps = read("snow_pumps.csv")
pxy = np.array([[float(r["x"]), float(r["y"])] for r in pumps])
names = [r["label"] for r in pumps]
dist = np.hypot(deaths[:, None, 0] - pxy[None, :, 0], deaths[:, None, 1] - pxy[None, :, 1])
near = dist.argmin(1)
broad = names.index("Broad St")

fig = plt.figure(figsize=(10.0, 4.9))
ax = fig.add_axes([0.03, 0.16, 0.48, 0.76])
is_b = near == broad
ax.scatter(deaths[~is_b, 0], deaths[~is_b, 1], s=5, color=charts.line("dna"), lw=0, label="nearest pump: other")
ax.scatter(deaths[is_b, 0], deaths[is_b, 1], s=5, color=charts.line("rna"), lw=0, label="nearest pump: Broad St")
ax.scatter(pxy[:, 0], pxy[:, 1], marker="^", s=40, color=P.ink(), zorder=5, label="pump")
ax.annotate("Broad St pump", pxy[broad], xytext=(pxy[broad][0] + 2.2, pxy[broad][1] + 3.4),
            fontsize=FT["small"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_color(P.muted())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center", bbox_to_anchor=(0.5, -0.01), ncol=3)
charts.title(ax, "A  Cholera deaths, Soho, 1854")

bx = fig.add_axes([0.64, 0.14, 0.34, 0.76])
counts = np.bincount(near, minlength=len(names))
order = np.argsort(counts)[::-1]
order = [i for i in order if counts[i] > 0]
y = np.arange(len(order))[::-1]
bx.barh(y, counts[order], color=[P.fill("rna") if i == broad else P.fill("dna") for i in order],
        edgecolor=[P.edge("rna") if i == broad else P.edge("dna") for i in order], lw=0.8)
for yy, i in zip(y, order):
    bx.text(counts[i] + 5, yy, str(counts[i]), va="center", fontsize=FT["tiny"], color=P.ink())
bx.set_yticks(y)
bx.set_yticklabels([names[i] for i in order], fontsize=FT["tiny"])
bx.set_xlim(0, 410)
charts.style_axes(bx, "number of deaths")
charts.title(bx, "B  Deaths by nearest pump")
