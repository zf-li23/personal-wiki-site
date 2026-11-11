"""Representational similarity analysis (RSA) with a small hand-built convolutional hierarchy.

Stimuli: 48 images (32 x 32 pixels) in 4 categories (horizontal bar, vertical bar, diagonal bar,
cross), 12 exemplars each, with random position (shifts of up to 8 pixels), contrast and noise.
Model stages: pixels; layer 1 = energy of a bank of 4 oriented Gabor filters (quadrature pairs) at
every position; layer 2 = max pooling over 4 x 4 blocks; layer 3 = global max pooling (position
invariant). Synthetic "IT" responses: 60 units, each a random positive mixture of the layer-3
features passed through a rectifying nonlinearity, plus noise.
RDM entry (i, j) = 1 - Pearson correlation between response patterns to stimuli i and j.
A: RDMs of pixels, layer 3 and the synthetic IT population. B: Spearman correlation between the
upper triangle of each model RDM and the IT RDM.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import fftconvolve
from scipy.stats import spearmanr

import wikibio as bio

P = bio.P
rng = np.random.default_rng(7)
S = 32
yy, xx = np.mgrid[0:S, 0:S] - S / 2


def bar(angle, cx, cy, length=9, width=1.6):
    u = (xx - cx) * np.cos(angle) + (yy - cy) * np.sin(angle)
    v = -(xx - cx) * np.sin(angle) + (yy - cy) * np.cos(angle)
    return ((np.abs(u) < length) & (np.abs(v) < width)).astype(float)


imgs, labels = [], []
for c, ang in enumerate((0, np.pi / 2, np.pi / 4, None)):
    for e in range(12):
        cx, cy = rng.uniform(-8, 8, 2)
        im = bar(0, cx, cy) + bar(np.pi / 2, cx, cy) if ang is None else bar(ang, cx, cy)
        im = np.clip(im, 0, 1) * rng.uniform(0.5, 1.0) + rng.normal(0, 0.15, (S, S))
        imgs.append(im)
        labels.append(c)
imgs = np.array(imgs)

ks = np.arange(-6, 7)
KX, KY = np.meshgrid(ks, ks)
bank = []
for th in np.arange(4) * np.pi / 4:
    u = KX * np.cos(th) + KY * np.sin(th)
    env = np.exp(-(KX**2 + KY**2) / (2 * 2.5**2))
    bank.append((env * np.cos(2 * np.pi * u / 6), env * np.sin(2 * np.pi * u / 6)))


def layer1(im):
    return np.array([fftconvolve(im, a, mode="same") ** 2 + fftconvolve(im, b, mode="same") ** 2 for a, b in bank])


L1 = np.array([layer1(im) for im in imgs])
L2 = L1.reshape(48, 4, 8, 4, 8, 4).max(axis=(3, 5))
L3 = L1.max(axis=(2, 3))
mix = np.abs(rng.normal(size=(4, 60)))
IT = np.maximum(L3 / L3.std(0) @ mix - 1.0, 0) + rng.normal(0, 0.3, (48, 60))
reps = {"pixels": imgs.reshape(48, -1), "layer 1": L1.reshape(48, -1), "layer 2": L2.reshape(48, -1),
        "layer 3": L3, "IT (synthetic)": IT}
rdm = {k: 1 - np.corrcoef(v) for k, v in reps.items()}
iu = np.triu_indices(48, 1)

fig = plt.figure(figsize=(13, 4.2))
for j, k in enumerate(("pixels", "layer 3", "IT (synthetic)")):
    ax = fig.add_axes([0.02 + 0.2 * j, 0.14, 0.18, 0.7])
    ax.imshow(rdm[k], cmap="viridis", vmin=0, vmax=np.percentile(rdm[k][iu], 98))
    for b in (12, 24, 36):
        ax.axhline(b - 0.5, color="white", lw=0.5)
        ax.axvline(b - 0.5, color="white", lw=0.5)
    ax.set_xticks([6, 18, 30, 42])
    ax.set_xticklabels(["H", "V", "D", "X"], fontsize=8)
    ax.set_yticks([6, 18, 30, 42])
    ax.set_yticklabels(["H", "V", "D", "X"], fontsize=8)
    ax.set_title(k, fontsize=9)
fig.text(0.02, 0.92, "A  Representational dissimilarity matrices (48 stimuli, 4 categories)", fontsize=10)

bx = fig.add_axes([0.66, 0.16, 0.32, 0.66])
names = ["pixels", "layer 1", "layer 2", "layer 3"]
rho = [spearmanr(rdm[k][iu], rdm["IT (synthetic)"][iu])[0] for k in names]
bx.bar(range(4), rho, color=P.fill("dna"), edgecolor=P.edge("dna"))
bx.set_xticks(range(4))
bx.set_xticklabels(names, fontsize=9)
bx.set_ylim(min(0, min(rho) - 0.05), 1)
bx.axhline(0, color=P.muted(), lw=0.6)
bx.set_ylabel("Spearman correlation with IT RDM")
bx.set_title("B  Deeper stages match the invariant code", loc="left", fontsize=10)
