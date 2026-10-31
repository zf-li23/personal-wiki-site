# Spatial encoding in MRI with a 128 x 128 numerical phantom made of ellipses (a head-like slice: skull,
# brain, ventricles filled with CSF and two small lesions).
# A: the phantom (signal = proton density times the T1/T2 weighting of panel F at TR = 0.5 s, TE = 15 ms).
# B: under a linear gradient G_x the resonance frequency is omega(x) = gamma (B0 + G_x x), so the spectrum of
#    the slice is its projection onto x.
# C: k-space, |S(k_x, k_y)| on a log scale: the signal recorded with k = gamma G t / (2 pi) is the 2D Fourier
#    transform of the image.
# D: inverse FFT of the central 32 x 32 points of k-space only: a blurred image (resolution 1/(2 k_max)).
# E: inverse FFT with every second phase-encoding line omitted: the field of view halves along y and the
#    image folds over (aliasing), the reason for parallel-imaging reconstruction.
# F: spin-echo signal S = rho (1 - exp(-TR/T1)) exp(-TE/T2) at TR = 3 s against TE for white matter
#    (T1 = 0.8 s, T2 = 0.08 s), gray matter (1.3 s, 0.1 s) and CSF (4 s, 2 s) at 1.5 T: T2 weighting at long
#    TE makes CSF bright; (approximate literature values).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
n = 128
yy, xx = np.mgrid[-1:1:n * 1j, -1:1:n * 1j]


def ell(cx, cy, a, b, ang=0.0):
    c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    u = (xx - cx) * c + (yy - cy) * s
    v = -(xx - cx) * s + (yy - cy) * c
    return (u / a) ** 2 + (v / b) ** 2 <= 1


tissue = {"wm": (0.7, 0.8, 0.08), "gm": (0.8, 1.3, 0.10), "csf": (1.0, 4.0, 2.0), "bone": (0.15, 0.3, 0.01)}


def weight(name, TR, TE):
    rho, t1, t2 = tissue[name]
    return rho * (1 - np.exp(-TR / t1)) * np.exp(-TE / t2)


TR, TE = 0.5, 0.015
img = np.zeros((n, n))
img[ell(0, 0, 0.72, 0.9)] = weight("bone", TR, TE)
img[ell(0, 0, 0.66, 0.84)] = weight("gm", TR, TE)
img[ell(0, 0.02, 0.55, 0.72)] = weight("wm", TR, TE)
img[ell(-0.16, 0.1, 0.09, 0.28, 18)] = weight("csf", TR, TE)
img[ell(0.16, 0.1, 0.09, 0.28, -18)] = weight("csf", TR, TE)
img[ell(0.3, -0.42, 0.07, 0.07)] = weight("csf", TR, TE)
img[ell(-0.25, -0.38, 0.05, 0.05)] = 0.9 * weight("gm", TR, TE)

k = np.fft.fftshift(np.fft.fft2(img))
low = np.zeros_like(k)
c = n // 2
low[c - 16:c + 16, c - 16:c + 16] = k[c - 16:c + 16, c - 16:c + 16]
rec_low = np.abs(np.fft.ifft2(np.fft.ifftshift(low)))
und = np.fft.ifftshift(k)[::2, :]
rec_und = np.abs(np.fft.ifft2(und))

fig, axs = plt.subplots(2, 3, figsize=(11.5, 7.6))
gray = plt.get_cmap("gray")
for ax, data, title in ((axs[0, 0], img, "A   Phantom (T₁-weighted)"),
                        (axs[1, 0], rec_low, "D   Central 32 × 32 of k-space"),
                        (axs[1, 1], rec_und, "E   Every second kᵧ line: aliasing")):
    ax.imshow(data, cmap=gray, origin="lower", extent=(-1, 1, -1, 1) if data.shape[0] == n else (-1, 1, -0.5, 0.5),
              aspect="equal")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, title)
ax = axs[1, 1]
ax.set_ylim(-1, 1)

ax = axs[0, 1]
proj = img.sum(axis=0)
x = np.linspace(-1, 1, n)
ax.plot(x, proj / proj.max(), color=charts.line("protein"), lw=1.6)
ax.fill_between(x, proj / proj.max(), color=P.light("protein"), lw=0)
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.1)
charts.style_axes(ax, "x  ∝  frequency offset γGₓx / 2π", "signal")
charts.title(ax, "B   Spectrum under a gradient = projection")

ax = axs[0, 2]
ax.imshow(np.log10(np.abs(k) + 1e-3), cmap=plt.get_cmap("viridis"), origin="lower", extent=(-1, 1, -1, 1))
ax.set_xlabel("kₓ", fontsize=8, color=P.ink())
ax.set_ylabel("kᵧ", fontsize=8, color=P.ink())
ax.set_xticks([])
ax.set_yticks([])
charts.title(ax, "C   k-space, log |S(k)|")

ax = axs[1, 2]
te = np.linspace(0, 0.3, 300)
for name, tok, lab in (("wm", "protein", "white matter"), ("gm", "enzyme", "gray matter"), ("csf", "dna", "CSF")):
    ax.plot(te * 1e3, [weight(name, 3.0, t) for t in te], color=charts.line(tok), lw=1.8, label=lab)
ax.axvline(15, color=P.muted(), lw=0.6, ls=":")
ax.axvline(100, color=P.muted(), lw=0.6, ls=":")
ax.text(18, 0.95, "short TE", fontsize=7.5, color=P.muted())
ax.text(103, 0.95, "T₂-weighted", fontsize=7.5, color=P.muted())
ax.set_xlim(0, 300)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.88))
charts.style_axes(ax, "echo time TE / ms", "signal (TR = 3 s)")
charts.title(ax, "F   Contrast from T₁ and T₂")
fig.tight_layout()
