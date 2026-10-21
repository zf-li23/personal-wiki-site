"""Page transfers of three join algorithms as a function of the buffer size M."""

import math

import matplotlib.pyplot as plt
import numpy as np

b_r, b_s = 60_000, 1_500   # measurement (probe/outer side), gene (build/inner side)


def bnlj(M):
    return math.ceil(b_s / (M - 2)) * b_r + b_s          # smaller relation outer


def sort_cost(b, M):
    """External merge sort including writing the sorted output."""
    if b <= M:
        return 2 * b
    runs = math.ceil(b / M)
    merges = math.ceil(math.log(runs) / math.log(M - 1) - 1e-12)
    return 2 * b * (1 + merges)


def smj(M):
    return sort_cost(b_r, M) + sort_cost(b_s, M) + b_r + b_s


def hj(M):
    if b_s <= M - 2:
        return b_r + b_s                                   # build side fits in memory
    passes = 0
    size = b_s
    while size > M - 2:                                    # recursive partitioning
        size = math.ceil(size / (M - 1))
        passes += 1
    return 2 * (b_r + b_s) * passes + b_r + b_s


Ms = np.unique(np.round(np.logspace(np.log10(4), np.log10(3000), 300)).astype(int))
fig, ax = plt.subplots(figsize=(7, 4))
ax.loglog(Ms, [bnlj(M) for M in Ms], color="C0", lw=1.6, label="block nested-loop join")
ax.loglog(Ms, [smj(M) for M in Ms], color="C1", lw=1.6, label="sort-merge join")
ax.loglog(Ms, [hj(M) for M in Ms], color="C2", lw=1.6, label="hash join")
ax.axvline(b_s + 2, color="0.5", ls="--", lw=0.8)
ax.text(b_s + 2, 2e7, "  gene fits\n  in memory", fontsize=8.5, va="top")
ax.axhline(b_r + b_s, color="0.5", ls=":", lw=0.8)
ax.text(4.3, (b_r + b_s) * 0.8, "reading both inputs once", fontsize=8.5, va="top")
ax.set_xlabel("buffer pages M")
ax.set_ylabel("page transfers")
ax.set_title("measurement (60,000 pages) joined with gene (1,500 pages)", fontsize=10)
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()
