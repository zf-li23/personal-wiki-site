"""Spatial autocorrelation and clustering tests on synthetic data. A: a smooth expression field on a
30 x 30 grid of spots (Gaussian-filtered noise). B: the same values shuffled over the grid.
C: Moran's I with rook (4-neighbour) weights for both, against the permutation null of 999 random
relabelings of B's values (identical for A, since the values are the same); dashed: E[I] = -1/(n-1).
D: Ripley's L(r) - r for 300 points in the unit square with toroidal edge correction: complete
spatial randomness (CSR, a Poisson process) and a clustered Thomas process (30 parents, 10
offspring each, spread 0.02); shaded: the range of 99 CSR simulations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
m = 30
n = m * m
field = ndi.gaussian_filter(rng.normal(size=(m, m)), 1.2, mode="wrap")
field = (field - field.mean()) / field.std()
shuffled = rng.permutation(field.ravel()).reshape(m, m)


def moran(z):
    """Moran's I with binary rook weights on the grid (no wrap)."""
    z = z - z.mean()
    s = (z[1:, :] * z[:-1, :]).sum() + (z[:, 1:] * z[:, :-1]).sum()
    W = 2 * (m - 1) * m * 2          # each adjacent pair counted twice (w_ij and w_ji)
    return n / W * 2 * s / (z * z).sum()


I_a, I_b = moran(field), moran(shuffled)
null = np.array([moran(rng.permutation(field.ravel()).reshape(m, m)) for _ in range(999)])
p_a = (1 + np.sum(null >= I_a)) / 1000
p_b = (1 + np.sum(null >= I_b)) / 1000


def ripley_L(pts, r):
    d = np.abs(pts[:, None, :] - pts[None, :, :])
    d = np.minimum(d, 1 - d)                       # torus
    d = np.hypot(d[..., 0], d[..., 1])
    np.fill_diagonal(d, np.inf)
    N = len(pts)
    K = np.array([(d < ri).sum() for ri in r]) / (N * (N - 1))
    return np.sqrt(K / np.pi)


r = np.linspace(0.005, 0.15, 40)
csr = rng.uniform(size=(300, 2))
parents = rng.uniform(size=(30, 2))
thomas = (np.repeat(parents, 10, axis=0) + rng.normal(0, 0.02, (300, 2))) % 1.0
L_csr, L_th = ripley_L(csr, r), ripley_L(thomas, r)
env = np.array([ripley_L(rng.uniform(size=(300, 2)), r) for _ in range(99)])
RESULT = {"I_smooth": I_a, "I_shuffled": I_b, "p_smooth": p_a, "p_shuffled": p_b,
          "null_mean": null.mean(), "null_sd": null.std(), "E": -1 / (n - 1),
          "L-r thomas at 0.05": np.interp(0.05, r, L_th) - 0.05, "L-r csr at 0.05": np.interp(0.05, r, L_csr) - 0.05,
          "env at 0.05": (np.interp(0.05, r, env.min(0)) - 0.05, np.interp(0.05, r, env.max(0)) - 0.05)}

fig, axs = plt.subplots(1, 4, figsize=(12.6, 3.3), gridspec_kw={"width_ratios": [1, 1, 1.25, 1.25]})
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.17, top=0.86, wspace=0.28)
for a, z, t in [(axs[0], field, f"A  Smooth field, I = {I_a:.2f}"), (axs[1], shuffled, f"B  Shuffled, I = {I_b:.3f}")]:
    a.imshow(z, cmap="RdBu_r", vmin=-2.5, vmax=2.5, interpolation="nearest")
    a.set_xticks([])
    a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color(P.muted())
    charts.title(a, t)
axs[2].hist(null, 30, color=P.fill("neutral"), alpha=0.9)
axs[2].axvline(-1 / (n - 1), color=P.muted(), ls="--", lw=0.9)
axs[2].axvline(I_b, color=charts.line("dna"), lw=1.4)
axs[2].annotate(f"A: I = {I_a:.2f}\n(far right)", (0.98, 0.86), xycoords="axes fraction", ha="right",
                fontsize=7.5, color=P.ink())
axs[2].text(I_b + 0.004, axs[2].get_ylim()[1] * 0.9, "B", fontsize=7.5, color=charts.line("dna"))
charts.style_axes(axs[2], "Moran's I under permutation", "count")
charts.title(axs[2], "C  Permutation null (999)")
axs[3].fill_between(r, env.min(0) - r, env.max(0) - r, color=P.fill("neutral"), alpha=0.5, lw=0)
axs[3].plot(r, L_csr - r, color=charts.line("dna"), lw=1.4, label="CSR")
axs[3].plot(r, L_th - r, color=charts.line("rna"), lw=1.6, label="clustered (Thomas)")
axs[3].axhline(0, color=P.muted(), lw=0.7)
axs[3].legend(frameon=False, fontsize=7.5, labelcolor=P.ink())
charts.style_axes(axs[3], "distance r", "L(r) - r")
charts.title(axs[3], "D  Ripley's L function")
