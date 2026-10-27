# Single-molecule localization microscopy, simulated. Ground truth: fluorophores on two parallel filaments
# 80 nm apart (below the ~200 nm diffraction limit) and on a ring of radius 60 nm.
# A: the widefield image, each emitter blurred by a Gaussian PSF of standard deviation s = 100 nm.
# B: localization: in each frame a few sparse emitters are on; each is localized from N photons with
#    precision sigma_loc = s / sqrt(N) (N drawn from an exponential distribution, mean 1500 photons, so
#    sigma_loc ~ 3 nm at the mean); 20 localizations per fluorophore are rendered as a 2D histogram.
# C: the profile across the two filaments in both images: only the reconstruction separates them.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
s = 100.0

pts = []
for x0 in (-40, 40):
    y = rng.uniform(-400, 400, 160)
    pts.append(np.c_[np.full_like(y, x0) - 250, y])
th = rng.uniform(0, 2 * np.pi, 90)
pts.append(np.c_[250 + 60 * np.cos(th), 60 * np.sin(th)])
pts = np.vstack(pts)

L, n = 600, 240
edges = np.linspace(-L, L, n + 1)
cent = (edges[:-1] + edges[1:]) / 2
X, Y = np.meshgrid(cent, cent)
wide = np.zeros_like(X)
for x, y in pts:
    wide += np.exp(-((X - x) ** 2 + (Y - y) ** 2) / (2 * s**2))

locs = []
for x, y in pts:
    N = rng.exponential(1500, 20) + 200
    sig = s / np.sqrt(N)
    locs.append(np.c_[x + rng.normal(0, 1, 20) * sig, y + rng.normal(0, 1, 20) * sig])
locs = np.vstack(locs)
H, _, _ = np.histogram2d(locs[:, 1], locs[:, 0], bins=[edges, edges])
k = np.exp(-(np.arange(-3, 4) ** 2) / 2.0)
k /= k.sum()
H = np.apply_along_axis(lambda r: np.convolve(r, k, "same"), 0, H)
H = np.apply_along_axis(lambda r: np.convolve(r, k, "same"), 1, H)

SB = P.fill("highlight") if P.is_dark() else P.ink()
cmap = "magma" if P.is_dark() else "Greys"
fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.9), gridspec_kw={"width_ratios": [1, 1, 1.1]})
for ax, img, title in ((axs[0], wide, "A   Widefield (diffraction-limited)"), (axs[1], H, "B   Reconstruction from localizations")):
    ax.imshow(img, extent=(-L, L, -L, L), origin="lower", cmap=cmap, vmax=np.percentile(img, 99.7))
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(P.muted())
    ax.plot([300, 500], [-520, -520], color=SB, lw=3)
    ax.text(400, -490, "200 nm", color=SB, fontsize=7, ha="center", va="bottom")
    ax.set_title(title, loc="left", fontsize=9, color=P.ink())

ax = axs[2]
sel = np.abs(cent) < 300
pw = wide[sel].sum(axis=0)
ph = H[sel].sum(axis=0)
xs = cent + 250
m = (xs > -200) & (xs < 200)
ax.plot(xs[m], pw[m] / pw[m].max(), color=charts.line("neutral"), lw=1.8, label="widefield")
ax.plot(xs[m], ph[m] / ph[m].max(), color=charts.line("negative"), lw=1.6, label="localization")
for x0 in (-40, 40):
    ax.axvline(x0, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(-200, 200)
ax.set_ylim(0, 1.1)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "position across the filaments / nm", "normalized intensity")
ax.set_title("C   Two filaments 80 nm apart", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
