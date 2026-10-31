"""Molecular shape and aggregate geometry (schematic). The packing parameter P = v/(a0 l) compares
the volume v of the hydrocarbon chains with the product of the optimal head-group area a0 and the
chain length l. Cone-shaped amphiphiles with one chain and a large head (P < 1/3: detergents,
lysophospholipids) pack into spherical micelles; truncated cones (1/3 < P < 1/2) into cylindrical
micelles; cylinders (P between 1/2 and 1: phosphatidylcholine, sphingomyelin) into bilayers;
inverted cones with small heads (P > 1: phosphatidylethanolamine, diacylglycerol, cardiolipin with
Ca2+) into the inverted hexagonal phase H_II, in which the heads line water channels."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16, 7.4)


def lipid(ax, base, ang, head=0.16, top=0.10, bottom=0.10, length=0.62, zorder=5):
    """One amphiphile: head circle at `base`, tail pointing along angle `ang` (radians).
    `top` and `bottom` are the half-widths of the tail at the head end and at the chain end."""
    b = np.asarray(base, float)
    d = np.array([np.cos(ang), np.sin(ang)])
    n = np.array([-d[1], d[0]])
    p0 = b + d * head * 0.9
    p1 = p0 + d * length
    poly = [p0 + n * top, p1 + n * bottom, p1 - n * bottom, p0 - n * top]
    ax.add_patch(Polygon(poly, closed=True, facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=0.6, zorder=zorder))
    ax.add_patch(Circle(b, head, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=0.6, zorder=zorder + 1))


cols = [(2.2, "P < 1/3", "cone", dict(head=0.22, top=0.06, bottom=0.015)),
        (6.2, "1/2 < P < 1", "cylinder", dict(head=0.16, top=0.11, bottom=0.11)),
        (10.2, "P > 1", "inverted cone", dict(head=0.10, top=0.07, bottom=0.17))]
for x, ptxt, shape, kw in cols:
    lipid(ax, (x, 6.2), -np.pi / 2, length=1.0, **kw)
    bio.label(ax, (x, 6.95), shape, size="normal")
    bio.label(ax, (x, 4.85), ptxt, size="small")

# spherical micelle
c = np.array([2.2, 2.3])
for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    lipid(ax, c + 1.15 * np.array([np.cos(a), np.sin(a)]), a + np.pi, head=0.2, top=0.06, bottom=0.015, length=0.75)
bio.label(ax, (2.2, 0.55), "spherical micelle", size="small")
# bilayer
for x in np.arange(4.9, 7.6, 0.36):
    lipid(ax, (x, 3.25), -np.pi / 2, length=0.72)
    lipid(ax, (x, 1.35), np.pi / 2, length=0.72)
bio.label(ax, (6.2, 0.55), "bilayer", size="small")
# inverted hexagonal phase: three water channels lined by heads
for cx, cy in ((9.4, 2.9), (11.0, 2.9), (10.2, 1.55)):
    ax.add_patch(Circle((cx, cy), 0.28, facecolor=P.fill("extracellular"), edgecolor="none", zorder=3))
    for a in np.linspace(0, 2 * np.pi, 10, endpoint=False):
        lipid(ax, (cx + 0.36 * np.cos(a), cy + 0.36 * np.sin(a)), a, head=0.1, top=0.05, bottom=0.1, length=0.32)
bio.label(ax, (10.2, 0.55), r"inverted hexagonal H$_{\mathrm{II}}$", size="small")

bio.label(ax, (14.0, 5.7), r"$P = \dfrac{v}{a_0\, l}$", size="title")
bio.label(ax, (14.0, 4.4), "v: chain volume", size="small")
bio.label(ax, (14.0, 3.9), "l: chain length", size="small")
bio.label(ax, (14.0, 3.4), r"$a_0$: head-group area", size="small")
bio.arrow(ax, (13.0, 1.8), (15.0, 1.8), kind="process")
bio.label(ax, (14.0, 2.2), "increasing P", size="small")
bio.label(ax, (14.0, 1.35), "positive to negative\nmonolayer curvature", size="tiny")
