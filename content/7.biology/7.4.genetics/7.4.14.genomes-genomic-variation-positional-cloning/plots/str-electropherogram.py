"""A simulated capillary electrophoresis trace of a multiplex STR profile for two people at four loci (two
dye colors, fragment sizes in bp). Each person has one or two peaks per locus (homozygote or heterozygote);
the alleles are named by the number of repeat units, and the four-base repeat makes alleles 4 bp apart.
Small stutter peaks one unit shorter come from slippage of the polymerase during PCR."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
loci = [("D3S1358", 100, "dna", 4), ("vWA", 160, "dna", 4), ("FGA", 190, "receptor", 4), ("D8S1179", 280, "receptor", 4)]
people = {"Person 1": {"D3S1358": (15, 17), "vWA": (16, 16), "FGA": (21, 24), "D8S1179": (12, 14)},
          "Person 2": {"D3S1358": (14, 15), "vWA": (17, 18), "FGA": (22, 22), "D8S1179": (13, 16)}}
x = np.linspace(80, 340, 4000)
fig, axs = plt.subplots(2, 1, figsize=(9.4, 4.2), sharex=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.94, hspace=0.25)
for ax, (who, g) in zip(axs, people.items()):
    for name, base, tok, unit in loci:
        y = np.zeros_like(x)
        a1, a2 = g[name]
        hom = a1 == a2
        for j, a in enumerate((a1, a2) if not hom else (a1,)):
            pos = base + (a - 10) * unit
            h = 2.0 if hom else 1.0
            y += 0.5 * h * np.exp(-0.5 * ((x - pos) / 0.6) ** 2)
            y += 0.08 * h * np.exp(-0.5 * ((x - pos + unit) / 0.6) ** 2)
            shift = 0 if (hom or abs(a1 - a2) > 1) else (-1.8 if j == 0 else 1.8)
            ax.text(pos + shift, 1.05 if hom else 0.55, str(a), ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
        ax.plot(x, y, color=charts.line(tok), lw=1.0)
        mid = base + (np.mean([np.mean(pp[name]) for pp in people.values()]) - 10) * unit
        ax.text(mid, 1.25, name, ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted(), style="normal")
    ax.set_ylim(0, 1.4)
    ax.set_yticks([])
    charts.style_axes(ax, None, None)
    charts.title(ax, who)
axs[1].set_xlabel("fragment size / bp", fontsize=bio.core.FONT["small"], color=P.ink())
