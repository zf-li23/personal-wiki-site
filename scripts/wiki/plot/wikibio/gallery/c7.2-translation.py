# Translation elongation at the ribosome. The mRNA runs 5'->3' between the subunits; the three tRNA sites
# lie in the order E, P, A from 5' to 3'. Shown just before peptide-bond formation: the P site holds
# tRNA-Phe carrying the peptide Met-Ala-Phe, the A site the incoming Gly-tRNA (codon GGU, anticodon 3'-CCA-5'),
# the E site the deacylated tRNA-Ala on its way out. Anticodons are written 3'->5' so that each base sits on
# its partner in the codon. The peptide leaves through the exit tunnel of the large subunit, N-terminus first.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

fig, ax = bio.canvas(17, 10.6)
P = bio.P

dx = 0.42
y = 3.0
cx = 8.9
utr = "ACAGCC"
cds = "AUGGCAUUCGGUAAAGACUGGCUG"
seq = utr + cds
p_mid = len(utr) + 7          # middle base of codon 3 (UUC) sits in the P site
x0 = cx - p_mid * dx
rib = MB.ribosome(ax, (cx, y), width=3 * dx * 5, height=4.7)

# exit tunnel through the large subunit
tx = rib["sites"]["P"] - 0.55
tunnel = np.array([(tx - 0.24, y + 3.3), (tx - 0.36, rib["top"] - 0.02), (tx + 0.36, rib["top"] - 0.02), (tx + 0.24, y + 3.3)])
ax.add_patch(bio.core.Polygon(tunnel, closed=True, facecolor=P.light("rrna"), edgecolor=P.edge("rrna"), lw=0.8, ls=(0, (2.5, 1.5)),
                              zorder=4.5))

# mRNA: backbone, cap and coloured bases
xs = x0 + np.arange(len(seq)) * dx
ax.plot([xs[0] - 0.3, xs[-1] + 0.5], [y - 0.22, y - 0.22], color=P.edge("mrna"), lw=bio.core.LINE * 2.0, zorder=10,
        solid_capstyle="round")
MB.codons(ax, x0, y, seq, dx=dx, zorder=11)
ax.add_patch(bio.core.Circle((xs[0] - 0.42, y - 0.22), 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=11))
bio.label(ax, (xs[0] - 0.42, y - 0.62), "5′ cap", size="tiny")
bio.label(ax, (xs[-1] + 0.8, y - 0.22), "3′", size="tiny", bold=True)
# codon brackets below the ribosome-bound codons
for k in range(len(cds) // 3):
    a, b = xs[len(utr) + 3 * k] - dx * 0.45, xs[len(utr) + 3 * k + 2] + dx * 0.45
    yy = y - 0.52 if k not in (1, 2, 3) else rib["bottom"] - 0.25
    if k in (1, 2, 3):
        continue
    ax.plot([a, a, b, b], [yy + 0.08, yy, yy, yy + 0.08], color=P.muted(), lw=0.7, zorder=11)

# tRNAs: E (deacylated), P (peptidyl), A (aminoacyl)
yt = y + 0.42
MB.trna(ax, (rib["sites"]["E"], yt), "CGU", dx=dx, height=2.85, charged=False)
end_p = MB.trna(ax, (rib["sites"]["P"], yt), "AAG", dx=dx, height=2.85, charged=False)
MB.trna(ax, (rib["sites"]["A"], yt), "CCA", dx=dx, height=2.85, aa="Gly")
pep = MB.peptide(ax, [(tx - 0.5, rib["top"] + 0.75), (tx, rib["top"] - 0.3), (tx + 0.05, y + 3.55), end_p + (0.0, 0.25)],
                 ["Met", "Ala", "Phe"])
bio.label(ax, (pep[0][0] - 0.3, pep[0][1] + 0.05), "N", size="small", bold=True, ha="right")

# site letters and labels
for s, xx in rib["sites"].items():
    bio.label(ax, (xx, y - 0.62), s, size="normal", bold=True, color=P.on_fill())
bio.label(ax, (rib["sites"]["E"] - 2.25, y + 3.2), "Large subunit", size="small", ha="right")
bio.label(ax, (rib["sites"]["E"] - 1.9, rib["bottom"] + 0.25), "Small subunit", size="small", ha="right")
bio.callout(ax, (rib["sites"]["P"] + 0.62, y + 3.55), (13.6, 7.4), "Peptidyl transferase centre")
bio.callout(ax, (tx + 0.3, rib["top"] - 0.45), (12.9, 8.6), "Exit tunnel")
bio.callout(ax, (rib["sites"]["A"] + 0.62, y + 0.42), (13.6, 4.7), "Anticodon (3′→5′)")
bio.callout(ax, (xs[len(utr) + 3 * 4 + 1], y - 0.2), (14.4, 1.7), "Codon (5′→3′)")
bio.label(ax, (cx, rib["bottom"] - 0.35), "E: exit   P: peptidyl-tRNA   A: aminoacyl-tRNA", size="small", va="top")
bio.label(ax, (xs[len(utr)] - 0.3, y - 0.52), "Start", size="tiny", color=P.muted(), ha="right")

# direction of movement
bio.arrow(ax, (cx - 2.0, 0.45), (cx + 2.0, 0.45), kind="process")
bio.label(ax, (cx + 2.3, 0.45),  "Ribosome moves 5′ → 3′,\none codon per cycle", size="small", ha="left")

# legend of amino-acid classes
lx, ly = 0.6, 9.6
bio.label(ax, (lx, ly), "Amino acids", size="small", bold=True, ha="left")
for k, (cls, tok) in enumerate(MB.AA_TOKEN.items()):
    yy = ly - 0.5 - k * 0.45
    ax.add_patch(bio.core.Circle((lx + 0.15, yy), 0.13, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (lx + 0.4, yy), cls, size="tiny", ha="left")
