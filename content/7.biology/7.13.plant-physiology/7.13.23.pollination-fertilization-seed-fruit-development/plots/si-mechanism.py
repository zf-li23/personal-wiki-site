# Molecular logic of the two main self-incompatibility systems (SBGN activity flow, simplified).
# A: gametophytic SI of the S-RNase type (Solanaceae, Rosaceae, Plantaginaceae): S-RNases secreted by
#    the style enter every pollen tube; the pollen SLF F-box proteins (in an SCF ubiquitin ligase)
#    collectively recognize all non-self S-RNases and send them to the 26S proteasome; the self S-RNase
#    is not recognized, stays active, degrades the tube RNA and arrests growth ("collaborative non-self
#    recognition").
# B: sporophytic SI of Brassicaceae: the pollen-coat peptide SCR/SP11 binds the stigma receptor kinase
#    SRK of the same S haplotype; with MLPK the receptor activates the E3 ligase ARC1, which marks the
#    compatibility factor Exo70A1 for degradation; secretion to the pollen contact site stops, and the
#    pollen grain is not hydrated.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(21, 9.2)
d = network.Diagram(ax)
bio.panel(ax, "A", (0.2, 9.0))
bio.panel(ax, "B", (11.0, 9.0))
d.compartment("tube", (0.5, 0.4, 10.2, 8.2), "Pollen tube (self pollen, S1)", token="cytoplasm")
d.compartment("pap", (11.3, 0.4, 20.7, 8.2), "Stigma papilla cell (S1S2) with self pollen", token="cytoplasm")

d.activity("self", (2.6, 6.8), "S1-RNase (self)", token="enzyme")
d.activity("non", (6.4, 6.8), "S3-RNase (non-self)", token="enzyme")
d.activity("slf", (6.4, 4.6), "SCF-SLF", token="protein")
d.activity("prot", (8.8, 2.4), "26S proteasome", token="neutral")
d.activity("rna", (2.6, 4.0), "Tube RNA", token="rna")
d.phenotype("arrest", (2.6, 1.6), "Growth arrest", token="negative")
d.connect("slf", "non", kind="negative")
d.connect("non", "prot", kind="positive", via=[(8.8, 6.8)], text="ubiquitin", text_offset=(0.5, 0.0), text_at=0.7)
d.connect("self", "rna", kind="negative")
d.connect("rna", "arrest", kind="negative")
bio.label(ax, (4.3, 5.5), "not recognized", size="small", color=bio.P.muted())

d.activity("scr", (13.4, 6.8), "SCR/SP11 (pollen coat)", token="highlight")
d.activity("srk", (17.6, 6.8), "SRK + MLPK", token="receptor")
d.activity("arc1", (17.6, 4.6), "ARC1 (E3 ligase)", token="protein")
d.activity("exo", (13.4, 4.6), "Exo70A1", token="protein")
d.phenotype("hyd", (13.4, 2.0), "Pollen hydration", token="positive")
d.connect("scr", "srk", kind="positive", text="same haplotype", text_offset=(0, 0.35))
d.connect("srk", "arc1", kind="positive")
d.connect("arc1", "exo", kind="negative")
d.connect("exo", "hyd", kind="positive")
