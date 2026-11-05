"""Chlamydomonas reinhardtii: cell structure and life cycle (zygotic meiosis).
A: vegetative cell with two apical flagella, papilla, two contractile vacuoles, cup-shaped chloroplast
with a basal pyrenoid (starch sheath), eyespot in the chloroplast, nucleus in the cup.
B: life cycle on a circle; orange sector haploid, blue sector diploid."""
import numpy as np
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(31, 14)


def ell(c, rx, ry, a0, a1, n=80):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def chlamy(ax, c, s, flag=True, zorder=8):
    """A small Chlamydomonas-type cell of height ~ 2*s (for life-cycle nodes)."""
    x, y = c
    rx, ry = 0.62 * s, 0.8 * s
    bio.shape(ax, ell(c, rx, ry, 0, 360), token="cell_wall", lw=1.0, zorder=zorder)
    cup = np.vstack([ell(c, rx * 0.86, ry * 0.86, 60, -240), ell((x, y + 0.25 * s), rx * 0.48, ry * 0.5, -240, 60)])
    bio.shape(ax, cup, token="chloroplast", lw=0.8, zorder=zorder + 1)
    bio.shape(ax, ell((x, y - 0.55 * s), 0.16 * s, 0.13 * s, 0, 360), token="lipid_tail", lw=0.7, zorder=zorder + 2)
    bio.shape(ax, ell((x + 0.42 * s, y + 0.3 * s), 0.07 * s, 0.11 * s, 0, 360), token="drug", lw=0.5, zorder=zorder + 2)
    if flag:
        for sg in (-1, 1):
            t = np.linspace(0, 1, 30)
            fx = x + sg * (0.1 * s + 0.9 * s * t)
            fy = y + ry + 0.05 * s + 0.9 * s * t + 0.18 * s * np.sin(t * 6)
            ax.plot(fx, fy, color=P.edge("cell_wall"), lw=0.9, zorder=zorder)


# ---------------- A: cell structure ----------------
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (5.6, 13.3), "Vegetative cell", size="normal", bold=True)
c = np.array([5.6, 5.9])
RX, RY = 2.3, 3.2
bio.shape(ax, ell(c, RX + 0.18, RY + 0.18, 0, 360), token="cell_wall", lw=1.2, zorder=3)
bio.shape(ax, ell(c, RX, RY, 0, 360), token="cytoplasm", lw=0.8, zorder=4)
# papilla
bio.shape(ax, ell((c[0], c[1] + RY + 0.2), 0.32, 0.22, 0, 180).tolist() + [[c[0] - 0.32, c[1] + RY + 0.2]], token="cell_wall",
          lw=1.0, zorder=3)
# cup-shaped chloroplast
outer = ell(c, RX * 0.9, RY * 0.9, 55, -235)
inner = ell((c[0], c[1] + 0.75), RX * 0.52, RY * 0.56, -235, 55)
bio.shape(ax, np.vstack([outer, inner]), token="chloroplast", lw=1.0, zorder=5)
for k in range(9):  # thylakoid lines in the cup
    a = np.radians(-200 + k * 25)
    p0 = c + np.array([RX * 0.8 * np.cos(a), RY * 0.8 * np.sin(a)])
    p1 = c + np.array([RX * 0.66 * np.cos(a), RY * 0.7 * np.sin(a)]) + np.array([0, 0.2])
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge("thylakoid"), lw=0.6, zorder=6)
# pyrenoid with starch sheath
pc = (c[0], c[1] - 2.0)
for k in range(10):
    a0 = k * 36 + 4
    arc = np.vstack([ell(pc, 0.62, 0.48, a0, a0 + 28, 12), ell(pc, 0.44, 0.33, a0 + 28, a0, 12)])
    bio.shape(ax, arc, token="lipid_tail", lw=0.6, zorder=7)
bio.shape(ax, ell(pc, 0.4, 0.3, 0, 360), token="enzyme", lw=0.8, zorder=7)
# eyespot (in the chloroplast, anterior side)
bio.shape(ax, ell((c[0] + 1.75, c[1] + 1.35), 0.14, 0.32, 0, 360), token="drug", lw=0.7, zorder=8)
# nucleus in the cup
bio.nucleus(ax, (c[0], c[1] + 0.55), 0.78, pores=8)
# contractile vacuoles
for sx in (-0.45, 0.45):
    bio.shape(ax, ell((c[0] + sx, c[1] + RY - 0.55), 0.24, 0.2, 0, 360), token="vacuole", lw=0.8, zorder=8)
# mitochondria and Golgi
bio.mitochondrion(ax, (c[0] - 0.9, c[1] + 1.9), 0.7, 0.3, angle=60)
bio.golgi(ax, (c[0] + 0.85, c[1] + 2.0), 0.6, cisternae=3, angle=-30)
# flagella
for sg in (-1, 1):
    t = np.linspace(0, 1, 60)
    fx = c[0] + sg * (0.15 + 2.6 * t)
    fy = c[1] + RY + 0.35 + 3.4 * t * (1 - 0.35 * t) + 0.25 * np.sin(t * 9)
    ax.plot(fx, fy, color=P.edge("cell_wall"), lw=1.3, zorder=6, solid_capstyle="round")
bio.callout(ax, (c[0] + 2.0, c[1] + RY + 2.0), (9.9, 12.3), "Flagellum (2, equal, smooth)")
bio.callout(ax, (c[0] + 0.2, c[1] + RY + 0.35), (9.9, 10.8), "Papilla")
bio.callout(ax, (c[0] + 0.45, c[1] + RY - 0.55), (9.9, 9.9), "Contractile vacuoles")
bio.callout(ax, (c[0] + 1.75, c[1] + 1.35), (9.9, 8.3), "Eyespot (in chloroplast)")
bio.callout(ax, (c[0] + 0.85, c[1] + 2.0), (9.9, 9.1), "Golgi body")
bio.callout(ax, (c[0] + 1.85, c[1] - 0.6), (9.9, 5.9), "Cup-shaped chloroplast")
bio.callout(ax, (c[0] + 0.55, c[1] - 2.0), (9.9, 3.8), "Pyrenoid with starch sheath")
bio.callout(ax, (c[0] + RX + 0.12, c[1] - 1.5), (9.9, 2.6), "Glycoprotein cell wall")
bio.callout(ax, (c[0] - 0.4, c[1] + 0.55), (1.0, 7.6), "Nucleus")
bio.callout(ax, (c[0] - 0.9, c[1] + 1.9), (1.0, 10.0), "Mitochondrion")
bio.scale_bar(ax, (1.0, 1.2), 1.6, "5 µm")

# ---------------- B: life cycle ----------------
bio.panel(ax, "B", (14.6, 13.8))
bio.label(ax, (22.6, 13.3), "Life cycle: zygotic meiosis", size="normal", bold=True)


def d_veg(ax, xy, s):
    chlamy(ax, xy, 0.55)


def d_gam(ax, xy, s):
    chlamy(ax, (xy[0] - 0.45, xy[1] - 0.05), 0.4)
    chlamy(ax, (xy[0] + 0.45, xy[1] - 0.05), 0.4)
    bio.label(ax, (xy[0] - 0.45, xy[1] - 0.05), "+", size="tiny", bold=True, zorder=20)
    bio.label(ax, (xy[0] + 0.45, xy[1] - 0.05), "−", size="tiny", bold=True, zorder=20)


def d_zyg(ax, xy, s):
    x, y = xy
    bio.shape(ax, ell(xy, 0.6, 0.5, 0, 360), token="cell_wall", lw=1.0, zorder=8)
    bio.shape(ax, ell(xy, 0.42, 0.34, 0, 360), token="chloroplast", lw=0.8, zorder=9)
    for sg in (-1, 1):
        for dx in (0.08, 0.22):
            t = np.linspace(0, 1, 20)
            ax.plot(x + sg * (dx + 0.6 * t), y + 0.48 + 0.6 * t + 0.08 * np.sin(6 * t), color=P.edge("cell_wall"), lw=0.8, zorder=8)


def d_spore(ax, xy, s):
    x, y = xy
    for k in range(18):
        a = np.radians(k * 20)
        ax.plot([x + 0.55 * np.cos(a), x + 0.72 * np.cos(a)], [y + 0.55 * np.sin(a), y + 0.72 * np.sin(a)],
                color=P.edge("animal"), lw=1.0, zorder=8)
    bio.shape(ax, ell(xy, 0.58, 0.58, 0, 360), token="animal", lw=1.2, zorder=9)
    bio.shape(ax, ell(xy, 0.38, 0.38, 0, 360), token="lipid", lw=0.6, zorder=10)


def d_tetrad(ax, xy, s):
    for dx, dy in ((-0.38, 0.3), (0.38, 0.3), (-0.38, -0.36), (0.38, -0.36)):
        chlamy(ax, (xy[0] + dx, xy[1] + dy), 0.3, flag=False)


def st(t, f, bold=False):
    return dict(text=t, draw=f, icon_size=1.4, size="small", bold=bold)


plant.alternation_of_generations(ax, (22.6, 6.3), 4.0, [
    st("Vegetative cell (n)", d_veg, True), st("Gametes (mt+, mt−)", d_gam), st("Zygote (2n), 4 flagella", d_zyg),
    st("Zygospore (thick wall)", d_spore), st("4 haploid cells", d_tetrad)], meiosis=3, fertilization=1, gap=0.15,
    arrow_labels=["Nitrogen\nstarvation", None, "Rest", None, "Release,\ngrowth"])
# asexual loop at the vegetative cell
top = np.array([22.6, 10.3])
loop = ell((top[0] - 1.9, top[1] + 1.55), 0.9, 0.55, -20, 250, 60)
ax.plot(loop[:, 0], loop[:, 1], color=P.ink(), lw=1.2, zorder=12)
bio.arrow(ax, loop[-3], loop[-1] + np.array([0.15, 0.25]), kind="process", head=0.18)
bio.label(ax, (top[0] - 3.0, top[1] + 1.9), "Mitosis:\n2–16 zoospores", size="small", ha="right")
