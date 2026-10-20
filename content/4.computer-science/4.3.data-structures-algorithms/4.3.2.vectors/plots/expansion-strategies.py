"""Cost of growing a dynamic array by a constant increment versus by doubling:
total copying cost after n appends, and the actual cost of each append."""

import numpy as np
import matplotlib.pyplot as plt


def costs(n, grow, start):
    """Actual cost of each of n appends: 1 for the write plus copying on expansion."""
    capacity, size, out = start, 0, np.empty(n)
    for k in range(n):
        c = 1
        if size == capacity:
            c += size          # copy every element into the new block
            capacity = grow(capacity)
        size += 1
        out[k] = c
    return out


n = 2000
inc = costs(n, lambda c: c + 64, 64)
dbl = costs(n, lambda c: 2 * c, 1)
k = np.arange(1, n + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(k, np.cumsum(inc), color="C3", label="increment by 64")
ax1.plot(k, np.cumsum(dbl), color="C0", label="doubling")
ax1.plot(k, 3 * k, color="C7", ls="--", lw=1, label="3n")
ax1.set_xlabel("number of appends n")
ax1.set_ylabel("total cost")
ax1.set_title("total cost: quadratic vs linear")
ax1.legend()
ax1.grid(alpha=0.3)

m = 70
ax2.bar(k[:m], dbl[:m], color="C0", width=0.8, label="actual cost of each append")
ax2.plot(k[:m], np.cumsum(dbl[:m]) / k[:m], color="C1", lw=2, label="average so far")
ax2.axhline(3, color="C7", ls="--", lw=1)
ax2.set_xlabel("k-th append (doubling, initial capacity 1)")
ax2.set_ylabel("cost")
ax2.set_title("amortized cost below 3")
ax2.legend(loc="upper left")
ax2.grid(alpha=0.3)
fig.tight_layout()
