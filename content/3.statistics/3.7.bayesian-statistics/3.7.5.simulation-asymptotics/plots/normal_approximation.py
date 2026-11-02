"""Exact posteriors and their normal approximations at the posterior mode (binomial model)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize


def mode_and_info(logpost):
    res = optimize.minimize_scalar(lambda t: -logpost(t), bounds=(1e-4, 1 - 1e-4), method="bounded",
                                   options={"xatol": 1e-10})
    m, h = res.x, 1e-5
    info = -(logpost(m + h) - 2 * logpost(m) + logpost(m - h)) / h**2
    return m, info


def mixture_logpost(y, n):
    def f(t):
        prior = 0.5 * stats.beta(8, 2).pdf(t) + 0.5 * stats.beta(2, 8).pdf(t)
        return np.log(prior) + y * np.log(t) + (n - y) * np.log(1 - t)
    return f


t = np.linspace(0.001, 0.999, 999)
fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
cases = [
    ("Beta(3, 3) prior, y = 37, n = 41", lambda s: stats.beta(40, 7).logpdf(s)),
    ("mixture prior, y = 37, n = 41", mixture_logpost(37, 41)),
    ("mixture prior, y = 5, n = 10", mixture_logpost(5, 10)),
]
for ax, (title, f) in zip(axes, cases):
    m, info = mode_and_info(f)
    dens = np.exp(f(t))
    dens /= np.trapezoid(dens, t)
    ax.plot(t, dens, color="C3", lw=1.8, label="exact posterior")
    ax.plot(t, stats.norm(m, info**-0.5).pdf(t), color="C0", lw=1.5, ls="--", label="normal approximation")
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(r"$\theta$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("density")
axes[0].legend(fontsize=9)

# Beta(10, 10) prior with a fixed observed proportion 0.1 and growing n
fig2, axes2 = plt.subplots(1, 4, figsize=(13, 3.3), sharex=True)
t = np.linspace(0, 0.4, 801)
for ax, n in zip(axes2, [50, 100, 200, 400]):
    y = n // 10
    a, b = 10 + y, 10 + n - y
    m = (a - 1) / (a + b - 2)
    sd = np.sqrt(m * (1 - m) / (a + b - 2))
    ax.plot(t, stats.beta(a, b).pdf(t), color="C3", lw=1.8, label="exact")
    ax.plot(t, stats.norm(m, sd).pdf(t), color="C0", lw=1.5, ls="--", label="normal approx.")
    ax.set_title(f"y = {y}, n = {n}", fontsize=11)
    ax.set_xlabel(r"$\theta$")
    ax.grid(alpha=0.3)
axes2[0].legend(fontsize=9)
fig2.tight_layout()
fig.tight_layout()
