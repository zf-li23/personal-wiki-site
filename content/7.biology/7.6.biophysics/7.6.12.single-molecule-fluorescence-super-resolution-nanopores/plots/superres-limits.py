# Physical limits of super-resolution microscopy.
# A: STED: effective PSF width d = d0 / sqrt(1 + I/Is) against the depletion intensity (d0 = 250 nm), with
#    simulated 1D profiles: excitation Gaussian x survival exp(-I(x)/Is), doughnut I(x) = I_max sin^2(pi x / D),
#    D chosen so that its curvature at the zero matches the formula.
# B: single-molecule localization: resolution combining localization precision (FWHM 2.355 sigma_loc) and the
#    Nyquist criterion for label density rho (spacing 2/sqrt(rho)), R = sqrt((2.355 sigma)^2 + (2/sqrt(rho))^2),
#    for sigma_loc = 5, 10 and 20 nm.
# C: precision per photon: camera localization s/sqrt(N) (s = 100 nm) versus MINFLUX with a doughnut minimum
#    probed at +/- L/2, sigma = L/(4 sqrt(N)), for L = 100, 50 and 20 nm.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
ax = axs[0]
xi = np.logspace(-1, 3, 200)
d0 = 250.0
ax.loglog(xi, d0 / np.sqrt(1 + xi), color=charts.line("negative"), lw=1.8)
for x_ in (10, 100):
    ax.plot(x_, d0 / np.sqrt(1 + x_), "o", color=charts.line("negative"), ms=5)
    ax.text(x_ * 1.2, d0 / np.sqrt(1 + x_) * 1.08, f"{d0 / np.sqrt(1 + x_):.0f} nm", fontsize=8, color=P.ink())
charts.style_axes(ax, "I_max / I_s", "effective PSF FWHM / nm")
charts.title(ax, "A   STED: d = d0 / √(1 + I/Is)")
ins = ax.inset_axes([0.12, 0.12, 0.42, 0.38])
x = np.linspace(-300, 300, 600)
exc = np.exp(-4 * np.log(2) * x**2 / d0**2)
for xv, tok in ((0, "neutral"), (10, "dna"), (100, "rna")):
    D = np.pi * d0 / (2 * np.sqrt(np.log(2)))
    I = xv * np.sin(np.pi * x / D) ** 2 if xv > 0 else 0 * x
    ins.plot(x, exc * np.exp(-I), color=charts.line(tok), lw=1.1)
ins.set_xticks([-200, 0, 200])
ins.set_yticks([])
ins.tick_params(labelsize=6)
ins.set_xlabel("x / nm", fontsize=6.5)

ax = axs[1]
rho = np.logspace(1, 5, 200)          # labels per um^2
for sl, tok in ((5, "dna"), (10, "rna"), (20, "protein")):
    R = np.sqrt((2.355 * sl) ** 2 + (2 / np.sqrt(rho) * 1000) ** 2)
    ax.loglog(rho, R, color=charts.line(tok), lw=1.8, label=f"σ_loc = {sl} nm")
ax.loglog(rho, 2000 / np.sqrt(rho), color=P.muted(), lw=0.9, ls=":", label="Nyquist only")
ax.set_ylim(8, 800)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "label density / µm⁻²", "resolution / nm")
charts.title(ax, "B   SMLM needs dense labels and bright emitters")

ax = axs[2]
N = np.logspace(1, 4, 200)
ax.loglog(N, 100 / np.sqrt(N), color=P.ink(), lw=1.8, label="camera, s = 100 nm")
for L, tok in ((100, "protein"), (50, "dna"), (20, "rna")):
    ax.loglog(N, L / (4 * np.sqrt(N)), color=charts.line(tok), lw=1.6, ls="--", label=f"MINFLUX, L = {L} nm")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "detected photons N", "localization precision / nm")
charts.title(ax, "C   Structured probing beats the PSF width")
fig.tight_layout()
