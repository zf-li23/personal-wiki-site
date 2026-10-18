"""Least squares as orthogonal projection: n = 3, two covariates."""

import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([1.0, 0.0, 0.0])
X2 = np.array([0.3, 1.0, 0.0])
X = np.column_stack([X1, X2])
Y = np.array([1.6, 1.4, 1.5])
beta = np.linalg.solve(X.T @ X, X.T @ Y)
Yhat = X @ beta
b_other = np.array([0.55, 0.45])
Xb = X @ b_other

fig = plt.figure(figsize=(7, 5.5))
ax = fig.add_subplot(projection="3d")
s, t = np.meshgrid(np.linspace(-0.3, 2.2, 2), np.linspace(-0.3, 1.9, 2))
plane = s[..., None] * X1 + t[..., None] * X2
ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.15, color="C0")


def arrow(v, start=None, **kw):
    start = np.zeros(3) if start is None else start
    ax.quiver(*start, *(v - start), arrow_length_ratio=0.08, **kw)


arrow(X1, color="C0", lw=1.5)
arrow(X2, color="C0", lw=1.5)
arrow(Y, color="C3", lw=2.2)
arrow(Yhat, color="C2", lw=2.2)
arrow(Y, start=Yhat, color="C1", lw=2.0)
arrow(Xb, color="0.5", lw=1.2)
ax.plot(*zip(Xb, Y), color="0.5", ls="--", lw=1.0)
ax.text(*(X1 * 1.05), "X_1", color="C0")
ax.text(*(X2 * 1.08), "X_2", color="C0")
ax.text(*(Y * 1.03), "Y", color="C3")
ax.text(*(Yhat + np.array([0.05, -0.15, 0.0])), "X b_hat = H Y", color="C2")
ax.text(*((Y + Yhat) / 2 + np.array([0.05, 0.0, 0.0])), "residual  Y - X b_hat", color="C1")
ax.text(*(Xb + np.array([-0.1, -0.25, 0.0])), "X b", color="0.4")
ax.text(1.9, 1.7, 0.0, "R(X)", color="C0")
ax.set_xlabel("unit 1")
ax.set_ylabel("unit 2")
ax.set_zlabel("unit 3")
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.2, 1.9)
ax.set_zlim(0, 1.8)
ax.view_init(elev=20, azim=-60)
ax.set_title("OLS: X b_hat is the orthogonal projection of Y onto the column space")
fig.tight_layout()
