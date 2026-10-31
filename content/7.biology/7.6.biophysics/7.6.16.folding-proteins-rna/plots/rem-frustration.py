# The random-energy model of a heteropolymer and the principle of minimal frustration
# (Bryngelson and Wolynes 1987; Goldstein, Luthey-Schulten and Wolynes 1992). Units kB = 1.
# Misfolded (non-native) states: exp(S0) states with Gaussian energies of mean 0 and width dE.
# Microcanonical entropy S(E) = S0 - E^2 / (2 dE^2); it vanishes at E_min = -dE sqrt(2 S0).
# Free energy of the misfolded ensemble F_M(T) = -dE^2/(2T) - T S0 above the glass temperature
# T_g = dE / sqrt(2 S0) and F_M = E_min below it (the ensemble freezes into a few low-energy traps).
# The native state is one state of energy E_N below the band; it is stable below T_f, where F_M(T_f) = E_N.
# A: the density of states (log scale) with the isolated native level. B: F(T) of the two ensembles:
#    T_f > T_g, so the chain folds before it can freeze into a trap. C: T_f / T_g against the stability gap
#    E_min - E_N: a large gap relative to the roughness dE (a minimally frustrated sequence) is required.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
S0, dE = 40.0, 10.0           # conformational entropy (ln of ~2e17 states), energy roughness
Tg = dE / np.sqrt(2 * S0)
Emin = -dE * np.sqrt(2 * S0)
EN = -110.0                   # native energy


def F_mis(T):
    T = np.asarray(T, float)
    return np.where(T > Tg, -dE**2 / (2 * T) - T * S0, Emin)


def T_fold(EN):
    # largest root of -dE^2/(2T) - T S0 = EN above Tg
    a, b, c = S0, EN, dE**2 / 2       # S0 T^2 + EN T + dE^2/2 = 0
    disc = b * b - 4 * a * c
    return (-b + np.sqrt(disc)) / (2 * a) if disc >= 0 else np.nan


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
E = np.linspace(Emin, -Emin, 400)
lnn = S0 - E**2 / (2 * dE**2)
axs[0].fill_betweenx(E, 0, lnn, color=P.fill("protein"), alpha=0.6, lw=0)
axs[0].plot(lnn, E, color=charts.line("protein"), lw=1.6)
axs[0].plot([0, 3], [EN, EN], color=charts.line("negative"), lw=2.5)
axs[0].text(3.5, EN, "native state", va="center", fontsize=8, color=P.ink())
axs[0].annotate("", xy=(6, Emin), xytext=(6, EN), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
axs[0].text(7, (Emin + EN) / 2, "stability gap", va="center", fontsize=7.5, color=P.muted())
axs[0].text(22, 15, "misfolded\nensemble", fontsize=8, color=P.ink())
axs[0].set_xlim(0, 44)
axs[0].set_ylim(EN - 12, 95)
charts.style_axes(axs[0], "ln (number of states)", "energy (arbitrary units)")
charts.title(axs[0], "A   Density of states (S₀ = 40, ΔE = 10)")

T = np.linspace(0.3, 3.2, 400)
Tf = T_fold(EN)
axs[1].plot(T, F_mis(T), color=charts.line("protein"), lw=1.8, label="misfolded ensemble F_M(T)")
axs[1].axhline(EN, color=charts.line("negative"), lw=1.8, label="native state E_N")
for x, txt in ((Tg, "T_g"), (Tf, "T_f")):
    axs[1].axvline(x, color=P.muted(), lw=0.7, ls=":")
    axs[1].text(x + 0.04, -40, txt, fontsize=8.5, color=P.ink())
axs[1].set_ylim(-200, -30)
charts.style_axes(axs[1], "kB T (same units as energy)", "free energy")
axs[1].legend(fontsize=7.5, frameon=False, loc="lower left")
charts.title(axs[1], f"B   Folding before freezing: T_f/T_g = {Tf / Tg:.2f}")

gaps = np.linspace(0, 60, 200)
ratio = np.array([T_fold(Emin - g) for g in gaps]) / Tg
axs[2].plot(gaps / dE, ratio, color=charts.line("dna"), lw=1.8)
axs[2].axhline(1, color=P.muted(), lw=0.7, ls=":")
axs[2].plot([(Emin - EN) / dE], [Tf / Tg], "o", color=charts.line("negative"), ms=5)
axs[2].text(0.15, 1.08, "no gap: folding and freezing coincide", fontsize=7.5, color=P.muted())
charts.style_axes(axs[2], "stability gap / roughness  (E_min − E_N)/ΔE", "T_f / T_g")
charts.title(axs[2], "C   Minimal frustration: gap over roughness")
fig.tight_layout()
