import numpy as np
import matplotlib.pyplot as plt


def arrow2d(ax, start, end, color, label=None, width=2.0):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=width, mutation_scale=14))
    if label:
        ax.text(*(np.asarray(end) + np.array([0.08, 0.08])), label, color=color, fontsize=11)


def right_angle(ax, corner, u, v, size, color):
    u = size * u / np.linalg.norm(u)
    v = size * v / np.linalg.norm(v)
    pts = np.array([corner + u, corner + u + v, corner + v])
    ax.plot(pts[:, 0], pts[:, 1], color=color, lw=1)


fig = plt.figure(figsize=(11, 4.8))

# Left: Example 4.1.1, projection of b onto the line span(a)
ax = fig.add_subplot(1, 2, 1)
a = np.array([2.0, 1.0])
b = np.array([2.0, 4.0])
p = (a @ b) / (a @ a) * a
r = b - p
s = np.linspace(-0.6, 2.4, 2)
ax.plot(s * a[0], s * a[1], color="gray", lw=1, ls="--")
ax.text(*(2.3 * a + np.array([-0.4, -0.5])), r"span$(\boldsymbol{a})$", color="gray", fontsize=10)
arrow2d(ax, (0, 0), p, "C2", r"$\hat{x}\boldsymbol{a}$", width=4.0)
arrow2d(ax, (0, 0), a, "C0", r"$\boldsymbol{a}$")
arrow2d(ax, (0, 0), b, "C1", r"$\boldsymbol{b}$")
arrow2d(ax, p, b, "C3")
ax.text(*((p + b) / 2 + np.array([0.12, -0.1])), r"$\boldsymbol{r} = \boldsymbol{b} - \hat{x}\boldsymbol{a}$",
        color="C3", fontsize=11)
right_angle(ax, p, -a, r, 0.25, "C3")
ax.set_aspect("equal")
ax.set_xlim(-0.8, 5.0)
ax.set_ylim(-0.5, 4.6)
ax.grid(True, alpha=0.3)
ax.set_title("projection onto a line: $\\boldsymbol{r} \\perp \\boldsymbol{a}$")

# Right: Example 4.5.1, projection of b onto the plane R(A)
ax = fig.add_subplot(1, 2, 2, projection="3d")
a1 = np.array([1.0, 2.0, 1.0])
a2 = np.array([1.0, 1.0, 3.0])
A = np.column_stack([a1, a2])
b3 = np.array([0.0, 3.0, 5.0])
x0 = np.linalg.solve(A.T @ A, A.T @ b3)
p3 = A @ x0
r3 = b3 - p3
S, T = np.meshgrid(np.linspace(-0.6, 1.6, 2), np.linspace(-0.4, 2.0, 2))
X = S * a1[0] + T * a2[0]
Y = S * a1[1] + T * a2[1]
Z = S * a1[2] + T * a2[2]
ax.plot_surface(X, Y, Z, alpha=0.3, color="C0", edgecolor="none")
for vec, start, color, label in [
    (a1, np.zeros(3), "C0", r"$\boldsymbol{a}_1$"),
    (a2, np.zeros(3), "C0", r"$\boldsymbol{a}_2$"),
    (b3, np.zeros(3), "C1", r"$\boldsymbol{b}$"),
    (p3, np.zeros(3), "C2", r"$A\boldsymbol{x}_0 = P_A\boldsymbol{b}$"),
    (r3, p3, "C3", r"$\boldsymbol{r}$"),
]:
    ax.quiver(*start, *vec, color=color, arrow_length_ratio=0.08, linewidth=2)
    tip = start + vec
    ax.text(*(tip + np.array([0.05, 0.05, 0.15])), label, color=color, fontsize=10)
ax.text(1.4, 2.6, 0.2, r"$\mathcal{R}(A)$", color="C0", fontsize=10)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$x_3$")
for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.view_init(elev=18, azim=-60)
ax.set_title("projection onto the column space: $\\boldsymbol{r} \\perp \\mathcal{R}(A)$")
fig.tight_layout()
