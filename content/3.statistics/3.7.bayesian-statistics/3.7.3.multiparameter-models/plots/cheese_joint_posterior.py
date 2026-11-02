"""Cheese moisture example: joint posterior of (mu, sigma) and marginal posterior of mu
under the non-informative prior (Ann) and the normal-inverse-chi-square prior (Bob)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y = np.array([45.6, 41.1, 44.5, 44.0, 40.6, 44.1, 39.0, 39.5, 39.5, 41.7, 42.0, 42.6, 43.0,
              42.5, 42.7, 42.1, 42.4, 44.8, 41.0, 39.9, 43.9, 41.3, 45.1, 38.5, 43.8])
n, ybar = len(y), y.mean()
ss = np.sum((y - ybar) ** 2)  # (n - 1) s^2

# Ann: p(mu, sigma^2) proportional to 1/sigma^2
ann = dict(mu=ybar, kappa=n, nu=n - 1, nus2=ss)
# Bob: mu0 = 40, kappa0 = 1, nu0 = 1, prior median of sigma = 3
mu0, k0, nu0 = 40.0, 1.0, 1.0
s02 = 9 * stats.chi2(1).median()
kn = k0 + n
bob = dict(mu=(k0 * mu0 + n * ybar) / kn, kappa=kn, nu=nu0 + n,
           nus2=nu0 * s02 + ss + k0 * n / kn * (ybar - mu0) ** 2)


def log_joint(mu, sigma, p):
    """Log density of (mu, sigma) under N-Inv-chi2(mu_n, sigma_n^2/kappa_n; nu_n, sigma_n^2)."""
    s2 = sigma**2
    lp = stats.invgamma(p["nu"] / 2, scale=p["nus2"] / 2).logpdf(s2)
    lp += stats.norm(p["mu"], np.sqrt(s2 / p["kappa"])).logpdf(mu)
    return lp + np.log(2 * sigma)  # Jacobian from sigma^2 to sigma


def draws(p, size, rng):
    s2 = p["nus2"] / rng.chisquare(p["nu"], size)
    mu = rng.normal(p["mu"], np.sqrt(s2 / p["kappa"]))
    return mu, np.sqrt(s2)


rng = np.random.default_rng(0)
M, S = np.meshgrid(np.linspace(40.6, 43.8, 300), np.linspace(1.3, 3.3, 300))
fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
for ax, p, name, c in [(axes[0], ann, "Ann (non-informative prior)", "C0"),
                       (axes[1], bob, "Bob (conjugate prior)", "C3")]:
    dens = np.exp(log_joint(M, S, p))
    ax.contour(M, S, dens, levels=6, colors=c, linewidths=1.2)
    mu_s, sig_s = draws(p, 400, rng)
    ax.scatter(mu_s, sig_s, s=4, color="0.45", alpha=0.6)
    ax.set_title(name, fontsize=11)
    ax.set_xlim(40.6, 43.8)
    ax.set_ylim(1.3, 3.3)
    ax.set_xlabel(r"$\mu$ (% water)")
    ax.set_ylabel(r"$\sigma$")
    ax.grid(alpha=0.3)

m = np.linspace(39.5, 44.0, 600)
for p, name, c in [(ann, "Ann", "C0"), (bob, "Bob", "C3")]:
    scale = np.sqrt(p["nus2"] / p["nu"] / p["kappa"])
    axes[2].plot(m, stats.t(p["nu"], loc=p["mu"], scale=scale).pdf(m), color=c, lw=1.8,
                 label=rf"{name}: $t_{{{p['nu']:.0f}}}$({p['mu']:.2f}, {scale:.3f}$^2$)")
axes[2].axvline(mu0, color="0.5", ls="--", lw=1.0, label=r"Bob's prior mean $\mu_0$")
axes[2].set_title(r"marginal posterior of $\mu$", fontsize=11)
axes[2].set_xlabel(r"$\mu$ (% water)")
axes[2].set_ylabel("density")
axes[2].set_ylim(0, 1.45)
axes[2].legend(fontsize=8, loc="upper right")
axes[2].grid(alpha=0.3)
fig.tight_layout()
