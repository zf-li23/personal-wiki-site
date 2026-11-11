"""Theta phase precession of a place cell (dual-oscillator model).

A rat runs at v = 25 cm/s along a 2 m track through a place field centered at x = 100 cm
(Gaussian envelope, sigma = 12 cm). The local field potential theta oscillates at
f_theta = 8 Hz. Inside its field the cell's membrane oscillates slightly faster,
f_cell = f_theta + v / L with L = 60 cm, so its preferred firing phase relative to the LFP
advances by one full cycle over a distance L (O'Keefe and Recce, 1993).
Rate: r(t) = r_max G(x(t)) [ (1 + cos(2 pi f_cell t)) / 2 ]^4, with r_max = 120 Hz.
Spikes: inhomogeneous Poisson process, 12 laps (seed 0).
A: one lap: LFP theta (gray) and spikes (ticks) while the rat crosses the field.
B: spike phase against position for all laps (each spike drawn twice, phase and phase + 360 deg).
C: rate map (spike count per 2 cm bin / time per bin).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
v, ftheta, L, x0, sig, rmax = 25.0, 8.0, 60.0, 100.0, 12.0, 120.0
fcell = ftheta + v / L
dt = 0.0005
t = np.arange(0, 200.0 / v, dt)
x = v * t
G = np.exp(-((x - x0) ** 2) / (2 * sig**2))
rate = rmax * G * ((1 + np.cos(2 * np.pi * fcell * t - 2 * np.pi * (fcell - ftheta) * (x0 - L / 2) / v)) / 2) ** 4
theta_phase = np.mod(2 * np.pi * ftheta * t, 2 * np.pi)

laps = []
for lap in range(12):
    spk = rng.random(t.size) < rate * dt
    laps.append(np.flatnonzero(spk))

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8), gridspec_kw=dict(width_ratios=[1.5, 1, 1]))
ax = axs[0]
sel = (x > 55) & (x < 145)
ax.plot(x[sel], np.cos(theta_phase[sel]), color=P.muted(), lw=1.0, label="LFP theta")
ax.plot(x[sel], 2.4 * G[sel] - 1.2 + 0 * x[sel], color=P.edge("dna"), lw=1.6, ls="--", label="Field envelope")
idx = laps[0]
idx = idx[(x[idx] > 55) & (x[idx] < 145)]
ax.vlines(x[idx], 1.25, 1.65, color=P.edge("negative"), lw=1.2)
ax.text(57, 1.75, "Spikes", fontsize=8, color=P.edge("negative"))
ax.set_xlim(55, 145)
ax.set_ylim(-1.4, 2.1)
ax.set_yticks([])
ax.set_xlabel("Position / cm")
ax.set_title("A  One pass through the field", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")

ax = axs[1]
for idx in laps:
    ph = np.degrees(theta_phase[idx])
    ax.plot(x[idx], ph, ".", ms=3, color=P.edge("negative"))
    ax.plot(x[idx], ph + 360, ".", ms=3, color=P.edge("negative"))
ax.set_xlim(60, 140)
ax.set_ylim(0, 720)
ax.set_yticks([0, 180, 360, 540, 720])
ax.set_xlabel("Position / cm")
ax.set_ylabel("Theta phase / deg")
ax.set_title("B  Phase precession", loc="left", fontsize=10)

ax = axs[2]
edges = np.arange(0, 202, 2)
cnt = np.zeros(edges.size - 1)
for idx in laps:
    cnt += np.histogram(x[idx], edges)[0]
occ = 12 * (2.0 / v)
ax.bar(edges[:-1] + 1, cnt / occ, width=2, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4)
ax.set_xlim(40, 160)
ax.set_xlabel("Position / cm")
ax.set_ylabel("Rate / Hz")
ax.set_title("C  Rate map", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
