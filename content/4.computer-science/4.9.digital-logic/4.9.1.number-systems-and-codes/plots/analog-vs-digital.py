"""An analog waveform, its sampled-and-quantized version, and a binary
signal with noise: the receiver only has to decide which side of the
thresholds the voltage lies on."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
t = np.linspace(0, 2, 1000)
analog = 1.6 * np.sin(2 * np.pi * t) + 0.6 * np.sin(6 * np.pi * t + 0.5)

ts = np.linspace(0, 2, 25)
xs = 1.6 * np.sin(2 * np.pi * ts) + 0.6 * np.sin(6 * np.pi * ts + 0.5)
xq = np.round(xs * 2) / 2

bits = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1])
tb = np.linspace(0, len(bits), 1200, endpoint=False)
ideal = 3.3 * bits[tb.astype(int)]
noisy = ideal + rng.normal(0, 0.25, tb.size)

fig, axes = plt.subplots(3, 1, figsize=(8, 6.4))
ax = axes[0]
ax.plot(t, analog, color="C0", lw=1.6)
ax.set_title("(a) analog: continuous in time and in value")
ax.set_ylabel("voltage")
ax = axes[1]
ax.plot(t, analog, color="C0", lw=0.8, alpha=0.4)
ax.step(ts, xq, where="post", color="C1", lw=1.4)
ax.plot(ts, xq, "o", color="C1", ms=3)
ax.set_title("(b) sampled and quantized: discrete in time and in value")
ax.set_ylabel("level")
ax = axes[2]
ax.plot(tb, noisy, color="C2", lw=0.8)
ax.plot(tb, ideal, color="C3", lw=1.2, ls="--")
ax.axhspan(2.0, 3.8, color="C2", alpha=0.08)
ax.axhspan(-0.5, 0.8, color="C2", alpha=0.08)
ax.axhline(2.0, color="gray", lw=0.8, ls=":")
ax.axhline(0.8, color="gray", lw=0.8, ls=":")
ax.text(len(bits) + 0.1, 2.9, "logic 1", va="center", fontsize=9)
ax.text(len(bits) + 0.1, 0.1, "logic 0", va="center", fontsize=9)
ax.text(len(bits) + 0.1, 1.4, "forbidden", va="center", fontsize=9, color="gray")
ax.set_xlim(0, len(bits) + 1.6)
ax.set_title("(c) binary signal with noise: only the region matters")
ax.set_xlabel("time")
ax.set_ylabel("voltage (V)")
fig.tight_layout()
