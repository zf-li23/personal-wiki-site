"""Steady heat conduction in a unit square plate with a uniform heat source:
insulated edges except a cold segment (T = 0) on the middle of the top edge.
Cell-centered finite differences, assembled as a sparse matrix with Kronecker
products and solved with spsolve. Left: temperature field with isotherms.
Right: temperature along the vertical center line and along a horizontal
line just below the cold segment."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg as spla


def second_difference(n):
    main = 2.0 * np.ones(n)
    main[[0, -1]] = 1.0
    off = -np.ones(n - 1)
    return sparse.diags_array([off, main, off], offsets=[-1, 0, 1])


n = 100
h = 1.0 / n
alpha, q = 1.0, 1.0
I = sparse.eye_array(n)
D = second_difference(n)
A = sparse.kron(I, D) + sparse.kron(D, I)
xc = (np.arange(n) + 0.5) * h
cold = np.flatnonzero(np.abs(xc - 0.5) < 0.2)
d = np.zeros(n * n)
d[(n - 1) * n + cold] = 2.0
A = (A + sparse.diags_array(d)).tocsc()
b = np.full(n * n, q * h ** 2 / alpha)
T = spla.spsolve(A, b).reshape(n, n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), width_ratios=[1.15, 1])
im = ax1.imshow(T, origin="lower", extent=(0, 1, 0, 1), cmap="inferno")
cs = ax1.contour(xc, xc, T, levels=np.linspace(0.05, 0.65, 13), colors="white",
                 linewidths=0.6, alpha=0.7)
ax1.plot([0.3, 0.7], [1, 1], color="C0", lw=5, solid_capstyle="butt", clip_on=False)
ax1.text(0.5, 1.03, "T = 0", ha="center", va="bottom", color="C0")
ax1.text(0.5, 0.5, "uniform source q\ninsulated edges", ha="center", va="center",
         color="white", fontsize=9)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
fig.colorbar(im, ax=ax1, label="T  (q = alpha = 1)")

ax2.plot(xc, T[:, n // 2], color="C3", label="center line x = 0.5 (against y)")
j = int(0.9 * n)
ax2.plot(xc, T[j, :], color="C0", label=f"line y = {xc[j]:.2f} (against x)")
ax2.set_xlabel("position")
ax2.set_ylabel("T")
ax2.set_title(f"{n}x{n} cells, {A.nnz} nonzeros")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.tight_layout()
