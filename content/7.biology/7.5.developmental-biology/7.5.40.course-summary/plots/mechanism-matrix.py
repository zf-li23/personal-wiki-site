"""Which recurring mechanism each chapter of the course relies on.

Columns: chapters 7.5.3-7.5.39 (7.5.1-7.5.2 introduce all mechanisms and the methods, 7.5.40 is
this summary). Rows: the seven mechanisms of Section 40.2. A filled disc marks a mechanism that is
central to the chapter (it carries a model or a key experiment there), an open ring one that
appears as a secondary element. The assignment summarizes the chapters; it is a reading aid, not data.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rows = [
    ("cytoplasmic determinants", "rna", "D"),
    ("induction", "receptor", "I"),
    ("gradients and thresholds", "channel", "G"),
    ("self-organization", "enzyme", "S"),
    ("mechanics", "bone", "M"),
    ("clocks and timing", "highlight", "C"),
    ("stochasticity", "protein", "R"),
]

# chapter: mechanisms, upper case = central, lower case = secondary
use = {
    3: "Igs", 4: "Rsid", 5: "MCdir", 6: "DIsc", 7: "Msr", 8: "M", 9: "Mis", 10: "sg",
    11: "Gscr", 12: "Sg", 13: "Sic", 14: "DGs", 15: "Gsic", 16: "DIGs", 17: "IGsmc",
    18: "GMic", 19: "Csrd", 20: "imsg", 21: "Girs", 22: "ISMc", 23: "CGsm", 24: "igcm",
    25: "IRs", 26: "isc", 27: "DIrc", 28: "IMc", 29: "Misr", 30: "IMRs", 31: "IGRc",
    32: "GSc", 33: "Sgmc", 34: "CR", 35: "SGi", 36: "Rs", 37: "Rc", 38: "RCg", 39: "Crs",
}

chapters = sorted(use)
fig, ax = plt.subplots(figsize=(13.5, 3.9))
fig.subplots_adjust(left=0.17, right=0.99, bottom=0.2, top=0.97)
for j, (name, tok, code) in enumerate(rows):
    y = len(rows) - 1 - j
    ax.axhline(y, color=P.muted(), lw=0.3, alpha=0.5, zorder=1)
    for ch in chapters:
        s = use[ch]
        if code in s:
            ax.plot([ch], [y], "o", ms=9, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=3)
        elif code.lower() in s:
            ax.plot([ch], [y], "o", ms=7, mfc="none", mec=P.edge(tok), mew=1.3, zorder=3)
for sep in (6.5, 13.5, 17.5, 22.5, 32.5, 37.5):
    ax.axvline(sep, color=P.muted(), lw=0.6, ls=":", zorder=0)
groups = [(3, 6, "early embryo"), (7, 13, "models of form and pattern"), (14, 17, "body axes"),
          (18, 22, "ectoderm"), (23, 32, "mesoderm, endoderm, limbs"), (33, 37, "after the embryo"),
          (38, 39, "contexts")]
for a, b, txt in groups:
    ax.text((a + b) / 2, len(rows) - 0.35, txt, fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1])
ax.set_xticks(chapters)
ax.set_xticklabels([str(c) for c in chapters])
ax.set_xlim(2.4, 39.6)
ax.set_ylim(-0.6, len(rows) + 0.1)
ax.tick_params(labelsize=FT["tiny"])
charts.style_axes(ax, "chapter (7.5.n)")
