"""The time, force and energy scales of the cell, collected from the chapters of 7.3.

A: characteristic times of cellular processes on one logarithmic axis, from the capture of free Ca2+
by buffers to the decades over which elastin turns over; the three bands below the axis are the
speeds of signaling responses (channels, covalent modification, transcription; 7.3.18).
B: forces at the molecular scale (piconewtons). C: energies in units of k_B T (37 degrees C).
Every value is one quoted in the course; the chapter number is given after each label.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FS = 7.2

fig = plt.figure(figsize=(12.5, 7.4))
gs = fig.add_gridspec(3, 1, height_ratios=[4.2, 1.35, 1.35], hspace=0.55)
ax = fig.add_subplot(gs[0])
MIN, H, D, Y = 60.0, 3600.0, 86400.0, 3.15e7
times = [  # (seconds, label, token, label level, alignment)
    (5e-5, "Ca²⁺ captured by buffers (18)", "ca", 0, "center"),
    (5e-4, "Ca²⁺-triggered exocytosis (9)", "vesicle", 1, "center"),
    (1e-3, "action-potential upstroke (5)", "neuron", 2, "center"),
    (1e-2, "one kinesin step (14)", "protein", 3, "center"),
    (2.5, "FRAP half-recovery (2)", "positive", 0, "center"),
    (30, "actin turnover in cells (13)", "protein", 1, "center"),
    (1 * MIN, "coated pit → vesicle (10)", "vesicle", 2, "center"),
    (3 * MIN, "Rab5 → Rab7 switch (8)", "golgi", 3, "center"),
    (9 * MIN, "caspase-3 activation (25)", "negative", 4, "center"),
    (20 * MIN, "Golgi transit (9)", "golgi", 5, "center"),
    (1 * H, "mitosis (21)", "chromatin", 0, "center"),
    (100 * MIN, "NF-κB period (19)", "receptor", 1, "center"),
    (2 * H, "Hes1 period (24)", "dna", 2, "center"),
    (5.5 * H, "p53 pulses (22)", "negative", 3, "center"),
    (24 * H, "cell cycle, circadian clock (20, 24)", "chromatin", 4, "left"),
    (42 * D, "crypt becomes monoclonal (24)", "highlight", 0, "center"),
    (120 * D, "red-cell lifespan (24)", "blood", 1, "center"),
    (17 * Y, "adenoma → carcinoma (26)", "negative", 2, "center"),
    (50 * Y, "elastin half-life (23)", "neutral", 3, "right"),
]
ax.set_xscale("log")
ax.set_xlim(1e-5, 1e10)
ax.set_ylim(-2.2, 4.6)
ax.axhline(0, color=P.muted(), lw=1.0)
for t, txt, tok, lev, ha in times:
    y = 0.5 + 0.72 * lev
    ax.plot([t, t], [0, y - 0.12], color=P.muted(), lw=0.6)
    ax.plot([t], [0], "o", ms=6.5, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=5)
    ax.text(t * (0.8 if ha == "left" else 1.25 if ha == "right" else 1), y, txt, ha=ha, va="bottom", fontsize=FS, color=P.ink())
bands = [(1e-4, 1e-1, "ion channels: ms", "channel"), (1.0, 3e3, "modification: s–min", "enzyme"),
         (1.5e3, 1.5e5, "transcription: h", "dna")]
for i, (a, b, txt, tok) in enumerate(bands):
    y = -0.9 - 0.55 * (i % 2)
    ax.fill_between([a, b], y - 0.2, y + 0.2, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.text(np.sqrt(a * b), y, txt, ha="center", va="center", fontsize=FS, color=P.on_fill())
ticks = [1e-4, 1e-2, 1, MIN, H, D, 30 * D, Y, 10 * Y, 100 * Y]
ax.set_xticks(ticks)
ax.set_xticklabels(["0.1 ms", "10 ms", "1 s", "1 min", "1 h", "1 d", "1 month", "1 yr", "10 yr", "100 yr"])
ax.minorticks_off()
ax.set_yticks([])
charts.style_axes(ax, "characteristic time (logarithmic scale)")
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_position(("data", -2.1))
ax.text(1.3e-5, 4.55, "A", fontsize=11.5, fontweight="bold", color=P.ink(), va="top")


def ladder(axis, items, xlim, ticks, names, xlabel, letter):
    axis.set_xscale("log")
    axis.set_xlim(*xlim)
    axis.set_ylim(-0.6, 2.6)
    axis.axhline(0, color=P.muted(), lw=1.0)
    for k, item in enumerate(items):
        v, txt, tok = item[:3]
        lev, ha = item[3:] if len(item) > 3 else (k % 2, "center")
        y = 0.45 + 0.75 * lev
        axis.plot([v, v], [0, y - 0.1], color=P.muted(), lw=0.6)
        axis.plot([v], [0], "o", ms=6.5, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=5)
        axis.text(v * (0.9 if ha == "left" else 1.1 if ha == "right" else 1), y, txt, ha=ha, va="bottom", fontsize=FS, color=P.ink())
    axis.set_xticks(ticks)
    axis.set_xticklabels(names)
    axis.minorticks_off()
    axis.set_yticks([])
    charts.style_axes(axis, xlabel)
    axis.spines["left"].set_visible(False)
    axis.spines["bottom"].set_position(("data", -0.5))
    axis.text(xlim[0] * 1.15, 2.35, letter, fontsize=11.5, fontweight="bold", color=P.ink(), va="top")


forces = [
    (4.28 / 2.7, "kT / δ for actin (13)", "neutral", 0, "center"),
    (5.0, "talin unfolds (23)", "protein", 0, "right"),
    (6.0, "kinesin-1 stall (14)", "protein", 1, "center"),
    (7.0, "actin ratchet stall (13)", "positive", 2, "left"),
    (12.0, "catch-bond optimum (23)", "receptor", 0, "left"),
    (26.0, "Δψ pull on a presequence (6)", "mitochondrion", 1, "center"),
]
ladder(fig.add_subplot(gs[1]), forces, (0.3, 60), [0.5, 1, 2, 5, 10, 20, 50],
       ["0.5", "1", "2", "5", "10", "20", "50"], "force / pN", "B")

energies = [
    (1.0, "thermal energy (1 kT)", "neutral"),
    (38 / 2.58, "one H⁺ into gastric juice (5)", "h"),
    (65.0, "SNARE zippering (8)", "vesicle"),
    (500.0, "bending a vesicle, 8πκ (4, 8)", "lipid_head"),
]
ladder(fig.add_subplot(gs[2]), energies, (0.4, 2000), [0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],
       ["0.5", "1", "2", "5", "10", "20", "50", "100", "200", "500", "1000"], "energy / kT", "C")
