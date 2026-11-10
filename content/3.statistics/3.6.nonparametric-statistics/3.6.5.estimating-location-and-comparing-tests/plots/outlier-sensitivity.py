"""Sensitivity curves: the mean, median and Hodges-Lehmann estimate of the 12 heart-rate differences
when the largest observation (25) is replaced by a value y."""

import numpy as np
import matplotlib.pyplot as plt

base = np.array([-2, 4, 8, -5, 16, 3, 1, 12, 17, 20, 9], dtype=float)   # the data without 25
ys = np.linspace(-60, 120, 721)


def hodges_lehmann(x):
    i, j = np.triu_indices(len(x))
    return np.median((x[i] + x[j]) / 2)


est = {"mean": [], "median": [], "Hodges–Lehmann": []}
for y in ys:
    x = np.append(base, y)
    est["mean"].append(x.mean())
    est["median"].append(np.median(x))
    est["Hodges–Lehmann"].append(hodges_lehmann(x))

fig, ax = plt.subplots(figsize=(7.6, 4.4))
for (label, values), color in zip(est.items(), ["C2", "C0", "C1"]):
    ax.plot(ys, values, color=color, lw=1.9, label=label)
ax.axvline(25, color="0.5", ls=":", lw=1)
ax.text(27, 2.5, "observed value 25", fontsize=8, color="0.4")
ax.set_xlabel("value $y$ of the replaced observation")
ax.set_ylabel("estimate of location")
ax.set_xlim(ys[0], ys[-1])
ax.grid(alpha=0.3)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
