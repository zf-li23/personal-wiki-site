"""Common activation functions and their derivatives."""

import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 1001)
sig = 1 / (1 + np.exp(-z))
funcs = [
    ("sign", np.where(z >= 0, 1.0, -1.0), np.zeros_like(z)),
    ("sigmoid", sig, sig * (1 - sig)),
    ("tanh", np.tanh(z), 1 - np.tanh(z) ** 2),
    ("ReLU", np.maximum(0, z), (z > 0).astype(float)),
]

fig, axes = plt.subplots(1, 4, figsize=(13, 3.4), sharex=True)
for ax, (name, f, df) in zip(axes, funcs):
    if name == "sign":
        ax.plot(z[z < 0], f[z < 0], color="C0", label="g(z)")
        ax.plot(z[z >= 0], f[z >= 0], color="C0")
    else:
        ax.plot(z, f, color="C0", label="g(z)")
    ax.plot(z, df, color="C1", linestyle="--", label="g'(z)")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.set_title(name)
    ax.set_xlabel("z")
    ax.set_ylim(-1.3, 1.6 if name != "ReLU" else 5.2)
    ax.grid(alpha=0.3)
axes[0].legend(loc="upper left", fontsize=8)
fig.tight_layout()
