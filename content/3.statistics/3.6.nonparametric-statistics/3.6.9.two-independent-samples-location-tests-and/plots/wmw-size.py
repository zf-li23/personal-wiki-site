"""Rejection rates under equal medians but unequal spreads: WMW, Welch t and Brunner-Munzel tests."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
reps, alpha = 4000, 0.05
ratios = np.array([1, 1.5, 2, 3, 4])
designs = [(10, 30, "n1 = 10 (spread sd) vs n2 = 30 (sd 1)"),
           (30, 10, "n1 = 30 (spread sd) vs n2 = 10 (sd 1)")]

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, (n1, n2, title) in zip(axes, designs):
    rates = {"WMW": [], "Welch t": [], "Brunner-Munzel": []}
    for s in ratios:
        x = rng.normal(0, s, (reps, n1))
        y = rng.normal(0, 1, (reps, n2))
        rates["WMW"].append(np.mean(stats.mannwhitneyu(x, y, axis=1).pvalue < alpha))
        rates["Welch t"].append(np.mean(stats.ttest_ind(x, y, axis=1, equal_var=False).pvalue < alpha))
        rates["Brunner-Munzel"].append(np.mean(stats.brunnermunzel(x, y, axis=1).pvalue < alpha))
    for i, (name, r) in enumerate(rates.items()):
        ax.plot(ratios, r, "o-", color=f"C{i}", lw=2, label=name)
    ax.axhline(alpha, color="gray", ls=":")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("sd of sample 1 (sample 2 has sd 1; both medians 0)")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("rejection rate at alpha = 0.05")
axes[0].legend(frameon=False)
fig.suptitle(f"Type I error for H0: P(X > Y) = 1/2, normal data, {reps} replications")
fig.tight_layout()
