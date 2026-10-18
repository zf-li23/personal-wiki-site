"""Multipliers of individual, Bonferroni and T^2 intervals as functions of the dimension p (n = 200)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n, alpha = 200, 0.05
ps = np.arange(1, 101)
c_t = np.full(ps.shape, stats.t.ppf(1 - alpha / 2, n - 1))
c_bonf = stats.t.ppf(1 - alpha / (2 * ps), n - 1)
c_T2 = np.sqrt(ps * (n - 1) / (n - ps) * stats.f.ppf(1 - alpha, ps, n - ps))

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(ps, c_T2, color="C1", lw=2, label="T^2 intervals")
ax.plot(ps, c_bonf, color="C4", lw=2, ls="-.", label="Bonferroni, m = p")
ax.plot(ps, c_t, color="C0", lw=2, ls="--", label="individual t")
ax.set_xlabel("dimension p")
ax.set_ylabel("multiplier c")
ax.set_title("n = 200, alpha = 0.05")
ax.set_ylim(0, None)
ax.legend(frameon=False, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
