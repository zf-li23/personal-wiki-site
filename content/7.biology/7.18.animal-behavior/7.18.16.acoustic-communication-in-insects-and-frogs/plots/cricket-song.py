"""The calling song of a field cricket at three time scales (synthetic, Gryllus-like parameters).

Chirps of 4 syllables (pulses) repeated 3 times per second; each syllable lasts 18 ms with a
syllable period of 35 ms; the carrier is an almost pure tone of 4.8 kHz produced by the harp
resonator (one cycle per tooth strike). Amplitude envelopes rise and decay within each syllable.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fs = 100_000
fc, syl, per, nsyl, chirp_rate = 4800.0, 0.018, 0.035, 4, 3.0
t = np.arange(0, 1.4, 1 / fs)
env = np.zeros_like(t)
for c in np.arange(0.05, 1.4, 1 / chirp_rate):
    for k in range(nsyl):
        t0 = c + k * per
        m = (t >= t0) & (t < t0 + syl)
        x = (t[m] - t0) / syl
        env[m] = np.sin(np.pi * x) ** 0.6 * (1 - 0.15 * k)
s = env * np.sin(2 * np.pi * fc * t)
fig, axs = plt.subplots(3, 1, figsize=(10.5, 5.0))
axs[0].plot(t, s, color=P.edge("dna"), lw=0.4)
axs[0].set_xlim(0, 1.4)
axs[0].set_xlabel("Time / s")
axs[0].set_title("A  Chirps (about 3 per second)", loc="left", fontweight="bold", fontsize=9.5)
m = (t > 0.04) & (t < 0.2)
axs[1].plot(t[m] * 1e3, s[m], color=P.edge("dna"), lw=0.5)
for k in range(nsyl):
    x0 = 50 + k * per * 1e3
    axs[1].annotate("", (x0 + syl * 1e3, 1.15), (x0, 1.15), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.7))
axs[1].text(50, 1.3, "syllable 18 ms, syllable period 35 ms", fontsize=7.5, color=P.muted())
axs[1].set_ylim(-1.2, 1.6)
axs[1].set_xlabel("Time / ms")
axs[1].set_title("B  One chirp of four syllables", loc="left", fontweight="bold", fontsize=9.5)
m = (t > 0.058) & (t < 0.0605)
axs[2].plot(t[m] * 1e3, s[m], color=P.edge("dna"), lw=1.2)
axs[2].set_xlabel("Time / ms")
axs[2].set_title("C  Carrier: a nearly pure 4.8 kHz tone (one cycle per tooth strike)", loc="left", fontweight="bold", fontsize=9.5)
for ax in axs:
    ax.set_yticks([])
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
