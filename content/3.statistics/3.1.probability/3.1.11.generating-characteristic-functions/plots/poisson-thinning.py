"""Poisson thinning: N ~ Poi(10) eggs, each hatches with prob 0.3; W ~ Poi(3)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lam, p, reps = 10.0, 0.3, 20000
n = np.random.poisson(lam, size=reps)
w = np.random.binomial(n, p)

k = np.arange(0, 13)
freq = np.array([(w == j).mean() for j in k])

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(k, freq, width=0.7, color="C0", alpha=0.6, label="simulated W (20000 runs)")
ax.plot(k, stats.poisson.pmf(k, lam * p), "o-", color="C3", lw=1.5, label="Poi(lambda p) = Poi(3)")
ax.set_xlabel("k")
ax.set_ylabel("P(W = k)")
ax.set_title("Random sum of Bernoulli(0.3) over N ~ Poi(10) terms")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
