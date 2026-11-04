"""The flagellum of a Gram-negative bacterium in cross-section (schematic): filament, cap, hook, rod,
L, P, MS and C rings, export apparatus, MotA-MotB stators with proton flow; inset: Gram-positive basal body."""
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(24, 16)
x0, x1, xc = 1.0, 15.0, 8.0
y_im, y_pg, y_om = 4.0, 6.0, 8.0
ax.add_patch(Rectangle((x0, 1.0), x1 - x0, y_im - 1.0, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, y_im), x1 - x0, y_om - y_im, facecolor=M.periplasm_color(), edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, y_om), x1 - x0, 15.6 - y_om, facecolor=P.fill("extracellular"), edgecolor="none", zorder=1))
gap = [(xc - 1.9, xc + 1.9)]
M.bilayer(ax, x0, x1, y_im, skip=[(xc - 2.9, xc + 2.9)], zorder=4)
M.peptidoglycan(ax, x0, xc - 1.1, y_pg - 0.1, layers=1, spacing=0.3, seed=1, zorder=4)
M.peptidoglycan(ax, xc + 1.1, x1, y_pg - 0.1, layers=1, spacing=0.3, seed=2, zorder=4)
M.bilayer(ax, x0, x1, y_om, skip=[(xc - 1.2, xc + 1.2)], zorder=4)


def ring(y, half, h, tok, z=8):
    ax.add_patch(FancyBboxPatch((xc - half, y - h / 2), 2 * half, h, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=z))


# rod
ax.add_patch(Rectangle((xc - 0.25, y_im - 0.3), 0.5, y_om + 0.6 - y_im + 0.3, facecolor=P.fill("protein"),
                       edgecolor=P.edge("protein"), lw=1.0, zorder=9))
ring(y_om, 1.1, 0.55, "protein")          # L ring
ring(y_pg, 1.0, 0.5, "protein")           # P ring
ring(y_im, 1.6, 0.7, "enzyme")            # MS ring
# C ring: hanging bell below the membrane
ax.add_patch(FancyBboxPatch((xc - 2.0, 1.9), 0.5, 1.6, boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("receptor"),
                            edgecolor=P.edge("receptor"), lw=1.0, zorder=8))
ax.add_patch(FancyBboxPatch((xc + 1.5, 1.9), 0.5, 1.6, boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("receptor"),
                            edgecolor=P.edge("receptor"), lw=1.0, zorder=8))
ax.add_patch(FancyBboxPatch((xc - 2.0, 1.7), 4.0, 0.4, boxstyle="round,pad=0,rounding_size=0.15", facecolor=P.fill("receptor"),
                            edgecolor=P.edge("receptor"), lw=1.0, zorder=8))
# export apparatus
ax.add_patch(FancyBboxPatch((xc - 0.6, 2.4), 1.2, 1.0, boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("neutral"),
                            edgecolor=P.edge("neutral"), lw=1.0, zorder=9))
# stators
for sx in (xc - 2.55, xc + 2.55):
    ax.add_patch(FancyBboxPatch((sx - 0.35, y_im - 0.75), 0.7, 1.5, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.0, zorder=9))
    ax.plot([sx, sx], [y_im + 0.75, y_pg - 0.15], color=P.edge("channel"), lw=2.0, zorder=8)
    bio.arrow(ax, (sx + 0.75 * np.sign(sx - xc), y_im + 1.2), (sx + 0.75 * np.sign(sx - xc), y_im - 1.1), kind="process",
              color=P.edge("h"))
    bio.label(ax, (sx + 1.15 * np.sign(sx - xc), y_im + 1.25), "H⁺", size="small", color=P.edge("h"))
# hook and filament
t = np.linspace(0, 1, 50)
hx = xc + 1.6 * t ** 2
hy = y_om + 0.6 + 1.6 * t
ax.plot(hx, hy, color=P.edge("protein"), lw=6, solid_capstyle="round", zorder=7)
ys = np.linspace(hy[-1], 15.0, 200)
fx = hx[-1] + 0.5 * np.sin((ys - hy[-1]) * 1.3) + (ys - hy[-1]) * 0.05
ax.plot(fx, ys, color=P.edge("flagellum"), lw=4, solid_capstyle="round", zorder=7)
ax.add_patch(FancyBboxPatch((fx[-1] - 0.3, 15.0), 0.6, 0.35, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=8))
# layer labels on the left
for y, txt in [(y_om + 0.75, "outer membrane"), (y_pg + 0.35, "peptidoglycan"), (y_im + 0.85, "cytoplasmic\nmembrane")]:
    bio.label(ax, (x0 + 0.1, y), txt, size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 0.1, 15.2), "Outside", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 0.1, 7.3), "Periplasm", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 0.1, 1.3), "Cytoplasm", size="tiny", ha="left", color=P.muted())
c = 15.6
bio.callout(ax, (fx[-1] + 0.3, 15.15), (c, 15.2), "Cap (FliD)")
bio.callout(ax, (fx[150], ys[150]), (c, 13.2), "Filament (flagellin)")
bio.callout(ax, (hx[30], hy[30]), (c, 10.2), "Hook")
bio.callout(ax, (xc + 1.1, y_om), (c, 8.7), "L ring")
bio.callout(ax, (xc + 1.0, y_pg), (c, 6.8), "P ring")
bio.callout(ax, (xc + 0.25, 5.0), (c, 5.9), "Rod")
bio.callout(ax, (xc + 2.9, y_im), (c, 4.9), "Stator (MotA–MotB)")
bio.callout(ax, (xc + 1.6, y_im - 0.2), (c, 4.0), "MS ring")
bio.callout(ax, (xc + 2.0, 2.4), (c, 2.8), "C ring (switch:\nFliG, FliM, FliN)")
bio.callout(ax, (xc + 0.6, 2.7), (c, 1.6), "Export apparatus (type III)")
bio.label(ax, (x0, 0.5), "In Gram-positive bacteria the basal body has no L or P ring.", size="tiny", ha="left", color=P.muted())
