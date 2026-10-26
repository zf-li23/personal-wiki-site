# Initiation of translation.
# A: bacteria. The 30S subunit binds the ribosome-binding site directly: the Shine-Dalgarno sequence (AGGAGG,
#    centred about 7-8 nt upstream of the start codon) pairs with the anti-SD sequence near the 3' end of 16S rRNA;
#    IF3 holds the subunits apart and checks the start codon, IF1 blocks the A site, IF2-GTP brings
#    fMet-tRNAfMet into the P site. Joining of 50S triggers GTP hydrolysis by IF2 and release of the factors.
#    Several start sites can lie on one polycistronic mRNA.
# B: eukaryotes. eIF4F (cap-binding eIF4E, scaffold eIF4G, helicase eIF4A) binds the 5' cap; eIF4G also binds
#    PABP on the poly(A) tail (closed loop) and eIF3 on the 43S complex (40S + eIF1, eIF1A, eIF3, eIF5 and the
#    ternary complex eIF2-GTP-Met-tRNAi). The 43S complex scans 5'->3' and stops at the first AUG in a good
#    context (Kozak: gccRccAUGG, R = A/G at -3 and G at +4); eIF5 triggers GTP hydrolysis by eIF2, and eIF5B-GTP
#    joins the 60S subunit.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(25.0, 10.0)
dx = 0.3

# ---- A: bacteria ----
bio.panel(ax, "A", (0.1, 9.8))
bio.label(ax, (5.8, 9.5), "Bacteria: base pairing with 16S rRNA", size="small", bold=True)
y = 5.2
seq = "UAAGGAGGUAACAUAUGGCUAGC"
x0 = 1.2
xs = MB.codons(ax, x0, y, seq, dx=dx)
ax.plot([x0 - 0.5, xs[-1] + 0.6], [y - 0.2, y - 0.2], color=P.edge("mrna"), lw=1.6, zorder=10)
bio.label(ax, (x0 - 0.75, y - 0.2), "5′", size="tiny", bold=True)
bio.label(ax, (xs[-1] + 0.85, y - 0.2), "3′", size="tiny", bold=True)
# 30S subunit below the mRNA
small = bio.core.smooth_closed(np.array([(-0.5, 0.0), (-0.45, -0.7), (-0.15, -1.0), (0.2, -1.0), (0.48, -0.65), (0.5, 0.0)]) * [6.6, 2.6] + [xs[13], y - 0.35])
ax.add_patch(bio.core.PathPatch(bio.core.Path(small, closed=True), facecolor=P.light("rrna"), edgecolor=P.edge("rrna"), lw=1.0, zorder=4))
bio.label(ax, (xs[13] + 1.0, y - 2.65), "30S subunit", size="small", color=P.on_fill())
# anti-SD of 16S rRNA, written 3'->5' under the SD
anti = "AUUCCUCC"  # 3' end of 16S rRNA, read 3'->5' left to right
ax0 = xs[0]
for i, b in enumerate(anti):
    bio.box(ax, (ax0 + i * dx, y - 0.95), dx * 0.88, 0.34, token="rrna", radius=0.04, zorder=11)
    bio.label(ax, (ax0 + i * dx, y - 0.95), b, size="tiny", bold=True, color=P.on_fill(), zorder=12)
for i in range(0, 8):
    ax.plot([ax0 + i * dx] * 2, [y - 0.38, y - 0.76], color=P.muted(), lw=0.8, zorder=11)
bio.label(ax, (ax0 - 0.55, y - 0.95), "3′", size="tiny", bold=True)
bio.label(ax, (ax0 + 2.8, y - 1.45), "16S rRNA (anti-SD)", size="tiny", color=P.on_fill())
ax.plot([xs[2] - 0.13, xs[7] + 0.13], [y + 0.32, y + 0.32], color=P.edge("highlight"), lw=2)
bio.label(ax, ((xs[2] + xs[7]) / 2, y + 0.62), "Shine–Dalgarno", size="tiny")
ax.plot([xs[14] - 0.13, xs[16] + 0.13], [y - 0.42, y - 0.42], color=P.edge("negative"), lw=2, zorder=12)
bio.label(ax, (xs[15], y - 0.7), "start", size="tiny", color=P.on_fill())
bio.label(ax, ((xs[8] + xs[13]) / 2, y + 0.62), "spacer 5–9 nt", size="tiny", color=P.muted())
# initiator tRNA on AUG (anticodon 3'-UAC-5') with fMet
end = MB.trna(ax, (xs[15], y + 0.36), "UAC", aa="Met", dx=dx, height=2.0)
bio.label(ax, (end[0] + 0.75, end[1] + 0.45), "fMet", size="tiny", bold=True)
bio.protein(ax, (xs[15] - 1.05, y + 1.5), 0.9, 0.75, "enzyme", text="IF2")
bio.label(ax, (xs[15] - 1.05, y + 0.95), "GTP", size="tiny", color=P.muted())
bio.protein(ax, (xs[19], y + 0.85), 0.75, 0.75, "positive", text="IF1")
bio.label(ax, (xs[19], y + 1.45), "A site", size="tiny", color=P.muted())
bio.protein(ax, (xs[20], y - 1.3), 0.8, 0.7, "receptor", text="IF3")
bio.label(ax, (5.8, 1.0), "50S joins → IF2 hydrolyses GTP → factors leave → 70S initiation complex", size="tiny", color=P.muted())
bio.label(ax, (5.8, 0.5), "fMet-tRNAfMet is the only aminoacyl-tRNA that enters the P site directly", size="tiny", color=P.muted())

# ---- B: eukaryotes ----
bio.panel(ax, "B", (12.6, 9.8))
bio.label(ax, (18.8, 9.5), "Eukaryotes: cap binding, closed loop and scanning", size="small", bold=True)
yb = 5.2
xa, xb = 13.6, 24.2
t = np.linspace(xa, xb, 200)
ax.plot(t, yb - 0.2 + 0 * t, color=P.edge("mrna"), lw=1.6, zorder=10)
# closed loop: the 3' end with poly(A) arching back to the cap
loop = np.array([(xb, yb - 0.2), (xb + 0.5, yb - 1.8), (xb - 2.0, yb - 3.0), (xa + 2.5, yb - 3.05), (xa - 0.2, yb - 2.5)])
from scipy.interpolate import CubicSpline
lp = CubicSpline(np.arange(len(loop)), loop)(np.linspace(0, len(loop) - 1, 200))
ax.plot(lp[:, 0], lp[:, 1], color=P.edge("mrna"), lw=1.6, ls=(0, (3, 2)), zorder=9)
bio.label(ax, (xa + 4.6, yb - 2.7), "poly(A) tail (AAAA…)", size="tiny", color=P.muted())
ax.add_patch(bio.core.Circle((xa, yb - 0.2), 0.16, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), zorder=12))
bio.label(ax, (xa - 0.1, yb + 0.25), "m⁷G cap", size="tiny")
bio.protein(ax, (xa + 0.5, yb - 0.85), 0.8, 0.6, "enzyme", text="4E")
bio.protein(ax, (xa + 1.6, yb - 1.25), 1.6, 0.7, "receptor", text="eIF4G")
bio.protein(ax, (xa + 1.35, yb + 0.55), 0.8, 0.6, "positive", text="4A")
bio.protein(ax, (xa + 0.7, yb - 2.55), 1.0, 0.6, "metabolite", text="PABP")
bio.arrow(ax, (xa + 1.2, yb - 1.6), (xa + 0.85, yb - 2.2), kind="link")
# 43S complex scanning
c43 = xa + 4.0
small = bio.core.smooth_closed(np.array([(-0.5, 0.0), (-0.45, -0.7), (-0.15, -1.0), (0.2, -1.0), (0.48, -0.65), (0.5, 0.0)]) * [3.4, 1.9] + [c43, yb - 0.35])
ax.add_patch(bio.core.PathPatch(bio.core.Path(small, closed=True), facecolor=P.light("rrna"), edgecolor=P.edge("rrna"), lw=1.0, zorder=4))
bio.label(ax, (c43 + 0.2, yb - 1.5), "40S", size="small", color=P.on_fill())
bio.protein(ax, (c43 - 1.0, yb + 0.8), 1.0, 0.7, "antibody", text="eIF3")
bio.protein(ax, (c43 + 1.15, yb + 0.55), 0.7, 0.5, "neutral", text="1A")
bio.protein(ax, (c43 + 0.2, yb + 2.3), 1.0, 0.7, "enzyme", text="eIF2")
bio.label(ax, (c43 + 0.2, yb + 2.95), "GTP · Met-tRNAi", size="tiny", color=P.muted())
MB.trna(ax, (c43 + 0.2, yb + 0.36), "UAC", dx=dx, height=1.5, charged=False, zorder=13)
bio.arrow(ax, (c43 + 1.8, yb + 1.25), (c43 + 3.8, yb + 1.25), kind="process")
bio.label(ax, (c43 + 2.8, yb + 1.6), "scanning (ATP)", size="tiny")
# Kozak context
kz = "GCCACCAUGG"
kx = xa + 7.0
xk = MB.codons(ax, kx, yb, kz, dx=dx)
ax.plot([xk[6] - 0.13, xk[8] + 0.13], [yb - 0.42, yb - 0.42], color=P.edge("negative"), lw=2, zorder=12)
bio.label(ax, (xk[3], yb + 0.55), "−3", size="tiny", bold=True)
bio.label(ax, (xk[9], yb + 0.55), "+4", size="tiny", bold=True)
bio.label(ax, (xk[5], yb - 0.75), "Kozak context: gccRccAUGG", size="tiny")
bio.label(ax, (18.8, 1.0), "start codon recognized → eIF5: GTP hydrolysis by eIF2, factors leave", size="tiny", color=P.muted())
bio.label(ax, (18.8, 0.5), "eIF5B · GTP joins 60S → 80S initiation complex", size="tiny", color=P.muted())
