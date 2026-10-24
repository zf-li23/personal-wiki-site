# The EGF -> RAS -> RAF -> MEK -> ERK cascade in SBGN Process Description notation: each activation step is a
# process (square) turning the unmodified form into the phosphorylated one (state variables "P"), catalysed by
# the active kinase of the step above. Active ERK enters the nucleus and phosphorylates ELK1, which (with SRF)
# stimulates transcription of FOS.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(17, 21, scale=0.42)
d = network.Diagram(ax)
ym = 17.9
d.cell_frame((0, 0, 17, 21), ym, nucleus=(0.5, 0.4, 16.5, 5.6))

# ligand binding and receptor dimerisation with trans-autophosphorylation
d.macromolecule("egf", (2.6, 19.7), "EGF", token="drug")
d.macromolecule("egfr", (2.6, ym), "EGFR", token="receptor", states=[""])
d.macromolecule("c_egf", (9.0, 18.75), "EGF", token="drug", multimer=2)
d.macromolecule("c_egfr", (9.0, 17.55), "EGFR", token="receptor", multimer=2, states=[("P", "br")])
d.complex("rec", ["c_egf", "c_egfr"])
d.reaction(["egf", "egfr"], ["rec"], at=(5.6, ym), kind="association", angle=0)

# adaptor complex: GRB2 bound to the RAS exchange factor SOS
d.macromolecule("grb2", (12.85, 15.9), "GRB2", token="protein")
d.macromolecule("sos", (14.55, 15.9), "SOS", token="enzyme")
d.complex("grbsos", ["grb2", "sos"])

rows = {"ras": 14.0, "raf": 11.7, "mek": 9.4, "erk": 7.1}
L, M, R = 2.6, 6.6, 10.6
far = 14.4

# RAS: GDP/GTP exchange catalysed by SOS, at the receptor (right to left)
d.macromolecule("ras_gdp", (far, rows["ras"]), "RAS", token="channel", states=["GDP"])
d.macromolecule("ras_gtp", (M, rows["ras"]), "RAS", token="channel", states=["GTP"])
d.simple_chemical("gtp", (12.0, 12.85), "GTP", token="atp")
d.simple_chemical("gdp", (9.2, 12.85), "GDP", token="atp")
d.reaction([("ras_gdp", {}), ("gtp", {})], ["ras_gtp", "gdp"], at=(R, rows["ras"]), angle=180,
           modifiers=[("grbsos", "catalysis"), ("rec", "stimulation")])

# RAF activation (left to right), stimulated by RAS-GTP
d.macromolecule("raf", (L, rows["raf"]), "RAF", token="highlight", states=[""])
d.macromolecule("raf_p", (R, rows["raf"]), "RAF", token="highlight", states=["P"])
d.reaction(["raf"], ["raf_p"], at=(M, rows["raf"]), angle=0, modifiers=[("ras_gtp", "stimulation")])

# MEK double phosphorylation (right to left), catalysed by RAF
d.macromolecule("mek", (far, rows["mek"]), "MEK", token="protein", states=["", ""])
d.macromolecule("mek_pp", (M, rows["mek"]), "MEK", token="protein", states=["P", "P"])
d.reaction(["mek"], ["mek_pp"], at=(R, rows["mek"]), angle=180, modifiers=[("raf_p", "catalysis")])

# ERK double phosphorylation (left to right), catalysed by MEK
d.macromolecule("erk", (L, rows["erk"]), "ERK", token="positive", states=["", ""])
d.macromolecule("erk_pp", (R, rows["erk"]), "ERK", token="positive", states=["P", "P"])
d.reaction(["erk"], ["erk_pp"], at=(M, rows["erk"]), angle=0, modifiers=[("mek_pp", "catalysis")])

# nuclear translocation through the envelope
d.macromolecule("erk_n", (R, 4.3), "ERK", token="positive", states=["P", "P"])
d.reaction(["erk_pp"], ["erk_n"], at=(R, 5.6), angle=-90)

# ELK1 phosphorylation (right to left), catalysed by nuclear ERK
d.macromolecule("elk1", (far, 2.3), "ELK1", token="metabolite", states=[""])
d.macromolecule("elk1_p", (M, 2.3), "ELK1", token="metabolite", states=["P"])
d.reaction(["elk1"], ["elk1_p"], at=(R, 2.3), angle=180, modifiers=[("erk_n", "catalysis")])

# FOS transcription: from nothing (source) to mRNA, needs the gene, stimulated by ELK1-P
d.empty("src", (4.0, 4.75))
d.nucleic_acid("fos", (1.85, 3.3), "FOS", units=["ct:gene"])
d.nucleic_acid("fos_m", (4.0, 1.35), "FOS", token="mrna", units=["ct:mRNA"])
d.reaction(["src"], ["fos_m"], at=(4.0, 3.3), angle=-90, modifiers=[("fos", "necessary"), ("elk1_p", "stimulation")])
