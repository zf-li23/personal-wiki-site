# The effect of grain on measured landscape pattern. A 256 x 256 fractal neutral landscape (H = 0.5,
# 35% habitat) with fine-scale noise is aggregated to coarser grains by majority rule (a coarse cell is
# habitat if more than half of its fine cells are). A-C: the map at grains of 1, 4 and 16 cells.
# D: habitat proportion, number of patches and edge density (cell edges per unit area, in units of the
# finest grain) against grain, all relative to the finest grain.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy import ndimage
import wikibio as bio

P = bio.P
rng = np.random.default_rng(11)
n = 256
kx = np.fft.fftfreq(n)[:, None]
ky = np.fft.fftfreq(n)[None, :]
f = np.sqrt(kx ** 2 + ky ** 2)
f[0, 0] = 1
amp = f ** -1.5
amp[0, 0] = 0
z = np.fft.ifft2(amp * np.exp(2j * np.pi * rng.random((n, n)))).real
z = (z - z.mean()) / z.std() + 0.6 * rng.normal(size=(n, n))
m = z > np.quantile(z, 0.65)

def coarsen(m, g):
    k = m.reshape(n // g, g, n // g, g).mean(axis=(1, 3))
    return k > 0.5

grains = [1, 2, 4, 8, 16, 32]
stats = []
for g in grains:
    c = coarsen(m, g)
    _, npch = ndimage.label(c)
    e = (np.sum(c[:, 1:] != c[:, :-1]) + np.sum(c[1:, :] != c[:-1, :])) * g    # edge length in fine units
    stats.append((c.mean(), npch, e / n ** 2))
stats = np.array(stats)

cmap = ListedColormap([P.light("bone"), P.fill("plant")])
fig = plt.figure(figsize=(13.0, 3.9))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.5])
for k, g in enumerate((1, 4, 16)):
    ax = fig.add_subplot(gs[k])
    ax.imshow(coarsen(m, g), cmap=cmap, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{'ABC'[k]}  grain {g} × {g}", loc="left", fontweight="bold", fontsize=10)
ax = fig.add_subplot(gs[3])
for j, (lab, tok) in enumerate((("habitat proportion", "plant"), ("number of patches", "negative"),
                               ("edge density", "dna"))):
    ax.plot(grains, stats[:, j] / stats[0, j], "o-", color=P.fill(tok), lw=1.8, ms=4, label=lab)
ax.set_xscale("log", base=2)
ax.set_yscale("log")
ax.set_xticks(grains, [str(g) for g in grains])
ax.set_xlabel("Grain (cells of the finest map)")
ax.set_ylabel("Value relative to finest grain")
ax.legend(frameon=False, fontsize=7.5, loc="lower left")
ax.set_title("D  Metrics against grain", loc="left", fontweight="bold")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
