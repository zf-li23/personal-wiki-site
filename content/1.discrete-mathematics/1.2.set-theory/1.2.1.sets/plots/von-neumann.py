"""The von Neumann natural numbers 0 to 3 drawn as nested sets: each number is the set of all smaller
numbers, n + 1 = n U {n}, so a box for n contains one box for each of 0, ..., n - 1 (Definition 1.7.4)."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

COLORS = ["C0", "C1", "C2", "C3"]


def draw(ax, n, x, y, w, h, depth=0):
    """Draw the set n as a box at (x, y) of size w x h, with its elements 0..n-1 inside."""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=COLORS[n], alpha=0.18, ec=COLORS[n], lw=1.6))
    if n == 0:
        ax.text(x + w / 2, y + h / 2, r"$\varnothing$", ha="center", va="center", fontsize=max(13 - 2 * depth, 8))
        return
    pad, gap, top = 0.08, 0.07, 0.32
    inner_w = (w - 2 * pad - gap * (n - 1)) / n
    inner_h = h - pad - top
    for k in range(n):
        draw(ax, k, x + pad + k * (inner_w + gap), y + pad, inner_w, inner_h, depth + 1)
    ax.text(x + w / 2, y + h - top / 2, f"${n}$", ha="center", va="center", fontsize=max(12 - depth, 8))


labels = [r"$0 = \varnothing$", r"$1 = \{0\}$", r"$2 = \{0, 1\}$", r"$3 = \{0, 1, 2\}$"]
widths = [0.9, 1.7, 2.8, 4.3]
fig, ax = plt.subplots(figsize=(10, 3.4))
x = 0.1
for n, w in enumerate(widths):
    draw(ax, n, x, 0.6, w, 2.0)
    ax.text(x + w / 2, 0.3, labels[n], ha="center", va="center", fontsize=12)
    x += w + 0.35
ax.set_xlim(0, x)
ax.set_ylim(0, 2.8)
ax.set_aspect("equal")
ax.axis("off")
