"""Neumann eigenfunctions of the Laplacian on a disc and on an ellipse of eccentricity 0.8 (Section 33.7).

Top: the first four nonconstant modes of the unit disc, J1(kr) cos phi, J2(kr) cos 2 phi, J0(kr), J3(kr) cos 3 phi,
with k^2 = 3.39, 9.33, 14.68, 17.65 (the degenerate partners sin m phi are rotated copies). Bottom: the first six
nonconstant modes of an ellipse of the same area with e = 0.8, computed by finite differences (grid 0.02, no-flux
boundary); eigenvalues in units of the disc's area. Lines: nodal lines (the zero set), the candidate compartment
boundaries of the KST model; colour: sign.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
from scipy.special import jv, jnp_zeros
import wikibio as bio
from wikibio import charts as C
from matplotlib.colors import LinearSegmentedColormap

P = bio.P
cmap = LinearSegmentedColormap.from_list("d", [P.fill("channel"), P.surface(), P.fill("drug")])
fig, ax = bio.canvas(30.0, 12.6)

# disc
modes = [(1, jnp_zeros(1, 1)[0]), (2, jnp_zeros(2, 1)[0]), (0, 3.8317059702), (3, jnp_zeros(3, 1)[0])]
r = np.linspace(0, 1, 120)
ph = np.linspace(0, 2 * np.pi, 181)
R, PH = np.meshgrid(r, ph)
Xd, Yd = R * np.cos(PH), R * np.sin(PH)
bio.panel(ax, "A", (0.2, 12.4))
for k, (m, kk) in enumerate(modes):
    F = jv(m, kk * R) * np.cos(m * PH)
    pa = C.axes_at(ax, (1.0 + 4.9 * k, 7.2, 4.2, 4.2))
    lim = np.abs(F).max()
    pa.contourf(Xd, Yd, F, levels=21, cmap=cmap, vmin=-lim, vmax=lim)
    pa.contour(Xd, Yd, F, levels=[0], colors=[P.ink()], linewidths=1.4)
    pa.plot(np.cos(ph), np.sin(ph), color=P.muted(), lw=0.8)
    pa.set_aspect("equal")
    pa.axis("off")
    bio.label(ax, (3.1 + 4.9 * k, 11.8), f"J{m}  k² = {kk**2:.2f}", size="small")

# ellipse
e = 0.8
q = np.sqrt(1 - e * e)
a, b = 1 / np.sqrt(q), np.sqrt(q)
h = 0.02
x = np.arange(-a, a + h, h)
y = np.arange(-b, b + h, h)
X, Y = np.meshgrid(x, y, indexing="ij")
ins = (X / a) ** 2 + (Y / b) ** 2 < 1
idx = -np.ones(X.shape, int)
idx[ins] = np.arange(ins.sum())
I, J = np.nonzero(ins)
rows, cols, vals = [], [], []
deg = np.zeros(ins.sum())
for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    ii, jj = I + di, J + dj
    ok = (ii >= 0) & (ii < X.shape[0]) & (jj >= 0) & (jj < X.shape[1])
    ok[ok] &= ins[ii[ok], jj[ok]]
    rows.append(idx[I[ok], J[ok]])
    cols.append(idx[ii[ok], jj[ok]])
    deg[idx[I[ok], J[ok]]] += 1
rows = np.concatenate(rows + [np.arange(ins.sum())])
cols = np.concatenate(cols + [np.arange(ins.sum())])
vals = np.concatenate([-np.ones(len(rows) - ins.sum()), deg]) / h**2
Lap = sp.csr_matrix((vals, (rows, cols)))
w, V = sla.eigsh(Lap, k=7, sigma=-0.01, which="LM")
order = np.argsort(w)
th = np.linspace(0, 2 * np.pi, 200)
bio.panel(ax, "B", (0.2, 6.4))
for k in range(6):
    jcol = order[k + 1]
    F = np.full(X.shape, np.nan)
    F[ins] = V[:, jcol]
    pa = C.axes_at(ax, (0.6 + 4.9 * k, 1.0, 4.6, 4.6 * b / a))
    lim = np.nanmax(np.abs(F))
    pa.contourf(X, Y, F, levels=21, cmap=cmap, vmin=-lim, vmax=lim)
    pa.contour(X, Y, np.ma.masked_invalid(F), levels=[0], colors=[P.ink()], linewidths=1.4)
    pa.plot(a * np.cos(th), b * np.sin(th), color=P.muted(), lw=0.8)
    pa.set_xlim(-a, a)
    pa.set_ylim(-b, b)
    pa.set_aspect("equal")
    pa.axis("off")
    bio.label(ax, (2.9 + 4.9 * k, 4.25), f"mode {k + 1}: k² = {w[jcol]:.2f}", size="small")
