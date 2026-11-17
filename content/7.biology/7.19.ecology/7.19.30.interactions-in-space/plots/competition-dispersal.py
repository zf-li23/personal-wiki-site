"""Two competitors in a heterogeneous environment: u_t = d u_xx + u (m - u - b v), v_t = D v_xx + v (m - c u - v).

Domain (0, 1) with zero-flux ends, resource m(x) = 1 + 0.9 sin(2 pi x); finite volumes with 60 cells.
theta_d is the steady state of a species alone with diffusion rate d (Newton's method).
A: m(x) (dashed) and theta_d for slow (d = 0.001), intermediate (d = 0.08) and fast (d = 10) dispersers.
B: symmetric competition (b = c = 1): the invasion rate of a rare competitor with diffusion D into the
resident theta_d (d = 0.05) is the principal eigenvalue lambda_1 of D d^2/dx^2 + (m - theta_d); it is
zero at D = d and positive only for D < d: the slower disperser always invades and wins.
C: weak competition everywhere (b = c = 0.95) on a grid of (d, D) on log scales: the outcome predicted by
the two invasion rates. Coexistence for most rates, but a species is excluded when its competitor has an
intermediate dispersal rate (between about 0.01 and 0.3, around the maximum of total biomass at d = 0.08)
and it disperses considerably faster (blue: u wins, red: v wins).
"""

import numpy as np
from matplotlib.colors import ListedColormap
from scipy.sparse import diags

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
N = 60
h = 1.0 / N
x = (np.arange(N) + 0.5) * h
m = 1 + 0.9 * np.sin(2 * np.pi * x)
main = -2 * np.ones(N)
main[0] = main[-1] = -1
Lap = (diags([np.ones(N - 1), main, np.ones(N - 1)], [-1, 0, 1]) / h**2).toarray()


def theta(d, th0=None):
    th = m.copy() if th0 is None else th0.copy()
    for _ in range(80):
        F = d * Lap @ th + th * (m - th)
        J = d * Lap + np.diag(m - 2 * th)
        dth = np.linalg.solve(J, -F)
        th += dth
        if np.abs(dth).max() < 1e-11:
            break
    return th


def lam(D, hv):
    return np.linalg.eigvalsh(D * Lap + np.diag(hv)).max()


ds = np.logspace(-3, 1, 31)
ths = []
th = None
for d in ds:
    th = theta(d, th)
    ths.append(th)

fig, ax = bio.canvas(33.0, 11.0)
pa = C.axes_at(ax, (2.0, 1.7, 8.0, 7.6))
pa.plot(x, m, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="resource m(x)")
for d, tok in ((0.001, "dna"), (0.08, "plant"), (10.0, "negative")):
    pa.plot(x, theta(d, theta(min(d, 0.01)) if d > 0.01 else None), color=Q.line_color(tok), lw=1.7, label=f"d = {d:g}")
pa.set_xlim(0, 1)
pa.set_ylim(0, 2.0)
C.style_axes(pa, "position x", "density")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Single species: steady states", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.0, 1.7, 8.0, 7.6))
d0 = 0.05
th0 = theta(d0, theta(0.01))
Ds = np.logspace(-3, 1, 120)
lv = [lam(D, m - th0) for D in Ds]
pb.semilogx(Ds, lv, color=Q.line_color("negative"), lw=1.8)
pb.axhline(0, color=P.ink(), lw=0.8)
pb.axvline(d0, color=P.muted(), lw=0.8, ls=":")
pb.text(d0 * 1.15, max(lv) * 0.9, "D = d", fontsize=FS["tiny"], color=P.ink())
pb.text(0.0013, -0.05, "slower invader:\ninvades", fontsize=FS["tiny"], color=P.ink())
pb.text(0.6, max(lv) * 0.3, "faster invader:\nexcluded", fontsize=FS["tiny"], color=P.ink())
C.style_axes(pb, "invader diffusion rate D", "invasion rate lambda_1")
bio.panel(ax, "B", (11.3, 10.7))
bio.label(ax, (13.0, 10.0), "Symmetric competition: slow wins", size="small", bold=True, ha="left")

c = 0.95
G = np.zeros((len(ds), len(ds)))
for i in range(len(ds)):
    for j in range(len(ds)):
        lv_ = lam(ds[j], m - c * ths[i])
        lu_ = lam(ds[i], m - c * ths[j])
        G[j, i] = 2 * (lv_ > 0) + (lu_ > 0)
pc = C.axes_at(ax, (24.0, 1.7, 7.6, 7.6))
cols = [P.surface(), P.mix(P.fill("dna"), P.surface(), 0.3), P.mix(P.fill("negative"), P.surface(), 0.3),
        P.mix(P.fill("plant"), P.surface(), 0.3)]
lg = np.log10(ds)
pc.pcolormesh(lg, lg, G, cmap=ListedColormap(cols), vmin=-0.5, vmax=3.5, shading="nearest")
pc.plot([-3, 1], [-3, 1], color=P.ink(), lw=0.6, ls=":")
pc.text(-2.7, 0.3, "coexistence", fontsize=FS["tiny"], color=P.ink())
pc.text(-1.0, 0.75, "u wins", fontsize=FS["tiny"], color=P.ink(), ha="center")
pc.text(0.6, -1.0, "v wins", fontsize=FS["tiny"], color=P.ink(), ha="center", rotation=90)
pc.set_xticks([-3, -2, -1, 0, 1], ["0.001", "0.01", "0.1", "1", "10"])
pc.set_yticks([-3, -2, -1, 0, 1], ["0.001", "0.01", "0.1", "1", "10"])
C.style_axes(pc, "diffusion of u, d", "diffusion of v, D", box=True)
bio.panel(ax, "C", (22.3, 10.7))
bio.label(ax, (24.0, 10.0), "Weak competition, b = c = 0.95", size="small", bold=True, ha="left")
