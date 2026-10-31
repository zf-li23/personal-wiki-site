"""Anomalous diffusion: four mechanisms and an obstruction model (simulations, arbitrary units).
A: ensemble-averaged mean squared displacement of Brownian motion (alpha = 1), fractional
Brownian motion with Hurst exponent H = 0.35 (alpha = 2H = 0.7, antipersistent steps, as in a
viscoelastic medium), a continuous-time random walk with power-law waiting times psi(t) ~
t^-(1+a), a = 0.6 (alpha = 0.6, trapping), and a persistent random walk (alpha = 2 at short
times, 1 at long times, as for motor-driven or swimming particles). B: for the continuous-time
random walk, the time-averaged MSD of single trajectories (thin lines) is linear in the lag and
scatters widely between trajectories and lies below the subdiffusive ensemble average (thick):
weak ergodicity breaking. C: tracer diffusion on a square lattice among immobile obstacles occupying a
fraction phi of the sites: the long-time diffusion coefficient falls faster than the mean-field
1 - phi and vanishes at the percolation threshold phi_c = 0.407, near which motion is anomalous
over long times."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.97, bottom=0.17, top=0.87)

N, M = 2048, 300
lags = np.unique(np.logspace(0, np.log10(N / 4), 30).astype(int))


def ens_msd(X):
    return np.array([np.mean((X[:, l] - X[:, 0]) ** 2) for l in lags])


# Brownian motion
bm = np.cumsum(rng.normal(size=(M, N)), axis=1)
# fractional Gaussian noise by circulant embedding (Davies-Harte)
H = 0.35
k = np.arange(N)
gam = 0.5 * (np.abs(k + 1) ** (2 * H) - 2 * np.abs(k) ** (2 * H) + np.abs(k - 1) ** (2 * H))
row = np.concatenate([gam, [0], gam[1:][::-1]])
lam = np.clip(np.fft.fft(row).real, 0, None)
W = rng.normal(size=(M, 2 * N)) + 1j * rng.normal(size=(M, 2 * N))
fgn = np.fft.fft(np.sqrt(lam / (2 * N)) * W, axis=1).real[:, :N]
fbm = np.cumsum(fgn, axis=1)
# persistent random walk: velocity Ornstein-Uhlenbeck with correlation time 30 steps
tauv = 30.0
v = np.zeros((M, N))
for i in range(1, N):
    v[:, i] = v[:, i - 1] * (1 - 1 / tauv) + np.sqrt(2 / tauv) * rng.normal(size=M)
prw = np.cumsum(v, axis=1)
# CTRW on a time grid
a = 0.6
T = N
ctrw = np.zeros((M, N))
for m in range(M):
    t, x, path = 0.0, 0.0, np.zeros(N)
    last = 0
    while t < T:
        w = (rng.pareto(a) + 1.0) * 0.5
        t_new = t + w
        i0, i1 = int(np.ceil(t)), min(int(np.ceil(t_new)), N)
        path[i0:i1] = x
        x += rng.normal()
        t = t_new
    ctrw[m] = path

ax = axs[0]
for X, tok, lab, alpha in ((bm, "dna", r"Brownian, $\alpha = 1$", 1), (fbm, "bacterium", r"fBm, $H = 0.35$", 0.7),
                           (ctrw, "blood", r"CTRW, $a = 0.6$", 0.6), (prw, "highlight", "persistent walk", None)):
    m = ens_msd(X)
    j = np.argmin(np.abs(lags - 100))
    m = m * 100 / m[j]
    ax.plot(lags, m, "o", ms=3, color=charts.line(tok), label=lab)
    if alpha:
        ax.plot(lags, 100 * (lags / lags[j]) ** alpha, color=charts.line(tok), lw=0.8)
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "lag time / step", "MSD (scaled to 100 at lag 100)")
charts.title(ax, r"A  $\langle x^2\rangle \propto t^{\alpha}$")

ax = axs[1]
for m in range(12):
    x = ctrw[m]
    ta = np.array([np.mean((x[l:] - x[:-l]) ** 2) for l in lags])
    ax.plot(lags, ta, color=charts.line("blood"), lw=0.6, alpha=0.6)
ax.plot(lags, ens_msd(ctrw), color=P.ink(), lw=2, label="ensemble average")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "lag time / step", "time-averaged MSD")
charts.title(ax, "B  Single CTRW trajectories")

ax = axs[2]
Lg, nt, steps = 96, 400, 6000
phis = np.array([0.0, 0.1, 0.2, 0.25, 0.3, 0.35, 0.38])
Ds = []
moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
for ph in phis:
    obst = rng.random((Lg, Lg)) < ph
    free = np.argwhere(~obst)
    pos = free[rng.integers(len(free), size=nt)].astype(int)
    start = pos.copy()
    unw = np.zeros_like(pos)
    for _ in range(steps):
        mv = moves[rng.integers(4, size=nt)]
        new = (pos + mv) % Lg
        ok = ~obst[new[:, 0], new[:, 1]]
        pos[ok] = new[ok]
        unw[ok] += mv[ok]
    Ds.append(np.mean(np.sum(unw**2, axis=1)) / (steps))
Ds = np.array(Ds)
ax.plot(phis, Ds / Ds[0], "o", color=charts.line("blood"), ms=4, label="simulation")
pp = np.linspace(0, 0.45, 100)
ax.plot(pp, 1 - pp, color=P.muted(), lw=1.0, ls="--", label=r"mean field $1 - \varphi$")
ax.axvline(0.407, color=P.muted(), lw=0.7, ls=":")
ax.text(0.41, 0.85, r"$\varphi_c$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"obstacle fraction $\varphi$", r"$D/D_0$ (after 6000 steps)")
charts.title(ax, "C  Obstructed diffusion")
