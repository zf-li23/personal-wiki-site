"""Bootstrap confidence intervals with the FEV data (654 children, East Boston; Tager et al. 1979; public
version from the Vanderbilt Biostatistics data repository). A: bootstrap distribution of the sample median
of FEV from 10 000 resamples of the 654 children; the shaded region between the 2.5th and 97.5th
percentiles is the 95 % percentile interval. B: bootstrap distribution of the ratio of mean FEV in smokers
to non-smokers (resampling within each group). Random seed 0.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
rows = list(csv.DictReader(open("fev.csv")))
fev = np.array([float(r["fev"]) for r in rows])
smoke = np.array([int(r["smoke"]) for r in rows])
B = 10000

med = np.median(fev)
boot_med = np.median(rng.choice(fev, size=(B, len(fev))), axis=1)
a, c = fev[smoke == 1], fev[smoke == 0]
ratio = a.mean() / c.mean()
boot_ratio = rng.choice(a, size=(B, len(a))).mean(axis=1) / rng.choice(c, size=(B, len(c))).mean(axis=1)

fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.4))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.2)
for ax, bs, est, name, xl, tok in [(axs[0], boot_med, med, "A  Median FEV, all 654 children", "bootstrap median (L)", "dna"),
                                   (axs[1], boot_ratio, ratio, "B  Ratio of mean FEV, smokers / non-smokers",
                                    "bootstrap ratio", "rna")]:
    lo, hi = np.percentile(bs, [2.5, 97.5])
    bins = np.unique(bs).size < 200
    ax.hist(bs, bins=60 if not bins else np.unique(bs).size, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.3)
    ax.axvspan(lo, hi, color=P.fill("neutral"), alpha=0.35, lw=0)
    ax.axvline(est, color=P.ink(), lw=1.0)
    ax.text(0.98, 0.92, f"estimate {est:.3f}\n95 % percentile CI\n{lo:.3f} to {hi:.3f}\nbootstrap SE {bs.std(ddof=1):.3f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=FT["tiny"], color=P.ink())
    ax.set_yticks([])
    charts.style_axes(ax, xl, "frequency" if ax is axs[0] else None)
    charts.title(ax, name)
