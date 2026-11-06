"""Stele types in transverse section (schematic). Xylem blue, phloem orange, ground tissue and pith pale,
endodermis as a dark line. Solid arrows: the classical sequence of the stelar theory; dashed arrow: the
eustele evolved from a protostele (via progymnosperms), not from fern siphonosteles."""
import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 15.4)
XF, XE = P.fill("xylem"), P.edge("xylem")
PF, PE = P.fill("phloem"), P.edge("phloem")
GF, GE = P.light("parenchyma"), P.edge("parenchyma")
EN = P.edge("endodermis")
R = 2.0


def stem(c):
    ax.add_patch(Circle(c, R, facecolor=GF, edgecolor=GE, lw=1.0, zorder=2))


def disc(c, r, fc, ec, z=4):
    ax.add_patch(Circle(c, r, facecolor=fc, edgecolor=ec, lw=0.8, zorder=z))


def ring(c, r0, r1, fc, ec, z=4, a0=0, a1=360):
    ax.add_patch(Wedge(c, r1, a0, a1, width=r1 - r0, facecolor=fc, edgecolor=ec, lw=0.8, zorder=z))


def endo(c, r, z=6):
    ax.add_patch(Circle(c, r, fill=False, edgecolor=EN, lw=1.3, zorder=z))


def bundle(c, xy, r, kind="amphicribral", z=5, ang=0.0):
    x, y = c[0] + xy[0], c[1] + xy[1]
    if kind == "amphicribral":
        ax.add_patch(Circle((x, y), r, facecolor=PF, edgecolor=PE, lw=0.7, zorder=z))
        ax.add_patch(Ellipse((x, y), r * 1.1, r * 0.75, angle=ang, facecolor=XF, edgecolor=XE, lw=0.7, zorder=z + 1))
        ax.add_patch(Circle((x, y), r * 1.12, fill=False, edgecolor=EN, lw=0.9, zorder=z + 1))
    else:  # collateral: phloem outward
        d = np.array([xy[0], xy[1]]) / (np.hypot(*xy) or 1)
        ax.add_patch(Circle((x, y), r, facecolor=XF, edgecolor=XE, lw=0.7, zorder=z))
        px, py = x + d[0] * r * 0.85, y + d[1] * r * 0.85
        ax.add_patch(Ellipse((px, py), r * 1.5, r * 0.8, angle=np.degrees(np.arctan2(d[1], d[0])) + 90, facecolor=PF,
                             edgecolor=PE, lw=0.7, zorder=z + 1))


def title(c, t, sub=None):
    bio.label(ax, (c[0], c[1] - R - 0.45), t, size="small", bold=True)
    if sub:
        bio.label(ax, (c[0], c[1] - R - 0.95), sub, size="tiny", color=P.muted(), italic=True)


xs = [2.6 + 6.2 * i for i in range(5)]
y1, y2 = 11.6, 4.0
# --- top row
c = (xs[0], y1); stem(c); disc(c, 0.95, PF, PE); disc(c, 0.6, XF, XE); endo(c, 1.02); title(c, "Haplostele", "Rhynia")
c = (xs[1], y1); stem(c); disc(c, 1.05, PF, PE)
star = [(c[0] + (0.95 if k % 2 == 0 else 0.36) * np.cos(np.pi * k / 5 + np.pi / 2),
         c[1] + (0.95 if k % 2 == 0 else 0.36) * np.sin(np.pi * k / 5 + np.pi / 2)) for k in range(10)]
ax.add_patch(Polygon(star, closed=True, facecolor=XF, edgecolor=XE, lw=0.8, zorder=5)); endo(c, 1.12)
title(c, "Actinostele", "Psilotum, Lycopodium")
c = (xs[2], y1); stem(c); disc(c, 1.05, PF, PE)
for dy in (-0.62, -0.2, 0.22, 0.64):
    w = np.sqrt(max(0.0, 0.9 ** 2 - dy ** 2))
    ax.add_patch(Polygon([(c[0] - w, c[1] + dy - 0.1), (c[0] + w, c[1] + dy - 0.1), (c[0] + w, c[1] + dy + 0.1),
                          (c[0] - w, c[1] + dy + 0.1)], facecolor=XF, edgecolor=XE, lw=0.7, zorder=5))
endo(c, 1.12); title(c, "Plectostele", "Lycopodium clavatum")
c = (xs[3], y1); stem(c); ring(c, 0.55, 1.1, PF, PE); ring(c, 0.55, 0.85, XF, XE, z=5); disc(c, 0.55, GF, GE, z=5); endo(c, 1.17)
title(c, "Ectophloic siphonostele", "Osmunda")
c = (xs[4], y1); stem(c); ring(c, 0.38, 1.1, PF, PE); ring(c, 0.6, 0.88, XF, XE, z=5); disc(c, 0.38, GF, GE, z=5)
endo(c, 1.17); endo(c, 0.33); title(c, "Amphiphloic siphonostele", "solenostele: Marsilea")
# --- bottom row
c = (xs[0], y2); stem(c)
for k in range(7):
    a = 2 * np.pi * k / 7
    bundle(c, (1.05 * np.cos(a), 1.05 * np.sin(a)), 0.3, ang=np.degrees(a) + 90)
title(c, "Dictyostele", "meristeles: Polypodium")
c = (xs[1], y2); stem(c)
for k in range(9):
    a = 2 * np.pi * k / 9
    bundle(c, (1.35 * np.cos(a), 1.35 * np.sin(a)), 0.22, ang=np.degrees(a) + 90)
for k in range(4):
    a = 2 * np.pi * k / 4 + 0.4
    bundle(c, (0.55 * np.cos(a), 0.55 * np.sin(a)), 0.26, ang=np.degrees(a) + 90)
title(c, "Polycyclic stele", "Pteridium")
c = (xs[2], y2)
t = np.linspace(0, 2 * np.pi, 400)
rr = R * (1 + 0.05 * np.cos(12 * t))
ax.add_patch(Polygon(np.c_[c[0] + rr * np.cos(t), c[1] + rr * np.sin(t)], facecolor=GF, edgecolor=GE, lw=1.0, zorder=2))
disc(c, 0.75, P.surface(), GE, z=3)
endo(c, 1.15)
for k in range(12):
    a = 2 * np.pi * k / 12
    x, y = c[0] + 0.98 * np.cos(a), c[1] + 0.98 * np.sin(a)
    ax.add_patch(Circle((x, y), 0.15, facecolor=XF, edgecolor=XE, lw=0.6, zorder=5))
    ax.add_patch(Circle((x - 0.08 * np.cos(a), y - 0.08 * np.sin(a)), 0.06, facecolor=P.surface(), edgecolor=XE, lw=0.4, zorder=6))
    a2 = a + np.pi / 12
    ax.add_patch(Circle((c[0] + 1.58 * np.cos(a2), c[1] + 1.58 * np.sin(a2)), 0.17, facecolor=P.surface(), edgecolor=GE, lw=0.5, zorder=4))
title(c, "Arthrostele", "Equisetum")
c = (xs[3], y2); stem(c)
for k in range(10):
    a = 2 * np.pi * k / 10
    bundle(c, (1.05 * np.cos(a), 1.05 * np.sin(a)), 0.2, kind="collateral")
title(c, "Eustele", "dicot stem")
c = (xs[4], y2); stem(c)
rng = np.random.default_rng(4)
pts = []
while len(pts) < 26:
    p = rng.uniform(-1.7, 1.7, 2)
    if np.hypot(*p) < 1.75 and all(np.hypot(*(p - q)) > 0.5 for q in pts):
        pts.append(p)
for p in pts:
    bundle(c, tuple(p), 0.13 if np.hypot(*p) > 1.1 else 0.17, kind="collateral")
title(c, "Atactostele", "monocot stem")

# arrows of the classical sequence
for a, b in [((xs[0] + 2.2, y1), (xs[1] - 2.2, y1)), ((xs[1] + 2.2, y1), (xs[2] - 2.2, y1)), ((xs[2] + 2.2, y1), (xs[3] - 2.2, y1)),
             ((xs[3] + 2.2, y1), (xs[4] - 2.2, y1)), ((xs[0] + 2.2, y2), (xs[1] - 2.2, y2)), ((xs[3] + 2.2, y2), (xs[4] - 2.2, y2))]:
    bio.arrow(ax, a, b, kind="process")
bio.arrow(ax, (xs[4] - 0.6, y1 - 3.45), (xs[0] + 0.9, y2 + 2.3), kind="process", bend=0.0)
bio.arrow(ax, (xs[1] + 0.6, y1 - 3.45), (xs[3] - 0.3, y2 + 2.3), kind="process", dashed=True)
bio.label(ax, (xs[3] + 0.2, y2 + 2.75), "eustele directly from a protostele\n(via progymnosperms)", size="tiny",
          color=P.muted(), ha="left")
# legend
for i, (fc, ec, t) in enumerate([(XF, XE, "Xylem"), (PF, PE, "Phloem"), (GF, GE, "Ground tissue, pith")]):
    ax.add_patch(Circle((1.0 + 4.2 * i, 0.5), 0.2, facecolor=fc, edgecolor=ec, lw=0.7))
    bio.label(ax, (1.35 + 4.2 * i, 0.5), t, size="small", ha="left")
ax.plot([13.6, 14.2], [0.5, 0.5], color=EN, lw=1.3)
bio.label(ax, (14.4, 0.5), "Endodermis", size="small", ha="left")
