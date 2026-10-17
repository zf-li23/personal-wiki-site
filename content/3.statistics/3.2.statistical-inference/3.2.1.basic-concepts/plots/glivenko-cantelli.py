"""Kolmogorov distance D_n between the EDF and the true CDF as n grows (20 replications)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def ks_distance(sample):
    x = np.sort(sample)
    n = len(x)
    f = norm.cdf(x)
    i = np.arange(1, n + 1)
    return np.max(np.maximum(i / n - f, f - (i - 1) / n))


ns = np.unique(np.logspace(1, 4, 25).astype(int))
fig, ax = plt.subplots(figsize=(7, 4.2))
for rep in range(20):
    data = np.random.normal(size=ns[-1])
    ax.plot(ns, [ks_distance(data[:n]) for n in ns], color="C0", alpha=0.35, lw=0.9)
ax.plot(ns, 1 / np.sqrt(ns), color="C3", lw=1.6, ls="--", label="reference $1/\\sqrt{n}$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("sample size n")
ax.set_ylabel("$D_n = \\sup_x |F_n(x) - F(x)|$")
ax.set_title("Glivenko-Cantelli: $D_n \\to 0$ almost surely")
ax.legend()
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
