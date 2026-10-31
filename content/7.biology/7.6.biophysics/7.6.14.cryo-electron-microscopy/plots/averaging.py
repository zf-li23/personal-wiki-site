# Signal-to-noise ratio and averaging in single-particle analysis.
# Top row: a projection of the toy complex (64 x 64 pixels) buried in white Gaussian noise with a
# per-pixel SNR of 0.05 (signal variance / noise variance, a typical value for a single particle), and
# averages of N = 10, 100 and 1000 such images with known alignment; the noise falls as 1/sqrt(N).
# Top right: the measured SNR of the average against N (dots) and the expectation 0.05 N (line).
# Bottom row ("Einstein from noise"): 2000 images of pure noise, each shifted to the position of maximum
# cross-correlation with a reference (computed with the FFT), then averaged. The average reproduces the
# reference although no particle was ever imaged: alignment to a reference imposes it on the data.
# Independent half-sets, references from the data themselves and checking that the result does not
# depend on the starting model guard against this reference bias.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 64
y, x = np.mgrid[0:n, 0:n] - n / 2 + 0.5
img = np.exp(-(x**2 + y**2) / (2 * 4.0**2)) * 1.2
for j in range(7):
    a = 2 * np.pi * j / 7 + 0.2
    img += np.exp(-((x - 16 * np.cos(a)) ** 2 + (y - 16 * np.sin(a)) ** 2) / (2 * 4.0**2))
img += 0.7 * np.exp(-((x - 9) ** 2 + (y - 6) ** 2) / (2 * 3.0**2))
img -= img.mean()
img /= img.std()
snr1 = 0.05
sd = 1 / np.sqrt(snr1)


def noisy(m):
    return img[None] + sd * rng.standard_normal((m, n, n))


fig = plt.figure(figsize=(13, 6.3))
gs = fig.add_gridspec(2, 5)
stack = noisy(1000)
for i, N in enumerate((1, 10, 100, 1000)):
    ax = fig.add_subplot(gs[0, i])
    av = stack[:N].mean(axis=0)
    ax.imshow(av, cmap="gray", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, "single image" if N == 1 else f"average of {N}")
ax = fig.add_subplot(gs[0, 4])
Ns = np.unique(np.logspace(0, 3, 12).astype(int))
meas = []
for N in Ns:
    av = stack[:N].mean(axis=0)
    meas.append(img.var() / (av - img).var())
ax.loglog(Ns, snr1 * Ns, color=charts.line("protein"), lw=1.5, label="SNR = 0.05 N")
ax.loglog(Ns, meas, "o", color=charts.line("negative"), ms=4, label="measured")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "number averaged N", "SNR of average")
charts.title(ax, "SNR grows as N")

ref = img
ax = fig.add_subplot(gs[1, 0])
ax.imshow(ref, cmap="gray", origin="lower")
ax.set_xticks([])
ax.set_yticks([])
charts.title(ax, "reference")
Fr = np.conj(np.fft.fft2(ref))
noise = rng.standard_normal((2000, n, n))
aligned = np.zeros((2000, n, n))
for i in range(2000):
    cc = np.real(np.fft.ifft2(np.fft.fft2(noise[i]) * Fr))
    dy, dx = np.unravel_index(np.argmax(cc), cc.shape)
    aligned[i] = np.roll(np.roll(noise[i], -dy, axis=0), -dx, axis=1)
for i, N in enumerate((1, 100, 2000)):
    ax = fig.add_subplot(gs[1, i + 1])
    ax.imshow(aligned[:N].mean(axis=0), cmap="gray", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.title(ax, "one aligned noise image" if N == 1 else f"average of {N} noise images")
ax = fig.add_subplot(gs[1, 4])
cc = [np.corrcoef(aligned[:N].mean(axis=0).ravel(), ref.ravel())[0, 1] for N in Ns]
ax.semilogx(Ns, cc, "o-", color=charts.line("highlight"), ms=4, lw=1.2)
ax.set_ylim(0, 1)
charts.style_axes(ax, "number of noise images", "correlation with reference")
charts.title(ax, "Einstein from noise")
fig.tight_layout()
