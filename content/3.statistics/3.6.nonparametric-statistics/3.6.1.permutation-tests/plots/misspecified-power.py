"""Regression through the origin when the true model has an intercept:
rejection rates of the t-test for the slope and of the permutation test, two designs."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, alpha, beta0, sigma = 30, 0.05, 1.0, 1.0
nrep, nperm = 4000, 999
betas = np.linspace(-1.0, 1.0, 21)
tcrit = stats.t.ppf(1 - alpha / 2, n - 1)

z = rng.standard_normal(n)
z = (z - z.mean()) / z.std()
designs = {}
for delta in (0.0, 2.0):
    # Shift x so that delta = beta0 * sum(x) / (sigma * sqrt(sum(x^2))) takes the given value
    m = delta / np.sqrt(n - delta ** 2) if delta > 0 else 0.0
    designs[delta] = z + m

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), sharey=True)
for ax, (delta, x) in zip(axes, designs.items()):
    xc = x - x.mean()
    perms = np.array([rng.permutation(xc) for _ in range(nperm)])
    sxx0 = np.sum(x ** 2)
    rate_t, rate_p, tstats = [], [], {}
    for b1 in betas:
        y = beta0 + b1 * x + sigma * rng.standard_normal((nrep, n))
        # t-test of the slope in the model fitted through the origin
        b = y @ x / sxx0
        resid = y - b[:, None] * x
        s_b = np.sqrt((resid ** 2).sum(axis=1) / (n - 1) / sxx0)
        t = b / s_b
        tstats[b1] = t
        rate_t.append(np.mean(np.abs(t) > tcrit))
        # Permutation test based on the correlation (same permutations for every data set)
        yc = y - y.mean(axis=1, keepdims=True)
        s_obs = np.abs(yc @ xc)
        s_perm = np.abs(yc @ perms.T)
        pval = (1 + (s_perm >= s_obs[:, None]).sum(axis=1)) / (nperm + 1)
        rate_p.append(np.mean(pval <= alpha))
    # Size-adjusted t-test: critical value from the simulated null distribution
    cadj = np.quantile(np.abs(tstats[betas[10]]), 1 - alpha)
    rate_adj = [np.mean(np.abs(tstats[b1]) > cadj) for b1 in betas]
    ax.plot(betas, rate_p, "o-", color="C0", lw=2, ms=4, label="permutation test")
    ax.plot(betas, rate_t, "s--", color="C3", lw=2, ms=4, label="t-test, nominal critical value")
    ax.plot(betas, rate_adj, ":", color="C2", lw=2, label="t-test, size-adjusted")
    ax.axhline(alpha, color="gray", lw=1)
    ax.set_title(f"n = {n}, beta0 = 1, delta = {delta:.0f}: t-test size = {rate_t[10]:.3f}",
                 fontsize=10)
    ax.set_xlabel("true slope beta1")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("rejection rate")
axes[0].legend(fontsize=8, loc="upper center")
axes[0].set_ylim(0, 1.02)
fig.tight_layout()
