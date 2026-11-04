# The growth of a bacterial population in a batch culture.
# A: the same exponential growth (generation time g = 30 min, N0 = 1e3 cells per mL) on an arithmetic and
#    on a semilogarithmic axis: only the semilog plot shows a constant rate as a straight line.
# B: the four phases of the growth cycle, from a Monod model with a Baranyi-Roberts lag and first-order death
#    after starvation (wikibio.microbio.batch_growth; mu_max = 0.9 per h, lag 3 h, S0 = 1 g/L glucose,
#    death rate 0.1 per h). The viable count (CFU) falls in the death phase while the total count
#    (microscopic, or turbidity) stays nearly constant until the dead cells lyse (slow lysis, 0.02 per h).
# C: the lag depends on the history of the inoculum: the Baranyi physiological state q0 sets the lag
#    ln(1 + 1/q0) / mu_max. Exponential-phase cells into the same medium: no lag; stationary-phase cells:
#    a lag; heat-damaged cells, or a transfer from a rich to a poorer medium: a longer lag.
import math

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
fig = plt.figure(figsize=(13.5, 4.3))
gs = fig.add_gridspec(1, 4, width_ratios=[0.8, 0.8, 1.9, 1.35], wspace=0.55)

# ---- A: arithmetic versus semilogarithmic ---------------------------------------------------------
g, N0 = 0.5, 1e3
t = np.linspace(0, 5, 200)
N = N0 * 2 ** (t / g)
for k, (ylog, name) in enumerate(((False, "arithmetic"), (True, "semilogarithmic"))):
    ax = fig.add_subplot(gs[0, k])
    ax.plot(t, N if ylog else N / 1e6, color=charts.line("bacterium"), lw=2.0)
    ax.plot(np.arange(0, 5.01, 0.5), (N0 * 2 ** (np.arange(0, 5.01, 0.5) / g)) / (1 if ylog else 1e6), "o", ms=3.2,
            color=charts.line("bacterium"))
    if ylog:
        ax.set_yscale("log")
        charts.style_axes(ax, "time $t$ / h", "cells / mL$^{-1}$ (log scale)")
    else:
        charts.style_axes(ax, "time $t$ / h", "cells / (10$^6$ mL$^{-1}$)")
    charts.title(ax, ("A   " if k == 0 else "") + name)
    ax.set_xticks([0, 1, 2, 3, 4, 5])

# ---- B: the four phases ----------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 2])
mu, lag = 0.9, 3.0
q0 = 1 / (math.exp(mu * lag) - 1)
tt = np.linspace(0, 48, 900)
_, Nv, S = M.batch_growth(tt, mu_max=mu, Ks=0.01, Y=1.7e9, S0=1.0, N0=1e6, q0=q0, kd=0.1, tau_s=10.0)
rate = np.gradient(np.log(Nv), tt)
t_exp_end = tt[np.flatnonzero((tt > lag) & (rate < 0.1 * mu))[0]]
t_death = tt[np.flatnonzero((tt > t_exp_end) & (rate < -0.05))[0]]
# total count: cells made never disappear except by slow lysis of dead cells
dead = np.maximum.accumulate(Nv) - Nv
lysed = np.zeros_like(dead)
for i in range(1, len(tt)):
    dt = tt[i] - tt[i - 1]
    lysed[i] = lysed[i - 1] + 0.02 * max(dead[i - 1] - lysed[i - 1], 0) * dt
Ntot = Nv + dead - lysed
phases = [(0, lag, "lag", "neutral"), (lag, t_exp_end, "exponential", "positive"),
          (t_exp_end, t_death, "stationary", "highlight"), (t_death, 48, "death", "negative")]
for a, b, name, tok in phases:
    ax.axvspan(a, b, color=P.mix(P.fill(tok), P.surface(), 0.8 if not P.is_dark() else 0.88), lw=0, zorder=0)
for k, (a, b, name, tok) in enumerate(phases):
    ax.text((a + b) / 2 if name != "lag" else b + 0.3, 1.2e10 if k % 2 == 0 else 5e9, name,
            ha="center" if name != "lag" else "left", va="center", fontsize=7.3, color=charts.line(tok), weight="bold")
ax.plot(tt, Ntot, color=charts.line("neutral"), lw=1.5, ls="--", label="total count")
ax.plot(tt, Nv, color=charts.line("bacterium"), lw=2.2, label="viable count (CFU)")
ax.set_yscale("log")
ax.set_ylim(3e5, 3e10)
ax.set_xlim(0, 48)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "time $t$ / h", "cells / mL$^{-1}$")
charts.title(ax, "B   The growth cycle of a batch culture")

# ---- C: the lag depends on the inoculum ------------------------------------------------------------
ax = fig.add_subplot(gs[0, 3])
cases = [("exponential-phase inoculum", 50.0, "positive"),
         ("stationary-phase inoculum", q0, "highlight"),
         ("damaged cells or poorer medium", 1 / (math.exp(mu * 5.0) - 1), "negative")]
t2 = np.linspace(0, 18, 400)
for name, q, tok in cases:
    _, n, _ = M.batch_growth(t2, mu_max=mu, Ks=0.01, Y=1.7e9, S0=2.0, N0=1e5, q0=q, kd=0.0, tau_s=10.0)
    lam = M.lag_time(mu, q)
    ax.plot(t2, n, color=charts.line(tok), lw=1.9, label=f"{name}\n  lag {lam:.1f} h")
ax.set_yscale("log")
ax.set_ylim(1e3, 1e10)
ax.legend(fontsize=6.8, frameon=False, loc="lower right")
charts.style_axes(ax, "time $t$ / h", "cells / mL$^{-1}$")
charts.title(ax, "C   The lag depends on the inoculum")
