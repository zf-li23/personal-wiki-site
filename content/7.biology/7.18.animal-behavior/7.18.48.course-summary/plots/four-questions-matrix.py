"""Which of Tinbergen's four questions each chapter of the course mainly answers.

Columns: chapters 7.18.1-7.18.47 (7.18.48 is this summary), grouped into the seven parts of the
course. Rows: mechanism, development, function, evolution. A filled disc marks a question that
carries the main argument of the chapter, an open ring one that appears as a secondary theme.
The assignment summarizes the chapters; it is a reading aid, not data.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rows = [
    ("mechanism (causation)", "neuron", "M"),
    ("development (ontogeny)", "protein", "D"),
    ("function (adaptive value)", "positive", "F"),
    ("evolution (phylogeny)", "rna", "E"),
]

# chapter: questions, upper case = central, lower case = secondary
use = {
    1: "MDFE", 2: "mFE", 3: "Md", 4: "MDe", 5: "Dfe", 6: "Mfe", 7: "Mf", 8: "Mfe",
    9: "Mfe", 10: "Mfe", 11: "Mdf", 12: "MfE", 13: "Mf", 14: "Mf", 15: "Mfe", 16: "MfE",
    17: "MDFE", 18: "MFe", 19: "MDf", 20: "mdFE", 21: "MDf",
    22: "mFe", 23: "mFe", 24: "mFE", 25: "dF", 26: "dF", 27: "MFe",
    28: "Fe", 29: "FE", 30: "FE", 31: "Fe", 32: "FE",
    33: "mFe", 34: "Fe", 35: "Fe", 36: "mFE",
    37: "mF", 38: "MFE", 39: "FE", 40: "mFe",
    41: "MDFe", 42: "MFe", 43: "Mfe", 44: "MfE", 45: "MdE", 46: "mDFE", 47: "MDFE",
}

chapters = sorted(use)
fig, ax = plt.subplots(figsize=(13.5, 3.3))
fig.subplots_adjust(left=0.2, right=0.995, bottom=0.2, top=0.86)
for j, (name, tok, code) in enumerate(rows):
    y = len(rows) - 1 - j
    ax.axhline(y, color=P.muted(), lw=0.3, alpha=0.5, zorder=1)
    for ch in chapters:
        s = use[ch]
        if code in s:
            ax.plot([ch], [y], "o", ms=9, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=3)
        elif code.lower() in s:
            ax.plot([ch], [y], "o", ms=6.5, mfc="none", mec=P.edge(tok), mew=1.2, zorder=3)

groups = [(1, 5, "foundations"), (6, 21, "neuroethology"), (22, 27, "survival and resources"),
          (28, 32, "reproduction"), (33, 36, "social evolution"), (37, 40, "communication"),
          (41, 47, "learning and cognition")]
for a, b, txt in groups:
    if b < 47:
        ax.axvline(b + 0.5, color=P.muted(), lw=0.6, ls=":", zorder=0)
    ax.text((a + b) / 2, len(rows) - 0.55, txt, fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")

ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xticks(chapters)
ax.set_xticklabels([str(c) for c in chapters])
ax.set_xlim(0.4, 47.6)
ax.set_ylim(-0.6, len(rows) - 0.1)
ax.tick_params(labelsize=FT["tiny"])
charts.style_axes(ax, "chapter (7.18.n)")
ax.tick_params(axis="y", labelsize=FT["small"])
# bracket the proximate and ultimate pairs of rows
for y0, y1, txt in [(2, 3, "proximate"), (0, 1, "ultimate")]:
    ax.annotate("", xy=(-0.165, y0 - 0.25), xytext=(-0.165, y1 + 0.25), xycoords=("axes fraction", "data"),
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
    ax.text(-0.175, (y0 + y1) / 2, txt, transform=ax.get_yaxis_transform(), fontsize=FT["tiny"],
            color=P.muted(), rotation=90, ha="right", va="center")
