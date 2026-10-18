"""Constraint regions of ridge regression (disk) and the Lasso (diamond) with RSS contours."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

# RSS(beta) = (beta - b)^T A (beta - b) + const, with OLS estimate b
b = np.array([2.2, 0.5])
A = np.array([[1.0, 0.5], [0.5, 1.0]])
g1, g2 = np.meshgrid(np.linspace(-1.6, 3.4, 400), np.linspace(-1.6, 3.0, 400))
d1, d2 = g1 - b[0], g2 - b[1]
rss = A[0, 0] * d1**2 + 2 * A[0, 1] * d1 * d2 + A[1, 1] * d2**2


def constrained_min(norm, c, m=20000):
    """Minimize RSS on the boundary of the unit ball of the given norm scaled by c."""
    t = np.linspace(0, 2 * np.pi, m)
    u = np.column_stack([np.cos(t), np.sin(t)])
    u = u / np.linalg.norm(u, ord=norm, axis=1)[:, None] * c
    d = u - b
    val = np.einsum("ij,jk,ik->i", d, A, d)
    return u[np.argmin(val)], val.min()


c = 1.0
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, norm, title in [(axes[0], 2, "Ridge: beta1^2 + beta2^2 <= c"), (axes[1], 1, "Lasso: |beta1| + |beta2| <= c")]:
    sol, val = constrained_min(norm, c)
    levels = val * np.array([1, 1.8, 3.0, 4.5])
    ax.contour(g1, g2, rss, levels=levels, colors="C1", linewidths=1.2)
    if norm == 2:
        ax.add_patch(Circle((0, 0), c, color="C0", alpha=0.35))
    else:
        ax.add_patch(Polygon([[c, 0], [0, c], [-c, 0], [0, -c]], closed=True, color="C0", alpha=0.35))
    ax.plot(*b, "o", color="C1")
    ax.annotate("OLS estimate", b, xytext=(b[0] - 0.3, b[1] + 1.4), arrowprops=dict(arrowstyle="->"))
    ax.plot(*sol, "o", color="C3", zorder=4)
    ax.annotate(f"solution ({sol[0]:.2f}, {sol[1]:.2f})", sol, xytext=(sol[0] - 1.6, sol[1] - 1.2),
                arrowprops=dict(arrowstyle="->"))
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.set_xlim(-1.6, 3.4)
    ax.set_ylim(-1.6, 3.0)
    ax.set_aspect("equal")
    ax.set_xlabel("beta1")
    ax.set_ylabel("beta2")
    ax.set_title(title)
fig.tight_layout()
