# Histone tail modifications and their readers (schematic). Tails drawn to residue scale from the globular core
# (box): H3 (N-terminal 1-40, plus K79 in the core), H4 (1-25), H2A (C-terminal K119), H2B (K120 human / K123 yeast).
# Marks: ac = acetylation, me = methylation, ph = phosphorylation, ub = ubiquitination (lollipops by type).
# Right: chromatin state associated with each mark and its reader domains. Cross-talk
# (H3S10ph -> H3K14ac; H2Bub -> H3K4me and H3K79me) listed as text.
import wikibio as bio
from matplotlib.patches import Circle

P = bio.P
fig, ax = bio.canvas(23.0, 12.0)
TOK = {"ac": "positive", "me": "negative", "ph": "highlight", "ub": "receptor"}
XS = 0.2   # canvas units per residue


def tail(y, name, length, marks, core_x=9.6, direction=-1, label_res=True):
    """A histone tail of `length` residues leaving the core box at core_x; marks = [(residue, kind, text)]."""
    bio.box(ax, (core_x + 0.9 * (-direction), y), 1.8, 0.9, "chromatin", name, size="small", radius=0.15, zorder=8)
    x_end = core_x + direction * length * XS
    ax.plot([core_x, x_end], [y, y], color=P.edge("chromatin"), lw=2.0, zorder=7)
    pos = {}
    for k, (res, kind, text) in enumerate(marks):
        x = core_x + direction * (length - res) * XS if direction < 0 else core_x + res * XS
        h = 0.65 + 0.42 * (k % 2)
        ax.plot([x, x], [y, y + h], color=P.muted(), lw=0.8, zorder=6)
        ax.add_patch(Circle((x, y + h), 0.17, facecolor=P.fill(TOK[kind]), edgecolor=P.edge(TOK[kind]), lw=0.9, zorder=9))
        bio.label(ax, (x, y + h + 0.36), text, size="tiny", zorder=10)
        pos[text] = (x, y + h)
    return pos


h3 = tail(9.6, "H3", 40, [(4, "me", "K4"), (9, "me", "K9"), (10, "ph", "S10"), (14, "ac", "K14"), (18, "ac", "K18"),
                          (27, "me", "K27"), (36, "me", "K36")])
bio.label(ax, (9.6 - 41 * XS, 9.6), "N", size="tiny", color=P.muted())
ax.add_patch(Circle((11.0, 10.1), 0.17, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.9, zorder=9))
bio.label(ax, (11.0, 10.5), "K79 (core)", size="tiny")
h4 = tail(6.6, "H4", 25, [(5, "ac", "K5"), (8, "ac", "K8"), (12, "ac", "K12"), (16, "ac", "K16"), (20, "me", "K20")])
bio.label(ax, (9.6 - 26 * XS, 6.6), "N", size="tiny", color=P.muted())
tail(4.0, "H2A", 10, [(9, "ub", "K119")], core_x=4.2, direction=1)
bio.label(ax, (4.2 + 11 * XS, 4.0), "C", size="tiny", color=P.muted())
h2b = tail(1.6, "H2B", 10, [(8, "ub", "K120")], core_x=4.2, direction=1)
bio.label(ax, (4.2 + 11 * XS, 1.6), "C", size="tiny", color=P.muted())

# cross-talk (text)
bio.label(ax, (14.6, 3.6), "cross-talk", size="small", bold=True, ha="left")
bio.label(ax, (14.6, 2.9), "H3 S10ph  →  H3 K14ac (GCN5)", size="tiny", ha="left")
bio.label(ax, (14.6, 2.3), "H2B K120ub (K123 in yeast)  →  H3 K4me (COMPASS), H3 K79me (Dot1)", size="tiny", ha="left")
bio.label(ax, (14.6, 1.7), "H3K36me3  →  Rpd3S deacetylation of gene bodies", size="tiny", ha="left")

# legend of mark types
for k, (kind, name) in enumerate([("ac", "acetylation"), ("me", "methylation"), ("ph", "phosphorylation"),
                                  ("ub", "ubiquitination")]):
    x = 0.8 + k * 2.4
    ax.add_patch(Circle((x, 0.4), 0.17, facecolor=P.fill(TOK[kind]), edgecolor=P.edge(TOK[kind]), lw=0.9))
    bio.label(ax, (x + 0.3, 0.4), name, size="tiny", ha="left")

# reader table
rows = [("H3K4me3", "active promoters", "PHD (TAF3, BPTF)"),
        ("H3K9me3", "constitutive heterochromatin", "chromodomain (HP1)"),
        ("H3K27me3", "Polycomb silencing", "chromodomain (CBX), EED"),
        ("H3K36me3", "transcribed gene bodies", "PWWP, chromodomain (Eaf3)"),
        ("H3/H4 Kac", "active promoters, enhancers", "bromodomain (BRD4, TAF1)"),
        ("H4K16ac", "decompaction", "blocks Sir3 binding"),
        ("H2AK119ub", "Polycomb (PRC1)", "PRC2 accessory subunits")]
x0, y0 = 14.6, 10.6
bio.label(ax, (x0, y0 + 0.6), "mark", size="small", bold=True, ha="left")
bio.label(ax, (x0 + 2.3, y0 + 0.6), "state", size="small", bold=True, ha="left")
bio.label(ax, (x0 + 5.9, y0 + 0.6), "readers", size="small", bold=True, ha="left")
for k, (m, st, rd) in enumerate(rows):
    y = y0 - 0.85 * k
    bio.label(ax, (x0, y), m, size="tiny", ha="left", bold=True)
    bio.label(ax, (x0 + 2.3, y), st, size="tiny", ha="left")
    bio.label(ax, (x0 + 5.9, y), rd, size="tiny", ha="left")
