"""A linear Gaussian beta-VAE: its optimum is probabilistic PCA with noise variance beta * sigma^2.

Decoder p(x|z) = N(W z, sigma^2 I), prior z ~ N(0, I), encoder q(z|x) = N(V x, D) with D diagonal.
The beta-weighted negative ELBO equals beta times the negative ELBO with noise variance
beta * sigma^2 (up to a constant), so the optimum is the PPCA solution with s^2 = beta * sigma^2:
along the data eigenvector with variance lam_i the decoder gain is sqrt(max(lam_i - s^2, 0)),
the KL per latent is 0.5 * log+(lam_i / s^2) and the expected distortion is min(lam_i, s^2)
(reverse water-filling, the Gaussian rate-distortion solution).
A: 2-D data (variances 4 and 0.25 along rotated axes, sigma^2 = 0.3) and the reconstructions
   W E[z|x] for beta = 1 and beta = 6: the minor direction is not encoded and the major one is shrunk.
B: KL per latent against beta for 5-D data with variances 6, 3, 1.5, 0.6, 0.2 (sigma^2 = 0.4):
   latent i switches off at beta = lam_i / sigma^2.
C: the rate-distortion curve traced by beta.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)

# A: two-dimensional example
lam2 = np.array([4.0, 0.25])
sig2 = 0.3
ang = np.deg2rad(30)
Q = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
X = (rng.normal(size=(300, 2)) * np.sqrt(lam2)) @ Q.T


def recon(X, beta):
    s2 = beta * sig2
    w2 = np.maximum(lam2 - s2, 0.0)
    # posterior mean along eigenvector i: w_i x_i / (w_i^2 + s^2); decoded: w_i^2 x_i / (w_i^2 + s^2)
    gain = w2 / (w2 + s2)
    Y = X @ Q  # coordinates in the eigenbasis
    return (Y * gain) @ Q.T


fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
ax.scatter(X[:, 0], X[:, 1], s=6, color=P.muted(), alpha=0.5, label="data $\\boldsymbol{x}$")
for beta, col, mk in ((1.0, P.edge("dna"), "o"), (6.0, P.edge("negative"), "s")):
    R = recon(X[:60], beta)
    ax.scatter(R[:, 0], R[:, 1], s=10, marker=mk, color=col, label=f"reconstruction, $\\beta$ = {beta:g}", zorder=3)
for i in range(12):
    R = recon(X[i:i + 1], 1.0)
    ax.plot([X[i, 0], R[0, 0]], [X[i, 1], R[0, 1]], color=P.edge("dna"), lw=0.6, alpha=0.6)
ax.set_aspect("equal")
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-4.2, 4.2)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Reconstructions of a linear VAE", loc="left", fontsize=10)

# B: KL per latent against beta
lam = np.array([6.0, 3.0, 1.5, 0.6, 0.2])
s5 = 0.4
betas = np.logspace(-1, np.log10(30), 300)
ax = axs[1]
cols = [P.edge(t) for t in ("dna", "protein", "enzyme", "rna", "negative")]
for i, l in enumerate(lam):
    kl = 0.5 * np.log(np.maximum(l / (betas * s5), 1.0))
    ax.semilogx(betas, kl, color=cols[i], lw=1.8, label=f"$\\lambda_{i + 1}$ = {l:g}")
    ax.axvline(l / s5, color=cols[i], lw=0.7, ls=":")
ax.axvline(1.0, color=P.muted(), lw=1.0, ls="--")
ax.text(1.05, 1.95, "$\\beta = 1$", fontsize=8, color=P.muted())
ax.set_xlabel("$\\beta$")
ax.set_ylabel("KL per latent / nat")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
ax.set_title("B  Latents switch off one by one", loc="left", fontsize=10)

# C: rate-distortion curve
ax = axs[2]
s2 = betas * s5
rate = np.array([np.sum(0.5 * np.log(np.maximum(lam / s, 1.0))) for s in s2])
dist = np.array([np.sum(np.minimum(lam, s)) for s in s2])
ax.plot(dist, rate, color=P.edge("protein"), lw=2.0)
for b in (0.25, 1.0, 4.0, 16.0):
    s = b * s5
    r = np.sum(0.5 * np.log(np.maximum(lam / s, 1.0)))
    dd = np.sum(np.minimum(lam, s))
    ax.plot(dd, r, "o", color=P.edge("negative"), ms=5)
    ax.annotate(f"$\\beta$ = {b:g}", (dd, r), xytext=(6, 4), textcoords="offset points", fontsize=8, color=P.ink())
ax.set_xlabel("Distortion $\\mathbb{E}\\,\\Vert \\boldsymbol{x} - \\hat{\\boldsymbol{x}} \\Vert^2$")
ax.set_ylabel("Rate (total KL) / nat")
ax.set_title("C  Rate against distortion", loc="left", fontsize=10)
for a in axs[1:]:
    a.grid(True, alpha=0.3)
fig.tight_layout()
