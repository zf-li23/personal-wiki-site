# Phases carry most of the structural information.
# Two two-dimensional "molecules" made of Gaussian atoms (sigma 0.55 A) in a 32 A periodic box: a
# six-membered ring with a substituent (A) and a zigzag chain (B). Their Fourier coefficients F1, F2 are
# computed by FFT; then the amplitudes of one are combined with the phases of the other and transformed
# back. C: |F1| with the phases of F2. D: |F2| with the phases of F1. Each hybrid map resembles the
# structure that supplied the phases. Negative density in the hybrids is not shown.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink = P.ink()

n, px = 128, 0.25
x = (np.arange(n) - n // 2) * px
X, Y = np.meshgrid(x, x, indexing="xy")


def mol(coords, sig=0.55):
    rho = np.zeros_like(X)
    for cx, cy in coords:
        rho += np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * sig**2))
    return rho


ang = np.deg2rad(np.arange(6) * 60 + 30)
ring = [(1.4 * np.cos(t) - 1.0, 1.4 * np.sin(t)) for t in ang] + [(-1.0 + 2.6, 1.5), (-1.0 + 3.9, 2.1)]
chain = [(-4.2 + 1.25 * i, 0.75 * (-1) ** i - 0.4 * (i == 6)) for i in range(7)] + [(3.3, -1.8)]
r1, r2 = mol(ring), mol(chain)
F1, F2 = np.fft.fft2(r1), np.fft.fft2(r2)
h12 = np.real(np.fft.ifft2(np.abs(F1) * np.exp(1j * np.angle(F2))))
h21 = np.real(np.fft.ifft2(np.abs(F2) * np.exp(1j * np.angle(F1))))

fig, axs = plt.subplots(1, 4, figsize=(13, 3.6))
w = 6.5
m = np.abs(x) <= w
ext = (x[m][0], x[m][-1], x[m][0], x[m][-1])
panels = ((r1, "A  ring: amplitudes and phases"), (r2, "B  chain: amplitudes and phases"),
          (h12, "C  |F| of ring, phases of chain"), (h21, "D  |F| of chain, phases of ring"))
for ax, (img, title) in zip(axs, panels):
    sub = img[np.ix_(m, m)]
    sub = sub / sub.max()
    ax.imshow(np.ma.masked_less(sub, 0.08), origin="lower", extent=ext, interpolation="bilinear", cmap="Blues", vmin=-0.4, vmax=1)
    ax.set_title(title, fontsize=8.5, loc="left", color=ink)
    charts.style_axes(ax, "x / Å", None, box=True)
axs[0].set_ylabel("y / Å", color=ink, fontsize=8)
fig.tight_layout()
