# Two hypotheses of squamate relationships (cladograms). (A) Morphology (simplified after Estes et al. 1988
# and Gauthier et al. 2012): Iguania is the sister group of all other squamates (Scleroglossa), and the
# limb-reduced burrowers (snakes, amphisbaenians, dibamids) group together. (B) Molecular phylogenies
# (Townsend et al. 2004; Pyron et al. 2013; Burbrink et al. 2020): dibamids and geckos branch first, and
# iguanians are nested in Toxicofera with anguimorphs and snakes; amphisbaenians are lacertoids.
import wikibio as bio
from wikibio import phylo

P = bio.P
MORPH = "(Iguania,(Gekkota,(Scincoidea,(Lacertoidea,(Anguimorpha,(Serpentes,(Amphisbaenia,Dibamidae)))))));"
MOLEC = ("(Dibamidae,(Gekkota,(Scincoidea,((Lacertoidea,Amphisbaenia)Lacertoidea_s.l.,"
         "(Serpentes,(Anguimorpha,Iguania))Toxicofera))));")
ICONS = {"Iguania": "phylopic/iguana", "Gekkota": "phylopic/gecko", "Scincoidea": "phylopic/lizard",
         "Anguimorpha": "phylopic/monitor-lizard", "Serpentes": "phylopic/snake",
         "Amphisbaenia": "phylopic/amphisbaenian"}
fig, ax = bio.canvas(26, 9.5)
bio.panel(ax, "A", (0.4, 9.1))
bio.label(ax, (5.5, 9.1), "Morphology", size="normal", bold=True)
phylo.tree(ax, MORPH, origin=(0.6, 0.9), width=6.0, height=7.4, root_edge=0.4, icons=ICONS, icon_size=0.5,
           icon_width=1.2, icon_color="animal", label_size="small",
           clades=[dict(tips=["Gekkota", "Dibamidae"], token="dna", style="bar", label="Scleroglossa")])
bio.panel(ax, "B", (13.4, 9.1))
bio.label(ax, (18.5, 9.1), "Molecules", size="normal", bold=True)
phylo.tree(ax, MOLEC, origin=(13.6, 0.9), width=6.0, height=7.4, root_edge=0.4, icons=ICONS, icon_size=0.5,
           icon_width=1.2, icon_color="animal", label_size="small",
           tip_text={"Lacertoidea": "Lacertoidea", "Amphisbaenia": "Amphisbaenia"},
           clades=[dict(node="Toxicofera", token="mrna", style="band", label="Toxicofera")])
