import numpy as np
import matplotlib.pyplot as plt

# A region with two holes and its positively oriented boundary
s = np.linspace(0, 2 * np.pi, 400)
outer = np.c_[2.6 * np.cos(s) + 0.25 * np.cos(3 * s), 1.7 * np.sin(s) + 0.15 * np.sin(2 * s)]
holes = [
    (np.c_[-1.0 + 0.55 * np.cos(s), 0.1 + 0.45 * np.sin(s)]),
    (np.c_[1.1 + 0.4 * np.cos(s), -0.2 + 0.6 * np.sin(s)]),
]

fig, ax = plt.subplots(figsize=(8, 5.6))
ax.fill(outer[:, 0], outer[:, 1], color="tab:green", alpha=0.25, lw=0)
for h in holes:
    ax.fill(h[:, 0], h[:, 1], color=fig.get_facecolor(), lw=0)


def arrows(curve, reverse, color):
    c = curve[::-1] if reverse else curve
    ax.plot(c[:, 0], c[:, 1], color=color, lw=2)
    n = len(c)
    for k in range(0, n - 1, n // 4):
        ax.annotate("", xy=c[k + 3], xytext=c[k], arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=20))


arrows(outer, False, "tab:blue")
for h in holes:
    arrows(h, True, "tab:red")

# a walker on the outer boundary: the region lies to the left
k = 60
p, q = outer[k], outer[k + 2]
tng = (q - p) / np.linalg.norm(q - p)
left = np.array([-tng[1], tng[0]])
ax.annotate("", xy=p + 0.6 * left, xytext=p, arrowprops=dict(arrowstyle="-|>", color="tab:gray", lw=1.5))
ax.text(*(p + 0.75 * left), "D on the left", fontsize=9, ha="center")
ax.text(0.0, 1.0, "D", fontsize=16, ha="center")
ax.text(2.2, -1.75, "outer boundary: counterclockwise", color="tab:blue", fontsize=10, ha="center")
ax.text(0.0, -0.95, "inner boundaries: clockwise", color="tab:red", fontsize=10, ha="center")
ax.set_aspect("equal")
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-2.1, 2.1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Positive orientation of the boundary of a multiply connected region")
fig.tight_layout()
