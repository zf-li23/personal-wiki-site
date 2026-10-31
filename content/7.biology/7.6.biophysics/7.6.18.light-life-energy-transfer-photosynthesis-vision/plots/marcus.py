# Marcus theory of non-adiabatic electron transfer.
# A: free-energy parabolas along a collective solvent/nuclear coordinate q (scaled so that the acceptor
#    minimum is at q = 1): G_D = lambda q^2 (electron on the donor), G_A = lambda (q - 1)^2 + dG0. The barrier
#    is the intersection, dG* = (dG0 + lambda)^2 / (4 lambda). Three driving forces: normal region
#    (-dG0 < lambda), activationless (-dG0 = lambda) and inverted (-dG0 > lambda); lambda = 0.5 eV.
# B: rate against driving force, k = (2 pi / hbar) |H|^2 (4 pi lambda kT)^(-1/2) exp[-(dG0 + lambda)^2 /
#    (4 lambda kT)], |H| = 1 meV, T = 298 K, for three reorganization energies. Dashed: the same with
#    lambda = 0.5 eV split into a classical solvent part (0.3 eV) and one quantized intramolecular mode
#    (h nu = 0.18 eV, lambda_v = 0.2 eV; Marcus-Levich-Jortner sum over vibrational quanta): nuclear tunneling
#    makes the inverted region much shallower. Markers: a forward step (-dG0 = 0.5 eV) and a charge
#    recombination (-dG0 = 1.2 eV) with the same coupling.
# C: temperature dependence for lambda = 0.5 eV (classical formula): only the activationless reaction is
#    nearly temperature independent (it even speeds up slightly on cooling, through the 1/sqrt(T) prefactor).
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gammaln

import wikibio as bio
from wikibio import charts

P = bio.P
hbar = 6.582119569e-16  # eV s
kB = 8.617333e-5        # eV / K
H = 1e-3


def k_cl(dG, lam, T=298.0):
    kT = kB * T
    return 2 * np.pi / hbar * H**2 / np.sqrt(4 * np.pi * lam * kT) * np.exp(-(dG + lam) ** 2 / (4 * lam * kT))


def k_mlj(dG, lam_s=0.3, lam_v=0.2, hw=0.18, T=298.0):
    kT = kB * T
    S = lam_v / hw
    tot = 0.0
    for n in range(40):
        fc = np.exp(-S + n * np.log(S) - gammaln(n + 1))
        tot = tot + fc * np.exp(-(dG + lam_s + n * hw) ** 2 / (4 * lam_s * kT))
    return 2 * np.pi / hbar * H**2 / np.sqrt(4 * np.pi * lam_s * kT) * tot


fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0), gridspec_kw=dict(width_ratios=[1.25, 1.1, 0.9]))
ax = axs[0]
lam = 0.5
q = np.linspace(-0.7, 2.3, 400)
ax.plot(q, lam * q**2, color=charts.line("dna"), lw=1.8)
ax.text(1.68, 1.12, "D (electron\non donor)", fontsize=7, color=charts.line("dna"))
cases = [(-0.2, "normal", "enzyme"), (-0.5, "activationless", "atp"), (-1.0, "inverted", "rna")]
for dG, name, tok in cases:
    ax.plot(q, lam * (q - 1) ** 2 + dG, color=charts.line(tok), lw=1.5)
    qs = (1 + dG / lam) / 2  # crossing point of the two parabolas
    Gs = lam * qs**2
    ax.plot(qs, Gs, "o", ms=4, color=charts.line(tok))
    ax.text(1.0, dG - 0.05, f"A, {name}: ΔG° = {dG:.1f} eV", fontsize=6.8, ha="center",
            va="top", color=charts.line(tok))
ax.annotate("", xy=(1.0, lam), xytext=(1.0, 0), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
ax.text(1.04, 0.2, "λ", fontsize=9, color=P.ink())
ax.set_xlim(-0.7, 2.3)
ax.set_ylim(-1.25, 1.3)
charts.style_axes(ax, "reaction coordinate q", "free energy / eV")
charts.title(ax, "A   Parabolas and the crossing point")

ax = axs[1]
x = np.linspace(0, 2.0, 400)
for lam, tok in ((0.25, "enzyme"), (0.5, "dna"), (1.0, "protein")):
    ax.plot(x, np.log10(k_cl(-x, lam)), color=charts.line(tok), lw=1.6, label=f"λ = {lam:g} eV")
ax.plot(x, np.log10(k_mlj(-x)), color=charts.line("dna"), lw=1.2, ls="--", label="λ = 0.5 eV with a quantum mode")
for xx, lab in ((0.5, "forward"), (1.2, "recombination")):
    ax.plot(xx, np.log10(k_cl(-xx, 0.5)), "o", ms=5, color=charts.line("rna"))
    ax.text(xx + 0.05, np.log10(k_cl(-xx, 0.5)) + 0.25, lab, fontsize=7, color=charts.line("rna"))
ax.set_ylim(2, 11.5)
ax.legend(fontsize=7, frameon=False, loc="lower center")
charts.style_axes(ax, "driving force −ΔG° / eV", "log₁₀ (k / s⁻¹)")
charts.title(ax, "B   The inverted region")

ax = axs[2]
T = np.linspace(80, 320, 200)
for dG, name, tok in cases:
    ax.plot(T, np.log10(k_cl(dG, 0.5, T)), color=charts.line(tok), lw=1.6, label=name)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "T / K", "log₁₀ (k / s⁻¹)")
charts.title(ax, "C   Temperature (λ = 0.5 eV)")
fig.tight_layout()
