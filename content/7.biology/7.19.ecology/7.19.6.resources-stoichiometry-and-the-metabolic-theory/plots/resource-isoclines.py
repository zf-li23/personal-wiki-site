"""Resource-dependent growth isoclines for pairs of resources (after Tilman 1982).

Per-capita growth g(R1, R2) - m with saturating uptake f(x) = x / (1 + x) and mortality m = 0.5, so the zero
isocline is where f(.) = 0.5. Contours: g = -0.15 (dashed), 0 (thick), +0.15 (dotted).
(a) essential: g = min(f(R1), f(R2)) - m
(b) perfectly substitutable: g = f(R1 + 0.5 R2) - m
(c) complementary: g = f(Q) - m with Q = R1 + R2 + 1.5 sqrt(R1 R2)
(d) antagonistic: Q = R1 + R2 - 0.6 sqrt(R1 R2)
(e) inhibitory: g = min(h(R1), h(R2)) - m with h(x) = 2.2 x / (1 + x + x^2 / 1.5)
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
r = np.linspace(0.001, 5, 400)
R1, R2 = np.meshgrid(r, r)


def f(x):
    return x / (1 + x)


def h(x):
    return 2.2 * x / (1 + x + x ** 2 / 1.5)


m = 0.5
cases = [
    ("a  Essential", np.minimum(f(R1), f(R2)) - m),
    ("b  Perfectly substitutable", f(R1 + 0.5 * R2) - m),
    ("c  Complementary", f(R1 + R2 + 1.5 * np.sqrt(R1 * R2)) - m),
    ("d  Antagonistic", f(np.maximum(R1 + R2 - 0.6 * np.sqrt(R1 * R2), 0)) - m),
    ("e  Inhibitory", np.minimum(h(R1), h(R2)) - m),
]
fig, axes = plt.subplots(1, 5, figsize=(15.0, 3.5))
for ax, (title, g) in zip(axes, cases):
    ax.contourf(R1, R2, g, levels=[0, 10], colors=[P.fill("positive")], alpha=0.25)
    ax.contour(R1, R2, g, levels=[-0.15], colors=[P.edge("negative")], linewidths=1.3, linestyles="--")
    ax.contour(R1, R2, g, levels=[0.0], colors=[P.ink()], linewidths=2.2)
    ax.contour(R1, R2, g, levels=[0.15], colors=[P.edge("positive")], linewidths=1.3, linestyles=":")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("resource 1, $R_1$", fontsize=9)
    ax.set_title(title, loc="left", fontsize=9.5)
axes[0].set_ylabel("resource 2, $R_2$", fontsize=9)
axes[0].text(4.9, 4.7, "growth > 0", ha="right", fontsize=8, color=P.edge("positive"))
axes[0].text(0.2, 0.25, "growth < 0", fontsize=8, color=P.edge("negative"))
fig.tight_layout()
