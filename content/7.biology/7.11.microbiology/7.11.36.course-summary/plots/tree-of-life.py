"""The tree of life in outline (cladogram; branch lengths have no meaning). Rooted between Bacteria and
Archaea, with the eukaryotes branching from within the Archaea as the sister group of the Asgard
archaea. Stars: lineages with macroscopic multicellular members (animals, fungi with fruiting bodies,
brown algae, red algae, land plants); every other branch, and most members of these, is microbial."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(20, 14)
nw = ("((Terrabacteria,Gracilicutes,CPR)bac,"
      "((Euryarchaea,DPANN)e,(TACK,(Asgard,"
      "(Discoba,Metamonada,(Alveolata,Stramenopiles,Rhizaria)sar,Haptista,Cryptista,Archaeplastida,"
      "(Amoebozoa,(Fungi,Animals)op)am)euk)ae)pr)arc)r;")
text = {
    "Terrabacteria": "Terrabacteria (Bacillota, Actinomycetota, Cyanobacteriota, ...)",
    "Gracilicutes": "Gracilicutes (Pseudomonadota, FCB, PVC, spirochetes, ...)",
    "CPR": "candidate phyla radiation",
    "Euryarchaea": "Methanobacteriota, Halobacteriota, Thermoplasmatota",
    "DPANN": "DPANN archaea",
    "TACK": "TACK archaea (Thermoproteota)",
    "Asgard": "Asgard archaea",
    "Discoba": "Discoba (euglenids, kinetoplastids)",
    "Metamonada": "Metamonada (Giardia, Trichomonas)",
    "Alveolata": "Alveolata (ciliates, dinoflagellates, apicomplexans)",
    "Stramenopiles": "Stramenopiles (diatoms, oomycetes, brown algae)",
    "Rhizaria": "Rhizaria (foraminifera, radiolarians)",
    "Haptista": "Haptista (coccolithophores)",
    "Cryptista": "Cryptista",
    "Archaeplastida": "Archaeplastida (red and green algae, land plants)",
    "Amoebozoa": "Amoebozoa (amoebae, slime molds)",
    "Fungi": "Fungi",
    "Animals": "Animals",
}
t = phylo.tree(ax, nw, origin=(1.0, 0.7), width=6.0, height=12.4, root_edge=0.4, tip_text=text,
               label_size="small",
               clades=[dict(node="bac", token="bacterium", style=["branch", "bar"], label="Bacteria"),
                       dict(node="arc", token="enzyme", style="branch"),
                       dict(tips=["Euryarchaea", "DPANN", "TACK", "Asgard"], token="enzyme", style="bar",
                            label="Archaea"),
                       dict(node="euk", token="nucleus", style=["branch", "bar"], label="Eukaryotes")],
               marks=[dict(node=n, kind="star", token="highlight", at=0.6)
                      for n in ("Stramenopiles", "Archaeplastida", "Fungi", "Animals")])
bio.label(ax, (1.0, 0.2), "star: lineage with macroscopic multicellular members", size="tiny",
          ha="left", color=P.muted())
