"""Fourier partial sums of the square wave sgn(x) on (-pi, pi): convergence to
the midpoint 0 at the jumps, and the Gibbs overshoot of about 9% of the jump."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 4000)
square = np.sign(np.sin(x))


def partial(x, N):
    k = np.arange(1, N + 1, 2)
    return 4 / np.pi * np.sum(np.sin(np.outer(k, x)) / k[:, None], axis=0)


fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
ax = axes[0]
ax.plot(x, square, color="black", linewidth=1.8, label="square wave")
for k, N in enumerate([1, 3, 9, 29]):
    ax.plot(x, partial(x, N), color=f"C{k}", linewidth=1.1, label=rf"$S_{{{N}}}(x)$")
ax.plot([-np.pi, 0, np.pi], [0, 0, 0], "o", color="black", markersize=4)
ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_xticklabels([r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])
ax.set_title(r"$\frac{4}{\pi}\sum_{k \leq N,\ k\ \mathrm{odd}} \frac{\sin kx}{k}$; the sum is $0$ at the jumps",
             fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(True, alpha=0.3)

ax = axes[1]
xz = np.linspace(0, 0.8, 2000)
for k, N in enumerate([9, 29, 99, 299]):
    ax.plot(xz, partial(xz, N), color=f"C{k}", linewidth=1.1, label=rf"$S_{{{N}}}$")
gibbs = 2 / np.pi * 1.851937052
ax.axhline(1, color="black", linewidth=1.2)
ax.axhline(gibbs, color="gray", linewidth=0.9, linestyle="--")
ax.text(0.45, gibbs + 0.01, r"$\frac{2}{\pi}\int_0^\pi \frac{\sin t}{t}\,\mathrm{d}t \approx 1.179$", fontsize=10)
ax.set_ylim(0.6, 1.3)
ax.set_xlabel(r"$x$")
ax.set_title("Gibbs phenomenon: the overshoot moves to the jump but does not shrink", fontsize=10)
ax.legend(fontsize=8, loc="lower right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
