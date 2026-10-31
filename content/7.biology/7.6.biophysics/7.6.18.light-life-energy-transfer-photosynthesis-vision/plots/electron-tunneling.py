# Electron tunneling between redox cofactors.
# A: decay length of a bound electron outside its well, xi = hbar / sqrt(2 m_e (V0 - E)), for an electron
#    bound by V0 - E (0.1-10 eV); xi = 0.195 nm / sqrt(V0 - E in eV). The wave function falls as exp(-x / xi),
#    so the coupling between two wells falls as exp(-d / xi) and the rate as exp(-2 d / xi).
# B: the Moser-Dutton ruler for the activationless (maximal) rate,
#    log10 k_max = 13 - (beta / ln 10)(R - 0.36 nm), R the edge-to-edge distance,
#    beta = 9 rho + 28 (1 - rho) per nm for a medium with packing density rho (Page et al. 1999);
#    rho = 0.76 (average protein, beta = 14 per nm) gives the familiar slope of 6 decades per nm.
#    Shaded: the edge-to-edge distances of most physiological electron-transfer steps (0.4-1.4 nm).
# C: the two-well toy model. An electron starting in well A oscillates to well B with probability
#    P_B(t) = [4H^2 / (4H^2 + D^2)] sin^2(sqrt(4H^2 + D^2) t / (2 hbar)), H the coupling and D the energy
#    mismatch between the wells: a mismatch of a few H suppresses transfer, which is why nuclear fluctuations
#    that bring the levels into resonance gate the transfer (Marcus theory).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

ax = axs[0]
V = np.logspace(-1, 1, 200)
xi = 0.195 / np.sqrt(V)
ax.plot(V, xi, color=charts.line("dna"), lw=1.8)
for v in (0.5, 1.0, 4.0):
    ax.plot(v, 0.195 / np.sqrt(v), "o", ms=4, color=charts.line("rna"))
    ax.text(v * 1.1, 0.195 / np.sqrt(v) + 0.02, f"{v:g} eV: {0.195 / np.sqrt(v):.2f} nm", fontsize=7, color=P.ink())
ax.set_xscale("log")
ax.set_ylim(0, 0.7)
charts.style_axes(ax, "binding energy V₀ − E / eV", "decay length ξ / nm")
charts.title(ax, "A   How far a wave function leaks")

ax = axs[1]
R = np.linspace(0.3, 2.5, 200)
ax.axvspan(0.4, 1.4, color=P.fill("protein"), alpha=0.18, lw=0)
for rho, tok, lab in ((1.0, "enzyme", "ρ = 1 (dense protein)"), (0.76, "dna", "ρ = 0.76 (average protein)"),
                      (0.5, "protein", "ρ = 0.5"), (0.0, "neutral", "ρ = 0 (vacuum-like)")):
    beta = 9 * rho + 28 * (1 - rho)
    ax.plot(R, 13 - beta / np.log(10) * (R - 0.36), color=charts.line(tok), lw=1.6, label=f"{lab}, β = {beta:.0f} nm⁻¹")
for t, lab in ((1e-12, "1 ps"), (1e-9, "1 ns"), (1e-6, "1 μs"), (1e-3, "1 ms"), (1.0, "1 s")):
    ax.axhline(-np.log10(t), color=P.muted(), lw=0.5, ls=":")
    ax.text(2.48, -np.log10(t) + 0.15, lab, fontsize=6.5, ha="right", color=P.muted())
ax.set_xlim(0.3, 2.5)
ax.set_ylim(-2, 13.5)
ax.legend(fontsize=6.5, frameon=False, loc="upper right")
charts.style_axes(ax, "edge-to-edge distance R / nm", r"$\log_{10}(k_{\max}/\mathrm{s}^{-1})$")
charts.title(ax, "B   The Moser–Dutton ruler")

ax = axs[2]
Hc = 1.0
t = np.linspace(0, 12, 500)  # in units of hbar / H
for D, tok in ((0.0, "dna"), (2.0, "enzyme"), (6.0, "rna")):
    Om = np.sqrt(4 * Hc**2 + D**2)
    ax.plot(t, 4 * Hc**2 / Om**2 * np.sin(Om * t / 2) ** 2, color=charts.line(tok), lw=1.6, label=f"mismatch Δ = {D:g} H")
ax.set_ylim(0, 1.45)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time t / (ħ/H)", "probability in well B")
charts.title(ax, "C   Two wells: resonance matters")
fig.tight_layout()
