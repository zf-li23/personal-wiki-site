import numpy as np
import matplotlib.pyplot as plt

# Example 6.1.1: eigenvalues 1 (eigenvector x1 = (0.2, 0.8)) and 0.5 (eigenvector x2 = (1, -1))
A = np.array([[0.6, 0.1], [0.4, 0.9]])
x1 = np.array([0.2, 0.8])
starts = [np.array([1.0, 0.0]), np.array([0.0, 1.4]), np.array([1.6, 0.4]), np.array([0.9, 1.6]), np.array([0.5, 0.1])]
steps = 12

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
ax = axes[0]
s = np.linspace(0, 2.6, 2)
ax.plot(s * x1[0], s * x1[1], color="gray", lw=1.5, label=r"eigenline span$(\boldsymbol{x}_1)$, $\lambda = 1$")
for k, x in enumerate(starts):
    traj = [x]
    for _ in range(steps):
        traj.append(A @ traj[-1])
    traj = np.array(traj)
    ax.plot(traj[:, 0], traj[:, 1], "o-", color=f"C{k}", markersize=4, lw=1)
    ax.plot(*x, "s", color=f"C{k}", markersize=7)
ax.annotate("", xy=(1.3, 0.3), xytext=(1.0, 0.6),
            arrowprops=dict(arrowstyle="<->", color="gray", lw=1))
ax.text(0.95, 0.15, r"direction $\boldsymbol{x}_2$, $\lambda = 0.5$", color="gray", fontsize=9)
ax.set_xlabel("population of region 1")
ax.set_ylabel("population of region 2")
ax.set_title(r"iterates $A^t\boldsymbol{x}$ (squares: $t = 0$)")
ax.set_aspect("equal")
ax.set_xlim(-0.05, 1.8)
ax.set_ylim(-0.05, 2.1)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=9)

ax = axes[1]
t = np.arange(steps + 1)
for k, x in enumerate(starts):
    limit = x.sum() * x1
    err = []
    y = x.copy()
    for _ in t:
        err.append(np.linalg.norm(y - limit))
        y = A @ y
    ax.semilogy(t, err, "o-", color=f"C{k}", markersize=4, lw=1)
ax.semilogy(t, 0.5 ** t, "--", color="gray", lw=1.5, label=r"$0.5^t$")
ax.set_xlabel("t")
ax.set_ylabel(r"distance to the limit $(x_1 + x_2)\boldsymbol{x}_1$")
ax.set_title("the second eigenvalue sets the rate of convergence")
ax.grid(True, which="major", alpha=0.3)
ax.legend(fontsize=9)
fig.tight_layout()
