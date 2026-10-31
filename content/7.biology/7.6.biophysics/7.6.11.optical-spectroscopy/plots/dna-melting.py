# Melting of DNA followed by absorbance at 260 nm, analyzed with the two-state model.
# A: A260(T) for an intramolecular (hairpin-like) two-state transition with Tm = 65 C and van 't Hoff
#    enthalpies 150, 300 and 600 kJ/mol; sloping baselines for duplex and single strands, 30 % hyperchromicity.
# B: fraction melted and its temperature derivative; the van 't Hoff enthalpy follows from the slope at Tm,
#    df/dT = dH / (4 R Tm^2), and from the width of the derivative peak.
# C: a bimolecular duplex (two complementary 12-mers; dissociation dH = 400 kJ/mol, dS = 1.10 kJ/(mol K)):
#    Tm rises with total strand concentration C_T as 1/Tm = (dS - R ln(C_T/4)) / dH (van 't Hoff plot inset).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314e-3
T = np.linspace(20, 100, 500)
Tk = T + 273.15
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
toks = ("dna2", "dna", "rna")
Tm = 65 + 273.15
for dH, tok in zip((150, 300, 600), toks):
    K = np.exp(-dH / R * (1 / Tk - 1 / Tm))
    f = K / (1 + K)
    Ads = 1.0 + 0.0008 * (T - 20)
    Ass = 1.30 + 0.0012 * (T - 20)
    A = Ads * (1 - f) + Ass * f
    axs[0].plot(T, A, color=charts.line(tok), lw=1.8, label=f"ΔH_vH = {dH} kJ/mol")
    axs[1].plot(T, f, color=charts.line(tok), lw=1.8)
    dfdT = np.gradient(f, T)
    axs[1].plot(T, dfdT / dfdT.max() * 0.0 + dfdT * 10, color=charts.line(tok), lw=1.0, ls="--")
axs[0].plot(T, 1.0 + 0.0008 * (T - 20), color=P.muted(), lw=0.8, ls=":")
axs[0].plot(T, 1.30 + 0.0012 * (T - 20), color=P.muted(), lw=0.8, ls=":")
axs[0].text(22, 1.34, "single strands", fontsize=8, color=P.muted())
axs[0].text(80, 1.0, "duplex", fontsize=8, color=P.muted())
axs[0].legend(fontsize=7.5, frameon=False, loc="center left")
charts.style_axes(axs[0], "temperature / °C", "A260 (relative)")
charts.title(axs[0], "A   Hyperchromic melting curves")
axs[1].axvline(65, color=P.muted(), lw=0.7, ls=":")
axs[1].text(23, 0.9, "solid: fraction melted f\ndashed: 10 × df/dT (K⁻¹)", fontsize=8, color=P.ink())
charts.style_axes(axs[1], "temperature / °C", "f,   10 df/dT")
charts.title(axs[1], "B   Width reports ΔH_vH")

ax = axs[2]
dH, dS = 400.0, 1.10
for CT, tok in zip((0.5e-6, 5e-6, 50e-6), toks):
    # fraction of strands in duplex for A + B <=> AB with [A]0 = [B]0 = CT/2
    Ka = np.exp((dH - Tk * dS) / (R * Tk))     # association constant; dH, dS are those of dissociation
    c = CT / 2
    single = 2 / (1 + np.sqrt(1 + 4 * Ka * c))  # fraction of strands not in duplex
    ax.plot(T, single, color=charts.line(tok), lw=1.8, label=f"C_T = {CT * 1e6:g} µM")
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "temperature / °C", "fraction single-stranded")
charts.title(ax, "C   Bimolecular duplex: Tm depends on C_T")
ins = ax.inset_axes([0.62, 0.5, 0.34, 0.34])
CTs = np.logspace(-7, -4, 20)
Tms = dH / (dS - R * np.log(CTs / 4))
ins.plot(np.log(CTs / 4), 1e3 / Tms, "o", ms=3, color=charts.line("dna"))
ins.set_xlabel("ln(C_T/4)", fontsize=7)
ins.set_ylabel("1000/Tm (K⁻¹)", fontsize=7)
ins.tick_params(labelsize=6)
fig.tight_layout()
