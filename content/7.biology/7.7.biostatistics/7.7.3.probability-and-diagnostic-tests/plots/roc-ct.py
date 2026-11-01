"""Empirical ROC curve of a radiologist's five-point rating of 109 CT images (58 normal, 51 abnormal;
Hanley and McNeil 1982). Each point corresponds to calling 'test positive' all ratings at or above a level
(5+, 4+, 3+, 2+). The trapezoidal area under the curve is 0.893, the probability that a randomly chosen
abnormal image is rated higher than a randomly chosen normal one (ties counted as one half). Youden's
index is largest (0.64) for the criterion 4+.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
normal = np.array([33, 6, 6, 11, 2])
abnormal = np.array([3, 2, 2, 11, 33])
se = np.array([abnormal[k:].sum() / abnormal.sum() for k in range(6)])
sp = np.array([normal[:k].sum() / normal.sum() for k in range(6)])
fpr, tpr = 1 - sp, se
auc = np.trapezoid(tpr[::-1], fpr[::-1])
J = se + sp - 1
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1, 1.05]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.88, wspace=0.28)
ax = axs[0]
w = 0.38
r = np.arange(1, 6)
ax.bar(r - w / 2, normal, w, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, label="truly normal (58)")
ax.bar(r + w / 2, abnormal, w, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.8, label="truly abnormal (51)")
ax.set_xticks(r)
ax.set_xticklabels(["1\ndefinitely\nnormal", "2", "3\nquestion-\nable", "4", "5\ndefinitely\nabnormal"], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(ax, None, "number of images")
charts.title(ax, "A  CT ratings by true status")
ax = axs[1]
ax.fill_between(fpr[::-1], tpr[::-1], color=P.fill("enzyme"), alpha=0.35, lw=0)
ax.plot(fpr, tpr, "-o", color=charts.line("enzyme"), lw=1.6, ms=4)
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls=":")
for k, lab in zip(range(1, 5), ["2+", "3+", "4+", "5+"]):
    ax.text(fpr[k] + 0.03, tpr[k] - 0.055, f"{lab} ({fpr[k]:.2f}, {tpr[k]:.2f})", fontsize=FT["tiny"], color=P.ink())
kb = int(np.argmax(J))
ax.plot(fpr[kb], tpr[kb], "s", color=charts.line("rna"), ms=6)
ax.text(0.45, 0.25, f"AUC = {auc:.3f}\nmax J = {J[kb]:.2f} at 4+", fontsize=FT["small"], color=P.ink())
ax.set_aspect("equal")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
charts.style_axes(ax, "1 - specificity", "sensitivity")
charts.title(ax, "B  Empirical ROC curve")
