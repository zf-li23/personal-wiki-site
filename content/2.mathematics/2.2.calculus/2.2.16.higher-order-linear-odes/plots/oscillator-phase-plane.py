"""Phase plane of the damped oscillator written as a system x' = v, v' = -x - 2k v."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

cases = [(0.15, "underdamped, k = 0.15"), (1.0, "critically damped, k = 1"), (2.5, "overdamped, k = 2.5")]
angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
starts = np.column_stack([np.cos(angles), np.sin(angles)])
ts = np.linspace(0, 30, 1500)

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
for ax, (k, name) in zip(axes, cases):
    A = np.array([[0.0, 1.0], [-1.0, -2 * k]])
    flows = np.array([expm(t * A) for t in ts])
    for j, x0 in enumerate(starts):
        path = flows @ x0
        col = "C3" if j == 0 else "C0"
        ax.plot(path[:, 0], path[:, 1], color=col, lw=1.6 if j == 0 else 1.0)
        i = 40
        ax.annotate("", xy=path[i + 1], xytext=path[i],
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0))
    lam, vecs = np.linalg.eig(A)
    if np.all(np.isreal(lam)):
        for v in np.real(vecs.T):
            v = v / np.linalg.norm(v)
            ax.plot([-1.6 * v[0], 1.6 * v[0]], [-1.6 * v[1], 1.6 * v[1]], color="C1", ls="--", lw=1.3)
    ax.plot([0], [0], "o", color="k", ms=4)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("v = x'")
    ax.set_title(name)
fig.suptitle("Damped oscillator as a system x' = v, v' = -x - 2k v (red: x(0) = 1, v(0) = 0)")
fig.tight_layout()
