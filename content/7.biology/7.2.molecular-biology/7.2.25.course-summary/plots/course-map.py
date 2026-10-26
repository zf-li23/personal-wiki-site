# The plan of course 7.2 as a map of its main line: five parts in reading order
# (carrier -> tools -> maintenance -> read-out and its control -> integration), each a column of chapter
# boxes. Part IV is split into its transcriptional half (10-15) and its RNA and protein half (16-20).
# The boxes of part V list the earlier chapters each integrative chapter builds on; the bar at the bottom
# marks that the two tool chapters are used by every later chapter.
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 13.2)

cols = [
    ("I  Carrier", "What holds the information?", "dna", 2.35, [(2, "Genome content"), (3, "DNA topology,\nsupercoiling"), (4, "Chromatin and\nthe nucleosome")]),
    ("II  Tools", "How do we see and change it?", "enzyme", 6.75, [(5, "Cloning and manipulating\nnucleic acids"), (6, "Measurement and\nsequencing")]),
    ("III  Maintenance", "How is it copied and kept?", "dna2", 11.15, [(7, "DNA replication"), (8, "Damage and repair"), (9, "Recombination,\nmobile elements")]),
    (None, "Transcription", "rna", 15.55, [(10, "Bacterial transcription"), (11, "Operons and phage"), (12, "Eukaryotic polymerases,\npromoters"),
                                            (13, "General factors, PIC"), (14, "Activators, enhancers,\ncoactivators"), (15, "Chromatin regulation,\nepigenetics")]),
    (None, "RNA and protein", "trna", 19.95, [(16, "RNA splicing"), (17, "Capping, poly(A),\nRNA processing"), (18, "mRNA stability,\nregulatory RNA"),
                                              (19, "Translation and\nthe genetic code"), (20, "Translational control")]),
    ("V  Integration", "How do the parts combine?", "protein", 24.55, [(21, "Biomolecular condensates\n← 4, 14, 15, 18"), (22, "Quantitative view\n← 10, 11, 18, 19"),
                                                                     (23, "RNA world\n← 7, 16, 17, 19"), (24, "Gene editing\n← 5, 8, 9, 14, 17"), (25, "Course summary\n← all")]),
]

W, H, TOP, STEP = 4.05, 0.92, 10.0, 1.12
for head, question, tok, x, chapters in cols:
    if head:
        bio.box(ax, (x, 12.35), W, 0.78, tok, head, radius=0.3, size="normal")
        bio.label(ax, (x, 11.6), question, size="tiny", color=P.muted())
    else:
        bio.label(ax, (x, 11.05), question, size="small", bold=True)
    for k, (num, text) in enumerate(chapters):
        y = TOP - k * STEP - (0.55 if head is None else 0.0)
        ax.add_patch(FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle="round,pad=0,rounding_size=0.16",
                                             facecolor=P.mix(P.fill(tok), P.surface(), 0.55), edgecolor=P.edge(tok), lw=0.9, zorder=10))
        bio.label(ax, (x - W / 2 + 0.2, y), f"{num}", size="small", bold=True, ha="left", zorder=12)
        bio.label(ax, (x - W / 2 + 0.75, y), text, size="tiny", ha="left", zorder=12)

# part IV header spanning its two halves
bio.box(ax, (17.75, 12.35), 2 * W + 0.35, 0.78, "rna", "IV  Read-out and its control", radius=0.3, size="normal")
bio.label(ax, (17.75, 11.6), "How is it read, and how is the reading controlled?", size="tiny", color=P.muted())

# the main line
for a, b in ((2.35 + W / 2, 6.75 - W / 2), (6.75 + W / 2, 11.15 - W / 2), (11.15 + W / 2, 13.55), (21.95, 24.55 - W / 2)):
    bio.arrow(ax, (a + 0.02, 12.35), (b - 0.02, 12.35), kind="process", lw=1.6)
bio.arrow(ax, (15.55 + W / 2 - 0.1, 11.05), (19.95 - W / 2 + 0.1, 11.05), kind="process", lw=1.0, color=P.muted())

# tools are used throughout
y0 = 3.05
ax.plot([6.75 - W / 2, 24.55 + W / 2], [y0, y0], color=P.edge("enzyme"), lw=2.2, solid_capstyle="round", zorder=8)
ax.plot([6.75, 6.75], [y0, 10.0 - 1 * STEP - H / 2], color=P.edge("enzyme"), lw=1.0, ls=(0, (3, 2)), zorder=8)
bio.label(ax, (15.6, y0 - 0.22), "footprinting, gel shift, reporters, qPCR, ChIP, sequencing, cloning: used in every later chapter",
          size="tiny", color=P.edge("enzyme"), va="top")

# crop the empty band below the bar
ax.set_ylim(2.2, 13.2)
fig.set_size_inches(27 * 0.45, (13.2 - 2.2) * 0.45)
