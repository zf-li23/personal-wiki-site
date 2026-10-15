import numpy as np
import matplotlib.pyplot as plt

# A = U Sigma V^T acting on the unit circle, one factor at a time
A = np.array([[3.0, 0.0], [4.0, 5.0]])
U, s, Vt = np.linalg.svd(A)
# Fix signs: v1 points to the right, and U, V are rotations (det A > 0, so det U = det V);
# flipping a column of V together with the matching column of U keeps A = U Sigma V^T
if Vt[0, 0] < 0:
    U[:, 0] *= -1
    Vt[0, :] *= -1
if np.linalg.det(U) < 0:
    U[:, 1] *= -1
    Vt[1, :] *= -1
S = np.diag(s)

theta = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(theta), np.sin(theta)])
basis = np.eye(2)
V = Vt.T

stages = [
    ("x on the unit circle", np.eye(2)),
    ("V^T x: rotate", Vt),
    ("Sigma V^T x: stretch axes", S @ Vt),
    ("U Sigma V^T x = A x: rotate", U @ S @ Vt),
]

fig, axes = plt.subplots(1, 4, figsize=(16, 4.4))
for k, (ax, (title, M)) in enumerate(zip(axes, stages)):
    lim = 1.6 if k < 2 else 7.0
    pts = M @ circle
    ax.fill(pts[0], pts[1], color="tab:blue", alpha=0.12)
    ax.plot(pts[0], pts[1], color="tab:blue", lw=2)
    # Track the right singular vectors v1, v2 through each stage
    for i, c in enumerate(["tab:red", "tab:green"]):
        w = M @ V[:, i]
        ax.annotate("", xy=w, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color=c, lw=2))
    # A marker point that shows the rotation
    p = M @ np.array([1.0, 0.0])
    ax.plot(*p, "o", color="tab:orange", ms=8)
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=11)
    ax.grid(True, alpha=0.3)
axes[0].text(0.03, 0.95, "red: v1, green: v2\norange: image of e1\n(first two panels zoomed in)",
             transform=axes[0].transAxes, va="top", fontsize=9)
axes[2].text(0.03, 0.95, f"sigma1 = {s[0]:.2f}\nsigma2 = {s[1]:.2f}",
             transform=axes[2].transAxes, va="top", fontsize=9)
fig.suptitle("SVD of A = [[3, 0], [4, 5]]: rotation, axis scaling, rotation", fontsize=12)
fig.tight_layout()
