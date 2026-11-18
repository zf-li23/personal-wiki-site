"""Which families of models each chapter of the course uses.

Columns: chapters 7.19.1-7.19.54 (7.19.55 is this summary), grouped into the levels of the course.
Rows: the eight model families of Section 55.2. A filled disc marks a family that carries the main
argument of the chapter, an open ring one that appears as a secondary tool. The assignment summarizes
the chapters; it is a reading aid, not data.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rows = [
    ("individual performance, energetics", "neuron", "P"),
    ("growth and regulation", "positive", "G"),
    ("structure and chance", "protein", "S"),
    ("space", "dna", "X"),
    ("species interactions", "negative", "I"),
    ("community theory", "rna", "C"),
    ("compartments, energy flow, climate", "enzyme", "E"),
    ("harvesting and conservation", "metabolite", "H"),
]

# chapter: families, upper case = central, lower case = secondary
use = {
    1: "gs", 2: "P", 3: "Pe", 4: "P", 5: "Ps", 6: "Pe", 7: "P",
    8: "S", 9: "Sg", 10: "Gh", 11: "G", 12: "G", 13: "Gs", 14: "Sh", 15: "Sh", 16: "Xh", 17: "X",
    18: "Ps", 19: "Ps", 20: "S", 21: "gs",
    22: "I", 23: "Ic", 24: "ip", 25: "I", 26: "I", 27: "Ix", 28: "Ig", 29: "I", 30: "XI",
    31: "Cs", 32: "Cs", 33: "Ci", 34: "Cx", 35: "Cp", 36: "Cse", 37: "CS", 38: "CI", 39: "ICe",
    40: "E", 41: "Pe", 42: "Ep", 43: "E", 44: "E", 45: "E", 46: "E", 47: "Ex",
    48: "X", 49: "Xs",
    50: "ch", 51: "Hsx", 52: "Hs", 53: "Hgi", 54: "Hei",
}

chapters = sorted(use)
fig, ax = plt.subplots(figsize=(14.0, 3.9))
fig.subplots_adjust(left=0.215, right=0.995, bottom=0.17, top=0.88)
for j, (name, tok, code) in enumerate(rows):
    y = len(rows) - 1 - j
    ax.axhline(y, color=P.muted(), lw=0.3, alpha=0.5, zorder=1)
    for ch in chapters:
        s = use[ch]
        if code in s:
            ax.plot([ch], [y], "o", ms=8.5, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=3)
        elif code.lower() in s:
            ax.plot([ch], [y], "o", ms=6, mfc="none", mec=P.edge(tok), mew=1.2, zorder=3)

groups = [(1, 7, "individual"), (8, 21, "population"), (22, 30, "interactions"),
          (31, 39, "community"), (40, 47, "ecosystem, globe"), (48, 49, "landscape"),
          (50, 54, "applied")]
for a, b, txt in groups:
    if b < 54:
        ax.axvline(b + 0.5, color=P.muted(), lw=0.6, ls=":", zorder=0)
    ax.text((a + b) / 2, len(rows) - 0.55, txt, fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")

ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xticks(chapters)
ax.set_xticklabels([str(c) for c in chapters])
ax.set_xlim(0.4, 54.6)
ax.set_ylim(-0.6, len(rows) - 0.1)
charts.style_axes(ax, "chapter (7.19.n)")
ax.tick_params(axis="x", labelsize=FT["tiny"])
ax.tick_params(axis="y", labelsize=FT["small"])
