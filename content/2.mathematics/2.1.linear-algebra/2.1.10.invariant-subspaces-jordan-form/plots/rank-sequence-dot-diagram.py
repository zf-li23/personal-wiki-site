"""Jordan structure of a nilpotent matrix read off from its rank sequence
(Example 10.9.1: blocks of orders 3, 2, 1)."""

import numpy as np
import matplotlib.pyplot as plt

blocks = [3, 2, 1]
n = sum(blocks)
ranks = [n] + [sum(max(b - k, 0) for b in blocks) for k in range(1, max(blocks) + 2)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2),
                               gridspec_kw={"width_ratios": [1, 1.1]})

# Left: rank sequence r_k = rank(A^k) and its drops
ks = np.arange(len(ranks))
ax1.plot(ks, ranks, "o-", markersize=8, linewidth=2)
for k in range(1, len(ranks)):
    drop = ranks[k - 1] - ranks[k]
    if drop:
        ax1.annotate(f"drop {drop}", xy=(k - 0.5, (ranks[k - 1] + ranks[k]) / 2),
                     xytext=(8, 4), textcoords="offset points", fontsize=10)
ax1.set_xticks(ks)
ax1.set_xlabel(r"$k$")
ax1.set_ylabel(r"$r_k = \operatorname{rank}(A^k)$")
ax1.set_title("Rank sequence: drops count blocks of order at least k")
ax1.grid(True, alpha=0.3)

# Right: dot diagram, one column per Jordan chain, row d = level d of the chain
for j, b in enumerate(blocks):
    for d in range(1, b + 1):
        ax2.plot(j, d, "o", markersize=22, color="C0" if d == 1 else "C1")
        power = b - d
        prefix = "" if power == 0 else ("A" if power == 1 else "A^{%d}" % power)
        label = r"$%s\boldsymbol{v}_%d$" % (prefix, j + 1)
        ax2.annotate(label, (j, d), xytext=(18, -4), textcoords="offset points", fontsize=10)
    for d in range(1, b):
        ax2.annotate("", xy=(j, d + 0.22), xytext=(j, d + 0.78),
                     arrowprops=dict(arrowstyle="->", lw=1.4, color="gray"))
for d in range(1, max(blocks) + 1):
    count = sum(1 for b in blocks if b >= d)
    ax2.text(len(blocks) + 0.2, d, rf"row {d}: {count} = $r_{{{d - 1}}} - r_{{{d}}}$",
             va="center", fontsize=10)
ax2.set_xlim(-0.6, len(blocks) + 2.4)
ax2.set_ylim(0.4, max(blocks) + 0.7)
ax2.set_xticks(range(len(blocks)))
ax2.set_xticklabels([rf"$J_{{0,{b}}}$" for b in blocks])
ax2.set_yticks(range(1, max(blocks) + 1))
ax2.set_ylabel("level in the Jordan chain")
ax2.set_title("Jordan chains: arrows apply A, bottom row = eigenvectors")
for side in ["top", "right"]:
    ax2.spines[side].set_visible(False)
fig.tight_layout()
