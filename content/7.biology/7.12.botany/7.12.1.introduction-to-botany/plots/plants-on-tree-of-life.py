"""Where the organisms of traditional botany sit on the tree of life (cladogram; branch lengths
have no meaning). Simplified after Adl et al. (2019) and Burki et al. (2020): the eukaryotes branch
from within the Archaea; the relationships among the eukaryote supergroups are drawn as a polytomy
except for the well-supported SAR and Amorphea clades. Stars mark lineages that the two-kingdom
system placed in the plant kingdom (algae, fungi and fungus-like organisms); bands mark the three
modern circumscriptions of "plants". Lichens are not a lineage but a symbiosis of a fungus with a
green alga or cyanobacterium.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(25, 15)
nw = ("((Other_bacteria,Cyanobacteria)bac,"
      "(Other_archaea,(Discoba,(Alveolata,Stramenopiles,Rhizaria)sar,Haptophytes,Cryptophytes,"
      "(Glaucophytes,Red_algae,(Chlorophyta,(Charophytes,Land_plants)strep)vir)arch,"
      "(Slime_molds,(Fungi,Animals)op)am)euk)ae)r;")
text = {
    "Other bacteria": "other bacteria",
    "Cyanobacteria": "Cyanobacteria (blue-green algae)",
    "Other archaea": "Archaea",
    "Discoba": "Discoba: euglenids",
    "Alveolata": "Alveolata: dinoflagellates (and ciliates, apicomplexans)",
    "Stramenopiles": "Stramenopiles: brown algae, diatoms, golden algae, oomycetes",
    "Rhizaria": "Rhizaria (foraminifera, radiolarians)",
    "Haptophytes": "Haptophytes (coccolithophores)",
    "Cryptophytes": "Cryptophytes",
    "Glaucophytes": "Glaucophytes",
    "Red algae": "Red algae",
    "Chlorophyta": "Chlorophyta (most green algae)",
    "Charophytes": "Charophytes (stoneworts, Zygnema, ...)",
    "Land plants": "Land plants (bryophytes, ferns, seed plants)",
    "Slime molds": "Amoebozoa: slime molds (and amoebae)",
    "Fungi": "Fungi",
    "Animals": "Animals",
}
icons = {
    "Cyanobacteria": "phylopic/cyanobacterium",
    "Discoba": "phylopic/euglena",
    "Alveolata": "phylopic/dinoflagellate",
    "Stramenopiles": "phylopic/kelp",
    "Haptophytes": "phylopic/coccolithophore",
    "Cryptophytes": "phylopic/cryptophyte",
    "Red algae": "phylopic/porphyra",
    "Chlorophyta": "phylopic/chlamydomonas",
    "Charophytes": "phylopic/chara",
    "Land plants": "phylopic/fern",
    "Slime molds": "phylopic/physarum",
    "Fungi": "phylopic/agaricus",
}
botanical = ["Cyanobacteria", "Discoba", "Alveolata", "Stramenopiles", "Haptophytes", "Cryptophytes",
             "Glaucophytes", "Red algae", "Chlorophyta", "Charophytes", "Land plants", "Slime molds", "Fungi"]
t = phylo.tree(ax, nw, origin=(1.0, 0.6), width=6.5, height=13.6, root_edge=0.4, tip_text=text,
               label_size="small", icons=icons, icon_size=0.62, icon_color="plant",
               clades=[dict(node="bac", token="bacterium", style="branch"),
                       dict(node="arch", token="positive", style=["branch", "bar"], label="Archaeplastida"),
                       dict(node="vir", token="plant", style="bar", label="Viridiplantae"),
                       dict(tips=["Land plants"], token="chloroplast", style="bar", label="Embryophyta")],
               marks=[dict(node=n, kind="star", token="highlight", at=0.55) for n in botanical])
bio.label(ax, (1.0, 0.15), "star: placed in the plant kingdom by the two-kingdom system", size="tiny",
          ha="left", color=P.muted())
