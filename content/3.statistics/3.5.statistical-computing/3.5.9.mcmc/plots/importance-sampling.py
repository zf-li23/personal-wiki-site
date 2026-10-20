"""Importance sampling. Left: running estimates of E_p[1] = 1 for the target Gamma(0.5, 2.5)
with proposals Gamma(2, 2) (infinite variance, a > 2 alpha) and Gamma(0.5, 1) (finite variance).
Right: 100 estimates of P(X > 4), X ~ N(0, 1), by crude Monte Carlo and by importance
sampling from N(4, 1), each with n = 1000."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
alpha, beta = 0.5, 2.5
n = 5000
steps = np.arange(1, n + 1)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4))
ax = axes[0]
for (a, b), col in (((2.0, 2.0), "C3"), ((0.5, 1.0), "C0")):
    y = rng.gamma(shape=a, scale=1 / b, size=n)
    w = stats.gamma.pdf(y, alpha, scale=1 / beta) / stats.gamma.pdf(y, a, scale=1 / b)
    label = f"proposal Gamma({a:g}, {b:g})" + (": infinite variance" if a > 2 * alpha else ": finite variance")
    ax.plot(steps, np.cumsum(w) / steps, color=col, lw=1.3, label=label)
ax.axhline(1.0, color="C7", ls="--", lw=1)
ax.set_xscale("log")
ax.set_xlabel("number of proposals m")
ax.set_ylabel("running IS estimate of E_p[1]")
ax.set_title("Weights must not explode: check E_p[w] < infinity", fontsize=10)
ax.legend(fontsize=8)

ax = axes[1]
x0, reps, m = 4.0, 100, 1000
truth = stats.norm.sf(x0)
crude = np.array([np.mean(rng.standard_normal(m) > x0) for _ in range(reps)])
isest = []
for _ in range(reps):
    y = rng.normal(x0, 1.0, m)
    w = np.exp(-y ** 2 / 2 + (y - x0) ** 2 / 2)
    isest.append(np.mean(w * (y > x0)))
isest = np.array(isest)
jitter = rng.uniform(-0.12, 0.12, reps)
ax.plot(1 + jitter, crude * 1e5, "o", ms=3, color="C3", alpha=0.7)
ax.plot(2 + jitter, isest * 1e5, "o", ms=3, color="C0", alpha=0.7)
ax.axhline(truth * 1e5, color="C7", ls="--", lw=1, label=f"true value {truth:.3e}")
ax.set_xticks([1, 2])
ax.set_xticklabels(["crude MC", "IS with N(4, 1)"])
ax.set_xlim(0.5, 2.5)
ax.set_ylabel("estimate of P(X > 4)  (x 1e-5)")
ax.set_title(f"sd: crude {crude.std():.1e}, IS {isest.std():.1e}", fontsize=10)
ax.legend(fontsize=8)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
