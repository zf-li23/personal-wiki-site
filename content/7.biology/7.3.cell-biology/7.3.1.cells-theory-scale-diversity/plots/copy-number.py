# Number of molecules per cell at a given concentration, N = c V N_A, against cell volume (log-log).
# Volumes: Mycoplasma genitalium ~0.015 fL (0.3 um sphere), E. coli ~1 fL, haploid budding yeast ~40 fL,
# HeLa ~3000 fL, Xenopus oocyte ~1 uL = 1e9 fL. Lines for 1 nM, 1 uM and 1 mM; the shaded band marks
# fewer than ten molecules per cell, where concentrations stop being continuous and noise dominates.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
NA = 6.022e23

fig, ax = plt.subplots(figsize=(6.6, 4.0))
V = np.logspace(-2.5, 9.5, 100)  # fL
for c, txt, tok in ((1e-9, "1 nM", "dna"), (1e-6, "1 µM", "protein"), (1e-3, "1 mM", "metabolite")):
    N = c * V * 1e-15 * NA
    ax.loglog(V, N, color=charts.line(tok), lw=1.8)
    ax.text(10 ** 8.7, c * 10 ** 8.7 * 1e-15 * NA * 2.2, txt, fontsize=7.5, color=charts.line(tok), ha="right")
ax.axhspan(1e-3, 10, color=P.fill("negative"), alpha=0.35, lw=0)
ax.text(10 ** 3.6, 0.04, "fewer than 10 molecules per cell", fontsize=7, color=P.ink())
for v, txt in ((0.015, "Mycoplasma"), (1, "E. coli"), (40, "yeast"), (3000, "HeLa"), (1e9, "frog oocyte")):
    ax.axvline(v, color=P.muted(), lw=0.6, ls=":")
    ax.text(v * 1.2, 3e13, txt, fontsize=7, color=P.ink(), rotation=90, va="top",
            style="italic" if txt in ("Mycoplasma", "E. coli") else "normal")
ax.set_xlim(10 ** -2.5, 10 ** 9.5)
ax.set_ylim(1e-3, 1e14)
charts.style_axes(ax, "cell volume V / fL (1 fL = 1 µm³)", "molecules per cell N")
fig.tight_layout()
