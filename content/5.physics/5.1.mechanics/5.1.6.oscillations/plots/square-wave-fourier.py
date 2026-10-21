"""Fourier synthesis and amplitude spectrum of a square wave."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.25, 1.25, 3000)  # in units of the period T
w = 2 * np.pi
square = np.sign(np.cos(w * t))


def partial_sum(n_terms):
    s = np.zeros_like(t)
    for j in range(n_terms):
        k = 2 * j + 1
        s += 4 / np.pi * (-1) ** j * np.cos(k * w * t) / k
    return s


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [2, 1]})
ax1.plot(t, square, color="k", lw=1.2, label="square wave")
for n_terms, c in [(1, "C0"), (2, "C1"), (3, "C2"), (20, "C3")]:
    k_max = 2 * n_terms - 1
    ax1.plot(t, partial_sum(n_terms), color=c, lw=1.3, label=f"harmonics up to k = {k_max}")
ax1.set_xlabel("t / T")
ax1.set_ylabel("x")
ax1.set_ylim(-1.5, 1.7)
ax1.legend(fontsize=8, loc="upper right", ncol=2)
ax1.set_title("Partial sums of the Fourier series")

k = np.arange(1, 12)
Ak = np.where(k % 2 == 1, 4 / (np.pi * k), 0.0)
ax2.vlines(k, 0, Ak, color="C0", lw=3)
ax2.plot(k, Ak, "o", color="C0")
ax2.set_xticks(k)
ax2.set_xlabel("k (frequency / fundamental)")
ax2.set_ylabel("A_k")
ax2.set_ylim(0, 1.4)
ax2.set_title("Amplitude spectrum")
fig.tight_layout()
