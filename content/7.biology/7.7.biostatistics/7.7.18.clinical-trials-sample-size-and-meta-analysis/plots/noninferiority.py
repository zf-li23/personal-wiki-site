"""Reading superiority, non-inferiority and equivalence from confidence intervals (schematic).

Each line is the confidence interval for the difference new minus standard in the risk of a bad outcome
(negative favours the new treatment); M is the non-inferiority margin and -M / +M the equivalence margins.
The conclusions in the right column follow from where the interval lies relative to 0 and the margins
(two-sided 95 % intervals for superiority and non-inferiority, 90 % intervals for equivalence by TOST).
"""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
M = 2.0
cases = [(-3.2, -1.0, "superior and non-inferior", "dna"),
         (-1.5, 1.2, "non-inferior and equivalent; not superior", "plant"),
         (-2.6, 1.0, "non-inferior; not equivalent, not superior", "enzyme"),
         (0.3, 1.5, "non-inferior, yet significantly worse", "protein"),
         (-1.0, 2.8, "inconclusive", "neutral"),
         (2.4, 4.0, "inferior", "rna")]
fig, ax = plt.subplots(figsize=(8.6, 3.6))
fig.subplots_adjust(left=0.05, right=0.6, bottom=0.17, top=0.9)
for i, (lo, hi, lab, tok) in enumerate(cases):
    y = len(cases) - i
    ax.plot([lo, hi], [y, y], color=charts.line(tok), lw=2.2, solid_capstyle="butt")
    ax.plot((lo + hi) / 2, y, "o", ms=5, color=charts.line(tok))
    ax.text(5.4, y, lab, va="center", fontsize=FT["tiny"], color=P.ink(), clip_on=False)
ax.axvline(0, color=P.ink(), lw=0.9)
ax.axvline(M, color=charts.line("rna"), lw=1.1, ls="--")
ax.axvline(-M, color=charts.line("rna"), lw=0.8, ls=":")
ax.axvspan(-M, M, color=P.fill("neutral"), alpha=0.12, lw=0)
ax.text(M, len(cases) + 0.7, "+M (non-inferiority margin)", ha="center", fontsize=FT["tiny"], color=charts.line("rna"))
ax.text(-M, len(cases) + 0.7, "-M", ha="center", fontsize=FT["tiny"], color=charts.line("rna"))
ax.set_xlim(-4, 5)
ax.set_ylim(0.4, len(cases) + 1)
ax.set_yticks([])
charts.style_axes(ax, "difference in risk, new minus standard / percentage points")
ax.text(-3.9, 0.55, "favours new", fontsize=FT["tiny"], color=P.muted())
ax.text(4.9, 0.55, "favours standard", ha="right", fontsize=FT["tiny"], color=P.muted())
