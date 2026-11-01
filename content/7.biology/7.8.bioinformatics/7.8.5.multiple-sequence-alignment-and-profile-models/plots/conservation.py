# Conservation of the 40 alignment columns around the Walker A motif of the MCM family (the alignment of the
# guide-tree figure: 15 sequences, MCM2-7 of human, MCM6 of eight eukaryotes and the archaeal MCM).
# A: sequence logo; stack height is the information content log2(20) - H (bits, with the small-sample
# correction), letters scaled by their frequency. B: Shannon entropy H of each column (low = conserved).
# C: Jensen-Shannon divergence between the column distribution (pseudocount 0.1 per residue) and the
# background frequencies of Robinson and Robinson (high = conserved and unusual). Columns 11-13 (GDP), 17 (K)
# and 18 (S) of the Walker A motif are invariant (stars); column 14 separates MCM6 (S) from the other
# paralogs (G).
import numpy as np
import wikibio as bio
from wikibio import sequence as seqmod
from wikibio import charts as C

P = bio.P
ALN = {
    "MCM6_HUMAN": "LRGDINVCIVGDPSTAKSQFLKHVEEFSPRAVYTSGKASS", "MCM6_MOUSE": "LRGDINVCIVGDPSTAKSQFLKHVDEFSPRAVYTSGKASS",
    "MCM6_DROME": "LRGDINVCIVGDPSTAKSQFLKQVSDFSPRAIYTSGKASS", "MCM6_ANOGA": "LRGDINVCIVGDPSTAKSQFLKQVSDFSPRAVYTSGKASS",
    "MCM6_ARATH": "LRGDINVCIVGDPSCAKSQFLKYTAGIVPRSVYTSGKSSS", "MCM6_ORYSI": "LRGDINVCIVGDPSCAKSQFLKYTAGIVPRSVYTSGKSSS",
    "MCM6_DICDI": "LRGDINVCIVGDPSTSKSTFLKYLVSFLPRTVYTSGKASS", "MCM6_SCHPO": "LRGDLNICIVGDPSTSKSQFLKYVCNFLPRAIYTSGKASS",
    "MCM6_YEAST": "LRGDINICVVGDPSTSKSQFLKYVVGFAPRSVYTSGKASS", "MCM2_HUMAN": "VRGDINVLLCGDPGTAKSQFLKYIEKVSSRAIFTTGQGAS",
    "MCM3_HUMAN": "IRGDINILLIGDPSVAKSQLLRYVLCTAPRAIPTTGRGSS", "MCM4_HUMAN": "FRAEINILLCGDPGTSKSQLLQYVYNLVPRGQYTSGKGSS",
    "MCM5_HUMAN": "RRGDINLLMLGDPGTAKSQLLKFVEKCSPIGVYTSGKGSS", "MCM7_HUMAN": "IRGNINICLMGDPGVAKSQLLSYIDRLAPRSQYTTGRGSS",
    "MCM_SACS2": "IRGDIHILIIGDPGTAKSQMLQFISRVAPRAVYTTGKGST"}
AA = "ACDEFGHIKLMNPQRSTVWY"
rob = dict(A=0.07805, R=0.05129, N=0.04487, D=0.05364, C=0.01925, Q=0.04264, E=0.06295, G=0.07377, H=0.02199,
           I=0.05142, L=0.09019, K=0.05744, M=0.02243, F=0.03856, P=0.05203, S=0.07120, T=0.05841, W=0.01330,
           Y=0.03216, V=0.06441)
q = np.array([rob[a] for a in AA])
q = q / q.sum()
seqs = list(ALN.values())
Lc = len(seqs[0])
cnt = np.array([[sum(s[j] == a for s in seqs) for a in AA] for j in range(Lc)], float)
p = cnt / cnt.sum(axis=1, keepdims=True)
with np.errstate(divide="ignore", invalid="ignore"):
    H = -np.nansum(np.where(p > 0, p * np.log2(p), 0), axis=1)
ps = (cnt + 0.1) / (cnt.sum(axis=1, keepdims=True) + 2)
m = (ps + q) / 2
JS = 0.5 * (ps * np.log2(ps / m)).sum(axis=1) + 0.5 * (q * np.log2(q / m)).sum(axis=1)
fig, ax = bio.canvas(24.0, 12.0)
cw = 0.5
x0 = 2.4
seqmod.logo(ax, cnt, at=(x0, 6.6), col_width=cw, height=4.0, alphabet=AA, start=1)
bio.label(ax, (x0 + Lc * cw / 2, 11.4), "MCM family, 15 sequences", size="small", bold=True)
b = C.axes_at(ax, (x0, 3.5, Lc * cw, 2.0))
b.bar(np.arange(Lc), H, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, width=0.8)
b.set_xlim(-0.5, Lc - 0.5)
b.set_xticks([])
C.style_axes(b, None, "entropy (bits)")
c = C.axes_at(ax, (x0, 0.7, Lc * cw, 2.0))
c.bar(np.arange(Lc), JS, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.5, width=0.8)
c.set_xlim(-0.5, Lc - 0.5)
c.set_xticks(np.arange(0, Lc, 5), [str(i + 1) for i in range(0, Lc, 5)])
C.style_axes(c, "alignment column", "JS divergence")
for i in (10, 11, 12, 16, 17):
    b.text(i, H[i] + 0.1, "*", ha="center", fontsize=bio.core.FONT["tiny"], color=C.line("negative"))
bio.panel(ax, "A", (0.2, 11.6))
bio.panel(ax, "B", (0.2, 5.7))
bio.panel(ax, "C", (0.2, 2.9))
