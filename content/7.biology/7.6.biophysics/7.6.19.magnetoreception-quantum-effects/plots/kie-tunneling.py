# Kinetic isotope effects of hydrogen transfer: semiclassical, with tunneling corrections, and in the
# vibrationally assisted (gated) tunneling picture used for enzymes.
# A and B, transition-state picture. Classical rate k = A exp(-E/RT) with E_H = 50 kJ/mol and
#   E_D = E_H + 4.6 kJ/mol (zero-point energy of a C-H stretch at 2900 cm^-1 lost in the transition state,
#   C-D at 2130 cm^-1). Tunneling correction for a parabolic barrier: the transmission probability at energy E
#   is P(E) = 1 / (1 + exp[2 pi (V - E) / (hbar w)]) with imaginary barrier frequency 800 cm^-1 for H and
#   800 / sqrt(2) cm^-1 for D; the thermal average Q = int_0^inf P(E) exp[-(E - V)/kT] dE / kT (energies
#   counted from the reactant zero-point level, so the integral is truncated at E = 0).
# A: Arrhenius plots of k_H and k_D (classical: dashed; with tunneling: solid). B: k_H / k_D against
#   temperature; the semiclassical ceiling is about 7 at room temperature.
# C: gated tunneling. The proton tunnels between donor and acceptor wells whose ground-state wave functions
#   overlap as exp(-a_X d^2), a_X = m_X w_X / (2 hbar), w_H = 3000 cm^-1, m_D w_D = sqrt(2) m_H w_H; the
#   tunneling distance d = d0 - x is shortened by a thermally populated gating vibration x (mass 30 u,
#   frequency W), so the average overlap is (1 + 2 a s^2)^(-1/2) exp[-a d0^2 / (1 + 2 a s^2)] with
#   s^2 = kT / (M W^2); d0 = 0.055 nm. A stiff gating mode (400 cm^-1) gives a large, nearly
#   temperature-independent KIE (as in soybean lipoxygenase, KIE about 80); a soft one (150 cm^-1) a smaller,
#   temperature-dependent KIE.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314462618e-3  # kJ / mol / K
hc_cm = 1.19626566e-2  # kJ/mol per cm^-1
T = np.linspace(250, 350, 51)
EH, dZPE = 50.0, 4.6


def Q(T, nu_cm, V):
    hw = nu_cm * hc_cm
    E = np.linspace(0, V + 60 * R * T.max(), 6000)
    out = []
    for t in T:
        kt = R * t
        Pt = 1 / (1 + np.exp(np.clip(2 * np.pi * (V - E) / hw, -700, 700)))
        out.append(np.trapezoid(Pt * np.exp(-(E - V) / kt), E) / kt)
    return np.array(out)


kH_cl = np.exp(-EH / (R * T))
kD_cl = np.exp(-(EH + dZPE) / (R * T))
kH = kH_cl * Q(T, 800.0, EH)
kD = kD_cl * Q(T, 800.0 / np.sqrt(2), EH + dZPE)

fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0))
ax = axs[0]
x = 1000 / T
ax.plot(x, np.log(kH), color=charts.line("dna"), lw=1.7, label="H, with tunneling")
ax.plot(x, np.log(kH_cl), color=charts.line("dna"), lw=1.2, ls="--", label="H, classical")
ax.plot(x, np.log(kD), color=charts.line("rna"), lw=1.7, label="D, with tunneling")
ax.plot(x, np.log(kD_cl), color=charts.line("rna"), lw=1.2, ls="--", label="D, classical")
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "1000 K / T", "ln (k / A)")
charts.title(ax, "A   Tunneling speeds up H most")

ax = axs[1]
ax.plot(T, kH_cl / kD_cl, color=P.muted(), lw=1.4, ls="--", label="zero-point energy only")
ax.plot(T, kH / kD, color=charts.line("enzyme"), lw=1.8, label="with parabolic-barrier tunneling")
ax.axhspan(1, 7, color=P.fill("neutral"), alpha=0.25, lw=0)
ax.set_yscale("log")
ax.text(255, 4.5, "semiclassical range", fontsize=7, color=P.muted())
ax.set_ylim(1, 100)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "T / K", r"$k_{\mathrm{H}}/k_{\mathrm{D}}$")
charts.title(ax, "B   Tunneling enlarges the KIE")

ax = axs[2]
hbar, amu, c = 1.054571817e-34, 1.66053907e-27, 2.99792458e10
wH = 2 * np.pi * c * 3000.0
aH = 1.00784 * amu * wH / (2 * hbar)
aD = np.sqrt(2) * aH
d0 = 0.55e-10
kB = 1.380649e-23
for W, tok, lab in ((400.0, "dna", "stiff gating, 400 cm⁻¹"), (150.0, "rna", "soft gating, 150 cm⁻¹")):
    K = 30 * amu * (2 * np.pi * c * W) ** 2
    s2 = kB * T / K
    ov = lambda a: (1 + 2 * a * s2) ** -0.5 * np.exp(-a * d0**2 / (1 + 2 * a * s2))
    ax.plot(T, ov(aH) / ov(aD), color=charts.line(tok), lw=1.8, label=lab)
ax.set_yscale("log")
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "T / K", r"$k_{\mathrm{H}}/k_{\mathrm{D}}$ (tunneling factor)")
charts.title(ax, "C   Gated tunneling in enzymes")
fig.tight_layout()
