"""Can parasites regulate their hosts? (Section 28.4)
A: microparasite with recovery to susceptibility (Proposition 28.4.1): host birth rate b = 1, death
rate d = 0.5 (r = 0.5), transmission beta = 0.01, recovery gamma = 0.5. Total host numbers for
virulence alpha = 0.3 < r (unregulated: hosts grow at rate r - alpha) and alpha = 1, 2 > r
(regulated at N* = N_T alpha / (alpha - r), dotted). Log scale.
B: the regulated host density N* and the equilibrium prevalence r/alpha against virulence:
regulation needs alpha > r; host density is lowest at intermediate virulence.
C: macroparasite model (Proposition 28.4.2) with r = 0.5, alpha = 0.1, lambda = 10, H0 = 10,
mu + b = 2: host numbers for aggregation k = 0.5 and k = 5 (damped to a stable equilibrium) and
for random distribution of worms (k very large: neutral, persistent oscillations).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
b, d, beta, gam = 1.0, 0.5, 0.01, 0.5
r = b - d
cols = [C.line("negative"), C.line("dna"), C.line("positive")]

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
for al, col in zip([0.3, 1.0, 2.0], cols):
    f = lambda t, z: [b * (z[0] + z[1]) - d * z[0] - beta * z[0] * z[1] + gam * z[1],
                      beta * z[0] * z[1] - (al + d + gam) * z[1]]
    s = solve_ivp(f, [0, 60], [100, 1], method="LSODA", rtol=1e-9, dense_output=True)
    t = np.linspace(0, 60, 600)
    ax.semilogy(t, s.sol(t).sum(0), color=col, lw=1.4, label=f"α = {al:g}")
    if al > r:
        ax.axhline((al + d + gam) / beta * al / (al - r), color=col, lw=0.7, ls=(0, (1, 2)))
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper left")
ax.set_ylim(50, 1e5)
C.style_axes(ax, "Time", "Host population N (log scale)")
C.title(ax, "A  Regulation requires α > r")

ax = axes[1]
al = np.linspace(0.52, 6, 300)
Nstar = (al + d + gam) / beta * al / (al - r)
ax.plot(al, Nstar, color=C.line("dna"), lw=1.5, label="host density N*")
ax.set_ylim(0, 1500)
ax.axvline(r, color=P.muted(), lw=0.8)
ax.text(r + 0.08, 1400, "α = r", fontsize=FS["tiny"], color=P.muted(), va="top")
C.style_axes(ax, "Virulence α", "Equilibrium host density N*")
ax2 = ax.twinx()
ax2.plot(al, r / al, color=C.line("negative"), lw=1.3, ls=(0, (4, 2)), label="prevalence I*/N* = r/α")
ax2.set_ylim(0, 1)
C.style_axes(ax2, None, "Prevalence")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=FS["tiny"], frameon=False, loc="upper right")
C.title(ax, "B  Host suppression and virulence")

ax = axes[2]
rr, a2, lam, H0, mb = 0.5, 0.1, 10.0, 10.0, 2.0
for k, col, lab in [(0.5, cols[0], "k = 0.5"), (5.0, cols[1], "k = 5"), (1e6, P.muted(), "random (k → ∞)")]:
    f = lambda t, z: [z[0] * (rr - a2 * z[1]), z[1] * (lam * z[0] / (H0 + z[0]) - (mb + a2)) - (a2 / k) * z[1] ** 2]
    s = solve_ivp(f, [0, 200], [50, 3], method="LSODA", rtol=1e-9, atol=1e-10, dense_output=True)
    t = np.linspace(0, 200, 2000)
    ax.semilogy(t, s.sol(t)[0], color=col, lw=1.3, label=lab)
ax.set_ylim(1e-3, 3e3)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right", ncol=3)
C.style_axes(ax, "Time", "Hosts H (log scale)")
C.title(ax, "C  Aggregated worms stabilize")
fig.tight_layout()
