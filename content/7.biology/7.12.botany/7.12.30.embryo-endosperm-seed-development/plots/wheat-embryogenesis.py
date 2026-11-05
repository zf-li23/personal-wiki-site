"""Embryo development in wheat (Triticum aestivum), schematic longitudinal sections, micropylar end down,
endosperm to the right. A four-celled proembryo from oblique divisions; B club-shaped embryo (embryo
proper above, suspensor below, protoderm around); C a notch on one side marks the shoot apex, the tissue
above it becomes the cotyledon; D the cotyledon grows up as the scutellum against the endosperm, the
coleoptile primordium covers the shoot apex, the epiblast appears opposite the scutellum, the radicle and
coleorhiza appear below; E mature embryo with a schizogenous cavity between radicle and coleorhiza.
"""
import numpy as np
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 9.6)
EMB, SCU, COL, RAD, RHZ, END, SUS = "carbohydrate", "golgi", "chloroplast", "positive", "atp", "cytoplasm", "neutral"
sc = bio.smooth_closed


def patch(pts, tok, lw=0.9, z=6, fill=None):
    pts = np.asarray(pts, float)
    ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fill or P.fill(tok),
                           edgecolor=P.edge(tok), lw=lw, joinstyle="round", zorder=z))


def endosperm(x0, y0, w, h):
    patch(sc([(x0, y0), (x0 + w, y0 + 0.2), (x0 + w + 0.2, y0 + h * 0.6), (x0 + w, y0 + h), (x0, y0 + h)], n=120), END,
          z=3, fill=P.light(END), lw=0.6)


def stage(x, letter, text):
    bio.label(ax, (x, 0.45), f"{letter}  {text}", size="normal")


Y = 1.4
# A: four-celled proembryo
x = 2.2
endosperm(x + 0.7, Y, 1.4, 3.5)
q = sc([(x - 0.45, Y + 0.3), (x + 0.45, Y + 0.3), (x + 0.55, Y + 1.0), (x, Y + 1.5), (x - 0.55, Y + 1.0)], n=100)
patch(q, EMB, z=6)
for a, b in (((x - 0.5, Y + 0.65), (x + 0.5, Y + 1.05)), ((x - 0.05, Y + 0.3), (x + 0.15, Y + 0.86)),
             ((x - 0.2, Y + 0.78), (x + 0.05, Y + 1.45))):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(EMB), lw=0.7, zorder=7)
bio.callout(ax, (x - 0.35, Y + 1.0), (x - 1.1, Y + 2.3), "Oblique walls")
bio.label(ax, (x + 1.4, Y + 1.9), "Endosperm", size="small", color=P.muted())
stage(x, "A", "Four-celled")

# B: club-shaped embryo
x = 7.2
endosperm(x + 0.9, Y, 1.4, 4.2)
club = sc([(x - 0.18, Y + 0.2), (x + 0.18, Y + 0.2), (x + 0.22, Y + 1.0), (x + 0.6, Y + 1.7), (x + 0.7, Y + 2.7),
           (x, Y + 3.3), (x - 0.7, Y + 2.7), (x - 0.6, Y + 1.7), (x - 0.22, Y + 1.0)], n=200)
patch(club, EMB, z=6)
ax.plot([x - 0.25, x + 0.25], [Y + 1.2, Y + 1.2], color=P.edge(EMB), lw=0.7, zorder=7)
bio.callout(ax, (x + 0.6, Y + 2.6), (x + 1.4, Y + 4.3), "Embryo proper")
bio.callout(ax, (x - 0.12, Y + 0.6), (x - 1.3, Y + 0.3), "Suspensor")
bio.callout(ax, (x - 0.66, Y + 2.2), (x - 1.5, Y + 3.2), "Protoderm")
stage(x, "B", "Club-shaped")

# C: notch
x = 12.4
endosperm(x + 0.9, Y, 1.4, 4.6)
body = sc([(x - 0.15, Y + 0.2), (x + 0.15, Y + 0.2), (x + 0.3, Y + 1.0), (x + 0.75, Y + 1.8), (x + 0.8, Y + 3.0),
           (x + 0.3, Y + 3.8), (x - 0.4, Y + 3.5), (x - 0.65, Y + 2.9), (x - 0.35, Y + 2.45), (x - 0.7, Y + 2.05),
           (x - 0.55, Y + 1.5), (x - 0.25, Y + 1.0)], n=220)
patch(body, EMB, z=6)
top = sc([(x - 0.4, Y + 2.6), (x + 0.75, Y + 2.3), (x + 0.8, Y + 3.0), (x + 0.3, Y + 3.8), (x - 0.4, Y + 3.5),
          (x - 0.62, Y + 2.95)], n=120)
patch(top, SCU, lw=0.7, z=7)
ax.add_patch(Ellipse((x - 0.38, Y + 2.38), 0.26, 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                     lw=0.6, zorder=8))
bio.callout(ax, (x - 0.45, Y + 2.4), (x - 1.5, Y + 2.0), "Notch: shoot apex")
bio.callout(ax, (x + 0.4, Y + 3.3), (x + 1.3, Y + 5.0), "Future cotyledon")
stage(x, "C", "Notch")

# D: scutellum, coleoptile primordium, epiblast, radicle
x = 17.6
endosperm(x + 1.0, Y, 1.4, 5.4)
scu = sc([(x + 0.2, Y + 0.9), (x + 0.9, Y + 1.6), (x + 1.0, Y + 3.5), (x + 0.7, Y + 5.0), (x + 0.2, Y + 5.2),
          (x + 0.05, Y + 4.2), (x + 0.25, Y + 2.4)], n=200)
patch(scu, SCU, z=6)
axis = sc([(x - 0.15, Y + 0.3), (x + 0.3, Y + 0.4), (x + 0.4, Y + 1.6), (x + 0.3, Y + 3.0), (x - 0.3, Y + 3.2),
           (x - 0.55, Y + 2.2), (x - 0.45, Y + 1.0)], n=200)
patch(axis, EMB, z=7)
col = sc([(x - 0.45, Y + 2.35), (x - 0.55, Y + 3.0), (x - 0.15, Y + 3.45), (x + 0.3, Y + 3.15), (x + 0.2, Y + 2.6),
          (x - 0.1, Y + 2.95), (x - 0.3, Y + 2.6)], n=150)
patch(col, COL, lw=0.7, z=8)
ax.add_patch(Ellipse((x - 0.05, Y + 2.7), 0.24, 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                     lw=0.6, zorder=9))
epi = sc([(x - 0.5, Y + 1.9), (x - 0.95, Y + 2.05), (x - 0.95, Y + 1.7), (x - 0.48, Y + 1.6)], n=60)
patch(epi, SCU, lw=0.6, z=8)
rhz = sc([(x - 0.42, Y + 0.6), (x - 0.4, Y + 1.35), (x + 0.3, Y + 1.35), (x + 0.32, Y + 0.6), (x - 0.05, Y + 0.35)], n=100)
patch(rhz, RHZ, lw=0.6, z=8)
rad = sc([(x - 0.2, Y + 0.75), (x - 0.2, Y + 1.2), (x + 0.12, Y + 1.2), (x + 0.12, Y + 0.75), (x - 0.04, Y + 0.6)], n=80)
patch(rad, RAD, lw=0.6, z=9)
bio.callout(ax, (x + 0.8, Y + 4.4), (x + 1.4, Y + 6.3), "Scutellum")
bio.callout(ax, (x - 0.4, Y + 3.1), (x - 1.5, Y + 4.2), "Coleoptile primordium")
bio.callout(ax, (x - 0.9, Y + 1.85), (x - 1.6, Y + 2.7), "Epiblast")
bio.callout(ax, (x - 0.35, Y + 0.8), (x - 1.6, Y + 0.6), "Radicle and coleorhiza")
stage(x, "D", "Organ primordia")

# E: mature embryo
x = 23.4
endosperm(x + 1.05, Y, 1.5, 6.4)
scu = sc([(x + 0.25, Y + 0.6), (x + 1.0, Y + 1.5), (x + 1.15, Y + 3.8), (x + 0.85, Y + 5.9), (x + 0.3, Y + 6.3),
          (x + 0.1, Y + 5.0), (x + 0.3, Y + 2.6)], n=220)
patch(scu, SCU, z=6)
col = sc([(x - 0.55, Y + 2.9), (x - 0.6, Y + 4.4), (x - 0.15, Y + 5.3), (x + 0.3, Y + 4.4), (x + 0.25, Y + 2.9)], n=150)
patch(col, COL, z=7)
inner = sc([(x - 0.38, Y + 3.0), (x - 0.4, Y + 4.2), (x - 0.15, Y + 4.85), (x + 0.1, Y + 4.2), (x + 0.08, Y + 3.0)], n=150)
patch(inner, EMB, lw=0.6, z=8)
for k, (yy, s) in enumerate(((3.3, -1), (3.7, 1), (4.1, -1))):
    lf = sc([(x - 0.15 + s * 0.08, Y + yy), (x - 0.15 + s * 0.2, Y + yy + 0.35), (x - 0.15 + s * 0.05, Y + yy + 0.55)], n=40)
    patch(lf, "plant", lw=0.5, z=9)
axis = sc([(x - 0.55, Y + 1.7), (x - 0.55, Y + 3.0), (x + 0.3, Y + 3.0), (x + 0.35, Y + 1.7)], n=100)
patch(axis, EMB, z=7)
epi = sc([(x - 0.55, Y + 2.5), (x - 1.05, Y + 2.7), (x - 1.05, Y + 2.3), (x - 0.55, Y + 2.15)], n=60)
patch(epi, SCU, lw=0.6, z=8)
rhz = sc([(x - 0.6, Y + 0.5), (x - 0.6, Y + 1.8), (x + 0.4, Y + 1.8), (x + 0.4, Y + 0.5), (x - 0.1, Y + 0.25)], n=120)
patch(rhz, RHZ, z=8)
patch(sc([(x - 0.42, Y + 0.6), (x - 0.42, Y + 1.7), (x + 0.22, Y + 1.7), (x + 0.22, Y + 0.6), (x - 0.1, Y + 0.42)], n=100),
      RHZ, lw=0.4, z=8.5, fill=P.light("cytoplasm"))
rad = sc([(x - 0.3, Y + 0.75), (x - 0.3, Y + 1.7), (x + 0.1, Y + 1.7), (x + 0.1, Y + 0.75), (x - 0.1, Y + 0.6)], n=100)
patch(rad, RAD, lw=0.6, z=9)
bio.callout(ax, (x + 1.0, Y + 4.6), (x + 1.4, Y + 7.6), "Scutellum")
bio.callout(ax, (x - 0.5, Y + 4.4), (x - 1.6, Y + 6.0), "Coleoptile")
bio.callout(ax, (x - 0.2, Y + 3.9), (x - 1.6, Y + 5.2), "Plumule")
bio.callout(ax, (x - 1.0, Y + 2.5), (x - 1.6, Y + 3.3), "Epiblast")
bio.callout(ax, (x - 0.1, Y + 1.3), (x - 1.6, Y + 1.9), "Radicle")
bio.callout(ax, (x - 0.55, Y + 0.7), (x - 1.6, Y + 0.6), "Coleorhiza")
bio.callout(ax, (x + 0.17, Y + 1.0), (x + 1.4, Y - 0.2), "Cavity")
stage(x, "E", "Mature")
