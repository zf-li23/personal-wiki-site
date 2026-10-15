"""Trajectories X(t) = exp(tA) x0 of X' = AX for six 2x2 matrices: the
eigenvalues and the Jordan structure of A determine the phase portrait."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

cases = [
    (np.array([[-1.0, 0.0], [0.0, -3.0]]), "stable node", r"$\lambda = -1, -3$"),
    (np.array([[1.0, 0.0], [0.0, -2.0]]), "saddle", r"$\lambda = 1, -2$"),
    (np.array([[-0.3, 1.0], [-1.0, -0.3]]), "stable spiral", r"$\lambda = -0.3 \pm \mathrm{i}$"),
    (np.array([[0.0, 1.0], [-1.0, 0.0]]), "center (Example 11.8.1)", r"$\lambda = \pm \mathrm{i}$"),
    (np.array([[-1.0, 0.0], [0.0, -1.0]]), "star node (every vector is an eigenvector)", r"$A = -I$: two blocks $J_{-1,1}$"),
    (np.array([[-1.0, 1.0], [0.0, -1.0]]), "degenerate node", r"$A = J_{-1,2}$: one block"),
]

angles = np.linspace(0, 2 * np.pi, 16, endpoint=False)
starts = 1.8 * np.column_stack([np.cos(angles), np.sin(angles)])
ts = np.linspace(-3, 6, 600)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for ax, (A, name, spec) in zip(axes.flat, cases):
    flows = np.array([expm(t * A) for t in ts])          # exp(tA) for every t
    is_center = np.allclose(A + A.T, 0)
    pts = np.column_stack([np.linspace(0.4, 2.0, 5), np.zeros(5)]) if is_center else starts
    for x0 in pts:
        path = flows @ x0
        keep = np.all(np.abs(path) < 2.2, axis=1)
        path = np.where(keep[:, None], path, np.nan)
        ax.plot(path[:, 0], path[:, 1], color="C0", linewidth=1.1)
        # arrow in the direction of increasing t, placed at t = 0.6
        i = np.searchsorted(ts, 0.6)
        if keep[i] and keep[i + 1]:
            ax.annotate("", xy=path[i + 1], xytext=path[i],
                        arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.1))
    lam, vecs = np.linalg.eig(A)
    if np.all(np.isreal(lam)) and not np.allclose(A, A[0, 0] * np.eye(2)):
        for v in np.real(vecs.T):
            if np.linalg.norm(v) > 0:
                v = v / np.linalg.norm(v)
                ax.plot([-2.2 * v[0], 2.2 * v[0]], [-2.2 * v[1], 2.2 * v[1]],
                        color="C1", linewidth=1.6, linestyle="--")
    ax.plot([0], [0], "o", color="C3", markersize=5)
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 2.1)
    ax.set_aspect("equal")
    ax.set_title(f"{name}\n{spec}", fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
fig.suptitle(r"Phase portraits of $\boldsymbol{X}' = A\boldsymbol{X}$ (dashed: real eigenvector lines)")
fig.tight_layout()
