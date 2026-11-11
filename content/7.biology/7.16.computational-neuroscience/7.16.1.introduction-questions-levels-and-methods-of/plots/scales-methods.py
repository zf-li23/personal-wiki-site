"""Spatial and temporal scales accessible to methods in neuroscience (approximate orders of
magnitude, in the spirit of the Churchland-Sejnowski diagram, with current techniques). For each
method, the left bar spans spatial scales from resolution to field of view, the right bar temporal
scales from resolution to the longest practical recording (chronic implants, longitudinal imaging).
Electron microscopy has no temporal extent: it images fixed tissue."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
methods = [  # name, log10 space [m] min, max, log10 time [s] min, max, token
    ("Electron microscopy", -9.0, -3.0, None, None, "neutral"),
    ("Patch clamp", -8.5, -4.5, -4.5, 3.5, "channel"),
    ("Single units", -5.0, -4.0, -4.0, 4.0, "neuron"),
    ("Neuropixels probes", -5.0, -2.0, -4.2, 6.5, "receptor"),
    ("Voltage imaging", -5.5, -3.0, -3.3, 2.0, "highlight"),
    ("2-photon Ca²⁺ imaging", -6.0, -3.0, -1.5, 7.0, "ca"),
    ("Optogenetics", -5.0, -2.0, -3.0, 4.0, "positive"),
    ("EEG / MEG", -2.0, -0.7, -3.0, 4.0, "dna"),
    ("fMRI", -3.0, -0.7, 0.0, 4.5, "blood"),
    ("PET", -2.3, -0.7, 1.5, 4.0, "mitochondrion"),
    ("TMS", -2.0, -1.0, -3.0, 0.5, "negative"),
    ("Lesions", -3.0, -0.7, 5.0, 8.5, "bone"),
]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.6), sharey=True)
fig.subplots_adjust(left=0.19, right=0.98, bottom=0.21, top=0.92, wspace=0.08)
y = np.arange(len(methods))[::-1]
for yi, (name, x0, x1, t0, t1, tok) in zip(y, methods):
    a1.barh(yi, x1 - x0, left=x0, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.9)
    if t0 is not None:
        a2.barh(yi, t1 - t0, left=t0, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.9)
a1.set_yticks(y)
a1.set_yticklabels([m[0] for m in methods])
for ax, lo, hi, step, xl in [(a1, -9, 0, 1, "spatial scale / m"), (a2, -6, 9, 2, "temporal scale / s")]:
    ax.set_xlim(lo - 0.3, hi + 0.3)
    ax.set_xticks(range(lo, hi + 1, step))
    ax.set_xticklabels([f"$10^{{{k}}}$" for k in range(lo, hi + 1, step)])
    charts.style_axes(ax, xl)
a1.set_ylim(-1.9, len(methods) - 0.4)
for x, name in [(-9, "molecule"), (-6, "synapse"), (-4.3, "neuron"), (-3, "circuit"), (-1.7, "area"), (-0.15, "brain")]:
    a1.axvline(x, color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5, zorder=0)
    a1.text(x, -1.45, name, fontsize=FT["tiny"], color=P.muted(), ha="center", va="center")
for t, name in [(-3, "1 ms"), (0, "1 s"), (3.56, "1 h"), (4.94, "1 d"), (7.5, "1 yr")]:
    a2.axvline(t, color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5, zorder=0)
    a2.text(t, -1.45, name, fontsize=FT["tiny"], color=P.muted(), ha="center", va="center")
charts.title(a1, "A  Space")
charts.title(a2, "B  Time")
