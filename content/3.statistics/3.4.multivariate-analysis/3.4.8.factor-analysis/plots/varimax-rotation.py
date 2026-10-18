"""Varimax rotation of the principal component loadings of the consumer-preference data."""

import numpy as np
import matplotlib.pyplot as plt

names = ["taste", "good buy", "flavor", "snack", "energy"]
L = np.array([[0.56, 0.82], [0.78, -0.53], [0.65, 0.75], [0.94, -0.10], [0.80, -0.54]])


def varimax(L, iters=500, tol=1e-12):
    h = np.sqrt((L**2).sum(axis=1))
    A = L / h[:, None]
    p, m = A.shape
    T = np.eye(m)
    crit = 0.0
    for _ in range(iters):
        B = A @ T
        U, s, Vt = np.linalg.svd(A.T @ (B**3 - B @ np.diag((B**2).sum(axis=0)) / p))
        T = U @ Vt
        if s.sum() - crit < tol:
            break
        crit = s.sum()
    return T


T = varimax(L)
Lrot = L @ T
fig, axes = plt.subplots(1, 2, figsize=(11, 5.3))
for ax, title, rotated in [(axes[0], "unrotated loadings", False), (axes[1], "varimax: rotated factor axes", True)]:
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="0.6", ls=":"))
    ax.plot(L[:, 0], L[:, 1], "o", color="C0")
    offsets = [(5, 4), (-62, 4), (5, 4), (5, 4), (5, -12)]
    for name, (a, b), off in zip(names, L, offsets):
        ax.annotate(name, (a, b), xytext=off, textcoords="offset points")
    if rotated:
        for j, color in zip(range(2), ["C3", "C2"]):
            d = T[:, j]
            ax.annotate("", xy=1.15 * d, xytext=-0.3 * d, arrowprops=dict(arrowstyle="->", color=color, lw=1.8))
            ax.text(*(1.18 * d), f"F{j + 1}*", color=color, fontsize=11)
        ang = np.degrees(np.arctan2(T[1, 0], T[0, 0]))
        ax.set_title(f"{title} (angle {ang:.0f} deg)")
    else:
        ax.set_title(title)
    ax.set_xlim(-1.2, 1.35)
    ax.set_ylim(-1.2, 1.35)
    ax.set_aspect("equal")
    ax.set_xlabel("loading on F1")
    ax.set_ylabel("loading on F2")
fig.tight_layout()
