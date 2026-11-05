# The ANA grade, Ceratophyllales and the other lineages of Mesangiospermae (APG IV; Soltis et al. 2018),
# with selected character changes mapped on the branches: dioecy and an 8-celled, 9-nucleate embryo sac in
# Amborella; a 4-celled, 4-nucleate embryo sac with diploid endosperm in Nymphaeales and Austrobaileyales;
# the 7-celled, 8-nucleate embryo sac with triploid endosperm in Mesangiospermae; tricolpate pollen in
# eudicots (convergent tricolpate-like pollen in Schisandraceae); ethereal-oil cells in Austrobaileyales and
# in magnoliids + Chloranthales. The polytomy shows the unresolved relationships among Mesangiospermae.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Amborellales,(Nymphaeales,(Austrobaileyales,((Magnoliids,Chloranthales)MC,Monocots,"
          "(Ceratophyllales,Eudicots)CE)Mesangiospermae)Rest)Rest2)Angiosperms;")
fig, ax = bio.canvas(30, 12)
t = phylo.tree(ax, NEWICK, origin=(1.0, 1.0), width=12.5, height=9.6, label_size="normal", root_edge=0.6,
               clades=[dict(tips=["Amborellales"], token="neutral", style="branch"),
                       dict(tips=["Nymphaeales"], token="neutral", style="branch"),
                       dict(tips=["Austrobaileyales"], token="neutral", style="branch"),
                       dict(node="Mesangiospermae", token="plant", style="bar", label="Mesangiospermae")],
               marks=[dict(node="Amborellales", kind="trait", at=0.5, token="negative", text="1"),
                      dict(node="Nymphaeales", kind="trait", at=0.5, token="dna", text="2"),
                      dict(node="Austrobaileyales", kind="trait", at=0.35, token="dna", text="2"),
                      dict(node="Austrobaileyales", kind="star", at=0.7, token="highlight", text="4"),
                      dict(node="Mesangiospermae", kind="trait", at=0.5, token="positive", text="3"),
                      dict(node="MC", kind="star", at=0.5, token="highlight", text="4"),
                      dict(node="Eudicots", kind="trait", at=0.5, token="rna", text="5"),
                      dict(node="Austrobaileyales", kind="dot", at=0.88, token="rna", text="5'")])
bio.label(ax, (2.2, 11.4), "ANA grade: Amborellales, Nymphaeales, Austrobaileyales", size="title", ha="left")
KEY = ["1  Dioecy; embryo sac 8-celled, 9-nucleate; triploid endosperm",
       "2  Embryo sac 4-celled, 4-nucleate; diploid endosperm",
       "3  Embryo sac 7-celled, 8-nucleate (Polygonum type); triploid endosperm",
       "4  Ethereal-oil cells",
       "5  Tricolpate pollen (5': convergent tricolpate-like pollen in Schisandraceae)"]
for i, k in enumerate(KEY):
    bio.label(ax, (18.4, 9.2 - i * 1.05), k, size="small", ha="left")
