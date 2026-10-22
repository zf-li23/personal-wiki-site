"""Brownian motion of a sphere of radius 100 nm in water at 25 C (D = k_B T / (6 pi eta r)
= 2.45 um^2/s), simulated as a random walk with Gaussian steps every 0.01 s. Left: three
trajectories over 10 s. Right: mean squared displacement in the plane averaged over 2000
particles against time, compared with the Einstein-Smoluchowski law <r^2> = 4 D t."""

import numpy as np
import matplotlib.pyplot as plt

kB, T, eta, r = 1.380649e-23, 298.15, 0.890e-3, 100e-9
D = kB * T / (6 * np.pi * eta * r) * 1e12   # um^2 s^-1
dt, n = 0.01, 1000
rng = np.random.default_rng(0)
steps = rng.normal(0, np.sqrt(2 * D * dt), size=(2000, n, 2))
pos = np.cumsum(steps, axis=1)
t = dt * np.arange(1, n + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.8))
for k, col in enumerate(["C0", "C1", "C3"]):
    xy = np.vstack([[0, 0], pos[k]])
    ax1.plot(xy[:, 0], xy[:, 1], color=col, lw=0.7)
    ax1.plot(xy[-1, 0], xy[-1, 1], "o", color=col, ms=3)
ax1.plot(0, 0, "ko", ms=3)
ax1.set_aspect("equal")
ax1.set_xlabel(r"$x\,/\,\mu\mathrm{m}$")
ax1.set_ylabel(r"$y\,/\,\mu\mathrm{m}$")

msd = (pos**2).sum(axis=2).mean(axis=0)
ax2.plot(t, msd, color="C0", lw=1.8, label="simulation, 2000 particles")
ax2.plot(t, 4 * D * t, color="C3", lw=1.2, ls="--", label=rf"$4Dt$, $D$ = {D:.2f} $\mu$m$^2$ s$^{{-1}}$")
ax2.set_xlim(0, 10)
ax2.set_ylim(0, None)
ax2.set_xlabel(r"$t\,/\,\mathrm{s}$")
ax2.set_ylabel(r"$\langle r^2\rangle\,/\,\mu\mathrm{m}^2$")
ax2.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
