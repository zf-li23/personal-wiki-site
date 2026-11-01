"""Paired data: systolic blood pressure of 15 hypertensive patients before and after captopril
(MacGregor et al. 1979, BMJ 2:1106). A: each patient's two readings joined by a line. B: before against
after; the strong correlation (r = 0.90) between the two readings of the same patient is what the paired
design exploits. C: the 15 differences (before - after) with their mean and 95 % t interval, against 0 and
the clinically relevant 10 mmHg.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
before = np.array([210, 169, 187, 160, 167, 176, 185, 206, 173, 146, 174, 201, 198, 148, 154.0])
after = np.array([201, 165, 166, 157, 147, 145, 168, 180, 147, 136, 151, 168, 179, 129, 131.0])
d = before - after
n = d.size
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=[1, 1.1, 1]))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.38)

ax = axs[0]
for b, a in zip(before, after):
    ax.plot([0, 1], [b, a], color=P.mix(charts.line("dna"), P.surface(), 0.35), lw=0.9)
ax.plot(np.zeros(n), before, "o", ms=4, color=charts.line("dna"))
ax.plot(np.ones(n), after, "o", ms=4, color=charts.line("rna"))
ax.set_xticks([0, 1])
ax.set_xticklabels(["before", "after"], fontsize=FT["tiny"])
ax.set_xlim(-0.3, 1.3)
charts.style_axes(ax, None, "systolic BP / mmHg")
charts.title(ax, "A  Each patient, two readings")

ax = axs[1]
ax.plot(before, after, "o", ms=4, color=charts.line("enzyme"))
lim = [120, 215]
ax.plot(lim, lim, color=P.muted(), lw=0.8, ls="--")
ax.text(196, 207, "after = before", fontsize=FT["tiny"], color=P.muted(), ha="right")
r = np.corrcoef(before, after)[0, 1]
ax.text(124, 205, f"r = {r:.2f}", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(lim)
ax.set_ylim(lim)
charts.style_axes(ax, "before / mmHg", "after / mmHg")
charts.title(ax, "B  Readings are correlated")

ax = axs[2]
rng = np.random.default_rng(0)
ax.scatter(rng.uniform(-0.12, 0.12, n), d, s=14, color=charts.line("rna"), lw=0, zorder=3)
se = d.std(ddof=1) / np.sqrt(n)
h = stats.t.isf(0.025, n - 1) * se
ax.errorbar(0.4, d.mean(), h, fmt="o", ms=5, color=P.ink(), capsize=4, lw=1.2)
ax.text(0.5, d.mean(), f"mean {d.mean():.1f}\n95% CI {d.mean() - h:.1f} to {d.mean() + h:.1f}",
        fontsize=FT["tiny"], color=P.ink(), va="center")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.axhline(10, color=P.muted(), lw=0.8, ls=":")
ax.text(-0.3, 11, "10 mmHg", fontsize=FT["tiny"], color=P.muted())
ax.set_xlim(-0.35, 1.25)
ax.set_xticks([])
charts.style_axes(ax, None, "before - after / mmHg")
charts.title(ax, "C  Differences d = before - after")
