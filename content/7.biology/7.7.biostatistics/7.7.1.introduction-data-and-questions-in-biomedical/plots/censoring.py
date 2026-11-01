"""Right censoring in a study with staggered entry (schematic with invented times).

Left: calendar time. Eight patients enter a trial between months 0 and 24 and are followed until death
(filled dot), loss to follow-up (open circle before the end of the study) or the end of the study at month 36
(administrative censoring, open circle on the dashed line). Right: the same follow-up on the study time
scale, every patient starting at time 0; the analysis uses this scale, and for a censored patient we know
only that the survival time exceeds the observed time.
"""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
# entry month, end month, outcome: 1 death, 0 lost to follow-up, 2 alive at study end
pts = [(0, 14, 1), (2, 36, 2), (5, 21, 0), (8, 30, 1), (11, 36, 2), (15, 26, 1), (19, 36, 2), (22, 29, 0)]
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5), sharey=True)
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.12)
end = 36
for k, ax in enumerate(axs):
    for i, (a, b, o) in enumerate(pts):
        y = len(pts) - i
        x0, x1 = (a, b) if k == 0 else (0, b - a)
        tok = "rna" if o == 1 else "dna"
        ax.plot([x0, x1], [y, y], color=charts.line(tok), lw=1.6, solid_capstyle="butt")
        if o == 1:
            ax.plot(x1, y, "o", ms=5, color=charts.line(tok))
        else:
            ax.plot(x1, y, "o", ms=5, mfc="none", mec=charts.line(tok), mew=1.2)
        if k == 0 and o == 0:
            ax.text(x1 + 0.8, y, "lost", va="center", fontsize=FT["tiny"], color=P.muted())
    ax.set_yticks(range(1, len(pts) + 1))
    ax.set_yticklabels([str(len(pts) + 1 - j) for j in range(1, len(pts) + 1)])
    ax.set_ylim(0.3, len(pts) + 0.7)
axs[0].axvline(end, color=P.muted(), lw=0.9, ls="--")
axs[0].text(end - 0.5, 0.55, "study ends", ha="right", fontsize=FT["tiny"], color=P.muted())
axs[0].set_xlim(-1, 40)
axs[1].set_xlim(-1, 40)
charts.style_axes(axs[0], "calendar time / months", "patient")
charts.style_axes(axs[1], "time since entry / months")
charts.title(axs[0], "A  Staggered entry, calendar time")
charts.title(axs[1], "B  Study time: all patients start at 0")
axs[1].plot([], [], "o", color=charts.line("rna"), ms=5, label="death (event)")
axs[1].plot([], [], "o", mfc="none", mec=charts.line("dna"), ms=5, label="censored")
axs[1].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
