# The arthropod integument (schematic, not to scale; insect-like). A: a block of body wall. The epidermis
# (a single cell layer on a basal lamina) secretes the cuticle: a thin epicuticle (cement, wax and
# cuticulin layers; no chitin) and the chitin-protein procuticle, divided into the sclerotized exocuticle
# and the lamellate endocuticle (chitin microfibrils in helicoidally rotating lamellae); pore canals cross
# the procuticle, a dermal gland opens on the surface, and a seta is formed by a trichogen (shaft) and a
# tormogen (socket) cell. B: a joint between two sclerites. The sclerotized exocuticle is interrupted by a
# flexible arthrodial membrane (unsclerotized procuticle, folded); an apodeme (inward fold of cuticle)
# gives the muscle an attachment.
import numpy as np
from matplotlib.patches import Rectangle, Ellipse, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 11.5)


def rect(x, y, w, h, tok, z=5, lw=0.8):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z))


# ---- A: block of body wall
x0, W = 1.2, 10.0
y_epi, y_exo, y_endo, y_cell, y_bl = 9.2, 7.7, 4.2, 2.6, 2.45
rect(x0, y_epi, W, 0.32, "mrna", z=7)            # epicuticle
rect(x0, y_exo, W, y_epi - y_exo, "lipid_head")   # exocuticle
rect(x0, y_endo, W, y_exo - y_endo, "lipid")      # endocuticle
for yy in np.linspace(y_endo + 0.25, y_exo - 0.2, 9):  # lamellae
    ax.plot([x0, x0 + W], [yy, yy], color=P.edge("lipid"), lw=0.5, zorder=6)
# epidermal cells
nc = 9
cw = W / nc
for i in range(nc):
    ax.add_patch(Rectangle((x0 + i * cw, y_cell), cw, y_endo - y_cell, facecolor=P.fill("ectoderm"),
                           edgecolor=P.edge("ectoderm"), lw=0.7, zorder=5))
    if i not in (3, 6, 7):
        ax.add_patch(Ellipse((x0 + (i + 0.5) * cw, y_cell + 0.75), 0.5, 0.42, facecolor=P.fill("nucleus"),
                             edgecolor=P.edge("nucleus"), lw=0.6, zorder=6))
ax.plot([x0, x0 + W], [y_bl, y_bl], color=P.ink(), lw=1.6, zorder=6)  # basal lamina
# pore canals
for xp in np.linspace(x0 + 0.5, x0 + W - 0.4, 13):
    t = np.linspace(y_endo, y_epi, 60)
    ax.plot(xp + 0.07 * np.sin((t - y_endo) * 9), t, color=P.edge("mrna"), lw=0.5, zorder=6)
# dermal gland (cell 3) with duct
gx = x0 + 3.5 * cw
ax.add_patch(Ellipse((gx, y_cell + 0.8), 0.85, 1.1, facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"), lw=0.8, zorder=7))
ax.plot([gx, gx], [y_cell + 1.3, y_epi + 0.32], color=P.edge("golgi"), lw=1.6, zorder=8)
# seta (cells 6-7): trichogen + tormogen, shaft through a socket
sx = x0 + 7.0 * cw
ax.add_patch(Ellipse((sx - 0.35, y_cell + 0.75), 0.7, 1.0, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=7))
ax.add_patch(Ellipse((sx + 0.4, y_cell + 0.95), 0.6, 0.8, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, zorder=7))
ax.add_patch(Polygon([(sx - 0.45, y_epi + 0.32), (sx + 0.45, y_epi + 0.32), (sx + 0.25, y_epi + 0.6), (sx - 0.25, y_epi + 0.6)],
                     facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=0.8, zorder=8))
ax.add_patch(Polygon([(sx - 0.08, y_cell + 1.2), (sx + 0.08, y_cell + 1.2), (sx + 0.05, y_epi + 0.5), (sx + 1.0, 11.2), (sx + 0.85, 11.25),
                      (sx - 0.05, y_epi + 0.55)], facecolor=P.fill("mrna"), edgecolor=P.edge("mrna"), lw=0.7, zorder=9))
bio.panel(ax, "A", (0.2, 11.4))
L = 11.6  # label column
items = [((x0 + W - 0.2, y_epi + 0.16), (L, 10.4), "Epicuticle (no chitin; wax layer)"),
         ((x0 + W - 0.2, 8.5), (L, 8.6), "Exocuticle (sclerotized)"),
         ((x0 + W - 0.2, 6.0), (L, 6.4), "Endocuticle (lamellate)"),
         ((x0 + W - 0.2, 3.4), (L, 3.6), "Epidermis"),
         ((x0 + W - 0.2, y_bl), (L, 2.1), "Basal lamina")]
for pt, tx, s in items:
    bio.callout(ax, pt, tx, s, size="small")
bio.callout(ax, (gx, 6.6), (1.6, 0.9), "Duct of dermal gland", size="small")
bio.callout(ax, (x0 + 5.3 * cw, 5.4), (5.4, 0.9), "Pore canal", size="small")
bio.callout(ax, (sx + 0.6, 10.6), (sx - 1.3, 11.1), "Seta", size="small")
bio.callout(ax, (sx + 0.4, y_cell + 0.9), (9.3, 0.9), "Socket and shaft cells", size="small")
ax.plot([x0 - 0.35, x0 - 0.35], [y_endo, y_epi], color=P.muted(), lw=0.9)
bio.label(ax, (x0 - 0.6, (y_endo + y_epi) / 2), "Procuticle", size="small", rotation=90, color=P.muted())

# ---- B: joint between two sclerites
bx = 16.0
bio.panel(ax, "B", (bx - 0.7, 11.4))
yt, th = 8.4, 0.9   # top of cuticle, thickness
t = np.linspace(0, 1, 200)
xs = bx + 10.0 * t
# arthrodial membrane between x=bx+4 and bx+6 is folded downward
fold = np.where((xs > bx + 4) & (xs < bx + 6), -0.9 * np.sin(np.pi * (xs - bx - 4) / 2) ** 2, 0.0)
top = yt + fold
# endocuticle/procuticle continuous
ax.fill_between(xs, top - th, top - 0.08, color=P.fill("lipid"), zorder=5, lw=0)
ax.plot(xs, top - th, color=P.edge("lipid"), lw=0.8, zorder=6)
ax.fill_between(xs, top - 0.08, top, color=P.fill("mrna"), zorder=6, lw=0)
for a, b in ((bx, bx + 3.9), (bx + 6.1, bx + 10)):
    m = (xs >= a) & (xs <= b)
    ax.fill_between(xs[m], top[m] - 0.5, top[m] - 0.08, color=P.fill("lipid_head"), zorder=7, lw=0)
# apodeme: an inward fold of cuticle from the right sclerite
ax.add_patch(Polygon([(bx + 6.6, yt - th + 0.02), (bx + 7.1, yt - th + 0.02), (bx + 6.95, yt - 3.0), (bx + 6.75, yt - 3.0)],
                     facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=0.8, zorder=7))
# muscle from the left sclerite to the apodeme tip
ax.add_patch(Polygon([(bx + 1.2, yt - th), (bx + 2.6, yt - th), (bx + 6.8, yt - 2.85), (bx + 6.8, yt - 3.1)],
                     facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.8, zorder=4))
bio.label(ax, (bx + 2.0, yt + 0.45), "Sclerite", size="small")
bio.label(ax, (bx + 8.0, yt + 0.45), "Sclerite", size="small")
bio.callout(ax, (bx + 5.0, yt - 1.2), (bx + 5.0, 4.9), "Arthrodial membrane", size="small")
bio.callout(ax, (bx + 6.9, yt - 2.4), (bx + 8.6, 4.3), "Apodeme", size="small")
bio.callout(ax, (bx + 4.2, yt - 2.0), (bx + 1.2, 4.3), "Muscle", size="small")
bio.label(ax, (bx + 5.0, 2.6), "Outside up; hemocoel below", size="tiny", color=P.muted())
