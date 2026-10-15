import numpy as np
import matplotlib.pyplot as plt

# One vector a, two bases of R^2: standard e1, e2 and t1, t2 with (t1, t2) = (e1, e2) T
T = np.array([[2.0, 1.0], [1.0, 2.0]])
t1, t2 = T[:, 0], T[:, 1]
a = np.array([4.0, 5.0])
y = np.linalg.solve(T, a)           # new coordinates: x = T y

fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
for ax, (b1, b2, coords, name) in zip(
        axes,
        [(np.array([1.0, 0.0]), np.array([0.0, 1.0]), a, "standard basis e1, e2"),
         (t1, t2, y, "basis t1 = 2e1 + e2, t2 = e1 + 2e2")]):
    # Grid lines of the coordinate system defined by b1, b2
    for k in range(-6, 7):
        p0, p1 = k * b1 - 8 * b2, k * b1 + 8 * b2
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="gray", lw=0.5, alpha=0.5)
        p0, p1 = -8 * b1 + k * b2, 8 * b1 + k * b2
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="gray", lw=0.5, alpha=0.5)
    # Basis vectors
    for b, lab, c in [(b1, "1", "tab:red"), (b2, "2", "tab:green")]:
        ax.annotate("", xy=b, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color=c, lw=2.5))
    # Decomposition a = c1 b1 + c2 b2 as a broken path
    mid = coords[0] * b1
    ax.plot([0, mid[0]], [0, mid[1]], color="tab:red", lw=1.5, ls="--")
    ax.plot([mid[0], a[0]], [mid[1], a[1]], color="tab:green", lw=1.5, ls="--")
    ax.annotate("", xy=a, xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color="tab:blue", lw=2.5))
    ax.text(a[0] + 0.15, a[1] + 0.1, "a", color="tab:blue", fontsize=13)
    ax.set_xlim(-1, 6.5)
    ax.set_ylim(-1, 6.5)
    ax.set_aspect("equal")
    ax.set_title(f"{name}\ncoordinates of a: ({coords[0]:g}, {coords[1]:g})", fontsize=11)
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
fig.suptitle("Same vector, two coordinate vectors: x = T y with T = [[2, 1], [1, 2]]", fontsize=12)
fig.tight_layout()
