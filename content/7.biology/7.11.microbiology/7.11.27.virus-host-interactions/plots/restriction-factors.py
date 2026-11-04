# Restriction factors along the retroviral replication cycle, and the viral antagonist of each.
# Upper row: the host block and the step it hits. Lower row: the viral protein that removes it.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 7.6)

bio.label(ax, (9.6, 7.35), "A constitutive host block at every step, and a viral antagonist for each",
          size="title", bold=True)

STEPS = [
    (2.1, "Entry\nand fusion", "IFITM proteins", "alter the endosomal\nmembrane, block fusion",
     None, None),
    (5.6, "Uncoating", "TRIM5$\\alpha$", "binds the capsid lattice,\nforces premature uncoating",
     "capsid substitutions", "species-specific:\na barrier between primates"),
    (9.1, "Reverse\ntranscription", "APOBEC3G\nSAMHD1", "C→U deamination of the\nnascent DNA; dNTP depletion",
     "Vif (HIV-1)\nVpx (HIV-2)", "both antagonists are\nubiquitin-ligase adaptors"),
    (12.6, "Nuclear import\nand integration", "MxB", "blocks import of the\npre-integration complex",
     None, None),
    (16.1, "Assembly\nand budding", "Tetherin (BST-2)", "two membrane anchors\nretain budded virions",
     "Vpu (HIV-1)\nOrf7a (SARS-CoV-2)", "unrelated proteins,\nthe same function"),
]

Y_CYCLE, Y_FACTOR, Y_ANTAG = 4.3, 6.0, 2.2
for i, (x, step, factor, what, antag, note) in enumerate(STEPS):
    bio.box(ax, (x, Y_CYCLE), 3.0, 0.95, token="virus", radius=0.2)
    bio.label(ax, (x, Y_CYCLE), step, size="small", bold=True, color=P.on_fill())
    if i < len(STEPS) - 1:
        bio.arrow(ax, (x + 1.58, Y_CYCLE), (STEPS[i + 1][0] - 1.58, Y_CYCLE), kind="process")
    bio.box(ax, (x, Y_FACTOR), 3.2, 1.15, token="positive", radius=0.2)
    bio.label(ax, (x, Y_FACTOR + 0.3), factor, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (x, Y_FACTOR - 0.28), what, size="tiny", color=P.on_fill())
    bio.arrow(ax, (x - 0.7, Y_FACTOR - 0.65), (x - 0.7, Y_CYCLE + 0.52), kind="inhibition",
              color=P.edge("positive"))
    if antag:
        bio.box(ax, (x, Y_ANTAG), 3.2, 1.05, token="negative", radius=0.2)
        bio.label(ax, (x, Y_ANTAG + 0.25), antag, size="small", bold=True, color=P.on_fill())
        bio.label(ax, (x, Y_ANTAG - 0.28), note, size="tiny", color=P.on_fill())
        bio.arrow(ax, (x + 0.7, Y_ANTAG + 0.6), (x + 0.7, Y_FACTOR - 0.65), kind="inhibition",
                  color=P.edge("negative"))

bio.label(ax, (18.9, Y_FACTOR), "host\nrestriction", size="small", color=P.edge("positive"), ha="center")
bio.label(ax, (18.9, Y_CYCLE), "viral\ncycle", size="small", color=P.edge("virus"), ha="center")
bio.label(ax, (18.9, Y_ANTAG), "viral\nantagonist", size="small", color=P.edge("negative"), ha="center")

bio.label(ax, (9.6, 0.8), "Restriction factors are present before infection and are induced further by interferon; "
                           "the genes encoding them and\ntheir antagonists are among the fastest-evolving in "
                           "their genomes, each imposing selection on the other", size="tiny", color=P.muted())
