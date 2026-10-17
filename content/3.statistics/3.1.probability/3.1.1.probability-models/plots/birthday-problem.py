"""Birthday problem: probability that among n people at least two share a birthday (365 days)."""

import numpy as np
import matplotlib.pyplot as plt

N = 365
n = np.arange(1, 81)
p_distinct = np.cumprod((N - n + 1) / N)
p_share = 1 - p_distinct
approx = 1 - np.exp(-n * (n - 1) / (2 * N))

fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(n, p_share, color="C0", lw=2, label="exact: 1 - N!/((N-n)! N^n)")
ax.plot(n, approx, color="C1", lw=1.5, ls="--", label="approx: 1 - exp(-n(n-1)/(2N))")
ax.axhline(0.5, color="gray", lw=0.8, ls=":")
n50 = int(n[np.argmax(p_share >= 0.5)])
ax.axvline(n50, color="gray", lw=0.8, ls=":")
ax.annotate(f"n = {n50}: {p_share[n50 - 1]:.3f}", xy=(n50, p_share[n50 - 1]), xytext=(n50 + 8, 0.35),
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_xlabel("number of people n")
ax.set_ylabel("P(at least two share a birthday)")
ax.set_xlim(0, 80)
ax.set_ylim(0, 1.02)
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
