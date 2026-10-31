# Facilitated diffusion: search time of a DNA-binding protein for one site in a bacterial genome.
# M = 4.6e6 bp, base-pair spacing b = 0.34 nm. Each round: three-dimensional excursion of mean duration tau3,
# then nonspecific binding and one-dimensional sliding for tau1, which scans n = sqrt(8 D1 tau1 / pi) / b new
# base pairs (the mean range of a 1D Brownian walk). Search time tau_s = (M / n)(tau1 + tau3).
# A: tau_s against the fraction of time bound to DNA, f = tau1/(tau1 + tau3), for tau3 = 1 ms and three 1D
#    diffusion coefficients; the optimum is at tau1 = tau3 (f = 1/2), and a purely 3D search (n = 1 per round)
#    is shown for comparison. B: the speed-stability problem: on a rough nonspecific landscape (standard
#    deviation sigma of the binding energy) the 1D diffusion coefficient falls as D0 exp(-(sigma/kT)^2)
#    (Zwanzig), D0 = 1 um^2/s, and the optimal search time rises steeply beyond sigma ~ 1-2 kT.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
M, b, tau3 = 4.6e6, 0.34, 1e-3


def tsearch(tau1, D1):
    n = np.maximum(np.sqrt(8 * D1 * tau1 / np.pi) / b, 1.0)
    return M / n * (tau1 + tau3)


fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
f = np.linspace(0.005, 0.995, 400)
tau1 = f / (1 - f) * tau3
for D1um, tok in ((0.01, "neutral"), (0.046, "dna"), (0.2, "rna")):
    D1 = D1um * 1e6  # nm^2/s
    ts = tsearch(tau1, D1)
    ell = np.sqrt(8 * D1 * tau3 / np.pi) / b
    axs[0].semilogy(f, ts, color=charts.line(tok), lw=1.8, label=f"D₁ = {D1um:g} µm²/s (n* = {ell:.0f} bp)")
    axs[0].plot(0.5, tsearch(tau3, D1), "o", color=charts.line(tok), ms=4)
axs[0].axhline(M * tau3, color=P.muted(), lw=0.8, ls=":")
axs[0].text(0.25, M * tau3 * 0.8, "one base pair per round (no sliding)", fontsize=7.5, color=P.muted())
charts.style_axes(axs[0], "fraction of time bound nonspecifically", "search time for one protein / s")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 0.85))
charts.title(axs[0], "A   An optimum at equal 1D and 3D times")

sig = np.linspace(0, 3, 200)
D0 = 1e6
Dr = D0 * np.exp(-sig**2)
axs[1].semilogy(sig, tsearch(tau3, Dr), color=charts.line("dna"), lw=1.8, label="optimal search time")
ax2 = axs[1].twinx()
ax2.semilogy(sig, Dr / 1e6, color=charts.line("rna"), lw=1.2, ls="--")
ax2.set_ylabel("D₁ / (µm² s⁻¹)", color=charts.line("rna"), fontsize=8)
ax2.tick_params(colors=P.muted(), labelcolor=charts.line("rna"), labelsize=7)
for sp in ax2.spines.values():
    sp.set_color(P.muted())
axs[1].axvspan(0, 1.5, color=P.fill("positive"), alpha=0.3, lw=0)
axs[1].text(0.1, tsearch(tau3, Dr)[-1] * 0.5, "fast sliding\nσ ≲ 1–2 kT", fontsize=8, color=P.ink())
charts.style_axes(axs[1], "roughness of nonspecific landscape σ / kT", "search time / s")
charts.title(axs[1], "B   Speed requires a smooth landscape")
fig.tight_layout()
