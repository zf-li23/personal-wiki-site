"""Impurity measures of a two-class node as functions of the proportion p of class 1."""

import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(1e-6, 1 - 1e-6, 501)
entropy = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
gini = 2 * p * (1 - p)
error = np.minimum(p, 1 - p)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(p, entropy, label="entropy (bits)")
ax.plot(p, entropy / 2, linestyle="--", label="entropy / 2")
ax.plot(p, gini, label="Gini index 2p(1 - p)")
ax.plot(p, error, label="misclassification min(p, 1 - p)")
ax.set_xlabel("proportion p of class 1 in the node")
ax.set_ylabel("impurity")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
