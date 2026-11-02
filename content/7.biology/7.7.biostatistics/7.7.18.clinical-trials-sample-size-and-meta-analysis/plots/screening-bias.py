"""Biases peculiar to screening.

A: lead time (schematic): screening advances the date of diagnosis without changing the date of death, so
survival measured from diagnosis is longer even when screening does nothing. B: length bias (simulation,
seed 0): tumours with long preclinical phases are over-represented among those found at a single
screening round, because the probability of being caught is proportional to the length of the detectable
preclinical phase. C: the National Lung Screening Trial (Aberle et al. 2011, NEJM; extended follow-up
2019, J Thorac Oncol): lung cancers diagnosed in the low-dose CT and chest-radiography arms at a median
6.5 years and 11.3 years; the early excess of CT-detected cancers largely disappears, which bounds the
amount of overdiagnosis.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.5), gridspec_kw=dict(width_ratios=[1.3, 1, 0.9]))
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.17, top=0.86, wspace=0.32)
ax = axs[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ev = [(1.0, "onset"), (3.5, "detectable"), (6.0, "symptoms"), (9.0, "death")]
for y, dx, name in [(2.1, 6.0, "no screening"), (0.9, 4.2, "screened")]:
    ax.plot([1, 9], [y, y], color=P.muted(), lw=1)
    for x, lab in ev:
        ax.plot(x, y, "o", ms=4, color=P.muted())
    ax.annotate("", xy=(9, y + 0.32), xytext=(dx, y + 0.32),
                arrowprops=dict(arrowstyle="<->", color=charts.line("rna" if dx < 5 else "dna"), lw=1.4))
    ax.text((dx + 9) / 2, y + 0.45, f"survival from diagnosis: {9 - dx:.1f} y", ha="center", fontsize=FT["tiny"],
            color=P.ink())
    ax.plot(dx, y, "D", ms=6, color=charts.line("rna" if dx < 5 else "dna"))
    ax.text(0.9, y, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink())
for x, lab in ev:
    ax.text(x, 0.35, lab, ha="center", fontsize=FT["tiny"], color=P.muted())
ax.text(5.1, 0.55, "lead time", ha="center", fontsize=FT["tiny"], color=charts.line("rna"))
ax.set_title("A  Lead time", loc="left", fontsize=FT["small"], color=P.ink(), weight="bold")
ax = axs[1]
rng = np.random.default_rng(0)
dur = rng.lognormal(np.log(2), 0.8, 20000)
onset = rng.uniform(0, 30, 20000)
caught = (onset <= 20) & (onset + dur >= 20)
bins = np.linspace(0, 12, 41)
ax.hist(dur, bins=bins, density=True, color=P.fill("neutral"), alpha=0.7, label="all tumours")
ax.hist(dur[caught], bins=bins, density=True, histtype="step", color=charts.line("rna"), lw=1.6,
        label="found at one screen")
ax.axvline(np.median(dur), color=P.muted(), lw=0.8, ls="--")
ax.axvline(np.median(dur[caught]), color=charts.line("rna"), lw=0.8, ls="--")
ax.text(0.97, 0.6, f"median {np.median(dur):.1f} y vs {np.median(dur[caught]):.1f} y", transform=ax.transAxes,
        ha="right", fontsize=FT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "detectable preclinical phase / years", "density")
charts.title(ax, "B  Length bias")
ax = axs[2]
fu = np.array([0, 1])
ct = [1060, 1701]
cxr = [941, 1681]
ax.bar(fu - 0.18, ct, 0.34, color=P.fill("rna"), ec=P.edge("rna"), label="low-dose CT")
ax.bar(fu + 0.18, cxr, 0.34, color=P.fill("dna"), ec=P.edge("dna"), label="chest radiograph")
for x, a, b in zip(fu, ct, cxr):
    ax.text(x, max(a, b) + 40, f"excess {a - b}", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(fu)
ax.set_xticklabels(["6.5 y", "11.3 y"])
ax.set_ylim(0, 2050)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "median follow-up", "lung cancers diagnosed")
charts.title(ax, "C  NLST: excess diagnoses")
