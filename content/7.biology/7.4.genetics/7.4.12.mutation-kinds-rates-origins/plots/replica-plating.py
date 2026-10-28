"""Replica plating (Lederberg and Lederberg 1952). A master plate without penicillin carries about 60 colonies; a
sterile velvet pad pressed on it picks up cells from every colony and prints them, in the same arrangement, onto
three replica plates containing penicillin. Only resistant colonies grow on the replicas, and they appear at the
same positions on all three, so the resistant cells were already present on the master plate before any contact
with penicillin. Colony positions are random (fixed seed); the resistant ones are marked on the master plate."""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)

n = 45
r = 1.0 * np.sqrt(rng.uniform(0, 1, n))
t = rng.uniform(0, 2 * np.pi, n)
pts = np.c_[r * np.cos(t), r * np.sin(t)]
resistant = np.zeros(n, bool)
resistant[[4, 17, 30, 41]] = True

fig, ax = bio.canvas(19.0, 7.6)


def plate(cx, cy, R, title, sub, show, mark=False):
    ax.add_patch(Circle((cx, cy), R, facecolor=P.light("extracellular"), edgecolor=P.edge("neutral"), lw=1.2, zorder=3))
    ax.add_patch(Circle((cx, cy), R * 0.93, fill=False, edgecolor=P.edge("neutral"), lw=0.6, zorder=3))
    for (x, y), res in zip(pts, resistant):
        if show == "all" or res:
            tok = "negative" if (mark and res) or (show != "all") else "bacterium"
            ax.add_patch(Circle((cx + x * R * 0.8, cy + y * R * 0.8), 0.075 * R, facecolor=P.fill(tok),
                                edgecolor=P.edge(tok), lw=0.6, zorder=5 if res else 4))
    bio.label(ax, (cx, cy + R + 0.35), title, size="small", bold=True)
    bio.label(ax, (cx, cy - R - 0.4), sub, size="tiny", color=P.muted())


plate(2.2, 3.4, 1.7, "Master plate", "no penicillin: all colonies grow", "all", mark=True)
# velvet pad
ax.add_patch(Circle((7.0, 3.4), 1.3, facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=3,
                    hatch="...."))
bio.label(ax, (7.0, 5.15), "Velvet pad", size="small", bold=True)
bio.label(ax, (7.0, 1.6), "picks up cells of every colony", size="tiny", color=P.muted())
bio.arrow(ax, (4.2, 3.4), (5.5, 3.4))
for k, cx in enumerate((11.0, 14.2, 17.4)):
    plate(cx, 3.4, 1.35, f"Replica {k + 1}", "penicillin", "res")
    bio.arrow(ax, (8.25, 4.0), (cx - 1.2, 4.35), bend=0.06 + 0.07 * k)
bio.label(ax, (14.2, 0.55), "Resistant colonies at the same positions on every replica", size="small")
bio.label(ax, (2.2, 0.55), "red: colonies whose cells are resistant", size="tiny")
