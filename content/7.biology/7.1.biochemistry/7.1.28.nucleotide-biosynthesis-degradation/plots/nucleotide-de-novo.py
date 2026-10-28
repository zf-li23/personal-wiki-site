"""De novo synthesis of purine and pyrimidine ribonucleotides, with the main feedback controls.
Purines (left): the ring is built on ribose 5-phosphate. PRPP synthetase makes PRPP; glutamine-PRPP
amidotransferase (the committed step) gives 5-phosphoribosylamine (PRA); glycine, two formyl groups from
N10-formyltetrahydrofolate, a second glutamine amide, bicarbonate and the amino group of aspartate (released
as fumarate) are added in nine more steps to give IMP (in animals AIR is carboxylated directly to CAIR).
IMP branches to AMP (aspartate, GTP) and to GMP (NAD+ oxidation to XMP, then glutamine, ATP).
Pyrimidines (right): carbamoyl phosphate synthetase II (Gln, HCO3-, 2 ATP) and aspartate transcarbamoylase
(committed step in bacteria) give N-carbamoylaspartate; dihydroorotase closes the ring (CPS II, ATCase and
dihydroorotase form the trifunctional CAD in animals); dihydroorotate dehydrogenase on the outer face of the
inner mitochondrial membrane passes electrons to ubiquinone; orotate receives ribose 5-phosphate from PRPP
and OMP is decarboxylated to UMP (both steps on UMP synthase in animals); UTP is aminated to CTP.
ADSS, ADSL: adenylosuccinate synthetase and lyase; IMPDH: IMP dehydrogenase.
Red text: feedback inhibitors; green text: activators."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(28.0, 17.4)
neg, pos = P.edge("negative"), P.edge("positive")


def note(xy, text, color, ha="left"):
    bio.label(ax, xy, text, size="tiny", color=color, ha=ha, bold=True)


pw = M.Pathway(ax, size="small")
# ---- purines ----
XA, XB = 6.0, 12.6
ys = [16.4, 14.6, 12.8, 11.0, 9.2, 7.4, 5.6]
for k, (i, t) in enumerate([("r5p", "Ribose 5-phosphate"), ("prpp", "PRPP"), ("pra", "5-Phosphoribosylamine"),
                            ("gar", "GAR"), ("fgar", "FGAR"), ("fgam", "FGAM"), ("air", "AIR")]):
    pw.node(i, (XA, ys[k]), t, bold=i in ("prpp",))
for k, (i, t) in enumerate([("cair", "CAIR"), ("saicar", "SAICAR"), ("aicar", "AICAR"), ("faicar", "FAICAR"),
                            ("imp", "IMP")]):
    pw.node(i, (XB, ys[6 - k]), t, bold=i == "imp", token="highlight" if i == "imp" else "metabolite")
pw.step("r5p", "prpp", enzyme="PRPP synthetase", side=("ATP", "AMP"))
m_at, _, _ = pw.step("prpp", "pra", enzyme="Gln-PRPP\namidotransferase", side=("Gln", "Glu + PPᵢ"))
pw.step("pra", "gar", enzyme="GAR synthetase", side=("Gly + ATP", "ADP + Pᵢ"))
pw.step("gar", "fgar", enzyme="GAR transformylase", side=("N¹⁰-formyl-THF", "THF"))
pw.step("fgar", "fgam", enzyme="FGAM synthetase", side=("Gln + ATP", "Glu + ADP"))
pw.step("fgam", "air", enzyme="AIR synthetase", side=("ATP", "ADP + Pᵢ"))
pw.step("air", "cair", enzyme="AIR carboxylase", side=("HCO₃⁻", None), flip=True)
pw.step("cair", "saicar", enzyme="SAICAR synthetase", side=("Asp + ATP", "ADP + Pᵢ"))
pw.step("saicar", "aicar", enzyme="SAICAR lyase", side=(None, "fumarate"))
pw.step("aicar", "faicar", enzyme="AICAR transformylase", side=("N¹⁰-formyl-THF", "THF"))
pw.step("faicar", "imp", enzyme="IMP cyclohydrolase", side=(None, "H₂O"), flip=True)
# branches
pw.node("samp", (9.9, 14.6), "Adenylosuccinate", size="tiny")
pw.node("amp", (9.9, 16.4), "AMP", bold=True, token="highlight")
pw.node("xmp", (15.3, 14.6), "XMP")
pw.node("gmp", (15.3, 16.4), "GMP", bold=True, token="highlight")
pw.step("imp", "samp", enzyme="ADSS", side=("Asp + GTP", "GDP + Pᵢ"))
pw.step("samp", "amp", enzyme="ADSL", side=(None, "fumarate"), flip=True)
pw.step("imp", "xmp", enzyme="IMPDH", side=("NAD⁺", "NADH"), flip=True)
pw.step("xmp", "gmp", enzyme="GMP synthetase", side=("Gln + ATP", "AMP + PPᵢ"))
note((0.3, 15.5), "⊣ ADP, GDP", neg)
note((0.3, 13.7), "⊣ IMP, AMP, GMP\n↑ PRPP", neg)
note((9.9, 13.1), "⊣ AMP", neg, ha="center")
note((15.3, 13.1), "⊣ GMP", neg, ha="center")
bio.label(ax, (9.3, 4.0), "Purines: ring built on ribose 5-P\n(steps PRA → IMP: 4 ATP, 2 Gln, Gly, Asp,\n2 formyl-THF, HCO₃⁻)",
          size="tiny", color=P.muted())

# ---- pyrimidines ----
XC = 21.6
yp = [16.4, 14.8, 13.2, 11.6, 10.0, 8.4, 6.8, 5.2, 3.6]
for k, (i, t) in enumerate([("gln", "Gln + HCO₃⁻"), ("cp", "Carbamoyl phosphate"), ("ca", "N-Carbamoylaspartate"),
                            ("dho", "Dihydroorotate"), ("oro", "Orotate"), ("omp", "OMP"), ("ump", "UMP"),
                            ("udp", "UDP"), ("utp", "UTP")]):
    pw.node(i, (XC, yp[k]), t, bold=i in ("cp", "ump"), token="highlight" if i == "ump" else "metabolite")
pw.node("ctp", (26.0, 3.6), "CTP", bold=True, token="highlight")
pw.step("gln", "cp", enzyme="CPS II", side=("2 ATP", "Glu + 2 ADP + Pᵢ"))
pw.step("cp", "ca", enzyme="ATCase", side=("Asp", "Pᵢ"))
pw.step("ca", "dho", enzyme="dihydroorotase", side=(None, "H₂O"))
pw.step("dho", "oro", enzyme="DHODH", side=("Q", "QH₂"))
pw.step("oro", "omp", enzyme="OPRT", side=("PRPP", "PPᵢ"))
pw.step("omp", "ump", enzyme="OMP decarboxylase", side=(None, "CO₂"))
pw.step("ump", "udp", enzyme="UMP kinase", side=("ATP", "ADP"))
pw.step("udp", "utp", enzyme="NDP kinase", side=("ATP", "ADP"))
pw.step("utp", "ctp", enzyme="CTP synthetase", side=("Gln + ATP", "Glu + ADP + Pᵢ"), flip=True)
# CAD and UMP synthase brackets
for (y0, y1, text) in [(11.4, 16.6, "CAD\n(animals)"), (6.6, 10.2, "UMP\nsynthase")]:
    x = 25.4
    ax.plot([x, x + 0.25, x + 0.25, x], [y1, y1, y0, y0], color=P.muted(), lw=1.2)
    bio.label(ax, (x + 0.45, (y0 + y1) / 2), text, size="tiny", color=P.muted(), ha="left")
note((18.6, 16.0), "animals:\n⊣ UTP; ↑ PRPP, ATP", neg, ha="center")
note((18.6, 14.0), r"$\it{E.\ coli}$:" "\n⊣ CTP; ↑ ATP", neg, ha="center")
bio.label(ax, (18.6, 10.8), "inner mitochondrial\nmembrane (→ Q)", size="tiny", color=P.edge("mitochondrion"))
bio.label(ax, (18.0, 6.0), "Pyrimidines: ring closed first,\nribose 5-P added as PRPP", size="tiny", color=P.muted())
