"""Decomposition of N2O5 in CCl4 at 40 C: concentration-time curve with the tangent at t = 2700 s,
and the linearized plot ln c vs t fitted by least squares (first-order kinetics)."""

import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 300, 600, 900, 1200, 1800, 2400, 3000], dtype=float)
c = np.array([0.200, 0.180, 0.161, 0.144, 0.130, 0.104, 0.084, 0.068])

# least-squares fit of ln c = ln c0 - k t
slope, intercept = np.polyfit(t, np.log(c), 1)
k = -slope
c0 = np.exp(intercept)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

tt = np.linspace(0, 6000, 400)
ax1.plot(t, c, "o", color="C0", label="data")
ax1.plot(tt, c0 * np.exp(-k * tt), color="C0", lw=1.5, label="first-order fit")
t1 = 2700.0
c1 = c0 * np.exp(-k * t1)
s1 = -k * c1
ax1.plot(tt, c1 + s1 * (tt - t1), color="C3", ls="--", lw=1.2, label="tangent at t = 2700 s")
ax1.plot([t1], [c1], "s", color="C3")
ax1.set_xlim(0, 6000)
ax1.set_ylim(0, 0.22)
ax1.set_xlabel("t / s")
ax1.set_ylabel(r"$c(\mathrm{N_2O_5})$ / (mol L$^{-1}$)")
ax1.set_title(f"slope at 2700 s = {s1:.2e} mol L$^{{-1}}$ s$^{{-1}}$", fontsize=10)
ax1.legend(frameon=False, fontsize=9)

ax2.plot(t, np.log(c), "o", color="C0", label="data")
ax2.plot(tt[tt <= 3200], intercept + slope * tt[tt <= 3200], color="C0", lw=1.5,
         label=rf"fit: $k$ = {k:.2e} s$^{{-1}}$")
ax2.set_xlabel("t / s")
ax2.set_ylabel(r"$\ln\,[c / (\mathrm{mol\,L^{-1}})]$")
ax2.set_title("ln c is linear in t: first order", fontsize=10)
ax2.legend(frameon=False, fontsize=9)
fig.tight_layout()
