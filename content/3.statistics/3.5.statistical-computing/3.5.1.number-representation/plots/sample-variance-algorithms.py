"""Relative error of four sample-variance algorithms when the data have a large mean compared with their spread."""

from fractions import Fraction

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
z = rng.standard_normal(1000)


def two_pass(x):
    m = x.sum() / len(x)
    return ((x - m) ** 2).sum() / (len(x) - 1)


def textbook(x):
    n = len(x)
    return ((x**2).sum() - x.sum() ** 2 / n) / (n - 1)


def west(x):
    m, t = x[0], 0.0
    for k in range(2, len(x) + 1):
        d = x[k - 1] - m
        m = m + d / k
        t = t + (k - 1) * d * d / k
    return t / (len(x) - 1)


def cotton(x):
    m, t = x[0], 0.0
    for k in range(2, len(x) + 1):
        m_old = m
        m = m + (x[k - 1] - m) / k
        t = t + x[k - 1] ** 2 + (k - 1) * m_old**2 - k * m**2
    return t / (len(x) - 1)


def exact_variance(x):
    # exact rational arithmetic on the stored doubles
    q = [Fraction(float(v)) for v in x]
    m = sum(q) / len(q)
    return float(sum((v - m) ** 2 for v in q) / (len(q) - 1))


shifts = 10.0 ** np.arange(0, 10)
algos = [("two-pass", two_pass), ("West (one pass)", west), ("textbook", textbook), ("Cotton", cotton)]
errors = {name: [] for name, _ in algos}
for c in shifts:
    x = z + c
    ref = exact_variance(x)
    for name, f in algos:
        errors[name].append(max(abs(f(x) - ref) / ref, 1e-17))

fig, ax = plt.subplots(figsize=(7.5, 4.8))
for (name, _), m in zip(algos, ["o", "s", "^", "D"]):
    ax.loglog(shifts, errors[name], marker=m, ms=5, lw=1.2, label=name)
ax.axhline(1, color="0.5", ls=":", lw=1)
ax.set_xlabel("mean of the data c (data = c + N(0, 1) sample, n = 1000)")
ax.set_ylabel("relative error of S^2")
ax.set_title("Subtracting two large sums loses all digits once u c^2 is comparable to the variance", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
