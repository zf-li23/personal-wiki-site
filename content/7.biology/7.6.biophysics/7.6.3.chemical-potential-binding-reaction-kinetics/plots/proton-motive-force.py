# The proton-motive force, quantitatively (T = 310 K, 2.303 RT/F = 61.5 mV).
# A: the two components of the proton-motive force, electrical (membrane potential) and chemical
#    (-61.5 mV x pH difference), for typical energized membranes: mammalian mitochondria (170 mV, 0.5 pH unit),
#    E. coli at external pH 7 (140 mV, 0.4), and illuminated chloroplast thylakoids in steady state (about 30 mV,
#    2.5 pH units). Values are representative; all are given as the magnitude of the driving force on protons
#    moving into the matrix, cytoplasm or stroma.
# B: the largest phosphorylation potential an ATP synthase can sustain, n F dp, with n = c/3 protons per ATP for a
#    c ring of c subunits, at dp = 150 and 200 mV (lines); shaded band: the phosphorylation potential in the
#    mitochondrial matrix and cytosol, about 45 to 60 kJ/mol. Points mark the known ring sizes: bovine
#    mitochondria (c8), yeast mitochondria and E. coli (c10), chloroplasts (c14) and some cyanobacteria (c15).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
F = 96485.33212
Z = 2.303 * 8.314462618 * 310 / F * 1000  # mV per pH unit
fig, axs = plt.subplots(1, 2, figsize=(11.5, 3.8), gridspec_kw={"width_ratios": [1.15, 1.0]})

ax = axs[0]
rows = [("mitochondrion", 170, 0.5), ("E. coli (pH 7 outside)", 140, 0.4), ("thylakoid (light)", 30, 2.5)]
for i, (name, psi, dph) in enumerate(rows):
    y = len(rows) - 1 - i
    chem = Z * dph
    ax.barh(y, psi, color=P.fill("dna"), edgecolor=P.edge("dna"), height=0.55, label="electrical ΔΨ" if i == 0 else None)
    ax.barh(y, chem, left=psi, color=P.fill("h"), edgecolor=P.edge("h"), height=0.55,
            label="chemical 61.5 mV × ΔpH" if i == 0 else None)
    ax.text(psi + chem + 4, y, f"{psi + chem:.0f} mV", va="center", fontsize=7.5, color=P.ink())
ax.set_yticks(range(len(rows)))
ax.set_yticklabels(["thylakoid (light)", "$\\it{E.\\ coli}$ (pH 7 outside)", "mitochondrion"], fontsize=7.5)
ax.set_xlim(0, 300)
ax.legend(fontsize=7, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.78))
charts.style_axes(ax, "proton-motive force Δp / mV")
ax.set_title("A   Two components of Δp", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
c = np.linspace(7, 16, 100)
for dp, tok, ls in ((150, "neutral", (0, (5, 2.5))), (200, "h", "-")):
    ax.plot(c, c / 3 * F * dp * 1e-3 / 1000, color=charts.line(tok), lw=1.8, ls=ls, label=f"Δp = {dp} mV")
ax.axhspan(45, 60, color=P.fill("atp"), alpha=0.3, lw=0)
ax.text(7.2, 61.5, "ΔG_p in cells", fontsize=7, color=P.ink())
for cc, txt in ((8, "bovine\nmitochondria"), (10, "yeast mitochondria,\n$\\it{E.\\ coli}$"), (14, "chloroplast"), (15, "")):
    ax.plot([cc], [cc / 3 * F * 0.2 / 1000], "o", color=charts.line("h"), ms=5)
    if txt:
        ax.text(cc + 0.15, cc / 3 * F * 0.2 / 1000 - 9, txt, fontsize=6.6, color=P.ink())
ax.set_xlim(7, 16)
ax.set_ylim(20, 110)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "c-ring size (c subunits)", "max. ΔG_p = (c/3) F Δp / (kJ mol⁻¹)")
ax.set_title("B   Ring size and the H⁺/ATP ratio", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
