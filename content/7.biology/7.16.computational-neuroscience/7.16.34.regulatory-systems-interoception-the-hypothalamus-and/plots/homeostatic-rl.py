"""Homeostatic reinforcement learning (Keramati and Gutkin 2014), Definition 34.5.2.

Drive D(h) = |h* - h|^(n/m) in one dimension (n = 4, m = 3), set point h* = 0.
Reward of an outcome that changes the internal state by K: r(h) = D(h) - D(h + K).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
n, m = 4.0, 3.0
h = np.linspace(-3, 1.5, 400)


def D(x):
    return np.abs(x) ** (n / m)


fig, axs = plt.subplots(1, 2, figsize=(10, 3.7))
axs[0].plot(h, D(h), color=P.edge("dna"), lw=2.2)
for h0, K, tok in [(-2.0, 1.0, "positive"), (0.0, 1.0, "negative")]:
    axs[0].annotate("", xy=(h0 + K, D(h0 + K)), xytext=(h0, D(h0)),
                    arrowprops=dict(arrowstyle="->", color=P.edge(tok), lw=1.8))
    axs[0].plot([h0, h0 + K], [D(h0), D(h0 + K)], "o", color=P.edge(tok), ms=4)
axs[0].text(-2.0, D(-2.0) + 0.25, "deprived: r > 0", color=P.edge("positive"), fontsize=8.5, ha="center")
axs[0].text(0.5, D(1.0) + 0.35, "sated: r < 0", color=P.edge("negative"), fontsize=8.5, ha="center")
axs[0].axvline(0, color=P.muted(), lw=0.8, ls=":")
axs[0].set_xlabel("Internal state $h$ (set point $h^* = 0$)")
axs[0].set_ylabel("Drive $D(h)$")
axs[0].set_title("A  Drive and the effect of one outcome ($K = 1$)", loc="left", fontsize=10)
for K, tok in [(0.25, "neutral"), (0.5, "dna"), (1.0, "negative")]:
    axs[1].plot(h, D(h) - D(h + K), color=P.edge(tok), lw=2, label=f"outcome size $K = {K}$")
axs[1].axhline(0, color=P.muted(), lw=0.8)
axs[1].axvline(0, color=P.muted(), lw=0.8, ls=":")
axs[1].set_xlabel("Internal state before the outcome $h$")
axs[1].set_ylabel("Reward $r = D(h) - D(h+K)$")
axs[1].set_title("B  Reward depends on the internal state", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)
for ax in axs:
    ax.grid(True, alpha=0.3)
fig.tight_layout()
