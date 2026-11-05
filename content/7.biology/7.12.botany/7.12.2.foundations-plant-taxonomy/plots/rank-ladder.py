"""The taxonomic hierarchy of the cultivated apple, Malus domestica, as a ladder of nested ranks.

Left: the rank (principal ranks in bold) with its Latin term and the standard suffix of names at that
rank under the ICN (Art. 16-19; ranks above order shown with the suffixes for plants). Right: the taxon
of the apple at each rank. Order and family follow APG IV; subfamily, tribe and subtribe follow the
current classification of Rosaceae (Amygdaloideae, Maleae, Malinae). The suffix is highlighted in each
name. Kingdom and division are given in the traditional form used by Chinese floras (Plantae,
Magnoliophyta); APG itself names no ranks above order.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19, 14.6)

rows = [
    # (rank, latin, suffix, stem, ending, principal)
    ("Kingdom", "regnum", "(none)", "Plantae", "", True),
    ("Division (phylum)", "divisio", "-phyta", "Magnolio", "phyta", True),
    ("Class", "classis", "-opsida", "Magnoli", "opsida", True),
    ("Subclass", "subclassis", "-idae", "Ros", "idae", False),
    ("Order", "ordo", "-ales", "Ros", "ales", True),
    ("Family", "familia", "-aceae", "Ros", "aceae", True),
    ("Subfamily", "subfamilia", "-oideae", "Amygdal", "oideae", False),
    ("Tribe", "tribus", "-eae", "Mal", "eae", False),
    ("Subtribe", "subtribus", "-inae", "Mal", "inae", False),
    ("Genus", "genus", "(none)", "Malus", "", True),
    ("Species", "species", "binomial", "Malus domestica", "", True),
]
top, step = 13.2, 1.16
bio.label(ax, (0.6, top + 0.95), "Rank", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (5.4, top + 0.95), "Latin", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (8.2, top + 0.95), "Suffix", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (11.2, top + 0.95), "Taxon of the apple", size="small", bold=True, ha="left", color=P.muted())
for i, (rank, latin, suf, stem, end, principal) in enumerate(rows):
    y = top - i * step
    indent = 0.25 * i
    tok = "positive" if principal else "neutral"
    w = 18.6 - (11.2 + indent)
    bio.box(ax, (11.2 + indent + w / 2, y), w, 0.82, token=tok, radius=0.2)
    bio.label(ax, (0.6, y), rank, size="normal" if principal else "small", bold=principal, ha="left")
    bio.label(ax, (5.4, y), latin, size="small", italic=True, ha="left", color=P.muted())
    bio.label(ax, (8.2, y), suf, size="small", ha="left")
    x = 11.5 + indent
    italic = rank in ("Genus", "Species")
    t = ax.text(x, y, stem, fontsize=bio.core.FONT["normal"], color=P.on_fill(), ha="left", va="center",
                style="italic" if italic else "normal", zorder=12)
    if end:
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        ax.text(bb.x1, y, end, fontsize=bio.core.FONT["normal"], color=P.edge("negative"), ha="left", va="center",
                weight="bold", zorder=12)
    if i:
        ax.plot([11.2 + indent - 0.05, 11.2 + indent - 0.05], [y + 0.41, y + step - 0.41], color=P.muted(),
                lw=0.8, zorder=3)
bio.label(ax, (0.6, 0.35), "bold: principal ranks of the ICN; red: standard suffix of the rank", size="tiny",
          ha="left", color=P.muted())
