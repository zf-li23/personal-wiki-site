"""Substrate affinity of ammonia oxidizers. Michaelis-Menten curves v/vmax = S/(Km + S) for total ammonium
(NH3 + NH4+) with the half-saturation constant of Nitrosopumilus maritimus (Km = 0.13 uM, Martens-Habbena et
al. 2009) and a representative value for ammonia-oxidizing bacteria such as Nitrosomonas (Km = 50 uM;
published values range from about 10 to several hundred uM). The shaded band marks the concentrations of
ammonium typical of the open ocean (about 0.01-0.3 uM)."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
S = np.logspace(-3, 3.5, 400)
fig, ax = plt.subplots(figsize=(6.8, 3.8))
ax.axvspan(0.01, 0.3, color=P.light("extracellular"), lw=0)
ax.text(0.055, 1.03, "open ocean", fontsize=6.8, ha="center", color=P.muted())
for name, Km, tok, style in [("Nitrosopumilus maritimus (archaeon)", 0.13, "rna", "italic"),
                             ("ammonia-oxidizing bacteria (typical)", 50.0, "dna", "normal")]:
    v = S / (Km + S)
    ax.plot(S, v, color=charts.line(tok), lw=1.8, label=name)
    ax.plot(Km, 0.5, "o", ms=4, color=charts.line(tok))
ax.set_xscale("log")
ax.set_ylim(0, 1.1)
ax.set_xlim(1e-3, 3e3)
ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.92))
charts.style_axes(ax, "total ammonium / µM", "rate / maximal rate")
