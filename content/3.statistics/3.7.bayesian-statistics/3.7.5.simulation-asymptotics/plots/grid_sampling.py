"""Discrete-grid sampling from a two-parameter posterior (semi-conjugate normal model, simulated data)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
y = rng.normal(10.0, 2.0, size=12)          # simulated data
n, ybar = len(y), y.mean()
mu0, tau0 = 5.0, 2.0                       # mu ~ N(mu0, tau0^2)
nu0, s0sq = 3.0, 4.0                       # sigma^2 ~ Inv-chi^2(nu0, s0sq), independent of mu

mu = np.linspace(4, 14, 201)
sig = np.linspace(0.6, 6, 217)
M, S = np.meshgrid(mu, sig, indexing="ij")
# log prior for (mu, sigma): Inv-chi^2 density of sigma^2 times the Jacobian 2 sigma
log_prior = stats.norm(mu0, tau0).logpdf(M) + stats.invgamma(nu0 / 2, scale=nu0 * s0sq / 2).logpdf(S**2) + np.log(2 * S)
log_lik = stats.norm(M[..., None], S[..., None]).logpdf(y).sum(axis=-1)
lp = log_prior + log_lik
p = np.exp(lp - lp.max())
p /= p.sum()                               # step 3: normalize on the grid

# steps 4-5: marginal of mu, then sigma given mu, then jitter
p_mu = p.sum(axis=1)
draws = 1000
i = rng.choice(len(mu), size=draws, p=p_mu)
j = np.array([rng.choice(len(sig), p=p[k] / p[k].sum()) for k in i])
dmu, dsig = mu[1] - mu[0], sig[1] - sig[0]
mu_s = mu[i] + rng.uniform(-dmu / 2, dmu / 2, draws)
sig_s = sig[j] + rng.uniform(-dsig / 2, dsig / 2, draws)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
levels = p.max() * np.array([0.001, 0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.95])
ax = axes[0]
ax.contour(M, S, p, levels=levels, colors="C0", linewidths=1)
ax.set_title("unnormalized posterior on a grid", fontsize=11)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma$")
ax.grid(alpha=0.3)
ax = axes[1]
ax.contour(M, S, p, levels=levels, colors="0.6", linewidths=0.8)
ax.scatter(mu_s, sig_s, s=4, color="C3", alpha=0.6)
ax.set_title("1000 grid draws with jitter", fontsize=11)
ax.set_xlabel(r"$\mu$")
ax.grid(alpha=0.3)
for ax in axes:
    ax.set_xlim(5, 13)
    ax.set_ylim(0.8, 5.5)
fig.tight_layout()
