"""Which recurring method or principle each chapter of the course relies on.

Columns: chapters 7.16.1-7.16.53 (7.16.54 is this summary). Rows: the methods and principles of
Section 54.10. A filled disc marks a principle that is central to the chapter (it carries a model,
a theorem or the main argument there), an open ring one that appears as a secondary element.
The assignment summarizes the chapters; it is a reading aid, not data.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rows = [
    ("excitability, bifurcation, hysteresis", "channel", "B"),
    ("linearization and eigenmodes", "enzyme", "L"),
    ("mean-field reduction", "neuron", "M"),
    ("balance and homeostasis", "receptor", "E"),
    ("attractors and state-space geometry", "positive", "A"),
    ("normative models and efficiency", "highlight", "N"),
    ("inference and prediction errors", "protein", "P"),
    ("learning rules and credit assignment", "rna", "R"),
    ("encoding, decoding, dimensionality", "neutral", "D"),
]

# chapter: principles, upper case = central, lower case = secondary
use = {
    1: "Nd", 2: "Le", 3: "D", 4: "L", 5: "Bl", 6: "BL", 7: "B", 8: "Bm",
    9: "d", 10: "l", 11: "l", 12: "Le", 13: "L", 14: "REb", 15: "LMEBa",
    16: "D", 17: "Nl", 18: "Lan", 19: "ND", 20: "N", 21: "Re", 22: "RLn", 23: "Ne",
    24: "BN", 25: "le", 26: "DPn", 27: "PN", 28: "DLa", 29: "PNr", 30: "Be", 31: "MAEr",
    32: "AD", 33: "RLAn", 34: "EP", 35: "Bl", 36: "a", 37: "Pr", 38: "R", 39: "PR",
    40: "RP", 41: "R", 42: "Ad", 43: "ARm", 44: "ALM", 45: "AMb", 46: "PRa", 47: "ANPm",
    48: "PRn", 49: "MLD", 50: "Rn", 51: "l", 52: "BE", 53: "n",
}

chapters = sorted(use)
fig, ax = plt.subplots(figsize=(14.0, 4.4))
fig.subplots_adjust(left=0.2, right=0.995, bottom=0.17, top=0.93)
for j, (name, tok, code) in enumerate(rows):
    y = len(rows) - 1 - j
    ax.axhline(y, color=P.muted(), lw=0.3, alpha=0.5, zorder=1)
    for ch in chapters:
        s = use[ch]
        if code in s:
            ax.plot([ch], [y], "o", ms=8, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=3)
        elif code.lower() in s:
            ax.plot([ch], [y], "o", ms=6, mfc="none", mec=P.edge(tok), mew=1.2, zorder=3)
groups = [(1, 3, "frame"), (4, 8, "neurons"), (9, 14, "synapses"), (15, 15, "nets"),
          (16, 28, "coding and the senses"), (29, 33, "movement"), (34, 41, "drives, value, RL"),
          (42, 50, "memory and cognition"), (51, 53, "disease")]
for a, b, txt in groups:
    if b < 53:
        ax.axvline(b + 0.5, color=P.muted(), lw=0.6, ls=":", zorder=0)
    ax.text((a + b) / 2, len(rows) - 0.45, txt, fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xticks(chapters)
ax.set_xticklabels([str(c) for c in chapters])
ax.set_xlim(0.4, 53.6)
ax.set_ylim(-0.6, len(rows) - 0.05)
ax.tick_params(labelsize=FT["tiny"])
charts.style_axes(ax, "chapter (7.16.n)")
