# A three-state model of kinesin-1 (Formula 27.3.4): state 0 waits for ATP; ATP binds at k_on [ATP] e^{-F d0/kBT}
# (reversible, k_off); from the ATP state the motor commits to a forward step (k1 e^{-F d1/kBT}) or, rarely, to an
# ATP-driven backward step (kb e^{+F db/kBT}); the stepped state returns to state 0 at k2 (hydrolysis and
# phosphate release, load-independent). a = 8.2 nm, k_on = 1.5 /(uM s), k_off = 10 /s, k1 = k2 = 200 /s,
# kb = k1/800, d0 = 0.8 nm, d1 = 1.2 nm, db = 2.6 nm, kBT = 4.1 pN nm. Free energy per ATP 25 kBT (for B).
# A: force-velocity curves at 2 mM and 5 uM ATP; the stall force (k1 = kb) does not depend on ATP.
# B: efficiency F V / (dmu x ATP turnover) at 2 mM: zero without load and at stall, maximal in between.
# C: velocity against [ATP] at three loads (Michaelis-Menten). D: Vmax falls and K_M rises with load.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
kT, a = 4.1, 8.2
kon, koff, k10, k2 = 1.5, 10.0, 200.0, 200.0
kb0, d0, d1, db = k10 / 800, 0.8, 1.2, 2.6


def rates(F, atp):
    return kon * atp * np.exp(-d0 * F / kT), koff, k10 * np.exp(-d1 * F / kT), kb0 * np.exp(db * F / kT)


def occupancy(F, atp):
    u0, ko, k1, kb = rates(F, atp)
    p1 = 1 / ((ko + k1 + kb) / u0 + 1 + (k1 + kb) / k2)
    return p1, k1, kb


def velocity(F, atp):
    p1, k1, kb = occupancy(F, atp)
    return a * p1 * (k1 - kb)


def turnover(F, atp):
    p1, k1, kb = occupancy(F, atp)
    return p1 * (k1 + kb)


Fs = kT * np.log(k10 / kb0) / (d1 + db)
F = np.linspace(0, 8, 400)
fig, axs = plt.subplots(2, 2, figsize=(10, 7))
ax = axs[0, 0]
for atp, tok, lab in ((2000, "enzyme", "2 mM ATP"), (5, "dna", "5 µM ATP (×10)")):
    sc = 1 if atp > 100 else 10
    ax.plot(F, sc * velocity(F, atp), color=charts.line(tok), lw=1.8, label=lab)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(Fs, color=P.muted(), lw=0.8, ls="--")
ax.text(Fs + 0.1, 650, f"stall {Fs:.1f} pN\n(both [ATP])", fontsize=7.5, color=P.ink())
ax.set_ylim(-150, 900)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "load $F$ / pN", "$V$ / (nm s$^{-1}$)")
charts.title(ax, "A   Force–velocity relation")

ax = axs[0, 1]
Fe = np.linspace(0, Fs, 300)
eta = Fe * velocity(Fe, 2000) / (25 * kT * turnover(Fe, 2000))
ax.plot(Fe, eta, color=charts.line("enzyme"), lw=1.8, label="model, 2 mM ATP")
ax.plot(Fe, Fe * a / (25 * kT), color=P.muted(), lw=0.9, ls="--", label="tight coupling, $Fa/\\Delta\\mu$")
ax.set_ylim(0, 0.65)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "load $F$ / pN", "efficiency $\\eta$")
charts.title(ax, "B   Backward steps waste ATP near stall")

ax = axs[1, 0]
A = np.logspace(0, 4, 300)
for Fl, tok in ((1.05, "enzyme"), (3.59, "dna"), (5.63, "rna")):
    ax.semilogx(A, velocity(Fl, A), color=charts.line(tok), lw=1.8, label=f"{Fl} pN")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "[ATP] / µM", "$V$ / (nm s$^{-1}$)")
charts.title(ax, "C   Michaelis–Menten at each load")

ax = axs[1, 1]
Fk = np.linspace(0, 6.5, 200)
vmax = velocity(Fk, 1e9)
u0, ko, k1, kb = rates(Fk, 1.0)
KM = (ko + k1 + kb) / u0 / (1 + (k1 + kb) / k2)
ax.plot(Fk, vmax / vmax[0], color=charts.line("enzyme"), lw=1.8, label="$V_\\max(F)/V_\\max(0)$")
ax.plot(Fk, KM / KM[0], color=charts.line("rna"), lw=1.8, label="$K_\\mathrm{M}(F)/K_\\mathrm{M}(0)$")
ax.text(0.2, 1.48, f"$V_\\max(0)$ = {vmax[0]:.0f} nm/s, $K_\\mathrm{{M}}(0)$ = {KM[0]:.0f} µM", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 1.6)
ax.legend(fontsize=7.5, frameon=False, loc="center left")
charts.style_axes(ax, "load $F$ / pN", "relative value")
charts.title(ax, "D   Load lowers $V_\\max$ and raises $K_\\mathrm{M}$")
fig.tight_layout()
