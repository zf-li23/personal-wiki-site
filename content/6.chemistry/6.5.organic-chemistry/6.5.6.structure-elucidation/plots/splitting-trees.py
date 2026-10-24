"""Splitting trees for first-order multiplets. (a) A proton coupled to two equivalent protons
(J = 7 Hz): a 1:2:1 triplet. (b) A proton coupled to two different protons: the vinyl CH of
styrene couples to the trans (J = 17.6 Hz) and the cis (J = 10.9 Hz) terminal protons, a doublet
of doublets with four equal lines. (c) Simulated vinyl region of styrene at 400 MHz: three
doublets of doublets (6.72, 5.75, 5.24 ppm; geminal J = 0.9 Hz)."""

import numpy as np
import matplotlib.pyplot as plt

MHZ = 400.0


def tree(ax, couplings, title):
    """Draw a splitting tree; couplings applied top to bottom (J in Hz)."""
    pos = np.array([0.0])
    level = 3.0
    for j in couplings:
        new = np.concatenate([pos - j / 2, pos + j / 2])
        for p in pos:
            for q in (p - j / 2, p + j / 2):
                ax.plot([p, p, q, q], [level, level - 0.35, level - 0.65, level - 1.0], color="C0", lw=1.2)
        ax.text(max(pos) + j / 2 + 1.5, level - 0.5, f"J = {j:g} Hz", fontsize=9, va="center")
        pos = new
        level -= 1.0
    vals, counts = np.unique(np.round(pos, 6), return_counts=True)
    for v, c in zip(vals, counts):
        ax.plot([v, v], [0, 0.45 * c], color="C3", lw=2.2)
    ax.plot([min(pos) - 3, max(pos) + 3], [0, 0], color="0.6", lw=0.8)
    ax.set_title(title, fontsize=10)
    ax.set_xlim(min(pos) - 4, max(pos) + 18)
    ax.set_ylim(-0.3, 3.3)
    ax.axis("off")


fig, axes = plt.subplots(1, 3, figsize=(10, 3.4), gridspec_kw={"width_ratios": [1, 1.2, 1.6]})
tree(axes[0], [7.0, 7.0], "(a) triplet, 1:2:1")
tree(axes[1], [17.6, 10.9], "(b) doublet of doublets")

w = 0.5
x = np.linspace(5.0, 6.95, 20000)
y = np.zeros_like(x)
for d, js in [(6.72, (17.6, 10.9)), (5.75, (17.6, 0.9)), (5.24, (10.9, 0.9))]:
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            c = d * MHZ + s1 * js[0] / 2 + s2 * js[1] / 2
            y += w / np.pi / ((x * MHZ - c) ** 2 + w**2)
ax = axes[2]
ax.plot(x, y / y.max(), color="C0", lw=1)
ax.set_xlim(6.95, 5.0)
ax.set_yticks([])
ax.set_xlabel(r"$\delta$ / ppm")
for d, t in [(6.72, "H$_a$"), (5.75, "H$_b$ (trans to H$_a$)"), (5.24, "H$_c$ (cis to H$_a$)")]:
    ax.text(d, 1.05, t, ha="center", fontsize=8)
ax.set_ylim(0, 1.25)
ax.set_title("(c) styrene, vinyl protons", fontsize=10)
fig.tight_layout()
