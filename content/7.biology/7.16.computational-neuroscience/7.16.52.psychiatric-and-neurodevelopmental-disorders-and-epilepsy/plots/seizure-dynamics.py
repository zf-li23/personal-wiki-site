"""Seizure onset and offset as bifurcations of a fast oscillator driven by a slow variable.

Fast subsystem: normal form of a subcritical Hopf bifurcation with a fold of limit cycles,
  dz/dt = g (mu + |z|^2 - |z|^4) z + i omega z + noise,   z = x + i y, omega = 2 pi * 3 (3 Hz), g = 20 /s,
which for -1/4 < mu < 0 is bistable (rest and a large limit cycle) and for mu > 0 has only the cycle.
Slow variable (an "excitability" such as extracellular K+ or a permittivity variable):
  d mu / dt = eps (a - |z|^2), eps = 0.02 /s, a = 0.4,
so mu rises during rest and falls during seizures: onset by the subcritical Hopf bifurcation (or earlier,
by noise, within the bistable range), offset at the fold of limit cycles (mu = -1/4).
Time unit seconds, Euler-Maruyama with dt = 1 ms, 150 s, noise std 0.05.
A: amplitude |z| against mu with the bifurcation diagram (stable rest, stable and unstable cycles).
B: the signal x(t) (an "EEG") and mu(t).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
dt, T = 1e-3, 150.0
g = 20.0
om = 2 * np.pi * 3.0
eps, a, sig = 0.02, 0.4, 0.05
n = int(T / dt)
z = 0.01 + 0j
mu = -0.2
xs = np.empty(n)
ms = np.empty(n)
rs = np.empty(n)
for k in range(n):
    r2 = (z * z.conjugate()).real
    z = z + dt * (g * (mu + r2 - r2 * r2) * z + 1j * om * z) + sig * np.sqrt(dt) * (rng.normal() + 1j * rng.normal())
    mu = mu + dt * eps * (a - r2)
    xs[k] = z.real
    ms[k] = mu
    rs[k] = abs(z)
t = np.arange(n) * dt

fig, axs = plt.subplots(1, 2, figsize=(11.5, 3.9), gridspec_kw={"width_ratios": [1, 1.6]})
ax = axs[0]
mus = np.linspace(-0.35, 0.15, 400)
ax.plot(mus[mus < 0], 0 * mus[mus < 0], color=P.ink(), lw=2.0, label="rest (stable)")
ax.plot(mus[mus >= 0], 0 * mus[mus >= 0], color=P.ink(), lw=1.2, ls="--")
mm = mus[mus >= -0.25]
ax.plot(mm, np.sqrt((1 + np.sqrt(1 + 4 * mm)) / 2), color=P.edge("negative"), lw=2.0, label="seizure cycle (stable)")
m2 = mm[mm <= 0]
ax.plot(m2, np.sqrt((1 - np.sqrt(1 + 4 * m2)) / 2), color=P.edge("negative"), lw=1.2, ls="--", label="unstable cycle")
step = 20
ax.plot(ms[::step], rs[::step], color=P.edge("dna"), lw=0.5, alpha=0.6, label="trajectory")
ax.axvspan(-0.25, 0, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.text(-0.125, 1.35, "bistable", ha="center", fontsize=8, color=P.muted())
ax.set_xlabel("Slow excitability $\\mu$")
ax.set_ylabel("Oscillation amplitude $|z|$")
ax.set_ylim(-0.05, 1.45)
ax.legend(frameon=False, fontsize=7.5, loc="center right")
ax.set_title("A  Bifurcation diagram", loc="left", fontsize=10)
ax = axs[1]
ax.plot(t, xs, color=P.edge("dna"), lw=0.5)
ax.set_xlabel("Time / s")
ax.set_ylabel("Signal $x$")
ax2 = ax.twinx()
ax2.plot(t, ms, color=P.edge("negative"), lw=1.5)
ax2.axhline(0, color=P.edge("negative"), lw=0.6, ls=":")
ax2.axhline(-0.25, color=P.edge("negative"), lw=0.6, ls=":")
ax2.set_ylabel("$\\mu$", color=P.edge("negative"))
ax2.set_ylim(-0.6, 0.15)
ax.set_ylim(-1.5, 3.0)
ax.set_title("B  Recurrent seizures: onset at Hopf, offset at fold", loc="left", fontsize=10)
fig.tight_layout()
