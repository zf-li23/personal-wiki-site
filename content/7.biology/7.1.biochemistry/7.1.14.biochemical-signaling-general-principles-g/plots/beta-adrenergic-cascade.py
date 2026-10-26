"""The beta-adrenergic cascade in a hepatocyte, in SBGN process description notation.

Epinephrine binds the beta-adrenergic receptor (association); the occupied receptor catalyses GDP/GTP
exchange on Gs-alpha; Gs-alpha-GTP stimulates adenylyl cyclase (AC), which converts ATP to cAMP;
cAMP phosphodiesterase (PDE) degrades cAMP to 5'-AMP. Four cAMP dissociate the inactive R2C2
tetramer of protein kinase A into R2(cAMP)4 and two active C subunits. PKA phosphorylates
phosphorylase kinase (PhK), which is also stimulated by Ca2+ (through its calmodulin subunit), and
glycogen synthase (GS, inactivated by phosphorylation). PhK phosphorylates glycogen phosphorylase b to
the active a form, which cleaves glycogen by phosphorolysis to glucose 1-phosphate; in the liver this
is converted to glucose (several steps, omitted process) and released into the blood.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(18.0, 20.0, scale=0.42)
d = network.Diagram(ax)
ym = 17.2
d.cell_frame((0, 0, 18, 20), ym)

# receptor activation
d.simple_chemical("epi", (2.3, 19.0), "Epi", token="drug")
d.macromolecule("bar", (2.3, ym), "β-AR", token="receptor")
d.macromolecule("c_epi", (7.0, 18.0), "Epi", token="drug", w=1.6)
d.macromolecule("c_bar", (7.0, 16.85), "β-AR", token="receptor")
d.complex("rec", ["c_epi", "c_bar"])
d.reaction(["epi", "bar"], ["rec"], at=(4.6, ym), kind="association", angle=0)

# G protein activation (right to left under the membrane)
L, M, R, far = 2.4, 6.6, 10.6, 14.8
d.macromolecule("gs_gdp", (far, 14.6), "Gsα", token="channel", states=["GDP"])
d.macromolecule("gs_gtp", (M, 14.6), "Gsα", token="positive", states=["GTP"])
d.reaction(["gs_gdp"], ["gs_gtp"], at=(R, 14.6), angle=180, modifiers=[("rec", "catalysis")])

# adenylyl cyclase: ATP -> cAMP, and PDE
d.macromolecule("ac", (L, 12.6), "AC", token="enzyme")
d.connect("gs_gtp", "ac", "stimulation")
d.simple_chemical("atp", (L + 1.9, 11.0), "ATP", token="atp")
d.simple_chemical("camp", (R, 11.0), "cAMP", token="highlight")
d.reaction(["atp"], ["camp"], at=(M, 11.0), angle=0, modifiers=[("ac", "catalysis")])
d.simple_chemical("amp", (far + 1.2, 11.0), "5′-AMP", token="atp")
d.macromolecule("pde", (far - 0.8, 12.6), "PDE", token="negative")
d.reaction(["camp"], ["amp"], at=(far - 0.8, 11.0), angle=0, modifiers=[("pde", "catalysis")])

# PKA dissociation
d.macromolecule("r2c2", (L + 0.3, 8.6), "PKA R₂C₂", token="enzyme", units=["inactive"])
d.simple_chemical("camp2", (L + 0.3, 7.2), "4 cAMP", token="highlight", clone=True)
d.macromolecule("pkac", (R + 1.0, 8.6), "PKA C", token="enzyme", multimer=2)
d.macromolecule("r2", (R + 1.0, 7.1), "R₂(cAMP)₄", token="neutral")
d.reaction(["r2c2", "camp2"], ["pkac", "r2"], at=(M, 8.0), kind="dissociation", angle=0)

# targets of PKA: phosphorylase kinase (activated) and glycogen synthase (inactivated)
d.macromolecule("phk", (far, 5.4), "PhK", token="protein", states=[""])
d.macromolecule("phk_p", (M, 5.4), "PhK", token="protein", states=["P"])
d.reaction(["phk"], ["phk_p"], at=(R, 5.4), angle=180, modifiers=[("pkac", "catalysis")])
d.simple_chemical("ca", (M, 6.75), "Ca²⁺", token="ca")
d.connect("ca", "phk_p", "stimulation")
d.macromolecule("gs", (far + 0.5, 8.6), "GS", token="metabolite", states=[""], units=["active"])
d.macromolecule("gs_p", (far + 0.5, 6.9), "GS", token="metabolite", states=["P"], units=["inactive"])
d.reaction(["gs"], ["gs_p"], at=(far + 0.5, 7.75), angle=-90, modifiers=[("pkac", "catalysis", {"via": [(far - 1.5, 8.6), (far - 1.5, 7.75)]})])

# glycogen phosphorylase b -> a
d.macromolecule("gpb", (L, 3.4), "phosphorylase b", token="antibody", states=[""])
d.macromolecule("gpa", (R + 0.4, 3.4), "phosphorylase a", token="antibody", states=["P"])
d.reaction(["gpb"], ["gpa"], at=(M - 0.4, 3.4), angle=0, modifiers=[("phk_p", "catalysis")])

# glycogen -> glucose 1-P -> glucose
d.simple_chemical("glycogen", (far + 1.0, 3.4), "glycogen", token="carbohydrate")
d.simple_chemical("g1p", (far + 1.0, 1.2), "Glc-1-P", token="carbohydrate")
d.reaction(["glycogen"], ["g1p"], at=(far + 1.0, 2.3), angle=-90, modifiers=[("gpa", "catalysis")])
d.simple_chemical("glc", (M, 1.2), "glucose", token="carbohydrate")
d.reaction(["g1p"], ["glc"], at=(R + 0.4, 1.2), angle=180, kind="omitted")
bio.arrow(ax, (M - 1.0, 1.2), (L + 0.2, 1.2), kind="process", bg=bio.P.fill("cytoplasm"))
bio.label(ax, (L - 0.5, 1.2), "to blood\n(GLUT2)", size="small", bold=True)
