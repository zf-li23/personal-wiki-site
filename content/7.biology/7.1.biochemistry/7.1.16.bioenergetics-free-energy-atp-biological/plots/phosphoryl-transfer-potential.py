"""Phosphoryl group transfer potential: compounds ranked by the standard Gibbs energy of hydrolysis
of their donor phosphoryl group (Lehninger 8e, Table 13-6). Arrows: kinase-catalyzed transfers,
which run downhill from the high-energy donors of catabolism via ADP/ATP to low-energy acceptors;
creatine kinase is reversible."""

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(17.0, 11.0)
q = charts.axes_at(ax, (2.2, 0.7, 1.0, 9.8))
q.set_ylim(-66, -6)
q.set_xlim(0, 1)
q.set_xticks([])
charts.style_axes(q, None, r"$\Delta_{\mathrm{r}}G'^{\circ}$ of hydrolysis / (kJ mol$^{-1}$)")
q.invert_yaxis()

def Y(g):
    return 0.7 + 9.8 * (g + 6) / (-60)

items = [(-61.9, "Phosphoenolpyruvate", 7.4, "highlight"), (-49.3, "1,3-Bisphosphoglycerate", 7.4, "highlight"),
         (-43.0, "Phosphocreatine", 12.9, "muscle"), (-30.5, "ATP", 7.4, "atp"),
         (-20.9, "Glucose 1-phosphate", 12.9, "metabolite"), (-13.8, "Glucose 6-phosphate", 7.4, "metabolite"),
         (-9.2, "Glycerol 3-phosphate", 12.9, "metabolite")]
pos = {}
for g, name, x, tok in items:
    y = Y(g)
    ax.plot([3.25, x - 2.0], [y, y], color=P.muted(), lw=0.6, ls=":")
    bio.box(ax, (x, y), 4.0, 0.75, tok, name, size="small")
    bio.label(ax, (x + 2.15, y), f"{g:.1f}", size="tiny", ha="left", color=P.muted())
    pos[name] = (x, y)
yc = Y(-25)
ax.plot([3.25, 16.9], [yc, yc], color=P.muted(), lw=0.9, ls="--")
bio.label(ax, (3.5, yc + 0.3), "high-energy compounds", size="tiny", ha="left", color=P.muted())
bio.label(ax, (3.5, yc - 0.3), "low-energy compounds", size="tiny", ha="left", color=P.muted())
x0, y0 = pos["ATP"]
for n in ("Phosphoenolpyruvate", "1,3-Bisphosphoglycerate"):
    x, y = pos[n]
    bio.arrow(ax, (x - 2.2, y), (x0 - 2.2, y0), kind="process", bend=0.25 if n == "Phosphoenolpyruvate" else 0.3)
bio.arrow(ax, (x0 - 2.1, y0 + 0.4), pos["Glucose 6-phosphate"] - __import__("numpy").array([2.1, 0.4]), kind="process", bend=0.35)
xp, yp = pos["Phosphocreatine"]
bio.arrow(ax, (x0 + 2.05, y0 - 0.15), (xp - 2.05, yp + 0.1), kind="process", bend=-0.1)
bio.arrow(ax, (xp - 2.05, yp + 0.4), (x0 + 2.05, y0 - 0.45), kind="process", bend=-0.1)
xg, yg = pos["Glycerol 3-phosphate"]
bio.arrow(ax, (x0 + 2.05, y0 + 0.2), (xg - 2.05, yg), kind="process", bend=0.15)
bio.label(ax, (3.7, Y(-40)), "pyruvate kinase,\nPGK", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (10.3, Y(-38.6)), "creatine\nkinase", size="tiny", color=P.muted())
bio.label(ax, (3.7, Y(-17.3)), "hexokinase", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (11.0, Y(-17)), "glycerol\nkinase", size="tiny", color=P.muted())
