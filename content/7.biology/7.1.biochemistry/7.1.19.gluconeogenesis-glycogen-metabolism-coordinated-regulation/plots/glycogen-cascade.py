"""Reciprocal covalent regulation of glycogen phosphorylase and glycogen synthase (SBGN process description).

Left: epinephrine (muscle, liver) or glucagon (liver) -> cAMP -> PKA, which phosphorylates and activates
phosphorylase kinase; phosphorylase kinase (also activated by Ca2+ through its calmodulin subunit)
phosphorylates glycogen phosphorylase b on Ser14, giving the active a form. AMP activates phosphorylase b
allosterically (muscle); glucose binds phosphorylase a (liver) and promotes its dephosphorylation by PP1.
Right: GSK3, after priming by casein kinase II (CKII), phosphorylates glycogen synthase a, giving the
inactive b form; insulin activates PKB, which phosphorylates and inactivates GSK3. PP1 (stimulated by
insulin, inhibited by phosphorylase a in the liver) dephosphorylates phosphorylase a and glycogen
synthase b; glucose 6-phosphate makes synthase b a better substrate for PP1 and activates it directly.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(28.0, 18.0, scale=0.4)
d = network.Diagram(ax, size="small")
d.compartment("cyt", (0.3, 0.3, 27.7, 17.7), "Cytosol (myocyte or hepatocyte)", token="cytoplasm", label_pos="bl")

# --- hormones -------------------------------------------------------------------------------------
d.simple_chemical("epi", (4.85, 16.4), "epinephrine,\nglucagon", token="drug", r=0.85)
d.macromolecule("pka", (4.85, 13.9), "PKA", token="enzyme")
d.connect("epi", "pka", "stimulation", text="cAMP", text_offset=(0.5, 0))
d.simple_chemical("ins", (23.4, 16.4), "insulin", token="drug", r=0.75)
d.macromolecule("pkb", (23.4, 13.9), "PKB", token="enzyme")
d.connect("ins", "pkb", "stimulation", text="IRS1, PI3K", text_offset=(0.8, 0))

# --- phosphorylase kinase ---------------------------------------------------------------------------
d.macromolecule("phkb", (2.3, 11.4), "phosphorylase kinase", token="protein", states=[""], size="tiny")
d.macromolecule("phka", (8.4, 11.4), "phosphorylase kinase", token="protein", states=["P"], size="tiny")
d.reaction(["phkb"], ["phka"], at=(4.85, 11.4), angle=0, modifiers=[("pka", "catalysis")])
d.simple_chemical("ca", (11.6, 11.4), "Ca²⁺", token="ca", r=0.5)
d.connect("ca", "phka", "stimulation")

# --- glycogen phosphorylase -------------------------------------------------------------------------
d.macromolecule("phb", (4.2, 8.5), "phosphorylase b", token="antibody", states=[""])
d.macromolecule("pha", (11.4, 8.5), "phosphorylase a", token="antibody", states=["P"])
d.reaction(["phb"], ["pha"], at=(7.8, 9.3), angle=0, modifiers=[("phka", "catalysis", {"via": [(7.8, 10.4)]})])
d.reaction(["pha"], ["phb"], at=(7.8, 7.7), angle=180, id="dephos_ph")
d.simple_chemical("amp", (1.4, 9.9), "AMP", r=0.45)
d.connect("amp", "phb", "stimulation")
d.simple_chemical("glc", (4.2, 6.3), "glucose\n(liver)", r=0.62)
d.connect("glc", "dephos_ph", "stimulation")
d.phenotype("brk", (11.4, 10.6), "glycogen breakdown", size="tiny")
d.connect("pha", "brk", "stimulation")

# --- glycogen synthase ------------------------------------------------------------------------------
d.macromolecule("gsa", (17.2, 8.5), "glycogen synthase a", token="carbohydrate", states=[""])
d.macromolecule("gsb", (24.4, 8.5), "glycogen synthase b", token="carbohydrate", states=["P"], units=["3 sites"])
d.reaction(["gsa"], ["gsb"], at=(20.8, 9.3), angle=0, id="phos_gs")
d.reaction(["gsb"], ["gsa"], at=(20.8, 7.7), angle=180, id="dephos_gs")
d.macromolecule("gsk", (20.8, 11.4), "GSK3", token="receptor", states=[""])
d.macromolecule("gskp", (26.0, 11.4), "GSK3", token="receptor", states=["P"], units=["inactive"])
d.reaction(["gsk"], ["gskp"], at=(23.4, 11.4), angle=0, modifiers=[("pkb", "catalysis")])
d.connect("gsk", "phos_gs", "catalysis")
d.macromolecule("ck2", (16.6, 11.4), "CKII", token="neutral")
d.connect("ck2", "phos_gs", "necessary", text="priming", text_offset=(-0.3, 0.2))
d.simple_chemical("g6p", (26.5, 6.0), "G6P", r=0.5)
d.connect("g6p", "dephos_gs", "stimulation", via=[(24.4, 6.0)])
d.connect("g6p", "gsb", "stimulation", bend=-0.25)
d.phenotype("syn", (17.2, 6.4), "glycogen synthesis", size="tiny")
d.connect("gsa", "syn", "stimulation")

# --- PP1 ------------------------------------------------------------------------------------------
d.macromolecule("pp1", (14.3, 4.3), "PP1", token="positive", w=2.2)
d.connect("pp1", "dephos_ph", "catalysis", via=[(7.8, 4.3)])
d.connect("pp1", "dephos_gs", "catalysis", via=[(20.8, 4.3)])
d.connect("pha", "pp1", "inhibition", text="liver", text_offset=(0.5, 0.1))
d.simple_chemical("ins2", (14.3, 1.6), "insulin", token="drug", r=0.65, clone=True)
d.connect("ins2", "pp1", "stimulation")
