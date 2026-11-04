"""The bloodstream form of Trypanosoma brucei (schematic, not to scale): the kinetoplast (kDNA) at the base of
the flagellum inside the single mitochondrion, the flagellum attached along the cell, glycosomes, and the dense
coat of variant surface glycoprotein (VSG)."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon, PathPatch
from matplotlib.path import Path
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(13.2, 8.6)

# ---------------- A: cell
x = np.linspace(0, 1, 200)
cx = 1.0 + 9.0 * x
cy = 4.6 + 0.55 * np.sin(np.pi * x * 1.2 - 0.3)
w = 0.62 * np.sin(np.pi * np.clip(x, 0.02, 0.98)) ** 0.7
top = np.c_[cx, cy + w]
bot = np.c_[cx, cy - w][::-1]
body = np.vstack([top, bot])
ax.add_patch(Polygon(body, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("protein"), lw=1.3, zorder=5))
# VSG coat: small dots on the outline
for (px, py) in body[::5]:
    ax.add_patch(Ellipse((px, py), 0.12, 0.12, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.4, zorder=6))
# mitochondrion running along the cell
mi = (x > 0.12) & (x < 0.85)
ax.plot(cx[mi], cy[mi] - 0.18, color=P.edge("mitochondrion"), lw=4.0, solid_capstyle="round", zorder=7)
# kinetoplast near the posterior end, basal body next to it
kx, ky = 1.0 + 9.0 * 0.15, np.interp(0.15, x, cy)
ax.add_patch(Ellipse((kx, ky - 0.18), 0.5, 0.3, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=8))
bx = kx + 0.55
ax.add_patch(Ellipse((bx, ky + 0.12), 0.2, 0.28, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=8))
# nucleus
nx, ny = 1.0 + 9.0 * 0.52, np.interp(0.52, x, cy)
ax.add_patch(Ellipse((nx, ny + 0.05), 1.1, 0.72, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=8))
ax.add_patch(Ellipse((nx + 0.1, ny + 0.1), 0.3, 0.25, facecolor=P.fill("nucleolus"), edgecolor=P.edge("nucleolus"), lw=0.6, zorder=9))
# glycosomes
for xf in (0.33, 0.42, 0.66, 0.72):
    gx, gy = 1.0 + 9.0 * xf, np.interp(xf, x, cy) + 0.25
    ax.add_patch(Ellipse((gx, gy), 0.22, 0.22, facecolor=P.fill("peroxisome"), edgecolor=P.edge("peroxisome"), lw=0.6, zorder=8))
# flagellum: from the flagellar pocket near the basal body, along the top edge, free beyond the anterior tip
fx = np.linspace(0.2, 1.0, 160)
fxx = 1.0 + 9.0 * fx
fyy = np.interp(fx, x, cy) + np.interp(fx, x, w) + 0.12 + 0.08 * np.sin(fx * 40)
ext = np.linspace(10.0, 11.6, 30)
ax.plot(np.r_[fxx, ext], np.r_[fyy, cy[-1] + 0.05 + 0.18 * np.sin((ext - 10) * 5)], color=P.edge("flagellum"),
        lw=1.8, zorder=9)
ax.plot([bx, fxx[0]], [ky + 0.25, fyy[0]], color=P.edge("flagellum"), lw=1.8, zorder=9)
# undulating membrane fold (thin shading between body edge and flagellum)
uw = np.interp(fx, x, cy) + np.interp(fx, x, w)
ax.fill_between(fxx, uw, fyy, color=P.fill("membrane"), alpha=0.6, zorder=6, lw=0)
bio.callout(ax, (kx, ky - 0.2), (1.6, 2.4), "kinetoplast (kDNA)")
bio.callout(ax, (bx, ky + 0.2), (1.2, 6.9), "basal body, flagellar pocket")
bio.callout(ax, (nx, ny - 0.3), (5.0, 2.4), "nucleus")
bio.callout(ax, (1.0 + 9.0 * 0.6, np.interp(0.6, x, cy) - 0.2), (7.4, 2.4), "single mitochondrion")
bio.callout(ax, (1.0 + 9.0 * 0.42, np.interp(0.42, x, cy) + 0.25), (4.2, 7.6), "glycosomes")
bio.callout(ax, (1.0 + 9.0 * 0.75, uw[120] + 0.1), (8.0, 7.6), "flagellum attached along the cell")
bio.callout(ax, top[150], (10.6, 6.9), "VSG coat")
bio.label(ax, (5.8, 1.3), "bloodstream form, about 20 µm long", size="small", italic=False, color=P.muted())

