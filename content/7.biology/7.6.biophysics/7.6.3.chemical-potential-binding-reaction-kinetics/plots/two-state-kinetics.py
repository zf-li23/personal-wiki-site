# Kinetics of a two-state reaction S <-> P with rate constants k+ (S to P) and k- (P to S).
# A: a free-energy profile along a reaction coordinate (schematic double well): P lies dG = -2 kBT below S, the
#    barrier is dG_dagger = 12 kBT above S; detailed balance fixes k+/k- = exp(-dG/kBT) whatever the barrier.
# B: relaxation of the fraction x = [P]/C from x = 0 (solid) and from x = 1 (dashed), dx/dt = k+(1 - x) - k- x,
#    for k+ = 0.88 and k- = 0.12 per unit time (time in units of 1/(k+ + k-)): both approach x_eq = 0.88 with the
#    same time constant tau = 1/(k+ + k-).
# C: Eyring rate k = (kBT/h) exp(-dG_dagger/kBT) at 310 K against the barrier, with the corresponding mean waiting
#    times 1/k marked; kBT/h = 6.5e12 per second.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.7))

ax = axs[0]
xi = np.linspace(-1.45, 1.45, 400)
# tilted double well a (xi^2 - 1)^2 - xi: minima near -1 (S) and +1 (P), barrier near 0
G = 13 * (xi ** 2 - 1) ** 2 - xi
iS = np.argmin(np.where(xi < 0, G, np.inf))
G = G - G[iS]
ax.plot(xi, G, color=charts.line("protein"), lw=1.9)
gS = G[iS]
gP = np.min(np.where(xi > 0, G, np.inf))
gT = G[np.abs(xi) < 0.5].max()
ax.axhline(gS, color=P.muted(), lw=0.6, ls=":")
ax.annotate("", (-0.95, gT), (-0.95, gS), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
ax.text(-0.9, (gS + gT) / 2, f"ΔG‡ ≈ {gT - gS:.0f} kBT", fontsize=7, color=P.ink())
ax.annotate("", (1.25, gP), (1.25, gS), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
ax.text(1.3, (gS + gP) / 2, f"ΔG ≈ {gP - gS:.0f} kBT", fontsize=7, color=P.ink(), va="center")
ax.text(-1.0, gS - 1.6, "S", fontsize=9, color=P.ink(), ha="center")
ax.text(1.0, gP - 1.6, "P", fontsize=9, color=P.ink(), ha="center")
ax.text(0.05, gT + 0.6, "transition state", fontsize=7, color=P.ink(), ha="center")
ax.set_ylim(gP - 3, gT + 2.5)
ax.set_xlim(-1.6, 1.75)
ax.set_xticks([])
charts.style_axes(ax, "reaction coordinate", "G / kBT")
ax.set_title("A   Free-energy profile", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
kp, km = 0.88, 0.12
t = np.linspace(0, 5, 300)
xe = kp / (kp + km)
ax.plot(t, xe * (1 - np.exp(-(kp + km) * t)), color=charts.line("dna"), lw=1.9, label="from x = 0")
ax.plot(t, xe + (1 - xe) * np.exp(-(kp + km) * t), color=charts.line("negative"), lw=1.6, ls=(0, (5, 2.5)),
        label="from x = 1")
ax.axhline(xe, color=P.muted(), lw=0.7, ls=":")
ax.axvline(1, color=P.muted(), lw=0.7, ls=":")
ax.text(1.05, 0.12, "t = τ", fontsize=7, color=P.muted())
ax.text(3.2, xe - 0.08, "x_eq = k₊/(k₊ + k₋)", fontsize=7, color=P.ink())
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "t / τ,  τ = 1/(k₊ + k₋)", "fraction in P,  x")
ax.set_title("B   Relaxation to equilibrium", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
kT_h = 1.380649e-23 * 310 / 6.62607015e-34
dg = np.linspace(0, 52, 300)
ax.semilogy(dg, kT_h * np.exp(-dg), color=charts.line("protein"), lw=1.9)
for tau, txt in ((1e-9, "1 ns"), (1e-6, "1 µs"), (1e-3, "1 ms"), (1.0, "1 s"), (3600.0, "1 h"), (8.64e4 * 365, "1 yr")):
    g = np.log(kT_h * tau)
    ax.plot([g], [1 / tau], "o", color=charts.line("protein"), ms=4)
    ax.text(g + 1.0, 1 / tau * 1.8, txt, fontsize=6.8, color=P.ink())
ax.set_xlim(0, 52)
ax.set_ylim(1e-10, 1e14)
charts.style_axes(ax, "barrier ΔG‡ / kBT", "rate k / s⁻¹")
ax.set_title("C   Eyring rate at 310 K", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
