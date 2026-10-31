"""Cell migration as a persistent random walk: velocity is an Ornstein-Uhlenbeck process in two
dimensions with speed scale S and persistence time P. A: simulated 10 h trajectories (all starting at
the origin) for slow, persistent mesenchymal-like cells (S = 0.5 um/min, P = 30 min) and fast,
less persistent amoeboid-like cells (S = 8 um/min, P = 2 min). B: mean squared displacement of 200
simulated cells of each kind (dots) and the Furth formula <r^2> = 2 S^2 P [t - P(1 - exp(-t/P))]: ballistic
(slope 2) below the persistence time, diffusive (slope 1) above it, with D = S^2 P / 2."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.4))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.98, bottom=0.15, top=0.88)
dt, T = 0.5, 600.0
nt = int(T / dt)
rng = np.random.default_rng(0)


def walk(S, Pt, ncell):
    v = rng.normal(0, S / np.sqrt(2), (ncell, 2))
    a = np.exp(-dt / Pt)
    pos = np.zeros((nt, ncell, 2))
    for i in range(1, nt):
        v = a * v + np.sqrt(1 - a * a) * rng.normal(0, S / np.sqrt(2), (ncell, 2))
        pos[i] = pos[i - 1] + v * dt
    return pos


kinds = [("mesenchymal-like", 0.5, 30.0, "bacterium"), ("amoeboid-like", 8.0, 2.0, "blood")]
ax = axs[0]
res = {}
for lab, S, Pt, tok in kinds:
    pos = walk(S, Pt, 200)
    res[lab] = pos
    for j in range(6):
        ax.plot(pos[:, j, 0], pos[:, j, 1], color=charts.line(tok), lw=0.7, alpha=0.9, label=lab if j == 0 else None)
ax.set_aspect("equal")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(ax, r"$x$ / $\mu$m", r"$y$ / $\mu$m")
charts.title(ax, "A  Trajectories (10 h)")

ax = axs[1]
lags = np.unique(np.logspace(0, np.log10(nt / 4), 25).astype(int))
for lab, S, Pt, tok in kinds:
    pos = res[lab]
    msd = [np.mean(np.sum((pos[l:] - pos[:-l]) ** 2, axis=2)) for l in lags]
    t = lags * dt
    ax.loglog(t, msd, "o", ms=3, color=charts.line(tok))
    tt = np.logspace(np.log10(t[0]), np.log10(t[-1]), 100)
    ax.loglog(tt, 2 * S ** 2 * Pt * (tt - Pt * (1 - np.exp(-tt / Pt))), color=charts.line(tok), lw=1.3, label=lab)
    ax.axvline(Pt, color=charts.line(tok), lw=0.6, ls=":")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(ax, "lag time / min", r"MSD / $\mu$m$^2$")
charts.title(ax, "B  Ballistic to diffusive")
