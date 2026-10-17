"""Bayes' rule: probability of disease given a positive test, as a function of prevalence."""

import numpy as np
import matplotlib.pyplot as plt

prev = np.logspace(-4, -0.3, 400)
fig, ax = plt.subplots(figsize=(7, 4.3))
for acc, c in [(0.95, "C0"), (0.99, "C1"), (0.999, "C2")]:
    post = prev * acc / (prev * acc + (1 - prev) * (1 - acc))
    ax.plot(prev, post, color=c, lw=2, label=f"sensitivity = specificity = {acc}")
p0, a0 = 0.001, 0.95
post0 = p0 * a0 / (p0 * a0 + (1 - p0) * (1 - a0))
ax.plot([p0], [post0], "o", color="C3")
ax.annotate(f"prevalence 0.001: {post0:.4f}", xy=(p0, post0), xytext=(2e-4, 0.35),
            arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
ax.set_xscale("log")
ax.set_xlabel("prevalence P(A)")
ax.set_ylabel("P(disease | positive) = P(A | B)")
ax.set_ylim(0, 1.02)
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
