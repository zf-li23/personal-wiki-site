"""Scatter plots for several correlation coefficients, plus two nonlinear dependences with zero correlation."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 500
fig, axes = plt.subplots(2, 3, figsize=(10, 6.4))
for ax, rho in zip(axes.flat[:4], [-0.8, 0.0, 0.5, 0.95]):
    z = rng.normal(size=(n, 2))
    x = z[:, 0]
    y = rho * z[:, 0] + np.sqrt(1 - rho**2) * z[:, 1]
    ax.scatter(x, y, s=5, alpha=0.5, color="C0")
    ax.set_title(f"rho = {rho}, sample r = {np.corrcoef(x, y)[0, 1]:.2f}")

ax = axes.flat[4]
t = rng.uniform(0, 2 * np.pi, n)
r = np.sqrt(rng.uniform(0, 1, n))
x, y = r * np.cos(t), r * np.sin(t)
ax.scatter(x, y, s=5, alpha=0.5, color="C1")
ax.set_title(f"uniform on disk, r = {np.corrcoef(x, y)[0, 1]:.2f}")

ax = axes.flat[5]
x = rng.normal(size=n)
y = x**2 + 0.2 * rng.normal(size=n)
ax.scatter(x, y, s=5, alpha=0.5, color="C1")
ax.set_title(f"Y = X^2 + noise, r = {np.corrcoef(x, y)[0, 1]:.2f}")

for ax in axes.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
fig.tight_layout()
