# Thermodynamics of an RNA hairpin in the nearest-neighbour model.
# Example: 5'-GGAC(UUCG)GUCC-3', a four-base-pair stem closed by the UUCG tetraloop.
# Stacking free energies at 37 C and enthalpies of Watson-Crick nearest neighbours (Turner 2004 set,
# kcal/mol): GG/CC -3.26 (dH -13.39), GA/CU -2.35 (-12.44), AC/UG = GU/CA -2.24 (-11.40).
# The loop is given a single approximate free-energy cost of +4.5 kcal/mol (initiation of a four-nucleotide
# loop less the favourable terminal mismatch and tetraloop bonus) and no enthalpy.
# A: the free-energy budget at 37 C. B: two-state melting curves at three Na+ concentrations.
# C: the melting temperature is linear in ln[Na+]: dTm/dln[Na+] = (R Tm^2 / dH) dn, with dn = 0.6 counterions
#    released on unfolding (a value chosen to give about 8 C per decade, typical of small hairpins).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R = 1.987e-3  # kcal/mol/K
stacks = [("GG/CC", -3.26, -13.39), ("GA/CU", -2.35, -12.44), ("AC/UG", -2.24, -11.40)]
loop = ("UUCG loop", 4.5, 0.0)
terms = stacks + [loop]
dG37 = sum(t[1] for t in terms)
dH = sum(t[2] for t in terms)
T37 = 310.15
dS = (dH - dG37) / T37
Tm1 = dH / dS          # at 1 M Na+ (the reference state of the parameters)
dn = 0.6

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1), gridspec_kw={"width_ratios": [1.1, 1, 1]})
ax = axs[0]
run = 0.0
for i, (name, g, _) in enumerate(terms):
    tok = "rna" if g < 0 else "negative"
    ax.bar(i, g, bottom=run, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, width=0.6)
    ax.text(i, run + g + (-0.35 if g < 0 else 0.25), f"{g:+.2f}", ha="center", fontsize=7.5, color=P.ink())
    run += g
ax.bar(len(terms), dG37, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, width=0.6)
ax.text(len(terms), dG37 - 0.35, f"{dG37:+.2f}", ha="center", fontsize=7.5, color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xticks(range(len(terms) + 1))
ax.set_xticklabels([t[0] for t in terms] + ["hairpin"], fontsize=7.5)
ax.set_ylim(-9.5, 1.5)
charts.style_axes(ax, None, "ΔG°₃₇ / (kcal mol⁻¹)")
charts.title(ax, "A   5′-GGAC(UUCG)GUCC-3′: free-energy budget")

T = np.linspace(20, 100, 400) + 273.15
cols = {0.01: "dna", 0.1: "neutral", 1.0: "rna"}
for na, tok in cols.items():
    Tm = 1 / (1 / Tm1 - R * dn * np.log(na) / (-dH))   # shift of Tm with ln[Na+]
    dSn = dH / Tm
    dG = dH - T * dSn
    frac = 1 / (1 + np.exp(dG / (R * T)))         # fraction folded, unimolecular
    axs[1].plot(T - 273.15, frac, color=charts.line(tok), lw=1.8, label=f"{na * 1000:g} mM Na⁺,  T_m = {Tm - 273.15:.0f} °C")
charts.style_axes(axs[1], "temperature / °C", "fraction folded")
axs[1].legend(fontsize=7.5, frameon=False, loc="lower left")
charts.title(axs[1], "B   Two-state melting")

na = np.logspace(-3, 0, 50)
Tm = 1 / (1 / Tm1 - R * dn * np.log(na) / (-dH))
axs[2].semilogx(na * 1000, Tm - 273.15, color=charts.line("rna"), lw=1.8)
slope = (Tm[-1] - Tm[0]) / 3
axs[2].text(1.5, Tm[-1] - 273.15 - 1.5, f"≈ {slope:.0f} °C per tenfold [Na⁺]", fontsize=8, color=P.ink())
charts.style_axes(axs[2], "[Na⁺] / mM", "melting temperature / °C")
charts.title(axs[2], "C   Counterions stabilize the hairpin")
fig.tight_layout()
