"""Characteristic functions of four symmetric distributions (all real and even)."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2001)
curves = [
    ("N(0, 1): exp(-t^2/2)", np.exp(-t**2 / 2)),
    ("U(-1, 1): sin(t)/t", np.sinc(t / np.pi)),
    ("Laplace: 1/(1+t^2)", 1 / (1 + t**2)),
    ("Cauchy: exp(-|t|)", np.exp(-np.abs(t))),
]

fig, ax = plt.subplots(figsize=(8, 4.5))
for label, y in curves:
    ax.plot(t, y, lw=1.8, label=label)
ax.axhline(0, color="0.5", lw=0.8)
ax.set_xlabel("t")
ax.set_ylabel("phi(t)")
ax.set_ylim(-0.3, 1.05)
ax.set_title("Characteristic functions: phi(0) = 1, |phi(t)| <= 1")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
