"""Which pathways run in four metabolic states (from 7.1.19-7.1.22 and 7.1.29).

Columns: well fed; early fasting (overnight to day 3); prolonged starvation (weeks); untreated
type 1 diabetes. Rows: the main fluxes of liver, adipose tissue and muscle. Cells: strongly
increased (double up arrow), increased, roughly basal, decreased, relative to the postabsorptive
state. Hormone balance written above each column. Qualitative summary, not measured data.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P

states = [
    ("Well fed", "insulin ↑, glucagon ↓"),
    ("Early fasting\n(hours to day 3)", "insulin ↓, glucagon ↑"),
    ("Prolonged\nstarvation", "insulin low, glucagon ↑,\ncortisol ↑"),
    ("Untreated\ntype 1 diabetes", "no insulin,\nglucagon ↑↑"),
]
rows = [  # tissue, flux, values per state (2, 1, 0, -1)
    ("Liver", "Glycolysis", (1, -1, -1, -1)),
    ("Liver", "Glycogen synthesis", (1, -1, -1, -1)),
    ("Liver", "Glycogen breakdown", (-1, 1, -1, 1)),
    ("Liver", "Gluconeogenesis", (-1, 1, 1, 2)),
    ("Liver", "Fatty acid synthesis", (1, -1, -1, -1)),
    ("Liver", "β Oxidation", (-1, 1, 1, 2)),
    ("Liver", "Ketogenesis", (-1, 1, 2, 2)),
    ("Liver", "Urea cycle", (0, 1, -1, 1)),
    ("Adipose", "Lipolysis", (-1, 1, 1, 2)),
    ("Adipose", "TAG synthesis", (1, -1, -1, -1)),
    ("Muscle", "Glucose uptake (GLUT4)", (1, -1, -1, -1)),
    ("Muscle", "Protein breakdown", (-1, 1, 0, 1)),
]
SYM = {2: "↑↑", 1: "↑", 0: "–", -1: "↓"}

cw, ch = 3.1, 0.68
x0 = 6.2
top = 1.4 + len(rows) * ch
fig, ax = bio.canvas(x0 + len(states) * cw + 0.4, top + 2.9, scale=0.5)

for k, (s, h) in enumerate(states):
    xc = x0 + (k + 0.5) * cw
    bio.label(ax, (xc, top + 1.95), s, size="small", bold=True)
    bio.label(ax, (xc, top + 0.75), h, size="tiny", color=P.muted())

prev = None
for i, (tissue, flux, vals) in enumerate(rows):
    yc = top - (i + 0.5) * ch
    if tissue != prev:
        bio.label(ax, (0.3, yc), tissue, size="small", bold=True, ha="left", color=P.muted())
        if prev is not None:
            ax.plot([0.3, x0 + len(states) * cw], [yc + ch / 2, yc + ch / 2], color=P.muted(), lw=0.6,
                    ls=(0, (3, 2)))
        prev = tissue
    bio.label(ax, (x0 - 0.2, yc), flux, size="small", ha="right")
    for k, v in enumerate(vals):
        xc = x0 + (k + 0.5) * cw
        token = "positive" if v > 0 else "negative" if v < 0 else "neutral"
        ax.add_patch(FancyBboxPatch((xc - cw / 2 + 0.1, yc - ch / 2 + 0.07), cw - 0.2, ch - 0.14,
                                    boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill(token),
                                    edgecolor=P.edge(token), lw=0.8, zorder=5))
        bio.label(ax, (xc, yc), SYM[v], size="normal", bold=True, color=P.on_fill(), zorder=6)
