"""Three data structures of biomedical research, each shown with a real data set.

A: cross-sectional data, one row per child and one measurement occasion (first rows of the FEV data,
   Tager et al. 1979). B: longitudinal data, the reaction time of six subjects measured on each of ten days
   of sleep restriction (sleepstudy, Belenky et al. 2003). C: time-to-event data, the follow-up of 16 patients
   of the Veterans' Administration lung cancer trial (Kalbfleisch and Prentice), each line ending in a death
   (filled dot) or a censored time (open circle).
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def read(name):
    with open(name) as fh:
        return list(csv.DictReader(fh))


fig = plt.figure(figsize=(11.0, 3.9))
gs = fig.add_gridspec(1, 3, left=0.03, right=0.985, bottom=0.15, top=0.86, wspace=0.32, width_ratios=[1.15, 1, 1])

# A: the data matrix
ax = fig.add_subplot(gs[0])
ax.axis("off")
rows = read("fev_rows.csv")
cols = ["id", "age", "fev", "height", "sex", "smoke"]
units = ["", "yr", "L", "in", "0/1", "0/1"]
xs = np.linspace(0.05, 0.95, len(cols))
for x, c, u in zip(xs, cols, units):
    ax.text(x, 0.93, c, ha="center", fontsize=FT["small"], color=P.ink(), weight="bold", transform=ax.transAxes)
    ax.text(x, 0.86, u, ha="center", fontsize=FT["tiny"], color=P.muted(), transform=ax.transAxes)
ax.plot([0.0, 1.0], [0.83, 0.83], color=P.muted(), lw=0.8, transform=ax.transAxes)
for i, r in enumerate(rows):
    y = 0.77 - i * 0.083
    for x, c in zip(xs, cols):
        v = r[c]
        if c == "height":
            v = f"{float(v):.1f}"
        elif c == "fev":
            v = f"{float(v):.3f}"
        ax.text(x, y, v, ha="center", fontsize=FT["tiny"], color=P.ink(), transform=ax.transAxes)
ax.text(0.5, 0.06, "... 654 children, each measured once", ha="center", fontsize=FT["tiny"],
        color=P.muted(), transform=ax.transAxes)
ax.annotate("", xy=(-0.02, 0.12), xytext=(-0.02, 0.8), xycoords="axes fraction",
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
ax.text(-0.04, 0.46, "units", rotation=90, ha="center", va="center", fontsize=FT["tiny"], color=P.muted(),
        transform=ax.transAxes)
charts.title(ax, "A  Cross-sectional: units x variables")

# B: longitudinal trajectories
ax = fig.add_subplot(gs[1])
s = read("sleepstudy_subset.csv")
subjects = sorted({r["subject"] for r in s})
for k, sub in enumerate(subjects):
    pts = sorted((int(r["days"]), float(r["reaction"])) for r in s if r["subject"] == sub)
    d, y = zip(*pts)
    ax.plot(d, y, "-o", ms=2.6, lw=1.1, color=charts.line(["dna", "rna", "plant", "protein", "enzyme", "neutral"][k]))
charts.style_axes(ax, "day of sleep restriction", "reaction time / ms")
ax.set_xticks(range(0, 10, 3))
charts.title(ax, "B  Longitudinal: repeated measures")

# C: time-to-event with censoring
ax = fig.add_subplot(gs[2])
v = read("veteran.csv")
v.sort(key=lambda r: int(r["time"]))
for i, r in enumerate(v):
    t, ev = int(r["time"]), int(r["status"])
    tok = "dna" if r["trt"] == "1" else "rna"
    ax.plot([0, t], [i, i], color=charts.line(tok), lw=1.4, solid_capstyle="butt")
    if ev:
        ax.plot(t, i, "o", ms=4.2, color=charts.line(tok))
    else:
        ax.plot(t, i, "o", ms=4.2, mfc="none", mec=charts.line(tok), mew=1.1)
ax.set_yticks([])
ax.set_ylim(-1, len(v))
charts.style_axes(ax, "days since randomization", "patient")
ax.plot([], [], "o", color=P.ink(), ms=4, label="death")
ax.plot([], [], "o", mfc="none", mec=P.ink(), ms=4, label="censored")
ax.plot([], [], color=charts.line("dna"), lw=1.4, label="standard")
ax.plot([], [], color=charts.line("rna"), lw=1.4, label="test")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.title(ax, "C  Time-to-event: follow-up and censoring")
