"""Fringes of quasi-monochromatic light: a flat spectrum of relative width 0.1 washes out
the fringes near the order k_M = lambda / delta_lambda = 10."""

import numpy as np
import matplotlib.pyplot as plt

lam0 = 1.0
rel = 0.1                     # delta_lambda / lambda
sig0 = 1.0 / lam0             # central wavenumber 1/lambda
dsig = rel * sig0             # spectral width in 1/lambda
delta = np.linspace(0, 24, 4000)   # optical path difference in units of lambda0

sigs = np.linspace(sig0 - dsig / 2, sig0 + dsig / 2, 61)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 5.2), sharex=True)
for j, s in enumerate(sigs[[0, 30, 60]]):
    ax1.plot(delta, 1 + np.cos(2 * np.pi * s * delta), lw=0.9, color=f"C{j}",
             label=f"λ = {1 / s:.3f} λ0")
ax1.set_ylabel("I (single λ)")
ax1.legend(fontsize=7, ncol=3, loc="lower left", frameon=False)
ax1.set_ylim(-0.45, 2.1)
ax1.set_xlim(0, 24)

I = np.mean(1 + np.cos(2 * np.pi * np.outer(delta, sigs)), axis=1)
env = np.abs(np.sinc(dsig * delta))          # np.sinc(x) = sin(pi x)/(pi x)
ax2.plot(delta, I, color="C0", lw=1.2, label="sum over the line")
ax2.plot(delta, 1 + env, color="0.5", ls="--", lw=0.9, label="1 ± |sinc|, V = |sin u / u|")
ax2.plot(delta, 1 - env, color="0.5", ls="--", lw=0.9)
ax2.axvline(1 / dsig, color="C3", lw=0.9, ls=":")
ax2.text(1 / dsig + 0.3, 1.85, "δ_M = λ²/Δλ", color="C3", fontsize=9)
ax2.set_xlabel("optical path difference  δ / λ0")
ax2.set_ylabel("I (quasi-monochromatic)")
ax2.set_xlim(0, 24)
ax2.set_ylim(0, 2.1)
ax2.legend(fontsize=8, loc="lower right", frameon=False)
fig.tight_layout()
