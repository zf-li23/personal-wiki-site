"""Two common ways axes mislead: a truncated bar axis and a dual y axis (synthetic data)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

dark = sum(to_rgb(plt.rcParams["figure.facecolor"])) < 1.5
BLUE, ORANGE = ("#3987e5", "#d95926") if dark else ("#2a78d6", "#eb6834")

fig, axes = plt.subplots(1, 4, figsize=(12, 3.2), width_ratios=[1, 1, 1.25, 1.25],
                         layout="constrained")

# Truncated versus zero-based bars: a 4 % difference.
viability = [96.0, 100.0]
names = ["treated", "control"]
for ax, bottom, title in [(axes[0], 95, "Truncated axis"), (axes[1], 0, "Zero-based axis")]:
    ax.bar(names, viability, color=[ORANGE, BLUE], width=0.6)
    ax.set_ylim(bottom, 101)
    ax.set_ylabel("Viability (%)")
    ax.set_title(title, fontsize=10)

# Dual axis: two series whose apparent agreement depends on the two arbitrary scales.
t = np.arange(0, 13)
rng = np.random.default_rng(0)
gene_a = 200 * 1.10 ** t + rng.normal(0, 8, t.size)      # grows 10 % per hour
gene_b = 50 * 1.03 ** t + rng.normal(0, 0.6, t.size)     # grows 3 % per hour
ax = axes[2]
ax.plot(t, gene_a, color=BLUE, linewidth=2)
ax.set_ylabel("gene A (counts)", color=BLUE)
ax.set_xlabel("Time (h)")
twin = ax.twinx()
twin.plot(t, gene_b, color=ORANGE, linewidth=2)
twin.set_ylabel("gene B (counts)", color=ORANGE)
twin.set_ylim(gene_b.min() - 0.5, gene_b.max() + 0.5)
ax.set_ylim(gene_a.min() - 15, gene_a.max() + 15)
ax.set_title("Dual y axis: the curves 'agree'", fontsize=10)

# One axis, both series indexed to their value at time 0.
ax = axes[3]
ax.plot(t, gene_a / gene_a[0], color=BLUE, linewidth=2)
ax.plot(t, gene_b / gene_b[0], color=ORANGE, linewidth=2)
ax.text(t[-1], gene_a[-1] / gene_a[0], " A", color=BLUE, va="center")
ax.text(t[-1], gene_b[-1] / gene_b[0], " B", color=ORANGE, va="center")
ax.set_xlim(0, 13.5)
ax.set_ylabel("Fold change vs. 0 h")
ax.set_xlabel("Time (h)")
ax.set_title("Indexed to a common baseline", fontsize=10)

for ax in (axes[0], axes[1], axes[3]):
    ax.spines[["top", "right"]].set_visible(False)
