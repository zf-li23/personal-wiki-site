"""Numerical solution of Laplace's equation: a conductor held at phi = 1 inside a grounded box.

Five-point finite differences on a square grid; the sparse linear system is solved with
scipy.sparse.linalg.spsolve. By the uniqueness theorem the discrete solution approximates
the one and only potential that satisfies these boundary conditions.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, identity, kron
from scipy.sparse.linalg import spsolve

n = 161                      # grid points per side, box [0, 1]^2, phi = 0 on its walls
h = 1.0 / (n - 1)
x = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, x, indexing="xy")

# conductor: an L-shaped electrode (convex and concave corners), held at phi = 1
cond = ((X > 0.30) & (X < 0.70) & (Y > 0.30) & (Y < 0.42)) | \
       ((X > 0.30) & (X < 0.42) & (Y > 0.30) & (Y < 0.70))
fixed = cond.copy()
fixed[0, :] = fixed[-1, :] = fixed[:, 0] = fixed[:, -1] = True
phi_fixed = np.where(cond, 1.0, 0.0)

# discrete Laplacian on the full grid, then eliminate the fixed (Dirichlet) nodes
D = diags([1.0, -2.0, 1.0], [-1, 0, 1], shape=(n, n))
I = identity(n)
L = (kron(I, D) + kron(D, I)).tocsr() / h**2
free = ~fixed.ravel()
A = L[free][:, free]
b = -L[free][:, ~free] @ phi_fixed.ravel()[~free]
phi = phi_fixed.ravel().copy()
phi[free] = spsolve(A.tocsc(), b)
phi = phi.reshape(n, n)

Ey, Ex = np.gradient(-phi, h)
Ex = np.ma.masked_where(cond, Ex)
Ey = np.ma.masked_where(cond, Ey)
E = np.hypot(Ex, Ey)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
cs = ax1.contour(X, Y, np.ma.masked_where(cond, phi), levels=np.linspace(0.05, 0.95, 10),
                 cmap="viridis", linewidths=1.3)
ax1.clabel(cs, fmt="%.2f", fontsize=7)
ax1.streamplot(X, Y, Ex, Ey, color="0.6", linewidth=0.7, density=1.4, arrowsize=0.7)
ax1.contourf(X, Y, cond.astype(float), levels=[0.5, 1.5], colors=["0.75"])
ax1.set_title(r"Equipotentials and field lines ($\varphi = 1$ on the electrode)")
cf = ax2.contourf(X, Y, np.ma.log10(E + 1e-3), levels=30, cmap="magma")
fig.colorbar(cf, ax=ax2, label=r"$\log_{10} E$")
ax2.contourf(X, Y, cond.astype(float), levels=[0.5, 1.5], colors=["0.75"])
ax2.set_title("Field strength: large at convex corners, small at the concave one")
for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
fig.tight_layout()
