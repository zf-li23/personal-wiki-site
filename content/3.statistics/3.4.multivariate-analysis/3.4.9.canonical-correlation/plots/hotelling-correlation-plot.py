"""Hotelling's reading/arithmetic example: variables plotted by their correlations with U_1 and U_2."""

import numpy as np
import matplotlib.pyplot as plt

Sigma = np.array([[100, 60, 30, 7.2], [60, 100, -6, 8.4], [30, -6, 144, 57.6], [7.2, 8.4, 57.6, 144]])
names = ["reading speed", "reading power", "arithmetic speed", "arithmetic power"]


def mpow(A, k):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(w**k) @ V.T


S11, S12, S22 = Sigma[:2, :2], Sigma[:2, 2:], Sigma[2:, 2:]
P1, rho, P2t = np.linalg.svd(mpow(S11, -0.5) @ S12 @ mpow(S22, -0.5))
A = (mpow(S11, -0.5) @ P1).T
sd = np.sqrt(np.diag(Sigma))
corr = (A @ Sigma[:2, :]) / sd  # Corr(U_k, X_i) for all four variables
fig, ax = plt.subplots(figsize=(6, 6))
ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="0.5"))
ax.axhline(0, color="0.7", lw=0.8)
ax.axvline(0, color="0.7", lw=0.8)
for i, name in enumerate(names):
    color = "C0" if i < 2 else "C3"
    ax.annotate("", xy=corr[:, i], xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=color, lw=1.6))
    dx, dy = [(0.03, 0.03), (0.03, 0.03), (-0.25, -0.1), (0.03, 0.08)][i]
    ax.text(corr[0, i] + dx, corr[1, i] + dy, name, color=color)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")
ax.set_xlabel(f"correlation with U_1  (rho_1* = {rho[0]:.2f})")
ax.set_ylabel(f"correlation with U_2  (rho_2* = {rho[1]:.2f})")
ax.set_title("Variables in the plane of the first-set canonical variates")
fig.tight_layout()
