"""Three Fourier transform pairs, with the convention F(xi) = integral of f(x) exp(-i xi x) dx."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1001)
xi = np.linspace(-12, 12, 1201)
fig, axes = plt.subplots(3, 2, figsize=(10, 8))

# rectangular pulse
ax = axes[0, 0]
ax.plot(x, (np.abs(x) <= 1).astype(float), color="C0", lw=1.8)
ax.set_title("f(x) = 1 for |x| <= 1, 0 otherwise")
ax = axes[0, 1]
ax.plot(xi, 2 * np.sinc(xi / np.pi), color="C0", lw=1.8)
ax.set_title("F(xi) = 2 sin(xi) / xi")

# two-sided exponential
ax = axes[1, 0]
ax.plot(x, np.exp(-np.abs(x)), color="C1", lw=1.8)
ax.set_title("f(x) = exp(-|x|)")
ax = axes[1, 1]
ax.plot(xi, 2 / (1 + xi**2), color="C1", lw=1.8)
ax.set_title("F(xi) = 2 / (1 + xi^2)")

# Gaussians of different widths
for i, s in enumerate([0.4, 1.0, 2.0]):
    axes[2, 0].plot(x, np.exp(-x**2 / (2 * s**2)), color=f"C{i + 2}", lw=1.8, label=f"s = {s}")
    axes[2, 1].plot(xi, s * np.sqrt(2 * np.pi) * np.exp(-(s * xi) ** 2 / 2), color=f"C{i + 2}", lw=1.8, label=f"s = {s}")
axes[2, 0].set_title("f(x) = exp(-x^2 / (2 s^2))")
axes[2, 1].set_title("F(xi) = s sqrt(2 pi) exp(-s^2 xi^2 / 2)")
axes[2, 0].legend(fontsize=8)
axes[2, 1].legend(fontsize=8)

for ax in axes[:, 0]:
    ax.set_xlim(-5, 5)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set_xlabel("x")
for ax in axes[:, 1]:
    ax.set_xlim(-12, 12)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set_xlabel("xi")
fig.tight_layout()
