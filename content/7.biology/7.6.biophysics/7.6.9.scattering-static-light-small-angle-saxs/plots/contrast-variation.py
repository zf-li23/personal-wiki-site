# Contrast variation in small-angle neutron scattering.
# A: neutron scattering-length densities (SLD, in 1e10 cm^-2) as functions of the D2O fraction x of the
#    solvent. Solvent: rho_s(x) = (1 - x) rho(H2O) + x rho(D2O), with rho(H2O) = -0.56 and rho(D2O) = 6.36,
#    computed from b(H) = -3.739 fm, b(D) = 6.671 fm, b(O) = 5.803 fm and the molecular volumes of the two
#    waters. Macromolecules (typical values; exchangeable hydrogens follow the solvent, so the SLD rises
#    with x): protein 1.8 -> 3.1, nucleic acid 3.5 -> 4.4, perdeuterated protein 7.0 -> 8.3,
#    phospholipid (acyl chains dominate) 0.3 -> 0.6. Circles: match points, where the component becomes invisible.
# B: Stuhrmann plot of a concentric two-component model particle resembling a nucleosome core: a protein
#    sphere of radius 32 A (Rg = 24.8 A, volume 137 nm^3, about that of the histone octamer) inside a DNA
#    shell from 46 to 50 A (Rg = 48.1 A, volume 116 nm^3, about that of 147 bp of DNA). Rg^2 = Rm^2 + alpha / drho is linear in 1/drho
#    (beta = 0 because the centres coincide), with alpha > 0: the component of higher SLD (DNA) is outside.
#    Marked points: the D2O fractions where protein or DNA is matched, giving the Rg of the other component.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
NA = 6.02214076e23
bH, bD, bO = -3.739, 6.671, 5.803                      # fm
vH = 18.015 / 0.9982 / NA * 1e24                      # A^3 per molecule
vD = 20.028 / 1.1044 / NA * 1e24
rH = (2 * bH + bO) / vH * 10                          # fm/A^3 -> 1e10 cm^-2
rD = (2 * bD + bO) / vD * 10
x = np.linspace(0, 1, 101)
solvent = (1 - x) * rH + x * rD
comps = (("protein", 1.8, 3.1, "protein"), ("nucleic acid", 3.5, 4.4, "dna"),
         ("deuterated protein", 7.0, 8.3, "highlight"), ("lipid", 0.3, 0.6, "lipid"))

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axs[0]
ax.plot(100 * x, solvent, color=P.ink(), lw=2.0, label="H₂O/D₂O solvent")
match = {}
for name, a, b, tok in comps:
    rho = a + (b - a) * x
    ax.plot(100 * x, rho, color=charts.line(tok), lw=1.7, label=name)
    xm = (a - rH) / ((rD - rH) - (b - a))
    if 0 <= xm <= 1:
        match[name] = xm
        ax.plot(100 * xm, a + (b - a) * xm, "o", color=charts.line(tok), ms=7, mfc="none", mew=1.5)
        ax.text(100 * xm + 2, a + (b - a) * xm - 0.55, f"{100 * xm:.0f} %", color=charts.line(tok), fontsize=8)
ax.set_xlim(0, 100)
ax.set_ylim(-1, 9)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "D₂O in solvent  (%)", "SLD  /  (10¹⁰ cm⁻²)")
charts.title(ax, "A   Scattering-length densities and match points")

ax = axs[1]
Rp, r1, r2 = 32.0, 46.0, 50.0
Vp = 4 / 3 * np.pi * Rp**3
Vd = 4 / 3 * np.pi * (r2**3 - r1**3)
rg2p = 3 / 5 * Rp**2
rg2d = 3 / 5 * (r2**5 - r1**5) / (r2**3 - r1**3)
xs = np.linspace(0, 1, 400)
sol = (1 - xs) * rH + xs * rD
dp = 1.8 + 1.3 * xs - sol
dd = 3.5 + 0.9 * xs - sol
drho = (dp * Vp + dd * Vd) / (Vp + Vd)                 # mean contrast of the particle
rg2 = (dp * Vp * rg2p + dd * Vd * rg2d) / (dp * Vp + dd * Vd)
ok = np.abs(drho) > 0.35
inv = 1 / drho
seg = np.split(np.arange(len(xs)), np.where(np.diff(ok.astype(int)) != 0)[0] + 1)
for s in seg:
    if ok[s[0]]:
        ax.plot(inv[s], rg2[s] / 100, color=charts.line("neutral"), lw=1.8)
for name, tok, val in (("protein matched", "dna", rg2d), ("DNA matched", "protein", rg2p)):
    key = "protein" if name.startswith("protein") else "nucleic acid"
    xm = match[key]
    i = np.argmin(np.abs(xs - xm))
    ax.plot(inv[i], val / 100, "o", color=charts.line(tok), ms=7)
    ax.annotate(f"{name} ({100 * xm:.0f} % D₂O)\nRg = {np.sqrt(val):.1f} Å", xy=(inv[i], val / 100),
                xytext=(inv[i] + 0.2, val / 100 - 4.0) if inv[i] < 0 else (inv[i] - 1.6, val / 100 + 2.5), fontsize=7.5,
                color=charts.line(tok), arrowprops=dict(arrowstyle="-", color=charts.line(tok), lw=0.7))
for xx in (0.0, 1.0):
    i = np.argmin(np.abs(xs - xx))
    ax.plot(inv[i], rg2[i] / 100, "s", color=P.muted(), ms=4)
    ax.text(inv[i], rg2[i] / 100 - 1.6, f"{100 * xx:.0f} % D₂O", color=P.muted(), fontsize=7, ha="center")
ax.axvline(0, color=P.muted(), lw=0.6)
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(0, 30)
charts.style_axes(ax, "1 / Δρ̄  /  (10⁻¹⁰ cm²)", "Rg²  /  (100 Å²)")
charts.title(ax, "B   Stuhrmann plot of a core–shell particle")
fig.tight_layout()
