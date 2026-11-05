"""Thickening of storage roots (schematic transverse sections). A: carrot, mostly secondary phloem
with a small secondary-xylem core; B: radish, mostly secondary xylem with scattered tertiary vascular
strands from supernumerary cambia; C: sugar beet, concentric rings of supernumerary cambia alternating
vascular and parenchyma rings; D: sweet potato root tuber, many supernumerary cambia around vessel
groups scattered in the xylem parenchyma. A cross marks the primary xylem (diarch; polyarch in D).
"""

import math

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28.0, 9.0)
XY, PH, CAM, PAR, PER = "xylem", "phloem", "cambium", "parenchyma", "cork"
rng = np.random.default_rng(2)


def disc(c, r, tk, z, light=False, lw=1.0):
    ax.add_patch(Circle(c, r, facecolor=P.light(tk) if light else P.fill(tk), edgecolor=P.edge(tk), lw=lw, zorder=z))


def ring(c, r, tk, z, lw=1.6, dashed=False):
    ax.add_patch(Circle(c, r, fill=False, edgecolor=P.edge(tk), lw=lw, zorder=z, ls=(0, (3, 2)) if dashed else "-"))


def cross(c, s, n=2):
    for k in range(n):
        a = math.pi * k / n
        u = np.array([math.cos(a), math.sin(a)]) * s
        ax.plot([c[0] - u[0], c[0] + u[0]], [c[1] - u[1], c[1] + u[1]], color=P.edge(XY), lw=2.2, zorder=9)


def small_bundle(c, r):
    disc(c, r * 1.6, PH, 7, light=True, lw=0.6)
    disc(c, r, XY, 7.5, lw=0.6)
    ring(c, r * 1.15, CAM, 7.6, lw=0.8)


R = 3.0
cs = [(3.6, 4.6), (10.6, 4.6), (17.6, 4.6), (24.6, 4.6)]
titles = ["Carrot", "Radish", "Sugar beet", "Sweet potato"]
for k, (c, t) in enumerate(zip(cs, titles)):
    bio.panel(ax, "ABCD"[k], (c[0] - 3.4, 8.8))
    bio.label(ax, (c[0], 8.55), t, size="title", va="top")
    disc(c, R, PER, 3)
# A carrot
c = cs[0]
disc(c, R * 0.95, PH, 4)
ring(c, R * 0.42, CAM, 6)
disc(c, R * 0.42, XY, 5, light=True)
cross(c, 0.5)
bio.callout(ax, (c[0] + 1.9, c[1] + 1.3), (c[0] + 1.5, 0.9), "Secondary phloem", size="small")
bio.callout(ax, (c[0] - 0.6, c[1] - 0.6), (c[0] - 1.6, 0.4), "Xylem core", size="small")
# B radish
c = cs[1]
disc(c, R * 0.95, PH, 4, light=True)
disc(c, R * 0.84, XY, 4.2, light=True)
ring(c, R * 0.86, CAM, 6)
for _ in range(16):
    rr, a = R * 0.72 * math.sqrt(rng.uniform(0.08, 1)), rng.uniform(0, 2 * math.pi)
    small_bundle((c[0] + rr * math.cos(a), c[1] + rr * math.sin(a)), 0.13)
cross(c, 0.4)
bio.callout(ax, (c[0] + 2.0, c[1] - 1.85), (c[0] + 1.6, 0.9), "Thin phloem", size="small")
bio.callout(ax, (c[0] - 1.2, c[1] - 1.0), (c[0] - 1.6, 0.4), "Xylem parenchyma", size="small")
# C beet
c = cs[2]
rs = np.linspace(R * 0.92, R * 0.3, 6)
for i, r in enumerate(rs):
    disc(c, r, PAR if i % 2 == 0 else PH, 4 + i * 0.1, light=(i % 2 == 0))
    n = int(2 * math.pi * r / 0.55)
    for j in range(n):
        a = 2 * math.pi * (j + 0.5 * (i % 2)) / n
        if i % 2 == 1:
            p = (c[0] + (r - 0.12) * math.cos(a), c[1] + (r - 0.12) * math.sin(a))
            ax.add_patch(Circle(p, 0.11, facecolor=P.fill(XY), edgecolor=P.edge(XY), lw=0.4, zorder=6))
    if i % 2 == 1:
        ring(c, r - 0.25, CAM, 6.5, lw=1.0, dashed=True)
disc(c, R * 0.22, XY, 6, light=True)
cross(c, 0.35)
bio.callout(ax, (c[0] + rs[1] * 0.7, c[1] + rs[1] * 0.7), (c[0] + 1.4, 0.9), "Vascular ring", size="small")
bio.callout(ax, (c[0] - rs[2] * 0.75, c[1] - rs[2] * 0.6), (c[0] - 1.7, 0.4), "Parenchyma ring", size="small")
# D sweet potato
c = cs[3]
disc(c, R * 0.95, PH, 4, light=True)
ring(c, R * 0.8, CAM, 6)
disc(c, R * 0.78, PAR, 4.5, light=True)
for _ in range(22):
    rr, a = R * 0.68 * math.sqrt(rng.uniform(0.1, 1)), rng.uniform(0, 2 * math.pi)
    small_bundle((c[0] + rr * math.cos(a), c[1] + rr * math.sin(a)), 0.12)
cross(c, 0.4, n=3)
bio.callout(ax, (c[0] + 0.8, c[1] + 1.2), (c[0] + 1.3, 0.9), "Vessel group + cambium", size="small")
bio.callout(ax, (c[0] - 2.5, c[1] - 0.6), (c[0] - 1.7, 0.4), "Main cambium", size="small")
