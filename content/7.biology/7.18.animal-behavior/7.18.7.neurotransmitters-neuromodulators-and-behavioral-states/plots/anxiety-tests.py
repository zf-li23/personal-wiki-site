"""Apparatus for anxiety-like behavior: elevated plus maze, and open-field tracks from a random walk
with a bias toward the walls (thigmotaxis). Arena = unit square; center = inner square 0.25..0.75."""
import numpy as np
from matplotlib.patches import Rectangle

import wikibehav as wb
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 10)
wb.plus_maze(ax, (4.8, 4.8), arm=3.0, width=0.8, closed=(1, 3))
bio.panel(ax, "A", (0.3, 9.7))
bio.label(ax, (4.8, 0.5), "Elevated plus maze", size="small")


def walk(bias, steps=6000, seed=0):
    rng = np.random.default_rng(seed)
    p = np.array([0.5, 0.5]); h = 0.0; out = [p.copy()]
    for _ in range(steps):
        # direction to the nearest wall
        d = np.array([p[0], 1 - p[0], p[1], 1 - p[1]])
        k = int(np.argmin(d))
        wall = [np.pi, 0.0, -np.pi / 2, np.pi / 2][k]
        h += rng.normal(0, 0.45) + bias * np.sin(wall - h) * (0.5 - d[k]) * 2
        step = 0.012 * np.array([np.cos(h), np.sin(h)])
        q = p + step
        for i in range(2):
            if q[i] < 0.01 or q[i] > 0.99:
                step[i] = -step[i]
                h = np.arctan2(step[1], step[0])
        p = np.clip(p + step, 0.01, 0.99); out.append(p.copy())
    return np.array(out)


for j, (bias, title, letter) in enumerate([(0.25, "Strong thigmotaxis", "B"), (0.0, "Weak thigmotaxis", "C")]):
    x0, y0, s = 10.5 + j * 8.3, 1.4, 7.2
    tr = walk(bias, seed=2 + j)
    ax.add_patch(Rectangle((x0, y0), s, s, facecolor=P.fill("extracellular"), edgecolor=P.ink(), lw=1.6, zorder=3))
    ax.add_patch(Rectangle((x0 + s / 4, y0 + s / 4), s / 2, s / 2, fill=False, edgecolor=P.muted(), lw=0.9, ls="--", zorder=4))
    ax.plot(x0 + tr[:, 0] * s, y0 + tr[:, 1] * s, color=P.edge("rna"), lw=0.5, alpha=0.8, zorder=5)
    inside = np.mean((np.abs(tr[:, 0] - 0.5) < 0.25) & (np.abs(tr[:, 1] - 0.5) < 0.25))
    bio.panel(ax, letter, (x0 - 0.2, 9.7))
    bio.label(ax, (x0 + s / 2, 9.2), title, size="small")
    bio.label(ax, (x0 + s / 2, 0.75), f"time in center: {inside * 100:.0f} %", size="small")
