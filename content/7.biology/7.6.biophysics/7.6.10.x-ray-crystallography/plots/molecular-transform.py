# The diffraction pattern of a crystal samples the transform of one molecule at the reciprocal lattice.
# A two-dimensional "molecule" of seven Gaussian atoms (sigma 0.8 A) is placed alone (A) or at the
# points of a 9 x 9 patch of an oblique lattice, a = 24 A, b = 22.2 A, gamma = 71 deg (C); the
# occupancy of the lattice points is tapered towards the edges, which removes the side lobes of a sharply
# bounded patch. Intensities |F(s)|^2 are computed with a fast Fourier transform on a 1024 x 1024 grid
# of 0.3 A pixels and shown on a logarithmic scale up to |s| = 0.25 A^-1 (d = 4 A).
# B: the continuous molecular transform. D: the crystal transform. It vanishes except near the points of
#    the reciprocal lattice, and the spot intensities follow the molecular transform of B: lattice and
#    motif enter as a product (convolution theorem). The finite size of the patch gives every spot a
#    width of the order of 1/(N a).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink = P.ink()

n, px = 1024, 0.3
L = n * px
x = (np.arange(n) - n // 2) * px
X, Y = np.meshgrid(x, x, indexing="xy")

atoms = 1.6 * np.array([[0.0, 0.0], [1.4, 0.4], [2.2, -0.7], [1.5, -1.9], [3.6, -0.5], [4.3, 0.7],
                        [-1.0, 1.1]])
atoms -= atoms.mean(axis=0)
weights = np.array([1, 1, 1, 1.3, 1, 1.3, 1])
sig = 0.8

rho1 = np.zeros_like(X)
for (ax_, ay_), w in zip(atoms, weights):
    rho1 += w * np.exp(-((X - ax_) ** 2 + (Y - ay_) ** 2) / (2 * sig**2))

# lattice of delta functions (rounded to pixels) with a smooth taper that suppresses the side lobes of
# the finite crystal; the crystal is their convolution with the molecule
a = np.array([80, 0]) * px          # lattice vectors are whole numbers of pixels: 24 A and
b = np.array([24, 70]) * px         # 22.2 A at 71 deg
lat = np.zeros_like(X)
nc = 9
for i in range(nc):
    for j in range(nc):
        r = (i - (nc - 1) / 2) * a + (j - (nc - 1) / 2) * b
        u, v = np.rint(r / px).astype(int) + n // 2
        taper = np.exp(-((i - (nc - 1) / 2) ** 2 + (j - (nc - 1) / 2) ** 2) / (2 * 2.5**2))
        lat[v, u] += taper
ft = np.fft.fft2
rhoc = np.real(np.fft.ifft2(ft(np.fft.ifftshift(rho1)) * ft(lat)))


def intensity(rho):
    F = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(rho)))
    return np.abs(F) ** 2


s = np.fft.fftshift(np.fft.fftfreq(n, d=px))
smax = 0.25
k = np.abs(s) <= smax
I1 = intensity(rho1)[np.ix_(k, k)]
Ic = intensity(rhoc)[np.ix_(k, k)]
ext_s = (s[k][0], s[k][-1], s[k][0], s[k][-1])

fig, axs = plt.subplots(1, 4, figsize=(14, 3.9))
cm_r = "Blues"
cm_f = "magma"

ax = axs[0]
w = 12.0
m = np.abs(x) <= w
ax.imshow(np.ma.masked_less(rho1[np.ix_(m, m)], 0.03), origin="lower", extent=(x[m][0], x[m][-1], x[m][0], x[m][-1]), interpolation="bilinear", cmap=cm_r, vmin=-0.4)
ax.set_title("A  one molecule", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "x / Å", "y / Å", box=True)

ax = axs[1]
ax.imshow(np.log10(I1 / I1.max() + 1e-6), origin="lower", extent=ext_s, cmap=cm_f, vmin=-4, vmax=0)
ax.set_title("B  molecular transform", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"$s_x$ / Å$^{-1}$", r"$s_y$ / Å$^{-1}$", box=True)

ax = axs[2]
w = 100.0
m = np.abs(x) <= w
ax.imshow(np.ma.masked_less(rhoc[np.ix_(m, m)], 0.03), origin="lower", extent=(x[m][0], x[m][-1], x[m][0], x[m][-1]), interpolation="bilinear", cmap=cm_r, vmin=-0.4)
ax.set_title("C  9 × 9 crystal", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "x / Å", "y / Å", box=True)

ax = axs[3]
ax.imshow(np.log10(Ic / Ic.max() + 1e-6), origin="lower", extent=ext_s, cmap=cm_f, vmin=-4, vmax=0)
ax.set_title("D  crystal transform", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"$s_x$ / Å$^{-1}$", None, box=True)

fig.tight_layout()
