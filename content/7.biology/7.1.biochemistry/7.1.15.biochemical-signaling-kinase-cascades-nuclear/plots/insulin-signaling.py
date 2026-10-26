"""The two main branches of insulin signaling, in SBGN process description notation.

Insulin binds the preformed (alpha-beta)2 insulin receptor (INSR), whose beta subunits
autophosphorylate in trans and phosphorylate IRS1 on several Tyr residues. Left, the mitogenic branch:
phosphotyrosine of IRS1 binds the SH2 domain of the adaptor Grb2, whose SH3 domains hold the
exchange factor Sos; Sos catalyses GDP/GTP exchange on Ras; Ras-GTP stimulates the activation of Raf
(MAPKKK), which doubly phosphorylates MEK (MAPKK), which doubly phosphorylates ERK (MAPK); ERK enters
the nucleus and phosphorylates the transcription factor Elk1, which with SRF stimulates
transcription of genes for growth and division. Right, the metabolic branch: IRS1-P activates PI3K,
which converts the membrane lipid PIP2 to PIP3 (reversed by the phosphatase PTEN); PIP3 recruits
PKB (Akt), which PDK1 phosphorylates; PKB phosphorylates and inactivates GSK3, so that glycogen
synthase (GS) is no longer phosphorylated by GSK3 and stays active, and stimulates the translocation
of GLUT4 from intracellular vesicles to the plasma membrane.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(24.0, 22.0, scale=0.42)
d = network.Diagram(ax, size="small")
ym = 19.4
d.cell_frame((0, 0, 24, 22), ym, nucleus=(0.5, 0.4, 11.0, 4.6))

# receptor
d.macromolecule("ins", (2.2, 21.1), "insulin", token="drug")
d.macromolecule("insr", (2.2, ym), "INSR (αβ)₂", token="receptor", states=[""])
d.macromolecule("c_ins", (7.4, 20.25), "insulin", token="drug")
d.macromolecule("c_insr", (7.4, 19.0), "INSR (αβ)₂", token="receptor", states=[("P", "br")])
d.complex("rec", ["c_ins", "c_insr"])
d.reaction(["ins", "insr"], ["rec"], at=(4.8, ym), kind="association", angle=0)

# IRS1
d.macromolecule("irs", (16.0, 17.0), "IRS1", token="protein", states=[""])
d.macromolecule("irs_p", (11.0, 17.0), "IRS1", token="protein", states=["P"])
d.reaction(["irs"], ["irs_p"], at=(13.5, 17.0), angle=180, modifiers=[("rec", "catalysis", {"via": [(13.5, 18.4)]})])

# MAPK branch
d.macromolecule("grb2", (5.2, 15.2), "Grb2", token="antibody")
d.macromolecule("sos", (7.0, 15.2), "Sos", token="enzyme")
d.complex("gs", ["grb2", "sos"])
d.connect("irs_p", "gs", "stimulation")
d.macromolecule("ras_gdp", (9.3, 13.1), "Ras", token="channel", states=["GDP"])
d.macromolecule("ras_gtp", (2.5, 13.1), "Ras", token="channel", states=["GTP"])
d.reaction(["ras_gdp"], ["ras_gtp"], at=(6.1, 13.1), angle=180, modifiers=[("gs", "catalysis")])
d.macromolecule("raf", (2.5, 11.0), "Raf", token="highlight", states=[""])
d.macromolecule("raf_p", (9.3, 11.0), "Raf", token="highlight", states=["P"])
d.reaction(["raf"], ["raf_p"], at=(6.1, 11.0), angle=0, modifiers=[("ras_gtp", "stimulation")])
d.macromolecule("mek", (9.3, 8.9), "MEK", token="protein", states=["", ""])
d.macromolecule("mek_pp", (2.5, 8.9), "MEK", token="protein", states=["P", "P"])
d.reaction(["mek"], ["mek_pp"], at=(6.1, 8.9), angle=180, modifiers=[("raf_p", "catalysis")])
d.macromolecule("erk", (2.5, 6.8), "ERK", token="positive", states=["", ""])
d.macromolecule("erk_pp", (9.3, 6.8), "ERK", token="positive", states=["P", "P"])
d.reaction(["erk"], ["erk_pp"], at=(6.1, 6.8), angle=0, modifiers=[("mek_pp", "catalysis")])
d.macromolecule("erk_n", (9.3, 3.6), "ERK", token="positive", states=["P", "P"])
d.reaction(["erk_pp"], ["erk_n"], at=(9.3, 5.15), angle=-90)
d.macromolecule("elk", (2.0, 1.6), "Elk1", token="metabolite", states=[""])
d.macromolecule("elk_p", (6.0, 1.6), "Elk1–SRF", token="metabolite", states=["P"])
d.reaction(["elk"], ["elk_p"], at=(4.0, 1.6), angle=0, modifiers=[("erk_n", "catalysis")])
d.phenotype("grow", (9.3, 1.6), "growth genes", size="tiny")
d.connect("elk_p", "grow", "stimulation")

# PI3K branch
d.macromolecule("pi3k", (16.0, 15.0), "PI3K", token="enzyme")
d.connect("irs_p", "pi3k", "stimulation")
d.simple_chemical("pip2", (13.4, ym - 0.05), "PIP₂", token="lipid")
d.simple_chemical("pip3", (20.6, ym - 0.05), "PIP₃", token="lipid")
d.reaction(["pip2"], ["pip3"], at=(17.0, ym - 0.05), angle=0, modifiers=[("pi3k", "catalysis", {"via": [(17.0, 15.0)]})])
d.macromolecule("pten", (20.6, 16.6), "PTEN", token="negative")
d.reaction(["pip3"], ["pip2"], at=(17.0, ym - 1.4), angle=180, modifiers=[("pten", "catalysis", {"via": [(17.6, 16.6), (17.6, ym - 1.4)]})])
d.macromolecule("pkb", (14.0, 12.6), "PKB (Akt)", token="enzyme", states=[""])
d.macromolecule("pkb_p", (20.6, 12.6), "PKB (Akt)", token="enzyme", states=["P"])
d.macromolecule("pdk1", (17.3, 14.0), "PDK1", token="drug")
d.reaction(["pkb"], ["pkb_p"], at=(17.3, 12.6), angle=0, modifiers=[("pdk1", "catalysis"), ("pip3", "necessary", {"via": [(22.6, ym - 0.05), (22.6, 13.4), (17.6, 13.4)]})])
d.macromolecule("gsk", (20.6, 10.2), "GSK3", token="antibody", states=[""])
d.macromolecule("gsk_p", (14.0, 10.2), "GSK3", token="antibody", states=["P"], units=["inactive"])
d.reaction(["gsk"], ["gsk_p"], at=(17.3, 10.2), angle=180, modifiers=[("pkb_p", "catalysis")])
d.macromolecule("gsa", (14.0, 7.6), "glycogen synthase", token="carbohydrate", states=[""], units=["active"])
d.macromolecule("gsi", (20.6, 7.6), "glycogen synthase", token="carbohydrate", states=["P"], units=["inactive"])
d.reaction(["gsa"], ["gsi"], at=(17.3, 7.6), angle=0, modifiers=[("gsk", "catalysis", {"via": [(22.7, 10.2), (22.7, 8.7), (17.3, 8.7)]})])
d.macromolecule("glut_v", (14.0, 4.2), "GLUT4", token="channel", units=["vesicle"])
d.macromolecule("glut_m", (20.6, 4.2), "GLUT4", token="channel", units=["plasma membrane"])
d.reaction(["glut_v"], ["glut_m"], at=(17.3, 4.2), angle=0, modifiers=[("pkb_p", "stimulation", {"via": [(23.1, 12.6), (23.1, 5.4), (17.3, 5.4)]})])
d.phenotype("upt", (17.3, 1.8), "glucose uptake, glycogen synthesis", size="tiny")
d.connect("glut_m", "upt", "stimulation")
d.connect("gsa", "upt", "stimulation")
