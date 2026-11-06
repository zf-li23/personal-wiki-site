# Auxin biosynthesis, conjugation and degradation (simplified).
# Main route Trp -(TAA)-> IPyA -(YUC)-> IAA; IBA -> IAA by peroxisomal beta-oxidation.
# Reversible storage conjugates on the left, irreversible inactivation on the right.
import wikibio as bio
from wikibio import metabolism as M

fig, ax = bio.canvas(19, 11.5)
P = bio.P
pw = M.Pathway(ax, size="small")
pw.node("trp", (9.5, 10.6), "Tryptophan", bold=True)
pw.node("ipya", (9.5, 8.6), "Indole-3-pyruvate (IPyA)")
pw.node("iaa", (9.5, 6.1), "IAA (free, active)", bold=True)
pw.node("iba", (15.2, 8.6), "IBA")
pw.step("trp", "ipya", enzyme="TAA1 / TAR\n(aminotransferase)", enzyme_size="tiny")
pw.step("ipya", "iaa", enzyme="YUC\n(flavin monooxygenase)", side=(None, "CO₂"), enzyme_size="tiny")
pw.step("iba", "iaa", enzyme="β-oxidation\n(peroxisome)", enzyme_size="tiny", bend=-0.08)

# reversible storage conjugates
bio.label(ax, (3.2, 7.4), "Reversible (storage)", size="small", bold=True)
pw.node("glc", (3.2, 5.9), "IAA–glucose, IAA–inositol\n(ester conjugates)", h=0.75)
pw.node("ala", (3.2, 3.4), "IAA–Ala, IAA–Leu\n(amide conjugates)", h=0.75)
pw.step("iaa", "glc", reversible=True, enzyme="UGT / hydrolase", enzyme_size="tiny")
pw.step("iaa", "ala", reversible=True, enzyme="GH3 / ILR1-ILL\nhydrolases", enzyme_size="tiny", enzyme_flip=True)

# irreversible inactivation
bio.label(ax, (15.6, 5.2), "Irreversible (inactivation)", size="small", bold=True)
pw.node("asp", (15.6, 3.9), "IAA–Asp, IAA–Glu", h=0.6)
pw.node("ox", (9.5, 3.2), "oxIAA")
pw.node("oxg", (9.5, 1.2), "oxIAA–glucose")
pw.node("oxasp", (15.6, 1.2), "oxIAA–Asp / Glu", h=0.6)
pw.step("iaa", "asp", enzyme="GH3", enzyme_size="tiny")
pw.step("iaa", "ox", enzyme="DAO (dioxygenase)", enzyme_size="tiny")
pw.step("ox", "oxg", enzyme="UGT", enzyme_size="tiny")
pw.step("asp", "oxasp", enzyme="oxidation", enzyme_size="tiny")
