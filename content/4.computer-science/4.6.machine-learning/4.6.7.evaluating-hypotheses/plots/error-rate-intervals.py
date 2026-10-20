"""95% confidence intervals for a true error rate from repeated test sets, and interval width versus test-set size."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
p, n, reps, z = 0.2, 50, 100, 1.96
r = rng.binomial(n, p, reps)
e = r / n
half = z * np.sqrt(e * (1 - e) / n)
miss = (e - half > p) | (e + half < p)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.3))
ax = axes[0]
idx = np.arange(reps)
ax.errorbar(idx[~miss], e[~miss], yerr=half[~miss], fmt="o", ms=3, lw=1, color="C0", label="covers true error")
ax.errorbar(idx[miss], e[miss], yerr=half[miss], fmt="o", ms=3, lw=1.5, color="C3", label="misses true error")
ax.axhline(p, color="k", ls="--", lw=1)
ax.set_xlabel("test set")
ax.set_ylabel("error rate")
ax.set_title(f"{reps} test sets of size n = {n}, true error {p}: {miss.sum()} intervals miss")
ax.legend(fontsize=8, loc="upper right")

ax = axes[1]
ns = np.arange(30, 1001)
for q in (0.05, 0.1, 0.2, 0.5):
    ax.plot(ns, z * np.sqrt(q * (1 - q) / ns), label=f"error = {q}")
ax.axhline(0.05, color="gray", ls=":", lw=1)
ax.set_xscale("log")
ax.set_xlabel("test set size n")
ax.set_ylabel("half-width of 95% interval")
ax.set_title("interval half-width shrinks like 1/sqrt(n)")
ax.legend(fontsize=8)
fig.tight_layout()
