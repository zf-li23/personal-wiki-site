"""Koch's postulates as a four-step experiment: observe the pathogen in diseased (not healthy) animals,
isolate it in pure culture, inoculate a healthy animal, and reisolate the same organism."""
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(30, 11)


def field(c, r, n, seed, empty=False):
    """A microscope field of view with rod-shaped bacteria among red blood cells."""
    ax.add_patch(Circle(c, r, facecolor=P.fill("extracellular"), edgecolor=P.ink(), lw=1.2, zorder=3))
    rng = np.random.default_rng(seed)
    for _ in range(7):
        a, d = rng.uniform(0, 2 * np.pi), rng.uniform(0, r - 0.35)
        ax.add_patch(Circle((c[0] + d * np.cos(a), c[1] + d * np.sin(a)), 0.22, facecolor=P.fill("blood"),
                            edgecolor=P.edge("blood"), lw=0.6, zorder=4))
    if not empty:
        for _ in range(n):
            a, d = rng.uniform(0, 2 * np.pi), rng.uniform(0, r - 0.3)
            M.bacillus(ax, (c[0] + d * np.cos(a), c[1] + d * np.sin(a)), 0.3, 0.1, angle=rng.uniform(0, 180),
                       token="bacterium", zorder=6)


def plate(c, r=1.3, seed=0):
    """An agar plate with a streak pattern ending in isolated colonies of one kind (a pure culture)."""
    ax.add_patch(Circle(c, r, facecolor=P.fill("cytoplasm"), edgecolor=P.ink(), lw=1.2, zorder=3))
    ax.add_patch(Circle(c, r - 0.1, facecolor="none", edgecolor=P.muted(), lw=0.6, zorder=3.5))
    rng = np.random.default_rng(seed)
    # dense first streak (top-left) thinning to isolated colonies (bottom-right)
    for k, (cx, cy, n, spread) in enumerate([(-0.45, 0.45, 26, 0.32), (0.35, 0.35, 12, 0.3), (0.2, -0.45, 6, 0.35)]):
        for _ in range(n):
            x = c[0] + cx + rng.normal(0, spread * 0.6)
            y = c[1] + cy + rng.normal(0, spread * 0.4)
            if np.hypot(x - c[0], y - c[1]) < r - 0.25:
                ax.add_patch(Circle((x, y), 0.07 + 0.03 * k, facecolor=P.fill("bacterium"),
                                    edgecolor=P.edge("bacterium"), lw=0.5, zorder=5))


def step(x, n, text):
    ax.add_patch(Circle((x, 10.2), 0.33, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), zorder=8))
    bio.label(ax, (x, 10.2), str(n), size="small", bold=True, color=P.on_fill())
    bio.label(ax, (x, 0.75), text, size="small")


# 1: diseased vs healthy animal
step(3.6, 1, "Pathogen present in every\ndiseased animal, absent\nfrom healthy ones")
bio.icon(ax, "servier/mouse", at=(2.0, 8.2), height=1.4)
bio.label(ax, (2.0, 7.2), "diseased", size="tiny", color=P.muted())
bio.icon(ax, "servier/mouse", at=(5.2, 8.2), height=1.4)
bio.label(ax, (5.2, 7.2), "healthy", size="tiny", color=P.muted())
field((2.0, 4.6), 1.35, 9, 1)
field((5.2, 4.6), 1.35, 0, 2, empty=True)
bio.arrow(ax, (2.0, 6.95), (2.0, 6.1), kind="process")
bio.arrow(ax, (5.2, 6.95), (5.2, 6.1), kind="process")
bio.label(ax, (3.6, 2.6), "microscopy and staining", size="tiny", color=P.muted())
# 2: pure culture
step(11.0, 2, "Isolated and grown\nin pure culture")
plate((11.0, 5.2), seed=1)
bio.label(ax, (11.0, 2.6), "streak plate; pick one colony", size="tiny", color=P.muted())
bio.arrow(ax, (6.9, 5.2), (9.2, 5.2), kind="process")
# 3: inoculation
step(18.4, 3, "Cells of the pure culture\ncause the disease in a\nhealthy animal")
bio.icon(ax, "servier/mouse", at=(18.4, 5.6), height=1.8)
bio.label(ax, (18.4, 4.2), "becomes diseased", size="tiny", color=P.muted())
bio.arrow(ax, (12.8, 5.2), (16.6, 5.4), kind="process")
bio.label(ax, (14.7, 5.85), "inoculate", size="tiny", color=P.muted())
# 4: reisolation
step(25.8, 4, "Same organism reisolated\nand identical to the\noriginal isolate")
plate((25.8, 5.2), seed=2)
bio.arrow(ax, (20.3, 5.4), (24.0, 5.2), kind="process")
bio.label(ax, (22.2, 5.85), "reisolate", size="tiny", color=P.muted())
bio.label(ax, (25.8, 2.6), "compare with step 2", size="tiny", color=P.muted())
