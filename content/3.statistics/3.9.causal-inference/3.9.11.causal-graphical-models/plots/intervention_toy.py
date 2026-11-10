"""Three causal models with the same observational distribution but different effects of do(X = 3)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 4000


def model_1(n, x_do=None):
    """X -> Y: X = U_X, Y = X + U_Y."""
    x = rng.normal(0, 1, n) if x_do is None else np.full(n, x_do)
    y = x + rng.normal(0, 1, n)
    return x, y


def model_2(n, x_do=None):
    """Y -> X: Y = U_Y with variance 2, X = Y / 2 + U_X with variance 1/2."""
    y = rng.normal(0, np.sqrt(2), n)
    x = y / 2 + rng.normal(0, np.sqrt(0.5), n) if x_do is None else np.full(n, x_do)
    return x, y


def model_3(n, x_do=None):
    """X <- Z -> Y: X = 0.8 Z + U_X, Y = 1.25 Z + U_Y."""
    z = rng.normal(0, 1, n)
    x = 0.8 * z + rng.normal(0, 0.6, n) if x_do is None else np.full(n, x_do)
    y = 1.25 * z + rng.normal(0, np.sqrt(0.4375), n)
    return x, y


models = [("Model 1: $X \\to Y$", model_1), ("Model 2: $Y \\to X$", model_2),
          ("Model 3: $X \\leftarrow Z \\to Y$", model_3)]
fig, axes = plt.subplots(2, 3, figsize=(11, 6.2), sharex="row", sharey="row")
grid = np.linspace(-5, 7, 300)
for j, (title, model) in enumerate(models):
    x, y = model(n)
    ax = axes[0, j]
    ax.scatter(x, y, s=3, alpha=0.25, color="C0")
    ax.axvline(3, color="C3", lw=1, ls="--")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("$x$")
    if j == 0:
        ax.set_ylabel("$y$ (observational sample)")

    ax = axes[1, j]
    _, y_do = model(n, x_do=3.0)
    ax.hist(y_do, bins=50, density=True, color="C1", alpha=0.6, label="$Y$ under do($X$ = 3)")
    ax.plot(grid, stats.norm.pdf(grid, 3, 1), color="C0", lw=1.6, label="$Y$ given $X$ = 3")
    ax.set_xlabel("$y$")
    if j == 0:
        ax.set_ylabel("density")
        ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
