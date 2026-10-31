# Localization precision of single emitters (simulation).
# Camera pixels a = 100 nm, Gaussian PSF sigma s = 130 nm, background b = 4 photons per pixel (Poisson),
# 13 x 13 pixel regions; N = 100 to 10^4 detected photons, 400 spots per N, emitter placed at random within
# the central pixel. Positions are estimated by (i) maximum likelihood with the pixel-integrated Gaussian model
# (Newton iterations, N, s and b known) and (ii) the background-blind centroid.
# A: one simulated spot with N = 500. B: localizations of 400 such spots of an emitter at the origin.
# C: standard deviation of the estimate against N, with the photon-limited bound s/sqrt(N), the
#    Thompson-Larson-Webb formula and the Mortensen maximum-likelihood formula; the MLE follows the bound,
#    the centroid is biased towards the region center by the background.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
a, s, b, npx = 100.0, 130.0, 4.0, 13
edges = (np.arange(npx + 1) - npx / 2) * a


def model(x0, y0, N):
    # pixel-integrated Gaussian, arrays of shape (M, npx, npx)
    ex = 0.5 * (erf((edges[None, 1:] - x0[:, None]) / (np.sqrt(2) * s)) - erf((edges[None, :-1] - x0[:, None]) / (np.sqrt(2) * s)))
    ey = 0.5 * (erf((edges[None, 1:] - y0[:, None]) / (np.sqrt(2) * s)) - erf((edges[None, :-1] - y0[:, None]) / (np.sqrt(2) * s)))
    return N * ey[:, :, None] * ex[:, None, :] + b


def mle(img, N, x0, y0, iters=12, h=0.5):
    x, y = x0.copy(), y0.copy()
    for _ in range(iters):
        def ll(xx, yy):
            mu = model(xx, yy, N)
            return np.sum(img * np.log(mu) - mu, axis=(1, 2))
        f0 = ll(x, y)
        gx = (ll(x + h, y) - ll(x - h, y)) / (2 * h)
        gy = (ll(x, y + h) - ll(x, y - h)) / (2 * h)
        hxx = (ll(x + h, y) - 2 * f0 + ll(x - h, y)) / h**2
        hyy = (ll(x, y + h) - 2 * f0 + ll(x, y - h)) / h**2
        x = x - np.clip(gx / np.minimum(hxx, -1e-9), -50, 50)
        y = y - np.clip(gy / np.minimum(hyy, -1e-9), -50, 50)
    return x, y


cent = 0.5 * (edges[1:] + edges[:-1])
Ns = np.array([100, 200, 500, 1000, 2000, 5000, 10000])
M = 400
sd_mle, sd_cen = [], []
for N in Ns:
    xt = rng.uniform(-a / 2, a / 2, M)
    yt = rng.uniform(-a / 2, a / 2, M)
    img = rng.poisson(model(xt, yt, N))
    tot = img.sum(axis=(1, 2))
    cx = (img.sum(axis=1) * cent).sum(1) / tot
    cy = (img.sum(axis=2) * cent).sum(1) / tot
    x, y = mle(img, N, cx, cy)
    sd_mle.append(np.sqrt(0.5 * (np.var(x - xt) + np.var(y - yt))))
    sd_cen.append(np.sqrt(0.5 * (np.mean((cx - xt) ** 2) + np.mean((cy - yt) ** 2))))
    if N == 500:
        example = img[0]
        x500, y500 = mle(rng.poisson(model(np.zeros(M), np.zeros(M), N)), N, np.zeros(M), np.zeros(M))

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1, 1, 1.25]})
ax = axs[0]
ax.imshow(example, cmap="gray_r", extent=(edges[0], edges[-1], edges[0], edges[-1]), origin="lower")
ax.set_xticks([-500, 0, 500])
ax.set_yticks([-500, 0, 500])
charts.style_axes(ax, "x / nm", "y / nm")
charts.title(ax, "A   One spot, N = 500, b = 4")
ax = axs[1]
ax.plot(x500, y500, ".", ms=3, color=charts.line("dna"))
th = np.linspace(0, 2 * np.pi, 100)
sig = np.std(x500)
ax.plot(2 * sig * np.cos(th), 2 * sig * np.sin(th), color=charts.line("negative"), lw=1.0)
ax.set_aspect("equal")
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.text(-37, 33, f"σ = {sig:.1f} nm", fontsize=8, color=P.ink())
charts.style_axes(ax, "x / nm", "y / nm")
charts.title(ax, "B   400 localizations (MLE)")
ax = axs[2]
NN = np.logspace(2, 4, 100)
sa2 = s**2 + a**2 / 12
ax.loglog(NN, s / np.sqrt(NN), color=P.muted(), lw=1.0, ls=":", label="s/√N (no pixels, no background)")
ax.loglog(NN, np.sqrt(sa2 / NN + 8 * np.pi * s**4 * b / (a**2 * NN**2)), color=charts.line("protein"), lw=1.2,
          ls="--", label="Thompson et al. (2002)")
tau = 2 * np.pi * sa2 * b / (NN * a**2)
ax.loglog(NN, np.sqrt(sa2 / NN * (1 + 4 * tau + np.sqrt(2 * tau / (1 + 4 * tau)))), color=charts.line("negative"),
          lw=1.4, label="Mortensen et al. (2010), MLE")
ax.loglog(Ns, sd_mle, "o", color=charts.line("dna"), ms=5, label="simulation, MLE")
ax.loglog(Ns, sd_cen, "s", color=charts.line("rna"), ms=4, mfc="none", label="simulation, centroid")
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "detected photons N", "localization error / nm")
charts.title(ax, "C   Precision approaches the Cramér-Rao bound")
fig.tight_layout()
