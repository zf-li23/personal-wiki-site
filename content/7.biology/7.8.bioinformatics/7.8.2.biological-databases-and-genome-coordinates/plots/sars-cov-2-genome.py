# The SARS-CoV-2 reference genome NC_045512.2 drawn from its RefSeq feature table (one-based coordinates):
# 5' UTR 1-265, ORF1ab 266-21555 (ORF1a ends at 13483; the -1 ribosomal frameshift site is near 13468),
# S 21563-25384, ORF3a 25393-26220, E 26245-26472, M 26523-27191, ORF6 27202-27387, ORF7a 27394-27759,
# ORF7b 27756-27887, ORF8 27894-28259, N 28274-29533, ORF10 29558-29674, 3' UTR 29675-29903.
# The D614G substitution A23403G in S is marked.
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import sequence as S

P = bio.P
L = 29903
fig, ax = bio.canvas(30.0, 8.0)
gb = S.Browser(ax, (1, L), 2.0, 29.0, chrom="NC_045512.2")
gb.axis(6.6, step=5000, label_text=False)
bio.label(ax, (2.0, 7.6), "NC_045512.2  (29,903 nt, positive-sense RNA genome)", size="small", ha="left")
y = 4.6
ax.plot([gb.x(1), gb.x(L)], [y, y], color=P.edge("rna"), lw=1.2, zorder=2)
genes = [("ORF1a", 266, 13483, "rna"), ("ORF1b", 13468, 21555, "rna"), ("S", 21563, 25384, "highlight"),
         ("ORF3a", 25393, 26220, "protein"), ("E", 26245, 26472, "protein"), ("M", 26523, 27191, "protein"),
         ("ORF6", 27202, 27387, "protein"), ("ORF7a", 27394, 27759, "protein"), ("ORF7b", 27756, 27887, "protein"),
         ("ORF8", 27894, 28259, "protein"), ("N", 28274, 29533, "protein"), ("ORF10", 29558, 29674, "protein")]
small = {"E": 0, "ORF6": 1, "ORF7a": 2, "ORF7b": 3, "ORF8": 4, "ORF10": 5}
for name, a, b, tok in genes:
    yy = y + (0.25 if name == "ORF1b" else 0.0)
    h = 0.7
    if name == "ORF1a":
        yy = y - 0.25
    ax.add_patch(Rectangle((gb.x(a - 0.5), yy - h / 2), gb.x(b + 0.5) - gb.x(a - 0.5), h, facecolor=P.fill(tok),
                           edgecolor=P.edge(tok), lw=0.7, zorder=5))
    xc = (gb.x(a) + gb.x(b)) / 2
    if name in small:
        k = small[name]
        bio.callout(ax, (xc, yy - h / 2), (xc + 0.5, 3.4 - 0.45 * k), name, size="tiny")
    else:
        bio.label(ax, (xc, yy), name, size="small", color=P.on_fill(), zorder=7)
bio.label(ax, (gb.x(133), 3.5), "5' UTR", size="tiny", color=P.muted())
bio.label(ax, (gb.x(29700) + 0.2, 5.2), "3' UTR", size="tiny", color=P.muted())
bio.callout(ax, (gb.x(13468), y + 0.6), (gb.x(13468) - 1.5, y + 1.5), "-1 frameshift (pp1ab)", size="tiny")
xm = gb.x(23403)
ax.plot([xm, xm], [y + 0.4, y + 1.3], color=P.edge("negative"), lw=1.4, zorder=8)
bio.label(ax, (xm, y + 1.55), "A23403G (D614G)", size="tiny", color=P.edge("negative"))
bio.label(ax, ((gb.x(266) + gb.x(21555)) / 2, 3.2), "replicase polyproteins pp1a / pp1ab", size="tiny", color=P.muted())
bio.label(ax, (gb.x(26800), 0.4), "accessory and structural genes", size="tiny", color=P.muted())
