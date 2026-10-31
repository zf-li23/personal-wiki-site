# Anomalous scattering near an absorption edge and the breakdown of Friedel's law.
# A: model of the anomalous scattering factors of selenium near its K edge (E0 = 12.658 keV). f'' is an
#    arctan step (0.5 -> 3.8 electrons, width 1.5 eV) plus a Lorentzian "white line" (height 2.5, width
#    2 eV) just above the edge, as in fluorescence scans of selenomethionine crystals; f' follows from
#    the Kramers-Kronig relation f'(E) = (1/pi) P int f''(E') / (E - E') dE' (local, Hilbert-transform
#    form), with an additive constant so that f' = -3.5 well below the edge. The usual MAD wavelengths
#    are marked: peak (maximum f''), inflection (minimum f'), and a high-energy remote.
# B: Argand diagram of one Bijvoet pair (F_N = 70 exp(i 30 deg), F_A = 30 exp(i 80 deg), k = f''/(f0 + f') = 0.4).
#    F_N is the contribution of all normal scattering (including
#    f0 + f' of the anomalous atoms), F'' the anomalous part, 90 deg ahead of the anomalous atoms'
#    normal contribution. For +h it adds as +i k F_A, for the conjugate of -h as -i k F_A, so
#    |F(+h)| != |F(-h)|.
# C: expected Bijvoet ratio <|Delta F|>/<|F|> ~ sqrt(2 N_A / N_T) f'' / Z_eff (rms estimate, N_T = 7.8
#    non-hydrogen atoms per residue, Z_eff = 6.7) against the number of residues per anomalous atom: Se at
#    the peak (f'' = 3.8), Se below the edge (0.5), and S at 1.54 A (0.56) and at 2.1 A (0.95).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

E0 = 12658.0
x = np.linspace(-60, 60, 1201)                 # E - E0 in eV
G, A, f2_0 = 1.5, 3.3, 0.5
h, g, x1 = 2.5, 2.0, 1.5
f2 = f2_0 + A * (0.5 + np.arctan(x / G) / np.pi) + h * g**2 / ((x - x1) ** 2 + g**2)
# Hilbert partners: step -> (A / 2 pi) ln((x^2 + G^2) / Lambda^2); Lorentzian -> h g (x - x1) / (...)
f1 = (A / (2 * np.pi)) * np.log((x**2 + G**2) / 60.0**2) + h * g * (x - x1) / ((x - x1) ** 2 + g**2)
f1 += -3.5 - f1[0]

fig, axs = plt.subplots(1, 3, figsize=(14, 4.4), gridspec_kw={"width_ratios": [1.1, 1, 1]})
ax = axs[0]
ax.plot(x, f2, color=charts.line("protein"), lw=1.8, label="f''")
ax.plot(x, f1, color=charts.line("dna"), lw=1.8, label="f'")
ipk = np.argmax(f2)
iinf = np.argmin(f1)
for i, name in ((ipk, "peak"), (iinf, "inflection")):
    ax.axvline(x[i], color=muted, lw=0.8, ls=(0, (3, 2)))
    ax.text(x[i] + 0.8, 5.6 if name == "peak" else -9.6, name, fontsize=8, color=ink)
ax.axvline(50, color=muted, lw=0.8, ls=(0, (3, 2)))
ax.text(38, 5.6, "remote", fontsize=8, color=ink)
ax.axhline(0, color=muted, lw=0.5)
ax.legend(fontsize=9, frameon=False, loc="center left")
ax.set_ylim(-10.5, 7)
ax.set_title("A  Se K edge (model)", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"$E - 12.658\,$keV / eV", "electrons")

ax = axs[1]
FN = 70 * np.exp(1j * np.deg2rad(30))
FA = 30 * np.exp(1j * np.deg2rad(80))
k = 0.4
Fp = FN + 1j * k * FA
Fm = FN - 1j * k * FA


def arr(z0, z1, col, lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((z0.real, z0.imag), (z1.real, z1.imag), arrowstyle="-|>", mutation_scale=11,
                                 color=col, lw=lw, ls=ls))


arr(0, FN, ink)
arr(0, FA, charts.line("highlight"), lw=1.2)
ax.text(FA.real - 9, FA.imag * 0.6, r"$\boldsymbol{F}_{\mathrm{A}}$", fontsize=10, color=charts.line("highlight"))
arr(FN, Fp, charts.line("protein"))
arr(FN, Fm, charts.line("dna"))
arr(0, Fp, charts.line("protein"), lw=1.0, ls=(0, (4, 2)))
arr(0, Fm, charts.line("dna"), lw=1.0, ls=(0, (4, 2)))
ax.text(FN.real * 0.5 + 2, FN.imag * 0.5 - 7, r"$\boldsymbol{F}_{\mathrm{N}}$", fontsize=11, color=ink)
ax.text(Fp.real - 30, Fp.imag + 5, r"$\boldsymbol{F}(+\boldsymbol{h})$", fontsize=10,
        color=charts.line("protein"))
ax.text(Fm.real + 3, Fm.imag - 7, r"$\boldsymbol{F}(-\boldsymbol{h})^*$", fontsize=10, color=charts.line("dna"))
ax.text(40, -18, rf"$|F(+h)|$ = {abs(Fp):.1f}" + "\n" + rf"$|F(-h)|$ = {abs(Fm):.1f}", fontsize=9, color=ink)
ax.axhline(0, color=muted, lw=0.5)
ax.axvline(0, color=muted, lw=0.5)
ax.set_xlim(-10, 85)
ax.set_ylim(-25, 70)
ax.set_aspect("equal")
ax.set_title("B  a Bijvoet pair", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "Re F", "Im F", box=True)

ax = axs[2]
res = np.logspace(1, 3.5, 100)
NT = 7.8 * res
for f2v, tok, name in ((3.8, "protein", "Se, peak (f'' = 3.8)"), (0.95, "highlight", "S, 2.1 Å (0.95)"),
                       (0.56, "neutral", "S, 1.54 Å (0.56)"), (0.5, "dna", "Se, below edge (0.5)")):
    ax.loglog(res, 100 * np.sqrt(2 / NT) * f2v / 6.7, color=charts.line(tok), lw=1.7, label=name)
ax.axhline(1, color=muted, lw=0.7, ls=(0, (3, 2)))
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
ax.set_title("C  expected anomalous signal", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "residues per anomalous atom", r"$\langle|\Delta F|\rangle / \langle|F|\rangle$ / %")
fig.tight_layout()
