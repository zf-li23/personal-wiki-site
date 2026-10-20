import numpy as np
import matplotlib.pyplot as plt

# Comparisons per element of Shellsort with four gap sequences on random input.


def gaps_shell(n):
    g, h = [], n // 2
    while h > 0:
        g.insert(0, h)
        h //= 2
    return g


def gaps_ps(n):
    g, h = [], 1
    while h < n:
        g.append(h)
        h = 2 * h + 1
    return g


def gaps_pratt(n):
    g, i2, i3 = [1], 0, 0
    while (h := min(2 * g[i2], 3 * g[i3])) < n:
        g.append(h)
        i2 += h == 2 * g[i2]
        i3 += h == 3 * g[i3]
    return g


def gaps_sedgewick(n):
    g, i = [], 0
    while (a := 9 * 4**i - 9 * 2**i + 1) < n:
        g.append(a)
        if (b := 4 ** (i + 2) - 3 * 2 ** (i + 2) + 1) < n:
            g.append(b)
        i += 1
    return g


def shell_sort(a, gaps):
    cmp = 0
    for h in reversed(gaps):
        for j in range(h, len(a)):
            x, i = a[j], j
            while i >= h:
                cmp += 1
                if not x < a[i - h]:
                    break
                a[i] = a[i - h]
                i -= h
            a[i] = x
    return cmp


rng = np.random.default_rng(0)
ns = 2 ** np.arange(6, 14)
seqs = [("Shell: n/2, n/4, ..., 1", gaps_shell, "tab:red"),
        ("Papernov-Stasevich: 2^k - 1", gaps_ps, "tab:orange"),
        ("Pratt: 2^p 3^q", gaps_pratt, "tab:blue"),
        ("Sedgewick 1986: 1, 5, 19, 41, ...", gaps_sedgewick, "tab:green")]
fig, ax = plt.subplots(figsize=(8, 5))
for label, gaps, c in seqs:
    ys = [shell_sort(rng.permutation(n).tolist(), gaps(n)) / n for n in ns]
    ax.plot(ns, ys, marker="o", ms=4, color=c, label=label)
ax.plot(ns, np.log2(ns), color="gray", ls=":", label=r"$\log_2 n$")
ax.set_xscale("log", base=2)
ax.set_xlabel("n")
ax.set_ylabel("comparisons / n")
ax.set_title("Shellsort on random permutations")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
