"""Rank-k PCA reconstruction of a synthetic grayscale image (rows as observations, columns as variables)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
h, w = 120, 160
yy, xx = np.mgrid[0:h, 0:w]
img = 0.3 + 0.2 * np.sin(xx / 9.0) * np.cos(yy / 13.0)
img += 0.5 * (((xx - 50) ** 2 + (yy - 60) ** 2) < 28 ** 2)            # disk
img += 0.4 * ((np.abs(xx - 115) < 25) & (np.abs(yy - 45) < 18))       # rectangle
img += 0.35 * ((yy > 80) & (xx > 95) & (yy - 80 < (xx - 95) * 0.6))    # triangle
img += 0.05 * rng.standard_normal((h, w))

mean = img.mean(0)
Xc = img - mean
U, d, Vt = np.linalg.svd(Xc, full_matrices=False)
var = d ** 2
cum = np.cumsum(var) / var.sum()

fig = plt.figure(figsize=(13, 5.6))
ks = [1, 5, 20]
for i, k in enumerate(ks):
    ax = fig.add_subplot(2, 4, i + 1)
    rec = mean + (U[:, :k] * d[:k]) @ Vt[:k]
    ax.imshow(rec, cmap="gray", vmin=img.min(), vmax=img.max())
    ax.set_title(f"k = {k} ({100 * cum[k - 1]:.0f}% of variance)")
    ax.axis("off")
ax = fig.add_subplot(2, 4, 4)
ax.imshow(img, cmap="gray", vmin=img.min(), vmax=img.max())
ax.set_title("original")
ax.axis("off")
ax = fig.add_subplot(2, 1, 2)
ax.plot(np.arange(1, 61), cum[:60], "o-", ms=3, color="C0")
ax.set_xlabel("number of principal components k")
ax.set_ylabel("cumulative proportion")
ax.set_ylim(0, 1.02)
ax.grid(alpha=0.3)
fig.tight_layout()
