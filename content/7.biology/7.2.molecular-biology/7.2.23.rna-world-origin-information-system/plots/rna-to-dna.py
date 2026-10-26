# The handover from RNA to DNA: the two chemical differences, the biosynthetic direction and the order of events.
# A: the 2'-OH attacks the adjacent phosphodiester in line (the reaction the small self-cleaving ribozymes
#    catalyse), so RNA is 1e5-1e6 times more labile than DNA; hydrolytic deamination of cytosine gives uracil,
#    which a thymine-containing genome can recognize as damage and excise.
# B: every dNDP is made from an NDP by ribonucleotide reductase and dTMP from dUMP by thymidylate synthase,
#    so DNA precursors are derivatives of RNA precursors and never the reverse.
# C: the standard order of events, with the catalytic and informational roles as they are handed over.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 13.2)

NEG = P.edge("negative")


def ring(xy, text, token="rna", r=0.42):
    ax.add_patch(bio.core.Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.0, zorder=11))
    bio.label(ax, xy, text, size="tiny", color=P.on_fill(), zorder=12)


# ----------------------------------------------------------------- A: the two chemical differences
bio.panel(ax, "A", (0.1, 13.0))
bio.label(ax, (6.2, 13.0), "Two chemical differences, two different jobs", size="small", bold=True)

# A1: the 2'-OH and backbone cleavage
y = 11.0
bio.label(ax, (0.6, y + 0.85), "1  The $2'$-OH cleaves the backbone", size="tiny", bold=True, ha="left")
for i, (x, lab) in enumerate(((1.8, "N"), (4.6, "N"))):
    ring((x, y), lab, token="rna", r=0.36)
ax.plot([2.16, 4.24], [y, y], color=P.edge("rna"), lw=1.8, zorder=6)
ax.add_patch(bio.core.Circle((3.2, y), 0.24, facecolor=P.fill("negative"), edgecolor=NEG, lw=0.9, zorder=12))
bio.label(ax, (3.2, y), "P", size="tiny", color=P.on_fill(), zorder=13)
ax.add_patch(bio.core.Circle((1.8, y - 0.62), 0.11, color=P.edge("highlight"), zorder=13))
bio.label(ax, (1.05, y - 0.72), "$2'$-OH", size="tiny", color=P.edge("highlight"), ha="right")
bio.arrow(ax, (1.95, y - 0.55), (3.05, y - 0.2), kind="process", color=NEG)
bio.arrow(ax, (5.4, y), (6.6, y), kind="process")
ring((7.6, y), "N", token="rna", r=0.36)
bio.label(ax, (7.6, y - 0.85), "$2',3'$-cyclic\nphosphate", size="tiny", color=P.muted())
ring((9.9, y), "N", token="rna", r=0.36)
bio.label(ax, (9.9, y - 0.75), "free $5'$-OH", size="tiny", color=P.muted())
bio.label(ax, (8.9, y + 0.95), "RNA is cleaved $10^{5}$–$10^{6}$ times\nfaster than DNA at neutral pH",
          size="tiny", color=P.ink(), ha="left")

# A2: cytosine deamination
y = 8.2
bio.label(ax, (0.6, y + 1.0), "2  Cytosine deaminates, so thymine labels the damage", size="tiny", bold=True, ha="left")
ring((1.8, y), "C", token="dna2")
bio.arrow(ax, (2.5, y), (3.9, y), kind="process")
bio.label(ax, (3.2, y + 0.45), "+ H$_2$O", size="tiny", color=P.muted())
bio.label(ax, (3.2, y - 0.45), "− NH$_3$", size="tiny", color=P.muted())
ring((4.6, y), "U", token="negative")
bio.label(ax, (3.2, y - 0.95), "in an RNA genome this U would be read\nas a legitimate base: a mutation",
          size="tiny", color=NEG)
bio.arrow(ax, (5.3, y), (6.7, y), kind="process", dashed=True)
ring((7.4, y), "T", token="dna")
bio.label(ax, (7.4, y + 0.8), "DNA uses $5$-methyluracil", size="tiny", color=P.muted())
bio.box(ax, (10.6, y), 4.4, 1.3, token="positive",
        text="any U in DNA is damage\n→ uracil-DNA glycosylase\nexcises it", size="tiny", radius=0.12)
bio.label(ax, (6.2, 6.5), "the methyl group is a label, not an improvement; its price is a whole biosynthetic branch",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: biosynthetic direction
bio.panel(ax, "B", (0.1, 5.6))
bio.label(ax, (6.2, 5.6), "The precursors run one way only", size="small", bold=True)
yb = 3.7
bio.box(ax, (2.2, yb), 2.6, 0.95, token="rna", text="NDP\n(ribo)", size="tiny", radius=0.12)
bio.box(ax, (7.0, yb), 3.0, 0.95, token="dna", text="dNDP\n(deoxyribo)", size="tiny", radius=0.12)
bio.arrow(ax, (3.6, yb), (5.4, yb), kind="process")
bio.label(ax, (4.5, yb + 0.5), "ribonucleotide reductase", size="tiny", color=P.muted())
bio.label(ax, (4.5, yb - 0.5), "(7.1.28)", size="tiny", color=P.muted())
bio.arrow(ax, (5.4, yb - 0.95), (3.6, yb - 0.95), kind="inhibition", color=NEG)
bio.label(ax, (4.5, yb - 1.45), "no pathway runs this way", size="tiny", color=NEG)
yb2 = 1.3
bio.box(ax, (2.2, yb2), 2.6, 0.95, token="rna", text="dUMP", size="tiny", radius=0.12)
bio.box(ax, (7.0, yb2), 3.0, 0.95, token="dna", text="dTMP", size="tiny", radius=0.12)
bio.arrow(ax, (3.6, yb2), (5.4, yb2), kind="process")
bio.label(ax, (4.5, yb2 + 0.5), "thymidylate synthase", size="tiny", color=P.muted())
bio.label(ax, (10.0, 2.5), "DNA precursors are\nderivatives of RNA\nprecursors: RNA is\nmetabolically upstream",
          size="tiny", color=P.ink(), ha="left")

# ----------------------------------------------------------------- C: the order of events
bio.panel(ax, "C", (13.0, 13.0))
bio.label(ax, (19.4, 13.0), "The handover, and what it left behind", size="small", bold=True)

stages = [
    ("RNA world", "RNA", "RNA", "rna", 11.4),
    ("RNA + peptides", "RNA", "RNA, peptides", "rna", 9.2),
    ("RNP world", "RNA", "proteins (RNA at the core)", "rrna", 7.0),
    ("DNA / protein world", "DNA", "proteins", "dna", 4.8),
]
for name, store, cat, token, y in stages:
    bio.box(ax, (16.3, y), 4.4, 1.2, token=token, text=name, size="small", radius=0.12, zorder=10)
    bio.label(ax, (19.0, y + 0.3), f"stores: {store}", size="tiny", color=P.ink(), ha="left")
    bio.label(ax, (19.0, y - 0.3), f"catalyses: {cat}", size="tiny", color=P.muted(), ha="left")
for y0, y1 in ((11.4, 9.2), (9.2, 7.0), (7.0, 4.8)):
    bio.arrow(ax, (16.3, y0 - 0.62), (16.3, y1 + 0.62), kind="process")
bio.label(ax, (15.1, 10.3), "peptide bond\nformation", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (15.1, 8.1), "protein catalysis\ntakes over", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (15.1, 5.9), "reverse transcription:\nstorage moves to DNA", size="tiny", color=P.muted(), ha="right")

bio.box(ax, (19.4, 2.5), 10.6, 2.3, token="highlight",
        text="relics: the peptidyl transferase centre, the spliceosome and group II introns, RNase P,\n"
             "self-splicing introns, riboswitches, the adenosine handle of CoA / FAD / NAD / SAM,\n"
             "and the derivation of every deoxyribonucleotide from a ribonucleotide",
        size="tiny", radius=0.14)
bio.label(ax, (19.4, 0.85), "$\\approx 4.0$ Ga   →   $\\approx 3.6$ Ga: the window between a stable hydrosphere"
          " and the first fossil evidence of life", size="tiny", color=P.muted())
