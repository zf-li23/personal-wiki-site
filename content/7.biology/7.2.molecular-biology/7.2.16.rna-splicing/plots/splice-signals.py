# The splicing signals of a mammalian U2-type intron.
# A: map of an intron between two exons: the 5' splice site (exon|GURAGU), the branch site 18-40 nt
# upstream of the 3' splice site, the polypyrimidine tract and the 3' splice site (YAG|G), with the
# factors of the early (E) complex that recognize each signal; below, the yeast consensus.
# B: sequence logos built from the classic percentages of the consensus base at each position
# (Mount 1982 for the splice sites: 5' A64 G73 | G100 U100 A62 A68 G84 U63; 3' C65 A100 G100 after a
# pyrimidine tract; branch site U47 N C63 U53 R72 A91 C47 as compiled by Weaver). The remaining probability
# is shared equally by the other bases (R split between A and G; tract positions drawn as 80 % pyrimidine),
# so the logos show conservation, not complete base distributions.
import numpy as np
import wikibio as bio
from wikibio import quant as Q
from wikibio import sequence as S

P = bio.P
fig, ax = bio.canvas(23.0, 9.6)

# --- A: intron map ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.45))
y = 6.8
x_e1, x_5, x_bp, x_py0, x_py1, x_3, x_e2 = 1.2, 4.2, 13.6, 15.0, 17.2, 18.0, 21.8
bio.box(ax, ((x_e1 + x_5) / 2, y), x_5 - x_e1, 0.8, token="mrna", text="Exon 1", size="small", radius=0.1, zorder=6)
bio.box(ax, ((x_3 + x_e2) / 2, y), x_e2 - x_3, 0.8, token="mrna", text="Exon 2", size="small", radius=0.1, zorder=6)
ax.plot([x_5, x_3], [y, y], color=P.edge("rna"), lw=1.8, zorder=4)
bio.label(ax, ((x_5 + x_bp) / 2, y - 0.35), "intron (tens of nt to hundreds of kb)", size="tiny", color=P.muted())
# signals on the intron
bio.label(ax, (x_5 + 0.75, y + 0.42), "GURAGU", size="small", bold=True, color=P.edge("rna"))
bio.label(ax, (x_bp, y + 0.42), "YNYURAY", size="small", bold=True, color=P.edge("rna"))
ax.plot([x_bp + 0.45, x_bp + 0.45], [y - 0.05, y - 0.45], color=P.edge("negative"), lw=1.0)
bio.label(ax, (x_bp + 0.45, y - 0.65), "branch A", size="tiny", color=P.edge("negative"))
bio.box(ax, ((x_py0 + x_py1) / 2, y), x_py1 - x_py0, 0.42, token="highlight", text="(Y)n", size="tiny", radius=0.06, zorder=6)
bio.label(ax, (x_3 - 0.42, y + 0.42), "YAG", size="small", bold=True, color=P.edge("rna"))
for xx in (x_5, x_3):
    ax.plot([xx, xx], [y - 0.55, y + 0.55], color=P.ink(), lw=1.0, ls=(0, (2, 1.5)), zorder=7)
# distance bracket between branch point and 3' splice site
Q.bracket(ax, (x_bp + 0.45, y - 1.05), (x_3, y - 1.05), text="18–40 nt", side=-1)
# factors of the E complex
fy = y + 1.85
bio.protein(ax, (x_5 + 0.3, fy), 1.6, 0.85, "protein", text="U1 snRNP", size="tiny")
bio.protein(ax, (x_bp + 0.3, fy), 1.6, 0.8, "enzyme", text="SF1 (BBP)", size="tiny")
bio.protein(ax, ((x_py0 + x_py1) / 2, fy), 1.4, 0.8, "receptor", text="U2AF65", size="tiny")
bio.protein(ax, (x_3 - 0.2, fy + 0.05), 1.15, 0.7, "positive", text="U2AF35", size="tiny")
for xx in (x_5 + 0.3, x_bp + 0.3, (x_py0 + x_py1) / 2, x_3 - 0.2):
    ax.plot([xx, xx], [fy - 0.42, y + 0.7], color=P.muted(), lw=0.7, zorder=3)
bio.label(ax, (8.9, fy + 0.95), "early (E) complex: recognition of the signals", size="small", color=P.muted())
# yeast consensus
bio.label(ax, (1.2, y - 2.0), "Yeast:", size="small", bold=True, ha="left")
bio.label(ax, (3.0, y - 2.0), "exon | GUAUGU … UACUAAC … YAG | exon  (branch A = last A of UACUAAC, invariant)",
          size="small", ha="left")
bio.label(ax, (x_e2 + 0.35, y - 0.02), "3′", size="tiny", bold=True)
bio.label(ax, (x_e1 - 0.3, y - 0.02), "5′", size="tiny", bold=True)

# --- B: logos --------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 4.0))
alphabet = "ACGU"


def row(dist):
    # dist: dict base -> probability; missing bases share the rest equally
    left = 1 - sum(dist.values())
    others = [b for b in alphabet if b not in dist]
    return [dist.get(b, left / len(others) if others else 0.0) for b in alphabet]


def cons(base, pc):
    if base == "N":
        return [0.25] * 4
    if base == "R":
        f = pc / 100
        return row({"A": f / 2, "G": f / 2})
    return row({base: pc / 100})


five = [("A", 64), ("G", 73), ("G", 100), ("U", 100), ("A", 62), ("A", 68), ("G", 84), ("U", 63)]
m5 = np.array([cons(b, p) for b, p in five])
branch = [("U", 47), ("N", 0), ("C", 63), ("U", 53), ("R", 72), ("A", 91), ("C", 47)]
mb = np.array([cons(b, p) for b, p in branch])
py = row({"U": 0.45, "C": 0.35})
three = [py] * 8 + [cons("N", 0), cons("C", 65), cons("A", 100), cons("G", 100), cons("N", 0)]
m3 = np.array(three)

cw, hh, yl = 0.5, 2.2, 1.1
g5 = S.logo(ax, m5, at=(1.6, yl), col_width=cw, height=hh, alphabet=alphabet, kind="probability", numbers=False,
            title="5′ splice site")
labels5 = ["−2", "−1", "+1", "+2", "+3", "+4", "+5", "+6"]
for i, t in enumerate(labels5):
    bio.label(ax, (g5["x"](i), yl - 0.22), t, size="tiny", color=P.muted())
xb = 1.6 + 2 * cw
ax.plot([xb, xb], [yl - 0.05, yl + hh + 0.05], color=P.ink(), lw=0.9, ls=(0, (2, 1.5)))
bio.label(ax, (2.6, yl - 0.65), "exon | intron", size="tiny", color=P.muted())

gb = S.logo(ax, mb, at=(8.0, yl), col_width=cw, height=hh, alphabet=alphabet, kind="probability", numbers=False,
            title="Branch site", axis=True)
for i in range(7):
    bio.label(ax, (gb["x"](i), yl - 0.22), "A" if i == 5 else "·", size="tiny",
              color=P.edge("negative") if i == 5 else P.muted())
bio.label(ax, (gb["x"](5), yl - 0.6), "branch nucleotide", size="tiny", color=P.edge("negative"))

g3 = S.logo(ax, m3, at=(14.4, yl), col_width=cw, height=hh, alphabet=alphabet, kind="probability", numbers=False,
            title="3′ splice site")
for i, t in [(0, "−12"), (4, "−8"), (8, "−4"), (10, "−2"), (11, "−1"), (12, "+1")]:
    bio.label(ax, (g3["x"](i), yl - 0.22), t, size="tiny", color=P.muted())
xb = 14.4 + 12 * cw
ax.plot([xb, xb], [yl - 0.05, yl + hh + 0.05], color=P.ink(), lw=0.9, ls=(0, (2, 1.5)))
bio.label(ax, (14.4 + 4 * cw, yl - 0.65), "polypyrimidine tract", size="tiny", color=P.muted())
bio.label(ax, (xb + 0.1, yl - 0.65), "intron | exon", size="tiny", color=P.muted())
