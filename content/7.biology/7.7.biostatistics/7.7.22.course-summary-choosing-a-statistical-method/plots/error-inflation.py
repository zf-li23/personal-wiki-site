"""Common errors of the course, quantified with the values computed in the chapters (7.7.n).

A: actual false-positive rates of analyses run at a nominal 5 %: all 10 pairwise t tests among 5 groups
   (7.7.12); 5 unadjusted interim analyses of a trial (7.7.18); cells treated as independent replicates
   (3 mice per group, 10 cells per mouse) at intraclass correlations 0.1, 0.3 and 0.5 (7.7.12, simulation);
   the overall F test of a model chosen by forward selection among 50 noise variables (7.7.21, simulation).
B: ratio of the reported to the correct standard error: sleepstudy slope by ordinary least squares and by a
   random-intercept model, against the random-slope model (7.7.17); least-squares fit of a mean squared
   displacement curve, against the spread of the estimates over simulated trajectories (7.7.11).
C: apparent against honestly estimated performance of the birthwt prediction model (7.7.21): AUC and
   calibration slope in the development data, by cross-validation and by bootstrap optimism correction;
   the 27-variable maximum likelihood model against ridge regression under nested cross-validation.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rates = [("10 pairwise t tests, 5 groups", 0.29),
         ("5 unadjusted interim looks", 0.14),
         ("cells as replicates, ICC 0.1", 0.16),
         ("cells as replicates, ICC 0.3", 0.33),
         ("cells as replicates, ICC 0.5", 0.45),
         ("stepwise selection in noise", 0.89)]
ses = [("sleepstudy, OLS", 1.24 / 1.55),
       ("sleepstudy, random intercept", 0.80 / 1.55),
       ("MSD fit, OLS", 0.0044 / 0.219)]
perf = [("AUC", 0.750, 0.695, 0.715),
        ("calibration slope", 1.00, 0.71, 0.81)]

fig = plt.figure(figsize=(12.0, 4.6))
axA = fig.add_axes([0.20, 0.17, 0.20, 0.72])
axB = fig.add_axes([0.59, 0.55, 0.16, 0.34])
axC = fig.add_axes([0.59, 0.17, 0.16, 0.22])
axD = fig.add_axes([0.83, 0.17, 0.15, 0.72])

y = np.arange(len(rates))[::-1]
axA.barh(y, [r for _, r in rates], color=P.fill("negative"), edgecolor=charts.line("negative"), height=0.62)
axA.axvline(0.05, color=P.ink(), lw=1.0, ls="--")
axA.text(0.06, len(rates) - 0.35, "nominal 0.05", fontsize=FT["tiny"], color=P.ink(), va="bottom")
for yy, (name, r) in zip(y, rates):
    axA.text(-0.02, yy, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
             transform=axA.get_yaxis_transform())
    axA.text(r + 0.02, yy, f"{r:.2f}", va="center", fontsize=FT["tiny"], color=P.ink())
axA.set_yticks([])
axA.set_xlim(0, 1)
axA.set_ylim(-0.6, len(rates) - 0.1)
charts.style_axes(axA, "actual false-positive rate")
charts.title(axA, "A  Nominal 5 %, actual", loc="right")

y = np.arange(len(ses))[::-1]
axB.barh(y, [r for _, r in ses], color=P.fill("dna"), edgecolor=charts.line("dna"), height=0.6)
axB.axvline(1, color=P.ink(), lw=1.0, ls="--")
axB.set_xscale("log")
axB.set_xlim(0.01, 1.5)
for yy, (name, r) in zip(y, ses):
    axB.text(-0.02, yy, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
             transform=axB.get_yaxis_transform())
    axB.text(r * 1.12, yy, f"{r:.2f}", va="center", fontsize=FT["tiny"], color=P.ink())
axB.set_yticks([])
charts.style_axes(axB, "reported SE / correct SE")
charts.title(axB, "B  Ignored correlation", loc="right")

labels = ["apparent", "cross-validation", "bootstrap"]
toks = ["neutral", "rna", "enzyme"]
w = 0.26
for j, (lab, tok) in enumerate(zip(labels, toks)):
    vals = [p[1 + j] for p in perf]
    axC.bar(np.arange(2) + (j - 1) * w, vals, w, color=P.fill(tok), edgecolor=charts.line(tok), label=lab)
axC.set_xticks([0, 1])
axC.set_xticklabels([p[0] for p in perf], fontsize=FT["tiny"])
axC.set_ylim(0.5, 1.05)
axC.legend(fontsize=FT["tiny"], frameon=False, loc="upper right", bbox_to_anchor=(-0.04, 1.0), ncol=1)
charts.style_axes(axC)
charts.title(axC, "C  Optimism, birthwt model", loc="right")

models = [("27 variables, ML", 0.35), ("ridge, 27 variables", 1.07)]
axD.bar([0, 1], [m[1] for m in models], 0.55, color=[P.fill("negative"), P.fill("positive")],
        edgecolor=[charts.line("negative"), charts.line("positive")])
axD.axhline(1, color=P.ink(), lw=1.0, ls="--")
for i, (_, v) in enumerate(models):
    axD.text(i, v + 0.03, f"{v:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
axD.set_xticks([0, 1])
axD.set_xticklabels([m[0] for m in models], fontsize=FT["tiny"])
axD.set_ylim(0, 1.3)
charts.style_axes(axD, None, "calibration slope, nested CV")
charts.title(axD, "D  Overfitting and shrinkage", loc="right")
