# The eight gamete classes of the three-point testcross b pr vg (Example 8.4.1) and the resulting map
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(19, 9.2)
par = (("b+", "pr", "vg+"), ("b", "pr+", "vg"))
cls = [(("b+", "pr", "vg+"), 1640), (("b", "pr+", "vg"), 1632), (("b", "pr", "vg+"), 118), (("b+", "pr+", "vg"), 110),
       (("b+", "pr", "vg"), 247), (("b", "pr+", "vg+"), 241), (("b+", "pr+", "vg+"), 5), (("b", "pr", "vg"), 7)]
loci = [0.12, 0.42, 0.9]  # 6.0 and 12.5 cM to scale
T.three_point(ax, (0.6, 7.7), par, loci, cls, width=5.6, row=0.78, count_x=8.6, type_x=9.3)
# map below
y = 0.75
x0, w = 0.6, 5.6
ax.plot([x0, x0 + w], [y, y], color=bio.P.edge("chromatin"), lw=3.0, solid_capstyle="round")
for f, g in zip(loci, ["b", "pr", "vg"]):
    ax.plot([x0 + f * w] * 2, [y - 0.18, y + 0.18], color=bio.P.ink(), lw=1.3)
    bio.label(ax, (x0 + f * w, y + 0.3), T.allele(g), size="small", va="bottom")
bio.label(ax, (x0 + (loci[0] + loci[1]) / 2 * w, y - 0.32), "6.0 cM", size="tiny", va="top")
bio.label(ax, (x0 + (loci[1] + loci[2]) / 2 * w, y - 0.32), "12.5 cM", size="tiny", va="top")
bio.label(ax, (9.3, y + 0.1), "n = 4000;  C = 12 / 30 = 0.40,  I = 0.60", size="small", ha="left")
