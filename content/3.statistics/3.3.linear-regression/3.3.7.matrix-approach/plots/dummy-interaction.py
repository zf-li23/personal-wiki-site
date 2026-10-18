"""One model with a dummy variable and an interaction gives two regression lines."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 40
age = rng.uniform(24, 144, 2 * n)
boy = np.repeat([0.0, 1.0], n)
height = 78 + 0.52 * age + 1.5 * boy + 0.04 * age * boy + 3.5 * rng.normal(size=2 * n)
X = np.column_stack([np.ones(2 * n), age, boy, age * boy])
b = np.linalg.lstsq(X, height, rcond=None)[0]
grid = np.linspace(20, 150, 2)
fig, ax = plt.subplots(figsize=(7, 4.6))
for g, c, m, name in [(0, "C3", "o", "girls (X_2 = 0)"), (1, "C0", "s", "boys (X_2 = 1)")]:
    sel = boy == g
    ax.plot(age[sel], height[sel], m, color=c, ms=4, alpha=0.8, label=name)
    ax.plot(grid, (b[0] + b[2] * g) + (b[1] + b[3] * g) * grid, color=c, lw=1.8)
ax.set_title(f"fit: girls  {b[0]:.1f} + {b[1]:.3f} X_1;   boys  {b[0] + b[2]:.1f} + {b[1] + b[3]:.3f} X_1", fontsize=10)
ax.set_xlabel("age in months X_1")
ax.set_ylabel("height (cm)")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
