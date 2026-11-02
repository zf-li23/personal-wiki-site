"""The smoking thread of the course: how the estimate of one effect changed from analysis to analysis.

All values are those computed in the chapters (7.7.n): point estimates with 95 % intervals; open markers
are point estimates for which the chapter reports no interval.
A: FEV of 654 children (Tager et al. 1979; public version Kahn 2005), smoking coefficient in litres by
   adjustment set (7.7.10, 7.7.15).
B: birthwt (189 births, Hosmer and Lemeshow), effect of maternal smoking on birth weight in grams by
   method (7.7.7, 7.7.12, 7.7.15; bootstrap intervals except matching).
C: birthwt, odds ratio of low birth weight (7.7.9, 7.7.14).
D: lung cancer: the Doll-Hill case-control odds ratio (1950) and the rate ratios of the British doctors
   cohort, 1951-2001 (Doll et al. 2004), by smoking habit (7.7.13).
E: veteran lung cancer trial (137 patients), hazard ratio of test vs standard chemotherapy (7.7.16).
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fev = [("crude difference", 0.711, 0.495, 0.927),
       ("adjusted: age", -0.209, -0.368, -0.050),
       ("age, sex (total effect)", -0.154, -0.307, -0.001),
       ("age, sex, height", -0.110, -0.228, 0.008)]
bwt = [("crude difference", -284, -488, -80),
       ("ANCOVA: race, weight", -400, -614, -186),
       ("regression, 8 covariates", -323, -516, -116),
       ("propensity strata", -328, -485, -31),
       ("propensity matching", -377, -684, -69),
       ("IPW, untruncated", -148, -392, 98),
       ("IPW, truncated", -210, -433, 0),
       ("overlap weights", -325, -524, -110)]
low = [("crude (2 x 2 table)", 2.02, 1.08, 3.78),
       ("adjusted: race only", 3.05, None, None),
       ("race, weight", 2.89, None, None),
       ("7-variable logistic", 2.36, 1.07, 5.22)]
lung = [("Doll-Hill 1950, OR", 14.0, 3.3, 59.3),
        ("doctors: former smokers", 4.0, None, None),
        ("current, 1-14 per day", 7.7, None, None),
        ("current, 15-24 per day", 13.7, None, None),
        ("current, 25+ per day", 24.5, None, None),
        ("all current smokers", 14.6, None, None)]
vet = [("treatment only", 1.02, 0.71, 1.45),
       ("+ Karnofsky, cell type", 1.30, 0.88, 1.93)]


def forest(ax, rows, tok, null, log=False):
    k = len(rows)
    for i, (name, e, lo, hi) in enumerate(rows):
        y = k - i
        if lo is not None:
            ax.plot([lo, hi], [y, y], color=charts.line(tok), lw=1.3)
            ax.plot(e, y, "o", ms=5, color=P.fill(tok), mec=charts.line(tok))
        else:
            ax.plot(e, y, "o", ms=5, mfc="none", mec=charts.line(tok), mew=1.2)
        ax.text(-0.03, y, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
                transform=ax.get_yaxis_transform())
    ax.axvline(null, color=P.muted(), lw=0.8, ls="--")
    ax.set_yticks([])
    ax.set_ylim(0.4, k + 0.6)
    if log:
        ax.set_xscale("log")
        ax.xaxis.set_minor_formatter(NullFormatter())


fig = plt.figure(figsize=(12.0, 7.4))
axA = fig.add_axes([0.17, 0.67, 0.27, 0.26])
axB = fig.add_axes([0.66, 0.51, 0.30, 0.42])
axC = fig.add_axes([0.17, 0.32, 0.27, 0.23])
axD = fig.add_axes([0.66, 0.08, 0.30, 0.30])
axE = fig.add_axes([0.17, 0.08, 0.27, 0.10])

forest(axA, fev, "dna", 0)
charts.style_axes(axA, "smoking coefficient, FEV / L")
charts.title(axA, "A  Children's FEV: confounding by age", loc="right")

forest(axB, bwt, "rna", 0)
charts.style_axes(axB, "effect of smoking on birth weight / g")
charts.title(axB, "B  Birth weight: adjustment and weighting", loc="right")

forest(axC, low, "enzyme", 1, log=True)
axC.set_xticks([1, 2, 3, 5])
axC.set_xticklabels(["1", "2", "3", "5"])
charts.style_axes(axC, "odds ratio of low birth weight (< 2500 g)")
charts.title(axC, "C  Low birth weight: crude and adjusted", loc="right")

forest(axD, lung, "negative", 1, log=True)
axD.set_xticks([1, 3, 10, 30, 60])
axD.set_xticklabels(["1", "3", "10", "30", "60"])
charts.style_axes(axD, "odds ratio or rate ratio of lung cancer vs never smokers")
charts.title(axD, "D  Lung cancer: strength and dose response", loc="right")

forest(axE, vet, "protein", 1, log=True)
axE.set_xticks([0.7, 1, 1.5, 2])
axE.set_xticklabels(["0.7", "1", "1.5", "2"])
charts.style_axes(axE, "hazard ratio, test vs standard")
charts.title(axE, "E  Lung cancer chemotherapy (veteran)", loc="right")
