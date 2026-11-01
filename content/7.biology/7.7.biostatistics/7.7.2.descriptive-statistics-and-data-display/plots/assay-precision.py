"""Precision of an ELISA (DNase data: 11 independent runs, 8 concentrations of rat serum DNase, two wells
each; Davidian and Giltinan 1995). A: optical density of run 1 against concentration; each pair of points
is a duplicate. B: coefficient of variation between duplicate wells (s / mean of the two wells) for all
88 pairs; the median CV is about 1-2 % at most concentrations but rises to 7 % at the lowest one, where the
signal is close to the background.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("dnase.csv") as fh:
    rows = [(int(r["run"]), float(r["conc"]), float(r["density"])) for r in csv.DictReader(fh)]
pairs = {}
for run, c, d in rows:
    pairs.setdefault((run, c), []).append(d)
concs = sorted({c for _, c in pairs})
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.08, right=0.99, bottom=0.17, top=0.87, wspace=0.28)
ax = axs[0]
for c in concs:
    ax.scatter([c, c], pairs[(1, c)], s=14, color=charts.line("enzyme"), lw=0)
ax.set_xscale("log", base=2)
charts.style_axes(ax, "DNase concentration / (ng/mL)", "optical density")
charts.title(ax, "A  Run 1: duplicate wells")
ax = axs[1]
rng = np.random.default_rng(0)
med = []
for k, c in enumerate(concs):
    cv = [100 * np.std(v, ddof=1) / np.mean(v) for (r, cc), v in pairs.items() if cc == c]
    med.append(np.median(cv))
    ax.scatter(k + rng.uniform(-0.15, 0.15, len(cv)), cv, s=10, color=charts.line("enzyme"), alpha=0.7, lw=0)
ax.plot(range(len(concs)), med, "-", color=P.ink(), lw=1.2, marker="s", ms=4, label="median CV")
ax.set_xticks(range(len(concs)))
ax.set_xticklabels([f"{c:.2g}" for c in concs], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "concentration / (ng/mL)", "CV between duplicates / %")
charts.title(ax, "B  Intra-assay CV")
