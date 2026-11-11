"""Eigenvectors of the successor representation in two-dimensional environments.

A 20 x 20 grid of states; an unbiased random walk to the four neighbors (moves into walls are
replaced by staying put, so T is symmetric). The SR M = (I - gamma T)^(-1) (gamma = 0.95) has the
same eigenvectors as T, ordered here by decreasing eigenvalue of M (the most predictive modes
first, which vary slowest in space). The first (constant) eigenvector is omitted.
Top row: open square box, eigenvectors 2-7: periodic patterns of increasing spatial frequency
(products of cosines), at several scales and orientations.
Bottom row: the same box with a wall from the left side to 3/4 of the width at mid height
(transitions across the wall are removed): the eigenvectors respect the barrier and the
low-frequency modes separate the two compartments.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
L = 20
gamma = 0.95


def walk(barrier):
    n = L * L
    T = np.zeros((n, n))
    idx = lambda i, j: i * L + j
    for i in range(L):
        for j in range(L):
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                blocked = not (0 <= a < L and 0 <= b < L)
                if barrier and not blocked and {i, a} == {L // 2 - 1, L // 2} and j < 3 * L // 4:
                    blocked = True
                if blocked:
                    T[idx(i, j), idx(i, j)] += 0.25
                else:
                    T[idx(i, j), idx(a, b)] += 0.25
    return T


fig, axs = plt.subplots(2, 6, figsize=(13, 4.8))
for row, barrier in enumerate((False, True)):
    T = walk(barrier)
    # M = (I - gamma T)^-1 has the eigenvectors of T, with eigenvalues 1 / (1 - gamma lambda):
    # ordering by the eigenvalues of T is the same as ordering by those of M
    w, V = np.linalg.eigh(T)
    order = np.argsort(w)[::-1]
    for k in range(6):
        v = V[:, order[k + 1]].reshape(L, L)
        ax = axs[row, k]
        lim = np.abs(v).max()
        ax.imshow(v, cmap="RdBu_r", vmin=-lim, vmax=lim, origin="lower")
        if barrier:
            ax.plot([-0.5, 3 * L // 4 - 0.5], [L / 2 - 0.5, L / 2 - 0.5], color=P.ink(), lw=2.5)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"eigenvector {k + 2}", fontsize=8)
    axs[row, 0].set_ylabel("Open box" if not barrier else "Box with wall", fontsize=9)
fig.tight_layout()
