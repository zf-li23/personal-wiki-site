"""Growth of receptive field size along a convolutional hierarchy.

For a stack of layers with kernel size K_l and stride s_l, the receptive field r_l (in input pixels)
and the jump j_l (input distance between neighbouring units) obey
    r_l = r_(l-1) + (K_l - 1) j_(l-1),   j_l = j_(l-1) s_l,   r_0 = j_0 = 1.
A: three architectures: 3x3 convolutions with stride 1 (r = 1 + 2L), the same with 2x2 pooling
(stride 2) after every second layer, and an AlexNet-like stack (kernels 11, 3, 5, 3, 3, 3, 3, 3 with
strides 4, 2, 1, 2, 1, 1, 1, 2). B: the schematic of three layers of 3-wide kernels, showing how one
unit at layer 3 depends on a growing window of the input.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def rf(kernels, strides):
    r, j, out = 1, 1, [1]
    for k, s in zip(kernels, strides):
        r = r + (k - 1) * j
        j = j * s
        out.append(r)
    return out


L = 12
archs = {
    "3x3 conv, stride 1": rf([3] * L, [1] * L),
    "3x3 conv + 2x2 pooling every 2 layers": rf([3, 2] * (L // 2), [1, 2] * (L // 2)),
}
alex_k, alex_s = [11, 3, 5, 3, 3, 3, 3, 3], [4, 2, 1, 2, 1, 1, 1, 2]
archs["AlexNet-like (conv and pool layers)"] = rf(alex_k, alex_s)

fig, axs = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [1.2, 1]})
ax = axs[0]
cols = [P.edge("dna"), P.edge("rna"), P.edge("positive")]
for (lab, vals), c in zip(archs.items(), cols):
    ax.plot(range(len(vals)), vals, "o-", color=c, lw=1.6, ms=4, label=lab)
ax.set_yscale("log")
ax.set_xlabel("Layer")
ax.set_ylabel("Receptive field size / input pixels")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Linear growth without pooling, geometric with it", loc="left", fontsize=10)

bx = axs[1]
bx.axis("off")
n = 11
for l in range(4):
    half = 3 - l
    for i in range(n):
        x = i - (n - 1) / 2
        inside = abs(x) <= half
        bx.add_patch(plt.Circle((x, l * 1.4), 0.28, facecolor=P.fill("neuron") if inside else "none",
                                edgecolor=P.edge("neuron") if inside else P.muted(), lw=1))
    if l > 0:
        for i in range(-half, half + 1):
            for dxx in (-1, 0, 1):
                bx.plot([i, i + dxx], [l * 1.4 - 0.28, (l - 1) * 1.4 + 0.28], color=P.muted(), lw=0.6)
    bx.text(-(n - 1) / 2 - 1.2, l * 1.4, "input" if l == 0 else f"layer {l}", ha="right", va="center",
            fontsize=8.5, color=P.ink())
bx.text(0, 4 * 1.4 - 0.2, "one unit at layer 3 sees 7 input pixels: 1 + 3 (3 - 1)", ha="center", fontsize=8.5,
        color=P.ink())
bx.set_xlim(-8.5, 6)
bx.set_ylim(-0.6, 5.8)
bx.set_aspect("equal")
bx.set_title("B  Receptive field of a unit (3-wide kernels)", loc="left", fontsize=10)
fig.tight_layout()
