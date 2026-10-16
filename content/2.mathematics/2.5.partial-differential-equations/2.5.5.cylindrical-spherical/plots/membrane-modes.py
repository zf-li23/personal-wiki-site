"""Normal modes of a circular membrane: J_m(j_mk r) cos(m theta) on the unit disk."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros

modes = [(0, 1), (1, 1), (2, 1), (0, 2), (3, 1), (1, 2)]
j01 = jn_zeros(0, 1)[0]

r = np.linspace(0, 1, 160)
th = np.linspace(0, 2 * np.pi, 241)
R, TH = np.meshgrid(r, th)
X, Y = R * np.cos(TH), R * np.sin(TH)

fig, axes = plt.subplots(2, 3, figsize=(10, 6.8))
for ax, (m, k) in zip(axes.flat, modes):
    j = jn_zeros(m, k)[-1]
    U = jv(m, j * R) * np.cos(m * TH)
    U = U / np.max(np.abs(U))
    ax.pcolormesh(X, Y, U, cmap="RdBu_r", vmin=-1, vmax=1, shading="gouraud")
    ax.contour(X, Y, U, levels=[0], colors="k", linewidths=1.2)
    ax.plot(np.cos(th), np.sin(th), color="k", lw=1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"(m, k) = ({m}, {k}),  omega / omega_01 = {j / j01:.3f}", fontsize=10)
fig.suptitle("Modes of a circular membrane (red: up, blue: down, black: nodal lines)")
fig.tight_layout()
