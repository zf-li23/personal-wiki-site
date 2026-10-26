"""Hormonal mobilization of triacylglycerols in the adipocyte (SBGN process description).

Epinephrine (and glucagon) raise cAMP and activate PKA, which phosphorylates perilipin 1 on the surface of
the lipid droplet and hormone-sensitive lipase (HSL). Phosphorylated perilipin releases CGI-58, which binds
and activates adipose triglyceride lipase (ATGL), and lets phosphorylated HSL reach the droplet. ATGL
hydrolyses triacylglycerol to diacylglycerol, HSL diacylglycerol to monoacylglycerol, monoacylglycerol
lipase (MGL) monoacylglycerol to glycerol; each step releases a fatty acid. Insulin lowers cAMP through
phosphodiesterase 3B. Fatty acids leave bound to serum albumin; glycerol goes to the liver.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(25.0, 13.4, scale=0.42)
d = network.Diagram(ax, size="small")
d.compartment("cell", (0.3, 2.2, 24.7, 13.1), "Adipocyte", token="cytoplasm")
d.compartment("blood", (0.3, 0.2, 24.7, 2.0), "Blood", token="extracellular", label_pos="bl")

d.simple_chemical("epi", (2.6, 11.8), "epinephrine", token="drug", r=0.85)
d.macromolecule("pka", (6.6, 11.8), "PKA", token="enzyme")
d.connect("epi", "pka", "stimulation", text="β receptor, cAMP", text_offset=(0, 0.25))
d.simple_chemical("ins", (11.0, 11.8), "insulin", token="drug", r=0.7)
d.macromolecule("pde", (11.0, 9.7), "PDE3B", token="negative")
d.connect("ins", "pde", "stimulation")
d.connect("pde", "pka", "inhibition", text="cAMP ↓", text_offset=(0.1, 0.3))

d.macromolecule("plin", (3.4, 8.6), "perilipin 1", token="lipid", states=[""])
d.macromolecule("plinp", (3.4, 6.6), "perilipin 1", token="lipid", states=["P"])
d.reaction(["plin"], ["plinp"], at=(3.4, 7.6), angle=-90, modifiers=[("pka", "catalysis", {"via": [(6.0, 7.6)]})])
d.macromolecule("hsl", (17.0, 9.7), "HSL", token="protein", states=[""])
d.macromolecule("hslp", (17.0, 7.3), "HSL", token="protein", states=["P"])
d.reaction(["hsl"], ["hslp"], at=(17.0, 8.5), angle=-90, modifiers=[("pka", "catalysis", {"via": [(8.2, 11.8), (8.2, 8.5)]})])
d.macromolecule("atgl", (6.7, 5.6), "ATGL", token="receptor")
d.connect("plinp", "atgl", "stimulation", text="CGI-58", text_offset=(0, 0.3))

y = 4.0
d.simple_chemical("tag", (3.2, y), "TAG", token="lipid", r=0.7)
d.simple_chemical("dag", (10.2, y), "DAG", token="lipid", r=0.7)
d.simple_chemical("mag", (17.0, y), "MAG", token="lipid", r=0.7)
d.simple_chemical("gly", (22.6, y), "glycerol", r=0.85)
d.simple_chemical("fa1", (6.7, 2.9), "FA", r=0.45)
d.simple_chemical("fa2", (13.6, 2.9), "FA", r=0.45)
d.simple_chemical("fa3", (19.8, 2.9), "FA", r=0.45)
d.reaction(["tag"], ["dag", "fa1"], at=(6.7, y), angle=0, modifiers=[("atgl", "catalysis")])
d.reaction(["dag"], ["mag", "fa2"], at=(13.6, y), angle=0, modifiers=[("hslp", "catalysis", {"via": [(13.6, 7.3)]})])
d.macromolecule("mgl", (19.8, 6.0), "MGL", token="channel")
d.reaction(["mag"], ["gly", "fa3"], at=(19.8, y), angle=0, modifiers=[("mgl", "catalysis")])

d.macromolecule("alb", (13.0, 1.0), "serum albumin + FA → muscle, heart", token="neutral", size="tiny")
d.connect("fa2", "alb", "process")
d.simple_chemical("glyb", (22.6, 1.0), "→ liver", r=0.5, size="tiny")
d.connect("gly", "glyb", "process")
