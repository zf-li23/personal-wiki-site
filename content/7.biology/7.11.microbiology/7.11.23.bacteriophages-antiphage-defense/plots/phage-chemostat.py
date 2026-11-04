# Phage and bacteria in a chemostat: the model of Levin, Stewart and Chao (1977).
#   ds/dt = D (s0 - s) - mu(s) N / Y
#   dN/dt = mu(s) N - delta N P - D N
#   dP/dt = beta delta N(t - tau) P(t - tau) exp(-D tau) - delta N P - D P
# with Monod growth mu(s) = mu_max s / (Ks + s). The delay is integrated by keeping a history buffer.
# Parameters: mu_max = 0.7 per h, Ks = 0.5 ug/ml, Y = 2e6 cells per ug, s0 = 10 ug/ml, D = 0.2 per h,
# delta = 1.5e-9 ml per h per phage, beta = 40, tau = 0.5 h. The resistant mutant has a 15 % lower mu_max
# and delta = 0.
# A: sensitive host and phage - the phage holds the host far below its resource-limited density, with
#    damped oscillations whose period is set by the latent period and the growth rate.
# B: the resource, showing that control has passed from the resource to the predator.
# C: a resistant mutant introduced at t = 50 h sweeps while phage are abundant; the cost of resistance
#    keeps a sensitive subpopulation, and with it the phage.
# D: the phage's growth rate against its latent period at two host densities: short latent periods win
#    when hosts are abundant, long ones when they are scarce.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
MU, KS, Y, S0, D = 0.7, 0.5, 2e6, 10.0, 0.2
DELTA, BETA, TAU = 1.5e-9, 40.0, 0.5
COST = 0.85


def simulate(T=200.0, dt=0.002, resistant_at=None):
    """Euler integration with a delay buffer; returns t, s, N (sensitive), R (resistant), Pp (phage)."""
    n = int(T / dt)
    lag = int(TAU / dt)
    s = np.empty(n)
    N = np.empty(n)
    R = np.empty(n)
    Pp = np.empty(n)
    s[0], N[0], R[0], Pp[0] = S0, 1e5, 0.0, 1e4
    for i in range(n - 1):
        mu = MU * s[i] / (KS + s[i])
        mur = COST * MU * s[i] / (KS + s[i])
        j = i - lag
        birth = BETA * DELTA * N[j] * Pp[j] * np.exp(-D * TAU) if j >= 0 else 0.0
        ds = D * (S0 - s[i]) - (mu * N[i] + mur * R[i]) / Y
        dN = mu * N[i] - DELTA * N[i] * Pp[i] - D * N[i]
        dR = mur * R[i] - D * R[i]
        dP = birth - DELTA * N[i] * Pp[i] - D * Pp[i]
        s[i + 1] = max(s[i] + dt * ds, 1e-9)
        N[i + 1] = max(N[i] + dt * dN, 1e-3)
        R[i + 1] = max(R[i] + dt * dR, 0.0)
        Pp[i + 1] = max(Pp[i] + dt * dP, 1e-3)
        if resistant_at is not None and abs((i + 1) * dt - resistant_at) < dt / 2:
            R[i + 1] = 1e3
    return np.arange(n) * dt, s, N, R, Pp


t, s1, N1, _, P1 = simulate()
t2, s2, N2, R2, P2 = simulate(resistant_at=50.0)
N_only = Y * (S0 - KS * D / (MU - D))          # density without phage (resource-limited steady state)

fig = plt.figure(figsize=(14.2, 4.3))
gs = fig.add_gridspec(1, 4, width_ratios=[1.15, 0.95, 1.15, 1.0], wspace=0.36)

# ---------------------------------------------------------------- A
ax = fig.add_subplot(gs[0, 0])
ax.plot(t, N1, color=charts.line("bacterium"), lw=1.8, label="sensitive bacteria")
ax.plot(t, P1, color=charts.line("virus"), lw=1.8, label="free phage")
ax.axhline(N_only, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.text(198, N_only * 1.5, "density without phage", fontsize=6.8, color=P.muted(), ha="right")
ax.set_yscale("log")
ax.set_ylim(1e3, 1e10)
ax.set_xlim(0, 200)
ax.legend(fontsize=6.8, frameon=False, loc="lower right", labelcolor=P.ink())
charts.style_axes(ax, "time / h", "ml$^{-1}$")
charts.title(ax, "A   Coexistence, not extinction")

# ---------------------------------------------------------------- B
ax = fig.add_subplot(gs[0, 1])
ax.plot(t, s1, color=charts.line("carbohydrate"), lw=1.8)
ax.axhline(S0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.text(198, S0 * 0.93, "input $s_0$", fontsize=6.8, color=P.muted(), ha="right", va="top")
ax.set_ylim(0, S0 * 1.1)
ax.set_xlim(0, 200)
charts.style_axes(ax, "time / h", "resource / ($\\mu$g ml$^{-1}$)")
charts.title(ax, "B   Control passes to the predator")

# ---------------------------------------------------------------- C
ax = fig.add_subplot(gs[0, 2])
ax.plot(t2, N2, color=charts.line("bacterium"), lw=1.8, label="sensitive")
ax.plot(t2, R2, color=charts.line("positive"), lw=1.8, label="resistant (15 % slower)")
ax.plot(t2, P2, color=charts.line("virus"), lw=1.8, label="phage")
ax.axvline(50, color=P.muted(), lw=0.8, ls=":")
ax.text(52, 2e9, "resistant mutant\nintroduced", fontsize=6.8, color=P.muted())
ax.set_yscale("log")
ax.set_ylim(1e2, 1e10)
ax.set_xlim(0, 200)
ax.legend(fontsize=6.8, frameon=False, loc="lower right", labelcolor=P.ink())
charts.style_axes(ax, "time / h", "ml$^{-1}$")
charts.title(ax, "C   A resistant mutant and the cost of resistance")

# ---------------------------------------------------------------- D
ax = fig.add_subplot(gs[0, 3])
tau = np.linspace(0.15, 2.0, 300)
for Nh, tok, name in ((5e8, "dna", "hosts abundant (5 × $10^8$ ml$^{-1}$)"), (5e6, "drug", "hosts scarce (5 × $10^6$ ml$^{-1}$)")):
    beta = 20 + 120 * (tau - 0.15)                       # a longer latent period gives a larger burst
    adsorb = 1 / (DELTA * Nh)                            # mean time to find the next host
    rate = np.log(beta) / (tau + adsorb)        # phage growth rate: ln(burst) per generation time
    rate = rate / rate.max()                    # each curve normalized to its own maximum
    ax.plot(tau, rate, color=charts.line(tok), lw=1.9, label=name)
    i = int(np.argmax(rate))
    ax.plot([tau[i]], [rate[i]], "o", ms=5, color=charts.line(tok))
ax.set_xlim(0.15, 2.0)
ax.set_ylim(0, 1.08)
ax.legend(fontsize=6.8, frameon=False, loc="lower right", labelcolor=P.ink())
charts.style_axes(ax, "latent period $\\tau$ / h", "growth rate (relative to its maximum)")
charts.title(ax, "D   The optimal latent period")
