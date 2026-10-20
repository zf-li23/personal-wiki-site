import numpy as np
import matplotlib.pyplot as plt

# Character comparisons per text character when reporting all occurrences
# of a random pattern in a random text, as the alphabet grows.


def brute(t, p):
    n, m, cmp = len(t), len(p), 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            cmp += 1
            if t[i + j] != p[j]:
                break
            j += 1
    return cmp


def kmp(t, p):
    m = len(p)
    nxt, j, k = [-1] * (m + 1), 0, -1
    while j < m:
        if k < 0 or p[k] == p[j]:
            k, j = k + 1, j + 1
            nxt[j] = k
        else:
            k = nxt[k]
    cmp, i, j = 0, 0, 0
    while i < len(t):
        if j < 0:
            i, j = i + 1, 0
            continue
        cmp += 1
        if t[i] == p[j]:
            i, j = i + 1, j + 1
            if j == m:
                j = nxt[m]
        else:
            j = nxt[j]
    return cmp


def good_suffix(p):
    m = len(p)
    gs = []
    for j in range(m):
        for s in range(1, m + 1):
            if all(k - s < 0 or p[k - s] == p[k] for k in range(j + 1, m)) and (j - s < 0 or p[j - s] != p[j]):
                gs.append(s)
                break
    return gs


def bm(t, p, use_gs):
    n, m = len(t), len(p)
    bc = {}
    for j, c in enumerate(p):
        bc[c] = j
    gs = good_suffix(p) if use_gs else [1] * m
    border = max(b for b in range(m) if p[:b] == p[m - b:])
    period = m - border if use_gs else 1  # shift after a full match
    cmp, i = 0, 0
    while i + m <= n:
        j = m - 1
        while j >= 0:
            cmp += 1
            if p[j] != t[i + j]:
                break
            j -= 1
        if j < 0:
            i += period
        else:
            i += max(gs[j], j - bc.get(t[i + j], -1))
    return cmp


rng = np.random.default_rng(0)
sizes = [2, 4, 8, 16, 32, 64, 128]
n = 20000
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=True)
for ax, m in zip(axes, (8, 32)):
    rows = {"brute force": [], "KMP": [], "BM, bad character only": [], "BM, bad character + good suffix": []}
    for s in sizes:
        t = "".join(chr(33 + c) for c in rng.integers(0, s, n))
        p = "".join(chr(33 + c) for c in rng.integers(0, s, m))
        rows["brute force"].append(brute(t, p) / n)
        rows["KMP"].append(kmp(t, p) / n)
        rows["BM, bad character only"].append(bm(t, p, False) / n)
        rows["BM, bad character + good suffix"].append(bm(t, p, True) / n)
    for (label, ys), c in zip(rows.items(), ["tab:gray", "tab:blue", "tab:orange", "tab:red"]):
        ax.plot(sizes, ys, marker="o", ms=4, color=c, label=label)
    ax.axhline(1 / m, color="gray", lw=1, ls=":")
    ax.text(sizes[-1], 1 / m * 1.15, "1/m", color="gray", fontsize=9, ha="right")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xlabel("alphabet size s")
    ax.set_title(f"pattern length m = {m}, text length n = {n}")
    ax.grid(alpha=0.3, which="both")
axes[0].set_ylabel("comparisons / n")
axes[0].legend(fontsize=9)
fig.tight_layout()
