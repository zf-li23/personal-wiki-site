# Ordering peptide fragments by overlaps. A hypothetical 24-residue polypeptide is cleaved in two samples:
# trypsin (after Lys and Arg, not before Pro) gives five fragments T1-T5, cyanogen bromide (after Met) gives
# three fragments C1-C3. Each fragment is sequenced (Edman degradation or MS/MS); fragments from one digest
# that span the cleavage sites of the other place the fragments in order. N-terminal (Gly) and C-terminal (Cys)
# residues determined separately mark the ends.
import re
import wikibio as bio

seq = "GAVLKMSDYRWFNPQKTMEHLRGC"
W = 0.52          # width of one residue
x0 = 1.6


def cuts(pattern):
    return [m.end() for m in re.finditer(pattern, seq)]


def fragments(sites):
    edges = [0] + sites + [len(seq)]
    return [(a, b) for a, b in zip(edges[:-1], edges[1:]) if b > a]


def row(y, frags, token, prefix):
    for k, (a, b) in enumerate(frags):
        cx = x0 + W * (a + b) / 2
        bio.box(ax, (cx, y), W * (b - a) - 0.08, 0.62, token, radius=0.12)
        for i in range(a, b):
            bio.label(ax, (x0 + W * (i + 0.5), y), seq[i], size="small", color=bio.P.on_fill(), zorder=12)
        if prefix:
            bio.label(ax, (cx, y + 0.55), f"{prefix}{k + 1}", size="tiny")


fig, ax = bio.canvas(16, 7.2)
tryp = fragments(cuts(r"[KR](?!P)"))
cnbr = fragments(cuts(r"M"))
bio.label(ax, (x0 - 0.25, 6.0), "sequence", size="small", ha="right")
bio.label(ax, (x0 - 0.25, 4.1), "trypsin", size="small", ha="right")
bio.label(ax, (x0 - 0.25, 2.2), "CNBr", size="small", ha="right")
row(6.0, [(0, len(seq))], "protein", "")
row(4.1, tryp, "enzyme", "T")
row(2.2, cnbr, "drug", "C")
for s in cuts(r"[KR](?!P)"):
    x = x0 + W * s
    ax.plot([x, x], [3.6, 6.35], color=bio.P.edge("enzyme"), lw=0.9, ls=(0, (3, 2)), zorder=4)
for s in cuts(r"M"):
    x = x0 + W * s
    ax.plot([x, x], [1.75, 6.35], color=bio.P.edge("drug"), lw=0.9, ls=(0, (1, 2)), zorder=4)
bio.label(ax, (x0 + W * 0.5, 6.85), "N-terminus: Gly", size="tiny", ha="left")
bio.label(ax, (x0 + W * len(seq), 6.85), "C-terminus: Cys", size="tiny", ha="right")
bio.label(ax, (x0 + W * len(seq) / 2, 0.9),
          "C1 joins T1 to T2, C2 joins T2, T3 and T4, C3 joins T4 and T5: order T1–T2–T3–T4–T5", size="small")
