"""Four pathways switched by protein degradation or proteolysis (SBGN activity flow; open arrows activate,
bars inhibit, dashed arcs are transcriptional feedback from target genes).

A Wnt/beta-catenin: without Wnt, the destruction complex (Axin, APC, GSK3, CK1) phosphorylates
beta-catenin, which beta-TrCP ubiquitylates for the proteasome; Wnt bound to Frizzled and LRP5/6 recruits
Dishevelled and Axin to the membrane and inactivates the complex, so beta-catenin accumulates, enters the
nucleus and converts TCF/LEF from repressor to activator. Axin2 is a target gene (negative feedback).
B Hedgehog: Patched inhibits Smoothened; Hh binding inactivates Patched, Smoothened accumulates in the
primary cilium and blocks the processing of Gli into its repressor form (which needs PKA, GSK3, CK1 and
partial proteasomal processing) and the restraint by SuFu, so full-length Gli activates targets, among
them Ptch1 (negative feedback) and Gli1.
C NF-kB: TNF, IL-1 or LPS activate IKK, which phosphorylates IkB-alpha for beta-TrCP-dependent degradation,
releasing NF-kB (p65-p50) into the nucleus; IkB-alpha and A20 are target genes (negative feedback).
D Notch: a ligand on the neighboring cell binds Notch; ADAM10 cleaves at S2 and gamma-secretase within
the membrane at S3, releasing the Notch intracellular domain (NICD), which with CSL (RBPJ) and Mastermind
activates Hes and Hey genes. No amplification: one receptor yields one NICD.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(22.0, 11.6)
d = network.Diagram(ax, size="small")
Y = [9.9, 8.5, 7.1, 5.7, 4.3, 2.9, 1.5]
W = 4.4


def col(k):
    return 0.35 + k * 5.5 + 2.6


def node(id, k, row, text, tok, dx=0.0, w=W):
    d.activity(id, (col(k) + dx, Y[row]), text, token=tok, w=w)


titles = ["Wnt / β-catenin", "Hedgehog", "NF-κB", "Notch"]
for k, t in enumerate(titles):
    bio.panel(ax, "ABCD"[k], (col(k) - 2.55, 11.45))
    bio.label(ax, (col(k), 11.0), t, size="small", bold=True)

# A Wnt
node("w0", 0, 0, "Wnt", "drug")
node("w1", 0, 1, "Frizzled + LRP5/6", "receptor")
node("w2", 0, 2, "Dishevelled", "protein")
node("w3", 0, 3, "Axin–APC–GSK3–CK1 complex", "negative")
node("w4", 0, 4, "β-catenin", "highlight")
node("w5", 0, 5, "TCF/LEF (repressor → activator)", "dna")
node("w6", 0, 6, "Myc, cyclin D, Axin2", "positive")
for a, b, kind in (("w0", "w1", "positive"), ("w1", "w2", "positive"), ("w2", "w3", "negative"),
                   ("w3", "w4", "negative"), ("w4", "w5", "positive"), ("w5", "w6", "positive")):
    d.connect(a, b, kind)
d.connect("w6", "w3", "positive", dashed=True, via=[(col(0) + 2.45, Y[6]), (col(0) + 2.45, Y[3])])

# B Hedgehog
node("h0", 1, 0, "Hedgehog", "drug")
node("h1", 1, 1, "Patched", "receptor")
node("h2", 1, 2, "Smoothened (in the cilium)", "receptor")
node("h3", 1, 3, "SuFu; PKA, GSK3, CK1", "negative")
node("h4", 1, 4, "Gli activator", "highlight")
node("h5", 1, 5, "Gli target genes", "dna")
node("h6", 1, 6, "Ptch1, Gli1", "positive")
for a, b, kind in (("h0", "h1", "negative"), ("h1", "h2", "negative"), ("h2", "h3", "negative"),
                   ("h3", "h4", "negative"), ("h4", "h5", "positive"), ("h5", "h6", "positive")):
    d.connect(a, b, kind)
d.connect("h6", "h1", "positive", dashed=True, via=[(col(1) + 2.45, Y[6]), (col(1) + 2.45, Y[1])])

# C NF-kB
node("n0", 2, 0, "TNF, IL-1, LPS", "drug")
node("n1", 2, 1, "TNFR1, IL-1R, TLR4", "receptor")
node("n2", 2, 2, "IKK (IKKα, IKKβ, NEMO)", "enzyme")
node("n3", 2, 3, "IκBα (→ β-TrCP, proteasome)", "negative")
node("n4", 2, 4, "NF-κB (p65–p50)", "highlight")
node("n5", 2, 5, "κB sites", "dna")
node("n6", 2, 6, "IκBα, A20, cytokines", "positive")
for a, b, kind in (("n0", "n1", "positive"), ("n1", "n2", "positive"), ("n2", "n3", "negative"),
                   ("n3", "n4", "negative"), ("n4", "n5", "positive"), ("n5", "n6", "positive")):
    d.connect(a, b, kind)
d.connect("n6", "n3", "positive", dashed=True, via=[(col(2) + 2.45, Y[6]), (col(2) + 2.45, Y[3])])
d.connect("n6", "n2", "negative", dashed=True, via=[(col(2) - 2.45, Y[6]), (col(2) - 2.45, Y[2])])
bio.label(ax, (col(2) - 2.62, 4.3), "A20", size="tiny", color=P.muted(), rotation=90)

# D Notch
node("c0", 3, 0, "Delta / Jagged (neighbor)", "drug")
node("c1", 3, 1, "Notch", "receptor")
node("c2", 3, 2, "S2 cleavage: ADAM10", "enzyme")
node("c3", 3, 3, "S3 cleavage: γ-secretase", "enzyme")
node("c4", 3, 4, "NICD", "highlight")
node("c5", 3, 5, "CSL + MAML (activator)", "dna")
node("c6", 3, 6, "Hes, Hey", "positive")
for a, b in (("c0", "c1"), ("c1", "c2"), ("c2", "c3"), ("c3", "c4"), ("c4", "c5"), ("c5", "c6")):
    d.connect(a, b, "positive")
bio.label(ax, (col(3), 0.6), "one receptor → one NICD", size="tiny", color=P.muted())
bio.label(ax, (col(0), 0.6), "β-TrCP and the proteasome destroy β-catenin", size="tiny", color=P.muted())
bio.label(ax, (col(1), 0.6), "Gli repressor made in the absence of Hh", size="tiny", color=P.muted())
bio.label(ax, (col(2), 0.6), "IκBα degradation frees NF-κB", size="tiny", color=P.muted())
