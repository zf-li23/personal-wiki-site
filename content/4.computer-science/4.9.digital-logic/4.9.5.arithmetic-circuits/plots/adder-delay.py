"""Gate levels on the critical path of an n-bit adder under a simple model
(generate/propagate: 1 level, each AND-OR carry step: 2 levels, sum XOR: 1 level).
Ripple carry grows linearly, a two-level 4-bit lookahead tree grows in steps,
and a parallel-prefix (Kogge-Stone) adder grows logarithmically. The lookahead
units use gates with up to five inputs, the prefix adder only two-input gates."""

import numpy as np
import matplotlib.pyplot as plt

n = np.array([4, 8, 16, 32, 64])
ripple = 1 + 2 * n + 1
prefix = 1 + 2 * np.log2(n) + 1
# lookahead in groups of 4: each level of the tree costs 2 levels up and 2 down
levels = np.ceil(np.log(n) / np.log(4))
lookahead = 1 + 2 * (2 * levels - 1) + 1

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(n, ripple, "o-", label="ripple carry")
ax.plot(n, lookahead, "s-", label="carry lookahead (groups of 4)")
ax.plot(n, prefix, "^-", label="parallel prefix (Kogge-Stone)")
ax.set_xscale("log", base=2)
ax.set_xticks(n)
ax.set_xticklabels([str(v) for v in n])
ax.set_xlabel("word width n (bits)")
ax.set_ylabel("gate levels on the critical path")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()
