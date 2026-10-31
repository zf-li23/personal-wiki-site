# Metropolis Monte Carlo and simulated annealing on a rugged two-dimensional energy landscape.
# E(x, y) = 0.6 [sin^2(3x) + sin^2(3y)] + 0.25 (x^2 + y^2)/4 - 2.5 exp(-[(x-2.2)^2 + (y+1.7)^2]/0.5)
# - 1.6 exp(-[(x+1.8)^2 + (y-1.6)^2]/1.0): many local minima from the oscillating term, a broad bowl, a
# deeper funnel at (2.2, -1.7) (global minimum) and a wider but shallower one at (-1.8, 1.6).
# Moves: Gaussian displacements of standard deviation 0.15, accepted with probability
# min(1, exp(-dE/T)); moves leaving the square [-4, 4]^2 are rejected. All runs start at (-3, -3).
# A: 4000 Metropolis steps at T = 0.05 (trapped near the start) and at T = 1.0 (wandering, but not
#    concentrated at the minimum).
# B: a simulated-annealing run, T(t) = T0 (T_end/T0)^(t/t_max) from T0 = 2.0 to T_end = 0.01 over
#    8000 steps (one of the runs that succeed): it explores at high temperature and settles in the
#    global minimum as T falls.
# C: energy of 30 independent annealing runs against step (thin lines) and the temperature schedule
#    (dashed, right axis); the fraction ending in the global funnel is given in the title, compared with
#    a rapid quench (T = 0.05 throughout). Unsuccessful annealing runs end in the wider, shallower
#    funnel: at intermediate temperatures its larger basin (higher entropy) is favoured, and by the time
#    the deeper funnel would win, barriers can no longer be crossed.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(4)


def energy(x, y):
    return (0.6 * (np.sin(3 * x) ** 2 + np.sin(3 * y) ** 2) + 0.25 * (x**2 + y**2) / 4
            - 2.5 * np.exp(-((x - 2.2) ** 2 + (y + 1.7) ** 2) / 0.5)
            - 1.6 * np.exp(-((x + 1.8) ** 2 + (y - 1.6) ** 2) / 1.0))


def metropolis(temps, start=(-3.0, -3.0), step=0.15):
    x = np.array(start, float)
    e = energy(*x)
    path, es = [x.copy()], [e]
    for T in temps:
        xn = x + step * rng.standard_normal(2)
        if np.abs(xn).max() > 4:                     # reflecting walls: reject moves out of the box
            path.append(x.copy())
            es.append(e)
            continue
        en = energy(*xn)
        if en <= e or rng.random() < np.exp(-(en - e) / T):
            x, e = xn, en
        path.append(x.copy())
        es.append(e)
    return np.array(path), np.array(es)


g = np.linspace(-4, 4, 300)
X, Y = np.meshgrid(g, g)
Z = energy(X, Y)
fig, axs = plt.subplots(1, 3, figsize=(14, 4.4), gridspec_kw={"width_ratios": [1, 1, 1.3]})
for ax in axs[:2]:
    ax.contourf(X, Y, Z, levels=30, cmap="Greys_r", alpha=0.85)
    ax.plot(2.2, -1.7, "*", color=charts.line("highlight"), ms=11, zorder=5)
    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xticks([])
    ax.set_yticks([])
ax = axs[0]
for T, tok in ((0.05, "negative"), (1.0, "dna")):
    pth, _ = metropolis(np.full(4000, T))
    ax.plot(pth[:, 0], pth[:, 1], color=charts.line(tok), lw=0.6, label=f"T = {T}")
ax.legend(fontsize=7.5, loc="upper right", framealpha=0.9, facecolor=P.surface(), edgecolor=P.muted())
charts.title(ax, "A   Metropolis at fixed T")
ax = axs[1]
steps = 8000
sched = 2.0 * (0.01 / 2.0) ** (np.arange(steps) / steps)
for _ in range(20):                                  # show a run that ends in the global funnel
    pth, ees = metropolis(sched)
    if ees[-1] < energy(2.2, -1.7) + 0.5:
        break
pts = ax.scatter(pth[::8, 0], pth[::8, 1], c=np.arange(len(pth))[::8], cmap="viridis", s=2, zorder=4)
charts.title(ax, "B   Simulated annealing (colour = time)")
ax = axs[2]
final = []
for r in range(30):
    _, es = metropolis(sched)
    ax.plot(es, color=charts.line("protein"), lw=0.4, alpha=0.6)
    final.append(es[-1])
quench = [metropolis(np.full(steps, 0.05))[1][-1] for _ in range(30)]
gmin = Z.min()
succ = np.mean(np.array(final) < gmin + 0.5)
succ_q = np.mean(np.array(quench) < gmin + 0.5)
ax.axhline(gmin, color=charts.line("highlight"), lw=0.8, ls=":")
ax2 = ax.twinx()
ax2.plot(sched, color=charts.line("negative"), lw=1.0, ls="--")
ax2.set_ylabel("temperature T (dashed)", fontsize=8, color=P.muted())
ax2.tick_params(colors=P.muted(), labelcolor=P.muted(), labelsize=7)
for name, sp in ax2.spines.items():
    sp.set_visible(name == "right")
    sp.set_color(P.muted())
charts.style_axes(ax, "Monte Carlo step", "energy E")
charts.title(ax, f"C   30 runs: annealing {succ:.0%}, quench {succ_q:.0%} reach the global minimum")
fig.tight_layout()
