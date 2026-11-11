"""The cochlea as a bank of gammatone filters.

g(t) = t^(n-1) exp(-2 pi b t) cos(2 pi f_c t), n = 4, b = 1.019 ERB(f_c),
ERB(f) = 24.7 (4.37 f / kHz + 1) Hz (Glasberg and Moore 1990).
A: impulse responses at f_c = 250, 1000 and 4000 Hz (normalized).
B: gains of 16 filters spaced evenly on the ERB-number scale between 100 Hz and 8 kHz.
C: output of 48 channels (half-wave rectified, normalized per channel) to a harmonic complex with
fundamental 200 Hz (harmonics 1-40, equal amplitude, cosine phase): low channels resolve single
harmonics and follow their waveform; high channels pass several harmonics and fire once per 5 ms period.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fs = 32000.0


def erb(f):
    return 24.7 * (4.37 * f / 1000 + 1)


def erb_number(f):
    return 21.4 * np.log10(4.37 * f / 1000 + 1)


def erb_inverse(e):
    return (10 ** (e / 21.4) - 1) * 1000 / 4.37


def gammatone(fc, dur=0.05):
    t = np.arange(int(dur * fs)) / fs
    b = 1.019 * erb(fc)
    g = t**3 * np.exp(-2 * np.pi * b * t) * np.cos(2 * np.pi * fc * t)
    return t, g / np.abs(g).max()


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1), gridspec_kw={"width_ratios": [1, 1, 1.25]})
ax = axs[0]
cols = [P.edge("dna"), P.edge("enzyme"), P.edge("rna")]
for k, (fc, c) in enumerate(zip((250, 1000, 4000), cols)):
    t, g = gammatone(fc, 0.025)
    ax.plot(t * 1e3, g - 2.4 * k, color=c, lw=1.0)
    ax.text(25.5, -2.4 * k, f"{fc} Hz", fontsize=8, color=c, va="center")
ax.set_xlim(0, 30)
ax.set_yticks([])
ax.set_xlabel("Time / ms")
ax.set_title("A  Impulse responses", loc="left", fontsize=10)
for s in ("left", "top", "right"):
    ax.spines[s].set_visible(False)

ax = axs[1]
fcs = erb_inverse(np.linspace(erb_number(100), erb_number(8000), 16))
f = np.logspace(np.log10(50), np.log10(12000), 800)
for fc in fcs:
    b = 1.019 * erb(fc)
    # magnitude of the 4th-order gammatone near its centre frequency
    gain = (1 + ((f - fc) / b) ** 2) ** (-2)
    ax.plot(f, 10 * np.log10(gain), color=P.edge("dna"), lw=1.0)
ax.set_xscale("log")
ax.set_ylim(-50, 3)
ax.set_xlabel("Frequency / Hz")
ax.set_ylabel("Gain / dB")
ax.set_title("B  A filter bank on the ERB scale", loc="left", fontsize=10)

ax = axs[2]
dur = 0.04
t = np.arange(int(dur * fs)) / fs
x = sum(np.cos(2 * np.pi * 200 * h * t) for h in range(1, 41))
fcs = erb_inverse(np.linspace(erb_number(150), erb_number(6000), 48))
img = []
for fc in fcs:
    _, g = gammatone(fc, 0.03)
    y = np.convolve(x, g)[: len(t)]
    y = np.clip(y, 0, None)
    seg = y[int(0.02 * fs):]
    img.append(seg / seg.max())
img = np.array(img)
ax.imshow(img, aspect="auto", origin="lower", cmap="Blues" if not P.is_dark() else "Blues_r",
          extent=[0, 20, 0, len(fcs)], interpolation="nearest")
ticks = [0, 12, 24, 36, 47]
ax.set_yticks([i + 0.5 for i in ticks])
ax.set_yticklabels([f"{fcs[i]:.0f}" for i in ticks])
ax.set_xlabel("Time / ms")
ax.set_ylabel("Channel centre frequency / Hz")
ax.set_title("C  Response to a 200 Hz harmonic complex", loc="left", fontsize=10)
fig.tight_layout()
