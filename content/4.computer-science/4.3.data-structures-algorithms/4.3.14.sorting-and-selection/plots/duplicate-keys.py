import numpy as np
import matplotlib.pyplot as plt

# Comparisons of quicksort with four partition schemes when the input
# has only d distinct keys (n = 1024, random pivots).


def make_sort(scheme, rng):
    cmp = 0

    def less(x, y):
        nonlocal cmp
        cmp += 1
        return x < y

    def partition(a, lo, hi):
        r = lo + int(rng.integers(hi - lo))
        a[lo], a[r] = a[r], a[lo]
        pivot = a[lo]
        if scheme in ("LUG", "DUP"):
            strict = scheme == "DUP"
            while lo < hi:
                hi -= 1
                while lo < hi and (less(pivot, a[hi]) if strict else not less(a[hi], pivot)):
                    hi -= 1
                if lo < hi:
                    a[lo] = a[hi]
                lo += 1
                while lo < hi and (less(a[lo], pivot) if strict else not less(pivot, a[lo])):
                    lo += 1
                if lo < hi:
                    a[hi] = a[lo]
            a[hi] = pivot
            return hi, hi + 1
        if scheme == "LGU":
            mi = lo
            for k in range(lo + 1, hi):
                if less(a[k], pivot):
                    mi += 1
                    a[mi], a[k] = a[k], a[mi]
            a[lo], a[mi] = a[mi], a[lo]
            return mi, mi + 1
        lt, i, gt = lo, lo, hi
        while i < gt:
            if less(a[i], pivot):
                a[lt], a[i] = a[i], a[lt]
                lt, i = lt + 1, i + 1
            elif less(pivot, a[i]):
                gt -= 1
                a[i], a[gt] = a[gt], a[i]
            else:
                i += 1
        return lt, gt

    def sort(a):
        stack = [(0, len(a))]
        while stack:
            lo, hi = stack.pop()
            if hi - lo > 1:
                l, g = partition(a, lo, hi)
                stack += [(lo, l), (g, hi)]
        return cmp

    return sort


n = 1024
ds = 2 ** np.arange(0, 11)
rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(8, 5))
for scheme, c in zip(["LUG", "LGU", "DUP", "3-way"], ["tab:red", "tab:orange", "tab:blue", "tab:green"]):
    ys = []
    for d in ds:
        a = rng.integers(0, d, n).tolist()
        ys.append(make_sort(scheme, rng)(a) / (n * np.log2(n)))
    ax.plot(ds, ys, marker="o", ms=4, color=c, label=scheme)
ax.set_xscale("log", base=2)
ax.set_yscale("log")
ax.set_xlabel("number of distinct keys d")
ax.set_ylabel(r"comparisons / $(n \log_2 n)$")
ax.set_title(f"Quicksort with duplicate keys (n = {n})")
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
