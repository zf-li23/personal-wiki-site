"""Simulated FDR, FWER and power of no correction, Benjamini-Hochberg and Bonferroni (1000 tests, 80% true nulls)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
m, m0, reps, shift, alpha = 1000, 800, 1000, 2.5, 0.05
names = ["uncorrected", "BH", "Bonferroni"]
fdp = {k: [] for k in names}
anyfalse = {k: [] for k in names}
power = {k: [] for k in names}
ranks = np.arange(1, m + 1)
for _ in range(reps):
    z = rng.standard_normal(m)
    z[m0:] += shift
    p = stats.norm.sf(z)
    srt = np.sort(p)
    below = np.nonzero(srt <= ranks / m * alpha)[0]
    thr = srt[below.max()] if below.size else -1.0
    rej = {"uncorrected": p <= alpha, "BH": p <= thr, "Bonferroni": p <= alpha / m}
    for k in names:
        v = rej[k][:m0].sum()
        r = rej[k].sum()
        fdp[k].append(v / max(r, 1))
        anyfalse[k].append(v > 0)
        power[k].append(rej[k][m0:].mean())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
bins = np.linspace(0, 0.3, 61)
for i, k in enumerate(names):
    ax1.hist(fdp[k], bins=bins, color=f"C{i}", alpha=0.6, label=k)
ax1.axvline(alpha, color="gray", ls="--")
ax1.set_xlabel("false discovery proportion V / max(R, 1)")
ax1.set_ylabel("replications")
ax1.set_title("Distribution of the false discovery proportion")
ax1.legend(frameon=False)

x = np.arange(3)
w = 0.25
for i, k in enumerate(names):
    vals = [np.mean(fdp[k]), np.mean(anyfalse[k]), np.mean(power[k])]
    bars = ax2.bar(x + (i - 1) * w, vals, w, color=f"C{i}", label=k)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.2f}", ha="center", fontsize=8)
ax2.set_xticks(x)
ax2.set_xticklabels(["FDR", "FWER", "power"])
ax2.axhline(alpha, color="gray", ls="--")
ax2.set_ylim(0, 1.1)
ax2.set_title("Averages over 1000 replications")
for ax in (ax1, ax2):
    ax.grid(alpha=0.3, axis="y")
fig.tight_layout()
