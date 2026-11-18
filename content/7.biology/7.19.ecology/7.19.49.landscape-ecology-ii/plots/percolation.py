"""Site percolation on neutral landscape maps.

Random neutral landscapes (Gardner et al. 1987): each cell of an L x L grid is habitat independently with
probability p. Clusters are sets of habitat cells connected through edge-sharing neighbours (4-neighbour
rule) or through edges and corners (8-neighbour rule); they are labelled with scipy.ndimage.label.
A-C: 160 x 160 maps at p = 0.50, 0.59 and 0.68 (4-neighbour rule); the largest cluster is highlighted.
D: fraction of all habitat that belongs to the largest cluster, and E: probability that some cluster
spans the map from the left to the right edge, against p (L = 128, 60 maps per value). Curves: random maps
with the 4-neighbour rule (threshold p_c = 0.5927 for an infinite lattice) and the 8-neighbour rule
(p_c = 0.4073), and spatially correlated (fractal) maps made by spectral synthesis (Fourier filtering of
white noise with amplitude proportional to f^-(H + 1), H = 0.5) and thresholded at their p-quantile,
4-neighbour rule. Clumped habitat stays connected at lower habitat amounts than random habitat, and the
transition is gradual.
"""

import numpy as np
from matplotlib.colors import ListedColormap
from scipy import ndimage

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
S4 = ndimage.generate_binary_structure(2, 1)
S8 = ndimage.generate_binary_structure(2, 2)


def fractal(L, H):
    fx = np.fft.fftfreq(L)[:, None]
    fy = np.fft.fftfreq(L)[None, :]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    noise = np.fft.fft2(rng.standard_normal((L, L)))
    return np.real(np.fft.ifft2(noise * amp))


def stats(hab, st):
    lab, n = ndimage.label(hab, structure=st)
    if n == 0:
        return 0.0, 0.0
    sizes = np.bincount(lab.ravel())[1:]
    big = sizes.max() / hab.sum()
    left = set(np.unique(lab[:, 0])) - {0}
    right = set(np.unique(lab[:, -1])) - {0}
    return big, float(bool(left & right))


fig, ax = bio.canvas(32.0, 19.0)
cmap = ListedColormap([P.surface(), P.light("plant"), P.edge("plant")])
L0 = 160
for j, p in enumerate((0.50, 0.59, 0.68)):
    hab = rng.random((L0, L0)) < p
    lab, n = ndimage.label(hab, structure=S4)
    sizes = np.bincount(lab.ravel())
    sizes[0] = 0
    img = hab.astype(int)
    img[lab == sizes.argmax()] = 2
    x0 = 1.4 + 10.4 * j
    pa = C.axes_at(ax, (x0, 10.2, 7.6, 7.6))
    pa.imshow(img, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
    pa.set_xticks([])
    pa.set_yticks([])
    for sp in pa.spines.values():
        sp.set_color(P.muted())
    frac = sizes.max() / hab.sum()
    bio.panel(ax, "ABC"[j], (x0 - 1.0, 18.6))
    bio.label(ax, (x0, 18.2), f"p = {p:.2f}: largest cluster {100 * frac:.0f} % of habitat", size="small", bold=True, ha="left")

ps = np.linspace(0.30, 0.80, 26)
L, reps = 128, 60
curves = {"random, 4-neighbour": [], "random, 8-neighbour": [], "fractal, 4-neighbour": []}
for p in ps:
    acc = {k: [] for k in curves}
    for _ in range(reps):
        hab = rng.random((L, L)) < p
        acc["random, 4-neighbour"].append(stats(hab, S4))
        acc["random, 8-neighbour"].append(stats(hab, S8))
        z = fractal(L, 0.5)
        hab = z < np.quantile(z, p)
        acc["fractal, 4-neighbour"].append(stats(hab, S4))
    for k in curves:
        curves[k].append(np.mean(acc[k], axis=0))
toks = {"random, 4-neighbour": "plant", "random, 8-neighbour": "dna", "fractal, 4-neighbour": "negative"}

pd_ = C.axes_at(ax, (2.6, 1.8, 12.0, 6.2))
pe = C.axes_at(ax, (18.6, 1.8, 12.0, 6.2))
for k, v in curves.items():
    v = np.array(v)
    c = Q.line_color(toks[k])
    pd_.plot(ps, v[:, 0], "o-", color=c, ms=3, lw=1.4, label=k)
    pe.plot(ps, v[:, 1], "o-", color=c, ms=3, lw=1.4, label=k)
for a in (pd_, pe):
    for pc, tk in ((0.5927, "plant"), (0.4073, "dna")):
        a.axvline(pc, color=Q.line_color(tk), lw=0.8, ls=(0, (3, 2)))
    a.set_xlim(0.3, 0.8)
    a.set_ylim(-0.02, 1.02)
C.style_axes(pd_, "habitat proportion p", "fraction of habitat in largest cluster")
C.style_axes(pe, "habitat proportion p", "probability of a spanning cluster")
pd_.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
pd_.text(0.598, 0.05, "p_c = 0.593", fontsize=FS["tiny"], color=Q.line_color("plant"))
pd_.text(0.335, 0.45, "p_c = 0.407", fontsize=FS["tiny"], color=Q.line_color("dna"))
bio.panel(ax, "D", (0.8, 8.9))
bio.label(ax, (2.6, 8.6), "Size of the largest cluster", size="small", bold=True, ha="left")
bio.panel(ax, "E", (16.8, 8.9))
bio.label(ax, (18.6, 8.6), "Connection across the map", size="small", bold=True, ha="left")
