# Five ventilation mechanisms of tetrapod lungs, schematic lateral views (anterior to the left). Thick arrows:
# movement of the pump; thin blue arrows: airflow during inspiration. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25, 10.2)
AIR = P.edge("dna")
MOV = P.edge("muscle")


def body(x0, y0, w=6.4, h=2.6):
    v = vs.smooth([(x0, y0 + h * 0.55), (x0 + 0.6, y0 + h * 0.95), (x0 + w * 0.5, y0 + h), (x0 + w, y0 + h * 0.7),
                   (x0 + w * 1.02, y0 + h * 0.3), (x0 + w * 0.5, y0), (x0 + 0.6, y0 + h * 0.1)])
    bio.shape(ax, v, token="animal", zorder=2)


def lung(c, rx, ry):
    bio.shape(ax, vs.oval(c, rx, ry), token="er", zorder=4, lw=0.8)


def move(a, b):
    bio.arrow(ax, a, b, kind="process", color=MOV, lw=2.4, head=0.22)


def air(a, b, bend=0.0):
    bio.arrow(ax, a, b, kind="process", color=AIR, lw=1.2, head=0.16, bend=bend)


def title(x, y, s):
    bio.label(ax, (x, y), s, size="small", ha="left")


# A frog buccal pump
x0, y0 = 0.6, 6.2
title(x0, 9.7, "A  Frog: buccal pump (positive pressure)")
body(x0, y0)
mouth = vs.smooth([(x0 + 0.3, y0 + 1.3), (x0 + 1.5, y0 + 1.8), (x0 + 2.5, y0 + 1.4), (x0 + 1.4, y0 + 0.8)])
bio.shape(ax, mouth, token="extracellular", zorder=3)
lung((x0 + 3.9, y0 + 1.5), 1.3, 0.55)
move((x0 + 1.4, y0 + 0.2), (x0 + 1.4, y0 + 0.75))
air((x0 + 0.1, y0 + 2.3), (x0 + 0.7, y0 + 1.7))
air((x0 + 2.4, y0 + 1.5), (x0 + 3.0, y0 + 1.5))
bio.label(ax, (x0 + 1.4, y0 - 0.3), "floor of mouth rises, nostrils closed", size="tiny")

# B lizard costal aspiration
x0 = 8.9
title(x0, 9.7, "B  Lizard: costal aspiration")
body(x0, y0)
lung((x0 + 3.3, y0 + 1.5), 1.6, 0.55)
for k in range(5):
    xr = x0 + 2.1 + 0.6 * k
    ax.plot([xr, xr - 0.25], [y0 + 2.4, y0 + 0.35], color=vs.edge("rib"), lw=2.0, zorder=5)
move((x0 + 3.3, y0 + 0.35), (x0 + 3.3, y0 - 0.3))
air((x0 - 0.2, y0 + 1.9), (x0 + 1.7, y0 + 1.6))
bio.label(ax, (x0 + 3.3, y0 - 0.6), "ribs swing outward, lungs fill by suction", size="tiny")

# C crocodylian hepatic piston
x0 = 17.4
title(x0, 9.7, "C  Crocodylian: hepatic piston")
body(x0, y0)
lung((x0 + 2.2, y0 + 1.6), 1.2, 0.55)
bio.shape(ax, vs.oval((x0 + 3.9, y0 + 1.3), 0.6, 0.65), token="mitochondrion", zorder=4, lw=0.8)
ax.plot([x0 + 4.4, x0 + 5.9], [y0 + 1.0, y0 + 0.4], color=MOV, lw=3.0, zorder=5)
move((x0 + 4.6, y0 + 1.9), (x0 + 5.6, y0 + 1.9))
air((x0 - 0.2, y0 + 1.9), (x0 + 0.9, y0 + 1.7))
bio.label(ax, (x0 + 3.9, y0 + 1.3), "liver", size="tiny", color=P.on_fill())
bio.label(ax, (x0 + 3.2, y0 - 0.3), "diaphragmaticus pulls the liver back", size="tiny")

# D bird air sacs
x0, y0 = 4.0, 1.2
title(x0, 4.7, "D  Bird: air-sac bellows")
body(x0, y0)
bio.shape(ax, np.array([(x0 + 2.3, y0 + 1.9), (x0 + 3.9, y0 + 1.9), (x0 + 3.9, y0 + 2.4), (x0 + 2.3, y0 + 2.4)]), token="er",
          zorder=4, lw=0.8)
for c in ((x0 + 1.5, y0 + 1.4), (x0 + 4.6, y0 + 1.5), (x0 + 5.4, y0 + 1.1)):
    bio.shape(ax, vs.oval(c, 0.55, 0.45), token="vesicle", zorder=3, lw=0.7)
ax.plot([x0 + 1.0, x0 + 4.6], [y0 + 0.35, y0 + 0.2], color=vs.edge("sternum"), lw=3.0, zorder=5)
move((x0 + 3.0, y0 + 0.15), (x0 + 2.6, y0 - 0.45))
air((x0 - 0.2, y0 + 2.1), (x0 + 2.2, y0 + 2.15))
bio.label(ax, (x0 + 3.0, y0 - 0.75), "sternum moves down and forward; rigid lung", size="tiny")

# E mammal diaphragm
x0 = 14.0
title(x0, 4.7, "E  Mammal: diaphragm")
body(x0, y0)
lung((x0 + 2.0, y0 + 1.4), 1.2, 0.7)
th = np.linspace(-1.25, 1.25, 30)
ax.plot(x0 + 3.5 - 0.35 * np.cos(th) + 0.35, y0 + 1.3 + 1.1 * np.sin(th), color=MOV, lw=3.0, zorder=5)
move((x0 + 3.6, y0 + 1.3), (x0 + 4.4, y0 + 1.3))
air((x0 - 0.2, y0 + 1.9), (x0 + 0.85, y0 + 1.6))
bio.label(ax, (x0 + 3.2, y0 - 0.3), "dome flattens, thorax expands", size="tiny")
