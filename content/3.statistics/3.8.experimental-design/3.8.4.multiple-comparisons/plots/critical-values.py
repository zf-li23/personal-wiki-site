"""Critical values on the |t| scale for all pairwise comparisons: LSD, Tukey, Bonferroni and Scheffe."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

nu, alpha = 16, 0.05
a = np.arange(2, 13)
m = a * (a - 1) / 2
crit = {
    "LSD": np.full(a.shape, stats.t.ppf(1 - alpha / 2, nu)),
    "Tukey": np.array([stats.studentized_range.ppf(1 - alpha, k, nu) for k in a]) / np.sqrt(2),
    "Bonferroni": stats.t.ppf(1 - alpha / (2 * m), nu),
    "Scheffe": np.sqrt((a - 1) * stats.f.ppf(1 - alpha, a - 1, nu)),
}
fig, ax = plt.subplots(figsize=(8, 4.4))
for i, (name, c) in enumerate(crit.items()):
    ax.plot(a, c, "o-", color=f"C{i}", lw=2, label=f"{name} ({c[2]:.3f} at a = 4)")
ax.axvline(4, color="gray", ls=":")
ax.set_xlabel("number of levels a")
ax.set_ylabel("critical value for |t0|")
ax.set_title("Pairwise comparisons, alpha = 0.05, 16 error degrees of freedom")
ax.legend(frameon=False)
ax.grid(alpha=0.3)
fig.tight_layout()
