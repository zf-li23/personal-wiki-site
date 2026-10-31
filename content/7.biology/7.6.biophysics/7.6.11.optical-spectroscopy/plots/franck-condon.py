# Franck-Condon progressions of a displaced harmonic oscillator.
# A: ground and excited potential curves (same curvature, excited minimum displaced by Delta), vibrational
#    levels, the ground-state v = 0 wavefunction and the vertical (Franck-Condon) absorption and emission.
# B: Franck-Condon factors |<0|v'>|^2 = exp(-S) S^v' / v'! for Huang-Rhys factors S = 0.3, 1 and 3.
# C: absorption and emission spectra built from the same progression (S = 1, vibrational quantum
#    1400 cm^-1, Gaussian width 450 cm^-1, 0-0 transition at 28000 cm^-1): mirror images about the 0-0 line;
#    the separation of the maxima, the Stokes shift, approaches 2 S hbar omega for S >> 1.
import matplotlib.pyplot as plt
import numpy as np
from math import factorial
from numpy.polynomial.hermite import hermval

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.3), gridspec_kw={"width_ratios": [1.15, 0.9, 1.25]})

# A potentials
ax = axs[0]
q = np.linspace(-3.2, 5.2, 400)
D, gap = 2.0, 9.0
Vg = 0.5 * q**2
Ve = gap + 0.5 * (q - D) ** 2
cg, ce = charts.line("dna"), charts.line("rna")
ax.plot(q, np.where(Vg < 8.5, Vg, np.nan), color=cg, lw=1.8)
ax.plot(q, np.where(Ve < gap + 8.5, Ve, np.nan), color=ce, lw=1.8)
for v in range(6):
    E = v + 0.5
    xx = np.sqrt(2 * E)
    ax.plot([-xx, xx], [E, E], color=cg, lw=0.6)
    ax.plot([D - xx, D + xx], [gap + E, gap + E], color=ce, lw=0.6)
psi0 = np.exp(-q**2 / 2)
ax.fill_between(q, 0.5, 0.5 + 1.2 * psi0**2, color=P.light("dna"), alpha=0.8, lw=0)
ax.annotate("", xy=(0, gap + 0.5 * D**2 + 0.3), xytext=(0, 0.5), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.3))
ax.annotate("", xy=(D, 0.5 * D**2 + 0.3), xytext=(D, gap + 0.5), arrowprops=dict(arrowstyle="-|>", color=charts.line("positive"), lw=1.3))
ax.text(-0.15, 6.0, "absorption", rotation=90, ha="right", va="center", fontsize=8, color=ink)
ax.text(D + 0.15, 6.0, "emission", rotation=90, ha="left", va="center", fontsize=8, color=charts.line("positive"))
ax.annotate("", xy=(D, -0.6), xytext=(0, -0.6), arrowprops=dict(arrowstyle="<->", color=muted, lw=0.8))
ax.text(D / 2, -1.1, "Δ", ha="center", fontsize=9, color=ink)
ax.text(4.6, 1.5, "S0", color=cg, fontsize=9)
ax.text(4.6, gap + 2.2, "S1", color=ce, fontsize=9)
ax.set_xlim(-3.4, 5.4)
ax.set_ylim(-1.6, 17.5)
ax.set_xticks([])
ax.set_yticks([])
charts.style_axes(ax, "nuclear coordinate Q", "energy")
charts.title(ax, "A   Vertical transitions")

# B FC factors
ax = axs[1]
cols = ("dna", "protein", "rna")
for k, (S, tok) in enumerate(zip((0.3, 1.0, 3.0), cols)):
    v = np.arange(0, 10)
    fc = np.exp(-S) * S**v / np.array([factorial(int(n)) for n in v])
    ax.bar(v + (k - 1) * 0.27, fc, width=0.26, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, label=f"S = {S}")
ax.set_xticks(range(10))
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, "final vibrational level v'", "Franck-Condon factor")
charts.title(ax, "B   Poisson progressions")

# C spectra
ax = axs[2]
nu = np.linspace(20000, 36000, 1200)
S, w, nu00, sig = 1.0, 1400.0, 28000.0, 450.0
absn = np.zeros_like(nu)
emis = np.zeros_like(nu)
for v in range(12):
    fc = np.exp(-S) * S**v / factorial(v)
    absn += fc * np.exp(-((nu - (nu00 + v * w)) ** 2) / (2 * sig**2))
    emis += fc * np.exp(-((nu - (nu00 - v * w)) ** 2) / (2 * sig**2))
absn /= absn.max()
emis /= emis.max()
ax.plot(nu / 1e3, absn, color=cg, lw=1.8, label="absorption")
ax.plot(nu / 1e3, emis, color=charts.line("positive"), lw=1.8, label="emission")
ax.axvline(nu00 / 1e3, color=muted, lw=0.7, ls=":")
ax.text(nu00 / 1e3 + 0.15, 0.3, "0-0", fontsize=8, color=muted)
ia, ie = nu[np.argmax(absn)], nu[np.argmax(emis)]
ax.annotate("", xy=(ia / 1e3, 1.06), xytext=(ie / 1e3, 1.06), arrowprops=dict(arrowstyle="<->", color=ink, lw=0.8))
ax.text(20.3, 0.9, f"Stokes shift\n{ia - ie:.0f} cm⁻¹\n(2Sħω = 2800)", ha="left", fontsize=8, color=ink)
ax.set_ylim(0, 1.15)
ax.legend(fontsize=8, frameon=False, loc="center right")
charts.style_axes(ax, "wavenumber / (10³ cm⁻¹)", "normalized intensity")
charts.title(ax, "C   Mirror image and Stokes shift (S = 1)")
fig.tight_layout()
