"""Densities of the exponential, normal, beta and gamma distributions."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(11, 7.5))

ax = axes[0, 0]
x = np.linspace(0, 10, 400)
for i, lam in enumerate([1.2, 0.6, 0.3]):
    ax.plot(x, stats.expon.pdf(x, scale=1 / lam), color=f"C{i}", lw=2, label=f"Exp({lam})")
ax.set_title("Exponential: f(x) = lambda exp(-lambda x)")
ax.legend(fontsize=8)

ax = axes[0, 1]
x = np.linspace(-5, 5, 500)
for i, (mu, var) in enumerate([(0, 0.2), (0, 1.0), (0, 5.0), (-2, 0.5)]):
    ax.plot(x, stats.norm.pdf(x, mu, np.sqrt(var)), color=f"C{i}", lw=2, label=f"N({mu}, {var})")
ax.set_title("Normal N(mu, sigma^2)")
ax.legend(fontsize=8)

ax = axes[1, 0]
x = np.linspace(0.001, 0.999, 500)
for i, (a, b) in enumerate([(0.5, 0.5), (5, 1), (1, 3), (2, 2), (2, 5), (1, 1)]):
    ax.plot(x, stats.beta.pdf(x, a, b), color=f"C{i}", lw=2, label=f"Beta({a}, {b})")
ax.set_ylim(0, 2.6)
ax.set_title("Beta(alpha, beta)")
ax.legend(fontsize=8)

ax = axes[1, 1]
x = np.linspace(0.001, 12, 500)
for i, a in enumerate([0.5, 1, 2, 3, 5]):
    ax.plot(x, stats.gamma.pdf(x, a, scale=1.0), color=f"C{i}", lw=2, label=f"Gamma({a}, 1)")
ax.set_ylim(0, 1.0)
ax.set_title("Gamma(alpha, lambda), rate lambda = 1")
ax.legend(fontsize=8)
for ax in axes.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
fig.tight_layout()
