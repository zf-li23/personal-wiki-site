"""Importance sampling and SIR for a normal model with observations censored at 0 (simulated data)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
# simulated data: n exact observations, m further observations known only to be positive
n, m = 10, 10
x = rng.normal(0.5, 1.0, size=n)
xbar, s2 = x.mean(), x.var(ddof=1)

# proposal g: the normal-inverse-chi^2 posterior of the exact observations, p(mu, sigma^2) ~ 1/sigma^2
S = 20000
sig2 = (n - 1) * s2 / rng.chisquare(n - 1, size=S)
mu = rng.normal(xbar, np.sqrt(sig2 / n))
sig = np.sqrt(sig2)

# importance weights: the extra likelihood factor Phi(mu/sigma)^m, on the log scale
logw = m * stats.norm.logcdf(mu / sig)
w = np.exp(logw - logw.max())
wn = w / w.sum()
ess = 1 / np.sum(wn**2)

# SIR: resample k draws without replacement, probabilities proportional to the weights
k = 2000
idx = rng.choice(S, size=k, replace=False, p=wn)

# exact posterior on a grid, for comparison
mg = np.linspace(-0.8, 2.2, 400)
sg = np.linspace(0.3, 2.5, 400)
MG, SG = np.meshgrid(mg, sg, indexing="ij")
# density of (mu, sigma): prior 1/sigma^2 times the Jacobian 2 sigma, times the full likelihood
lp = -(n + 1) * np.log(SG) - ((n - 1) * s2 + n * (xbar - MG) ** 2) / (2 * SG**2) + m * stats.norm.logcdf(MG / SG)
post = np.exp(lp - lp.max())
post_mu = post.sum(axis=1)
post_mu /= post_mu.sum() * (mg[1] - mg[0])

fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axes[0]
sel = rng.choice(S, size=2000, replace=False)
ax.scatter(mu[sel], sig[sel], s=3, color="0.6", alpha=0.5, label="proposal draws")
ax.scatter(mu[idx], sig[idx], s=3, color="C3", alpha=0.5, label="SIR draws")
ax.contour(MG, SG, post, levels=post.max() * np.array([0.05, 0.25, 0.6]), colors="C0", linewidths=1)
ax.set_xlim(-0.8, 2.2)
ax.set_ylim(0.3, 2.2)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma$")
ax.set_title("proposal vs resampled draws", fontsize=11)
ax.legend(fontsize=8, loc="upper left", markerscale=3)

ax = axes[1]
bins = np.linspace(-0.8, 2.2, 46)
ax.hist(mu, bins=bins, density=True, color="0.75", label="proposal (exact data only)")
ax.hist(mu[idx], bins=bins, density=True, histtype="step", color="C3", lw=1.5, label="SIR draws")
ax.plot(mg, post_mu, color="C0", lw=1.5, label="exact posterior (grid)")
ax.set_xlabel(r"$\mu$")
ax.set_title(r"marginal posterior of $\mu$", fontsize=11)
ax.legend(fontsize=8, loc="upper right")

ax = axes[2]
ax.plot(np.arange(1, S + 1) / S, np.sort(wn)[::-1] * S, color="C2", lw=1.5)
ax.axhline(1, color="0.5", lw=1, ls="--")
ax.set_yscale("log")
ax.set_xlabel("rank of draw / S")
ax.set_ylabel(r"normalized weight $\times S$")
ax.set_title(f"sorted weights; ESS = {ess:.0f} of S = {S}", fontsize=11)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
