"""Viscoelastic filtering in skin mechanoreceptors.

A: gain of a cascade of N identical Maxwell elements, |H| = (w tau / sqrt(1 + (w tau)^2))^N
(N = 1, 5, 20, 60; frequency in units of 1/tau), and of a Kelvin-Voigt element driven by force,
1 / sqrt(1 + (w tau)^2) (low pass).
B: schematic tuning curve of a Pacinian ending: threshold amplitude = 1 / |H_capsule H_encoder|,
with an effective second-order high pass for the capsule (corner 120 Hz) and a first-order low pass
for the membrane and spike encoder (corner 300 Hz); removing the capsule leaves the low pass only.
Normalised to the minimum of the intact curve.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))

x = np.logspace(-2, 2.5, 600)
cols = [P.edge("dna"), P.edge("enzyme"), P.edge("protein"), P.edge("rna")]
for N, c in zip((1, 5, 20, 60), cols):
    g = (x / np.sqrt(1 + x**2)) ** N
    ax.plot(x, 20 * np.log10(g), color=c, lw=1.8, label=f"Maxwell, N = {N}")
ax.plot(x, 20 * np.log10(1 / np.sqrt(1 + x**2)), color=P.muted(), lw=1.6, ls="--",
        label="Kelvin-Voigt (low pass)")
ax.axhline(-3, color=P.muted(), lw=0.7, ls=":")
ax.set_xscale("log")
ax.set_ylim(-60, 5)
ax.set_xlim(x[0], x[-1])
ax.set_xlabel(r"Normalised frequency $\omega\tau$")
ax.set_ylabel("Gain / dB")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Layers sharpen the high pass", loc="left", fontsize=10)

f = np.logspace(0, 3.5, 800)
w = 2 * np.pi * f
th, tl = 1 / (2 * np.pi * 120), 1 / (2 * np.pi * 300)
hp = (1j * w * th / (1 + 1j * w * th)) ** 2
lp = 1 / (1 + 1j * w * tl)
intact = 1 / np.abs(hp * lp)
bare = 1 / np.abs(lp)
ref = intact.min()
bx.plot(f, 20 * np.log10(intact / ref), color=P.edge("rna"), lw=2, label="intact corpuscle")
bx.plot(f, 20 * np.log10(bare / ref), color=P.edge("dna"), lw=2, ls="--", label="capsule removed")
fb = f[np.argmin(intact)]
bx.axvline(fb, color=P.muted(), lw=0.7, ls=":")
bx.text(fb * 1.08, 34, f"best frequency\n~{fb:.0f} Hz", fontsize=8, color=P.muted())
bx.set_xscale("log")
bx.set_ylim(-5, 45)
bx.set_xlabel("Vibration frequency / Hz")
bx.set_ylabel("Threshold amplitude / dB (re minimum)")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Pacinian tuning curve (schematic)", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
