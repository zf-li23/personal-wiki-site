# The three complement activation pathways converge on C3 and share the terminal pathway.
# Boxes are components or complexes, filled arrows are reactions (processes), open arrows are activation,
# dashed arrows are the amplification loop and secondary outputs.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 12.4)

# column titles
for x, t in ((2.9, "Classical pathway"), (8.2, "Lectin pathway"), (17.2, "Alternative pathway")):
    bio.label(ax, (x, 11.9), t, size="title", bold=True)

# classical
bio.box(ax, (2.9, 10.7), 4.4, 0.9, "antibody", "antigen–antibody complex\n(IgM, IgG; CRP)", size="tiny")
bio.box(ax, (2.9, 9.2), 4.4, 0.9, "enzyme", "C1q binds; C1r, C1s\nautoactivate", size="tiny")
bio.arrow(ax, (2.9, 10.25), (2.9, 9.65), kind="process")
# lectin
bio.box(ax, (8.2, 10.7), 4.4, 0.9, "carbohydrate", "microbial carbohydrates\n(mannose, GlcNAc)", size="tiny")
bio.box(ax, (8.2, 9.2), 4.4, 0.9, "enzyme", "MBL / ficolins bind;\nMASP-1, MASP-2 activate", size="tiny")
bio.arrow(ax, (8.2, 10.25), (8.2, 9.65), kind="process")
# shared C4/C2 step
bio.box(ax, (5.55, 7.5), 5.0, 0.9, "protein", "cleave C4 → C4b, C4a; C2 → C2b, C2a", size="tiny")
bio.arrow(ax, (2.9, 8.75), (4.6, 7.95), kind="process")
bio.arrow(ax, (8.2, 8.75), (6.5, 7.95), kind="process")
bio.box(ax, (5.55, 6.0), 4.2, 0.9, "positive", "C4b2b\nC3 convertase", size="small")
bio.arrow(ax, (5.55, 7.05), (5.55, 6.45), kind="process")

# alternative
bio.box(ax, (17.2, 10.7), 5.2, 0.9, "bacterium", "microbial surface;\nC3 spontaneous hydrolysis (tick-over)", size="tiny")
bio.box(ax, (17.2, 9.2), 5.2, 0.9, "protein", "C3b + factor B,\nfactor D cleaves B", size="tiny")
bio.arrow(ax, (17.2, 10.25), (17.2, 9.65), kind="process")
bio.box(ax, (17.2, 7.5), 5.2, 0.9, "drug", "properdin stabilises", size="tiny")
bio.arrow(ax, (17.2, 8.75), (17.2, 7.95), kind="process")
bio.box(ax, (17.2, 6.0), 4.2, 0.9, "positive", "C3bBb\nC3 convertase", size="small")
bio.arrow(ax, (17.2, 7.05), (17.2, 6.45), kind="process")

# C3
bio.box(ax, (11.4, 4.2), 5.4, 1.0, "highlight", "C3 → C3a + C3b", size="normal")
bio.arrow(ax, (5.55, 5.55), (9.4, 4.5), kind="catalysis", bg=P.surface())
bio.arrow(ax, (17.2, 5.55), (13.4, 4.5), kind="catalysis", bg=P.surface())
# amplification loop
bio.arrow(ax, (14.1, 3.8), (19.4, 5.5), kind="activation", dashed=True, bend=-0.5, bg=P.surface())
bio.label(ax, (19.1, 3.3), "amplification loop:\nC3b forms more convertase", size="tiny", color=P.muted())
# outputs of C3
bio.box(ax, (11.4, 2.5), 5.4, 0.8, "neutral", "C3b: opsonization; added to a C3 convertase\nit makes the C5 convertase", size="tiny")
bio.arrow(ax, (10.0, 3.7), (10.0, 2.9), kind="process", dashed=True)
bio.box(ax, (5.0, 2.5), 3.4, 0.8, "neutral", "C3a: anaphylatoxin", size="tiny")
bio.arrow(ax, (9.4, 3.9), (6.0, 2.9), kind="process", dashed=True)

# C5 convertase, C5, MAC
bio.box(ax, (11.4, 1.2), 6.0, 0.9, "positive", "C5 convertase: C4b2b3b  /  C3bBb3b", size="tiny")
bio.arrow(ax, (11.4, 2.05), (11.4, 1.7), kind="process")
bio.box(ax, (18.4, 1.2), 5.0, 0.9, "negative", "C5 → C5a + C5b;  C5b + C6, C7, C8, C9n\n→ membrane attack complex", size="tiny")
bio.arrow(ax, (14.4, 1.2), (15.9, 1.2), kind="process")
bio.box(ax, (5.0, 1.2), 3.4, 0.9, "neutral", "C5a: anaphylatoxin,\nchemoattractant", size="tiny")
bio.arrow(ax, (8.4, 1.2), (6.7, 1.2), kind="process", dashed=True)
