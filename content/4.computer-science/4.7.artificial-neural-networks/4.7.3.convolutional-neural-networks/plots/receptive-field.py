"""Receptive fields of stacked convolutions. Left: three 1-D layers with kernel
size 3 and stride 1; the output unit at the top sees 7 inputs. Middle: the same
stack with stride 2 in the first two layers; it sees 15 inputs. Right: in 2-D,
one unit after one, two and three 3x3 layers (stride 1) sees a 3x3, 5x5 and
7x7 patch of the input."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def draw_stack(ax, n_in, kernels, strides, title):
    # positions of units in each layer, in input coordinates
    layers = [np.arange(n_in, dtype=float)]
    for k, s in zip(kernels, strides):
        prev = layers[-1]
        n_out = (len(prev) - k) // s + 1
        layers.append(np.array([prev[i * s:i * s + k].mean() for i in range(n_out)]))
    # trace the receptive field of the middle unit of the top layer backwards
    active = [None] * len(layers)
    top = len(layers) - 1
    active[top] = {len(layers[top]) // 2}
    for l in range(top, 0, -1):
        k, s = kernels[l - 1], strides[l - 1]
        active[l - 1] = {i * s + u for i in active[l] for u in range(k)}
    for l, xs in enumerate(layers):
        for i, x in enumerate(xs):
            on = i in active[l]
            ax.scatter(x, l, s=60 if on else 25, color="C3" if on else "C7",
                       zorder=3, alpha=1.0 if on else 0.5)
            if l > 0 and on:
                k, s = kernels[l - 1], strides[l - 1]
                for u in range(k):
                    ax.plot([layers[l - 1][i * s + u], x], [l - 1, l], color="C3", lw=0.9, alpha=0.7)
    width = len(active[0])
    ax.set_yticks(range(len(layers)))
    ax.set_yticklabels(["input"] + [f"layer {l}" for l in range(1, len(layers))])
    ax.set_xticks([])
    ax.set_title(f"{title}\nreceptive field = {width}", fontsize=10)
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)


fig, axes = plt.subplots(1, 3, figsize=(14, 3.8), gridspec_kw={"width_ratios": [1, 1.6, 1]})
draw_stack(axes[0], 11, [3, 3, 3], [1, 1, 1], "k = 3, stride 1, 1, 1")
draw_stack(axes[1], 23, [3, 3, 3], [2, 2, 1], "k = 3, stride 2, 2, 1")

ax = axes[2]
n = 9
for i in range(n + 1):
    ax.plot([0, n], [i, i], color="C7", lw=0.5)
    ax.plot([i, i], [0, n], color="C7", lw=0.5)
for r, color, label in [(3, "C3", "after 3 layers: 7x7"), (2, "C1", "after 2 layers: 5x5"), (1, "C0", "after 1 layer: 3x3")]:
    c = n // 2
    ax.add_patch(Rectangle((c - r, c - r), 2 * r + 1, 2 * r + 1, facecolor=color, alpha=0.35,
                           edgecolor=color, lw=1.5, label=label))
ax.add_patch(Rectangle((n // 2, n // 2), 1, 1, facecolor="k", alpha=0.8))
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("2-D: stacked 3x3 convolutions", fontsize=10)
ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=1, frameon=False)
fig.tight_layout()
