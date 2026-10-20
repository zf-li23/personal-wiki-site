"""Envelope rejection sampling of the half-normal density with Exp(1) proposals
(c = sqrt(2e/pi)): accepted and rejected proposals under the envelope c g, and the
resulting standard normal sample after attaching a random sign."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
lam = 1.0
c = np.sqrt(2 / np.pi) / lam * np.exp(lam ** 2 / 2)

n = 4000
x = rng.exponential(1 / lam, n)
u = rng.uniform(0, 1, n)
heights = c * lam * np.exp(-lam * x) * u
accept = u <= np.exp(-0.5 * (x - lam) ** 2)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ax = axes[0]
grid = np.linspace(0, 4.5, 400)
f = np.sqrt(2 / np.pi) * np.exp(-grid ** 2 / 2)
ax.plot(grid, c * lam * np.exp(-lam * grid), color="C1", lw=2, label=f"envelope c g(x), c = {c:.3f}")
ax.plot(grid, f, color="C0", lw=2, label="half-normal f(x)")
m = 1200
ax.plot(x[:m][accept[:m]], heights[:m][accept[:m]], ".", ms=2.5, color="C0", alpha=0.7, label="accepted")
ax.plot(x[:m][~accept[:m]], heights[:m][~accept[:m]], ".", ms=2.5, color="C3", alpha=0.7, label="rejected")
ax.set_xlim(0, 4.5)
ax.set_ylim(0, 1.4)
ax.set_xlabel("x")
ax.set_title(f"Acceptance rate {accept.mean():.3f} (theory 1/c = {1 / c:.3f})", fontsize=10)
ax.legend(fontsize=8)

ax = axes[1]
signs = rng.choice([-1.0, 1.0], accept.sum())
z = signs * x[accept]
ax.hist(z, bins=40, density=True, color="C0", alpha=0.55, label=f"{z.size} accepted, random sign")
g = np.linspace(-4, 4, 400)
ax.plot(g, stats.norm.pdf(g), color="C3", lw=2, label="N(0, 1) density")
ax.set_xlabel("z")
ax.set_title("Resulting standard normal sample", fontsize=10)
ax.legend(fontsize=8)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
