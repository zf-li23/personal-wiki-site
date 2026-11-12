# The hypothetical ground plan of wing venation (Comstock-Needham system with the cubital and anal
# veins as recognised today), on a generalized forewing. Longitudinal veins, coloured by family: costa (C),
# subcosta (Sc), radius (R1 and the radial sector Rs with R2-R5), media (M1-M4), anterior cubitus (CuA1,
# CuA2), posterior cubitus (CuP), anal veins (A1-A3) and jugal vein (J). Crossveins (lower case): humeral
# (h), radial (r), radio-medial (r-m), medial (m), medio-cubital (m-cu) and cubito-cubital (cu-a, joining CuA and CuP). The
# claval furrow (along CuP) separates the remigium from the clavus (anal area); the jugal fold
# separates the jugum. Cells take the name of the vein in front of them (e.g. cell R1 behind R1).
import numpy as np
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(25, 12)
S, OX, OY = 1.9, 1.2, 6.0


def T(pts):
    return [(OX + S * x, OY + S * y) for x, y in pts]


outline = smooth_closed(T([(0, 1.5), (3, 1.95), (7, 2.5), (10, 2.55), (10.9, 1.7), (10.6, 0.2), (9.5, -1.2), (7.5, -1.95),
                           (5, -2.35), (2.6, -2.5), (1.1, -2.0), (0.35, -1.2), (0.1, 0.2)]))
bio.shape(ax, outline, "er", lw=1.0, zorder=2)
V = {
    "C": ("neutral", [(0, 1.5), (3, 1.95), (7, 2.5), (10, 2.55)]),
    "Sc": ("channel", [(0.2, 1.25), (2.5, 1.6), (5.6, 2.22)]),
    "R": ("negative", [(0.2, 1.0), (2.5, 1.3)]),
    "R1": ("negative", [(2.5, 1.3), (5.5, 1.85), (8.6, 2.5)]),
    "Rs": ("negative", [(2.5, 1.3), (4.5, 1.0)]),
    "R2+3": ("negative", [(4.5, 1.0), (6.5, 1.3)]),
    "R2": ("negative", [(6.5, 1.3), (8.2, 1.85), (9.55, 2.5)]),
    "R3": ("negative", [(6.5, 1.3), (8.6, 1.45), (10.6, 1.75)]),
    "R4+5": ("negative", [(4.5, 1.0), (6.8, 0.75)]),
    "R4": ("negative", [(6.8, 0.75), (8.8, 0.95), (10.85, 1.05)]),
    "R5": ("negative", [(6.8, 0.75), (8.8, 0.4), (10.65, 0.2)]),
    "M": ("positive", [(0.3, 0.45), (3.8, 0.1)]),
    "M1+2": ("positive", [(3.8, 0.1), (6.0, 0.05)]),
    "M1": ("positive", [(6.0, 0.05), (8.2, -0.15), (10.2, -0.55)]),
    "M2": ("positive", [(6.0, 0.05), (7.8, -0.55), (9.5, -1.2)]),
    "M3+4": ("positive", [(3.8, 0.1), (6.0, -0.6)]),
    "M3": ("positive", [(6.0, -0.6), (7.5, -1.1), (8.6, -1.6)]),
    "M4": ("positive", [(6.0, -0.6), (6.9, -1.2), (7.5, -1.95)]),
    "CuA": ("protein", [(0.3, -0.15), (3.5, -0.75)]),
    "CuA1": ("protein", [(3.5, -0.75), (5.4, -1.4), (6.4, -2.1)]),
    "CuA2": ("protein", [(3.5, -0.75), (4.6, -1.6), (5.0, -2.35)]),
    "CuP": ("drug", [(0.35, -0.45), (2.5, -1.4), (3.8, -2.45)]),
    "A1": ("enzyme", [(0.35, -0.7), (1.6, -1.6), (2.6, -2.5)]),
    "A2": ("enzyme", [(0.33, -0.85), (1.2, -1.6), (1.75, -2.35)]),
    "A3": ("enzyme", [(0.32, -1.0), (0.85, -1.5), (1.15, -2.0)]),
    "J": ("bone", [(0.28, -1.05), (0.45, -1.3), (0.55, -1.55)]),
}
for k, (tok, pts) in V.items():
    p = np.array(T(pts))
    ax.plot(p[:, 0], p[:, 1], color=P.edge(tok), lw=2.2 if k in ("C", "R", "M", "CuA", "Sc") else 1.6, zorder=5,
            solid_capstyle="round")


def at(name, x):
    pts = np.array(V[name][1])
    return np.interp(x, pts[:, 0], pts[:, 1])


cross = [("h", "C", "Sc", 0.9), ("r", "R1", "R2+3", 5.6), ("r-m", "R4+5", "M1+2", 5.0), ("m", "M1+2", "M3+4", 4.8),
         ("m-cu", "M3+4", "CuA1", 4.9), ("cu-a", "CuA", "CuP", 1.5)]
for name, a, b, x in cross:
    pa, pb = T([(x, at(a, x))])[0], T([(x, at(b, x))])[0]
    ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=P.ink(), lw=1.0, zorder=6)
    bio.label(ax, ((pa[0] + pb[0]) / 2 + 0.25, (pa[1] + pb[1]) / 2), name, size="tiny", ha="left", italic=True)
# vein labels at tips
tips = {"Sc": (0.1, 0.18), "R1": (0, 0.18), "R2": (0.1, 0.15), "R3": (0.25, 0), "R4": (0.25, 0), "R5": (0.25, -0.05),
        "M1": (0.25, -0.05), "M2": (0.2, -0.15), "M3": (0.15, -0.2), "M4": (0.05, -0.25), "CuA1": (0.05, -0.25),
        "CuA2": (0, -0.28), "CuP": (0, -0.3), "A1": (0, -0.3), "A2": (-0.05, -0.3), "A3": (-0.2, -0.25), "J": (-0.3, -0.15)}
for k, (dx, dy) in tips.items():
    x, y = V[k][1][-1]
    q = T([(x + dx / S * 2, y + dy / S * 2)])[0]
    bio.label(ax, q, k, size="small", bold=True, color=P.edge(V[k][0]))
q = T([(10.1, 2.85)])[0]
bio.label(ax, q, "C", size="small", bold=True)
# regions
bio.label(ax, T([(1.9, 0.72)])[0], "Remigium", size="small", color=P.muted())
bio.label(ax, T([(2.1, -2.05)])[0], "Clavus", size="tiny", color=P.muted())
bio.callout(ax, T([(0.5, -1.4)])[0], (0.6, 0.9), "Jugum", size="tiny")
bio.callout(ax, T([(3.0, -1.85)])[0], (11.0, 0.5), "Claval furrow (along CuP)", size="tiny")
bio.callout(ax, T([(0.12, 0.5)])[0], (0.3, 11.5), "Axillary area (wing base)", size="tiny")
for txt, xy in (("Costal margin", (5.0, 2.65)), ("Outer margin", (10.4, -0.9))):
    bio.label(ax, T([xy])[0], txt, size="tiny", color=P.muted(), rotation=8 if txt.startswith("Costal") else -55)
