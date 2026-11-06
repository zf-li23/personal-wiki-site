# Cellulose microfibril orientation and the direction of cell expansion (schematic, after Taiz et al. 6e,
# Fig. 14.14 and Fig. 18.27). Turgor pushes equally in all directions; the wall yields least along the
# microfibrils, so a cell expands at right angles to them. (A) random microfibrils: isotropic expansion;
# (B) transverse (hoop) microfibrils: elongation; (C) longitudinal microfibrils (after ethylene has turned
# the cortical microtubules by 90 degrees): lateral swelling.
import numpy as np
import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(16.5, 7.2)


def cell(c, w, h, fibrils, seed=0):
    x, y = c
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.22",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=2.6, zorder=4))
    col = P.edge("cell_wall")
    inset = 0.12
    x0, x1, y0, y1 = x - w / 2 + inset, x + w / 2 - inset, y - h / 2 + inset, y + h / 2 - inset
    if fibrils == "transverse":
        for yy in np.arange(y0 + 0.06, y1, 0.17):
            ax.plot([x0, x1], [yy, yy], color=col, lw=0.9, zorder=5)
    elif fibrils == "longitudinal":
        for xx in np.arange(x0 + 0.06, x1, 0.17):
            ax.plot([xx, xx], [y0, y1], color=col, lw=0.9, zorder=5)
    else:
        rng = np.random.default_rng(seed)
        n = int(26 * w * h)
        for _ in range(n):
            px, py = rng.uniform(x0 + 0.1, x1 - 0.1), rng.uniform(y0 + 0.1, y1 - 0.1)
            a = rng.uniform(0, np.pi)
            d = 0.16 * np.array([np.cos(a), np.sin(a)])
            ax.plot([px - d[0], px + d[0]], [py - d[1], py + d[1]], color=col, lw=0.9, zorder=5)


def turgor(c, r=0.42):
    for a in np.radians(np.arange(0, 360, 45)):
        u = np.array([np.cos(a), np.sin(a)])
        bio.arrow(ax, np.asarray(c) + 0.08 * u, np.asarray(c) + r * u, kind="process", color=P.fill("h"), lw=1.1,
                  head=0.13, zorder=7)


def panel(x0, letter, title, fib, after_wh, result):
    bio.panel(ax, letter, (x0 + 0.1, 7.05))
    bio.label(ax, (x0 + 2.7, 6.6), title, size="small", bold=True)
    c0 = (x0 + 1.0, 3.2)
    cell(c0, 1.25, 1.25, fib, seed=1)
    turgor(c0)
    w, h = after_wh
    c1 = (x0 + 3.85, 3.2)
    bio.arrow(ax, (x0 + 1.8, 3.2), (c1[0] - w / 2 - 0.15, 3.2), kind="process")
    cell(c1, w, h, fib, seed=2)
    bio.label(ax, (x0 + 2.7, 0.45), result, size="small")


panel(0.0, "A", "Random microfibrils", "random", (2.0, 2.0), "Isotropic expansion (sphere)")
panel(5.5, "B", "Transverse microfibrils (hoops)", "transverse", (1.35, 5.1), "Elongation along the axis")
panel(11.0, "C", "Longitudinal microfibrils", "longitudinal", (2.6, 1.35), "Lateral expansion (swelling)")
# expansion direction beside each enlarged cell
def double(a, b):
    bio.arrow(ax, a, b, kind="activation", lw=1.1)
    bio.arrow(ax, b, a, kind="activation", lw=1.1)


double((2.85, 4.55), (5.0, 4.55))
double((5.25, 2.2), (5.25, 4.2))
double((10.45, 0.95), (10.45, 5.5))
double((13.55, 4.25), (16.15, 4.25))
bio.label(ax, (2.7, 5.75), "Turgor (pink arrows) is equal in all directions", size="tiny", color=P.muted())
bio.label(ax, (13.7, 5.35), "e.g. after ethylene:\ncortical microtubules turn 90°", size="tiny", color=P.muted())
