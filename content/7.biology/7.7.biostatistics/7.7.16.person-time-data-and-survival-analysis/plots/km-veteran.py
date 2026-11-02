"""Kaplan-Meier estimates for the Veterans' Administration lung cancer trial (137 patients, 128 deaths;
Kalbfleisch and Prentice; R package survival, data set veteran).

A: standard vs test chemotherapy, with 95 % pointwise log(-log) Greenwood bands, censoring ticks, the
log-rank test and the number at risk below the axis. The curves cross near day 150.
B: the four histological cell types, with the 3-df log-rank test.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts, stats

P = bio.P
FT = bio.core.FONT

rows = list(csv.DictReader(open("veteran.csv")))
time = np.array([float(r["time"]) for r in rows])
event = np.array([int(r["status"]) for r in rows])
trt = np.array([int(r["trt"]) for r in rows])
cell = np.array([r["celltype"] for r in rows])


def steps(km, t_end):
    xs = np.r_[np.repeat(km.times, 2)[1:], t_end]
    return xs, np.repeat(km.S, 2), np.repeat(km.lo, 2), np.repeat(km.hi, 2)


def draw(ax, mask, tok, label, band=True):
    km = stats.kaplan_meier(time[mask], event[mask])
    t_end = time[mask].max()
    xs, ys, lo, hi = steps(km, t_end)
    if band:
        ax.fill_between(xs, lo, hi, color=P.fill(tok), alpha=0.25, lw=0)
    ax.plot(xs, ys, color=charts.line(tok), lw=1.6, label=label)
    ax.plot(km.censored, km.S_censored, "|", color=charts.line(tok), ms=6, mew=1.1)
    return km


fig = plt.figure(figsize=(10.2, 4.0))
axA = fig.add_axes([0.08, 0.30, 0.39, 0.62])
axB = fig.add_axes([0.59, 0.30, 0.39, 0.62])
kms = [draw(axA, trt == 1, "dna", "standard (n = 69)"), draw(axA, trt == 2, "rna", "test (n = 68)")]
lr = stats.logrank(time, event, trt)
axA.text(560, 0.82, f"log-rank $\\chi^2_1$ = {lr['chi2']:.3f}, p = {lr['p']:.2f}", fontsize=FT["tiny"], color=P.ink())
for km, tok in zip(kms, ["dna", "rna"]):
    axA.plot([km.median], [0.5], "o", ms=3, color=charts.line(tok))
axA.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
axA.set_xlim(0, 1000)
axA.set_ylim(0, 1.02)
axA.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1, 0.78))
charts.style_axes(axA, "days since randomization", "survival probability")
charts.title(axA, "A  Treatment arms (randomized)")
ticks = [0, 100, 200, 300, 400, 500, 600, 800, 1000]
for j, (arm, tok, name) in enumerate([(1, "dna", "standard"), (2, "rna", "test")]):
    y = -0.31 - 0.08 * j
    axA.text(-40, y, name, transform=axA.get_xaxis_transform(), ha="right", fontsize=FT["tiny"],
             color=charts.line(tok))
    for t in ticks:
        axA.text(t, y, str(int((time[trt == arm] >= t).sum())), transform=axA.get_xaxis_transform(),
                 ha="center", fontsize=FT["tiny"], color=charts.line(tok))
axA.text(-40, -0.23, "at risk", transform=axA.get_xaxis_transform(), ha="right", fontsize=FT["tiny"],
         color=P.muted())

for c, tok in [("squamous", "dna"), ("smallcell", "rna"), ("adeno", "protein"), ("large", "plant")]:
    m = cell == c
    km = stats.kaplan_meier(time[m], event[m])
    draw(axB, m, tok, f"{c} (n = {m.sum()}, median {km.median:.0f} d)", band=False)
lr4 = stats.logrank(time, event, cell)
axB.text(450, 0.55, f"log-rank $\\chi^2_3$ = {lr4['chi2']:.1f}\np = {lr4['p']:.1e}", fontsize=FT["tiny"], color=P.ink())
axB.set_xlim(0, 1000)
axB.set_ylim(0, 1.02)
axB.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(axB, "days since randomization", "survival probability")
charts.title(axB, "B  Histological cell type")
