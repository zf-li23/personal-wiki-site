"""Estimating a functional response from a simulated feeding experiment (Section 25.4.4).

Single predators are offered N0 prey for T = 1 day, without replacement, 6 replicates per density.
Type II data: true a = 0.8, h = 0.08; the expected number eaten solves Rogers' random predator
equation Ne = N0 [1 - exp(a (h Ne - T))] (written with the Lambert W function), and the observed
number is binomial. A: data with fits of Rogers' equation (accounts for depletion) and of the disc
equation (ignores it), by least squares. B: proportion eaten against N0 for the type II data and
for type III data (attack rate b N, b = 0.05, h = 0.08), with cubic logistic regressions: the
proportion falls from the start for type II and rises first for type III (Juliano's test).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares, minimize
from scipy.special import lambertw

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
T = 1.0
N0 = np.repeat([2, 4, 8, 16, 32, 64, 128], 6).astype(float)


def rogers(N0, a, h):
    return N0 - np.real(lambertw(a * h * N0 * np.exp(-a * (T - h * N0)))) / (a * h)


def type3_eaten(n0, b, h):
    s = solve_ivp(lambda t, n: [-b * n[0] ** 2 / (1 + b * h * n[0] ** 2)], [0, T], [n0], rtol=1e-8)
    return n0 - s.y[0, -1]


y2 = rng.binomial(N0.astype(int), rogers(N0, 0.8, 0.08) / N0)
y3 = rng.binomial(N0.astype(int), np.array([type3_eaten(n, 0.05, 0.08) for n in N0]) / N0)

fit_r = least_squares(lambda p: rogers(N0, *p) - y2, [0.5, 0.05], bounds=([1e-4, 1e-4], [10, 1]))
fit_d = least_squares(lambda p: p[0] * N0 * T / (1 + p[0] * p[1] * N0) - y2, [0.5, 0.05],
                      bounds=([1e-4, 1e-4], [10, 1]))
print("Rogers fit a, h =", fit_r.x, " disc fit a, h =", fit_d.x)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axes[0]
g = np.linspace(0.5, 130, 300)
jit = rng.uniform(-0.04, 0.04, N0.size)
ax.plot(N0 * (1 + jit), y2, "o", ms=3.5, color=C.line("neutral"), alpha=0.8, label="data")
ax.plot(g, rogers(g, 0.8, 0.08), color=P.ink(), lw=1.0, ls=(0, (2, 1.5)), label="true curve")
ax.plot(g, rogers(g, *fit_r.x), color=C.line("dna"), lw=1.4,
        label=f"Rogers fit: a = {fit_r.x[0]:.2f}, h = {fit_r.x[1]:.3f}")
ax.plot(g, fit_d.x[0] * g / (1 + fit_d.x[0] * fit_d.x[1] * g), color=C.line("negative"), lw=1.4,
        label=f"disc equation fit: a = {fit_d.x[0]:.2f}, h = {fit_d.x[1]:.3f}")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
C.style_axes(ax, "Initial prey number N0", "Prey eaten in 1 day")
C.title(ax, "A  Type II data, prey not replaced")

ax = axes[1]
for y, col, lab in [(y2, C.line("dna"), "type II data"), (y3, C.line("negative"), "type III data")]:
    X = np.vstack([np.ones_like(N0), N0, N0**2, N0**3]).T / np.array([1, 100, 1e4, 1e6])

    def nll(beta):
        eta = X @ beta
        return -np.sum(y * eta - N0 * np.logaddexp(0, eta))

    bhat = minimize(nll, np.zeros(4), method="BFGS").x
    Xg = np.vstack([np.ones_like(g), g, g**2, g**3]).T / np.array([1, 100, 1e4, 1e6])
    ax.plot(N0 * (1 + jit), y / N0, "o", ms=3, color=col, alpha=0.6)
    ax.plot(g, 1 / (1 + np.exp(-Xg @ bhat)), color=col, lw=1.4, label=f"{lab}: linear coef. {bhat[1]:+.1f}")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Initial prey number N0", "Proportion eaten")
C.title(ax, "B  Distinguishing type II from type III")
fig.tight_layout()
