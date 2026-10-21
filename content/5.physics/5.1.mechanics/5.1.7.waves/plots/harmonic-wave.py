"""Plane harmonic wave: waveform at several times and oscillation curves at two points."""

import numpy as np
import matplotlib.pyplot as plt

A, lam, T = 1.0, 1.0, 1.0
k, w = 2 * np.pi / lam, 2 * np.pi / T

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))

x = np.linspace(0, 2.0, 600)
for i, t in enumerate([0, T / 8, T / 4]):
    ax1.plot(x, A * np.cos(w * t - k * x), color=f"C{i}", lw=1.8, label=f"t = {t:g} T")
# follow one crest: x = u t
for i, t in enumerate([0, T / 8, T / 4]):
    xc = lam * t / T + lam
    ax1.plot([xc], [A], "o", color=f"C{i}", ms=5)
ax1.annotate("", xy=(1.25, 1.18), xytext=(1.0, 1.18), arrowprops=dict(arrowstyle="->", lw=1.2))
ax1.text(1.125, 1.24, "u", ha="center", fontsize=10)
ax1.set_ylim(-1.35, 1.45)
ax1.set_xlabel("x / λ")
ax1.set_ylabel("y / A")
ax1.set_title("Waveform y(x) at fixed t")
ax1.legend(loc="lower left", fontsize=8, ncol=3)

t = np.linspace(0, 2.0, 600)
ax2.plot(t, A * np.cos(w * t), color="C0", lw=1.8, label="x = 0")
ax2.plot(t, A * np.cos(w * t - k * lam / 4), color="C3", lw=1.8, ls="--", label="x = λ/4")
ax2.set_ylim(-1.35, 1.45)
ax2.set_xlabel("t / T")
ax2.set_ylabel("y / A")
ax2.set_title("Oscillation y(t) at fixed x")
ax2.legend(loc="lower left", fontsize=8, ncol=2)

fig.tight_layout()
