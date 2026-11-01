"""Deconvolution of capture spots by a Poisson mixture (simulation). A: reference expression profiles
of four cell types over 60 genes (columns sum to 1; each type has 15 marker genes). B: true and
estimated proportions of 300 spots with 1000 UMIs each, proportions drawn from a Dirichlet(0.5)
distribution; estimates by the EM algorithm for the mixture weights. C: mean absolute error of the
proportions against the number of UMIs per spot, without and with a gene-specific platform effect
(log-normal, sd 0.5) that the reference does not include: sampling error falls as the depth grows,
the bias from the platform effect does not."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
K, G, S = 4, 60, 300
mu = rng.gamma(1.0, 1.0, (G, K)) * 0.3
for k in range(K):
    mu[15 * k:15 * (k + 1), k] += rng.gamma(4.0, 1.0, 15)
mu /= mu.sum(0)
types = ["tumor", "fibroblast", "T cell", "macrophage"]
tok = ["negative", "plant", "dna", "rna"]


def em(y, mu, iters=300):
    """Maximum-likelihood mixture weights for y_g ~ Poisson(N sum_k pi_k mu_gk)."""
    pi = np.full(mu.shape[1], 1 / mu.shape[1])
    for _ in range(iters):
        lam = mu @ pi
        pi = pi * (mu.T @ (y / lam)) / y.sum()
    return pi


platform = np.exp(rng.normal(0, 0.5, G))   # one fixed set of gene-specific platform effects


def simulate(N, platform_sd, n=S):
    pis = rng.dirichlet(np.full(K, 0.5), n)
    eff = platform if platform_sd else np.ones(G)
    out = []
    for pi in pis:
        lam = eff * (mu @ pi)
        y = rng.poisson(N * lam / lam.sum())
        out.append(em(y, mu))
    return pis, np.array(out)


true, est = simulate(1000, 0)
mae1000 = np.abs(true - est).mean()
depths = np.array([100, 200, 500, 1000, 2000, 5000, 20000])
mae0 = [np.abs(np.subtract(*simulate(N, 0, 200))).mean() for N in depths]
mae5 = [np.abs(np.subtract(*simulate(N, 0.5, 200))).mean() for N in depths]
RESULT = {"mae1000": mae1000, "depths": depths, "mae0": np.round(mae0, 4), "mae5": np.round(mae5, 4)}

fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.5), gridspec_kw={"width_ratios": [0.8, 1, 1.15]})
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.35)
axs[0].imshow(mu, aspect="auto", cmap="viridis", interpolation="nearest")
axs[0].set_xticks(range(K))
axs[0].set_xticklabels(types, rotation=30, ha="right")
charts.style_axes(axs[0], None, "gene")
charts.title(axs[0], "A  Reference profiles")
for k in range(K):
    axs[1].scatter(true[:, k], est[:, k], s=6, color=P.fill(tok[k]), edgecolor=P.edge(tok[k]), lw=0.3, label=types[k])
axs[1].plot([0, 1], [0, 1], color=P.muted(), lw=0.8)
axs[1].legend(frameon=False, fontsize=7, labelcolor=P.ink(), markerscale=2)
charts.style_axes(axs[1], "true proportion", "estimated proportion")
charts.title(axs[1], f"B  1000 UMIs per spot, MAE {mae1000:.3f}")
axs[2].plot(depths, mae0, "o-", ms=3, color=charts.line("dna"), lw=1.4, label="reference matches platform")
axs[2].plot(depths, mae5, "o-", ms=3, color=charts.line("negative"), lw=1.4, label="platform effect, sd 0.5")
axs[2].set_xscale("log")
axs[2].set_yscale("log")
axs[2].set_yticks([0.003, 0.01, 0.03])
axs[2].set_yticklabels(["0.003", "0.01", "0.03"])
axs[2].yaxis.set_minor_formatter(plt.matplotlib.ticker.NullFormatter())
axs[2].legend(frameon=False, fontsize=7, labelcolor=P.ink())
charts.style_axes(axs[2], "UMIs per spot", "mean absolute error")
charts.title(axs[2], "C  Sampling error and bias")
