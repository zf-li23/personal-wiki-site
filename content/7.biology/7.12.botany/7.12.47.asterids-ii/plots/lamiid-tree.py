# Relationships of the lamiids at order and family level (APG IV 2016; Soltis et al. 2018; Refulio-Rodriguez
# & Olmstead 2014; Stull et al. 2015). Icacinales, Metteniusales and Garryales are successive sisters of the
# core lamiids, whose five orders are partly unresolved (Boraginales + Lamiales is the best-supported pair).
# Marks: 1 lamiids (opposite entire leaves, early sympetaly, superior ovary); 2 Gentianales (colleters,
# interpetiolar stipules, contorted corolla); 3 internal phloem (Gentianales except Rubiaceae; Solanaceae and
# Convolvulaceae, in parallel); 4 tropane alkaloids instead of iridoids (Solanaceae + Convolvulaceae);
# 5 helicoid (scorpioid) cymes and four nutlets; 6 fewer than five fertile stamens, zygomorphy.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Icacinaceae,Oncothecaceae)Icacinales,(Metteniusaceae,((Eucommiaceae,Garryaceae)Garryales,"
          "((Rubiaceae,(Gentianaceae,Loganiaceae,(Gelsemiaceae,Apocynaceae)))Gentianales,Vahliaceae,"
          "((Montiniaceae,(Sphenocleaceae,Hydroleaceae)),(Convolvulaceae,Solanaceae))Solanales,"
          "(Boraginaceae,LamialesTip)BL)Core)G)M)Lamiids;")
fig, ax = bio.canvas(32, 15)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=11.0, height=13.4, label_size="small", root_edge=0.5,
               tip_text={"LamialesTip": "Lamiales (24 families)", "Vahliaceae": "Vahliaceae (Vahliales)",
                         "Boraginaceae": "Boraginaceae (Boraginales)", "Metteniusaceae": "Metteniusaceae (Metteniusales)"},
               clades=[dict(node="Icacinales", token="neutral", style=("bar", "branch"), label="Icacinales"),
                       dict(node="Garryales", token="atp", style=("bar", "branch"), label="Garryales"),
                       dict(node="Gentianales", token="petal", style=("bar", "branch"), label="Gentianales"),
                       dict(node="Solanales", token="rna", style=("bar", "branch"), label="Solanales"),
                       dict(node="BL", token="plant", style=("bar", "branch"), label="")],
               marks=[dict(node="Lamiids", kind="star", at=0.5, token="highlight", text="1"),
                      dict(node="Gentianales", kind="trait", at=0.5, token="petal", text="2"),
                      dict(node=["Gentianaceae", "Loganiaceae", "Gelsemiaceae", "Apocynaceae"], kind="trait", at=0.5,
                           token="dna", text="3"),
                      dict(node=["Convolvulaceae", "Solanaceae"], kind="trait", at=0.5, token="rna", text="4"),
                      dict(node="Boraginaceae", kind="trait", at=0.5, token="plant", text="5"),
                      dict(node="LamialesTip", kind="trait", at=0.5, token="plant", text="6")])
KEY = ["1  Lamiids: opposite entire leaves, early sympetaly, superior ovary",
       "2  Colleters, interpetiolar stipules, contorted corolla",
       "3  Internal (intraxylary) phloem",
       "4  Tropane alkaloids; internal phloem (in parallel)",
       "5  Scorpioid cymes, four nutlets, rough hairs",
       "6  Fewer than five fertile stamens; zygomorphy",
       "Polytomy: relationships unresolved"]
for i, k in enumerate(KEY):
    bio.label(ax, (20.6, 5.6 - i * 0.82), k, size="small", ha="left")
