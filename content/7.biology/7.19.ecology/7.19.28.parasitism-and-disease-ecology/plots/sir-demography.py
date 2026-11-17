"""The SIR model in a host population with births and deaths (Section 28.3), fractions s, i.
A: a closed epidemic (no demography), R0 = 3, infectious period 1 week: the epidemic peaks when
s = 1/R0 and stops with a fraction s_inf of susceptibles left (dashed), given by the final size equation.
B: with births and deaths (life expectancy 1/mu = 50 years) and measles-like parameters (R0 = 15,
infectious period 2 weeks): recurrent epidemics damped toward the endemic equilibrium
s* = 1/R0; the interepidemic period approaches 2 pi sqrt(A D) (A = mean age at infection,
D = infectious period), about 2.3 years here.
C: the same with seasonal transmission beta(t) = beta0 (1 + 0.25 cos 2 pi t), mimicking school
terms: after a long transient, sustained biennial epidemics (years 180-200 shown), large and small
epidemics alternating. Incidence (new infections per year) on a log scale.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
S_col, I_col = C.line("dna"), C.line("negative")

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
R0, g = 3.0, 1.0
f = lambda t, z: [-R0 * g * z[0] * z[1], R0 * g * z[0] * z[1] - g * z[1]]
s = solve_ivp(f, [0, 25], [1 - 1e-4, 1e-4], max_step=0.02, rtol=1e-10, atol=1e-12)
sinf = brentq(lambda x: x - np.exp(-R0 * (1 - x)), 1e-9, 0.5)
ax.plot(s.t, s.y[0], color=S_col, lw=1.4, label="susceptible s")
ax.plot(s.t, s.y[1], color=I_col, lw=1.4, label="infectious i")
ax.axhline(1 / R0, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
ax.axhline(sinf, color=S_col, lw=0.8, ls=(0, (4, 2)))
ax.text(25, 1 / R0 + 0.02, "1/R0", ha="right", fontsize=FS["tiny"], color=P.muted())
ax.text(25, sinf + 0.02, f"s∞ = {sinf:.3f}", ha="right", fontsize=FS["tiny"], color=S_col)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="center right")
C.style_axes(ax, "Time (weeks)", "Fraction of population")
C.title(ax, "A  Closed epidemic, R0 = 3")

mu, gam, R0 = 1 / 50, 365 / 14, 15.0
beta0 = R0 * (gam + mu)


def rhs(t, z, eps):
    ls, li = z
    S, I = np.exp(ls), np.exp(li)
    b = beta0 * (1 + eps * np.cos(2 * np.pi * t))
    return [(mu - b * S * I - mu * S) / S, b * S - gam - mu]


A = 1 / (mu * (R0 - 1))
D = 1 / (gam + mu)
for ax, eps, lab in [(axes[1], 0.0, "B  Endemic, damped recurrent epidemics"),
                     (axes[2], 0.25, "C  Seasonal forcing: biennial epidemics")]:
    z0 = [np.log(0.1), np.log(1e-4)]
    s = solve_ivp(rhs, [0, 40 if eps == 0 else 200], z0, args=(eps,), method="LSODA", rtol=1e-9, atol=1e-11, dense_output=True)
    t = np.linspace(0, 40, 6000) if eps == 0 else np.linspace(180, 200, 6000)
    S, I = np.exp(s.sol(t))
    inc = beta0 * (1 + eps * np.cos(2 * np.pi * t)) * S * I
    ax.semilogy(t, inc, color=I_col, lw=1.0)
    ax.set_ylim(1e-6, 1)
    C.style_axes(ax, "Time (years)", "Incidence (fraction infected per year)")
    C.title(ax, lab)
axes[1].text(39, 0.3, f"period → 2π√(AD) = {2 * np.pi * np.sqrt(A * D):.1f} yr", ha="right",
             fontsize=FS["tiny"], color=P.ink())
fig.tight_layout()
