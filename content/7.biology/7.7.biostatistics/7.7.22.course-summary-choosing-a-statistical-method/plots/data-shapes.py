"""The shapes of the data sets of the course (7.7.n), on logarithmic axes.

A: individual-level data: number of units n (children, births, patients, animals, assay runs, subjects,
   samples) against the number of variables p recorded per unit; the marker gives the data type
   (cross-sectional, repeated measures, time to event, high-dimensional). airway: 8 samples, about 6 x 10^4
   genes (18,899 tested after filtering). The dashed line is p = n.
B: studies used through published summary tables, by number of participants: the Hanley-McNeil CT
   ratings, the Doll-Hill case-control study, the Physicians' Health Study, the British doctors cohort and
   the National Lung Screening Trial.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

# name, n, p, type, token (thread)
sets = [("FEV", 654, 5, "cross", "dna"),
        ("birthwt", 189, 10, "cross", "dna"),
        ("ToothGrowth", 60, 3, "cross", "enzyme"),
        ("Puromycin", 23, 3, "cross", "enzyme"),
        ("DNase (runs)", 11, 3, "repeated", "enzyme"),
        ("sleepstudy", 18, 3, "repeated", "protein"),
        ("veteran", 137, 8, "survival", "dna"),
        ("airway", 8, 6.0e4, "high", "rna")]
marker = {"cross": "o", "repeated": "s", "survival": "^", "high": "D"}
label = {"cross": "cross-sectional", "repeated": "repeated measures", "survival": "time to event",
         "high": "high-dimensional"}
summ = [("CT ratings (Hanley-McNeil)", 109), ("Doll-Hill case-control", 1298),
        ("Physicians' Health Study", 22071), ("British doctors cohort", 34439), ("NLST", 53454)]

fig = plt.figure(figsize=(11.5, 4.8))
axA = fig.add_axes([0.07, 0.14, 0.42, 0.78])
axB = fig.add_axes([0.73, 0.14, 0.24, 0.78])

grid = np.logspace(0, 5, 50)
axA.plot(grid, grid, color=P.muted(), lw=0.8, ls="--")
axA.text(3.0e2, 4.4e2, "p = n", fontsize=FT["tiny"], color=P.muted(), rotation=28)
off = {"FEV": (1.15, 1.0), "birthwt": (1.15, 1.0), "ToothGrowth": (1.15, 0.78), "Puromycin": (1.15, 1.18),
       "DNase (runs)": (0.8, 1.35), "sleepstudy": (1.15, 0.8), "veteran": (1.15, 1.0), "airway": (1.25, 0.9)}
seen = set()
for name, n, p, typ, tok in sets:
    lab = label[typ] if typ not in seen else None
    seen.add(typ)
    axA.scatter([n], [p], s=48, marker=marker[typ], color=P.fill(tok), edgecolor=charts.line(tok), lw=1.0,
                zorder=5, label=lab)
    fx, fy = off[name]
    axA.text(n * fx, p * fy, name, fontsize=FT["tiny"], color=P.ink(), va="center")
axA.set_xscale("log")
axA.set_yscale("log")
axA.set_xlim(4, 3e3)
axA.set_ylim(1.5, 3e5)
leg = axA.legend(fontsize=FT["tiny"], frameon=False, loc="upper right", markerscale=0.8)
for h in leg.legend_handles:
    h.set_facecolor(P.fill("neutral"))
    h.set_edgecolor(charts.line("neutral"))
charts.style_axes(axA, "units n", "variables per unit p")
charts.title(axA, "A  Individual-level data", loc="right")

y = np.arange(len(summ))[::-1]
axB.barh(y, [n for _, n in summ], color=P.fill("neutral"), edgecolor=charts.line("neutral"), height=0.6)
axB.set_xscale("log")
axB.set_xlim(50, 2e5)
for yy, (name, n) in zip(y, summ):
    axB.text(-0.03, yy, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
             transform=axB.get_yaxis_transform())
    axB.text(n * 1.15, yy, f"{n:,}", va="center", fontsize=FT["tiny"], color=P.ink())
axB.set_yticks([])
charts.style_axes(axB, "participants")
charts.title(axB, "B  Summary tables", loc="right")
