"""How a cut-off on a continuous marker trades sensitivity against specificity (binormal model, computed
exactly). A: marker values in people without the disease follow N(0, 1), in people with the disease N(1.5, 1);
with the cut-off at 1.0, the shaded areas are the false negatives (left of the cut-off, diseased) and the
false positives (right of it, healthy). B: the ROC curve traced out by moving the cut-off; the point marks
the cut-off of panel A, the square the cut-off 0.75 that maximizes Youden's index J = Se + Sp - 1.
The area under this curve is Phi(1.5 / sqrt 2) = 0.856.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
mu, c = 1.5, 1.0
x = np.linspace(-3.5, 5, 500)
h, d = stats.norm(0, 1), stats.norm(mu, 1)
fig, axs = plt.subplots(1, 2, figsize=(10.2, 3.7), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.88, wspace=0.25)
ax = axs[0]
ax.plot(x, h.pdf(x), color=charts.line("dna"), lw=1.8, label="without disease")
ax.plot(x, d.pdf(x), color=charts.line("rna"), lw=1.8, label="with disease")
ax.fill_between(x, d.pdf(x), where=x < c, color=P.fill("rna"), alpha=0.6, lw=0)
ax.fill_between(x, h.pdf(x), where=x >= c, color=P.fill("dna"), alpha=0.6, lw=0)
ax.axvline(c, color=P.ink(), lw=1.1, ls="--")
ax.text(c + 0.08, 0.425, "cut-off: test + to the right", fontsize=FT["tiny"], color=P.ink())
ax.text(-0.15, 0.04, f"false negatives\n1 - Se = {d.cdf(c):.2f}", fontsize=FT["tiny"], color=P.ink(), ha="right")
ax.text(2.6, 0.06, f"false positives\n1 - Sp = {h.sf(c):.2f}", fontsize=FT["tiny"], color=P.ink())
ax.set_ylim(0, 0.47)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "marker value", "density")
charts.title(ax, "A  One cut-off, two kinds of error")
ax = axs[1]
cs = np.linspace(-4, 6, 400)
ax.plot(h.sf(cs), d.sf(cs), color=charts.line("enzyme"), lw=1.8)
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls=":")
ax.plot(h.sf(c), d.sf(c), "o", color=P.ink(), ms=5)
cj = mu / 2
ax.plot(h.sf(cj), d.sf(cj), "s", color=charts.line("rna"), ms=5)
ax.annotate(f"max J = {d.sf(cj) - h.sf(cj):.2f}", (h.sf(cj), d.sf(cj)), xytext=(0.45, 0.45), fontsize=FT["tiny"],
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.text(0.55, 0.12, f"AUC = {stats.norm.cdf(mu / np.sqrt(2)):.3f}", fontsize=FT["small"], color=P.ink())
ax.set_aspect("equal")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.01)
charts.style_axes(ax, "1 - specificity", "sensitivity")
charts.title(ax, "B  ROC curve")
