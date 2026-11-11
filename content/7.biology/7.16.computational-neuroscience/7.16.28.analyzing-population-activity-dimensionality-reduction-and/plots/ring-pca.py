"""PCA of a ring-attractor-like population.

100 neurons with preferred directions evenly spaced on the circle and von Mises tuning
f_i(theta) = 1 + 9 exp(kappa (cos(theta - theta_i) - 1)), kappa = 2; the represented direction
theta(t) performs a random walk (s.d. 0.15 rad per bin) for 3000 bins; activity = tuning + Gaussian
noise (s.d. 1). A: activity of the neurons (sorted by preferred direction) in 150 bins, with the
represented direction. B: projection on PC1 and PC2, colored by theta: a ring. C: variance
spectrum (fraction per PC, first 20) of the data and of pure noise of the same size, with the
Marchenko-Pastur edge of the noise, and the participation ratio.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)
N, T, kap = 100, 3000, 2.0
pref = np.linspace(-np.pi, np.pi, N, endpoint=False)
theta = np.cumsum(rng.normal(0, 0.15, T))
th = (theta + np.pi) % (2 * np.pi) - np.pi
R = 1 + 9 * np.exp(kap * (np.cos(th[:, None] - pref[None, :]) - 1)) + rng.normal(0, 1, (T, N))
X = R - R.mean(0)
U, S, Vt = np.linalg.svd(X, full_matrices=False)
lam = S ** 2 / (T - 1)
pr = lam.sum() ** 2 / (lam ** 2).sum()
noise = rng.normal(0, 1, (T, N))
noise -= noise.mean(0)
lamn = np.linalg.svd(noise, compute_uv=False) ** 2 / (T - 1)
mp_edge = (1 + np.sqrt(N / T)) ** 2

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1), gridspec_kw={"width_ratios": [1.3, 1, 1]})
ax = axs[0]
sel = slice(1000, 1150)
im = ax.imshow(R[sel].T, aspect="auto", origin="lower", cmap="magma", extent=[0, 150, -180, 180])
ax.plot(np.arange(150) + 0.5, np.degrees(th[sel]), ".", color="white", ms=2)
ax.set_xlabel("Time bin")
ax.set_ylabel("Preferred direction / deg")
ax.set_title("A  Population activity", loc="left", fontsize=10)

ax = axs[1]
Z = X @ Vt[:2].T
sc = ax.scatter(Z[:, 0], Z[:, 1], c=np.degrees(th), cmap="twilight", s=4)
ax.set_aspect("equal")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
cb = fig.colorbar(sc, ax=ax, fraction=0.045)
cb.set_label("Represented direction / deg")
ax.set_title("B  The first two PCs", loc="left", fontsize=10)

ax = axs[2]
k = np.arange(1, 21)
ax.semilogy(k, lam[:20] / lam.sum(), "o-", color=P.edge("rna"), lw=1.8, ms=4, label="data")
ax.semilogy(k, lamn[:20] / lamn.sum(), "s-", color=P.muted(), lw=1.4, ms=3.5, label="noise only")
ax.set_xlabel("Principal component")
ax.set_ylabel("Fraction of variance")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title(f"C  Spectrum (participation ratio {pr:.1f})", loc="left", fontsize=10)
fig.tight_layout()
