"""Noise propagation in a two-gene cascade X -> Y (copy numbers; time in units of 1/gamma_Y).
X is made at rate 50 gamma_X and removed at rate gamma_X (mean 50); Y is made at rate
f(x) = 200 x^2/(50^2 + x^2) and removed at rate 1 (mean about 100), so the logarithmic gain of
the link at the mean is H = 1.
A: one cell simulated with the Gillespie algorithm for gamma_X = gamma_Y: the fluctuations of Y follow
those of X with a lag and add their own.
B: squared coefficient of variation of Y against gamma_X/gamma_Y. Points: exact stochastic simulation of
2500 cells; lines: the linear noise approximation (Theorem 17.1.1), its total, the intrinsic part
1/<y> and the propagated part. Fast upstream fluctuations are averaged out by Y.
C: noise at the end of a cascade of n linear-noise stages (all means 100, all removal rates equal),
for logarithmic gains H = 0.5, 1 and 2 per link (Lyapunov equation)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_continuous_lyapunov
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
K, BETA = 50.0, 200.0


def f(x):
    return BETA * x**2 / (K**2 + x**2)


def single(T, gx):
    x, y, t = 50, 100, 0.0
    ts, xs, ys = [0.0], [x], [y]
    while t < T:
        a = np.array([50.0 * gx, gx * x, f(x), y])
        a0 = a.sum()
        t += rng.exponential(1 / a0)
        r = rng.random() * a0
        c = np.cumsum(a)
        k = int(np.searchsorted(c, r))
        x += (1, -1, 0, 0)[k]
        y += (0, 0, 1, -1)[k]
        ts.append(t); xs.append(x); ys.append(y)
    return np.array(ts), np.array(xs), np.array(ys)


def ensemble(gx, ncell=2500):
    T = 8.0 / min(gx, 1.0)
    x = rng.poisson(50, ncell).astype(float)
    y = rng.poisson(100, ncell).astype(float)
    t = np.zeros(ncell)
    alive = np.ones(ncell, bool)
    while alive.any():
        xa, ya = x[alive], y[alive]
        a = np.stack([np.full_like(xa, 50.0 * gx), gx * xa, f(xa), ya])
        a0 = a.sum(0)
        dt = rng.exponential(1 / a0)
        tn = t[alive] + dt
        ok = tn < T
        c = np.cumsum(a, 0) / a0
        u = rng.random(xa.size)
        k = (u[None, :] > c).sum(0)
        dx = np.select([k == 0, k == 1], [1.0, -1.0], 0.0)
        dy = np.select([k == 2, k == 3], [1.0, -1.0], 0.0)
        idx = np.flatnonzero(alive)
        x[idx[ok]] += dx[ok]
        y[idx[ok]] += dy[ok]
        t[idx[ok]] = tn[ok]
        alive[idx[~ok]] = False
    return y.var() / y.mean() ** 2


fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.38)

ax = axs[0]
ts, xs, ys = single(40.0, 1.0)
ax.step(ts, xs / 50, where="post", color=charts.line("protein"), lw=0.9, label=r"$x/\langle x\rangle$")
ax.step(ts, ys / 100, where="post", color=charts.line("highlight"), lw=0.9, label=r"$y/\langle y\rangle$")
ax.set_xlim(0, 40)
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=2)
charts.style_axes(ax, r"time ($1/\gamma_Y$)", "copy number / mean")
charts.title(ax, "A  One cell")

ax = axs[1]
r = np.logspace(-1.3, 1.3, 200)
my = 100.0
intr = np.full_like(r, 1 / my)
prop = 1.0 / (r + 1) / 50.0
ax.semilogx(r, intr + prop, color=P.ink(), lw=1.6, label="LNA total")
ax.semilogx(r, intr, "--", color=charts.line("protein"), lw=1.2, label=r"intrinsic $1/\langle y\rangle$")
ax.semilogx(r, prop, ":", color=charts.line("highlight"), lw=1.6, label="propagated from X")
rs = np.array([0.1, 0.3, 1.0, 3.0, 10.0])
sim = [ensemble(g) for g in rs]
ax.semilogx(rs, sim, "o", ms=4.5, color=charts.line("negative"), label="simulation")
ax.set_ylim(0, 0.032)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, r"$\gamma_X/\gamma_Y$", r"$\eta_Y^2 = \mathrm{Var}(y)/\langle y\rangle^2$")
charts.title(ax, "B  Y averages fast upstream noise")

ax = axs[2]
ns = np.arange(1, 8)
for H, tok in [(0.5, "positive"), (1.0, "protein"), (2.0, "negative")]:
    out = []
    for n in ns:
        J = -np.eye(n)
        for i in range(1, n):
            J[i, i - 1] = H
        C = solve_continuous_lyapunov(J, -np.diag(np.full(n, 200.0)))
        out.append(C[-1, -1] / 100.0**2)
    ax.semilogy(ns, out, "o-", ms=4, lw=1.3, color=charts.line(tok), label=f"H = {H:g}")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "number of stages n", r"$\eta^2$ of the last stage")
charts.title(ax, "C  Cascades amplify or filter")
