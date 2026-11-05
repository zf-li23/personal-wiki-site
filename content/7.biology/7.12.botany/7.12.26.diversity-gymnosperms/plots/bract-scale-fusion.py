"""The bract-scale complex of conifer seed cones, seen from the cone axis (adaxial side; schematic). The bract
(green) subtends the ovuliferous (seed) scale (brown), a modified short shoot. In Pinaceae bract and scale are
free except at the base and each scale bears two inverted winged seeds; in Araucariaceae they are fused and
bear one seed. In Cupressaceae s.l. fusion increases from Cunninghamia (large bract, small three-lobed scale,
three seeds) and Cryptomeria (scale toothed, only its tip free) to the peltate, completely fused scales of
Taxodium, Sequoia and Cupressus; in Platycladus the fused scales are flat with a hooked tip, and in
Juniperus they become fleshy and coalesce into a berry-like cone."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 10.5)
BR, SC = "plant", "animal"


def poly(pts, tok, lw=0.9, z=6, light=False):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok),
                         lw=lw, joinstyle="round", zorder=z))


def seed(xy, wing=None, z=9, s=1.0):
    x, y = xy
    if wing == "up":
        poly([(x - 0.28 * s, y), (x - 0.35 * s, y + 1.2 * s), (x + 0.3 * s, y + 1.25 * s), (x + 0.28 * s, y)], "bract", lw=0.5, z=z - 1,
             light=True)
    if wing == "side":
        ax.add_patch(Ellipse((x, y), 0.75 * s, 0.5 * s, facecolor=P.light("bract"), edgecolor=P.edge("bract"), lw=0.5, zorder=z - 1))
    ax.add_patch(Ellipse((x, y), 0.36 * s, 0.48 * s, facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.6, zorder=z))


XS = [2.4, 6.9, 11.4, 15.9, 20.4, 24.9, 29.4]
Y = 2.6
# Pinaceae: free bract below, scale with 2 seeds and wings
x = XS[0]
poly([(x - 0.35, Y), (x - 0.6, Y + 2.0), (x, Y + 2.6), (x + 0.6, Y + 2.0), (x + 0.35, Y)], BR, z=5)
poly([(x - 0.4, Y + 0.1), (x - 1.35, Y + 3.3), (x - 1.0, Y + 4.3), (x + 1.0, Y + 4.3), (x + 1.35, Y + 3.3), (x + 0.4, Y + 0.1)], SC,
     z=6)
for dx in (-0.5, 0.5):
    seed((x + dx, Y + 0.9), wing="up")
# Araucariaceae: fused, one seed
x = XS[1]
poly([(x - 0.5, Y), (x - 1.5, Y + 3.2), (x - 0.6, Y + 4.3), (x, Y + 4.7), (x + 0.6, Y + 4.3), (x + 1.5, Y + 3.2), (x + 0.5, Y)], BR,
     z=5)
poly([(x - 0.4, Y + 0.2), (x - 0.75, Y + 2.6), (x + 0.75, Y + 2.6), (x + 0.4, Y + 0.2)], SC, z=6)
seed((x, Y + 1.4), s=1.4)
# Cunninghamia: large bract, small 3-lobed scale fused at base, 3 seeds
x = XS[2]
poly([(x - 0.4, Y), (x - 1.6, Y + 3.0), (x - 0.4, Y + 4.4), (x, Y + 4.9), (x + 0.4, Y + 4.4), (x + 1.6, Y + 3.0), (x + 0.4, Y)], BR,
     z=5)
poly([(x - 0.35, Y + 0.1), (x - 0.95, Y + 1.7), (x - 0.6, Y + 2.0), (x - 0.3, Y + 1.75), (x, Y + 2.05), (x + 0.3, Y + 1.75),
      (x + 0.6, Y + 2.0), (x + 0.95, Y + 1.7), (x + 0.35, Y + 0.1)], SC, z=6)
for dx in (-0.45, 0.0, 0.45):
    seed((x + dx, Y + 0.9), wing="side", s=0.8)
# Cryptomeria: fused except toothed tip; 2-5 seeds
x = XS[3]
poly([(x - 0.4, Y), (x - 1.35, Y + 2.9), (x - 1.0, Y + 3.3), (x + 1.0, Y + 3.3), (x + 1.35, Y + 2.9), (x + 0.4, Y)], BR, z=5)
pts = [(x - 0.4, Y + 0.05), (x - 1.25, Y + 2.8)]
for k in range(5):
    xx = x - 1.0 + 0.5 * k
    pts += [(xx - 0.05, Y + 3.2), (xx + 0.08, Y + 3.9), (xx + 0.25, Y + 3.2)]
pts += [(x + 1.25, Y + 2.8), (x + 0.4, Y + 0.05)]
poly(pts, SC, z=6)
for dx in (-0.6, -0.2, 0.2, 0.6):
    seed((x + dx, Y + 1.0), wing="side", s=0.75)
# Taxodium / Sequoia / Cupressus: peltate, completely fused (shield seen from outside + stalk)
x = XS[4]
poly([(x - 0.25, Y), (x - 0.3, Y + 2.2), (x + 0.3, Y + 2.2), (x + 0.25, Y)], SC, z=5)
poly([(x - 1.35, Y + 2.2), (x - 1.0, Y + 3.6), (x, Y + 4.0), (x + 1.0, Y + 3.6), (x + 1.35, Y + 2.2), (x, Y + 1.85)], SC, z=6)
ax.plot([x - 1.0, x + 1.0], [Y + 2.95, Y + 2.95], color=P.edge(SC), lw=0.6, zorder=7)
ax.plot([x], [Y + 2.95], marker="^", ms=6, color=P.edge(BR), zorder=8)
for dx in (-0.7, -0.35, 0.35, 0.7):
    seed((x + dx, Y + 1.35), wing="side", s=0.7)
# Platycladus: flat, hooked tip, wingless seeds
x = XS[5]
poly([(x - 0.4, Y), (x - 1.1, Y + 3.2), (x - 0.4, Y + 4.0), (x + 0.4, Y + 4.0), (x + 1.1, Y + 3.2), (x + 0.4, Y)], SC, z=6)
ax.plot([x, x + 0.25, x + 0.45], [Y + 3.6, Y + 4.3, Y + 4.15], color=P.edge(BR), lw=2.0, solid_capstyle="round", zorder=8)
for dx in (-0.3, 0.3):
    seed((x + dx, Y + 0.9), s=1.0)
# Juniperus: fleshy coalesced cone
x = XS[6]
ax.add_patch(Circle((x, Y + 2.0), 1.35, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=6))
for a in (90, 210, 330):
    r = np.radians(a)
    ax.plot([x, x + 1.2 * np.cos(r)], [Y + 2.0, Y + 2.0 + 1.2 * np.sin(r)], color=P.edge("dna"), lw=0.6, zorder=7)
    seed((x + 0.6 * np.cos(r + 1.05), Y + 2.0 + 0.6 * np.sin(r + 1.05)), s=0.9)

heads = ["Pinaceae", "Araucariaceae", "Cunninghamia", "Cryptomeria", "Taxodium, Sequoia,\nCupressus", "Platycladus", "Juniperus"]
subs = ["bract free; 2 seeds,\nterminal wing", "fused; 1 seed", "bract large, scale small;\n3 seeds", "fused, tip free and\ntoothed; 2-5 seeds",
        "peltate, fully fused;\n2-9 seeds", "flat, hooked tip;\n1-2 wingless seeds", "fleshy, coalesced;\nberry-like cone"]
for k, (x, h, s) in enumerate(zip(XS, heads, subs)):
    bio.label(ax, (x, 9.7), h, size="normal", bold=True, italic=k >= 2)
    bio.label(ax, (x, 1.35), s, size="small", color=P.muted())
bio.arrow(ax, (XS[2] - 1.5, 0.35), (XS[6] + 1.2, 0.35), kind="process", color=P.muted())
bio.label(ax, (XS[0], 0.35), "Bract (green), seed scale (brown)", size="tiny", color=P.muted())
bio.label(ax, ((XS[2] + XS[6]) / 2, 8.85), "Cupressaceae s.l.: increasing fusion of bract and scale", size="small",
          color=P.edge(SC), bold=True)
