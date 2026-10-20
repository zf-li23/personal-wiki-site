"""Common activation functions (left) and their derivatives (right):
sigmoid, tanh, ReLU, leaky ReLU, ELU, GELU and SiLU (Swish)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf, expit

z = np.linspace(-4, 4, 801)
Phi = 0.5 * (1 + erf(z / np.sqrt(2)))
phi = np.exp(-z ** 2 / 2) / np.sqrt(2 * np.pi)
s = expit(z)
funcs = {
    "sigmoid": (s, s * (1 - s)),
    "tanh": (np.tanh(z), 1 - np.tanh(z) ** 2),
    "ReLU": (np.maximum(z, 0), (z > 0).astype(float)),
    "leaky ReLU (0.1)": (np.where(z > 0, z, 0.1 * z), np.where(z > 0, 1.0, 0.1)),
    "ELU": (np.where(z > 0, z, np.expm1(z)), np.where(z > 0, 1.0, np.exp(z))),
    "GELU": (z * Phi, Phi + z * phi),
    "SiLU / Swish": (z * s, s + z * s * (1 - s)),
}
styles = ["-", "-", "-", "--", "-.", "-", ":"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
for (name, (f, df)), ls in zip(funcs.items(), styles):
    ax1.plot(z, f, ls=ls, lw=1.7, label=name)
    ax2.plot(z, df, ls=ls, lw=1.7, label=name)
ax1.set_ylim(-1.5, 4)
ax1.set_title("activation function", fontsize=10)
ax2.set_ylim(-0.2, 1.3)
ax2.set_title("derivative", fontsize=10)
for ax in (ax1, ax2):
    ax.axhline(0, color="C7", lw=0.6)
    ax.axvline(0, color="C7", lw=0.6)
    ax.set_xlabel("z")
    ax.grid(alpha=0.3)
ax1.legend(fontsize=8, loc="upper left")
fig.tight_layout()
