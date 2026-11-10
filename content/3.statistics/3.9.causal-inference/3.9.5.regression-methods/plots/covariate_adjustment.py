"""Sampling distributions of three estimators of the average effect in a simulated CRE."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, reps = 100, 3000


def one_draw(p, slope_c, slope_t):
    """Draw a super-population sample, run a CRE, return the three estimates."""
    x = rng.normal(size=n)
    y0 = slope_c * x + rng.normal(size=n)
    y1 = 1.0 + slope_t * x + rng.normal(size=n)          # tau_sp = 1
    w = np.zeros(n, dtype=bool)
    w[rng.permutation(n)[: int(round(p * n))]] = True
    y = np.where(w, y1, y0)
    dif = y[w].mean() - y[~w].mean()
    design = np.column_stack([np.ones(n), w, x])
    ols = np.linalg.lstsq(design, y, rcond=None)[0][1]
    design_int = np.column_stack([design, w * (x - x.mean())])
    inter = np.linalg.lstsq(design_int, y, rcond=None)[0][1]
    return dif, ols, inter


names = ["difference in means", "OLS with covariate", "OLS with interaction"]
colors = ["C0", "C1", "C2"]
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Panel 1: common slope, balanced design
est = np.array([one_draw(0.5, 1.0, 1.0) for _ in range(reps)])
grid = np.linspace(-0.2, 2.2, 300)
ax = axes[0]
for k in range(3):
    kde = stats.gaussian_kde(est[:, k])
    ax.plot(grid, kde(grid), color=colors[k], lw=2,
            label=f"{names[k]} (sd {est[:, k].std():.2f})")
ax.axvline(1.0, color="gray", ls=":", lw=1)
ax.set_xlabel("estimate of the average effect")
ax.set_ylabel("density")
ax.set_title("Common slope, p = 0.5")
ax.legend(fontsize=8, frameon=False)

# Panel 2: heterogeneous slopes, varying treated proportion
ps = np.linspace(0.1, 0.9, 9)
sds = np.array([np.array([one_draw(p, -1.0, 3.0) for _ in range(1500)]).std(axis=0) for p in ps])
ax = axes[1]
for k in range(3):
    ax.plot(ps, sds[:, k], "o-", color=colors[k], lw=2, ms=4, label=names[k])
ax.set_xlabel("proportion treated p")
ax.set_ylabel("sampling standard deviation")
ax.set_title("Slopes -1 (control) and 3 (treated)")
ax.legend(fontsize=8, frameon=False)
fig.tight_layout()
