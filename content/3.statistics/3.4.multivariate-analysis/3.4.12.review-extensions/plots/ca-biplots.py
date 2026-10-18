"""Correspondence analysis biplots (scaling 1 and scaling 2) of a 3 sites by 5 species abundance table."""

import numpy as np
import matplotlib.pyplot as plt

F = np.array([[45, 10, 15, 0, 10], [25, 8, 10, 0, 3], [7, 15, 20, 14, 12]], dtype=float)
P = F / F.sum()
r, c = P.sum(axis=1), P.sum(axis=0)
Q = (P - np.outer(r, c)) / np.sqrt(np.outer(r, c))
U, s, Vt = np.linalg.svd(Q, full_matrices=False)
U, s, V = U[:, :2], s[:2], Vt[:2].T
sign = np.sign(V[3])  # orient axes so that species 4 has positive coordinates
U, V = U * sign, V * sign
A = V / np.sqrt(c)[:, None]          # species, scaling 1
Frow = U / np.sqrt(r)[:, None] * s   # sites, scaling 1
B = U / np.sqrt(r)[:, None]          # sites, scaling 2
G = A * s                            # species, scaling 2

sites = [f"Site {i}" for i in range(1, 4)]
species = [f"Sp {j}" for j in range(1, 6)]
fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
for ax, rows, cols, title in [(axes[0], Frow, A, "Scaling 1: sites at chi-square distances"), (axes[1], B, G, "Scaling 2: species at chi-square distances")]:
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.scatter(*rows.T, color="k", s=25)
    for (x, y), lab in zip(rows, sites):
        ax.annotate(lab, (x, y), xytext=(4, 4), textcoords="offset points")
    ax.scatter(*cols.T, color="C3", marker="s", s=25)
    for (x, y), lab in zip(cols, species):
        ax.annotate(lab, (x, y), xytext=(4, -10), textcoords="offset points", color="C3")
    ax.set_xlabel(f"CA axis 1 ({100 * s[0]**2 / np.sum(s**2):.1f}% of inertia)")
    ax.set_ylabel("CA axis 2")
    ax.set_title(title)
    ax.margins(0.15)
fig.tight_layout()
