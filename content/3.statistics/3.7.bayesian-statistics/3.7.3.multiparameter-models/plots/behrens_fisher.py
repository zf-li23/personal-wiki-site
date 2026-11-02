"""Behrens-Fisher problem: posterior of delta = mu1 - mu2 by simulation (illustrative summary data)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# illustrative summary statistics of two independent normal samples
n1, m1, s1 = 10, 5.2, 1.0
n2, m2, s2 = 15, 4.4, 2.5

# non-informative priors p(mu_j, sigma_j^2) proportional to 1/sigma_j^2:
# mu_j | y_j ~ t_{n_j - 1}(ybar_j, s_j^2 / n_j), independently
post1 = stats.t(n1 - 1, loc=m1, scale=s1 / np.sqrt(n1))
post2 = stats.t(n2 - 1, loc=m2, scale=s2 / np.sqrt(n2))
rng = np.random.default_rng(0)
S = 100000
delta = post1.rvs(S, random_state=rng) - post2.rvs(S, random_state=rng)
lo, hi = np.quantile(delta, [0.025, 0.975])

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))
x = np.linspace(2.0, 7.0, 600)
axes[0].plot(x, post1.pdf(x), color="C0", lw=1.8, label=r"$\mu_1 \mid y$")
axes[0].plot(x, post2.pdf(x), color="C3", lw=1.8, label=r"$\mu_2 \mid y$")
axes[0].set_xlabel(r"$\mu$")
axes[0].set_ylabel("posterior density")
axes[0].set_title("marginal posteriors of the two means", fontsize=11)

axes[1].hist(delta, bins=120, density=True, color="C2", alpha=0.6, label="draws of " + r"$\delta$")
axes[1].axvline(0, color="0.3", lw=1.0)
axes[1].axvline(lo, color="C2", ls="--", lw=1.2, label="95% central interval")
axes[1].axvline(hi, color="C2", ls="--", lw=1.2)
axes[1].set_xlim(-2.5, 4.0)
axes[1].set_xlabel(r"$\delta = \mu_1 - \mu_2$")
axes[1].set_title(rf"posterior of $\delta$, $P(\delta > 0 \mid y)$ = {np.mean(delta > 0):.2f}", fontsize=11)
for ax in axes:
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
fig.tight_layout()
