# Neutral landscape models (Gardner et al. 1987; With 1997) and landscape metrics.
# Three 128 x 128 maps with the same proportion of habitat (p = 0.4): a simple random map and two
# fractal maps made by spectral synthesis (power spectrum ~ f^-(2H+2)) with Hurst exponents H = 0.2 and
# 0.8, thresholded at the 60th percentile. Patches are 4-connected groups of habitat cells.
# Metrics: number of patches NP, largest patch index LPI (% of the map), edge density ED (habitat /
# non-habitat cell edges per cell), landscape shape index LSI = E / (4 sqrt(A)) of the habitat class,
# and contagion (%), computed from the 4-neighbour adjacency of the two classes.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy import ndimage
import wikibio as bio

P = bio.P
n, p = 128, 0.4
rng = np.random.default_rng(3)

def fractal(H):
    kx = np.fft.fftfreq(n)[:, None]
    ky = np.fft.fftfreq(n)[None, :]
    f = np.sqrt(kx ** 2 + ky ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    z = np.fft.ifft2(amp * np.exp(2j * np.pi * rng.random((n, n)))).real
    return z

def classify(z):
    return z > np.quantile(z, 1 - p)

maps = [("Random", rng.random((n, n)) < p), ("Fractal, H = 0.2", classify(fractal(0.2))),
        ("Fractal, H = 0.8", classify(fractal(0.8)))]

def metrics(m):
    lab, npatch = ndimage.label(m)
    sizes = np.bincount(lab.ravel())[1:]
    e = np.sum(m[:, 1:] != m[:, :-1]) + np.sum(m[1:, :] != m[:-1, :])
    lsi = (e + 2 * (m[0, :].sum() + m[-1, :].sum() + m[:, 0].sum() + m[:, -1].sum())) / (4 * np.sqrt(m.sum()))
    pairs = np.zeros((2, 2))
    for a, b in ((m[:, 1:], m[:, :-1]), (m[1:, :], m[:-1, :])):
        for i in (0, 1):
            for j in (0, 1):
                pairs[i, j] += np.sum((a == i) & (b == j)) + np.sum((b == i) & (a == j))
    q = pairs / pairs.sum()
    nz = q[q > 0]
    contag = 100 * (1 + np.sum(nz * np.log(nz)) / (2 * np.log(2)))
    return npatch, 100 * sizes.max() / m.size, e / m.size, lsi, contag

cmap = ListedColormap([P.light("bone"), P.fill("plant")])
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.9))
for ax, (name, m) in zip(axes, maps):
    ax.imshow(m, cmap=cmap, interpolation="nearest")
    lab, _ = ndimage.label(m)
    sizes = np.bincount(lab.ravel())
    sizes[0] = 0
    ax.contour(lab == sizes.argmax(), levels=[0.5], colors=[P.edge("negative")], linewidths=0.8)
    npatch, lpi, ed, lsi, cg = metrics(m)
    ax.set_title(name, fontsize=10, fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0.5, -0.04, f"NP {npatch}   LPI {lpi:.1f}%   ED {ed:.2f}\nLSI {lsi:.1f}   contagion {cg:.0f}%",
            transform=ax.transAxes, ha="center", va="top", fontsize=8.5, color=P.ink())
fig.text(0.5, 0.01, "Habitat (green) 40% in each map; red outline: the largest patch", ha="center", fontsize=8,
         color=P.muted())
fig.tight_layout(rect=(0, 0.06, 1, 1))
