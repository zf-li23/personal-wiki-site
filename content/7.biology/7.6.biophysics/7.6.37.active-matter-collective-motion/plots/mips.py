"""Motility-induced phase separation of active Brownian particles whose speed decreases with the
local density, v(rho) = v0 exp(-rho/rho*), without any attraction. N = 2000 particles in a periodic
box of side 40, v0 = 1, D_r = 0.05, local density counted within radius 2. A: rho0/rho* = 0.6,
below the spinodal: the suspension stays homogeneous. B: rho0/rho* = 2, inside the spinodal
(Theorem 37.5.1): dense, slow clusters form spontaneously and coarsen, surrounded by a dilute fast
gas (snapshots after 100 rotational times). C: the effective diffusion coefficient of the
coarse-grained density, D_eff(rho) = v(v + rho v')/(2 D_r), becomes negative for rho > rho* (the condition
v'/v < -1/rho),
where small density fluctuations grow."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(6)
N, L, v0, Dr, dt, r = 2000, 40.0, 1.0, 0.05, 0.1, 2.0
rho0 = N / L ** 2


def run(rho_star, steps=1000):
    x = rng.uniform(0, L, (N, 2))
    th = rng.uniform(0, 2 * np.pi, N)
    for _ in range(steps):
        cnt = cKDTree(x, boxsize=L).query_ball_point(x, r, return_length=True)
        rho = cnt / (np.pi * r * r)
        v = v0 * np.exp(-rho / rho_star)
        x = (x + dt * v[:, None] * np.column_stack((np.cos(th), np.sin(th)))) % L
        x[x >= L] = 0.0
        th = th + np.sqrt(2 * Dr * dt) * rng.standard_normal(N)
    return x, rho


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.5))
fig.subplots_adjust(wspace=0.3, left=0.05, right=0.98, bottom=0.15, top=0.88)
for ax, frac, ttl in ((axs[0], 0.6, r"A  $\rho_0/\rho^* = 0.6$: homogeneous"),
                      (axs[1], 2.0, r"B  $\rho_0/\rho^* = 2$: clusters")):
    x, rho = run(rho0 / frac)
    ax.scatter(x[:, 0], x[:, 1], s=1.5, c=charts.line("bacterium"), lw=0)
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, None, None, box=True)
    charts.title(ax, ttl)

ax = axs[2]
q = np.linspace(0, 3, 300)          # rho/rho*
v = np.exp(-q)
deff = v * (v - q * v) / 2           # v (v + rho v') / (2 D_r), in units of v0^2/D_r
ax.plot(q, deff, color=charts.line("bacterium"), lw=1.5)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(1.0, color=P.muted(), lw=0.6, ls=":")
ax.fill_between(q, deff, 0, where=deff < 0, color=P.light("negative"), lw=0)
for frac in (0.6, 2.0):
    ax.plot(frac, np.exp(-2 * frac) * (1 - frac) / 2, "o", color=P.ink(), ms=4)
ax.text(1.6, 0.1, "unstable", fontsize=7, color=P.ink())
charts.style_axes(ax, r"density $\rho/\rho^*$", r"$D_{\mathrm{eff}}$ / ($v_0^2/D_{\mathrm{r}}$)")
charts.title(ax, "C  negative effective diffusion")
