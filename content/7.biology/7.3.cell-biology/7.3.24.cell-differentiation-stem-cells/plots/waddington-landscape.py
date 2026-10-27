"""A quantitative Waddington landscape: the GATA1-PU.1 switch of blood progenitors (after Huang and colleagues 2007).

GATA1 (x, erythroid and megakaryocyte fates) and PU.1 (y, myeloid fates) each activate their own genes and
repress each other:
    dx/dt = a x^4 / (th^4 + x^4) + b th^4 / (th^4 + y^4) - k x,
    dy/dt = a y^4 / (th^4 + y^4) + b th^4 / (th^4 + x^4) - k y,
with b = 1, th = 0.5, k = 1 (dimensionless) and self-activation strength a. With small gene-expression noise
(diffusion coefficient 0.03) the steady-state probability density P(x, y) is obtained by solving the
Fokker-Planck equation on a grid, and the quasi-potential U = -ln P plays the role of the landscape
(low U: valleys in which cells sit).
A: a = 1: three valleys, a shallow central one (the multipotent progenitor, which co-expresses both
factors at intermediate levels) and two deeper ones (GATA1-high and PU.1-high committed states).
B: a = 0.6: weaker self-activation removes the central valley; progenitors must fall into one of the two
fates. C: the steady states (difference x - y) against a: the symmetric (progenitor) state is stable only above a
critical a of about 0.78 (filled: stable; open: unstable; a pitchfork bifurcation of the symmetric state), which is how a slow change in a parameter
reshapes the landscape and commits a cell.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

import wikibio as bio
from wikibio import charts, quant

P = bio.P
b, th, n, k, Dn, Lx, M = 1.0, 0.5, 4, 1.0, 0.03, 2.4, 100


def field(a, x, y):
    fx = a * x**n / (th**n + x**n) + b * th**n / (th**n + y**n) - k * x
    fy = a * y**n / (th**n + y**n) + b * th**n / (th**n + x**n) - k * y
    return fx, fy


def landscape(a):
    """Steady-state Fokker-Planck solution (finite volumes, upwind drift, no-flux walls); returns U = -ln P."""
    h = Lx / M
    xs = (np.arange(M) + 0.5) * h
    rows, cols, vals = [], [], []
    for i in range(M):
        for j in range(M):
            p = i * M + j
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if not (0 <= ii < M and 0 <= jj < M):
                    continue
                fx, fy = field(a, (xs[i] + xs[ii]) / 2, (xs[j] + xs[jj]) / 2)
                rate = max(fx * di + fy * dj, 0.0) / h + Dn / h**2
                q = ii * M + jj
                rows += [q, p]
                cols += [p, p]
                vals += [rate, -rate]
    A = sp.csr_matrix((vals, (rows, cols)), shape=(M * M, M * M)).tolil()
    A[0, :] = 1.0
    rhs = np.zeros(M * M)
    rhs[0] = 1.0
    Pss = spl.spsolve(A.tocsr(), rhs).reshape(M, M)
    U = -np.log(np.maximum(Pss, 1e-300))
    return xs, U - U.min()


fig, ax = bio.canvas(28.0, 10.0)
for k_, (a, letter, title) in enumerate(((1.0, "A", "a = 1: progenitor valley"), (0.6, "B", "a = 0.6: two fates only"))):
    xs, U = landscape(a)
    Uc = np.minimum(U, 8.0)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    bio.panel(ax, letter, (0.1 + 9.2 * k_, 9.9))
    p3 = charts.axes_at(ax, (0.3 + 9.2 * k_, 0.6, 8.6, 8.6), projection="3d")
    p3.plot_surface(X, Y, Uc, cmap="viridis_r" if not P.is_dark() else "viridis", rstride=2, cstride=2, linewidth=0,
                    antialiased=True, alpha=0.95)
    p3.contour(X, Y, Uc, levels=np.linspace(0.25, 7.5, 10), zdir="z", offset=0, colors=[P.muted()], linewidths=0.5)
    p3.view_init(elev=38, azim=-125)
    p3.set_xlabel("GATA1 x", fontsize=bio.core.FONT["tiny"], color=P.ink(), labelpad=-6)
    p3.set_ylabel("PU.1 y", fontsize=bio.core.FONT["tiny"], color=P.ink(), labelpad=-6)
    p3.set_zlabel("U = −ln P", fontsize=bio.core.FONT["tiny"], color=P.ink(), labelpad=-8)
    p3.tick_params(labelsize=0, colors=P.surface(), length=0)
    for axis in (p3.xaxis, p3.yaxis, p3.zaxis):
        axis.set_pane_color((0, 0, 0, 0))
        axis._axinfo["grid"]["color"] = P.mix(P.muted(), P.surface(), 0.5)
        axis.line.set_color(P.muted())
    p3.set_facecolor("none")
    bio.label(ax, (4.6 + 9.2 * k_, 9.4), title, size="small", bold=True)

# C: stable states against a
bio.panel(ax, "C", (19.2, 9.9))
pc = charts.axes_at(ax, (20.6, 1.6, 7.0, 7.2))
avals = np.linspace(0.0, 1.5, 76)


def settle(a, x, y, steps=8000, dt=0.05):
    for _ in range(steps):
        fx, fy = field(a, x, y)
        x, y = x + dt * fx, y + dt * fy
    return x, y


def sym_roots(a):
    s = np.linspace(0.0, 3.0, 3001)
    g = a * s**n / (th**n + s**n) + b * th**n / (th**n + s**n) - k * s
    return [s[i] - g[i] * (s[i + 1] - s[i]) / (g[i + 1] - g[i]) for i in range(len(s) - 1) if g[i] * g[i + 1] < 0]


def antisym_eig(a, s):
    dself = a * n * th**n * s ** (n - 1) / (th**n + s**n) ** 2
    dcross = b * n * th**n * s ** (n - 1) / (th**n + s**n) ** 2
    return dself - k + dcross  # eigenvalue of the perturbation x - y


for a in avals:
    x, y = settle(a, np.array([2.2, 0.05]), np.array([0.05, 2.2]))
    for v in x - y:
        if abs(v) > 0.05:
            pc.plot(a, v, "o", ms=3.0, color=quant.line_color("blood" if v > 0 else "channel"))
    for s0 in sym_roots(a):
        stable = antisym_eig(a, s0) < 0
        pc.plot(a, 0.0, "o", ms=3.0 if stable else 2.4, color=quant.line_color("neutral"),
                markerfacecolor=quant.line_color("neutral") if stable else "none")
pc.axvline(1.0, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pc.axvline(0.6, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pc.text(1.03, 1.5, "A", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.text(0.63, 1.5, "B", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.text(0.05, 1.9, "GATA1 high (erythroid)", fontsize=bio.core.FONT["tiny"], color=quant.line_color("blood"))
pc.text(0.05, -2.1, "PU.1 high (myeloid)", fontsize=bio.core.FONT["tiny"], color=quant.line_color("channel"))
pc.text(1.05, 0.15, "progenitor (filled: stable)", fontsize=bio.core.FONT["tiny"], color=quant.line_color("neutral"))
pc.set_xlim(0, 1.5)
pc.set_ylim(-2.6, 2.6)
charts.style_axes(pc, "self-activation a", "stable states: x − y")
charts.title(pc, "Bifurcation of the progenitor state")
