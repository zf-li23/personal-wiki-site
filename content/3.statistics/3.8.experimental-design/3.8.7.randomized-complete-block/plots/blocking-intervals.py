"""Tukey 95% simultaneous intervals for the graft pressures: RCBD error versus the error of a one-way analysis that ignores the batches."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

psi = [8500, 8700, 8900, 9100]
y = np.array([[90.3, 89.2, 98.2, 93.9, 87.4, 97.9],
              [92.5, 89.5, 90.6, 94.7, 87.0, 95.8],
              [85.5, 90.8, 89.6, 86.2, 88.0, 93.4],
              [82.5, 89.5, 85.6, 87.4, 78.9, 90.7]])
a, b = y.shape
g = y.mean()
ss_tr = b * ((y.mean(axis=1) - g) ** 2).sum()
ss_bl = a * ((y.mean(axis=0) - g) ** 2).sum()
ss_e = ((y - g) ** 2).sum() - ss_tr - ss_bl
analyses = [("RCBD: MSE = %.2f, df = %d", ss_e / ((a - 1) * (b - 1)), (a - 1) * (b - 1)),
            ("blocks ignored: MSE = %.2f, df = %d", (ss_bl + ss_e) / (a * (b - 1)), a * (b - 1))]

means = y.mean(axis=1)
pairs = [(i, j) for i in range(a) for j in range(i + 1, a)]
labels = [f"{psi[j]}-{psi[i]}" for i, j in pairs]
diffs = np.array([means[j] - means[i] for i, j in pairs])

fig, ax = plt.subplots(figsize=(8, 4.4))
pos = np.arange(len(pairs))[::-1]
for k, (name, mse, df) in enumerate(analyses):
    half = stats.studentized_range.ppf(0.95, a, df) * np.sqrt(mse / b)
    off = 0.15 if k == 0 else -0.15
    ax.errorbar(diffs, pos + off, xerr=half, fmt="o", ms=5, capsize=3, lw=1.6,
                color=f"C{k}", label=name % (mse, df))
ax.axvline(0, color="gray", ls="--", lw=1)
ax.set_yticks(pos)
ax.set_yticklabels(labels)
ax.set_xlabel("difference in mean yield (%)")
ax.set_title("Tukey 95% family-wise intervals")
ax.legend(fontsize=9, loc="lower left")
ax.grid(alpha=0.3)
fig.tight_layout()
