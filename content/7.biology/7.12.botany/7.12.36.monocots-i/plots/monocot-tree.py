# Relationships of monocot orders and selected families (APG IV; Chase et al. 2006; Soltis et al. 2018).
# Dots mark families that were part of Cronquist's broad Liliaceae (Liliaceae s.l.): they fall into
# Liliales (Melanthiaceae, Colchicaceae, Smilacaceae, Liliaceae) and Asparagales (Hypoxidaceae,
# Asphodelaceae, Amaryllidaceae, Asparagaceae), with Orchidaceae and Iridaceae nested among them.
# Marks: 1 monocots; 2 aquatic clade of Alismatales (seeds without endosperm); 3 commelinids.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Acoraceae,((Araceae,((Alismataceae,Hydrocharitaceae),(Potamogetonaceae,Zosteraceae))Aquatic)Alismatales,"
          "(Petrosaviaceae,((Dioscoreaceae,(Stemonaceae,Pandanaceae)Pandanales)DP,"
          "(((Alstroemeriaceae,Colchicaceae),(Melanthiaceae,(Smilacaceae,Liliaceae)))Liliales,"
          "((Orchidaceae,(Hypoxidaceae,(Iridaceae,(Asphodelaceae,(Amaryllidaceae,Asparagaceae)))))Asparagales,"
          "(Arecaceae,((Bromeliaceae,(Cyperaceae,Poaceae))Poales,(Commelinaceae,Zingiberaceae)CZ))Commelinids)AC)LAC)PD))Rest)Monocots;")
fig, ax = bio.canvas(30, 17)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.6), width=12.5, height=15.6, label_size="small", root_edge=0.5,
               clades=[dict(tips=["Acoraceae"], token="neutral", style="bar", label="Acorales"),
                       dict(node="Alismatales", token="dna", style=("bar", "branch"), label="Alismatales"),
                       dict(tips=["Petrosaviaceae"], token="neutral", style="bar", label="Petrosaviales"),
                       dict(tips=["Dioscoreaceae"], token="atp", style="bar", label="Dioscoreales"),
                       dict(node="Pandanales", token="atp", style="bar", label="Pandanales"),
                       dict(node="Liliales", token="petal", style=("bar", "branch"), label="Liliales"),
                       dict(node="Asparagales", token="tepal", style=("bar", "branch"), label="Asparagales"),
                       dict(node="Commelinids", token="plant", style=("bar", "branch"), label="Commelinids")],
               marks=[dict(node="Monocots", kind="star", at=0.5, token="highlight", text="1"),
                      dict(node="Aquatic", kind="trait", at=0.5, token="dna", text="2"),
                      dict(node="Commelinids", kind="trait", at=0.5, token="plant", text="3")]
               + [dict(node=f, kind="dot", at=0.6, token="negative") for f in
                  ["Melanthiaceae", "Colchicaceae", "Smilacaceae", "Liliaceae", "Hypoxidaceae", "Asphodelaceae",
                   "Amaryllidaceae", "Asparagaceae"]])
KEY = ["1  Monocots: one cotyledon, scattered bundles, PII plastids",
       "2  Seeds without endosperm; aquatic or wetland",
       "3  Ferulic acid in cell walls (UV fluorescence)"]
for i, k in enumerate(KEY):
    bio.label(ax, (19.8, 14.2 - i * 0.8), k, size="small", ha="left")
phylo.legend(ax, (20.0, 15.2), [("dot", "In Cronquist's broad Liliaceae", "negative")])
