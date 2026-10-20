"""A signal made of 5 Hz and 12 Hz sine waves plus Gaussian noise, sampled at
100 Hz for 4 s, and its one-sided amplitude spectrum from scipy.fft.rfft."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

rng = np.random.default_rng(1)
fs = 100.0
t = np.arange(0, 4, 1 / fs)
clean = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)
signal = clean + 0.8 * rng.standard_normal(t.size)

amplitude = 2 * np.abs(fft.rfft(signal)) / t.size
freq = fft.rfftfreq(t.size, d=1 / fs)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(t, signal, color="C7", lw=0.8, label="noisy signal")
ax1.plot(t, clean, color="C0", lw=1.5, label="noise-free part")
ax1.set_xlim(0, 1)
ax1.set_xlabel("t (s)")
ax1.set_title("first second of the signal")
ax1.legend(fontsize=8, loc="upper right")
ax1.grid(alpha=0.3)
ax2.plot(freq, amplitude, color="C0")
ax2.set_xlabel("frequency (Hz)")
ax2.set_ylabel("amplitude")
ax2.set_title("one-sided amplitude spectrum")
ax2.grid(alpha=0.3)
fig.tight_layout()
