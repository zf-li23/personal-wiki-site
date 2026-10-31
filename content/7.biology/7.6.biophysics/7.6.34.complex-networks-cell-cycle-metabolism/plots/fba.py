"""Flux balance analysis of a toy model of central carbon metabolism: 8 internal metabolites
(glucose, pyruvate, ribose 5-phosphate, acetyl-CoA, NADH, NADPH, ATP, O2) and 11 reactions
(glucose uptake <= 10, glycolysis, pentose phosphate pathway, pyruvate dehydrogenase, TCA cycle,
oxidative phosphorylation, O2 uptake, lactate and acetate excretion, biomass, ATP maintenance >= 1).
Growth is the flux of the biomass reaction, maximized by linear programming subject to S v = 0 and
the flux bounds. A: maximal growth (contours) against glucose and oxygen uptake limits (the
phenotype phase plane); the dashed line is the line of optimality on which both substrates
limit growth. B: excreted fluxes and growth against the oxygen limit at glucose uptake 10: below the
line of optimality the cell excretes lactate (fermentation) and acetate (overflow). C: predicted growth of single-reaction
knockouts, relative to the wild type (O2 limit 12): glucose uptake, glycolysis, the pentose phosphate
pathway, PDH and biomass synthesis are essential; without oxidative phosphorylation (or O2) the cell
grows by fermentation at a fifth of the wild-type rate; the TCA cycle and the excretion pathways
are dispensable. The biomass reaction consumes precursors, NADPH, NADH and 20 ATP per unit."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import wikibio as bio
from wikibio import charts

P = bio.P
mets = ["Glc", "Pyr", "R5P", "AcCoA", "NADH", "NADPH", "ATP", "O2"]
rxns = ["uptake", "glycolysis", "PPP", "PDH", "TCA", "OxPhos", "O2 uptake", "lactate", "acetate", "biomass",
        "maintenance"]
S = np.zeros((8, 11))
col = {r: i for i, r in enumerate(rxns)}
row = {m: i for i, m in enumerate(mets)}
coef = {
    "uptake": {"Glc": 1},
    "glycolysis": {"Glc": -1, "Pyr": 2, "ATP": 2, "NADH": 2},
    "PPP": {"Glc": -1, "R5P": 1, "NADPH": 2},
    "PDH": {"Pyr": -1, "AcCoA": 1, "NADH": 1},
    "TCA": {"AcCoA": -1, "NADH": 4, "ATP": 1},
    "OxPhos": {"NADH": -1, "O2": -0.5, "ATP": 2.5},
    "O2 uptake": {"O2": 1},
    "lactate": {"Pyr": -1, "NADH": -1},
    "acetate": {"AcCoA": -1, "ATP": 1},
    "biomass": {"R5P": -0.2, "Pyr": -1.5, "AcCoA": -1.0, "NADPH": -0.4, "NADH": -3.5, "ATP": -20.0},
    "maintenance": {"ATP": -1},
}
for r, d in coef.items():
    for m, c in d.items():
        S[row[m], col[r]] = c


def fba(glc=10.0, o2=12.0, ko=None):
    bounds = [(0, None)] * 11
    bounds[col["uptake"]] = (0, glc)
    bounds[col["O2 uptake"]] = (0, o2)
    bounds[col["maintenance"]] = (1, None)
    if ko is not None:
        lo = 1 if ko == "maintenance" else 0
        bounds[col[ko]] = (lo, lo) if ko != "maintenance" else (1, 1)
    c = np.zeros(11)
    c[col["biomass"]] = -1
    res = linprog(c, A_eq=S, b_eq=np.zeros(8), bounds=bounds, method="highs")
    return (res.x if res.status == 0 else np.zeros(11))


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=(1, 1, 1.15)))
fig.subplots_adjust(wspace=0.42, left=0.06, right=0.98, bottom=0.2, top=0.88)
ax = axs[0]
g = np.linspace(0.5, 12, 40)
o = np.linspace(0, 30, 40)
Z = np.array([[fba(gg, oo)[col["biomass"]] for gg in g] for oo in o])
cs = ax.contourf(g, o, Z, levels=10, cmap="Purples")
ax.contour(g, o, Z, levels=10, colors=[P.muted()], linewidths=0.4)
# line of optimality: the O2 supply at which growth stops increasing with O2
lo = [fba(gg, 1000)[col["O2 uptake"]] for gg in g]
ax.plot(g, lo, color=P.ink(), lw=1.0, ls="--")
ax.set_ylim(0, 30)
charts.style_axes(ax, "glucose uptake limit", r"O$_2$ uptake limit")
charts.title(ax, "A  Phenotype phase plane")

ax = axs[1]
oo = np.linspace(0, 30, 61)
sols = np.array([fba(10, x) for x in oo])
ax.plot(oo, sols[:, col["biomass"]] * 10, color=charts.line("protein"), lw=1.6, label="growth × 10")
ax.plot(oo, sols[:, col["lactate"]], color=charts.line("blood"), lw=1.3, label="lactate")
ax.plot(oo, sols[:, col["acetate"]], color=charts.line("plant"), lw=1.3, ls="--", label="acetate")
ax.plot(oo, sols[:, col["O2 uptake"]], color=charts.line("dna"), lw=1.0, ls=":", label=r"O$_2$ used")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, r"O$_2$ uptake limit", "flux")
charts.title(ax, "B  Fermentation below the line")

ax = axs[2]
wt = fba()[col["biomass"]]
names = [r for r in rxns if r not in ("biomass", "maintenance")] + ["biomass"]
rel = [fba(ko=r)[col["biomass"]] / wt for r in names]
colors = [P.fill("negative") if v < 0.01 else (P.fill("highlight") if v < 0.99 else P.fill("positive")) for v in rel]
ax.barh(range(len(names)), rel, color=colors, edgecolor=P.muted(), lw=0.4)
for i, v in enumerate(rel):
    if v < 0.01:
        ax.text(0.02, i, "0 (essential)", va="center", fontsize=bio.core.FONT["tiny"], color=charts.line("negative"))
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names)
ax.invert_yaxis()
ax.set_xlim(0, 1.05)
charts.style_axes(ax, "growth of knockout / wild type", None)
charts.title(ax, "C  Knockout predictions")
