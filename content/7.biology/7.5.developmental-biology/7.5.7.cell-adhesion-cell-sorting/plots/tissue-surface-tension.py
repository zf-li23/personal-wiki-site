"""Measuring tissue surface tension and using it to predict engulfment.

A: parallel-plate compression of a spherical aggregate (Foty and colleagues). At mechanical
equilibrium, after the viscous flow has stopped, the force F on the plate balances the Laplace pressure:
F / (pi R3^2) = gamma (1/R1 + 1/R2), where R1 is the radius of curvature of the free profile in the
meridional plane, R2 the equatorial radius and R3 the radius of the contact disc with the plate.
B: surface tensions of chick embryonic tissue aggregates (Foty et al. 1996; mN/m) and the measured
sorting order: in each pair the tissue of higher tension ends up inside, enveloped by the tissue of
lower tension.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(29.0, 10.6)
bio.panel(ax, "A", (0.1, 10.5))
cx, cy = 6.0, 5.2
H, R2 = 2.0, 3.0      # half height, equatorial radius
R3 = 2.1              # contact radius
# profile: circular arc from (R3, H) to (R2, 0) with centre on the equator
c = (R2 ** 2 - R3 ** 2 - H ** 2) / (2 * (R2 - R3)) if False else None
r1 = (H ** 2 + (R2 - R3) ** 2) / (2 * (R2 - R3))   # arc through (R3, +-H) tangent-vertical at (R2, 0)
xc = R2 - r1
t = np.linspace(-np.arcsin(H / r1), np.arcsin(H / r1), 80)
right = np.c_[xc + r1 * np.cos(t), r1 * np.sin(t)]
left = np.c_[-right[:, 0], right[:, 1]][::-1]
outline = np.vstack([right, left[::-1][::-1]])
poly = np.vstack([right, left])
bio.shape(ax, poly + np.array([cx, cy]), "mesoderm", lw=1.2)
for yy in (cy + H, cy - H - 0.35):
    bio.box(ax, (cx, yy + 0.175), 8.6, 0.35, "neutral", radius=0.05)
bio.arrow(ax, (cx, cy + H + 1.6), (cx, cy + H + 0.45), kind="process")
bio.label(ax, (cx + 0.3, cy + H + 1.3), "F", size="normal", ha="left", italic=True)
bio.label(ax, (cx + 4.6, cy + H + 0.17), "plate", size="tiny", ha="left")
# dimension marks
ax.annotate("", xy=(cx + R2, cy), xytext=(cx, cy), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8), zorder=20)
bio.label(ax, (cx + R2 / 2, cy + 0.3), "R2", size="small", italic=True)
ax.annotate("", xy=(cx + R3, cy + H - 0.35), xytext=(cx, cy + H - 0.35), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8), zorder=20)
bio.label(ax, (cx + R3 / 2, cy + H - 0.7), "R3", size="small", italic=True)
ax.plot([cx + xc, cx + R2 - 0.1], [cy, cy - 0.02], color=P.ink(), lw=0.7, ls=(0, (2, 1.5)), zorder=20)
bio.callout(ax, (cx + R2 - 0.05, cy - 0.9), (cx + 4.4, cy - 2.6), "profile radius R1", size="tiny")
bio.label(ax, (cx, 1.0), "F / (π R3²) = γ (1/R1 + 1/R2)", size="small")

bio.panel(ax, "B", (13.6, 10.5))
pb = charts.axes_at(ax, (17.4, 1.6, 10.8, 7.8))
tissues = ["limb bud\nmesoderm", "pigmented\nretina", "heart\nventricle", "liver", "neural\nretina"]
vals = [20.1, 12.6, 8.5, 4.6, 1.6]
yv = np.arange(5)[::-1]
pb.barh(yv, vals, color=[P.fill("mesoderm")] * 5, edgecolor=P.edge("mesoderm"), height=0.6)
pb.set_yticks(yv)
pb.set_yticklabels(tissues)
for yy, v in zip(yv, vals):
    pb.text(v + 0.4, yy, f"{v:g}", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xlim(0, 25)
charts.style_axes(pb, "surface tension γ / (mN m⁻¹)")
charts.title(pb, "Higher tension sorts inside")
for k in range(4):
    y0, y1 = yv[k], yv[k + 1]
    pb.annotate("", xy=(23.5, y0 - 0.05), xytext=(23.5, y1 + 0.05),
                arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
pb.text(24.0, 2, "envelops\nthe one\nabove", fontsize=bio.core.FONT["tiny"], color=P.muted(), va="center")
