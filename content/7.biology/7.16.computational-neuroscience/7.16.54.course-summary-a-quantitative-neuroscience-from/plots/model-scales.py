"""The models of the course placed by the spatial and temporal scale of the process they describe.

Each marker is one model, at the order of magnitude of the size of the structure it describes
(a channel, a synapse, a cell, a circuit, a brain area, the body) and of the time scale of the
process (gating time, membrane or synaptic time constant, period, duration of a trial, of
learning, of a disease or of evolution). The number is the chapter (7.16.n); colour gives the part
of the course. Dotted lines mark reference times: 1 ms (a spike), 1 s (a behavioral trial),
1 day (circadian period, consolidation), 80 years (a human life). Orders of magnitude only.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
MIN, H, D, Y = 60.0, 3600.0, 86400.0, 3.15e7

classes = {
    "chan": ("channel", "molecules and channels"),
    "cell": ("neuron", "neurons and dendrites"),
    "syn": ("receptor", "synapses and plasticity"),
    "net": ("enzyme", "circuits and networks"),
    "sens": ("protein", "coding and the senses"),
    "mot": ("rna", "movement"),
    "val": ("positive", "value, learning, memory"),
    "cog": ("neutral", "cognition, disease, evolution"),
}

models = [  # (length / m, time / s, label, class)
    (1e-8, 1e-3, "channel gating (4)", "chan"),
    (1e-8, 0.1, "TRP thermal gating (25)", "chan"),
    (2e-8, 3e-4, "Ca2+ nanodomain (9)", "chan"),
    (1e-6, 1.0, "GPCR cascade (11)", "chan"),
    (3e-6, 0.2, "phototransduction (17)", "chan"),
    (3e-5, 1e-3, "Hodgkin-Huxley (5)", "chan"),
    (2e-5, 1e-2, "phase plane (6)", "cell"),
    (2e-5, 1.0, "bursting (7)", "cell"),
    (1e-5, 3e-2, "LIF, AdEx (8)", "cell"),
    (5e-4, 1e-2, "cable, Rall (13)", "cell"),
    (1e-2, 2e-3, "conduction (5)", "cell"),
    (1e-6, 2e-3, "binomial release (9)", "syn"),
    (1e-7, 5e-3, "receptor kinetics (10)", "syn"),
    (5e-7, 0.5, "Tsodyks-Markram (12)", "syn"),
    (1e-6, 3e-2, "STDP (14)", "syn"),
    (1e-6, 1 * H, "CaMKII switch (14)", "syn"),
    (1e-4, 3 * D, "synaptic scaling (14)", "syn"),
    (3e-4, 3.0, "BTSP (14, 42)", "syn"),
    (2e-3, 20 * D, "Hebb, Oja, BCM (22)", "syn"),
    (5e-3, 60 * D, "ocular dominance (22)", "syn"),
    (1e-3, 10 * D, "retinotectal map (21)", "syn"),
    (1e-3, 2.5e-2, "PING gamma (15)", "net"),
    (3e-3, 0.1, "Wilson-Cowan (15)", "net"),
    (3e-3, 2.0, "reservoir, FORCE (31)", "net"),
    (0.1, 300.0, "functional connectivity (49)", "net"),
    (2e-2, 1.5e-2, "avalanches (49)", "net"),
    (6e-2, 0.3, "intrinsic time scales (49)", "net"),
    (1e-4, 0.1, "LNP, STA (16)", "sens"),
    (2e-4, 4e-2, "DoG, Reichardt (17)", "sens"),
    (2e-3, 5e-2, "Gabor, ring model (18)", "sens"),
    (5e-2, 0.15, "ventral stream, CNN (19)", "sens"),
    (1e-4, 0.25, "fly hashing (23)", "sens"),
    (3e-2, 1e-3, "cochlear Hopf (24)", "sens"),
    (1e-3, 1e-5, "Jeffress ITD (24)", "sens"),
    (1e-3, 1.0, "pain gate (25)", "sens"),
    (0.1, 0.5, "cue combination (27)", "sens"),
    (1.0, 0.5, "optimal feedback control (29)", "mot"),
    (1.0, 15 * MIN, "motor adaptation (29)", "mot"),
    (2e-2, 0.7, "CPG (30)", "mot"),
    (1.7, 3.0, "inverted pendulum (30)", "mot"),
    (4e-3, 0.4, "M1 rotations (32)", "mot"),
    (1e-2, 2 * D, "VOR learning (33)", "mot"),
    (1e-3, 20.0, "neural integrator (33)", "mot"),
    (2e-3, 10.0, "AgRP need signal (34)", "val"),
    (1e-5, 1 * D, "TTFL clock (35)", "val"),
    (1e-2, 10.0, "sleep flip-flop (35)", "val"),
    (0.1, 1 * D, "two-process model (35)", "val"),
    (1e-2, 2.0, "TD and dopamine (39)", "val"),
    (1.5e-2, 0.12, "action selection (40)", "val"),
    (1e-3, 3 * D, "Aplysia LTF (38)", "val"),
    (3e-2, 30 * D, "addiction (37)", "val"),
    (3e-2, 1 * D, "meta-RL (41)", "val"),
    (1e-3, 0.1, "Hopfield recall (43)", "val"),
    (1e-4, 1.0, "ring attractor (44)", "val"),
    (2e-3, 3.0, "working memory (45)", "val"),
    (1e-2, 100.0, "successor representation (46)", "val"),
    (7e-3, 1.5, "DDM, Wong-Wang (47)", "val"),
    (5e-2, 1 * Y, "consolidation (42)", "val"),
    (1.2e-1, 3e-2, "predictive coding (48)", "cog"),
    (1e-8, 10 * H, "aggregation (51)", "cog"),
    (0.1, 10 * Y, "network spread (51)", "cog"),
    (1e-2, 30.0, "seizure dynamics (52)", "cog"),
    (1e-2, 3e5 * Y, "camera eye (53)", "cog"),
    (0.1, 3e6 * Y, "gene families (53)", "cog"),
]

fig, ax = plt.subplots(figsize=(13.5, 9.5))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.14, top=0.98)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(3e-9, 5.0)
ax.set_ylim(3e-6, 5e14)

refs = [(1e-3, "1 ms: a spike"), (1.0, "1 s: a trial"), (D, "1 day"), (80 * Y, "a human life")]
for t, txt in refs:
    ax.axhline(t, color=P.muted(), lw=0.6, ls=":", zorder=1)
    ax.text(4.5, t * 1.25, txt, fontsize=FT["tiny"], color=P.muted(), ha="right", va="bottom")

for Lm, t, txt, cl in models:
    tok = classes[cl][0]
    ax.plot([Lm], [t], "o", ms=6.5, color=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)

# greedy label placement: try offsets around each marker, keep the first that overlaps nothing
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
placed = []
pts = [ax.transData.transform((m[0], m[1])) for m in models]
base = [(6, 3, "left", "bottom"), (6, -3, "left", "top"), (-6, 3, "right", "bottom"), (-6, -3, "right", "top"),
        (0, 7, "center", "bottom"), (0, -7, "center", "top"), (10, 10, "left", "bottom"), (10, -10, "left", "top"),
        (-10, 10, "right", "bottom"), (-10, -10, "right", "top"), (0, 15, "center", "bottom"), (0, -15, "center", "top")]
offsets = [(dx * f, dy * f, ha, va) for f in (1, 2.0, 3.0) for dx, dy, ha, va in base]


def cost(bb):
    """Overlap area with placed labels and markers, plus a large penalty outside the axes."""
    c = 0.0
    for o in placed:
        w = min(bb.x1, o.x1) - max(bb.x0, o.x0)
        h = min(bb.y1, o.y1) - max(bb.y0, o.y0)
        if w > 0 and h > 0:
            c += w * h
    for p in pts:
        if bb.x0 - 5 < p[0] < bb.x1 + 5 and bb.y0 - 5 < p[1] < bb.y1 + 5:
            c += 200.0
    axbb = ax.get_window_extent()
    if bb.x0 < axbb.x0 or bb.x1 > axbb.x1 or bb.y0 < axbb.y0 or bb.y1 > axbb.y1:
        c += 1e6
    return c


for (Lm, t, txt, cl), p in zip(models, pts):
    best = None
    for k, (dx, dy, ha, va) in enumerate(offsets):
        tx = ax.annotate(txt, (Lm, t), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                         fontsize=FT["tiny"], color=P.ink(), zorder=6)
        bb = tx.get_window_extent(renderer)
        c = cost(bb) + 0.5 * k
        tx.remove()
        if best is None or c < best[0]:
            best = (c, dx, dy, ha, va)
        if c < 1.0:
            break
    _, dx, dy, ha, va = best
    tx = ax.annotate(txt, (Lm, t), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                     fontsize=FT["tiny"], color=P.ink(), zorder=6)
    placed.append(tx.get_window_extent(renderer))

xt = [1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]
ax.set_xticks(xt)
ax.set_xticklabels(["10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm", "10 cm", "1 m"])
yt = [1e-5, 1e-3, 1.0, MIN, H, D, Y, 100 * Y, 1e4 * Y, 1e6 * Y]
ax.set_yticks(yt)
ax.set_yticklabels(["10 µs", "1 ms", "1 s", "1 min", "1 h", "1 day", "1 year", "100 years",
                    "10⁴ years", "10⁶ years"])
ax.minorticks_off()
charts.style_axes(ax, "size of the structure described", "time scale of the process")

items = list(classes.values())
for k, (tok, name) in enumerate(items):
    xx = 0.03 + 0.24 * (k % 4)
    yy = 0.045 if k < 4 else 0.018
    fig.add_artist(plt.Line2D([xx], [yy], marker="o", ms=6.5, color=P.fill(tok), mec=P.edge(tok),
                              mew=0.9, transform=fig.transFigure))
    fig.text(xx + 0.01, yy, name, fontsize=FT["tiny"], color=P.ink(), ha="left", va="center")
