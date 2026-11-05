"""Transverse section of a two-needled pine leaf (Pinus massoniana type), schematic, built cell by cell
(wikibio.botany.Section). The flat face is adaxial (lower edge here). From outside: cuticle and
thick-walled epidermis with sunken stomata (guard cells below the surface, substomatal chamber beneath);
hypodermis; plicate mesophyll (wall infoldings drawn as short ridges) with marginal resin ducts (an
epithelium around a lumen); endodermis; transfusion tissue; two vascular bundles (xylem towards the flat
adaxial face, phloem towards the convex abaxial face).
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(31.0, 12.4)
C = np.array([11.0, 1.0])
R = 10.0
E, HY = 0.42, 0.55  # epidermis and hypodermis thickness
EC = C + np.array([0.0, 3.7])  # centre of the endodermis ellipse
EA, EB = 3.9, 2.35  # its semi-axes
DUCTS = [math.radians(a) for a in (22, 58, 90, 122, 158)]
STOMATA = [math.radians(a) for a in (40, 75, 106, 140)]
FLAT_STOMATA = [C[0] - 5.5, C[0] + 5.0]
DUCT_R = 0.55

S = B.Section(seed=7)


def depth(p):
    r = np.hypot(*(p - C).T)
    return np.minimum(R - r, p[:, 1] - C[1])


def ell(p):
    q = (p - EC) / np.array([EA, EB])
    return np.hypot(*q.T)


duct_c = [C + (R - E - HY - DUCT_R - 0.25) * np.array([math.cos(a), math.sin(a)]) for a in DUCTS]
bundles = [EC + np.array([-1.25, -0.25]), EC + np.array([1.25, -0.25])]

# epidermis along the arc and the flat face, with gaps (pores) over the stomata
n = int(math.pi * R / E)
for k in range(n):
    a = (k + 0.5) / n * math.pi
    p = C + (R - E / 2) * np.array([math.cos(a), math.sin(a)])
    if min(abs(a - s) for s in STOMATA) < 0.5 * E / R:
        S.add(p, E, "air")
        for sg in (-1, 1):
            q = C + (R - E - 0.12) * np.array([math.cos(a + sg * 0.16 / R), math.sin(a + sg * 0.16 / R)])
            S.add(q, 0.3, "guard")
        S.add(C + (R - E - 0.75) * np.array([math.cos(a), math.sin(a)]), 0.8, "air")
    else:
        S.add(p, E, "epidermis")
for x in np.arange(C[0] - R + E, C[0] + R - E, E):
    p = np.array([x + E / 2, C[1] + E / 2])
    if min(abs(p[0] - s) for s in FLAT_STOMATA) < 0.5 * E:
        S.add(p, E, "air")
        S.add([[p[0] - 0.16, C[1] + E + 0.12], [p[0] + 0.16, C[1] + E + 0.12]], 0.3, "guard")
        S.add([p[0], C[1] + E + 0.75], 0.8, "air")
    else:
        S.add(p, E, "epidermis")
# hypodermis: one or two layers of small thick-walled cells
S.ring(C, R - E - HY / 2, HY, "hypodermis", arc=(0.02, math.pi - 0.02))
S.row(C[0] - R + E + HY, C[0] + R - E - HY, C[1] + E + HY / 2, HY, "hypodermis")
# resin ducts: epithelium around a lumen
for d in duct_c:
    S.ring(d, DUCT_R + 0.2, 0.38, "epithelium")
    S.add(d, 2 * DUCT_R, "air")
# endodermis ring
m = 34
for k in range(m):
    t = 2 * math.pi * (k + 0.5) / m
    S.add(EC + np.array([EA * math.cos(t), EB * math.sin(t)]), 0.5, "endodermis")
# vascular bundles: xylem towards the flat face (below), phloem towards the arc (above)
for b in bundles:
    S.add(b, 0.5, "cambium")
    for k in range(9):
        S.add(b + np.array([(k % 3 - 1) * 0.3, -0.35 - (k // 3) * 0.28]), 0.27, "xylem")
    for k in range(8):
        S.add(b + np.array([(k % 4 - 1.5) * 0.28, 0.35 + (k // 4) * 0.26]), 0.26, "phloem")


def tissue(pts):
    d = depth(pts)
    e = ell(pts)
    tags, sizes = [], []
    for p, dd, ee in zip(pts, d, e):
        if dd < E + HY + 0.15:
            tags.append(None)
            sizes.append(1)
        elif any(np.hypot(*(p - q)) < DUCT_R + 0.45 for q in duct_c):
            tags.append(None)
            sizes.append(1)
        elif ee > 1.12:
            tags.append("mesophyll")
            sizes.append(0.78)
        elif ee < 0.88:
            near = min(np.hypot(*(p - q)) for q in bundles)
            if near < 1.0:
                tags.append(None)
                sizes.append(1)
            else:
                tags.append("transfusion")
                sizes.append(0.42)
        else:
            tags.append(None)
            sizes.append(1)
    return tags, sizes


S.fill((C[0] - R, C[1], C[0] + R, C[1] + R), tissue, 0.4)
S.mirror_circle(C, R)
S.mirror_line(C[1], above=False)
# clip to the half-disc
t = np.linspace(0, math.pi, 200)
outline = np.vstack([C + R * np.c_[np.cos(t), np.sin(t)], [C + np.array([-R, 0]), C + np.array([R, 0])]])
clip = PathPatch(Path(np.vstack([outline, outline[:1]]), closed=True), fill=False, edgecolor="none")
ax.add_patch(clip)
style = {"transfusion": ("carbohydrate", 0.5, 0.05, 0.4, 0), "epithelium": ("pericycle", 0.6, 0.05, 0, 0),
         "hypodermis": ("sclerenchyma", 0.7, 0.04, 0.5, 0), "epidermis": ("epidermis", 0.9, 0.04, 0.35, 0)}
groups = S.draw(ax, clip=clip, style=style)
# wall infoldings of the plicate mesophyll
rng = np.random.default_rng(3)
segs = []
for poly in groups.get("mesophyll", []):
    cen = poly.mean(axis=0)
    for j in rng.choice(len(poly), 3, replace=False):
        segs.append([poly[j], poly[j] + (cen - poly[j]) * 0.42])
from matplotlib.collections import LineCollection

ax.add_collection(LineCollection(segs, colors=P.edge("plant"), linewidths=0.6, zorder=5.4))
# sunken stomata: pore notch and the pair of guard cells below the surface
for a in STOMATA:
    u = np.array([math.cos(a), math.sin(a)])
    v = np.array([-u[1], u[0]])
    top = C + R * u
    ax.add_patch(Polygon([top + v * 0.22, top - v * 0.22, top - u * (E + 0.05)], closed=True,
                         facecolor=P.surface(), edgecolor="none", zorder=8.5))
    for sg in (-1, 1):
        ax.add_patch(Ellipse(C + (R - E - 0.15) * u + v * sg * 0.17, 0.32, 0.22, angle=math.degrees(a) + 90,
                             facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=0.7, zorder=8.6))
# cuticle
ax.plot(outline[:, 0], outline[:, 1], color=P.edge("lipid"), lw=2.2, zorder=8, solid_joinstyle="round")

X = 23.5


def lab(p, y, text):
    bio.callout(ax, p, (X, y), text)


pts = [
    (C + R * np.array([math.cos(1.0), math.sin(1.0)]), "Cuticle"),
    (S.anchor("epidermis", C + (R - 0.2) * np.array([math.cos(0.9), math.sin(0.9)])), "Epidermis"),
    (C + (R - E - 0.1) * np.array([math.cos(STOMATA[0]), math.sin(STOMATA[0])]), "Sunken stoma"),
    (S.anchor("hypodermis", C + (R - 0.7) * np.array([math.cos(0.6), math.sin(0.6)])), "Hypodermis"),
    (duct_c[0], "Resin duct"),
    (S.anchor("mesophyll", C + np.array([7.0, 2.5])), "Plicate mesophyll"),
    (S.anchor("endodermis", EC + np.array([EA, 0])), "Endodermis"),
    (S.anchor("transfusion", EC + np.array([2.6, 0.6])), "Transfusion tissue"),
    (bundles[1] + np.array([0.0, 0.5]), "Phloem"),
    (bundles[1] + np.array([0.0, -0.6]), "Xylem"),
]
pts.sort(key=lambda t: -t[0][1])
for k, (p, name) in enumerate(pts):
    lab(p, 11.4 - k * 1.08, name)
bio.label(ax, (C[0], 0.45), "Adaxial (flat) face", size="small", color=P.muted())
bio.label(ax, (C[0], 11.7), "Abaxial (convex) face", size="small", color=P.muted())
