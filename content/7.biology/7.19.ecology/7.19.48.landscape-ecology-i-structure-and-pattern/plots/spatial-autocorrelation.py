# Spatial autocorrelation of a landscape variable (e.g. soil moisture) on a 100 x 100 grid of 10 m cells.
# Gaussian random fields with correlation ranges of about 30 m and 150 m (white noise smoothed with
# Gaussian kernels) plus a small independent measurement error (nugget).
# A, B: the two fields. C: Moran's I correlogram by distance class (from 3000 randomly sampled cells).
# D: empirical semivariogram with fitted Gaussian models gamma(h) = c0 + c (1 - exp(-h^2/a^2))
#    (practical range sqrt(3) a).
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.optimize import curve_fit
import wikibio as bio

P = bio.P
rng = np.random.default_rng(5)
n, cell = 100, 10.0
fields = []
for sd in (1.5, 7.0):
    z = ndimage.gaussian_filter(rng.normal(size=(n, n)), sd, mode="wrap")
    z = (z - z.mean()) / z.std()
    z = z + 0.3 * rng.normal(size=(n, n))
    fields.append(z)

idx = rng.choice(n * n, 3000, replace=False)
pts = np.c_[idx // n, idx % n] * cell
dist = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(-1))
iu = np.triu_indices(len(idx), 1)
bins = np.arange(0, 520, 20)
mid = 0.5 * (bins[1:] + bins[:-1])

fig = plt.figure(figsize=(12.6, 4.2))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1.25, 1.25])
toks = ["dna", "negative"]
c_ax = fig.add_subplot(gs[2])
v_ax = fig.add_subplot(gs[3])
for k, (z, tok, lab) in enumerate(zip(fields, toks, ("short range", "long range"))):
    ax = fig.add_subplot(gs[k])
    ax.imshow(z, cmap="viridis", interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{'AB'[k]}  {lab}", loc="left", fontweight="bold", fontsize=10)
    v = z.ravel()[idx]
    dev = v - v.mean()
    prod = (dev[:, None] * dev[None, :])[iu]
    sq = 0.5 * ((v[:, None] - v[None, :]) ** 2)[iu]
    dd = dist[iu]
    I, g = [], []
    for lo, hi in zip(bins[:-1], bins[1:]):
        w = (dd > lo) & (dd <= hi)
        I.append(len(v) / w.sum() * prod[w].sum() / (dev ** 2).sum() * 0.5 * 2)   # Moran's I, binary weights
        g.append(sq[w].mean())
    col = P.fill(tok)
    c_ax.plot(mid, I, "o-", color=col, ms=3.5, lw=1.4, label=lab)
    g = np.array(g)
    model = lambda h, c0, c, a: c0 + c * (1 - np.exp(-(h / a) ** 2))
    (c0, c, a), _ = curve_fit(model, mid, g, p0=(0.1, 1.0, 50.0), bounds=([0, 0, 1], [2, 3, 1000]))
    v_ax.plot(mid, g, "o", color=col, ms=3.5)
    hh = np.linspace(0, 500, 200)
    v_ax.plot(hh, model(hh, c0, c, a), color=col, lw=1.6,
              label=f"{lab}: nugget {c0:.2f}, sill {c0 + c:.2f}, range {np.sqrt(3) * a:.0f} m")
c_ax.axhline(0, color=P.muted(), lw=0.8)
c_ax.set_xlabel("Distance / m")
c_ax.set_ylabel("Moran's I")
c_ax.legend(frameon=False, fontsize=7.5)
c_ax.set_title("C  Correlogram", loc="left", fontweight="bold")
v_ax.set_xlabel("Distance h / m")
v_ax.set_ylabel("Semivariance $\\gamma(h)$")
v_ax.set_ylim(0, 1.5)
v_ax.legend(frameon=False, fontsize=7, loc="lower right")
v_ax.set_title("D  Semivariogram", loc="left", fontweight="bold")
for ax in (c_ax, v_ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
