import numpy as np
import matplotlib.pyplot as plt

# Comparisons per element of the two heap-construction methods (max-heap)


def top_down(a):
    a, cmp = list(a), 0
    for i in range(1, len(a)):
        x = a[i]
        while i > 0:
            cmp += 1
            p = (i - 1) // 2
            if not a[p] < x:
                break
            a[i] = a[p]
            i = p
        a[i] = x
    return cmp


def bottom_up(a):
    a, cmp, n = list(a), 0, len(a)
    for i in reversed(range(n // 2)):
        x = a[i]
        while (c := 2 * i + 1) < n:
            if c + 1 < n:
                cmp += 1
                if a[c] < a[c + 1]:
                    c += 1
            cmp += 1
            if not x < a[c]:
                break
            a[i] = a[c]
            i = c
        a[i] = x
    return cmp


rng = np.random.default_rng(0)
ks = np.arange(4, 15)
ns = 2**ks - 1
series = {
    "top-down, increasing input (worst case)": [top_down(range(n)) / n for n in ns],
    "top-down, random input": [top_down(rng.permutation(n).tolist()) / n for n in ns],
    "Floyd bottom-up, increasing input": [bottom_up(range(n)) / n for n in ns],
    "Floyd bottom-up, random input": [bottom_up(rng.permutation(n).tolist()) / n for n in ns],
}

fig, ax = plt.subplots(figsize=(8, 5))
styles = [("tab:red", "-"), ("tab:red", "--"), ("tab:blue", "-"), ("tab:blue", "--")]
for (label, ys), (c, ls) in zip(series.items(), styles):
    ax.plot(ns, ys, marker="o", ms=4, color=c, ls=ls, label=label)
ax.axhline(2, color="gray", lw=1, ls=":")
ax.text(ns[0], 2.15, "2 comparisons per element", color="gray", fontsize=9)
ax.set_xscale("log", base=2)
ax.set_xlabel("heap size n")
ax.set_ylabel("comparisons / n")
ax.set_title("Building a heap: top-down insertion vs. Floyd's bottom-up heapify")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
