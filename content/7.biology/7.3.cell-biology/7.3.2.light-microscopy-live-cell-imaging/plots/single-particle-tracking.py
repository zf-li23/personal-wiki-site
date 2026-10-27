# Single-particle tracking and the mean squared displacement (MSD) in two dimensions.
# Simulated tracks (frame interval 0.05 s, 200 frames, localization error 20 nm):
#   free diffusion, D = 0.1 um^2/s:                 MSD = 4 D tau (+ 4 sigma^2 offset)
#   confined diffusion in a square corral of 0.4 um: MSD saturates at L^2/3 (L^2/6 per axis)
#   directed motion, D = 0.02 um^2/s plus v = 0.5 um/s: MSD = 4 D tau + v^2 tau^2
# A: the three trajectories. B: their time-averaged MSD curves on log-log axes (slope 1: diffusion; slope 2:
# transport; plateau: confinement).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
dt, n, err = 0.05, 200, 0.02


def track(D, v=0.0, box=None):
    x = np.zeros((n, 2))
    for i in range(1, n):
        x[i] = x[i - 1] + rng.normal(0, np.sqrt(2 * D * dt), 2) + np.array([v * dt, 0])
        if box is not None:
            for k in range(2):
                if x[i, k] > box / 2:
                    x[i, k] = box - x[i, k]
                if x[i, k] < -box / 2:
                    x[i, k] = -box - x[i, k]
    return x + rng.normal(0, err, x.shape)


def msd(x, lags):
    return np.array([np.mean(np.sum((x[l:] - x[:-l]) ** 2, axis=1)) for l in lags])


tracks = [("free, D = 0.1 µm²/s", track(0.1), "dna"), ("confined (0.4 µm corral)", track(0.1, box=0.4), "negative"),
          ("directed, v = 0.5 µm/s", track(0.02, v=0.5), "positive")]
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
offs = [(-2.2, 0.0), (0.0, 0.0), (0.8, -1.6)]
for (txt, x, tok), (ox, oy) in zip(tracks, offs):
    ax.plot(x[:, 0] - x[0, 0] + ox, x[:, 1] - x[0, 1] + oy, color=charts.line(tok), lw=0.9)
    ax.plot([ox], [oy], "o", color=charts.line(tok), ms=4)
ax.plot([3.4, 4.4], [-2.4, -2.4], color=P.ink(), lw=2)
ax.text(3.9, -2.3, "1 µm", fontsize=7, color=P.ink(), ha="center", va="bottom")
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_title("A   Trajectories (10 s each)", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
lags = np.unique(np.logspace(0, np.log10(n // 4), 25).astype(int))
tau = lags * dt
for txt, x, tok in tracks:
    ax.loglog(tau, msd(x, lags), "o", ms=3.5, color=charts.line(tok), label=txt)
tt = np.logspace(np.log10(dt), np.log10(tau[-1]), 50)
ax.loglog(tt, 4 * 0.1 * tt + 4 * err**2, color=charts.line("dna"), lw=1.0, ls="--")
ax.loglog(tt, 4 * 0.02 * tt + 0.25 * tt**2 + 4 * err**2, color=charts.line("positive"), lw=1.0, ls="--")
ax.axhline(2 * 0.4**2 / 6 + 4 * err**2, color=charts.line("negative"), lw=1.0, ls="--")
ax.text(0.06, 0.8, "dashed: theory", fontsize=7, color=P.muted())
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "lag time τ / s", "MSD / µm²")
ax.set_title("B   MSD(τ) distinguishes the modes", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
