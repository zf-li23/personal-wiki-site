"""The geologic time scale (ICS v2024/12): eons and eras of all Earth history; Phanerozoic eras and periods
with the five largest mass extinctions (red triangles) and a few first appearances."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(28, 11)
bio.label(ax, (1.0, 10.5), "Earth history (Mya)", size="small", bold=True, ha="left")
y = phylo.geo_scale(ax, (1.0, 27.0), (4567, 0), 9.9, ranks=("eon", "era"), height=0.6)
for a in (4000, 3000, 2000, 1000, 0):
    x = 1.0 + (4567 - a) / 4567 * 26.0
    ax.plot([x, x], [y, y - 0.15], color=P.muted(), lw=0.7)
    bio.label(ax, (x, y - 0.4), f"{a}", size="tiny", color=P.muted())
x0 = 1.0 + (4567 - 720) / 4567 * 26.0
ax.plot([x0, 1.0], [y - 0.7, 5.5], color=P.muted(), lw=0.6, ls=(0, (2, 2)))
ax.plot([27.0, 27.0], [y - 0.7, 5.5], color=P.muted(), lw=0.6, ls=(0, (2, 2)))
bio.label(ax, (1.0, 5.9), "last 720 Myr (Mya)", size="small", bold=True, ha="left")


def X(a):
    return 1.0 + (720 - a) / 720 * 26.0


y2 = phylo.geo_scale(ax, (1.0, 27.0), (720, 0), 5.4, ranks=("era", "period"), height=0.6)
for a in (700, 600, 500, 400, 300, 200, 100, 0):
    ax.plot([X(a), X(a)], [y2, y2 - 0.15], color=P.muted(), lw=0.7)
    bio.label(ax, (X(a), y2 - 0.4), f"{a}", size="tiny", color=P.muted())
for a in (445, 372, 252, 201.4, 66):
    ax.plot([X(a)], [5.65], marker="v", ms=8, color=P.edge("negative"), zorder=12)
EV = [(575, "Ediacaran\nbiota"), (530, "Cambrian\nexplosion"), (430, "vascular\nplants"), (365, "tetrapods"),
      (318, "amniotes"), (230, "dinosaurs"), (150, "birds"), (130, "angio-\nsperms"), (7, "hominins")]
for k, (a, t) in enumerate(EV):
    yy = 6.2 + 0.0 * k
    bio.label(ax, (X(a), yy + (0.9 if k % 2 else 0.2)), t, size="tiny", va="bottom")
    ax.plot([X(a), X(a)], [5.75, yy + (0.85 if k % 2 else 0.15)], color=P.muted(), lw=0.6)
