# The nitrogen-fixing clade and the distribution of root-nodule symbioses (after Soltis et al. 1995 and
# Werner et al. 2014, simplified to families). Fabales diverge first; Rosales are sister to Cucurbitales +
# Fagales. Filled dots: families with rhizobial nodules (Fabaceae; Parasponia in Cannabaceae); open dots:
# families with Frankia (actinorhizal) nodules; unmarked families do not nodulate.
import wikibio as bio
from wikibio import phylo

NEWICK = ("((Polygalaceae,Fabaceae)Fabales,"
          "((Rosaceae,((Rhamnaceae,Elaeagnaceae),(Ulmaceae,(Cannabaceae,(Moraceae,Urticaceae)))))Rosales,"
          "(((Coriariaceae,Cucurbitaceae),(Datiscaceae,Begoniaceae))Cucurbitales,"
          "(Nothofagaceae,(Fagaceae,((Myricaceae,Juglandaceae),(Casuarinaceae,Betulaceae))))Fagales)))NFC;")
RHIZ = ["Fabaceae", "Cannabaceae"]
FRANK = ["Rosaceae", "Rhamnaceae", "Elaeagnaceae", "Coriariaceae", "Datiscaceae", "Myricaceae", "Casuarinaceae",
         "Betulaceae"]
fig, ax = bio.canvas(30, 15)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.6), width=10.0, height=13.6, label_size="small", root_edge=0.4,
               clades=[dict(node="Fabales", token="petal", style="bar", label="Fabales"),
                       dict(node="Rosales", token="plant", style="bar", label="Rosales"),
                       dict(node="Cucurbitales", token="anther", style="bar", label="Cucurbitales"),
                       dict(node="Fagales", token="dna", style="bar", label="Fagales")],
               marks=[dict(node=[n], kind="dot", at=1.0, token="positive", size=0.34) for n in RHIZ]
               + [dict(node=[n], kind="speciation", at=1.0, token="neutral", size=0.34) for n in FRANK])
phylo.marker(ax, (21.0, 13.8), "dot", "positive", size=0.34)
bio.label(ax, (21.6, 13.8), "Rhizobial nodules (Fabaceae; Parasponia)", size="small", ha="left")
phylo.marker(ax, (21.0, 12.9), "speciation", "neutral", size=0.34)
bio.label(ax, (21.6, 12.9), "Frankia (actinorhizal) nodules in some genera", size="small", ha="left")
bio.label(ax, (21.0, 12.0), "Unmarked: no nodules", size="small", ha="left", color=bio.P.muted())
