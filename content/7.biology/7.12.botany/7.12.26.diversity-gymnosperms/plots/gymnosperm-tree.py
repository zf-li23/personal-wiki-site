"""The twelve families of living gymnosperms in the classification of Christenhusz et al. (2011): four
subclasses (Cycadidae, Ginkgoidae, Gnetidae, Pinidae) and eight orders. Cladogram, branch lengths not to
scale; the gnetophytes are drawn as the sister group of Pinaceae (the gnepine hypothesis, supported by many
phylogenomic analyses such as Ran et al. 2018, but still debated); Christenhusz et al. keep them as a
separate subclass. Right: approximate numbers of genera and species (current estimates)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Cycadaceae,Zamiaceae)Cycadales,Ginkgoaceae)CG,(((Ephedraceae,(Gnetaceae,Welwitschiaceae))Gnetidae,Pinaceae)Gnepine,"
          "((Araucariaceae,Podocarpaceae)Araucariales,(Sciadopityaceae,(Cupressaceae,Taxaceae)))Cupressales)Conifers)Gymnosperms;")
COUNTS = {"Cycadaceae": "1 / c. 120", "Zamiaceae": "9 / c. 250", "Ginkgoaceae": "1 / 1", "Ephedraceae": "1 / c. 70",
          "Gnetaceae": "1 / c. 40", "Welwitschiaceae": "1 / 1", "Pinaceae": "11 / c. 230", "Araucariaceae": "3 / c. 40",
          "Podocarpaceae": "c. 19 / c. 190", "Sciadopityaceae": "1 / 1", "Cupressaceae": "c. 30 / c. 160",
          "Taxaceae": "6 / c. 30"}
ORDER = {"Cycadaceae": "Cycadales", "Ginkgoaceae": "Ginkgoales", "Ephedraceae": "Ephedrales", "Gnetaceae": "Gnetales",
         "Welwitschiaceae": "Welwitschiales", "Pinaceae": "Pinales", "Araucariaceae": "Araucariales",
         "Sciadopityaceae": "Cupressales", "Zamiaceae": "Cycadales", "Podocarpaceae": "Araucariales",
         "Cupressaceae": "Cupressales", "Taxaceae": "Cupressales"}

fig, ax = bio.canvas(28, 15)
t = phylo.tree(ax, NEWICK, origin=(1.0, 1.0), width=8.5, height=12.6, direction="right", root_edge=0.3, label_size="small",
               icons={"Cycadaceae": "phylopic/cycad", "Ginkgoaceae": "phylopic/ginkgo", "Ephedraceae": "phylopic/ephedra",
                      "Gnetaceae": "phylopic/gnetum", "Welwitschiaceae": "phylopic/welwitschia", "Pinaceae": "phylopic/pine",
                      "Cupressaceae": "phylopic/conifer"},
               icon_size=0.7, icon_color="plant",
               clades=[dict(node="Cycadales", token="plant", style="band", label="Cycadidae"),
                       dict(tips=["Ginkgoaceae"], token="positive", style="band", label="Ginkgoidae"),
                       dict(node="Gnetidae", token="highlight", style="band", label="Gnetidae"),
                       dict(node="Conifers", token="animal", style="bar", label="Pinidae + Gnetidae")])
for tip in t.tips():
    bio.label(ax, (19.2, tip.xy[1]), ORDER.get(tip.name, ""), size="small", ha="left", color=P.muted())
    bio.label(ax, (23.6, tip.xy[1]), COUNTS[tip.name], size="small", ha="left", color=P.muted())
bio.label(ax, (19.2, 14.3), "Order", size="small", bold=True, ha="left")
bio.label(ax, (23.6, 14.3), "Genera / species", size="small", bold=True, ha="left")
