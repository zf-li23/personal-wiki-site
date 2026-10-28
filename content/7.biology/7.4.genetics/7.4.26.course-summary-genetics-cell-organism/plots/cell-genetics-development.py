"""Cell biology, genetics and development as one system: what each course contributes at each level.

Left: the cellular machinery (7.3, with 7.2 for chromatin); middle: the genetic consequence studied
in this course; right: what developmental biology (7.5) or evolutionary biology (7.10) builds on it.
Chapter numbers are in parentheses; arrows read 'is the mechanism of' and 'is the tool or input for'.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 17.5)

rows = [  # (cell, token, genetics, token, development / evolution, token)
    ("meiosis: pairing, crossovers,\ncohesin, spindle (7.3.21)", "chromatin",
     "segregation, assortment,\nrecombination, maps (7.4.5, 7.4.8, 7.4.9)", "dna",
     "germ line and gametes;\nmaternal age and aneuploidy", "neutral"),
    ("chromosome structure,\nkaryotype (7.3.17)", "chromatin",
     "rearrangements, aneuploidy,\npolyploidy (7.4.15, 7.4.16)", "dna",
     "dosage-sensitive development;\nsyndromes of trisomy", "neutral"),
    ("chromatin, X inactivation\n(7.3.17, 7.2.15)", "chromatin",
     "dosage compensation, imprinting,\nposition effects (7.4.6, 7.4.18)", "dna",
     "cell memory: Polycomb, trithorax\nmaintain Hox states (7.5)", "protein"),
    ("mitochondria, plastids\n(7.3.12)", "mitochondrion",
     "organellar and maternal\ninheritance (7.4.11)", "dna",
     "maternal-effect genes set\nthe axes of the embryo (7.5)", "protein"),
    ("cell cycle, checkpoints,\ncancer cells (7.3.20, 7.3.26)", "negative",
     "two hits, LOH, drivers,\nsignatures (7.4.21)", "dna",
     "growth control of tissues;\ncancer as failed development", "neutral"),
    ("signaling pathways\n(7.3.18, 7.3.19)", "receptor",
     "epistasis analysis orders\npathways (7.4.4, 7.4.20)", "dna",
     "induction, morphogen gradients,\nsignaling centers (7.5)", "protein"),
    ("differentiation, stem cells,\nclones (7.3.24)", "enzyme",
     "mosaics, twin spots, cell autonomy,\nscreens (7.4.9, 7.4.19, 7.4.20)", "dna",
     "segmentation hierarchy, Hox\ncolinearity, pattern (7.5)", "protein"),
    ("variation among cells and\nindividuals (7.3.1)", "neutral",
     "populations, quantitative traits,\nGWAS (7.4.22–7.4.25)", "dna",
     "adaptation, speciation,\ncoalescent (7.10)", "plant"),
]
X = (4.4, 13.5, 22.6)
W = (7.8, 9.4, 7.8)
H, dy, y0 = 1.55, 1.95, 15.0
for x, t in zip(X, ["cell biology (7.3)", "genetics (7.4)", "development (7.5), evolution (7.10)"]):
    bio.label(ax, (x, 16.8), t, size="normal", bold=True)
for i, (c, ct, g, gt, dv, dt) in enumerate(rows):
    y = y0 - i * dy
    for x, w, text, tok in [(X[0], W[0], c, ct), (X[1], W[1], g, gt), (X[2], W[2], dv, dt)]:
        bio.box(ax, (x, y), w, H, token=tok)
        bio.label(ax, (x, y), text, size="small", color=P.on_fill())
    bio.arrow(ax, (X[0] + W[0] / 2 + 0.1, y), (X[1] - W[1] / 2 - 0.1, y), kind="process")
    bio.arrow(ax, (X[1] + W[1] / 2 + 0.1, y), (X[2] - W[2] / 2 - 0.1, y), kind="activation")
bio.label(ax, ((X[0] + X[1]) / 2 + 0.25, 16.1), "mechanism", size="small", color=P.muted())
bio.label(ax, ((X[1] + X[2]) / 2 + 0.25, 16.1), "tool, input", size="small", color=P.muted())
ax.set_ylim(0.3, 17.4)
