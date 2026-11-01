"""Sensitivity to an unmeasured confounder U. For an observed risk ratio RR, a binary confounder can
fully explain the association only if RR_EU x RR_UD / (RR_EU + RR_UD - 1) >= RR, where RR_EU is the
ratio of the prevalence of U in exposed and unexposed people and RR_UD the risk ratio of U for the
outcome (Ding and VanderWeele 2016). Curves: the joint strengths that just explain away RR = 1.54
(the square root of 2.36, the adjusted odds ratio of smoking for low birth weight, approximating the risk ratio), RR = 3
and RR = 14.6 (current smokers' lung cancer death rate ratio, British doctors). Dots mark the E-value,
where both strengths are equal: 2.44, 5.45 and 28.7.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(6.2, 4.2))
fig.subplots_adjust(left=0.12, right=0.96, bottom=0.14, top=0.95)
for rr, tok in ((np.sqrt(2.36), "rna"), (3.0, "enzyme"), (14.6, "dna")):
    # solve RR_UD for a given RR_EU: a b / (a + b - 1) = rr  ->  b = rr (a - 1) / (a - rr)
    a = np.geomspace(rr * 1.0005, 400, 400)
    bb = rr * (a - 1) / (a - rr)
    ax.plot(a, bb, color=charts.line(tok), lw=1.7, label=f"observed RR = {rr:.3g}")
    e = rr + np.sqrt(rr * (rr - 1))
    ax.plot(e, e, "o", ms=6, color=P.fill(tok), mec=charts.line(tok))
    ax.text(e * 1.12, e * 1.12, f"E = {e:.2f}", fontsize=FT["tiny"], color=charts.line(tok))
ax.plot([1, 400], [1, 400], color=P.muted(), lw=0.7, ls=":")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1, 200)
ax.set_ylim(1, 200)
ticks = [1, 2, 5, 10, 20, 50, 100, 200]
ax.set_xticks(ticks)
ax.set_xticklabels([str(t) for t in ticks])
ax.set_yticks(ticks)
ax.set_yticklabels([str(t) for t in ticks])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center", bbox_to_anchor=(0.47, 1.0))
charts.style_axes(ax, "RR_EU: prevalence ratio of U, exposed vs unexposed", "RR_UD: risk ratio of U for outcome")
