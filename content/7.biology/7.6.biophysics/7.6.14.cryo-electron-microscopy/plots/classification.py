# Two-dimensional classification of a heterogeneous data set by k-means clustering.
# 1200 aligned images (48 x 48 pixels) of a toy complex in two conformations, 60 % in state 1 (a lid
# subunit closed over the ring) and 40 % in state 2 (lid swung out), with white noise at a per-pixel
# SNR of 0.03. Each image is a vector in a 2304-dimensional space; the Euclidean distance between
# normalized images is a monotone function of their cross-correlation.
# A: the two true projections. B: images projected on the first two principal components of the data
#    set, coloured by the (unknown) true state; the states form two overlapping clouds.
# C: class averages from k-means with K = 2 (k-means++ initialization, 30 iterations) applied to the
#    coordinates on the first ten principal components, which discards most of the noise; the numbers
#    give the fraction of the images in each class that truly belong to its majority state.
# D: the average of all images, a blurred mixture: averaging without classification destroys the
#    features that differ between the states.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)
n = 48
y, x = np.mgrid[0:n, 0:n] - n / 2 + 0.5


def blob(cx, cy, s=3.0, w=1.0):
    return w * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * s**2))


ring = blob(0, 0, 3.5, 1.2) + sum(blob(12 * np.cos(2 * np.pi * j / 6), 12 * np.sin(2 * np.pi * j / 6))
                                  for j in range(6))
states = [ring + blob(6, 4, 3.0, 1.0), ring + blob(19, 12, 3.0, 1.0)]
states = [(s - s.mean()) / s.std() for s in states]
M = 1200
truth = (rng.random(M) < 0.4).astype(int)
data = np.array([states[t] for t in truth]) + rng.standard_normal((M, n, n)) / np.sqrt(0.03)
V = data.reshape(M, -1)
V = (V - V.mean(axis=1, keepdims=True)) / V.std(axis=1, keepdims=True)


def kmeans(V, K, iters=30):
    c = [V[rng.integers(len(V))]]
    for _ in range(K - 1):
        d2 = np.min([((V - cc) ** 2).sum(1) for cc in c], axis=0) + 1e-12
        c.append(V[rng.choice(len(V), p=d2 / d2.sum())])
    c = np.array(c)
    for _ in range(iters):
        lab = np.argmin((c**2).sum(1)[None] - 2 * V @ c.T, axis=1)
        c = np.array([V[lab == k].mean(0) for k in range(K)])
    return lab, c


Vc = V - V.mean(0)
w, Ev = np.linalg.eigh(Vc @ Vc.T)
pcs = Ev[:, -10:][:, ::-1] * np.sqrt(np.abs(w[-10:][::-1]))     # first ten principal components
pc = pcs[:, :2]
lab, _ = kmeans(pcs, 2)
cent = np.array([V[lab == k].mean(0) for k in range(2)])

fig = plt.figure(figsize=(13, 3.8))
gs = fig.add_gridspec(1, 6, width_ratios=[1, 1, 1.9, 1, 1, 1])
for i in range(2):
    ax = fig.add_subplot(gs[0, i])
    ax.imshow(states[i], cmap="gray", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, f"A   state {i + 1}" if i == 0 else "state 2")
ax = fig.add_subplot(gs[0, 2])
for t, tok in ((0, "dna"), (1, "negative")):
    ax.plot(pc[truth == t, 0], pc[truth == t, 1], ".", ms=2.5, color=charts.line(tok),
            label=f"true state {t + 1}")
ax.legend(fontsize=7, frameon=False, markerscale=3)
charts.style_axes(ax, "PC 1", "PC 2")
charts.title(ax, "B   Images in principal-component space")
for k in range(2):
    ax = fig.add_subplot(gs[0, 3 + k])
    members = truth[lab == k]
    major = np.bincount(members, minlength=2).argmax()
    purity = (members == major).mean()
    ax.imshow(cent[k].reshape(n, n), cmap="gray", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, f"{'C   ' if k == 0 else ''}class {k + 1}: {len(members)} im., {purity:.0%}")
ax = fig.add_subplot(gs[0, 5])
ax.imshow(V.mean(0).reshape(n, n), cmap="gray", origin="lower")
ax.set_xticks([])
ax.set_yticks([])
charts.title(ax, "D   average of all")
fig.tight_layout()
