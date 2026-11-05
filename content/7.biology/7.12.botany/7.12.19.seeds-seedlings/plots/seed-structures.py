# Seed structure in eudicots and monocots. (A) Bean (Phaseolus vulgaris) opened between the cotyledons:
# exalbuminous seed, food stored in the two cotyledons. (B, C) Castor bean (Ricinus communis), an
# albuminous eudicot seed: (B) ventral view with the caruncle at one end and the raphe along the middle;
# (C) median section parallel to the cotyledons: oily endosperm around a thin, flat embryo with two broad
# veined cotyledons, a short axis and radicle at the caruncle end. (D) Maize grain (Zea mays), a caryopsis:
# pericarp fused with the seed coat, aleurone layer, starchy endosperm and the embryo at one side.
import math

import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
R = PM.ROLE
fig, ax = bio.canvas(36.0, 9.8)
ax.set_ylim(3.2, 13.0)


def patch(pts, role, lw=0.9, z=6, fill=None):
    pts = np.asarray(pts, float)
    return ax.add_patch(PathPatch(Path(np.vstack([pts, pts[:1]]), closed=True), facecolor=fill or P.fill(R.get(role, role)),
                           edgecolor=P.edge(R.get(role, role)), lw=lw, joinstyle="round", zorder=z))


def line(pts, role, lw=0.7, z=7):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(R.get(role, role)), lw=lw, solid_capstyle="round", zorder=z)


def ell(c, rx, ry, n=160, ang=0.0):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    a = math.radians(ang)
    x, y = rx * np.cos(t), ry * np.sin(t)
    return np.c_[c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a)]


# ---- A: bean
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (4.6, 12.1), "Bean (exalbuminous)", size="normal", bold=True)
a = PM.seed(ax, (4.6, 7.2), 5.2, kind="eudicot")
PM.callouts(ax, [(a["seed_coat"], "Seed coat", "right"), (a["cotyledon"], "Cotyledon", "left"),
                 (a["plumule"], "Plumule", "right"), (a["hypocotyl"], "Hypocotyl", "right"),
                 (a["radicle"], "Radicle", "left"), (a["hilum"], "Hilum", "right"), (a["micropyle"], "Micropyle", "left")],
            left=1.4, right=8.0, gap=0.55)

# ---- B: castor bean, ventral view (long axis vertical, caruncle at the top)
bio.panel(ax, "B", (9.6, 12.8))
bio.label(ax, (12.6, 12.1), "Castor bean, ventral view", size="normal", bold=True)
cB = np.array([12.4, 6.8])
outline = bio.smooth_closed([(0, 2.5), (0.95, 2.1), (1.35, 0.9), (1.4, -0.6), (1.05, -1.9), (0.4, -2.55), (-0.4, -2.55),
                             (-1.05, -1.9), (-1.4, -0.6), (-1.35, 0.9), (-0.95, 2.1)], n=240) + cB
patch(outline, "seed_coat", z=5)
rng = np.random.default_rng(3)
for k in range(26):  # mottled testa
    p = cB + np.array([rng.uniform(-1.05, 1.05), rng.uniform(-2.1, 1.8)])
    if np.hypot((p[0] - cB[0]) / 1.25, (p[1] - cB[1] + 0.1) / 2.35) < 0.93:
        b = bio.blob(p, rng.uniform(0.12, 0.3), rng.uniform(0.08, 0.2), wobble=0.2, seed=k, angle=rng.uniform(0, 180))
        ax.add_patch(PathPatch(Path(np.vstack([b, b[:1]]), closed=True), facecolor=P.edge(R["seed_coat"]), edgecolor="none",
                               lw=0, zorder=5.5))
car = bio.smooth_closed([(-0.62, 2.25), (-0.5, 2.75), (0.0, 2.98), (0.5, 2.75), (0.62, 2.25), (0.0, 2.05)], n=120) + cB
patch(car, "highlight", z=6.5)
raphe = np.c_[np.full(30, cB[0]) + 0.05 * np.sin(np.linspace(0, 3, 30)), np.linspace(cB[1] + 2.1, cB[1] - 2.35, 30)]
ax.plot(raphe[:, 0], raphe[:, 1], color=P.ink(), lw=1.6, zorder=6.4, solid_capstyle="round")
PM.callouts(ax, [((cB[0] + 0.3, cB[1] + 2.75), "Caruncle", "right"), ((cB[0] + 0.06, cB[1] - 0.6), "Raphe", "right"),
                 ((cB[0] - 1.2, cB[1] - 0.4), "Seed coat", "left")], left=10.1, right=15.2, gap=0.6)

# ---- C: castor bean, section parallel to the cotyledons
bio.panel(ax, "C", (17.6, 12.8))
bio.label(ax, (20.7, 12.1), "Castor bean, section", size="normal", bold=True)
cC = np.array([20.6, 6.8])
patch(outline - cB + cC, "seed_coat", z=5)
inner = cC + (outline - cB) * 0.9 + np.array([0, -0.05])
patch(inner, "endosperm", z=6)
# one broad, thin cotyledon with palmate veins (the other lies beneath it)
cot = bio.smooth_closed([(0, 1.75), (0.55, 1.4), (0.9, 0.3), (0.85, -0.9), (0.4, -1.75), (0.0, -1.95), (-0.4, -1.75),
                         (-0.85, -0.9), (-0.9, 0.3), (-0.55, 1.4)], n=200) + cC + np.array([0, -0.25])
cot_patch = patch(cot, "embryo", z=7)
base = cC + np.array([0, 1.45])
for ang in (-62, -35, -12, 12, 35, 62):
    t = math.radians(-90 + ang)
    L = 2.6 if abs(ang) < 20 else (2.2 if abs(ang) < 40 else 1.5)
    tip = base + L * np.array([math.cos(t), math.sin(t)])
    mid = base + 0.55 * L * np.array([math.cos(t), math.sin(t)]) + 0.12 * np.sign(ang) * np.array([1, 0])
    tt = np.linspace(0, 1, 30)[:, None]
    v = (1 - tt) ** 2 * base + 2 * (1 - tt) * tt * mid + tt ** 2 * tip  # quadratic Bezier
    (vl,) = ax.plot(v[:, 0], v[:, 1], color=P.edge(R["embryo"]), lw=0.7, zorder=7.5)
    vl.set_clip_path(cot_patch)
# embryo axis (hypocotyl + radicle) between cotyledon base and the micropyle under the caruncle
axis = bio.smooth_closed([(-0.2, 1.4), (-0.17, 2.0), (0.0, 2.25), (0.17, 2.0), (0.2, 1.4)], n=80) + cC
patch(axis, "radicle", z=8)
patch(car - cB + cC, "highlight", z=6.5)
PM.callouts(ax, [((cC[0] + 0.3, cC[1] + 2.75), "Caruncle", "right"), ((cC[0] + 0.0, cC[1] + 2.05), "Radicle", "left"),
                 ((cC[0] + 0.0, cC[1] + 1.6), "Hypocotyl", "left"), ((cC[0] + 0.45, cC[1] - 0.2), "Cotyledon (veined)", "right"),
                 ((cC[0] - 1.05, cC[1] - 1.5), "Endosperm (oily)", "left"), ((cC[0] + 1.28, cC[1] - 1.3), "Seed coat", "right")],
            left=18.2, right=23.3, gap=0.6)

# ---- D: maize grain
bio.panel(ax, "D", (26.4, 12.8))
bio.label(ax, (30.6, 12.1), "Maize grain (caryopsis)", size="normal", bold=True)
d = PM.seed(ax, (30.4, 6.6), 6.0, kind="monocot")
PM.callouts(ax, [(d["pericarp"], "Pericarp + seed coat", "right"), (d["aleurone"], "Aleurone layer", "right"),
                 (d["endosperm"], "Starchy endosperm", "right"), (d["scutellum"], "Scutellum", "right"),
                 (d["coleoptile"], "Coleoptile", "left"), (d["plumule"], "Plumule", "left"),
                 (d["radicle"], "Radicle", "left"), (d["coleorhiza"], "Coleorhiza", "left")],
            left=27.6, right=33.3, gap=0.55)
