"""EDF of a normal sample with pointwise Clopper-Pearson intervals and the DKW confidence band."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(3)
n, alpha = 50, 0.05
x = np.sort(rng.standard_normal(n))
k = np.arange(1, n + 1)                    # n F_n(x_(i)) = i without ties
fn = k / n
lo_cp = np.where(k > 0, stats.beta.ppf(alpha / 2, k, n - k + 1), 0.0)
hi_cp = np.where(k < n, stats.beta.ppf(1 - alpha / 2, k + 1, n - k), 1.0)
eps = np.sqrt(np.log(2 / alpha) / (2 * n))
lo_dkw, hi_dkw = np.maximum(fn - eps, 0), np.minimum(fn + eps, 1)

fig, ax = plt.subplots(figsize=(7.5, 4.4))
xs = np.r_[x, x[-1] + 0.6]
ax.fill_between(xs, np.r_[lo_dkw, lo_dkw[-1]], np.r_[hi_dkw, hi_dkw[-1]], step="post",
                color="C0", alpha=0.18, label=f"95% DKW band, F_n +/- {eps:.3f}")
ax.fill_between(xs, np.r_[lo_cp, lo_cp[-1]], np.r_[hi_cp, hi_cp[-1]], step="post",
                color="C0", alpha=0.35, label="95% pointwise Clopper-Pearson intervals")
ax.step(np.r_[x[0] - 0.6, x, x[-1] + 0.6], np.r_[0, fn, 1], where="post", color="C0", lw=1.5,
        label="EDF F_n")
xx = np.linspace(x[0] - 0.6, x[-1] + 0.6, 300)
ax.plot(xx, stats.norm.cdf(xx), color="C3", lw=1.5, label="true CDF N(0, 1)")
ax.set_xlabel("x")
ax.set_ylabel("probability")
ax.set_title("Pointwise confidence intervals and a simultaneous confidence band, n = 50",
             fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
