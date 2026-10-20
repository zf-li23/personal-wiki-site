"""Average number of key comparisons of a successful search against log2(n),
for binary search versions A and C and for Fibonacci search, at n = F(k) - 1."""

import numpy as np
import matplotlib.pyplot as plt


def version_a(n, r):
    lo, hi, c = 0, n, 0
    while lo < hi:
        mi = (lo + hi) // 2
        c += 1
        if r < mi:
            hi = mi
            continue
        c += 1
        if mi < r:
            lo = mi + 1
        else:
            return c
    return c


def fibonacci(n, r):
    lo, hi, c = 0, n, 0
    f, g = 1, 0
    while f <= hi:
        f, g = f + g, f
    while lo < hi:
        while hi - lo < f:
            f, g = g, f - g
        mi = lo + f - 1
        c += 1
        if r < mi:
            hi = mi
            continue
        c += 1
        if mi < r:
            lo = mi + 1
        else:
            return c
    return c


def version_c(n, r):
    lo, hi, c = 0, n, 0
    while lo < hi:
        mi = (lo + hi) // 2
        c += 1
        if r < mi:
            hi = mi
        else:
            lo = mi + 1
    return c + 1           # one final comparison to confirm the hit


fib = [1, 2]
while fib[-1] < 30000:
    fib.append(fib[-1] + fib[-2])
sizes = np.array([f - 1 for f in fib if 20 <= f <= 30000])   # n = F(k) - 1
x = np.log2(sizes)
fig, ax = plt.subplots(figsize=(7, 4))
for search, label, color in ((version_a, "binary search, version A", "C3"),
                             (fibonacci, "Fibonacci search", "C2"),
                             (version_c, "binary search, version C", "C0")):
    y = np.array([np.mean([search(n, r) for r in range(n)]) for n in sizes])
    slope = np.polyfit(x, y, 1)[0]
    ax.plot(x, y, "o-", ms=3, color=color, label=f"{label} (slope {slope:.2f})")
ax.set_xlabel("log2(n)")
ax.set_ylabel("average comparisons (successful search)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
