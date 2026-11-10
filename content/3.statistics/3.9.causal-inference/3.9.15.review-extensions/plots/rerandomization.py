"""Rerandomization: distribution of the difference in means and variance reduction versus theory."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, n_t, k = 100, 50, 4
# A fixed finite population: four covariates, outcome with R^2 about 0.5, constant effect 1
x = rng.normal(0, 1, (n, k))
y0 = x @ np.array([0.5, 0.5, 0.5, 0.5]) + rng.normal(0, 1, n)
y1 = y0 + 1.0
s_inv = np.linalg.inv(np.cov(x, rowvar=False))

draws = 40_000
tau_hat = np.empty(draws)
m_stat = np.empty(draws)
for d in range(draws):
    w = np.zeros(n, dtype=bool)
    w[rng.choice(n, n_t, replace=False)] = True
    diff = x[w].mean(axis=0) - x[~w].mean(axis=0)
    m_stat[d] = n_t * (n - n_t) / n * diff @ s_inv @ diff
    tau_hat[d] = y1[w].mean() - y0[~w].mean()

# R^2 of the outcome on the covariates (finite population), which governs the gain
beta = np.linalg.lstsq(np.c_[np.ones(n), x], y0, rcond=None)[0]
r2 = 1 - np.var(y0 - np.c_[np.ones(n), x] @ beta) / np.var(y0)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4))
a01 = stats.chi2.ppf(0.1, k)
keep = m_stat <= a01
bins = np.linspace(tau_hat.min(), tau_hat.max(), 60)
axes[0].hist(tau_hat, bins=bins, density=True, alpha=0.5, color="C0", label="complete randomization")
axes[0].hist(tau_hat[keep], bins=bins, density=True, alpha=0.6, color="C1",
             label="rerandomization, $p_a = 0.1$")
axes[0].axvline(1.0, color="black", ls="--", lw=1)
axes[0].set_xlabel(r"$\hat\tau^{\mathrm{dif}}$ (true effect 1)")
axes[0].set_ylabel("density")
axes[0].legend(fontsize=8)

p_accept = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0])
ratio_emp, ratio_th = [], []
for p in p_accept:
    a = stats.chi2.ppf(p, k) if p < 1 else np.inf
    sel = m_stat <= a
    ratio_emp.append(tau_hat[sel].var() / tau_hat.var())
    v_a = 1.0 if p == 1 else stats.chi2.cdf(a, k + 2) / stats.chi2.cdf(a, k)
    ratio_th.append(1 - (1 - v_a) * r2)
axes[1].plot(p_accept, ratio_emp, "o", label="simulation")
axes[1].plot(p_accept, ratio_th, "-", color="C3", label=r"theory $1 - (1 - v_a)R^2$")
axes[1].set_xscale("log")
axes[1].set_xlabel("acceptance probability $p_a$")
axes[1].set_ylabel("variance ratio to complete randomization")
axes[1].set_title(f"$K = {k}$ covariates, $R^2 = {r2:.2f}$", fontsize=10)
axes[1].legend(fontsize=8)
fig.tight_layout()
