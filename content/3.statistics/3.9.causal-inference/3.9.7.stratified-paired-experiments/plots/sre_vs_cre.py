"""Randomization distributions of the estimated average effect under CRE, SRE and PRE."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, reps = 80, 5000
x = np.sort(rng.normal(size=n))                  # covariate used for blocking
y0 = 2.0 * x + rng.normal(size=n)
y1 = y0 + 1.0 + 0.5 * rng.normal(size=n)         # heterogeneous effects
tau_fs = np.mean(y1 - y0)


def estimate(w):
    return y1[w].mean() - y0[~w].mean()


def cre():
    w = np.zeros(n, dtype=bool)
    w[rng.permutation(n)[: n // 2]] = True
    return w


def sre(n_strata=4):
    w = np.zeros(n, dtype=bool)
    size = n // n_strata                         # strata are consecutive blocks of sorted x
    for j in range(n_strata):
        idx = j * size + rng.permutation(size)[: size // 2]
        w[idx] = True
    return w


def pre():
    w = np.zeros(n, dtype=bool)
    first = rng.random(n // 2) < 0.5             # pairs are (0, 1), (2, 3), ...
    w[np.arange(0, n, 2)[first]] = True
    w[np.arange(1, n, 2)[~first]] = True
    return w


designs = {"CRE": cre, "SRE, 4 strata": sre, "PRE, 40 pairs": pre}
colors = ["C0", "C1", "C2"]
est = {k: np.array([estimate(f()) for _ in range(reps)]) for k, f in designs.items()}

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
grid = np.linspace(tau_fs - 1.6, tau_fs + 1.6, 300)
ax = axes[0]
for (k, e), c in zip(est.items(), colors):
    ax.plot(grid, stats.gaussian_kde(e)(grid), color=c, lw=2, label=f"{k} (sd {e.std():.3f})")
ax.axvline(tau_fs, color="gray", ls=":", lw=1)
ax.set_xlabel("estimated average effect")
ax.set_ylabel("randomization density")
ax.set_title("Same population, three designs")
ax.legend(fontsize=8, frameon=False)

ax = axes[1]
ax.scatter(x, y0, s=12, color="C0", label="Y(0)")
ax.scatter(x, y1, s=12, color="C3", label="Y(1)")
for b in np.quantile(x, [0.25, 0.5, 0.75]):
    ax.axvline(b, color="gray", lw=0.8, ls="--")
ax.set_xlabel("covariate x (dashed lines: stratum boundaries)")
ax.set_ylabel("potential outcome")
ax.set_title("Potential outcomes of the 80 units")
ax.legend(fontsize=8, frameon=False)
fig.tight_layout()
