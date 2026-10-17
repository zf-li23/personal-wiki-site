"""X ~ N(0,1), Y = S X with an independent random sign S: normal marginals, zero correlation, not jointly normal."""

import numpy as np
import matplotlib.pyplot as plt

n = 3000
x = np.random.standard_normal(n)
s = np.random.choice([-1, 1], size=n)
y = s * x
z1 = np.random.standard_normal(n)
z2 = np.random.standard_normal(n)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
axes[0].scatter(z1, z2, s=3, alpha=0.4, color="C0")
axes[0].set_title("independent N(0,1) pair (jointly normal)")
axes[1].scatter(x, y, s=3, alpha=0.4, color="C1")
axes[1].set_title(f"(X, SX): corr = {np.corrcoef(x, y)[0, 1]:.2f}, not jointly normal")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("first coordinate")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("second coordinate")
fig.tight_layout()
