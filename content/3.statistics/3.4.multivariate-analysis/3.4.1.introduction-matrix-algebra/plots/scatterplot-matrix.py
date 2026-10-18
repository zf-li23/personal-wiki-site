"""Scatter plot matrix of a simulated four-variable data set with two groups."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
p = 4
C = np.array([[1.0, 0.9, 0.2, 0.0], [0.9, 1.0, 0.2, 0.0], [0.2, 0.2, 1.0, -0.85], [0.0, 0.0, -0.85, 1.0]])
A = rng.multivariate_normal([0, 0, 0, 0], C, size=100)
B = rng.multivariate_normal([0.9, -0.9, 0.8, 0.8], C, size=100)
names = ["X1", "X2", "X3", "X4"]

fig, axes = plt.subplots(p, p, figsize=(9, 9))
lim = (-4, 4.5)
for i in range(p):
    for k in range(p):
        ax = axes[i, k]
        if i == k:
            bins = np.linspace(-4, 4.5, 22)
            ax.hist(A[:, k], bins=bins, alpha=0.6, color="C0")
            ax.hist(B[:, k], bins=bins, alpha=0.6, color="C1")
            ax.set_yticks([])
            ax.set_xlim(*lim)
        else:
            ax.scatter(A[:, k], A[:, i], s=6, alpha=0.6, color="C0", label="group A")
            ax.scatter(B[:, k], B[:, i], s=6, alpha=0.6, color="C1", label="group B")
            ax.set_xlim(*lim)
            ax.set_ylim(*lim)
        if i == p - 1:
            ax.set_xlabel(names[k])
        else:
            ax.set_xticklabels([])
        if k == 0 and i != 0:
            ax.set_ylabel(names[i])
        elif k != 0:
            ax.set_yticklabels([])
        if i == 0 and k == 0:
            ax.set_ylabel(names[0])
handles, labels = axes[0, 1].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False)
fig.tight_layout(rect=(0, 0, 1, 0.96))
