"""Coronary deaths of British male doctors by age and smoking: age-specific death rates and rate ratios."""

import numpy as np
import matplotlib.pyplot as plt

ages = ["35-44", "45-54", "55-64", "65-74", "75-84"]
sd = np.array([32, 104, 206, 186, 102.])
sp = np.array([52407, 43248, 28612, 12663, 5317.])
nd = np.array([2, 12, 28, 28, 31.])
npy = np.array([18790, 10673, 5710, 2585, 1462.])
rs, rn = sd / sp * 1e5, nd / npy * 1e5
rr = (sd / sp) / (nd / npy)
se = np.sqrt(1 / sd + 1 / nd)            # se of log rate ratio (Poisson counts)
x = np.arange(len(ages))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, rs, "o-", color="C3", lw=2, label="smokers")
axes[0].plot(x, rn, "s-", color="C0", lw=2, label="non-smokers")
axes[0].set_yscale("log")
axes[0].set_ylabel("deaths per 100,000 person-years")
axes[0].set_title("Age-specific coronary death rates")
axes[0].legend(frameon=False)

axes[1].errorbar(x, rr, yerr=[rr - rr * np.exp(-1.96 * se), rr * np.exp(1.96 * se) - rr],
                 fmt="o", color="C2", capsize=4, lw=2)
axes[1].axhline(1, color="gray", ls=":")
axes[1].set_yscale("log")
axes[1].set_yticks([0.5, 1, 2, 5, 10, 20])
axes[1].set_yticklabels(["0.5", "1", "2", "5", "10", "20"])
axes[1].set_ylabel("rate ratio, smokers / non-smokers")
axes[1].set_title("Rate ratios with 95% intervals")
for ax in axes:
    ax.set_xticks(x)
    ax.set_xticklabels(ages)
    ax.set_xlabel("age group (years)")
    ax.grid(alpha=0.3)
fig.tight_layout()
