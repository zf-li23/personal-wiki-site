# Solanaceae. A: floral diagram of Solanum: five sepals, five corolla lobes (plicate), five stamens
# alternating with the lobes and connivent, ovary of two carpels with two locules and swollen axile
# placentas bearing many ovules; the septum is oblique to the median plane (oblique ovary). B: relationships
# of some crops and weeds within Solanum, simplified after Sarkinen et al. (2013): the tomato clade (former
# Lycopersicon) and the potato clade are sisters; eggplant belongs to the spiny Leptostemonum clade; black
# nightshade to the Morelloid clade. Capsicum and Nicotiana are outgroups.
import wikibio as bio
from wikibio import phylo, plant

P = bio.P
fig, ax = bio.canvas(32, 13)
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (5.0, 12.2), r"$\it{Solanum}$ floral diagram", size="title")
plant.floral_diagram(ax, (5.0, 6.8), 3.6, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=40, connate=True),
    dict(organ="stamen", n=5, r=0.57, adnate=True),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=4, size=0.3, phase=30)], symmetry="radial")
plant.floral_formula(ax, (5.0, 1.6), "* K(5) C(5) A5 G_(2:2:∞)", style="cn", size="normal")
bio.label(ax, (5.0, 0.6), "Septum oblique to the median plane", size="small")

bio.panel(ax, "B", (11.5, 12.7))
bio.label(ax, (19.0, 12.2), r"Crops within $\it{Solanum}$", size="title")
NEWICK = ("(Nicotiana,(Capsicum,(((Tomato,Potato)PotatoClade,Nightshade)PM,Eggplant)Solanum)Solanoideae)Root;")
phylo.tree(ax, NEWICK, origin=(12.5, 1.5), width=9.0, height=9.5, label_size="small", root_edge=0.4,
           tip_text={"Nicotiana": r"Tobacco ($\it{Nicotiana\ tabacum}$)", "Capsicum": r"Chili pepper ($\it{Capsicum\ annuum}$)",
                     "Tomato": r"Tomato ($\it{S.\ lycopersicum}$)", "Potato": r"Potato ($\it{S.\ tuberosum}$)",
                     "Nightshade": r"Black nightshade ($\it{S.\ nigrum}$)", "Eggplant": r"Eggplant ($\it{S.\ melongena}$)"},
           icons={"Tomato": "phylopic/tomato"},
           clades=[dict(node="Solanum", token="rna", style=("bar",), label=r"$\it{Solanum}$"),
                   dict(node="PotatoClade", token="plant", style=("branch",), label="")],
           marks=[dict(node="Eggplant", kind="trait", at=0.5, token="negative", text="prickles"),
                  dict(node="Potato", kind="trait", at=0.5, token="atp", text="tubers")])
