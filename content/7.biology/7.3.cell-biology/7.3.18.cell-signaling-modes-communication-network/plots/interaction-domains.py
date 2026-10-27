"""Signaling proteins are built from a small set of interaction domains.

A: domain architectures of human signaling proteins drawn to scale (approximate residue boundaries from
UniProt); lines are linkers and disordered regions, P marks phosphotyrosines that serve as docking sites
or switches (Tyr527 of chicken Src, Tyr705 of STAT3). SH2 and PTB domains bind phosphotyrosine, SH3
binds Pro-rich motifs (PRR), PH binds phosphoinositides, PDZ binds C-terminal peptides; DH, Cdc25 and
RasGAP-like modules are the catalytic GEF or GAP domains; kinase and PLC X/Y boxes are enzymes.
B: assembly by induced proximity at an activated receptor tyrosine kinase: phosphotyrosines (P) are
read by the SH2 domains of Grb2, of the p85 subunit of PI3K and of PLCgamma; Grb2's SH3 domains hold Sos
by its Pro-rich tail; PIP3 made by PI3K recruits PH-domain proteins such as PKB to the membrane.
"""

from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 12.2)
S = 0.0078  # canvas units per residue
X0 = 3.6

COL = {"SH2": "receptor", "SH3": "channel", "PTB": "carbohydrate", "PH": "lipid", "PDZ": "antibody",
       "kinase": "enzyme", "cat": "highlight", "other": "neutral"}

proteins = [
    ("Grb2", 217, [(1, 58, "SH3", "SH3"), (60, 152, "SH2", "SH2"), (156, 215, "SH3", "SH3")], []),
    ("Src", 536, [(84, 145, "SH3", "SH3"), (151, 248, "SH2", "SH2"), (270, 519, "kinase", "kinase")], [527]),
    ("Shc1", 583, [(46, 233, "PTB", "PTB"), (488, 579, "SH2", "SH2")], [317]),
    ("IRS1", 1242, [(12, 115, "PH", "PH"), (160, 264, "PTB", "PTB")], [465, 612, 632, 662, 732, 896, 941, 989]),
    ("PI3K p85α", 724, [(3, 79, "SH3", "SH3"), (113, 301, "other", "BH"), (333, 428, "SH2", "SH2"),
                        (429, 621, "other", "iSH2"), (624, 718, "SH2", "SH2")], []),
    ("PLCγ1", 1290, [(16, 131, "PH", "PH"), (320, 464, "cat", "X box"), (550, 657, "SH2", "SH2"),
                     (668, 756, "SH2", "SH2"), (791, 851, "SH3", "SH3"), (952, 1070, "cat", "Y box")], [783]),
    ("STAT3", 770, [(138, 320, "other", "coiled coil"), (320, 465, "other", "DBD"), (585, 688, "SH2", "SH2")], [705]),
    ("Sos1", 1333, [(200, 390, "cat", "DH"), (444, 548, "PH", "PH"), (780, 1019, "cat", "Cdc25 (GEF)"),
                    (1050, 1333, "other", "PRR")], []),
    ("Dishevelled 2", 736, [(10, 92, "other", "DIX"), (265, 350, "PDZ", "PDZ"), (433, 507, "other", "DEP")], []),
]

bio.panel(ax, "A", (0.1, 12.1))
y = 11.3
for name, length, doms, ptyr in proteins:
    bio.label(ax, (X0 - 0.3, y), name, size="small", ha="right")
    ax.plot([X0, X0 + length * S], [y, y], color=P.muted(), lw=1.6, solid_capstyle="round", zorder=5)
    for a, b, kind, text in doms:
        tok = COL[kind]
        w = (b - a) * S
        ax.add_patch(FancyBboxPatch((X0 + a * S, y - 0.24), w, 0.48, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=8))
        bio.label(ax, (X0 + (a + b) / 2 * S, y), text, size="tiny", color=P.on_fill(), zorder=9)
    for r in ptyr:
        ax.add_patch(Circle((X0 + r * S, y + 0.36), 0.1, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                            lw=0.7, zorder=10))
        bio.label(ax, (X0 + r * S, y + 0.36), "P", size="tiny", color=P.on_fill(), zorder=11)
    bio.label(ax, (X0 + length * S + 0.15, y), f"{length} aa", size="tiny", color=P.muted(), ha="left")
    y -= 1.1
bio.scale_bar(ax, (X0, 1.25), 200 * S, "200 residues", size="tiny")

# B: assembly at an activated RTK
bio.panel(ax, "B", (15.4, 12.1))
mx0, mx1, my = 15.6, 21.8, 8.6
ax.add_patch(FancyBboxPatch((mx0, my - 0.25), mx1 - mx0, 0.5, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("membrane"), edgecolor=P.edge("membrane"), lw=0.8, zorder=3))
bio.label(ax, (mx0 + 0.1, my + 0.55), "outside", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (mx0 + 0.1, my - 0.6), "cytosol", size="tiny", color=P.muted(), ha="left")
rx = 18.0
for dx in (-0.28, 0.28):
    bio.box(ax, (rx + dx, my + 0.95), 0.42, 1.0, token="receptor", radius=0.15)
    ax.plot([rx + dx, rx + dx], [my - 0.3, my + 0.4], color=P.edge("receptor"), lw=2.2, zorder=6)
    bio.box(ax, (rx + dx, my - 1.0), 0.42, 0.9, token="enzyme", radius=0.15)
    ax.plot([rx + dx, rx + dx], [my - 1.45, my - 3.8], color=P.edge("enzyme"), lw=1.4, zorder=5)
ax.add_patch(Circle((rx, my + 1.6), 0.18, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.8, zorder=12))
bio.label(ax, (rx + 0.35, my + 1.65), "ligand", size="tiny", ha="left")
L, R = rx - 0.28, rx + 0.28
y1, y2, y3 = my - 2.1, my - 2.5, my - 3.4
for sx, sy in ((L, y1), (R, y2), (R, y3)):
    ax.add_patch(Circle((sx, sy), 0.12, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=10))
    bio.label(ax, (sx, sy), "P", size="tiny", color=P.on_fill(), zorder=11)
# Grb2 on the left site, Sos held by its SH3 domain
bio.box(ax, (L - 0.5, y1), 0.62, 0.4, token="receptor", text="SH2", size="tiny", radius=0.1)
bio.box(ax, (L - 0.5, y1 - 0.45), 0.62, 0.4, token="channel", text="SH3", size="tiny", radius=0.1)
bio.label(ax, (L - 0.5, y1 + 0.45), "Grb2", size="tiny")
bio.box(ax, (L - 1.7, y1 - 0.45), 0.95, 0.55, token="highlight", text="Sos", size="small", radius=0.12)
ax.plot([L - 1.22, L - 0.81], [y1 - 0.45, y1 - 0.45], color=P.ink(), lw=0.9, zorder=9)
bio.label(ax, (L - 1.0, y1 - 0.85), "PRR", size="tiny", color=P.muted())
# PI3K and PLCgamma on the right sites
bio.box(ax, (R + 0.5, y2), 0.62, 0.4, token="receptor", text="SH2", size="tiny", radius=0.1)
bio.box(ax, (R + 1.45, y2), 1.1, 0.5, token="enzyme", text="p110", size="tiny", radius=0.12)
bio.label(ax, (R + 1.0, y2 + 0.5), "PI3K (p85–p110)", size="tiny")
bio.box(ax, (R + 0.5, y3), 0.62, 0.4, token="receptor", text="SH2", size="tiny", radius=0.1)
bio.box(ax, (R + 1.5, y3), 1.2, 0.5, token="highlight", text="PLCγ", size="tiny", radius=0.12)
# PIP3 and PKB at membrane
for px in (20.2, 20.6, 21.0):
    ax.add_patch(Circle((px, my - 0.38), 0.09, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.6, zorder=9))
bio.box(ax, (20.6, my - 0.85), 0.7, 0.38, token="lipid", text="PH", size="tiny", radius=0.1)
bio.box(ax, (20.6, my - 1.35), 1.1, 0.55, token="enzyme", text="PKB", size="tiny", radius=0.12)
bio.arrow(ax, (19.75, my - 2.2), (20.12, my - 0.5), kind="process", color=P.ink(), lw=0.9, bend=-0.15)
bio.label(ax, (21.6, my - 0.38), "PIP₃", size="tiny", ha="left")
bio.label(ax, (18.9, 3.4), "induced proximity:\nphosphorylation creates\nbinding sites, and\nbinding brings enzymes\nto their substrates", size="tiny",
          color=P.muted())
