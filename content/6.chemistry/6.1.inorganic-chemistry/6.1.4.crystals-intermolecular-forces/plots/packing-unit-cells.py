"""Unit cells of simple cubic, body-centered cubic, face-centered cubic (ccp) and hexagonal close packing."""

import itertools

import numpy as np
import matplotlib.pyplot as plt

corners = np.array(list(itertools.product([0, 1], repeat=3)), float)
edges = [(a, b) for a, b in itertools.combinations(range(8), 2) if np.sum(np.abs(corners[a] - corners[b])) == 1]
faces = np.array([[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]])


def cube(ax):
    for a, b in edges:
        ax.plot(*zip(corners[a], corners[b]), color="0.5", lw=1)


def atoms(ax, pts, color, size):
    pts = np.asarray(pts)
    ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], s=size, color=color, edgecolors="black", linewidths=0.4, depthshade=True)


def finish(ax, title):
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=18, azim=-62)
    ax.set_axis_off()
    ax.set_title(title, fontsize=10.5)


fig = plt.figure(figsize=(12, 3.6))

ax = fig.add_subplot(1, 4, 1, projection="3d")
cube(ax)
atoms(ax, corners, "C0", 520)
finish(ax, "simple cubic\nCN 6, 1 atom per cell, 52.4%")

ax = fig.add_subplot(1, 4, 2, projection="3d")
cube(ax)
atoms(ax, corners, "C0", 380)
atoms(ax, [[0.5, 0.5, 0.5]], "C1", 380)
finish(ax, "body-centered cubic (bcc)\nCN 8, 2 atoms per cell, 68.0%")

ax = fig.add_subplot(1, 4, 3, projection="3d")
cube(ax)
atoms(ax, corners, "C0", 260)
atoms(ax, faces, "C2", 260)
finish(ax, "face-centered cubic (ccp)\nCN 12, 4 atoms per cell, 74.0%")

ax = fig.add_subplot(1, 4, 4, projection="3d")
c = np.sqrt(8 / 3)  # ideal c/a
ang = np.radians(np.arange(0, 360, 60))
hexagon = np.c_[np.cos(ang), np.sin(ang)]
for z in (0, c):
    ring = np.c_[hexagon, np.full(6, z)]
    for k in range(6):
        ax.plot(*zip(ring[k], ring[(k + 1) % 6]), color="0.5", lw=1)
    for k in range(6):
        ax.plot(*zip([0, 0, z], ring[k]), color="0.5", lw=0.5, ls=":")
for k in range(6):
    ax.plot(*zip([*hexagon[k], 0], [*hexagon[k], c]), color="0.5", lw=1)
layer_a = [[*p, z] for z in (0, c) for p in np.vstack([hexagon, [[0, 0]]])]
mid = np.radians([30, 150, 270])
layer_b = [[np.cos(t) / np.sqrt(3), np.sin(t) / np.sqrt(3), c / 2] for t in mid]
atoms(ax, layer_a, "C0", 200)
atoms(ax, layer_b, "C3", 200)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_zlim(-0.2, c + 0.2)
finish(ax, "hexagonal close packing (hcp)\nCN 12, ABAB stacking, 74.0%")
ax.set_box_aspect((2.2, 2.2, c + 0.4))

fig.subplots_adjust(left=0, right=1, top=0.86, bottom=0.0, wspace=0.05)
