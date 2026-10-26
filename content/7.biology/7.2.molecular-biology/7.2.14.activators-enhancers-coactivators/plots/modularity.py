# The modularity of activators (schematic). A: LexA DNA-binding domain alone binds a lexA operator but does not
# activate the reporter; the LexA-GAL4(AD) chimera activates it (Brent and Ptashne 1985). B: yeast two-hybrid
# assay (Fields and Song 1989): bait X fused to the GAL4 DNA-binding domain binds the UAS; the reporter is
# transcribed only when prey Y, fused to an activation domain, binds X.
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(22.0, 9.6)


def reporter(x, y, op_text, cds_text, on):
    parts = G.construct(ax, x, y, [{"kind": "operator", "text": op_text, "token": "highlight"},
                                   {"kind": "promoter"},
                                   {"kind": "cds", "text": cds_text, "token": "positive" if on else "neutral", "width": 2.4}],
                        unit=0.5, gap=0.25)
    if on:
        bio.arrow(ax, (parts[1]["x1"] + 0.1, y + 0.9), (parts[2]["x1"] + 0.2, y + 0.9), kind="process", color=P.edge("rna"))
        bio.label(ax, (parts[2]["x1"] + 0.4, y + 0.9), "mRNA", size="tiny", ha="left", color=P.edge("rna"))
    else:
        bio.label(ax, (parts[2]["x1"] + 0.4, y), "off", size="small", ha="left", color=P.muted())
    return parts


def mark(x, y, ok):
    bio.label(ax, (x, y), "+" if ok else "−", size="title", bold=True,
              color=P.edge("positive") if ok else P.edge("negative"))


# ---- A
bio.panel(ax, "A", (0.1, 9.5))
bio.label(ax, (0.6, 9.15), "Domain swap", size="normal", bold=True, ha="left")
for y, chimera in [(5.6, False), (1.4, True)]:
    parts = reporter(1.3, y, "lexA op", "lacZ", chimera)
    cx = parts[0]["centre"]
    bio.protein(ax, (cx, y + 0.85), 1.4, 0.9, "dna2", "LexA", size="tiny")
    if chimera:
        ax.plot([cx + 0.4, cx + 1.0], [y + 1.1, y + 1.45], color=P.edge("enzyme"), lw=2.0, zorder=11)
        bio.protein(ax, (cx + 1.35, y + 1.6), 1.3, 0.8, "enzyme", "AD", size="tiny")
        bio.label(ax, (cx + 2.15, y + 1.65), "GAL4 activation domain", size="tiny", ha="left", color=P.muted())
    bio.label(ax, (1.0, y + 2.55), "LexA–GAL4 AD chimera" if chimera else "LexA alone", size="small", ha="left")
    mark(8.0, y + 0.3, chimera)

# ---- B
bio.panel(ax, "B", (11.0, 9.5))
bio.label(ax, (11.5, 9.15), "Yeast two-hybrid", size="normal", bold=True, ha="left")
for y, prey in [(5.6, False), (1.4, True)]:
    parts = reporter(12.2, y, "UAS", "HIS3", prey)
    cx = parts[0]["centre"]
    bio.protein(ax, (cx, y + 0.85), 1.3, 0.85, "receptor", "DBD", size="tiny")
    bio.protein(ax, (cx + 1.0, y + 1.7), 1.2, 0.85, "drug", "X", size="small")
    if prey:
        bio.protein(ax, (cx + 2.1, y + 1.95), 1.1, 0.8, "metabolite", "Y", size="small")
        bio.protein(ax, (cx + 3.1, y + 1.65), 1.1, 0.75, "enzyme", "AD", size="tiny")
        bio.label(ax, (11.9, y + 2.7), "bait (DBD–X) + prey (Y–AD)", size="small", ha="left")
    else:
        bio.protein(ax, (cx + 4.6, y + 2.0), 1.1, 0.8, "metabolite", "Z", size="small")
        bio.protein(ax, (cx + 5.6, y + 2.0), 1.1, 0.75, "enzyme", "AD", size="tiny")
        bio.label(ax, (11.9, y + 2.7), "bait + noninteracting prey (Z–AD)", size="small", ha="left")
    mark(21.4, y + 0.3, prey)
