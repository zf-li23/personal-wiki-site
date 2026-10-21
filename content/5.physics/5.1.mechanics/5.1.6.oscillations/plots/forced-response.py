"""Steady-state amplitude and phase of a driven damped oscillator."""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.0, 2.5, 2000)  # omega / omega0
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))
for Q in [0.5, 1, 2, 5, 10]:
    # with beta / omega0 = 1 / (2 Q): A k / F0 = 1 / sqrt((1 - r^2)^2 + (r / Q)^2)
    denom = (1 - r**2) + 1j * r / Q
    amp = 1 / np.abs(denom)
    phase = -np.angle(denom)  # displacement lags the force, between -pi and 0
    ax1.plot(r, amp, lw=1.8, label=f"Q = {Q}")
    ax2.plot(r, phase, lw=1.8, label=f"Q = {Q}")
ax1.axvline(1, color="0.5", lw=0.8, ls=":")
ax1.set_xlabel("omega / omega0")
ax1.set_ylabel("A k / F0")
ax1.set_ylim(0, 11)
ax1.set_xlim(0, 2.5)
ax1.legend()
ax1.set_title("Amplitude response")

ax2.axvline(1, color="0.5", lw=0.8, ls=":")
ax2.axhline(-np.pi / 2, color="0.5", lw=0.8, ls=":")
ax2.set_yticks([0, -np.pi / 2, -np.pi])
ax2.set_yticklabels(["0", "-pi/2", "-pi"])
ax2.set_xlabel("omega / omega0")
ax2.set_ylabel("phi0")
ax2.set_xlim(0, 2.5)
ax2.legend(loc="upper right")
ax2.set_title("Phase of the displacement")
fig.tight_layout()
