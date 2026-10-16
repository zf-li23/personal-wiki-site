"""Fourier coefficients of a periodized function approach its Fourier transform as the period grows."""

import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(0, 6, 600)
fhat = 2 / (1 + xi**2)

fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
for ax, l in zip(axes, [2.0, 4.0, 16.0]):
    n = np.arange(0, int(6 * l / np.pi) + 1)
    xn = n * np.pi / l
    # 2l c_n for exp(-|x|) restricted to [-l, l]
    cn = 2 * (1 - (-1.0) ** n * np.exp(-l)) / (1 + xn**2)
    ax.plot(xi, fhat, color="0.5", lw=1.4, label="F(xi) = 2 / (1 + xi^2)")
    ax.vlines(xn, 0, cn, color="C0", lw=1.2)
    ax.plot(xn, cn, "o", color="C0", ms=3, label="2l c_n at xi_n = n pi / l")
    ax.set_title(f"half-period l = {l:g},  spacing pi / l = {np.pi / l:.2f}")
    ax.set_xlabel("xi")
    ax.set_xlim(0, 6)
axes[0].set_ylim(0, 2.2)
axes[0].legend(fontsize=8, loc="upper right")
fig.suptitle("f(x) = exp(-|x|) on [-l, l]: discrete spectrum of the Fourier series fills in the Fourier transform")
fig.tight_layout()
