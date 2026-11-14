"""Supergenes: the ruff chromosome 11 inversion and the fire ant social chromosome (schematic)."""

from matplotlib.patches import FancyBboxPatch, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 13.0)


def chrom(x, y, w, seg=None, seg_tok="rna", label=None, h=0.55, hatch=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.27",
                                facecolor=P.mix(P.fill("dna"), P.surface(), 0.7), edgecolor=P.edge("dna"), lw=1.0, zorder=5))
    if seg:
        a, b = seg
        ax.add_patch(Rectangle((x + a, y), b - a, h, facecolor=P.fill(seg_tok), edgecolor=P.edge(seg_tok),
                               lw=0.8, zorder=6, hatch="///" if hatch else None))
    if label:
        bio.label(ax, (x - 0.3, y + h / 2), label, size="tiny", ha="right")


# A: ruff
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (8.0, 12.3), "Ruff: inversion on chromosome 11", size="small", bold=True)
rows = [("Independent", None, None, "ancestral / ancestral", "about 84% of males; ornamented, hold courts"),
        ("Satellite", "rna", True, "satellite / ancestral", "about 15%; white ruff, no court"),
        ("Faeder", "rna", False, "faeder / ancestral", "under 1%; female mimic, large testes")]
y = 10.2
for name, tok, hatch, gt, note in rows:
    bio.label(ax, (0.6, y + 0.1), name, size="small", bold=True, ha="left")
    chrom(4.6, y + 0.35, 6.0, (2.0, 4.0) if tok else None, tok or "rna", hatch=hatch)
    chrom(4.6, y - 0.45, 6.0)
    bio.label(ax, (11.1, y + 0.3), gt, size="tiny", ha="left")
    bio.label(ax, (11.1, y - 0.3), note, size="tiny", ha="left", color=P.muted())
    y -= 2.4
bio.label(ax, (7.6, 2.4), "inversion / inversion: lethal (breakpoint disrupts CENPN)", size="tiny", color=P.edge("negative"))
bio.label(ax, (7.6, 1.6), "4.5 Mb inversion, about 3.8 Myr old; hatched: recombinant satellite haplotype", size="tiny",
          color=P.muted())

# B: fire ant
bio.panel(ax, "B", (19.0, 12.7))
bio.label(ax, (24.6, 12.3), "Fire ant: social chromosome", size="small", bold=True)
items = [("SB / SB", False, "monogyne colony: one queen"), ("SB / Sb", True, "queens of polygyne colonies"),
         ("Sb / Sb", "both", "die young")]
y = 10.2
for gt, sb, note in items:
    bio.label(ax, (19.6, y + 0.1), gt, size="small", bold=True, ha="left")
    chrom(22.4, y + 0.35, 5.2, (1.2, 4.0), "plant" if sb != "both" else "protein")
    chrom(22.4, y - 0.45, 5.2, (1.2, 4.0), "protein" if sb else "plant")
    bio.label(ax, (25.0, y - 1.0), note, size="tiny", color=P.muted())
    y -= 2.4
for tok, txt, xx in [("plant", "SB", 20.2), ("protein", "Sb", 23.2)]:
    ax.add_patch(Rectangle((xx, 2.2), 0.8, 0.45, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (xx + 1.1, 2.42), txt + " supergene variant", size="tiny", ha="left")
bio.label(ax, (24.6, 1.4), "workers carrying Sb kill SB / SB queens", size="tiny", color=P.muted())
