"""Randomization distribution, variance estimators and coverage in a fixed finite population."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, n_t = 100, 50
n_c = n - n_t
k_draws = 4000
z = stats.norm.ppf(0.975)

y0_base = rng.normal(0, 1, n)
eta = rng.normal(0, 1, n)                     # drives the heterogeneity of unit-level effects
assign = np.array([rng.permutation(n) < n_t for _ in range(k_draws)])


def population(h):
    """Fixed potential outcomes with average effect 1 and effect heterogeneity h."""
    y0 = y0_base
    y1 = y0 + 1.0 + h * eta
    return y0, y1


def simulate(y0, y1):
    yt = np.where(assign, y1, np.nan)
    yc = np.where(~assign, y0, np.nan)
    est = np.nanmean(yt, axis=1) - np.nanmean(yc, axis=1)
    st2, sc2 = np.nanvar(yt, axis=1, ddof=1), np.nanvar(yc, axis=1, ddof=1)
    v_ney = sc2 / n_c + st2 / n_t
    v_rho1 = v_ney - (np.sqrt(st2) - np.sqrt(sc2)) ** 2 / n
    return est, v_ney, v_rho1


def true_var(y0, y1):
    return y0.var(ddof=1) / n_c + y1.var(ddof=1) / n_t - (y1 - y0).var(ddof=1) / n


fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))

# Panel 1: randomization distribution for one heterogeneous population
y0, y1 = population(1.0)
tau_fs = np.mean(y1 - y0)
est, v_ney, _ = simulate(y0, y1)
ax = axes[0]
ax.hist(est, bins=40, density=True, color="C0", alpha=0.55, label="randomization distribution")
grid = np.linspace(est.min(), est.max(), 300)
ax.plot(grid, stats.norm.pdf(grid, tau_fs, np.sqrt(true_var(y0, y1))), color="C1", lw=2,
        label="normal, true variance")
ax.plot(grid, stats.norm.pdf(grid, tau_fs, np.sqrt(v_ney.mean())), color="C3", lw=2, ls="--",
        label="normal, mean Neyman estimate")
ax.axvline(tau_fs, color="black", lw=1)
ax.set_xlabel("difference-in-means estimate")
ax.set_ylabel("density")
ax.set_title("Heterogeneous effects (h = 1)", fontsize=10)
ax.legend(fontsize=7.5, loc="upper left")

# Panels 2 and 3: variance and coverage as heterogeneity grows
hs = np.linspace(0, 2, 11)
tv, mney, mrho, cover = [], [], [], []
for h in hs:
    y0, y1 = population(h)
    tau_fs = np.mean(y1 - y0)
    est, v_ney, v_rho1 = simulate(y0, y1)
    tv.append(true_var(y0, y1))
    mney.append(v_ney.mean())
    mrho.append(v_rho1.mean())
    cover.append(np.mean(np.abs(est - tau_fs) <= z * np.sqrt(v_ney)))
ax = axes[1]
ax.plot(hs, tv, color="C1", lw=2, label="true variance")
ax.plot(hs, mney, color="C3", lw=2, ls="--", label="mean Neyman estimate")
ax.plot(hs, mrho, color="C2", lw=2, ls=":", label="mean rho = 1 estimate")
ax.set_xlabel("effect heterogeneity h")
ax.set_ylabel("variance of the estimator")
ax.set_title("Variance and its estimators", fontsize=10)
ax.legend(fontsize=8)
ax = axes[2]
ax.plot(hs, cover, color="C3", lw=2, marker="o", ms=4)
ax.axhline(0.95, color="gray", ls="--", lw=1)
ax.set_ylim(0.9, 1.0)
ax.set_xlabel("effect heterogeneity h")
ax.set_ylabel("coverage of tau_fs")
ax.set_title("Coverage of the 95% Neyman interval", fontsize=10)
for a in axes:
    a.grid(alpha=0.3)
fig.tight_layout()
