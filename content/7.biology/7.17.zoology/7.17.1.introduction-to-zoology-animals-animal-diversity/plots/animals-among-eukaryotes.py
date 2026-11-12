"""Where animals sit among the eukaryotes (cladogram; branch lengths are meaningless).

Topology after the phylogenomic consensus of Burki et al. (2020, Trends Ecol. Evol. 35: 43) and, for the
holozoans, Torruella et al. (2015) and Grau-Bove et al. (2017): animals are opisthokonts, the sister
group of the choanoflagellates; with the filastereans (Capsaspora) and ichthyosporeans they form
Holozoa, the sister group of Holomycota (fungi and nucleariid amoebae). Relationships among the other
eukaryotic supergroups are drawn as a polytomy because the root of the eukaryote tree is unresolved.
Bars mark characters that arose on a branch.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((((((Metazoa,Choanoflagellata)Choanozoa,Filasterea)Filozoa,Ichthyosporea)Holozoa,"
          "(Fungi,Nucleariida)Holomycota)Opisthokonta,Amoebozoa)Amorphea,"
          "SAR,Archaeplastida,'Haptista and Cryptista',Discoba,Metamonada)Eukaryota;")
TEXT = {"Metazoa": "Metazoa (animals)", "Choanoflagellata": "Choanoflagellates", "Filasterea": "Filasterea (Capsaspora)",
        "Ichthyosporea": "Ichthyosporea", "Fungi": "Fungi", "Nucleariida": "Nucleariid amoebae",
        "Amoebozoa": "Amoebozoa", "SAR": "SAR (ciliates, apicomplexans, diatoms, foraminifera)",
        "Archaeplastida": "Archaeplastida (red algae, green plants)", "Discoba": "Discoba (euglenids, trypanosomes)",
        "Metamonada": "Metamonada (Giardia)"}
ICONS = {
    "Metazoa": "phylopic/honey-bee", "Choanoflagellata": "phylopic/choanoflagellate", "Fungi": "phylopic/agaricus",
    "Amoebozoa": "phylopic/amoeba", "SAR": "phylopic/paramecium", "Archaeplastida": "phylopic/chlamydomonas",
    "Discoba": "phylopic/euglena", "Metamonada": "phylopic/giardia", "Haptista and Cryptista": "phylopic/coccolithophore",
}
KEY = [("Opisthokonta", "single posterior flagellum"), ("Choanozoa", "collar of microvilli around the flagellum"),
       ("Metazoa", "epithelia, collagen-based ECM, embryo with germ layers")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.28, va="bottom")
         for k, (n, _) in enumerate(KEY)]
fig, ax = bio.canvas(24.5, 10.6)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.6), width=8.6, height=9.4, direction="right", root_edge=0.4,
               tip_text=TEXT, icons=ICONS, icon_size=0.62, icon_width=0.95, label_size="small",
               clades=[dict(node="Holozoa", token="animal", style="band", label="Holozoa"),
                       dict(node="Opisthokonta", token="dna", style="bar", label="Opisthokonta")],
               marks=MARKS)
x0, y0 = 17.6, 2.6
bio.label(ax, (x0, y0 + 0.5), "Characters gained", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(KEY):
    yy = y0 - k * 0.42
    phylo.marker(ax, (x0 + 0.12, yy), "trait", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
