"""The fold and the cusp: potential families, equilibria and the bifurcation set.

A: fold, phi(x; u) = x^3 + 3 u x for u = -1, -0.25, 0 and 0.5: a minimum and a maximum exist for u < 0,
merge at u = 0 and vanish for u > 0. B: cusp, phi(x; u, v) = x^4 + 6 u x^2 + 4 v x at u = -0.5 for
several v: two minima for |v| < 2(-u)^(3/2), one outside. C: equilibria of the cusp at u = -0.5
against v (stable: solid; unstable: dashed): the S-shaped curve folds back at v = +-2(-u)^(3/2);
arrows show the jumps of perfect delay; the vertical line at v = 0 is the Maxwell switch point.
D: the bifurcation (catastrophe) set v^2 + 4 u^3 = 0 in the control plane: three critical points
inside the cusp, one outside; dotted, the Maxwell set v = 0, u < 0.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(36.0, 9.6)
toks = ["ectoderm", "positive", "highlight", "mesoderm", "protein"]

bio.panel(ax, "A", (0.1, 9.5))
pa = charts.axes_at(ax, (1.8, 1.8, 6.6, 6.6))
x = np.linspace(-1.6, 1.6, 300)
for u, tok in zip((-1, -0.25, 0, 0.5), toks):
    pa.plot(x, x ** 3 + 3 * u * x, color=quant.line_color(tok), lw=1.8, label=f"u = {u:g}")
pa.set_ylim(-3, 3)
pa.set_xlim(-1.6, 1.6)
charts.style_axes(pa, "x", "φ(x; u)")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pa, "Fold: x³ + 3ux")

bio.panel(ax, "B", (9.3, 9.5))
pb = charts.axes_at(ax, (11.0, 1.8, 6.6, 6.6))
u = -0.5
vc = 2 * (-u) ** 1.5
for v, tok in zip((-0.9, -vc, 0, vc * 0.6, 0.9), toks):
    pb.plot(x, x ** 4 + 6 * u * x ** 2 + 4 * v * x, color=quant.line_color(tok), lw=1.8, label=f"v = {v:.2f}")
pb.set_ylim(-4, 4)
pb.set_xlim(-1.6, 1.6)
charts.style_axes(pb, "x", "φ(x; u = −0.5, v)")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper center", ncol=2)
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pb, "Cusp: x⁴ + 6ux² + 4vx")

bio.panel(ax, "C", (18.5, 9.5))
pc = charts.axes_at(ax, (20.2, 1.8, 6.6, 6.6))
xs = np.linspace(-1.8, 1.8, 600)
vs = -(xs ** 3 + 3 * u * xs)
stable = 3 * xs ** 2 + 3 * u > 0
col = quant.line_color("protein")
for mask, ls in ((stable & (xs < 0), "-"), (stable & (xs > 0), "-"), (~stable, (0, (3, 2)))):
    pc.plot(np.where(mask, vs, np.nan), xs, color=col, lw=2.0, ls=ls)
xf = np.sqrt(-u)
pc.annotate("", xy=(vc, -2 * xf), xytext=(vc, xf), arrowprops=dict(arrowstyle="->", color=P.edge("mesoderm"), lw=1.2))
pc.annotate("", xy=(-vc, 2 * xf), xytext=(-vc, -xf), arrowprops=dict(arrowstyle="->", color=P.edge("mesoderm"), lw=1.2))
pc.axvline(0, color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
pc.set_xlim(-1.6, 1.6)
pc.set_ylim(-1.8, 1.8)
charts.style_axes(pc, "control v", "equilibria x")
charts.title(pc, "Hysteresis at u = −0.5")

bio.panel(ax, "D", (27.6, 9.5))
pd = charts.axes_at(ax, (29.3, 1.8, 6.4, 6.6))
uu = np.linspace(-1, 0, 200)
vv = 2 * (-uu) ** 1.5
pd.fill_betweenx(uu, -vv, vv, color=P.light("highlight"), lw=0)
pd.plot(vv, uu, color=P.ink(), lw=1.6)
pd.plot(-vv, uu, color=P.ink(), lw=1.6)
pd.plot([0, 0], [-1, 0], color=P.muted(), lw=1.0, ls=(0, (1, 1.5)))
pd.text(-0.35, -0.75, "3 critical\npoints", fontsize=bio.core.FONT["tiny"], color=P.ink())
pd.text(1.0, -0.2, "1", fontsize=bio.core.FONT["tiny"], color=P.ink())
pd.text(0.05, -0.95, "Maxwell set", fontsize=bio.core.FONT["tiny"], color=P.muted(), rotation=90)
pd.set_xlim(-2, 2)
pd.set_ylim(-1, 0.5)
charts.style_axes(pd, "v", "u")
charts.title(pd, "Bifurcation set v² + 4u³ = 0")
