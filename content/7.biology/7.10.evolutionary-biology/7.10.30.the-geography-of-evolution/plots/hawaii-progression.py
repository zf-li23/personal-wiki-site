"""The progression rule in the Hawaiian Islands (Section 30.4.3). Left: the main islands, which formed in
sequence as the Pacific plate moved northwest over a volcanic hot spot (approximate ages after
Futuyma and Kirkpatrick 2017, Fig. 18.12). Right: the phylogeny expected for a clade that colonized
each island soon after it formed and never moved back to an older island: a comb in which the
earliest-diverging lineages live on the oldest island and the most recently diverged on the
youngest. Lineage names are schematic."""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={"width_ratios": [1.15, 1]})
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.13, top=0.88, wspace=0.08)

ISL = [("Kauai", "~5 Myr", (1.0, 3.2), 0.55, 0.42, "dna"),
       ("Oahu", "~2.5 Myr", (3.1, 2.7), 0.6, 0.38, "rna"),
       ("Maui Nui", "~1 Myr", (5.3, 2.0), 0.85, 0.42, "plant"),
       ("Hawaii", "<0.5 Myr", (7.6, 0.95), 0.95, 0.85, "highlight")]
for name, age, (x, y), rx, ry, tok in ISL:
    verts = bio.core.blob((x, y), rx, ry, wobble=0.1, seed=len(name))
    bio.core.shape(a, verts, token=tok)
    a.text(x, y + ry + 0.22, name, ha="center", fontsize=FT["small"], color=ink, weight="bold")
    a.text(x, y - ry - 0.25, age, ha="center", va="top", fontsize=FT["tiny"], color=muted)
a.annotate("", xy=(0.5, 4.3), xytext=(3.0, 3.6), arrowprops=dict(arrowstyle="-|>", color=muted, lw=1.2))
a.text(1.9, 4.25, "plate motion", fontsize=FT["tiny"], color=muted, rotation=17)
a.plot([9.0], [-0.1], marker="*", ms=12, color=P.edge("negative"))
a.text(9.0, -0.55, "hot spot", fontsize=FT["tiny"], color=muted, ha="center")
for (n1, _, p1, rx1, ry1, _t1), (n2, _, p2, rx2, ry2, _t2) in zip(ISL[:-1], ISL[1:]):
    a.annotate("", xy=(p2[0] - rx2 * 0.75, p2[1] + ry2 * 0.75), xytext=(p1[0] + rx1 * 0.85, p1[1] - ry1 * 0.2),
               arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.3, connectionstyle="arc3,rad=-0.25"))
a.text(4.2, 3.9, "colonization", fontsize=FT["tiny"], color=charts.line("negative"))
a.set_xlim(-0.2, 9.4)
a.set_ylim(-0.9, 4.7)
a.set_aspect("equal")
a.axis("off")
charts.title(a, "A  Islands formed in sequence")

# comb phylogeny: tips K1, K2, O1, M1, H1 (top to bottom); nodes at decreasing ages
tips = [("lineage 1", "dna"), ("lineage 2", "dna"), ("lineage 3", "rna"), ("lineage 4", "plant"), ("lineage 5", "highlight")]
node_age = [5.0, 4.4, 2.2, 0.8]
y = np.arange(len(tips))[::-1].astype(float)
prev_y = y[0]
x_prev = node_age[0]
yy = (y[0] + y[1]) / 2
b.plot([node_age[0] + 0.5, node_age[0]], [yy, yy], color=ink, lw=1.5)
spine = [(node_age[0], (y[0] + y[1]) / 2)]
cur_y = (y[0] + y[1]) / 2
b.plot([node_age[0], node_age[0]], [y[0], cur_y], color=ink, lw=1.5)
b.plot([node_age[0], 0], [y[0], y[0]], color=charts.line(tips[0][1]), lw=2.2)
for k in range(1, len(tips)):
    na = node_age[k] if k < len(node_age) else None
    if na is None:
        b.plot([node_age[-1], 0], [y[k], y[k]], color=charts.line(tips[k][1]), lw=2.2)
        b.plot([node_age[-1], node_age[-1]], [cur_y, y[k]], color=ink, lw=1.5)
        break
    ny = (y[k] + y[k + 1]) / 2
    b.plot([node_age[k - 1], node_age[k - 1]], [cur_y, ny], color=ink, lw=1.5)
    b.plot([node_age[k - 1], na], [ny, ny], color=ink, lw=1.5)
    b.plot([na, na], [ny, y[k]], color=ink, lw=1.5)
    b.plot([na, 0], [y[k], y[k]], color=charts.line(tips[k][1]), lw=2.2)
    cur_y = ny
    b.plot([node_age[k - 1], node_age[k - 1]], [ny, ny], color=ink)
for (lab, tok), yk, isl in zip(tips, y, ["Kauai", "Kauai", "Oahu", "Maui Nui", "Hawaii"]):
    b.text(-0.12, yk, f"{lab} ({isl})", va="center", ha="left", fontsize=FT["small"], color=ink)
b.set_xlim(5.8, -2.6)
b.set_ylim(-0.6, 4.6)
b.set_yticks([])
b.set_xticks([5, 4, 3, 2, 1, 0])
charts.style_axes(b, "time (Myr ago)")
b.spines["left"].set_visible(False)
charts.title(b, "B  Expected phylogeny: a comb")
