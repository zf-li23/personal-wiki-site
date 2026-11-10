"""Left: sample paths of the uniform empirical process sqrt(n) (F_n(t) - t) for n = 1000, which look like
Brownian bridges. Right: simulated distribution of sqrt(n) D_n for n = 20 under H0 against the
Kolmogorov distribution."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
n = 1000
for k in range(5):
    u = np.sort(rng.uniform(size=n))
    t = np.concatenate([[0.0], np.repeat(u, 2), [1.0]])
    fn = np.concatenate([[0.0], np.repeat(np.arange(n) / n, 2)[1:], [1.0, 1.0]])
    ax.plot(t, np.sqrt(n) * (fn - t), lw=0.9, color=f"C{k}")
ax.axhline(0, color="0.3", lw=0.8)
ax.set_xlim(0, 1)
ax.set_xlabel("$t$")
ax.set_ylabel("$\\sqrt{n}\\,(F_n(t) - t)$")
ax.set_title("empirical process, $n = 1000$", fontsize=11)
ax.grid(alpha=0.3)

ax = axes[1]
n, reps = 20, 20000
u = np.sort(rng.uniform(size=(reps, n)), axis=1)
i = np.arange(1, n + 1)
d = np.maximum((i / n - u).max(axis=1), (u - (i - 1) / n).max(axis=1))
ax.hist(np.sqrt(n) * d, bins=60, density=True, color="C0", alpha=0.45, label="simulated $\\sqrt{n} D_n$, $n = 20$")
s = np.linspace(0.2, 2.2, 400)
ax.plot(s, stats.kstwobign.pdf(s), color="C3", lw=2, label="Kolmogorov density")
ax.axvline(stats.kstwobign.isf(0.05), color="0.3", ls="--", lw=1)
ax.text(stats.kstwobign.isf(0.05) + 0.04, 1.5, "1.358", fontsize=9, color="0.3")
ax.set_xlabel("$x$")
ax.set_ylabel("density")
ax.set_title("null distribution of $\\sqrt{n} D_n$", fontsize=11)
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()
