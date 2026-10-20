"""Monte Carlo estimate of pi from n uniform points in the unit square:
the absolute error of 100 independent estimates against n, with the
standard error sqrt(pi (4 - pi) / n)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
sizes = np.logspace(2, 5.5, 8).astype(int)
reps = 100


def estimate_pi(n):
    pts = rng.random((n, 2))
    return 4.0 * np.mean((pts ** 2).sum(axis=1) <= 1.0)


errors = np.array([[abs(estimate_pi(n) - np.pi) for _ in range(reps)] for n in sizes])

fig, ax = plt.subplots(figsize=(7, 4.5))
for n, e in zip(sizes, errors):
    ax.scatter(np.full(reps, n), e, s=5, color="C0", alpha=0.3, linewidths=0)
ax.loglog(sizes, np.sqrt((errors ** 2).mean(axis=1)), "o-", color="C1", label="root mean square error")
ax.loglog(sizes, np.sqrt(np.pi * (4 - np.pi) / sizes), "--", color="C7", label="sqrt(pi (4 - pi) / n)")
ax.set_xlabel("number of points n")
ax.set_ylabel("|estimate - pi|")
ax.set_title("Monte Carlo error decreases like 1 / sqrt(n)")
ax.set_ylim(1e-5, 1)
ax.legend(loc="lower left")
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
