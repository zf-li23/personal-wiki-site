"""Hand-designed filters applied to a synthetic grayscale image (a square, a
disk and a diagonal bar with mild noise): a 5x5 Gaussian blur, the horizontal
and vertical Sobel filters, and the gradient magnitude. A convolutional layer
learns filters of this kind from data."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d

rng = np.random.default_rng(0)
n = 96
yy, xx = np.mgrid[0:n, 0:n]
img = np.zeros((n, n))
img[15:45, 12:42] = 1.0
img[(xx - 66) ** 2 + (yy - 30) ** 2 < 15 ** 2] = 0.7
bar = (np.abs(xx + yy - 130) < 5) & (yy > 55)
img[bar] = 0.9
img += 0.05 * rng.standard_normal(img.shape)

t = np.arange(-2, 3)
g = np.exp(-t ** 2 / 2.0)
gauss = np.outer(g, g) / np.outer(g, g).sum()
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
sobel_y = sobel_x.T

blur = correlate2d(img, gauss, mode="same", boundary="symm")
gx = correlate2d(img, sobel_x, mode="same", boundary="symm")
gy = correlate2d(img, sobel_y, mode="same", boundary="symm")
panels = [
    (img, "input image", "gray"),
    (blur, "Gaussian blur 5x5", "gray"),
    (gx, "Sobel x (vertical edges)", "RdBu_r"),
    (gy, "Sobel y (horizontal edges)", "RdBu_r"),
    (np.hypot(gx, gy), "gradient magnitude", "magma"),
]
fig, axes = plt.subplots(1, 5, figsize=(15, 3.3))
for ax, (a, title, cmap) in zip(axes, panels):
    if cmap == "RdBu_r":
        v = np.abs(a).max()
        ax.imshow(a, cmap=cmap, vmin=-v, vmax=v)
    else:
        ax.imshow(a, cmap=cmap)
    ax.set_title(title, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
