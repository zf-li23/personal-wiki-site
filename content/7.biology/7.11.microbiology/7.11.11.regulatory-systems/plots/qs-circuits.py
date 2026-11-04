"""Three quorum-sensing architectures (activity-flow diagrams; arrows activate, bars inhibit).
A: Vibrio harveyi and V. cholerae. Membrane receptors for species-specific autoinducers (AI-1, CAI-1) and
   for AI-2 are kinases at low cell density: phosphate flows through LuxU to LuxO, which with sigma-54
   activates the Qrr small RNAs; with Hfq these block translation of the master regulator LuxR (HapR in
   V. cholerae). At high density the bound receptors become phosphatases, Qrr disappears and LuxR/HapR
   is made.
B: Pseudomonas aeruginosa. LasR with 3-oxo-C12-HSL (made by LasI) sits at the top and activates the Rhl
   (C4-HSL) and PQS systems and its own synthase; the three systems together control virulence genes.
C: Staphylococcus aureus agr. AgrD is processed and exported by AgrB as the autoinducing peptide (AIP),
   sensed by the histidine kinase AgrC; AgrA-P activates the agr operon itself (P2) and RNAIII (P3),
   which raises secreted toxins and lowers surface adhesins."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
pos = {}


def node(key, xy, text, token="protein", w=2.2, h=0.75, italic=False):
    bio.box(ax, xy, w, h, token=token, text=text, size="tiny", italic=italic, radius=0.25, zorder=10)
    pos[key] = (xy, w, h)


def edge(a, b, kind="activation", dashed=False, bend=0.0, color=None):
    (xa, ya), wa, ha = pos[a]
    (xb, yb), wb, hb = pos[b]
    # attach to the box sides facing each other
    if abs(yb - ya) > abs(xb - xa):
        pa = (xa, ya - ha / 2 if yb < ya else ya + ha / 2)
        pb = (xb, yb + hb / 2 if yb < ya else yb - hb / 2)
    else:
        pa = (xa + wa / 2 if xb > xa else xa - wa / 2, ya)
        pb = (xb - wb / 2 if xb > xa else xb + wb / 2, yb)
    bio.arrow(ax, pa, pb, kind=kind, dashed=dashed, bend=bend, lw=1.1, head=0.2, color=color, shrink=0.05)


def chem(key, xy, text):
    node(key, xy, text, token="metabolite", w=1.8, h=0.6)


# ---- A: Vibrio
bio.panel(ax, "A", (0.2, 10.9))
bio.label(ax, (1.0, 10.6), "Vibrio harveyi / V. cholerae", size="small", bold=True, ha="left", italic=True)
for k, (x, ai, rc) in enumerate(((1.6, "AI-1 / CAI-1", "LuxN / CqsS"), (4.6, "AI-2", "LuxPQ"))):
    chem(f"ai{k}", (x, 9.2), ai)
    node(f"r{k}", (x, 7.6), rc, token="receptor", w=2.4)
    edge(f"ai{k}", f"r{k}", kind="inhibition")
bio.label(ax, (3.1, 8.4), "ligand turns\nkinase into\nphosphatase", size="tiny", color=P.muted())
node("luxu", (3.1, 6.0), "LuxU", w=1.6)
node("luxo", (3.1, 4.6), "LuxO-P + σ⁵⁴", w=2.4)
node("qrr", (3.1, 3.2), "Qrr sRNAs (+ Hfq)", token="rna", w=3.0)
node("luxr", (3.1, 1.8), "LuxR / HapR", token="positive", w=2.4)
edge("r0", "luxu")
edge("r1", "luxu")
edge("luxu", "luxo")
edge("luxo", "qrr")
edge("qrr", "luxr", kind="inhibition")
bio.label(ax, (3.1, 0.75), "high density: light (V. harveyi);\nbiofilm and toxin genes off (V. cholerae)",
          size="tiny", color=P.muted())

# ---- B: Pseudomonas
bx = 10.0
bio.panel(ax, "B", (bx - 1.6, 10.9))
bio.label(ax, (bx - 0.8, 10.6), "Pseudomonas aeruginosa", size="small", bold=True, ha="left", italic=True)
node("lasi", (bx + 0.2, 9.2), "LasI", token="enzyme", w=1.6)
chem("c12", (bx + 2.6, 9.2), "3-oxo-C12-HSL")
node("lasr", (bx + 5.2, 9.2), "LasR", token="positive", w=1.6)
edge("lasi", "c12", kind="process")
edge("c12", "lasr")
node("rhli", (bx + 0.2, 6.6), "RhlI", token="enzyme", w=1.6)
chem("c4", (bx + 2.6, 6.6), "C4-HSL")
node("rhlr", (bx + 5.2, 6.6), "RhlR", token="positive", w=1.6)
edge("rhli", "c4", kind="process")
edge("c4", "rhlr")
node("pqsa", (bx + 0.2, 4.2), "PqsABCDH", token="enzyme", w=2.0)
chem("pqs", (bx + 2.6, 4.2), "PQS")
node("pqsr", (bx + 5.2, 4.2), "PqsR", token="positive", w=1.6)
edge("pqsa", "pqs", kind="process")
edge("pqs", "pqsr")
edge("lasr", "rhlr")
bio.arrow(ax, (bx + 6.0, 9.2), (bx + 6.0, 4.2), kind="activation", lw=1.1, head=0.2, bend=0.35)
bio.arrow(ax, (bx + 5.2, 9.58), (bx + 0.2, 9.58), kind="activation", lw=1.0, head=0.18, bend=-0.25)
bio.label(ax, (bx + 2.6, 8.2), "autoinduction; LasR also\ninduces rhlI and pqsA", size="tiny", color=P.muted())
node("vir", (bx + 3.2, 1.6), "elastase, pyocyanin, rhamnolipids,\nHCN, biofilm matrix", token="highlight", w=5.6, h=1.1)
for k in ("rhlr", "pqsr"):
    edge(k, "vir")

# ---- C: Staphylococcus
cx = 20.5
bio.panel(ax, "C", (cx - 1.4, 10.9))
bio.label(ax, (cx - 0.6, 10.6), "Staphylococcus aureus (agr)", size="small", bold=True, ha="left", italic=True)
ax.plot([cx - 1.0, cx + 9.0], [8.4, 8.4], color=P.edge("lipid_head"), lw=4.0, solid_capstyle="round", zorder=2)
bio.label(ax, (cx + 9.0, 8.75), "membrane", size="tiny", color=P.muted(), ha="right")
node("agrd", (cx + 0.6, 6.8), "AgrD (pro-AIP)", w=2.6)
node("agrb", (cx + 0.6, 8.4), "AgrB", token="enzyme", w=1.6)
chem("aip", (cx + 3.2, 9.6), "AIP")
node("agrc", (cx + 5.6, 8.4), "AgrC", token="receptor", w=1.6)
node("agra", (cx + 5.6, 6.8), "AgrA-P", token="positive", w=1.8)
edge("agrd", "agrb", kind="process")
bio.arrow(ax, (cx + 1.0, 8.8), (cx + 2.4, 9.5), kind="process", lw=1.1, head=0.2)
bio.arrow(ax, (cx + 4.1, 9.5), (cx + 5.3, 8.8), kind="activation", lw=1.1, head=0.2)
edge("agrc", "agra")
bio.label(ax, (cx + 6.9, 7.6), "His~P → Asp", size="tiny", color=P.muted())
node("p2", (cx + 2.4, 5.0), "P2: agrBDCA", token="dna", w=2.6, italic=False)
node("p3", (cx + 6.4, 5.0), "P3: RNAIII", token="rna", w=2.4)
edge("agra", "p2")
edge("agra", "p3")
bio.arrow(ax, (cx + 1.6, 5.38), (cx + 0.6, 6.42), kind="process", lw=1.0, head=0.18, dashed=True)
node("tox", (cx + 4.8, 2.9), "secreted toxins and\nexoenzymes up", token="highlight", w=3.4, h=1.0)
node("adh", (cx + 8.0, 2.9), "surface\nadhesins down", token="neutral", w=2.2, h=1.0)
edge("p3", "tox")
edge("p3", "adh", kind="inhibition")
bio.label(ax, (cx + 4.0, 1.2), "positive feedback: AgrA-P induces more AgrB, AgrD, AgrC, AgrA", size="tiny",
          color=P.muted())
