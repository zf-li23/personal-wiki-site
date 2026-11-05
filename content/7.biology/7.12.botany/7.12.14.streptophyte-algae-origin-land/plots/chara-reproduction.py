"""Reproductive organs of Chara (schematic). A: a node of a branchlet with the oogonium (nucule, above) and
the antheridium (globule, below), each on a stalk cell, and unicellular spine cells. B: oogonium: the egg
is enclosed by five spirally twisted tube cells, capped by five corona cells. C: antheridium in section:
shield cells form the wall; each carries a manubrium bearing head cells and secondary head cells, from
which antheridial filaments grow, one biflagellate sperm per cell. D: germination of the zygote: after
meiosis one haploid nucleus survives; a protonema and a rhizoid grow out, and the protonema forms a new
shoot with nodes and internodes."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 12.6)


def ell(c, rx, ry, a0=0, a1=360, n=80, rot=0.0):
    t = np.radians(np.linspace(a0, a1, n))
    x, y = rx * np.cos(t), ry * np.sin(t)
    r = np.radians(rot)
    return np.c_[c[0] + x * np.cos(r) - y * np.sin(r), c[1] + x * np.sin(r) + y * np.cos(r)]


def oogonium(c, s, z=8):
    x, y = c
    bio.shape(ax, ell(c, 0.55 * s, 0.85 * s), token="chloroplast", lw=1.0, zorder=z)
    for k in range(5):  # spiral tube cells
        t = np.linspace(-0.8, 0.8, 40)
        xs = x + 0.54 * s * np.sqrt(1 - (t / 0.85) ** 2) * np.sin(np.pi * (t * 0.9 + k * 0.4))
        ys = y + t * 0.85 * s
        vis = np.cos(np.pi * (t * 0.9 + k * 0.4)) > 0
        ax.plot(np.where(vis, xs, np.nan), ys, color=P.edge("chloroplast"), lw=0.9, zorder=z + 1)
    for k in range(5):  # corona
        bio.shape(ax, ell((x + (k - 2) * 0.16 * s, y + 0.92 * s), 0.09 * s, 0.12 * s), token="plant", lw=0.6, zorder=z + 2)


def antheridium(c, r, z=8):
    bio.shape(ax, ell(c, r, r), token="drug", lw=1.0, zorder=z)
    for k in range(4):
        a = np.radians(45 + k * 90)
        ax.plot([c[0] + 0.2 * r * np.cos(a), c[0] + r * np.cos(a)], [c[1] + 0.2 * r * np.sin(a), c[1] + r * np.sin(a)],
                color=P.edge("drug"), lw=0.7, zorder=z + 1)


# ---------------- A: node ----------------
bio.panel(ax, "A", (0.2, 12.4))
bio.label(ax, (4.2, 11.9), "Node of a branchlet", size="normal", bold=True)
NY = 5.8
bio.shape(ax, [[0.6, NY - 0.28], [7.8, NY - 0.28], [7.8, NY + 0.28], [0.6, NY + 0.28]], token="plant", lw=1.0, zorder=3)
for xn in (3.6,):
    bio.shape(ax, [[xn - 0.25, NY - 0.38], [xn + 0.25, NY - 0.38], [xn + 0.25, NY + 0.38], [xn - 0.25, NY + 0.38]],
              token="chloroplast", lw=0.9, zorder=4)
    for a in (40, 140, 220, 320):
        r = np.radians(a)
        ax.plot([xn, xn + 0.9 * np.cos(r)], [NY, NY + 0.9 * np.sin(r)], color=P.edge("plant"), lw=1.6, zorder=2)
oogonium((3.6, NY + 2.4), 1.6)
ax.plot([3.6, 3.6], [NY + 0.38, NY + 1.05], color=P.edge("plant"), lw=2.0, zorder=3)
antheridium((3.6, NY - 1.6), 0.75)
ax.plot([3.6, 3.6], [NY - 0.38, NY - 0.85], color=P.edge("plant"), lw=2.0, zorder=3)
bio.callout(ax, (4.4, NY + 2.4), (6.4, NY + 3.6), "Oogonium (nucule)", size="small")
bio.callout(ax, (3.75, NY + 3.85), (6.4, NY + 4.6), "Corona", size="small")
bio.callout(ax, (4.3, NY - 1.6), (6.4, NY - 2.6), "Antheridium (globule)", size="small")
bio.callout(ax, (4.3, NY + 0.6), (6.4, NY + 1.0), "Spine cell", size="small")
bio.callout(ax, (1.4, NY), (1.2, NY - 1.6), "Internode", size="small")
bio.callout(ax, (3.4, NY - 0.3), (2.0, NY - 3.3), "Node", size="small")

# ---------------- B: oogonium ----------------
bio.panel(ax, "B", (9.0, 12.4))
bio.label(ax, (12.4, 11.9), "Oogonium", size="normal", bold=True)
oc = (12.0, 6.2)
bio.shape(ax, ell(oc, 1.45, 2.25), token="chloroplast", lw=1.2, zorder=4)
bio.shape(ax, ell((oc[0], oc[1] - 0.15), 1.0, 1.7), token="ovule", lw=0.9, zorder=5)
bio.nucleus(ax, (oc[0], oc[1] + 0.2), 0.35, pores=6)
for k in range(5):
    t = np.linspace(-1, 1, 60)
    xs = oc[0] + 1.42 * np.sqrt(1 - t ** 2) * np.sin(np.pi * (t * 0.75 + k * 0.4))
    ys = oc[1] + t * 2.2
    vis = np.cos(np.pi * (t * 0.75 + k * 0.4)) > 0.05
    ax.plot(np.where(vis, xs, np.nan), ys, color=P.edge("chloroplast"), lw=1.3, zorder=6)
for k in range(5):
    bio.shape(ax, ell((oc[0] + (k - 2) * 0.32, oc[1] + 2.45), 0.17, 0.24), token="plant", lw=0.8, zorder=7)
ax.plot([oc[0], oc[0]], [oc[1] - 2.25, oc[1] - 2.9], color=P.edge("plant"), lw=2.4, zorder=3)
bio.callout(ax, (oc[0] + 0.6, oc[1] + 2.5), (oc[0] + 1.8, oc[1] + 3.6), "Corona cells (5)", size="small")
bio.callout(ax, (oc[0] + 1.3, oc[1] - 0.6), (oc[0] + 2.0, oc[1] - 2.6), "Tube cells (5, spiral)", size="small")
bio.callout(ax, (oc[0] - 0.2, oc[1] - 0.6), (oc[0] - 2.0, oc[1] - 3.2), "Egg", size="small")
bio.callout(ax, (oc[0], oc[1] - 2.7), (oc[0] - 2.0, oc[1] - 4.1), "Stalk cell", size="small")

# ---------------- C: antheridium section ----------------
bio.panel(ax, "C", (17.0, 12.4))
bio.label(ax, (21.0, 11.9), "Antheridium (section)", size="normal", bold=True)
ac = np.array([21.0, 6.2])
R = 2.6
bio.shape(ax, ell(ac, R, R), token="drug", lw=1.2, zorder=3)
bio.shape(ax, ell(ac, R - 0.35, R - 0.35), token="cytoplasm", lw=0.8, zorder=4)
for k in range(8):
    a = np.radians(22.5 + k * 45)
    d = np.array([np.cos(a), np.sin(a)])
    ax.plot(*np.c_[ac + d * (R - 0.35), ac + d * R], color=P.edge("drug"), lw=0.9, zorder=5)
for k in range(4):
    a = np.radians(45 + k * 90)
    d = np.array([np.cos(a), np.sin(a)])
    p0, p1 = ac + d * (R - 0.35), ac + d * 0.75
    bio.shape(ax, np.vstack([p0 + np.array([-d[1], d[0]]) * 0.12, p1 + np.array([-d[1], d[0]]) * 0.12,
                             p1 - np.array([-d[1], d[0]]) * 0.12, p0 - np.array([-d[1], d[0]]) * 0.12]),
              token="lipid_head", lw=0.8, zorder=6)
    bio.shape(ax, ell(p1, 0.2, 0.2), token="lipid", lw=0.7, zorder=7)
    for j in (-1, 1):
        q = p1 + np.array([-d[1], d[0]]) * 0.3 * j - d * 0.1
        bio.shape(ax, ell(q, 0.12, 0.12), token="lipid", lw=0.6, zorder=7)
        n = np.array([-d[1], d[0]]) * j
        pts = [q + n * 0.12 * (i + 1) + d * 0.18 * np.sin(i * 1.3) for i in range(7)]
        for pt in pts:
            bio.shape(ax, ell(pt, 0.075, 0.075), token="dna", lw=0.4, zorder=6)
bio.callout(ax, ac + np.array([0, R - 0.15]), (ac[0] + 2.2, ac[1] + R + 1.0), "Shield cell", size="small")
p = ac + np.array([np.cos(np.radians(45)), np.sin(np.radians(45))]) * 1.6
bio.callout(ax, p, (ac[0] + 3.4, ac[1] + 1.6), "Manubrium", size="small")
p = ac + np.array([np.cos(np.radians(45)), np.sin(np.radians(45))]) * 0.75
bio.callout(ax, p, (ac[0] + 3.4, ac[1] + 0.4), "Head cell", size="small")
p = ac + np.array([np.cos(np.radians(-45)), np.sin(np.radians(-45))]) * 0.75 + np.array([0.3, 0.3]) * 1.2
bio.callout(ax, p, (ac[0] + 3.4, ac[1] - 1.8), "Antheridial filament\n(1 sperm per cell)", size="small")

# ---------------- D: germination ----------------
bio.panel(ax, "D", (26.4, 12.4))
bio.label(ax, (30.2, 11.9), "Zygote germination", size="normal", bold=True)
zc = (28.4, 3.0)
bio.shape(ax, ell(zc, 0.55, 0.85), token="animal", lw=1.2, zorder=5)
for k in range(4):
    t = np.linspace(-1, 1, 30)
    ax.plot(zc[0] + 0.5 * np.sin(np.pi * (t * 0.7 + k * 0.5)), zc[1] + t * 0.8, color=P.edge("animal"), lw=0.8, zorder=6)
xs = np.r_[zc[0] + 0.3, zc[0] + 1.0, zc[0] + 1.6, zc[0] + 2.0]
ys = np.r_[zc[1] + 0.8, zc[1] + 1.8, zc[1] + 3.0, zc[1] + 4.2]
ax.plot(xs, ys, color=P.edge("chloroplast"), lw=3.0, zorder=4)
ax.plot([zc[0] - 0.2, zc[0] - 0.9, zc[0] - 1.1], [zc[1] - 0.8, zc[1] - 1.6, zc[1] - 2.4], color=P.muted(), lw=1.6, zorder=4)
top = np.array([xs[-1], ys[-1]])
for k in range(3):
    y = top[1] + 0.9 + k * 1.1
    ax.plot([top[0], top[0]], [y - 1.1, y], color=P.edge("plant"), lw=2.2, zorder=4)
    for a in (20, 160, 60, 120):
        r = np.radians(a)
        ax.plot([top[0], top[0] + 0.7 * np.cos(r)], [y, y + 0.5 * np.sin(r)], color=P.edge("plant"), lw=1.2, zorder=4)
bio.callout(ax, zc, (zc[0] - 1.4, zc[1] + 1.8), "Zygote", size="small")
bio.callout(ax, (xs[1], ys[1]), (xs[1] + 1.4, ys[1] - 0.4), "Protonema", size="small")
bio.callout(ax, (zc[0] - 0.9, zc[1] - 1.6), (zc[0] + 1.4, zc[1] - 2.0), "Rhizoid", size="small")
bio.callout(ax, (top[0], top[1] + 2.0), (top[0] + 1.4, top[1] + 2.6), "New shoot", size="small")
