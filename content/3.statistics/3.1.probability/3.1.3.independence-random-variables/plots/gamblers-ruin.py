"""Gambler's ruin: ruin probability q(k) for total capital N = a + b, and simulated fortunes."""

import numpy as np
import matplotlib.pyplot as plt

N = 20
k = np.arange(0, N + 1)


def ruin(p, k, N):
    if p == 0.5:
        return 1 - k / N
    r = (1 - p) / p
    return (r**k - r**N) / (1 - r**N)


fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
for p, c in [(0.45, "C3"), (0.5, "C0"), (0.55, "C2")]:
    ax.plot(k, ruin(p, k, N), "o-", ms=3, color=c, label=f"p = {p}")
ax.set_xlabel("initial capital k (N = a + b = 20)")
ax.set_ylabel("ruin probability q(k)")
ax.legend(fontsize=9)
ax.set_title("Ruin probability")

rng = np.random.default_rng(0)
ax = axes[1]
a = 10
for i in range(8):
    x = [a]
    while 0 < x[-1] < N:
        x.append(x[-1] + (1 if rng.random() < 0.5 else -1))
    ax.plot(x, lw=1, color=f"C{i}", alpha=0.85)
ax.axhline(0, color="black", lw=1)
ax.axhline(N, color="black", lw=1, ls="--")
ax.set_xlabel("round n")
ax.set_ylabel("fortune X_n")
ax.set_title("Eight fair games starting from a = 10, stopped at 0 or 20")
fig.tight_layout()
