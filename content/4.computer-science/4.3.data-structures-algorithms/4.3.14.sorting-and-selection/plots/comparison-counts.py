import math
import numpy as np
import matplotlib.pyplot as plt

# Key comparisons of three O(n log n) sorts on random permutations,
# against the information-theoretic lower bound log2(n!).


def quick_sort(a):
    cmp = 0
    rng = np.random.default_rng(1)
    stack = [(0, len(a))]
    while stack:
        lo, hi = stack.pop()
        if hi - lo < 2:
            continue
        r = lo + int(rng.integers(hi - lo))
        a[lo], a[r] = a[r], a[lo]
        pivot, mi = a[lo], lo
        for k in range(lo + 1, hi):
            cmp += 1
            if a[k] < pivot:
                mi += 1
                a[mi], a[k] = a[k], a[mi]
        a[lo], a[mi] = a[mi], a[lo]
        stack += [(lo, mi), (mi + 1, hi)]
    return cmp


def merge_sort(a):
    cmp = 0
    width, n = 1, len(a)
    while width < n:
        out = []
        for lo in range(0, n, 2 * width):
            mid, hi = min(lo + width, n), min(lo + 2 * width, n)
            i, j = lo, mid
            while i < mid and j < hi:
                cmp += 1
                if a[j] < a[i]:
                    out.append(a[j])
                    j += 1
                else:
                    out.append(a[i])
                    i += 1
            out += a[i:mid] + a[j:hi]
        a, width = out, 2 * width
    return cmp


def heap_sort(a):
    cmp, n = 0, len(a)

    def sift(n, i):
        nonlocal cmp
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

    for i in reversed(range(n // 2)):
        sift(n, i)
    for m in range(n - 1, 0, -1):
        a[0], a[m] = a[m], a[0]
        sift(m, 0)
    return cmp


rng = np.random.default_rng(0)
ns = 2 ** np.arange(4, 13)
rows = {"heapsort": [], "quicksort (random pivot)": [], "mergesort": []}
for n in ns:
    for name, f in [("heapsort", heap_sort), ("quicksort (random pivot)", quick_sort), ("mergesort", merge_sort)]:
        runs = [f(rng.permutation(n).tolist()) for _ in range(3)]
        rows[name].append(np.mean(runs) / n)
bound = [math.lgamma(n + 1) / math.log(2) / n for n in ns]

fig, ax = plt.subplots(figsize=(8, 5))
for (name, ys), c in zip(rows.items(), ["tab:purple", "tab:orange", "tab:green"]):
    ax.plot(ns, ys, marker="o", ms=4, color=c, label=name)
ax.plot(ns, bound, color="black", lw=2, ls="--", label=r"lower bound $\log_2 n!\,/\,n$")
ax.plot(ns, 2 * np.log(ns), color="tab:orange", lw=1, ls=":", label=r"$2\ln n$ (quicksort, asymptotic)")
ax.set_xscale("log", base=2)
ax.set_xlabel("n")
ax.set_ylabel("comparisons / n")
ax.set_title("Comparisons per element on random permutations")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
