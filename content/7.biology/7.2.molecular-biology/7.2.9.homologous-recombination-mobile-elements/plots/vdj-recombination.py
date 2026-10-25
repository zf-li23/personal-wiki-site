# V(D)J recombination of the human heavy-chain locus (schematic, not to scale) and the arithmetic of
# antigen-receptor diversity. A: V segments carry 23-RSSs (open triangles), D segments are flanked by
# 12-RSSs (filled triangles), J segments carry 23-RSSs; D joins J, then V joins DJ. B: combinatorial
# numbers from segment counts (about 40 V, 23 D, 6 J heavy; 40 V x 5 J kappa; 30 V x 4 J lambda) and
# a conventional order-of-magnitude estimate with junctional diversity (hatched).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(23, 10.4)
H = 0.42
seg_tok = {"V": "protein", "D": "antibody", "J": "positive", "C": "enzyme"}


def segment(x, y, kind, label, w=0.55):
    bio.box(ax, (x, y), w, H, seg_tok[kind], text=label, size="tiny", radius=0.08)


def rss(x, y, spacer, direction):
    """Triangle pointing toward the segment it flanks; 12-RSS filled, 23-RSS open."""
    d = direction
    v = np.array([[x, y - 0.17], [x, y + 0.17], [x + d * 0.3, y]])
    if spacer == 12:
        ax.fill(v[:, 0], v[:, 1], color=P.edge("negative"), lw=0, zorder=12)
    else:
        ax.fill(v[:, 0], v[:, 1], facecolor=P.surface(), edgecolor=P.edge("negative"), lw=1.1, zorder=12)


def locus(y, parts, x0=1.4, x1=21.6):
    ax.plot([x0, x1], [y, y], color=P.edge("dna"), lw=2.0, zorder=5)
    for kind, x, lab in parts:
        segment(x, y, kind, lab)
        if kind == "V":
            rss(x + 0.62, y, 23, -1)
        elif kind == "D":
            rss(x - 0.62, y, 12, 1)
            rss(x + 0.62, y, 12, -1)
        elif kind == "J":
            rss(x - 0.62, y, 23, 1)


bio.panel(ax, "A", (0.4, 10.0))
bio.label(ax, (1.0, 10.0), "Heavy-chain locus (IGH): 12/23 rule", size="normal", bold=True, ha="left")
germ = [("V", 2.2, "V1"), ("V", 3.9, "V2"), ("V", 6.6, "Vn"), ("D", 9.2, "D1"), ("D", 10.9, "D2"), ("D", 13.4, "Dn"),
        ("J", 15.6, "J1"), ("J", 16.8, "J2"), ("J", 18.0, "J6"), ("C", 20.6, "Cμ")]
locus(8.7, germ)
for x in (5.25, 12.15):
    bio.label(ax, (x, 8.7 + 0.42), "···", size="small", color=P.muted())
bio.label(ax, (17.4, 8.7 + 0.42), "···", size="small", color=P.muted())
bio.label(ax, (1.4, 9.4), "Germline", size="small", color=P.muted(), ha="left")
# step 1: D2-J1 joined
bio.arrow(ax, (11.5, 8.1), (11.5, 7.45), kind="process")
bio.label(ax, (11.8, 7.78), "D–J joining (12 × 23)", size="tiny", ha="left", color=P.muted())
dj = [("V", 2.2, "V1"), ("V", 3.9, "V2"), ("V", 6.6, "Vn"), ("D", 9.2, "D1"), ("D", 13.0, "D2"), ("J", 13.6, "J1"),
      ("J", 14.8, "J2"), ("J", 16.0, "J6"), ("C", 20.6, "Cμ")]
locus(6.9, [p for p in dj if p[2] not in ("D2", "J1")])
segment(13.0, 6.9, "D", "D2")
segment(13.6, 6.9, "J", "J1")
rss(12.38, 6.9, 12, 1)
# step 2: V2 joined to D2J1
bio.arrow(ax, (11.5, 6.3), (11.5, 5.65), kind="process")
bio.label(ax, (11.8, 5.98), "V–DJ joining (23 × 12)", size="tiny", ha="left", color=P.muted())
ax.plot([1.4, 21.6], [5.1, 5.1], color=P.edge("dna"), lw=2.0, zorder=5)
segment(2.2, 5.1, "V", "V1"); rss(2.82, 5.1, 23, -1)
segment(3.9, 5.1, "V", "V2"); segment(4.5, 5.1, "D", "D2"); segment(5.1, 5.1, "J", "J1")
for (k, x, lab) in (("J", 6.3, "J2"), ("J", 7.5, "J6")):
    segment(x, 5.1, k, lab); rss(x - 0.62, 5.1, 23, 1)
segment(20.6, 5.1, "C", "Cμ")
bio.label(ax, (4.5, 4.45), "VDJ exon", size="tiny", color=P.muted())
# legend for triangles
rss(14.0, 4.4, 12, 1); bio.label(ax, (14.45, 4.4), "12-RSS", size="tiny", ha="left")
rss(16.0, 4.4, 23, 1); bio.label(ax, (16.45, 4.4), "23-RSS", size="tiny", ha="left")
bio.label(ax, (18.2, 4.4), "heptamer–spacer–nonamer", size="tiny", ha="left", color=P.muted())

# B: diversity numbers
bio.panel(ax, "B", (0.4, 3.4))
b = C.axes_at(ax, (6.2, 0.45, 13.5, 2.6))
items = [("Heavy chains, V × D × J", 40 * 23 * 6, "protein"), ("Light chains, κ + λ", 40 * 5 + 30 * 4, "positive"),
         ("Heavy–light pairs", 40 * 23 * 6 * (40 * 5 + 30 * 4), "enzyme")]
for k, (name, val, tok) in enumerate(items):
    yv = len(items) - k
    b.barh(yv, val, left=1, height=0.6, color=P.fill(tok), edgecolor=C.line(tok), lw=0.9)
    b.text(val * 1.4, yv, f"{val:,.0f}".replace(",", " "), va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.barh(0, 1e11, left=1, height=0.6, facecolor="none", edgecolor=C.line("neutral"), hatch="///", lw=0.9)
b.text(1e11 * 1.4, 0, "≥ 10¹¹", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_xscale("log")
b.set_xlim(1, 1e14)
b.set_xticks([1, 1e3, 1e6, 1e9, 1e12], ["1", "10³", "10⁶", "10⁹", "10¹²"])
b.minorticks_off()
b.set_yticks([3, 2, 1, 0], [i[0] for i in items] + ["With junctional diversity"])
b.set_ylim(-0.6, 3.6)
C.style_axes(b, "Number of distinct sequences", None)
b.tick_params(axis="y", length=0)
