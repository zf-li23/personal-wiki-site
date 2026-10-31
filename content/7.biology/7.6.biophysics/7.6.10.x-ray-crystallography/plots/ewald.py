# Real lattice, reciprocal lattice and the Ewald construction in two dimensions.
# A: an oblique real lattice (a = 1.0, b = 1.25, gamma = 105 deg) with its unit cell and the family of
#    lattice planes (1 1) with spacing d_11.
# B: the reciprocal lattice (a* perpendicular to b, b* perpendicular to a, |a*| = 1/(a sin gamma)),
#    the reciprocal vector H_11 perpendicular to the planes (1 1) with |H| = 1/d_11.
# C: the Ewald construction. The crystal sits at C, the incident wave vector s0/lambda ends at the
#    reciprocal origin O, and the sphere (circle) of radius 1/lambda passes through O. The orientation
#    is chosen so that the reciprocal point (2, 1) lies on the sphere; the diffracted beam runs from C
#    through that point. The limiting sphere of radius 2/lambda about O bounds all reflections that can
#    ever be brought into diffraction by rotating the crystal.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

gam = np.deg2rad(105.0)
a = np.array([1.0, 0.0])
b = 1.25 * np.array([np.cos(gam), np.sin(gam)])
area = a[0] * b[1] - a[1] * b[0]
astar = np.array([b[1], -b[0]]) / area
bstar = np.array([-a[1], a[0]]) / area


def arrow(ax, p, q, color, lw=1.6, style="-|>", ms=11, z=5):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, zorder=z,
                                 shrinkA=0, shrinkB=0))


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.8), gridspec_kw={"width_ratios": [1, 1, 1.25]})

# A: real lattice
ax = axs[0]
pts = np.array([i * a + j * b for i in range(-3, 5) for j in range(-2, 4)])
ax.plot(pts[:, 0], pts[:, 1], "o", color=charts.line("protein"), ms=5)
cell = np.array([[0, 0], a, a + b, b])
ax.add_patch(Polygon(cell, closed=True, facecolor=P.fill("protein"), alpha=0.35, edgecolor=P.edge("protein"), lw=1.3,
                     zorder=1))
arrow(ax, (0, 0), tuple(a), ink)
arrow(ax, (0, 0), tuple(b), ink)
ax.text(0.5, -0.22, "a", ha="center", fontsize=11, style="italic", color=ink)
ax.text(b[0] - 0.22, b[1] / 2, "b", ha="center", fontsize=11, style="italic", color=ink)
# planes (1 1): x/a + y/b in fractional coordinates = n, i.e. lines through n*a and n*b ... direction a - b
H = astar + bstar
d11 = 1 / np.linalg.norm(H)
nhat = H / np.linalg.norm(H)
t = np.array([-nhat[1], nhat[0]])
for n in range(-3, 5):
    p0 = n * d11 * nhat
    seg = np.array([p0 - 4 * t, p0 + 4 * t])
    ax.plot(seg[:, 0], seg[:, 1], color=charts.line("highlight"), lw=0.9, ls=(0, (4, 2)), zorder=0)
p1, p2 = 1 * d11 * nhat + 1.55 * t, 2 * d11 * nhat + 1.55 * t
arrow(ax, tuple(p1), tuple(p2), charts.line("highlight"), lw=1.0, style="<|-|>", ms=8)
ax.text(*(0.5 * (p1 + p2) + 0.18 * t + 0.05), r"$d_{11}$", fontsize=10, color=charts.line("highlight"))
ax.set_xlim(-1.6, 2.2)
ax.set_ylim(-1.3, 2.4)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "A", (-1.6, 2.3))
ax.set_title("real lattice and planes (1 1)", fontsize=9, color=ink)

# B: reciprocal lattice
ax = axs[1]
rpts = np.array([h * astar + k * bstar for h in range(-3, 4) for k in range(-3, 4)])
ax.plot(rpts[:, 0], rpts[:, 1], "o", color=charts.line("dna"), ms=5)
arrow(ax, (0, 0), tuple(astar), ink)
arrow(ax, (0, 0), tuple(bstar), ink)
ax.text(*(astar * 0.55 + [0.05, -0.2]), r"$\boldsymbol{a}^*$", fontsize=11, color=ink)
ax.text(*(bstar * 0.55 + [-0.33, 0.0]), r"$\boldsymbol{b}^*$", fontsize=11, color=ink)
arrow(ax, (0, 0), tuple(H), charts.line("highlight"), lw=2.0)
ax.text(*(H + [-1.25, 0.32]), r"$\boldsymbol{H}_{11}$, $|\boldsymbol{H}| = 1/d_{11}$", fontsize=9,
        color=charts.line("highlight"))
for (h, k) in ((1, 0), (0, 1), (-1, 1)):
    p = h * astar + k * bstar
    ax.text(p[0] + 0.06, p[1] - 0.2, f"{h}{k}" if h >= 0 else rf"$\bar{{{-h}}}{k}$", fontsize=7, color=muted)
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "B", (-2.4, 2.3))
ax.set_title("reciprocal lattice", fontsize=9, color=ink)

# C: Ewald construction
ax = axs[2]
R = 2.0                                     # 1/lambda in the units of the reciprocal lattice
Hr = 2 * astar + 1 * bstar
# choose s0 with s0 . H = -|H|^2 / (2R) (H on the sphere); take the solution with s0 roughly along +x
hn = np.linalg.norm(Hr)
cos_t = -hn / (2 * R)
ang_H = np.arctan2(Hr[1], Hr[0])
ang_s0 = ang_H + np.arccos(cos_t)
s0 = np.array([np.cos(ang_s0), np.sin(ang_s0)])
# rotate everything so that s0 points along +x
rot = np.array([[np.cos(-ang_s0), -np.sin(-ang_s0)], [np.sin(-ang_s0), np.cos(-ang_s0)]])
A2, B2 = rot @ astar, rot @ bstar
rp = np.array([h * A2 + k * B2 for h in range(-7, 8) for k in range(-7, 8)])
rp = rp[np.linalg.norm(rp, axis=1) < 4.6]
C = np.array([-R, 0.0])
on = np.abs(np.linalg.norm(rp - C, axis=1) - R) < 0.04
ax.add_patch(Circle((0, 0), 2 * R, fill=False, edgecolor=muted, lw=0.9, ls=(0, (2, 2))))
ax.add_patch(Circle(tuple(C), R, fill=False, edgecolor=charts.line("receptor"), lw=1.6))
ax.plot(rp[:, 0], rp[:, 1], "o", color=charts.line("dna"), ms=3.5, alpha=0.8)
ax.plot(rp[on, 0], rp[on, 1], "o", color=charts.line("highlight"), ms=8, mfc="none", mew=1.8)
Hp = rot @ Hr
arrow(ax, (-2 * R - 0.6, 0), tuple(C), ink, lw=1.2)
arrow(ax, tuple(C), (0, 0), ink, lw=1.6)
arrow(ax, tuple(C), tuple(Hp), charts.line("highlight"), lw=1.6)
arrow(ax, (0, 0), tuple(Hp), charts.line("highlight"), lw=1.0, style="-|>", ms=8)
ax.plot(*C, "o", color=ink, ms=5)
ax.text(C[0] - 0.1, C[1] - 0.38, "C (crystal)", fontsize=8, color=ink, ha="center")
ax.text(0.12, -0.32, "O", fontsize=9, color=ink)
ax.text(-1.2, 0.12, r"$\boldsymbol{s}_0/\lambda$", fontsize=10, color=ink)
mid = 0.5 * (C + Hp)
ax.text(mid[0] - 0.55, mid[1] + 0.25, r"$\boldsymbol{s}/\lambda$", fontsize=10, color=charts.line("highlight"))
ax.text(Hp[0] + 0.25, Hp[1] - 0.35, r"$\boldsymbol{H}_{21}$", fontsize=10, color=charts.line("highlight"))
ax.text(-R + 0.75 * R, 1.08 * R, r"Ewald sphere, radius $1/\lambda$", fontsize=8,
        color=charts.line("receptor"))
ax.text(1.7, -3.95, r"limiting sphere, $2/\lambda$", fontsize=8, color=muted)
ax.set_xlim(-4.8, 4.4)
ax.set_ylim(-4.4, 4.4)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "C", (-4.8, 4.3))
ax.set_title("Ewald construction", fontsize=9, color=ink)

fig.tight_layout()
