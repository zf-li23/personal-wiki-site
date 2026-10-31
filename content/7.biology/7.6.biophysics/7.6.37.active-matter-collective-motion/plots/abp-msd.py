"""Active Brownian particles in two dimensions (Definition 37.2.1): dr/dt = v0 n(theta) + sqrt(2 D_t) xi,
dtheta/dt = sqrt(2 D_r) eta, with v0 = 1, D_r = 1 (rotational time tau_r = 1) and D_t = 0.01.
A: trajectories of length 20 tau_r for the active particle and for a passive particle with the same
translational diffusion (inset scale). B: mean squared displacement of 500 particles (points)
against time, with the exact result 4 D_t t + 2 v0^2 tau_r [t - tau_r(1 - exp(-t/tau_r))] (line):
ballistic, ~ v0^2 t^2, for t << tau_r and diffusive with D_eff = D_t + v0^2 tau_r/2 for t >> tau_r;
the dashed line is passive diffusion."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(8)
v0, Dr, Dt, dt = 1.0, 1.0, 0.01, 0.005


def abp(n, T, v=v0):
    steps = int(T / dt)
    th = rng.uniform(0, 2 * np.pi, n)
    pos = np.zeros((n, 2))
    out = np.empty((steps + 1, n, 2))
    out[0] = pos
    for i in range(steps):
        pos = pos + v * dt * np.column_stack((np.cos(th), np.sin(th))) + np.sqrt(2 * Dt * dt) * rng.standard_normal((n, 2))
        th = th + np.sqrt(2 * Dr * dt) * rng.standard_normal(n)
        out[i + 1] = pos
    return out


fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.6))
fig.subplots_adjust(wspace=0.3, left=0.07, right=0.98, bottom=0.15, top=0.89)
ax = axs[0]
tr = abp(4, 20)
for j, tok in enumerate(["bacterium", "receptor", "enzyme", "highlight"]):
    ax.plot(tr[:, j, 0], tr[:, j, 1], color=charts.line(tok), lw=0.8)
pas = abp(1, 20, v=0.0)
ax.plot(pas[:, 0, 0], pas[:, 0, 1], color=P.ink(), lw=0.8)
ax.set_aspect("equal")
charts.style_axes(ax, r"x / $v_0\tau_{\mathrm{r}}$", r"y / $v_0\tau_{\mathrm{r}}$")
charts.title(ax, "A  active and passive tracks")

ax = axs[1]
tr = abp(500, 50)
t = np.arange(tr.shape[0]) * dt
idx = np.unique(np.logspace(0, np.log10(t.size - 1), 30).astype(int))
msd = (tr[idx] ** 2).sum(-1).mean(1)
tf = np.logspace(-2.3, np.log10(50), 200)
theory = 4 * Dt * tf + 2 * v0 ** 2 / Dr * (tf - (1 - np.exp(-Dr * tf)) / Dr)
ax.loglog(t[idx], msd, "o", color=charts.line("bacterium"), ms=3.5)
ax.loglog(tf, theory, color=charts.line("bacterium"), lw=1.2, label="active")
ax.loglog(tf, 4 * Dt * tf, "--", color=P.muted(), lw=1.0, label="passive")
ax.loglog(tf[tf < 0.5], (v0 * tf[tf < 0.5]) ** 2, ":", color=P.ink(), lw=0.9)
ax.text(0.2, 0.012, r"$\propto t^2$", fontsize=7, color=P.ink())
ax.text(8, 30, r"$\propto t$", fontsize=7, color=P.ink())
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, r"time / $\tau_{\mathrm{r}}$", "mean squared displacement")
charts.title(ax, "B  ballistic to diffusive")
