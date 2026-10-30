"""Evolution of Hox clusters by duplication (after the reconstruction summarized by Wolpert et al.).

Columns are paralogue groups 1-15. A proposed ancestral bilaterian cluster of about seven genes; Drosophila
(lab, pb, zen and bcd, which arose from a group 3 gene and lost Hox function, Dfd, Scr, Antp, Ubx, abd-A,
Abd-B; drawn as one row although in flies the cluster is split into the Antennapedia and bithorax
complexes); amphioxus with one cluster of 15 genes; and the four mouse clusters Hoxa-d (39 genes), which arose
by two rounds of whole-genome duplication followed by gene losses. Colours: anterior (1-2), group 3, central
(4-8) and posterior (9-15) genes. The spatial and temporal colinearity of 3' to 5' order is conserved.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34.0, 12.5)
x0, dx, w, h = 6.0, 1.75, 1.45, 0.8


def tok(g):
    return "dna" if g <= 2 else ("rna" if g == 3 else ("positive" if g <= 8 else "negative"))


rows = [
    ("ancestor (hypothetical)", {1: "", 2: "", 3: "", 4: "", 6: "", 7: "", 9: ""}),
    ("Drosophila", {1: "lab", 2: "pb", 3: "zen, bcd", 4: "Dfd", 5: "Scr", 6: "Antp", 7: "Ubx", 8: "abd-A", 9: "Abd-B"}),
    ("amphioxus", {g: str(g) for g in range(1, 16)}),
    ("mouse Hoxa", {g: f"a{g}" for g in (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13)}),
    ("mouse Hoxb", {g: f"b{g}" for g in (1, 2, 3, 4, 5, 6, 7, 8, 9, 13)}),
    ("mouse Hoxc", {g: f"c{g}" for g in (4, 5, 6, 8, 9, 10, 11, 12, 13)}),
    ("mouse Hoxd", {g: f"d{g}" for g in (1, 3, 4, 8, 9, 10, 11, 12, 13)}),
]
for g in range(1, 16):
    bio.label(ax, (x0 + (g - 1) * dx, 11.7), str(g), size="tiny", color=P.muted())
bio.label(ax, (x0 - 0.9, 11.7), "paralogue group", size="tiny", color=P.muted(), ha="right")
for i, (name, genes) in enumerate(rows):
    y = 10.6 - 1.3 * i - (0.4 if i >= 3 else 0)
    ax.plot([x0 - 0.8, x0 + 14 * dx + 0.8], [y, y], color=P.muted(), lw=1.0, zorder=3)
    bio.label(ax, (x0 - 1.0, y), name, size="small", ha="right", italic=(name == "Drosophila"))
    for g, txt in genes.items():
        bio.box(ax, (x0 + (g - 1) * dx, y), w, h, tok(g), None, radius=0.12)
        if txt:
            bio.label(ax, (x0 + (g - 1) * dx, y), txt, size="tiny", italic=True, color=P.on_fill())
bio.label(ax, (x0 + 7 * dx, 1.6), "3'  ->  5'     anterior expression, early  ->  posterior expression, late",
          size="tiny", color=P.muted())
bio.arrow(ax, (1.2, 6.4), (1.2, 4.2), kind="process")
bio.label(ax, (1.2, 3.6), "2 rounds of\ngenome\nduplication", size="tiny", color=P.muted())
for j, (g, txt) in enumerate(((1, "anterior"), (3, "group 3"), (6, "central"), (11, "posterior"))):
    bio.box(ax, (x0 + 8.5 * j * 0.9 + 2.0, 0.6), 0.6, 0.4, tok(g), None, radius=0.06)
    bio.label(ax, (x0 + 8.5 * j * 0.9 + 2.5, 0.6), txt, size="tiny", ha="left")
