"""The three modes of lung branching (Metzger et al. 2008) and a tree built from them (Algorithm 30.7.1).
A: domain branching: a parent branch sends out daughters in rows along its length, each row in one rotational
domain; planar bifurcation: the tip splits in two, both daughters in the plane of the parent and grandparent
(flat arrays at the edges of the lobes); orthogonal bifurcation: the tip splits in two in a plane rotated 90
degrees about the parent, so that successive generations alternate (filling the interior). B: a deterministic
tree in three dimensions, viewed obliquely: the main bronchus makes two rows of domain branches; each then
bifurcates, planar bifurcations at the periphery of the lobe alternating with orthogonal ones; segment length
and width shrink by a constant factor per generation. A few such subroutines, used in a fixed order, generate
the stereotyped branching of the mouse lung."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(8.8, 4.8))
gs = fig.add_gridspec(3, 2, width_ratios=[0.8, 1.6], hspace=0.6, wspace=0.1, left=0.03, right=0.99, bottom=0.04, top=0.92)
col = charts.line("dna2")
edge = charts.line("dna")


def seg(ax, p, q, w):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=edge, lw=w + 1.2, solid_capstyle="round")
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P_.fill("dna2"), lw=w, solid_capstyle="round")


for r, name in enumerate(("domain branching", "planar bifurcation", "orthogonal bifurcation")):
    a = fig.add_subplot(gs[r, 0])
    a.set_axis_off()
    a.set_aspect("equal")
    if r == 0:
        seg(a, (0, 0), (0, 4), 5)
        for k, y in enumerate((1, 2, 3)):
            seg(a, (0, y), (1.2, y + 0.7), 3)
            seg(a, (0, y + 0.4), (-0.7, y + 1.0), 2.5)
    elif r == 1:
        seg(a, (0, 0), (0, 2), 5)
        for s in (1, -1):
            seg(a, (0, 2), (s * 1.0, 3.2), 3.5)
            for t in (1, -1):
                seg(a, (s * 1.0, 3.2), (s * 1.0 + t * 0.6, 4.1), 2.5)
    else:
        seg(a, (0, 0), (0, 2), 5)
        for s in (1, -1):
            seg(a, (0, 2), (s * 1.0, 3.2), 3.5)
            seg(a, (s * 1.0, 3.2), (s * 1.0, 4.2), 2.0)
            a.plot([s * 1.0], [3.2], "o", ms=5, color=edge, mfc=P_.fill("dna2"))
    a.set_xlim(-2, 2)
    a.set_ylim(-0.3, 4.4)
    a.set_title(name, fontsize=FT["tiny"], color=P_.ink())
fig.text(0.03, 0.95, "A", fontsize=FT["title"], weight="bold", color=P_.ink())


def rot(v, axis, ang):
    axis = axis / np.linalg.norm(axis)
    return v * np.cos(ang) + np.cross(axis, v) * np.sin(ang) + axis * np.dot(axis, v) * (1 - np.cos(ang))


segs = []


def grow(p, d, nrm, L, gen, mode):
    q = p + d * L
    segs.append((p, q, gen))
    if gen >= 7:
        return
    if mode == "domain":
        for k, f in enumerate((0.3, 0.55, 0.8)):
            b = p + d * L * f
            for side, plane in ((1, nrm), (-1, np.cross(d, nrm))):
                dd = rot(d, plane, side * np.radians(60))
                grow(b, dd, np.cross(dd, plane), L * 0.45, gen + 1, "planar" if k % 2 else "orthogonal")
        return
    ang = np.radians(35)
    newn = nrm if mode == "planar" else np.cross(d, nrm)
    for s in (1, -1):
        dd = rot(d, newn, s * ang)
        grow(q, dd, newn, L * 0.78, gen + 1, "orthogonal" if mode == "planar" else "planar")


grow(np.zeros(3), np.array([0, 0, -1.0]), np.array([1.0, 0, 0]), 4.0, 0, "domain")
b = fig.add_subplot(gs[:, 1])
el, az = np.radians(20), np.radians(35)
R = np.array([[np.cos(az), -np.sin(az), 0], [np.sin(az) * np.sin(el), np.cos(az) * np.sin(el), np.cos(el)]])
for p, q, g in sorted(segs, key=lambda s: -s[2]):
    P2, Q2 = R @ p, R @ q
    w = 7.0 * 0.72**g
    b.plot([P2[0], Q2[0]], [P2[1], Q2[1]], color=edge, lw=w + 0.8, solid_capstyle="round")
    b.plot([P2[0], Q2[0]], [P2[1], Q2[1]], color=P_.fill("dna2"), lw=w, solid_capstyle="round")
b.set_aspect("equal")
b.set_axis_off()
b.set_title("B  A tree from the three subroutines (oblique view)", fontsize=FT["small"], color=P_.ink(), loc="left", weight="bold")
