# The projection-slice theorem, checked numerically, and reconstruction from projections.
# A: a two-dimensional test object f(x, y) (128 x 128 pixels: ellipses of different density, a stand-in
#    for a macromolecule) and the direction of one projection (theta = 30 degrees).
# B: the projection p_theta(s), the line integral of f along that direction (the Radon transform).
# C: the one-dimensional Fourier transform of p_theta (line) and the values of the two-dimensional Fourier
#    transform of f along the central line at the same angle (dots, by bilinear interpolation): they agree,
#    as the theorem states. Real parts are shown.
# D-F: filtered back-projection (ramp filter |k|, back-projection over all angles) from 8, 24 and 120
#    equally spaced projections over 180 degrees. With too few views the Fourier plane is under-sampled
#    at high frequency and streaks appear; the Crowther criterion for this object (diameter D = 100 px,
#    resolution d = 2 px) asks for about pi D / d = 157 views.
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import map_coordinates

import wikibio as bio
from wikibio import charts

P = bio.P
n = 128
yy, xx = (np.mgrid[0:n, 0:n] - n / 2 + 0.5) / (n / 2)


def ellipse(x0, y0, a, b, ang, val):
    c, s = np.cos(ang), np.sin(ang)
    u = (xx - x0) * c + (yy - y0) * s
    v = -(xx - x0) * s + (yy - y0) * c
    return val * ((u / a) ** 2 + (v / b) ** 2 <= 1)


f = (ellipse(0, 0, 0.72, 0.55, 0.3, 1.0) + ellipse(0.25, 0.1, 0.18, 0.28, 0.0, 0.8)
     + ellipse(-0.3, -0.1, 0.22, 0.12, 0.8, -0.5) + ellipse(0.05, -0.35, 0.08, 0.08, 0, 1.2)
     + ellipse(-0.15, 0.32, 0.1, 0.05, -0.5, 1.0))


def axes_of(deg):
    t = np.deg2rad(deg)
    d = np.array([np.sin(t), np.cos(t)])      # integration (beam) direction in (x, y)
    e = np.array([np.cos(t), -np.sin(t)])     # detector coordinate s
    return d, e


def project(img, deg):
    """Line integrals of img along direction d, sampled at detector positions s (pixels)."""
    d, e = axes_of(deg)
    sv = np.arange(n) - n / 2 + 0.5
    tv = np.arange(n) - n / 2 + 0.5
    S, T = np.meshgrid(sv, tv, indexing="ij")
    X = S * e[0] + T * d[0] + n / 2 - 0.5
    Y = S * e[1] + T * d[1] + n / 2 - 0.5
    return map_coordinates(img, [Y, X], order=1, cval=0.0).sum(axis=1)


theta = 30.0
p = project(f, theta)
s = np.arange(n) - n / 2 + 0.5

fig, axs = plt.subplots(2, 3, figsize=(12, 7.6))
ax = axs[0, 0]
ax.imshow(f, cmap="gray", origin="lower", extent=(-1, 1, -1, 1))
d, e = axes_of(theta)
for off in np.linspace(-0.8, 0.8, 7):
    perp = e * off
    ax.plot([perp[0] - 1.2 * d[0], perp[0] + 1.2 * d[0]], [perp[1] - 1.2 * d[1], perp[1] + 1.2 * d[1]],
            color=charts.line("highlight"), lw=0.7, alpha=0.8)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
charts.title(ax, "A   Object f(x, y) and rays at θ = 30°")

ax = axs[0, 1]
ax.plot(s, p, color=charts.line("protein"), lw=1.6)
charts.style_axes(ax, "s / pixel", "p_θ(s)")
charts.title(ax, "B   Projection (Radon transform)")

ax = axs[0, 2]
P1 = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(p)))
F2 = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(f)))
kk = np.arange(n) - n / 2
# the central line runs along e, perpendicular to the integration direction
kx = kk * e[0]
ky = kk * e[1]
vals = map_coordinates(F2.real, [ky + n / 2, kx + n / 2], order=1) + 1j * map_coordinates(
    F2.imag, [ky + n / 2, kx + n / 2], order=1)
sel = slice(n // 2 - 24, n // 2 + 25)
ax.plot(kk[sel] / n, P1.real[sel], color=charts.line("protein"), lw=1.5, label="1D FT of projection")
ax.plot(kk[sel][::2] / n, vals.real[sel][::2], "o", color=charts.line("negative"), ms=3.5,
        label="central line of 2D FT")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "k / pixel⁻¹", "Re F")
charts.title(ax, "C   Projection–slice theorem")

ramp = np.abs(np.fft.fftfreq(n))
for ax, nv in zip(axs[1], (8, 24, 120)):
    angs = np.arange(nv) * 180.0 / nv
    rec = np.zeros((n, n))
    X0, Y0 = xx * n / 2, yy * n / 2
    for a in angs:
        q = np.real(np.fft.ifft(np.fft.fft(project(f, a)) * ramp))
        _, ea = axes_of(a)
        sx = X0 * ea[0] + Y0 * ea[1] + n / 2 - 0.5
        rec += np.interp(sx, np.arange(n), q, left=0, right=0)
    ax.imshow(rec, cmap="gray", origin="lower", extent=(-1, 1, -1, 1),
              vmin=np.percentile(rec, 1), vmax=np.percentile(rec, 99.5))
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, f"{'DEF'[[8, 24, 120].index(nv)]}   Filtered back-projection, {nv} views")
fig.tight_layout()
