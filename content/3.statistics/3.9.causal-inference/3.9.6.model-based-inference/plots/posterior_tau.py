"""Posterior of the average effect in the six-unit normal example (model-based imputation)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
w = np.array([0, 1, 0, 1, 0, 1])
y = np.array([0.0, 9.9, 12.4, 3.6, 0.0, 24.9])     # first six NSW units (earnings, 1000 USD)
n = len(y)
sig_c, sig_t = 10.0, 8.0                             # known outcome standard deviations
prior_var = 100.0 ** 2                               # mu_c, mu_t ~ N(0, 100^2)


def posterior_mu(yg, sig):
    prec = len(yg) / sig ** 2 + 1 / prior_var
    return (yg.sum() / sig ** 2) / prec, 1 / prec


m_c, v_c = posterior_mu(y[w == 0], sig_c)
m_t, v_t = posterior_mu(y[w == 1], sig_t)

# Monte Carlo: draw theta, then the missing potential outcomes, then tau_fs (rho = 0)
draws = 20000
mu_c = rng.normal(m_c, np.sqrt(v_c), draws)
mu_t = rng.normal(m_t, np.sqrt(v_t), draws)
y1_mis = rng.normal(mu_t[:, None], sig_t, (draws, (w == 0).sum()))
y0_mis = rng.normal(mu_c[:, None], sig_c, (draws, (w == 1).sum()))
tau_fs = (y1_mis.sum(1) - y[w == 0].sum() + y[w == 1].sum() - y0_mis.sum(1)) / n

# Analytic posteriors
n_c, n_t = (w == 0).sum(), (w == 1).sum()
mean0 = (n_c * m_t - y[w == 0].sum() + y[w == 1].sum() - n_t * m_c) / n
var0 = (n_c * sig_t ** 2 + n_c ** 2 * v_t + n_t * sig_c ** 2 + n_t ** 2 * v_c) / n ** 2
# rho = 1: Y_i(1) = mu_t + (sig_t/sig_c)(Y_i(0) - mu_c), so tau_fs is linear in (mu_c, mu_t)
r = sig_t / sig_c
a_t = (n_c + n_t / r) / n                            # coefficient of mu_t
a_c = -(n_c * r + n_t) / n                           # coefficient of mu_c
const = (((r - 1) * y[w == 0]).sum() + ((1 - 1 / r) * y[w == 1]).sum()) / n
mean1 = a_t * m_t + a_c * m_c + const
var1 = a_t ** 2 * v_t + a_c ** 2 * v_c
mean_sp, var_sp = m_t - m_c, v_t + v_c

grid = np.linspace(-20, 35, 400)
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
ax = axes[0]
ax.hist(tau_fs, bins=60, density=True, color="C0", alpha=0.5, label="Monte Carlo draws")
ax.plot(grid, stats.norm.pdf(grid, mean0, np.sqrt(var0)), color="C1", lw=2,
        label=f"analytic N({mean0:.1f}, {np.sqrt(var0):.1f}^2)")
ax.set_xlabel(r"$\tau_{\mathrm{fs}}$")
ax.set_ylabel("posterior density")
ax.set_title("Finite-sample effect, independent outcomes")
ax.legend(fontsize=8, frameon=False)

ax = axes[1]
for m, v, lab, col in [(mean0, var0, r"$\tau_{\mathrm{fs}}$, $\rho = 0$", "C1"),
                       (mean1, var1, r"$\tau_{\mathrm{fs}}$, $\rho = 1$", "C2"),
                       (mean_sp, var_sp, r"$\tau_{\mathrm{sp}}$", "C3")]:
    ax.plot(grid, stats.norm.pdf(grid, m, np.sqrt(v)), color=col, lw=2,
            label=f"{lab}: sd {np.sqrt(v):.2f}")
ax.set_xlabel("average effect")
ax.set_title("Three posterior distributions")
ax.legend(fontsize=8, frameon=False)
fig.tight_layout()
