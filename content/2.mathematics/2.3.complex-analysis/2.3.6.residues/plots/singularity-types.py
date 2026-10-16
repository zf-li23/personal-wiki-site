"""Domain coloring near a pole and near an essential singularity.
Hue encodes arg f(z); the brightness bands are level sets of log2 |f(z)|."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb


def domain_coloring(w):
    hue = (np.angle(w) / (2 * np.pi)) % 1.0
    logmod = np.log2(np.abs(w) + 1e-300)
    bands = logmod - np.floor(logmod)
    value = 0.62 + 0.38 * bands
    hsv = np.stack([hue, 0.85 * np.ones_like(hue), value], axis=-1)
    return hsv_to_rgb(hsv)


cases = [
    (lambda z: 1 / z**2, 1.0, r"pole of order 2: $f(z) = 1/z^2$"),
    (lambda z: np.exp(1 / z), 0.6, r"essential singularity: $f(z) = e^{1/z}$"),
]
fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
for ax, (f, L, title) in zip(axes, cases):
    x = np.linspace(-L, L, 900)
    X, Y = np.meshgrid(x, x)
    Z = X + 1j * Y
    Z[np.abs(Z) < 1e-9] = 1e-9
    with np.errstate(all="ignore"):
        w = f(Z)
    w = np.where(np.isfinite(w), w, 1e300)
    ax.imshow(domain_coloring(w), extent=[-L, L, -L, L], origin="lower")
    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    ax.set_title(title)
    ax.set_xlabel("Re z")
    ax.set_ylabel("Im z")

# Solutions of e^{1/z} = 1 + i accumulate at 0 (Picard's theorem).
target = 1 + 1j
k = np.arange(-12, 13)
sols = 1 / (np.log(target) + 2j * np.pi * k)
axes[1].plot(sols.real, sols.imag, "o", ms=4, color="white", mec="black", mew=0.6,
             label=r"solutions of $e^{1/z} = 1 + i$")
axes[1].set_xlim(-0.6, 0.6)
axes[1].set_ylim(-0.6, 0.6)
axes[1].legend(loc="lower right", fontsize=9)
fig.tight_layout()
