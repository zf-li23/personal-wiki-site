# Two coordinate systems on one reference sequence. Top: one-based positions are written on the bases, zero-based
# positions on the fence posts between them; the highlighted 4-base interval is [3, 7) in zero-based half-open
# coordinates (BED, BAM, Python slices) and 4-7 in one-based closed coordinates (GFF, SAM text, VCF, HGVS).
# Bottom: three variants and their VCF records. The deletion and the insertion are anchored on the preceding
# base so that REF and ALT are both non-empty; in half-open coordinates the deleted bases are [8, 10) and the
# insertion point is the empty interval [6, 6).
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import sequence as S

P = bio.P
ref = "ACGTTGCAGCTA"
fig, ax = bio.canvas(25.0, 11.6)
cw, ch = 1.0, 0.8
x0 = 6.0
NUC = P.NUCLEOTIDE


def base(x, y, c, hi=False, edge=None):
    col = S.soft(NUC.get(c, P.fill("neutral")), 0.55 if not hi else 0.2)
    ax.add_patch(Rectangle((x, y), cw, ch, facecolor=col, edgecolor=edge or P.edge("neutral"), lw=1.4 if edge else 0.5,
                           zorder=4))
    bio.label(ax, (x + cw / 2, y + ch / 2), c, size="normal", color=P.on_fill(), zorder=6)


# --- top: the reference with both numberings
y = 9.4
for i, c in enumerate(ref):
    base(x0 + i * cw, y, c, hi=3 <= i < 7, edge=P.edge("highlight") if 3 <= i < 7 else None)
    bio.label(ax, (x0 + (i + 0.5) * cw, y + ch + 0.35), str(i + 1), size="small", color=P.edge("dna"))
for i in range(len(ref) + 1):
    xx = x0 + i * cw
    ax.plot([xx, xx], [y - 0.05, y - 0.35], color=P.edge("rna"), lw=1.0)
    bio.label(ax, (xx, y - 0.6), str(i), size="small", color=P.edge("rna"))
bio.label(ax, (x0 - 0.4, y + ch + 0.35), "one-based (on bases)", size="small", ha="right", color=P.edge("dna"))
bio.label(ax, (x0 - 0.4, y - 0.6), "zero-based (between bases)", size="small", ha="right", color=P.edge("rna"))
xa, xb = x0 + 3 * cw, x0 + 7 * cw
ax.annotate("", xy=(xa, y - 1.15), xytext=(xb, y - 1.15), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.9))
bio.label(ax, ((xa + xb) / 2, y - 1.5), "BED: start 3, end 7   (length 7 - 3 = 4)", size="small")
bio.label(ax, ((xa + xb) / 2, y + ch + 0.95), "GFF / VCF: 4-7   (length 7 - 4 + 1 = 4)", size="small")
bio.label(ax, (x0 + len(ref) * cw + 0.5, y + ch / 2), "reference", size="small", ha="left", color=P.muted())

# --- bottom: three variants
rows = [
    ("substitution", "POS=5  REF=T  ALT=C", {4: "C"}, [], None),
    ("deletion", "POS=8  REF=AGC  ALT=A", {}, [8, 9], 7),
    ("insertion", "POS=6  REF=G  ALT=GTT", {}, [], 5),
]
yb = 6.2
for r, (name, rec, sub, dele, anchor) in enumerate(rows):
    yy = yb - r * 1.9
    bio.label(ax, (x0 - 0.4, yy + ch / 2), name, size="normal", ha="right", bold=True)
    k = 0
    xx = x0
    for i, c in enumerate(ref):
        if i in dele:
            ax.plot([xx + 0.1, xx + cw - 0.1], [yy + ch / 2, yy + ch / 2], color=P.edge("negative"), lw=2.0, zorder=5)
            xx += cw
            continue
        cc = sub.get(i, c)
        base(xx, yy, cc, edge=P.edge("negative") if i in sub else (P.ink() if i == anchor else None))
        xx += cw
        if name == "insertion" and i == anchor:
            for ins in "TT":
                base(xx - cw * 0.0, yy - 0.0, ins, edge=P.edge("positive"))
                xx += cw
    bio.label(ax, (x0 + 15.5 * cw, yy + ch / 2), rec, size="small", ha="left")
bio.label(ax, (x0 + 15.5 * cw, yb + ch + 0.55), "VCF record", size="small", ha="left", bold=True)
bio.label(ax, (x0 + 6 * cw, 1.0), "black outline: anchor (padding) base;  red: changed or deleted;  green: inserted",
          size="tiny", color=P.muted())
