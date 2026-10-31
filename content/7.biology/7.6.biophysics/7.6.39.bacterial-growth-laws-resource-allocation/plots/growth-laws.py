# The bacterial growth laws (Scott, Gunderson, Mateescu, Zhang and Hwa 2010), from the proteome
# allocation model of Formula 39.2.2 with r = RNA/protein (proportional to the ribosomal proteome
# fraction): translational capacity lambda = kappa_t (r - r0), nutritional capacity
# lambda = kappa_n (r_max - r), r0 = 0.087, r_max = 0.65, kappa_t = 4.5 per hour without drug.
# A: varying nutrient quality kappa_n (filled circles, the first growth law, slope 1/kappa_t) and, for
# each medium, adding a translation inhibitor that lowers kappa_t (lines of negative slope -1/kappa_n,
# the second law). B: expressing a useless protein at fraction phi_U of the proteome lowers growth
# linearly, lambda = lambda_0 (1 - phi_U / phi_c), phi_c about 0.48 (third law), for three media.
# C: the cell-cycle side of growth (Cooper-Helmstetter with C = 40 min, D = 20 min, doubling time tau):
# origins and termini per newborn cell and their ratio, which marker-frequency analysis measures.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
r0, rmax, kt0 = 0.087, 0.65, 4.5
kns = [0.6, 1.2, 2.0, 3.0, 5.0]
toks = ["rna", "atp", "enzyme", "dna", "protein"]

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
lam_nut = []
for kn, tok in zip(kns, toks):
    lam = kt0 * kn * (rmax - r0) / (kt0 + kn)
    lam_nut.append(lam)
    kts = np.linspace(kt0, 0.4, 50)
    l2 = kts * kn * (rmax - r0) / (kts + kn)
    r2 = rmax - l2 / kn
    ax.plot(l2, r2, color=charts.line(tok), lw=1.4)
    ax.plot(l2[::12], r2[::12], "s", ms=4, color=charts.line(tok), mfc="none")
    ax.plot([lam], [r0 + lam / kt0], "o", ms=6, color=charts.line(tok))
lg = np.linspace(0, 2.0, 50)
ax.plot(lg, r0 + lg / kt0, color=P.ink(), lw=1.0, ls="--")
ax.text(1.55, r0 + 1.55 / kt0 - 0.06, "nutrients\n(slope $1/\\kappa_t$)", fontsize=7.5, color=P.ink())
ax.text(0.05, 0.6, "translation inhibitor\n(slope $-1/\\kappa_n$)", fontsize=7.5, color=P.ink())
ax.set_xlim(0, 2.0); ax.set_ylim(0, 0.7)
charts.style_axes(ax, "growth rate $\\lambda$ / h$^{-1}$", "RNA/protein $r$")
charts.title(ax, "A   First and second growth laws")

ax = axs[1]
phic = 0.48
phiU = np.linspace(0, 0.45, 50)
for lam0, tok in zip(lam_nut, toks):
    ax.plot(phiU, lam0 * (1 - phiU / phic), color=charts.line(tok), lw=1.8, label=f"$\\lambda_0$ = {lam0:.2f} h$^{{-1}}$")
ax.set_xlim(0, 0.5); ax.set_ylim(0, 1.6)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "useless protein $\\phi_U$", "growth rate $\\lambda$ / h$^{-1}$")
charts.title(ax, "B   Third law: the cost of protein")

ax = axs[2]
C, Dd = 40 / 60, 20 / 60
lam = np.linspace(0.1, 2.1, 200)
ax.plot(lam, 2 ** ((C + Dd) * lam / np.log(2)), color=charts.line("dna"), lw=2.0, label="origins per cell at birth, $2^{(C+D)/\\tau}$")
ax.plot(lam, 2 ** (Dd * lam / np.log(2)), color=charts.line("rna"), lw=1.6, label="termini per cell at birth, $2^{D/\\tau}$")
ax.plot(lam, 2 ** (C * lam / np.log(2)), color=P.muted(), lw=1.2, ls="--", label="ori/ter ratio, $2^{C/\\tau}$")
for tau in (20, 30, 60):
    l = np.log(2) * 60 / tau
    ax.axvline(l, color=P.muted(), lw=0.5, ls=":")
    ax.text(l, 12.5, f"{tau} min", fontsize=7, color=P.ink(), ha="center")
ax.set_yscale("log", base=2)
ax.set_ylim(1, 15)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "growth rate $\\lambda$ / h$^{-1}$", "copies per newborn cell")
charts.title(ax, "C   Overlapping replication rounds")
fig.tight_layout()
