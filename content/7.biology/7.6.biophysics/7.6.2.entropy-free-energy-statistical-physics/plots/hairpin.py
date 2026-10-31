# Energy against entropy in N independent RNA hairpins. Each hairpin is closed (energy 0, one conformation) or
# open (energy dh higher, with g open conformations, internal entropy ds = kB ln g). Illustrative values per mole
# of hairpins: dh = 200 kJ/mol, ds = 606 J/(mol K), so the melting temperature Tm = dh/ds = 330 K (57 C).
# A: fraction open against temperature, f = 1/(1 + exp[(dh - T ds)/RT]) (solid). Dashed: the model with
#    g = 1 (opening costs energy but gains no conformational entropy), f = 1/(1 + exp(dh/RT)): the mixing
#    entropy of which hairpins are open alone cannot melt the hairpins, f never exceeds 1/2.
# B: free energy per hairpin F(x)/N = x (dh - T ds) + RT [x ln x + (1 - x) ln(1 - x)] (in units of RT) as a
#    function of the open fraction x, below, at and above Tm; the minimum (dots) is the equilibrium fraction.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314462618
DH, DS = 200e3, 606.0
Tm = DH / DS

fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.8))
ax = axs[0]
T = np.linspace(280, 380, 400)
f = 1 / (1 + np.exp((DH - T * DS) / (R * T)))
ax.plot(T - 273.15, f, color=charts.line("rna"), lw=1.9, label="open state has entropy (g = e^(Δs/k))")
f1 = 1 / (1 + np.exp(DH / (R * T)))
ax.plot(T - 273.15, f1 + 0.002, color=charts.line("neutral"), lw=1.4, ls=(0, (5, 2.5)), label="g = 1: f < 10⁻³⁰")
ax.axvline(Tm - 273.15, color=P.muted(), lw=0.8, ls=":")
ax.text(Tm - 273.15 + 1.5, 0.08, f"Tm = {Tm - 273.15:.0f} °C", fontsize=7, color=P.muted())
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(T[0] - 273.15, T[-1] - 273.15)
ax.set_ylim(-0.02, 1.02)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "temperature / °C", "fraction of hairpins open")
ax.set_title("A   Melting curve", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
x = np.linspace(1e-4, 1 - 1e-4, 500)
for TT, tok in ((Tm - 8, "dna"), (Tm, "neutral"), (Tm + 8, "negative")):
    g = DH - TT * DS
    F = x * g / (R * TT) + x * np.log(x) + (1 - x) * np.log(1 - x)
    ax.plot(x, F, color=charts.line(tok), lw=1.7, label=f"T = {TT - 273.15:.0f} °C")
    xs = 1 / (1 + np.exp(g / (R * TT)))
    ax.plot([xs], [xs * g / (R * TT) + xs * np.log(xs) + (1 - xs) * np.log(1 - xs)], "o", color=charts.line(tok), ms=5)
ax.set_xlim(0, 1)
ax.set_ylim(-3.5, 3.5)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.legend(fontsize=7, frameon=False, loc="upper center")
charts.style_axes(ax, "open fraction x", "F / (N RT)")
ax.set_title("B   Free energy of the macrostates", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
