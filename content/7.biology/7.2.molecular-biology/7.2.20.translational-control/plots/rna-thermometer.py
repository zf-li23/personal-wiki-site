# An RNA thermometer: a hairpin that hides the ribosome-binding site melts with temperature.
# A: at 30 C the Shine-Dalgarno sequence (and the start codon) are paired in a stem, so the 30S subunit cannot
#    bind; at 42 C the stem melts and initiation proceeds (rpoH, encoding sigma32, in E. coli: its structure
#    involves the start region and sequences within the coding region; ROSE elements of rhizobial heat-shock
#    genes and the prfA leader of Listeria, a virulence switch at 37 C, are other examples).
# B: two-state melting of the hairpin, fraction open = 1/(1 + exp(dH/R (1/T - 1/Tm))) with Tm = 42 C (folded
#    when T < Tm; dH is the unfolding enthalpy), for dH = 150, 300 and 450 kJ/mol (illustrative values for
#    hairpins of increasing length); translation is taken as proportional to the open fraction. A larger dH
#    gives a sharper switch.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts
from wikibio import molbio as MB

P = bio.P
fig = plt.figure(figsize=(12.6, 4.2))
gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 13.6)
ax.set_ylim(0, 6.5)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A   Closed at 30 °C, open at 42 °C", loc="left", fontsize=9, color=P.ink())
dx = 0.3
# closed hairpin: stem of SD region paired with an anti-SD stretch
stem_l, stem_r = "AGGAGG", "CCUCCU"
x0, y0 = 1.0, 3.2
xs = MB.codons(ax, x0, y0, "UUU" + stem_l, dx=dx)
top = MB.codons(ax, x0 + 3 * dx, y0 + 0.8, stem_r[::-1], dx=dx)
for i in range(6):
    ax.plot([x0 + (3 + i) * dx] * 2, [y0 + 0.2, y0 + 0.6], color=P.muted(), lw=0.8)
loop = np.array([(x0 + 8.4 * dx, y0), (x0 + 9.6 * dx, y0 + 0.4), (x0 + 8.4 * dx, y0 + 0.8)])
ax.plot(loop[:, 0], loop[:, 1], color=P.edge("mrna"), lw=1.4)
ax.plot([x0 + 3 * dx - 0.2, x0 + 0.5], [y0 + 0.8, y0 + 1.75], color=P.edge("mrna"), lw=1.4)
MB.codons(ax, x0 - 0.6, y0 + 1.95, "AUGGCU", dx=dx)
bio.label(ax, (x0 + 1.8, y0 - 0.55), "SD paired in stem", size="tiny")
bio.label(ax, (x0 + 1.6, y0 + 2.6), "30 °C: no 30S binding", size="tiny", bold=True)
bio.arrow(ax, (5.0, 3.6), (6.6, 3.6), kind="process")
bio.label(ax, (5.8, 4.0), "heat", size="tiny", color=P.muted())
# open: linear mRNA with 30S bound
x1 = 7.0
lin = "UUU" + stem_l + "UAACAUAUGGCU"
xl = MB.codons(ax, x1, y0, lin, dx=dx)
small = bio.core.smooth_closed(np.array([(-0.5, 0.0), (-0.45, -0.7), (-0.15, -1.0), (0.2, -1.0), (0.48, -0.65), (0.5, 0.0)]) * [4.0, 1.6] + [xl[10], y0 - 0.3])
ax.add_patch(bio.core.PathPatch(bio.core.Path(small, closed=True), facecolor=P.light("rrna"), edgecolor=P.edge("rrna"), lw=1.0, zorder=4))
bio.label(ax, (xl[10], y0 - 1.15), "30S", size="small", color=P.on_fill())
bio.label(ax, (xl[10], y0 + 2.6), "42 °C: SD free, initiation", size="tiny", bold=True)

ax = fig.add_subplot(gs[1])
T = np.linspace(20, 55, 300)
R = 8.314e-3
Tm = 42 + 273.15
for dH, tok in ((150, "neutral"), (300, "rna"), (450, "negative")):
    f = 1 / (1 + np.exp(dH / R * (1 / (T + 273.15) - 1 / Tm)))
    ax.plot(T, f, color=charts.line(tok), lw=1.7, label=f"ΔH = {dH} kJ/mol")
for t in (30, 42):
    ax.axvline(t, color=P.muted(), lw=0.7, ls=":")
ax.set_xlim(20, 55)
ax.set_ylim(0, 1.03)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "temperature / °C", "fraction open (∝ translation)")
ax.set_title("B   Two-state melting", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
