# What resolution means: Fourier syntheses of the same structure truncated at d_min.
# A planar tyrosine-like fragment (a six-membered ring of C atoms 1.39 A apart, a C-beta, a hydroxyl O and
# two backbone atoms) in a two-dimensional periodic cell of 16 x 16 A. Structure factors are computed
# from point atoms with weight Z (C 6, N 7, O 8), a Gaussian atomic form factor exp(-b s^2) with
# b = 1.0 A^2, and an isotropic temperature factor exp(-B s^2 / 4) with B = 8 A^2. The electron density
# is the Fourier synthesis rho(x) = (1/A) sum F(h) exp(-2 pi i h.x) over all reflections with
# |s| = 1/d <= 1/d_min, for d_min = 3.5, 2.5, 1.5 and 1.0 A. Grey circles mark the true atom positions.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

cell = 16.0
ang = np.deg2rad(np.arange(6) * 60 + 90)
ring = [(1.39 * np.cos(t), 1.39 * np.sin(t)) for t in ang]
atoms = [(xx, yy, 6) for xx, yy in ring]
atoms += [(0.0, 1.39 + 1.51, 6), (0.0, -1.39 - 1.36, 8)]          # C-beta, O-eta
atoms += [(1.30, 1.39 + 1.51 + 0.75, 6), (1.30, 1.39 + 1.51 + 2.2, 7)]   # C-alpha, N
xyz = np.array([(a[0], a[1]) for a in atoms])
Z = np.array([a[2] for a in atoms], float)
frac = xyz / cell

hmax = 17
hh = np.arange(-hmax, hmax + 1)
H, K = np.meshgrid(hh, hh, indexing="ij")
s2 = (H**2 + K**2) / cell**2
F = np.zeros(H.shape, complex)
for (fx, fy), z in zip(frac, Z):
    F += z * np.exp(2j * np.pi * (H * fx + K * fy))
F *= np.exp(-1.0 * s2) * np.exp(-8.0 / 4 * s2)

ng = 160
g = (np.arange(ng) / ng - 0.5) * cell
GX, GY = np.meshgrid(g, g, indexing="xy")
phase_x = np.exp(-2j * np.pi * np.outer(hh, g / cell))         # (h, x)


def synth(dmin):
    Fm = np.where(s2 <= 1 / dmin**2, F, 0)
    # rho(x, y) = sum_h sum_k F(h,k) e^{-2 pi i (h x + k y)}
    rho = np.real(phase_x.T @ Fm @ phase_x)        # (x, h) (h, k) (k, y) -> (x, y)
    return rho.T / cell**2


fig, axs = plt.subplots(1, 4, figsize=(13, 3.6))
w = 5.5
m = np.abs(g) <= w + 0.6
ext = (g[m][0], g[m][-1], g[m][0], g[m][-1])
for ax, d in zip(axs, (3.5, 2.5, 1.5, 1.0)):
    rho = synth(d)[np.ix_(m, m)]
    rho /= rho.max()
    ax.contourf(g[m], g[m], rho, levels=np.linspace(0.12, 1, 10), cmap="Blues", vmin=-0.3, vmax=1)
    ax.contour(g[m], g[m], rho, levels=[0.12], colors=[charts.line("dna")], linewidths=0.8)
    ax.plot(xyz[:, 0], xyz[:, 1], "o", ms=4, mfc="none", mec=muted, mew=0.9)
    ax.set_title(rf"$d_{{\min}}$ = {d} Å", fontsize=9, loc="left", color=ink)
    ax.set_xlim(-w, w)
    ax.set_ylim(-w + 0.6, w + 0.6)
    ax.set_aspect("equal")
    charts.style_axes(ax, "x / Å", None, box=True)
axs[0].set_ylabel("y / Å", color=ink, fontsize=8)
fig.tight_layout()
