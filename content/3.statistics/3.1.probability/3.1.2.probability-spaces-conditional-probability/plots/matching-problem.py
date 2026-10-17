"""Matching problem: probability of no match q0(n) and the distribution of the number of matches."""

import math
import numpy as np
import matplotlib.pyplot as plt


def q(r, n):
    """Probability of exactly r correct letters among n."""
    return sum((-1) ** k / math.factorial(k) for k in range(n - r + 1)) / math.factorial(r)


fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ns = np.arange(1, 13)
q0 = [q(0, n) for n in ns]
ax = axes[0]
ax.plot(ns, q0, "o-", color="C0", label="q0(n) = sum_{k=0}^{n} (-1)^k / k!")
ax.axhline(math.exp(-1), color="C3", ls="--", lw=1.2, label="1/e = 0.3679")
ax.set_xlabel("number of letters n")
ax.set_ylabel("P(no letter in the correct envelope)")
ax.set_xticks(ns)
ax.set_ylim(-0.05, 0.6)
ax.legend(fontsize=8)
ax.set_title("No match: rapid convergence to 1/e")

n = 10
rs = np.arange(0, 7)
exact = [q(r, n) for r in rs]
poisson = [math.exp(-1) / math.factorial(r) for r in rs]
rng = np.random.default_rng(0)
sims = np.array([(rng.permutation(n) == np.arange(n)).sum() for _ in range(20000)])
freq = [(sims == r).mean() for r in rs]
ax = axes[1]
w = 0.27
ax.bar(rs - w, exact, width=w, color="C0", label=f"exact q_r({n})")
ax.bar(rs, poisson, width=w, color="C1", label="limit e^{-1} / r!")
ax.bar(rs + w, freq, width=w, color="C2", label="20000 random permutations")
ax.set_xlabel("number of correct letters r")
ax.set_ylabel("probability")
ax.set_title(f"Number of matches, n = {n}")
ax.legend(fontsize=8)
fig.tight_layout()
