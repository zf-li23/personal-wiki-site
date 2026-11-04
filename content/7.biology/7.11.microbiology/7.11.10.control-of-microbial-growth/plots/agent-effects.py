# Static, cidal and lytic agents, and the minimum inhibitory concentration.
# A-C: an exponentially growing culture (doubling time 40 min) receives an inhibitory concentration of an
#    agent at t = 2 h (arrow). Total cells (turbidity) and viable cells (CFU) on a log scale (model curves):
#    a bacteriostatic agent stops growth of both, and growth resumes if the agent is removed (dotted, removal
#    at 5 h); a bactericidal agent kills (viable count falls, first order, rate 1.5 per h) but the dead cells
#    stay intact, so turbidity is unchanged; a bacteriolytic agent kills and lyses, so both fall.
# D: broth dilution test for the MIC: twofold dilutions of the agent (0.25 to 32 ug/mL) inoculated with the
#    same number of cells; after incubation the tubes below the MIC are turbid. Here the MIC is 4 ug/mL.
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(14.5, 4.0))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.25], wspace=0.33)
t = np.linspace(0, 6, 400)
k = math.log(2) / (40 / 60)
t0 = 2.0
N0 = 1e6
pre = N0 * np.exp(k * np.minimum(t, t0))
Nt0 = N0 * math.exp(k * t0)
cases = []
# static
tot_s = np.where(t < t0, pre, Nt0)
rem = np.where(t < 5, tot_s, Nt0 * np.exp(k * (t - 5)))
cases.append(("A   Bacteriostatic", tot_s, tot_s, rem))
# cidal
via_c = np.where(t < t0, pre, Nt0 * np.exp(-1.5 * (t - t0)))
cases.append(("B   Bactericidal", np.where(t < t0, pre, Nt0), via_c, None))
# lytic
via_l = via_c
tot_l = np.where(t < t0, pre, Nt0 * (0.05 + 0.95 * np.exp(-1.2 * (t - t0))))
cases.append(("C   Bacteriolytic", tot_l, via_l, None))
for i, (title, tot, via, extra) in enumerate(cases):
    ax = fig.add_subplot(gs[0, i])
    ax.plot(t, tot, color=charts.line("neutral"), lw=2.0, ls="--", label="total cells (turbidity)")
    ax.plot(t, via, color=charts.line("bacterium"), lw=2.0, label="viable cells")
    if extra is not None:
        ax.plot(t[t >= 5], extra[t >= 5], color=charts.line("bacterium"), lw=1.4, ls=":")
        ax.text(4.3, Nt0 * 2.2, "agent\nremoved", fontsize=6.8, color=P.muted())
    ax.annotate("", xy=(t0, 2e6), xytext=(t0, 6e5), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0))
    ax.text(t0, 4.5e5, "agent\nadded", ha="center", va="top", fontsize=6.8, color=P.ink())
    ax.set_yscale("log")
    ax.set_ylim(1e5, 6e7)
    ax.set_xlim(0, 6)
    if i == 0:
        ax.legend(fontsize=6.8, frameon=False, loc="upper left")
    charts.style_axes(ax, "time / h", "cells / mL$^{-1}$" if i == 0 else None)
    charts.title(ax, title)

# ---- D: MIC tubes ----------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 3])
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "D   Broth dilution: MIC")
conc = [32, 16, 8, 4, 2, 1, 0.5, 0.25]
mic = 4
turbid = P.mix(P.fill("bacterium"), P.surface(), 0.15)
clear = P.mix(P.fill("metabolite"), P.surface(), 0.8)
w, h, y0 = 0.8, 3.0, 1.6
for j, c in enumerate(conc):
    x = 0.4 + j * 1.18
    r = w / 2
    th = np.linspace(np.pi, 2 * np.pi, 30)
    liq = np.r_[[[x, y0 + h * 0.7]], np.c_[x + r + r * np.cos(th), y0 + r + r * np.sin(th)], [[x + w, y0 + h * 0.7]]]
    ax.add_patch(PathPatch(Path(liq), facecolor=turbid if c < mic else clear, edgecolor="none"))
    wall = np.r_[[[x, y0 + h]], np.c_[x + r + r * np.cos(th), y0 + r + r * np.sin(th)], [[x + w, y0 + h]]]
    ax.add_patch(PathPatch(Path(wall), fill=False, edgecolor=P.muted(), lw=1.0))
    ax.text(x + r, y0 - 0.35, f"{c:g}", ha="center", va="top", fontsize=6.8, color=P.ink(),
            weight="bold" if c == mic else "normal")
ax.text(5.0, y0 - 1.05, "agent / ($\\mu$g mL$^{-1}$)", ha="center", va="top", fontsize=7, color=P.ink())
xm = 0.4 + conc.index(mic) * 1.18 + w / 2
ax.annotate("MIC", xy=(xm, y0 + h + 0.1), xytext=(xm, y0 + h + 0.9), ha="center", fontsize=7.5, color=P.ink(),
            weight="bold", arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
ax.text(2.2, 5.6, "no growth (clear)", ha="center", fontsize=6.8, color=P.muted())
ax.text(7.6, 5.6, "growth (turbid)", ha="center", fontsize=6.8, color=P.muted())
