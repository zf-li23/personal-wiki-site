# The missing wedge of electron tomography.
# A cross-section (x horizontal, z along the beam at zero tilt, vertical) through a slab of specimen:
# a membrane (two dense lines) and fourteen dense particles of 6 px radius in a 128 x 128 field.
# A: Fourier-space coverage of a tilt series from -60 to +60 degrees in 3-degree steps; each projection
#    fills one central line (projection-slice theorem); the two wedges around the k_z axis are never
#    measured. B: the object. C: filtered back-projection from a full tilt range (-90 to +90 degrees,
#    3-degree steps). D: the same from -60 to +60 degrees: particles are elongated along z (by about
#    1.55 for a 60-degree wedge), horizontal membranes vanish where they run perpendicular to the beam
#    and fringes appear above and below dense objects.
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import map_coordinates

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
n = 128
c0 = np.arange(n) - n / 2 + 0.5
X, Z = np.meshgrid(c0, c0, indexing="xy")
obj = np.zeros((n, n))
obj += 0.8 * (np.abs(Z - 18) < 1.5) * (np.abs(X) < 52)
obj += 0.8 * (np.abs(Z - 10) < 1.5) * (np.abs(X) < 52)
for _ in range(14):
    x0, z0 = rng.uniform(-45, 45), rng.uniform(-45, 0)
    obj += 1.0 * ((X - x0) ** 2 + (Z - z0) ** 2 <= 36)
obj += 0.6 * (np.abs(X + 30) < 1.5) * (np.abs(Z - 35) < 14)       # a vertical (beam-parallel) membrane piece


def axes_of(deg):
    t = np.deg2rad(deg)
    return np.array([np.sin(t), np.cos(t)]), np.array([np.cos(t), -np.sin(t)])


def project(img, deg):
    d, e = axes_of(deg)
    S, T = np.meshgrid(c0, c0, indexing="ij")
    xs = S * e[0] + T * d[0] + n / 2 - 0.5
    zs = S * e[1] + T * d[1] + n / 2 - 0.5
    return map_coordinates(img, [zs, xs], order=1, cval=0.0).sum(axis=1)


ramp = np.abs(np.fft.fftfreq(n))


def fbp(angles):
    rec = np.zeros((n, n))
    for a in angles:
        q = np.real(np.fft.ifft(np.fft.fft(project(obj, a)) * ramp))
        _, e = axes_of(a)
        rec += np.interp(X * e[0] + Z * e[1] + n / 2 - 0.5, np.arange(n), q, left=0, right=0)
    return rec


fig, axs = plt.subplots(1, 4, figsize=(14, 3.9))
ax = axs[0]
for a in np.arange(-60, 61, 3):
    _, e = axes_of(a)
    ax.plot([-e[0], e[0]], [-e[1], e[1]], color=charts.line("dna"), lw=0.7)
for sgn in (1, -1):
    tt = np.deg2rad(np.linspace(60, 120, 30))
    ax.fill(np.r_[0, np.cos(tt)], sgn * np.r_[0, np.sin(tt)], color=P.light("negative"), lw=0)
ax.text(0, 0.82, "missing\nwedge", ha="center", fontsize=7.5, color=P.ink())
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
charts.style_axes(ax, "kx", "kz", box=True)
charts.title(ax, "A   Coverage, ±60° tilts")
recs = [("B   Object (x–z section)", obj), ("C   Tilts −90° to +90°", fbp(np.arange(-90, 90, 3))),
        ("D   Tilts −60° to +60°", fbp(np.arange(-60, 61, 3)))]
for ax, (name, img) in zip(axs[1:], recs):
    ax.imshow(img, cmap="gray", origin="lower", vmin=np.percentile(img, 1), vmax=np.percentile(img, 99.7))
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, "x", "z (beam)", box=True)
    charts.title(ax, name)
fig.tight_layout()
