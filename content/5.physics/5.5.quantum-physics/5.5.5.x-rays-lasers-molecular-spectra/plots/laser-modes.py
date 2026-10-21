"""Longitudinal modes of a laser cavity under the Doppler-broadened gain curve of the 632.8 nm neon line."""

import numpy as np
import matplotlib.pyplot as plt

c = 2.998e8
fwhm = 1.5e9  # Hz, Doppler width of the gain curve
sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
threshold = 0.5  # gain needed to overcome cavity losses (relative units)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0), sharey=True)
dnu = np.linspace(-2.5e9, 2.5e9, 3000)
for ax, L in zip(axes, [1.0, 0.1]):
    gain = np.exp(-0.5 * (dnu / sigma) ** 2)
    ax.plot(dnu / 1e9, gain, color="C0", lw=1.6, label="gain curve")
    ax.axhline(threshold, color="0.4", ls="--", lw=1, label="threshold (losses)")
    spacing = c / (2 * L)
    offset = 0.3 * spacing  # cavity resonances need not sit at the line centre
    q = np.arange(-40, 41)
    modes = offset + q * spacing
    modes = modes[np.abs(modes) < 2.5e9]
    n_lasing = 0
    for m in modes:
        g = np.exp(-0.5 * (m / sigma) ** 2)
        on = g > threshold
        n_lasing += on
        ax.plot([m / 1e9] * 2, [0, g if on else 0.08], color="C3" if on else "0.6", lw=2.2 if on else 1)
    ax.set_title(f"L = {L:g} m: mode spacing c/2L = {spacing / 1e9:.2g} GHz, {n_lasing} lasing mode(s)", fontsize=10)
    ax.set_xlabel(r"$\nu - \nu_0$ / GHz")
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(0, 1.12)
axes[0].set_ylabel("gain (relative)")
axes[0].legend(fontsize=8, loc="upper left")
fig.tight_layout()
