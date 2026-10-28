"""The complementation test as trans-heterozygotes (schematic).

Left: m1 in gene a and m2 in gene b, one on each homologue: each homologue carries a wild-type copy of the
gene mutated on the other, both products are made, and the phenotype is wild type (complementation).
Right: m1 and m2 both in gene a: no functional copy of a, the phenotype is mutant (no complementation).
"""
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)


def homologue(x, y, genes, w=8.0, h=0.55, tok="dna"):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h / 2}",
                                facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=8))
    for gx, gw, name, mut in genes:
        t = "negative" if mut else "positive"
        ax.add_patch(FancyBboxPatch((x + gx, y - h / 2 + 0.04), gw, h - 0.08, boxstyle="round,pad=0,rounding_size=0.1",
                                    facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.9, zorder=9))
        bio.label(ax, (x + gx + gw / 2, y + 0.6), name, size="small", italic=True)
        if mut:
            bio.label(ax, (x + gx + gw / 2, y), "×", size="normal", bold=True, color=P.on_fill(), zorder=12)


def panel(x, letter, title, top, bottom, products, result, tok):
    bio.panel(ax, letter, (x - 0.6, 9.4))
    bio.label(ax, (x + 4.0, 8.9), title, size="normal", bold=True)
    homologue(x, 7.0, top)
    homologue(x, 5.3, bottom, tok="receptor")
    bio.label(ax, (x - 0.2, 7.0), "homologue 1", size="tiny", ha="right", color=P.muted())
    bio.label(ax, (x - 0.2, 5.3), "homologue 2", size="tiny", ha="right", color=P.muted())
    for i, (txt, ok) in enumerate(products):
        bio.box(ax, (x + 2.0 + i * 4.0, 3.3), 3.3, 0.8, token="positive" if ok else "neutral", text=txt, size="small")
    bio.box(ax, (x + 4.0, 1.4), 7.0, 0.9, token=tok, text=result, size="normal")
    bio.arrow(ax, (x + 4.0, 2.75), (x + 4.0, 1.95))


panel(2.2, "A", "Mutations in different genes",
      [(1.0, 2.0, "a", True), (5.0, 2.0, "b", False)], [(1.0, 2.0, "a", False), (5.0, 2.0, "b", True)],
      [("product A made", True), ("product B made", True)], "wild type: complementation", "positive")
panel(13.8, "B", "Mutations in the same gene",
      [(1.0, 2.0, "a", True), (5.0, 2.0, "b", False)], [(1.0, 2.0, "a", True), (5.0, 2.0, "b", False)],
      [("no product A", False), ("product B made", True)], "mutant: no complementation", "negative")
