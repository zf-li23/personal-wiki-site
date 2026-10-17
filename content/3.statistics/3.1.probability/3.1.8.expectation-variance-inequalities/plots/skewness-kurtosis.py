"""Standardized densities illustrating skewness (left) and kurtosis (right)."""

import numpy as np
import matplotlib.pyplot as plt
from math import gamma

x = np.linspace(-4, 5, 900)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

ax = axes[0]
phi = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
ax.plot(x, phi, color="C0", lw=1.8, label="N(0,1): skewness 0")
# standardized Exp(1): X - 1 has mean 0, variance 1
f_exp = np.where(x > -1, np.exp(-(x + 1)), 0.0)
ax.plot(x, f_exp, color="C1", lw=1.8, label="Exp(1) standardized: skewness 2")
# standardized Gamma(4, 1): (X - 4) / 2
k = 4.0
y = 2 * x + k
f_g = np.where(y > 0, 2 * y ** (k - 1) * np.exp(-y) / gamma(k), 0.0)
ax.plot(x, f_g, color="C2", lw=1.8, label="Gamma(4,1) standardized: skewness 1")
ax.set_xlim(-3.5, 5)
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("skewness")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
xs = np.linspace(-5, 5, 900)
ax.plot(xs, np.exp(-xs**2 / 2) / np.sqrt(2 * np.pi), color="C0", lw=1.8, label="N(0,1): kurtosis 0")
a = np.sqrt(3)
ax.plot(xs, np.where(np.abs(xs) <= a, 1 / (2 * a), 0.0), color="C3", lw=1.8, label="uniform: kurtosis -1.2")
b = 1 / np.sqrt(2)
ax.plot(xs, np.exp(-np.abs(xs) / b) / (2 * b), color="C4", lw=1.8, label="Laplace: kurtosis 3")
nu = 5
c = np.sqrt((nu - 2) / nu)
t = xs / c
ft = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2)) * (1 + t**2 / nu) ** (-(nu + 1) / 2) / c
ax.plot(xs, ft, color="C5", lw=1.4, ls="--", label="t_5 standardized: kurtosis 6")
ax.set_xlabel("x")
ax.set_title("kurtosis (all with mean 0, variance 1)")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
