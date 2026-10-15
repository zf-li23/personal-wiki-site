"""Polar decomposition A = UP of a real 2x2 matrix: P stretches along the
orthonormal eigenvectors v_i of P = (A^T A)^{1/2}, then U rotates."""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1.6, 0.9], [-0.4, 0.9]])
W, s, Vt = np.linalg.svd(A)
signs = np.sign(Vt[:, 0])        # orient v_1, v_2 to point to the right
Vt, W = Vt * signs[:, None], W * signs[None, :]
U = W @ Vt                       # orthogonal factor (a rotation, since det A > 0)
P = Vt.T @ np.diag(s) @ Vt       # positive definite factor
angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))

theta = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(theta), np.sin(theta)])
# an asymmetric marker so that rotation and stretching are visible
marker = np.array([[0.0, 0.0, 0.45, 0.0, 0.0, 0.3], [-0.5, 0.5, 0.5, 0.5, 0.05, 0.05]])

stages = [(np.eye(2), "unit circle, eigenvectors of $P$"),
          (P, r"after $P$: stretch by $\sigma_i$ along $\boldsymbol{v}_i$"),
          (U @ P, rf"after $U$: rotate by {angle:.1f} degrees, giving $A$")]

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6), sharex=True, sharey=True)
for ax, (M, title) in zip(axes, stages):
    ax.plot(*(M @ circle), color="C0", linewidth=1.8)
    ax.fill(*(M @ circle), color="C0", alpha=0.08)
    ax.plot(*(M @ marker), color="C2", linewidth=2)
    for i, c in enumerate(["C1", "C3"]):
        v = M @ Vt[i]
        ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
        name = rf"$\boldsymbol{{v}}_{i + 1}$" if M is stages[0][0] else rf"$\sigma_{i + 1}$-axis"
        ax.text(*(v * 1.15 + np.array([0.03, 0.03])), name, color=c, fontsize=11)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.set_title(title, fontsize=10)
axes[0].set_xlim(-2.1, 2.1)
axes[0].set_ylim(-1.7, 1.7)
fig.suptitle(rf"$A = UP$ with $\sigma_1 = {s[0]:.2f}$, $\sigma_2 = {s[1]:.2f}$")
fig.tight_layout()
