# The elongation cycle of the ribosome (bacterial names; eukaryotic eEF1A and eEF2 act in the same way).
# 1: decoding. The ternary complex EF-Tu-GTP-Gly-tRNA samples the A site; codon-anticodon pairing (GGU with
#    anticodon 3'-CCA-5') is monitored by the decoding centre of 16S rRNA, which triggers GTP hydrolysis.
# 2: accommodation and peptidyl transfer. EF-Tu-GDP leaves, the aminoacyl end swings into the peptidyl
#    transferase centre of the large subunit, and the alpha-amino group of Gly attacks the ester of the
#    peptidyl-tRNA: the peptide (Met-Ala-Phe) is transferred to the A-site tRNA, the P-site tRNA is deacylated.
# 3: hybrid states. The acceptor ends move to the P and E sites of the large subunit (A/P and P/E states) while
#    the anticodons stay; EF-G-GTP binds and, by GTP hydrolysis, drives translocation.
# 4: post-translocation. mRNA and tRNAs have moved by one codon (3 nt): the peptidyl-tRNA is in the P site,
#    the deacylated tRNA in the E site, from which it leaves, and the A site is free for the next codon (AAA).
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(25.0, 9.4)
dx = 0.27
y = 3.4
H = 1.75
seq = "GCAUUCGGUAAAGAC"


def scene(cx, shift, trnas, title, factor=None):
    rib = MB.ribosome(ax, (cx, y), width=15 * dx, height=3.4)
    s = rib["sites"]
    x0 = s["P"] - 4 * dx - shift * 3 * dx
    xs = MB.codons(ax, x0, y, seq, dx=dx)
    ax.plot([xs[0] - 0.2, xs[-1] + 0.2], [y - 0.2, y - 0.2], color=P.edge("mrna"), lw=1.6, zorder=10)
    bio.label(ax, (xs[0] - 0.45, y - 0.2), "5′", size="tiny", bold=True)
    bio.label(ax, (xs[-1] + 0.45, y - 0.2), "3′", size="tiny", bold=True)
    ends = {}
    for site, (ac, aa, charged) in trnas.items():
        ends[site] = MB.trna(ax, (s[site], y + 0.36), ac, aa=aa, dx=dx, height=H, charged=charged)
    for site, xx in s.items():
        bio.label(ax, (xx, rib["bottom"] + 0.28), site, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (cx, 8.85), title, size="small", bold=True)
    return rib, ends


# 1 decoding
rib, e = scene(3.0, 0, {"P": ("AAG", None, False), "A": ("CCA", "Gly", True)}, "1  Decoding")
MB.peptide(ax, [e["P"] + (0.0, 0.3), e["P"] + (-0.35, 1.25), e["P"] + (-0.9, 2.0)], ["Phe", "Ala", "Met"][::1])
bio.protein(ax, (rib["sites"]["A"] + 0.75, y + 2.4), 0.95, 0.7, "enzyme", text="EF-Tu")
bio.label(ax, (rib["sites"]["A"] + 0.75, y + 1.75), "GTP", size="tiny", color=P.muted())
bio.label(ax, (3.0, 1.55), "codon–anticodon check by 16S rRNA", size="tiny", color=P.muted())

# 2 peptidyl transfer
rib, e = scene(9.3, 0, {"P": ("AAG", None, False), "A": ("CCA", None, False)}, "2  Peptidyl transfer")
MB.peptide(ax, [e["A"] + (0.0, 0.3), e["A"] + (-0.3, 1.05), e["A"] + (-0.8, 1.75), e["A"] + (-1.3, 2.35)],
           ["Gly", "Phe", "Ala", "Met"])
bio.label(ax, (9.3, 1.55), "catalysed by 23S rRNA (PTC)", size="tiny", color=P.muted())

# 3 hybrid states + EF-G
rib, e = scene(15.6, 0, {"P": ("AAG", None, False), "A": ("CCA", None, False)}, "3  Hybrid states, EF-G")
MB.peptide(ax, [e["A"] + (0.0, 0.3), e["A"] + (-0.3, 1.05), e["A"] + (-0.8, 1.75), e["A"] + (-1.3, 2.35)],
           ["Gly", "Phe", "Ala", "Met"])
bio.protein(ax, (rib["sites"]["A"] + 0.95, y + 1.3), 0.9, 1.1, "receptor", text="EF-G")
bio.label(ax, (rib["sites"]["A"] + 0.95, y + 0.45), "GTP", size="tiny", color=P.muted())
bio.label(ax, (15.6, 1.55), "A/P and P/E states", size="tiny", color=P.muted())

# 4 post-translocation
rib, e = scene(21.9, 1, {"E": ("AAG", None, False), "P": ("CCA", None, False)}, "4  Translocated by 3 nt")
MB.peptide(ax, [e["P"] + (0.0, 0.3), e["P"] + (-0.3, 1.05), e["P"] + (-0.8, 1.75), e["P"] + (-1.3, 2.35)],
           ["Gly", "Phe", "Ala", "Met"])
bio.arrow(ax, (rib["sites"]["E"] - 0.3, y + 2.4), (rib["sites"]["E"] - 1.3, y + 3.0), kind="process", dashed=True)
bio.label(ax, (rib["sites"]["E"] - 1.3, y + 3.3), "tRNA leaves", size="tiny", color=P.muted())
bio.label(ax, (21.9, 1.55), "A site free for AAA (Lys)", size="tiny", color=P.muted())

for a in (5.5, 11.8, 18.1):
    bio.arrow(ax, (a + 0.2, 5.3), (a + 1.3, 5.3), kind="process")
bio.label(ax, (6.25, 5.75), "GTP → GDP", size="tiny", color=P.muted())
bio.label(ax, (6.25, 4.85), "EF-Tu leaves", size="tiny", color=P.muted())
bio.label(ax, (18.85, 5.75), "GTP → GDP", size="tiny", color=P.muted())
bio.label(ax, (18.85, 4.85), "EF-G leaves", size="tiny", color=P.muted())
bio.arrow(ax, (21.9, 0.95), (3.0, 0.95), kind="process", dashed=True)
bio.label(ax, (12.45, 0.55), r"next cycle: about 50 ms per codon in $\it{E.\ coli}$", size="tiny", color=P.muted())
