# Three generations of programmable targeting, and the consequence for libraries.
# A: ZFN pair - 4 fingers per arm, 3 bp per finger, FokI dimerizing across a 5-7 bp spacer.
# B: TALEN pair - one repeat per base pair, base set by the repeat-variable diresidue (RVD), 5' T required.
# C: Cas9 - one protein, 20 nt of guide RNA, NGG PAM, blunt cut 3 bp from the PAM.
# D: the RVD cipher as a matrix of repeat against base read.
# E: synthetic DNA per target: about 3 kb for a TALEN pair against 20 nt for a guide RNA.
import numpy as np
import wikibio as bio
from matplotlib.patches import Rectangle
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 17.4)

BP = 0.30          # one base pair, in canvas units
NEG = P.edge("negative")
X0 = 2.8           # left end of every duplex


def duplex(n, y, token="dna", token2="dna2"):
    """A duplex of n base pairs starting at X0; the top strand is at y, the bottom at y - 0.34."""
    x1 = X0 + n * BP
    for yy, tok in ((y, token), (y - 0.34, token2)):
        ax.plot([X0, x1], [yy, yy], color=P.edge(tok), lw=2.0, zorder=5, solid_capstyle="butt")
    for i in range(n + 1):
        ax.plot([X0 + i * BP, X0 + i * BP], [y, y - 0.34], color=P.mix(P.muted(), P.surface(), 0.6),
                lw=0.5, zorder=4)
    return x1


def at(bp):
    return X0 + bp * BP


def cut_mark(bp, y, text=None):
    x = at(bp)
    ax.plot([x, x], [y + 0.5, y - 0.84], color=NEG, lw=1.6, zorder=14)
    if text:
        bio.label(ax, (x, y - 1.15), text, size="tiny", color=NEG)


def fok(x, y, label_above=True):
    bio.protein(ax, (x, y), 1.25, 0.66, token="enzyme", text="FokI", size="tiny", zorder=13)


# ----------------------------------------------------------------- A: ZFN
yA = 14.0
bio.panel(ax, "A", (0.1, yA + 2.5))
bio.label(ax, (2.6, yA + 2.5), "Zinc finger nuclease", size="small", bold=True, ha="left")
duplex(34, yA)
for k in range(4):                                   # upper arm: four fingers, 3 bp each
    bio.protein(ax, (at(3 * k + 1.5), yA + 0.62), 3 * BP * 0.9, 0.6, token="receptor",
                text=f"F{k + 1}", size="tiny", wobble=0.04, zorder=11)
fok(at(14.0), yA + 0.62)
for k in range(4):                                   # lower arm, on the other strand
    bio.protein(ax, (at(22 + 3 * k + 1.5), yA - 0.96), 3 * BP * 0.9, 0.6, token="receptor",
                text=f"F{k + 1}", size="tiny", wobble=0.04, zorder=11)
fok(at(19.5), yA - 0.96)
cut_mark(17, yA)
bio.label(ax, (at(24), yA + 1.55), "the FokI domains must dimerize across the spacer to cut",
          size="tiny", color=P.muted())
bio.label(ax, (at(6), yA + 1.55), "3 bp per finger", size="tiny", color=P.muted())
bio.label(ax, (at(14), yA - 1.75), "spacer 5–7 bp; fingers are context-dependent, so arrays must be selected",
          size="tiny", color=P.muted())
bio.label(ax, (14.6, yA - 0.1), "two arms × 12 bp = 24 bp specified", size="tiny", color=P.ink(), ha="left")

# ----------------------------------------------------------------- B: TALEN
yB = 9.2
bio.panel(ax, "B", (0.1, yB + 2.5))
bio.label(ax, (2.6, yB + 2.5), "TALEN", size="small", bold=True, ha="left")
duplex(44, yB)
rvds = ["NG", "NI", "HD", "NN", "NG", "HD", "NI", "NG", "NN", "HD", "NI", "NG"]
for k, rvd in enumerate(rvds):
    bio.box(ax, (at(k + 1.5), yB + 0.75), BP * 0.9, 0.9, token="protein", text=rvd, size="tiny",
            radius=0.04, zorder=11)
    bio.box(ax, (at(30 + k + 0.5), yB - 1.09), BP * 0.9, 0.9, token="protein", text=rvd, size="tiny",
            radius=0.04, zorder=11)
bio.label(ax, (at(0.5), yB + 0.75), "T", size="tiny", bold=True, color=P.edge("dna"))
bio.label(ax, (at(0.5), yB + 1.45), "5′ T", size="tiny", color=P.muted())
fok(at(16.5), yB + 0.75)
fok(at(27.0), yB - 1.09)
cut_mark(22, yB)
bio.label(ax, (at(24), yB + 1.55), "one repeat per base pair; the RVD at positions 12–13 names the base",
          size="tiny", color=P.muted())
bio.label(ax, (at(25.5), yB - 1.55), "spacer 12–20 bp", size="tiny", color=P.muted())
bio.label(ax, (17.0, yB + 0.1), "design trivial, construction laborious:\n$\\approx 2$ kb of near-identical repeats per arm",
          size="tiny", color=P.ink(), ha="left")

# ----------------------------------------------------------------- C: Cas9
yC = 5.4
bio.panel(ax, "C", (0.1, yC + 2.1))
bio.label(ax, (2.6, yC + 2.1), "CRISPR–Cas9", size="small", bold=True, ha="left")
duplex(34, yC)
bio.shape(ax, bio.blob((at(14), yC + 1.55), 2.3, 0.72, wobble=0.05, seed=7), token="enzyme", zorder=6)
bio.label(ax, (at(14), yC + 1.55), "Cas9", size="small", bold=True, color=P.on_fill(), zorder=8)
ax.plot([at(5), at(25)], [yC + 0.22, yC + 0.22], color=P.edge("rna"), lw=2.4, zorder=9)
bio.label(ax, (at(15), yC + 0.62), "20 nt guide : protospacer", size="tiny", color=P.edge("rna"), zorder=10)
bio.box(ax, (at(26.5), yC - 0.17), 2.6 * BP, 0.9, token="highlight", text="NGG", size="tiny", radius=0.05,
        zorder=12)
bio.label(ax, (at(26.5), yC - 0.9), "PAM", size="tiny", color=P.edge("highlight"))
cut_mark(22, yC, "blunt cut, 3 bp from the PAM")
bio.label(ax, (14.0, yC + 1.1), "one protein for every target;\na new target = one oligonucleotide pair",
          size="tiny", color=P.ink(), ha="left")

# ----------------------------------------------------------------- D: the RVD cipher
bio.panel(ax, "D", (0.1, 3.75))
bio.label(ax, (4.6, 3.75), "The TALE cipher: RVD → base", size="small", bold=True)
code = {"NI": "A", "HD": "C", "NG": "T", "NN": "AG", "NH": "G", "N*": "CT"}
bases = ["A", "C", "G", "T"]
cw, ch = 0.85, 0.45
x_left, y_top = 3.2, 2.8
for j, b in enumerate(bases):
    bio.label(ax, (x_left + (j + 0.5) * cw, y_top + 0.35), b, size="tiny", bold=True)
for i, (rvd, reads) in enumerate(code.items()):
    y = y_top - (i + 0.5) * ch
    bio.label(ax, (x_left - 0.25, y), rvd, size="tiny", bold=True, ha="right")
    for j, b in enumerate(bases):
        hit = b in reads
        tok = "positive" if hit else "neutral"
        ax.add_patch(Rectangle((x_left + j * cw + 0.05, y - ch / 2 + 0.04), cw - 0.1, ch - 0.08,
                               facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7,
                               alpha=1.0 if hit else 0.3, zorder=6))
bio.label(ax, (x_left + 4 * cw + 0.45, 1.6), "NN reads A as well,\nwhich is why NH\nis preferred for G",
          size="tiny", color=P.muted(), ha="left")

# ----------------------------------------------------------------- E: cost per target
bio.panel(ax, "E", (10.4, 3.75))
bio.label(ax, (17.0, 3.75), "Synthetic DNA needed per target", size="small", bold=True)
items = [("ZFN pair", 2.2e3, "receptor"), ("TALEN pair", 3.0e3, "protein"), ("sgRNA", 20.0, "rna")]
pl = Q.Plot(ax, (16.0, 1.0, 5.4, 1.5), xlim=(10, 1e4), ylim=(-0.6, 2.6), xlog=True,
            xlabel="nucleotides of DNA synthesis per target",
            xticks=[(10, "10"), (100, "100"), (1e3, "1 kb"), (1e4, "10 kb")], yticks=None)
for i, (name, val, tok) in enumerate(items):
    y = 2 - i
    ax.plot([pl.X(10), pl.X(val)], [pl.Y(y), pl.Y(y)], color=Q.line_color(tok), lw=5.0,
            solid_capstyle="round", zorder=7)
    bio.label(ax, (pl.X(10) - 0.2, pl.Y(y)), name, size="tiny", ha="right")
bio.label(ax, (18.0, 2.85), "the ratio is why libraries of $10^{5}$ guides, and hence pooled screens, exist",
          size="tiny", color=P.muted())
