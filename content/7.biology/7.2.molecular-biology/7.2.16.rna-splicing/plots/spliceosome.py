# The spliceosome cycle and the RNA-RNA network at its active center.
# A: the major (U2-type) spliceosome assembles anew on every intron. E: U1 snRNP pairs with the 5' splice site,
# SF1 binds the branch site and U2AF the pyrimidine tract and AG. A: U2 snRNP pairs with the branch site
# (ATP-dependent; Prp5, UAP56). Pre-B/B: the U4/U6.U5 tri-snRNP joins. Bact: the helicase Brr2 unwinds U4
# from U6, U1 and U4 leave, U6 pairs with the 5' splice site and with U2. C: first transesterification
# (after Prp2 remodels). C*/P: second transesterification (Prp16, Prp22). ILS: the mRNA is released (Prp22)
# and the intron-lariat spliceosome is disassembled (Prp43); the snRNPs are recycled.
# B: base pairing in the catalytically activated spliceosome (schematic, not to scale): U6 pairs with the
# 5' end of the intron (ACAGA box with intron +4 to +6) and with U2 (helix I); U2 pairs with the branch site,
# leaving the branch A bulged; loop 1 of U5 contacts the last nucleotides of exon 1 and the first of exon 2.
import numpy as np
import wikibio as bio
from wikibio import ecology as E

P = bio.P
fig, ax = bio.canvas(25.0, 10.0)

# --- A: cycle -----------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.85))
steps = [
    dict(text="E\nU1 · SF1 · U2AF", token="protein", w=2.9, h=1.05),
    dict(text="A\nU2 on branch site", token="protein", w=2.9, h=1.05),
    dict(text="B\n+ U4/U6·U5", token="enzyme", w=2.6, h=1.05),
    dict(text="Bact\nU1, U4 leave", token="enzyme", w=2.6, h=1.05),
    dict(text="C\nstep 1 done", token="positive", w=2.6, h=1.05),
    dict(text="P\nstep 2 done", token="positive", w=2.6, h=1.05),
    dict(text="ILS\nmRNA released", token="neutral", w=2.8, h=1.05),
]
E.cycle(ax, (6.3, 4.85), 3.65, steps, start=90, size="small",
        arrow_labels=["ATP (Prp5)", "", "Brr2 (ATP)", "Prp2 (ATP)", "Prp16 (ATP)", "Prp22 (ATP)", "Prp43: recycle"],
        label_size="tiny", center_text="pre-mRNA\non a new intron")

# --- B: RNA network ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.4, 9.85))
y = 4.1
x0, x5, xbp, x3, x1 = 14.0, 16.2, 21.0, 22.6, 24.6
bio.box(ax, ((x0 + x5) / 2, y), x5 - x0, 0.55, token="mrna", text="Exon 1", size="tiny", radius=0.06, zorder=6)
bio.box(ax, ((x3 + x1) / 2, y), x1 - x3, 0.55, token="mrna", text="Exon 2", size="tiny", radius=0.06, zorder=6)
ax.plot([x5, x3], [y, y], color=P.edge("rna"), lw=1.6, zorder=5)
bio.label(ax, (x5 + 0.3, y - 0.45), "GU", size="tiny", bold=True, color=P.edge("rna"))
bio.label(ax, (x3 - 0.3, y - 0.45), "AG", size="tiny", bold=True, color=P.edge("rna"))
bio.label(ax, (13.75, y), "5′", size="tiny", bold=True)
bio.label(ax, (24.85, y), "3′", size="tiny", bold=True)
# bulged branch A
ax.add_patch(bio.core.Circle((xbp, y - 0.62), 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=0.9, zorder=11))
bio.label(ax, (xbp, y - 0.62), "A", size="tiny", bold=True, color=P.on_fill(), zorder=12)
ax.plot([xbp - 0.15, xbp, xbp + 0.15], [y, y - 0.42, y], color=P.edge("rna"), lw=1.2, zorder=5)


def snrna(xa, xb, yy, token, name, lab_dy=0.35):
    ax.plot([xa, xb], [yy, yy], color=P.edge(token), lw=3.2, solid_capstyle="round", zorder=7)
    bio.label(ax, ((xa + xb) / 2, yy + lab_dy), name, size="small", bold=True, color=P.edge(token))


def pairs(xa, xb, ya, yb, n=6):
    for xx in np.linspace(xa, xb, n):
        ax.plot([xx, xx], [ya, yb], color=P.muted(), lw=0.8, zorder=4)


# U6 pairs with intron +4..+6 just after the 5' splice site
snrna(x5 + 0.5, x5 + 1.6, y + 0.85, "trna", "")
bio.label(ax, (x5 + 0.4, y + 1.25), "U6 (ACAGA box)", size="small", bold=True, color=P.edge("trna"), ha="right")
pairs(x5 + 0.6, x5 + 1.5, y + 0.12, y + 0.78, 4)
# U2 pairs with the branch site (on both sides of the bulged A)
snrna(xbp - 1.2, xbp + 1.0, y + 0.85, "dna", "U2", lab_dy=0.35)
pairs(xbp - 1.1, xbp - 0.25, y + 0.12, y + 0.78, 4)
pairs(xbp + 0.25, xbp + 0.9, y + 0.12, y + 0.78, 3)
# U2/U6 helix I drawn above
snrna(x5 + 1.9, xbp - 1.45, y + 2.35, "trna", "U6 ISL")
snrna(x5 + 1.9, xbp - 1.45, y + 1.65, "dna", "")
pairs(x5 + 2.1, xbp - 1.65, y + 1.72, y + 2.28, 7)
bio.label(ax, (xbp - 1.1, y + 2.0), "U2–U6 helix I", ha="left", size="tiny", color=P.muted())
ax.plot([x5 + 1.6, x5 + 1.9], [y + 0.85, y + 2.35], color=P.edge("trna"), lw=2.0, zorder=7)
ax.plot([xbp - 1.2, xbp - 1.45], [y + 0.85, y + 1.65], color=P.edge("dna"), lw=2.0, zorder=7)
# Mg ions at the catalytic center
for k, xx in enumerate((18.6, 19.0)):
    bio.ion(ax, (xx, y + 3.05), "mg", r=0.17, text=False)
bio.label(ax, (19.35, y + 3.05), "catalytic Mg²⁺ ions held by U6", size="tiny", color=P.muted(), ha="left")
# U5 loop 1 bridging the exon ends
th = np.linspace(np.pi * 1.05, np.pi * 1.95, 80)
cx, r = (x5 + x3) / 2, (x3 - x5) / 2 + 0.2
ax.plot(cx + r * np.cos(th), y - 0.65 + 1.0 * np.sin(th) * 1.6, color=P.edge("enzyme"), lw=3.0, zorder=3)
bio.label(ax, (cx, y - 2.55), "U5 loop 1 holds both exon ends", size="small", bold=True, color=P.edge("enzyme"))
ax.plot([x5 - 0.05, x5 - 0.05], [y - 0.3, y - 0.95], color=P.edge("enzyme"), lw=1.0, ls=(0, (2, 1.5)))
ax.plot([x3 + 0.05, x3 + 0.05], [y - 0.3, y - 0.95], color=P.edge("enzyme"), lw=1.0, ls=(0, (2, 1.5)))
bio.label(ax, (19.3, 8.9), "Activated spliceosome: an RNA active site", size="normal", bold=True)
bio.label(ax, (19.3, 8.3), "U1 and U4 have left; proteins (Prp8 scaffold) not drawn", size="tiny", color=P.muted())
