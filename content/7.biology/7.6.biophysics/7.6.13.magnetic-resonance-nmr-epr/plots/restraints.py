# Geometric restraints from NMR and EPR.
# A: Karplus relation for the backbone three-bond coupling 3J(HN, HA) as a function of phi, with the parameters
#    of Vuister and Bax (1993): 3J = 6.51 cos^2(theta) - 1.76 cos(theta) + 1.60 Hz, theta = phi - 60 deg.
#    Typical phi of the alpha helix (-57 deg) and of the antiparallel beta sheet (-139 deg) are marked.
# B: residual dipolar coupling of a 1H-15N bond (r = 1.02 A) as a function of the angle theta between the bond
#    and the principal axis of an axially symmetric alignment, D = D_a (3 cos^2(theta) - 1) with an alignment
#    of D_a = 10 Hz: positive along the axis because gamma_N < 0, zero at the magic angle 54.7 deg.
# C: approximate distance ranges of the restraints and their distance laws: 1H-1H NOE (r^-6, to about 0.5 nm),
#    paramagnetic relaxation enhancement by a nitroxide (r^-6 but (gamma_e/gamma_H)^2 = 4.3e5 times stronger),
#    pseudocontact shift of a lanthanide (r^-3), dipolar broadening of cw-EPR spectra, DEER (dipolar frequency
#    52.04 MHz nm^3 / r^3; 1.8-6 nm, up to about 10 nm with deuteration) and, for comparison, FRET.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

ax = axs[0]
phi = np.linspace(-180, 180, 721)
th = np.radians(phi - 60)
j = 6.51 * np.cos(th) ** 2 - 1.76 * np.cos(th) + 1.60
ax.plot(phi, j, color=charts.line("protein"), lw=2.0)
for p, name, tok in ((-57, "α helix ≈ 4 Hz", "rna"), (-139, "β sheet ≈ 9 Hz", "enzyme")):
    jj = 6.51 * np.cos(np.radians(p - 60)) ** 2 - 1.76 * np.cos(np.radians(p - 60)) + 1.60
    ax.plot(p, jj, "o", color=charts.line(tok), ms=6)
    ax.text(p + 8, jj + 0.4, name, fontsize=7.5, color=P.ink())
ax.axvspan(-180, 0, color=P.light("highlight"), lw=0)
ax.text(-170, 0.4, "φ < 0: most residues", fontsize=7.5, color=P.ink())
ax.set_xlim(-180, 180)
ax.set_xticks(range(-180, 181, 60))
ax.set_ylim(0, 11)
charts.style_axes(ax, "φ / degree", "³J(Hᴺ, Hᵅ) / Hz")
charts.title(ax, "A   Karplus relation")

ax = axs[1]
t = np.linspace(0, 90, 300)
D = 10 * (3 * np.cos(np.radians(t)) ** 2 - 1)
ax.plot(t, D, color=charts.line("dna"), lw=2.0)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(54.74, color=P.muted(), lw=0.7, ls=":")
ax.text(56, 12, "magic angle\n54.7°", fontsize=7.5, color=P.muted())
ax.set_xlim(0, 90)
ax.set_xticks(range(0, 91, 15))
charts.style_axes(ax, "θ (N–H bond vs alignment axis) / degree", "D(¹⁵N–¹H) / Hz")
charts.title(ax, "B   Residual dipolar coupling, Dₐ = 10 Hz")

ax = axs[2]
rows = (("NOE (¹H–¹H)", "r⁻⁶", 0.18, 0.5, "protein"),
        ("³J, RDC (bond geometry)", "angles", 0.1, 0.3, "neutral"),
        ("PRE (nitroxide–¹H)", "r⁻⁶", 1.0, 3.0, "rna"),
        ("PCS (lanthanide–¹H)", "r⁻³", 1.0, 4.0, "enzyme"),
        ("cw-EPR line broadening", "r⁻³", 0.8, 2.5, "atp"),
        ("DEER (e⁻–e⁻)", "r⁻³", 1.8, 6.0, "dna"),
        ("DEER, deuterated", "r⁻³", 6.0, 10.0, "dna2"),
        ("FRET (for comparison)", "r⁻⁶", 2.0, 10.0, "neutral"))
for k, (name, law, a, b, tok) in enumerate(rows):
    y = len(rows) - k
    ax.barh(y, b - a, left=a, height=0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.text(0.085, y, name, ha="right", va="center", fontsize=7.5, color=P.ink())
    ax.text(b * 1.08, y, law, ha="left", va="center", fontsize=7.5, color=P.muted())
ax.set_xscale("log")
ax.set_xlim(0.09, 20)
ax.set_ylim(0.4, len(rows) + 0.6)
ax.set_yticks([])
charts.style_axes(ax, "distance / nm", None)
charts.title(ax, "C   Distance ranges of the restraints")
fig.tight_layout()
