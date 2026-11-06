"""Similar forms on the APG IV tree: a simplified cladogram of selected angiosperm families (after APG IV and
Soltis et al. 2018; branch lengths are not to scale). Letters mark the families with a lotus-like aquatic
habit (A), cactus-like stem succulence (S), carnivory (C), parasitism (P) and catkins with wind
pollination (W). Each letter appears on distant branches: the similarities are convergent, while the
carnivory of the sundews and pitcher plants, and the catkins of Fagales, arose once in each common ancestor."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Nymphaeaceae,(Magnoliaceae,(Nelumbonaceae,((Euphorbiaceae,Salicaceae,Rafflesiaceae)Malpighiales,"
          "(Fagaceae,Betulaceae,Juglandaceae)Fagales)Fabids,(Loranthaceae,((Droseraceae,Nepenthaceae)Carn,"
          "Cactaceae)Caryophyllales,(Sarraceniaceae,(Apocynaceae,Convolvulaceae,(Lentibulariaceae,"
          "Orobanchaceae)Lamiales)Lamiids)Asterids)Superasterids)Eudicots)Mesangiosperms)Angiosperms;")
TRAIT = {  # tip: (letter, example genera, order)
    "Nymphaeaceae": ("A", "Nymphaea, Euryale", "Nymphaeales"),
    "Magnoliaceae": ("", "Magnolia", "Magnoliales"),
    "Nelumbonaceae": ("A", "Nelumbo", "Proteales"),
    "Euphorbiaceae": ("S", "Euphorbia", "Malpighiales"),
    "Salicaceae": ("W", "Salix, Populus", "Malpighiales"),
    "Rafflesiaceae": ("P", "Rafflesia", "Malpighiales"),
    "Fagaceae": ("W", "Quercus, Castanea", "Fagales"),
    "Betulaceae": ("W", "Betula, Alnus", "Fagales"),
    "Juglandaceae": ("W", "Juglans", "Fagales"),
    "Loranthaceae": ("P", "Loranthus, Taxillus", "Santalales"),
    "Droseraceae": ("C", "Drosera, Dionaea", "Caryophyllales"),
    "Nepenthaceae": ("C", "Nepenthes", "Caryophyllales"),
    "Cactaceae": ("S", "Opuntia, Carnegiea", "Caryophyllales"),
    "Sarraceniaceae": ("C", "Sarracenia", "Ericales"),
    "Apocynaceae": ("S", "Stapelia (stapeliads)", "Gentianales"),
    "Convolvulaceae": ("P", "Cuscuta", "Solanales"),
    "Lentibulariaceae": ("C", "Utricularia, Pinguicula", "Lamiales"),
    "Orobanchaceae": ("P", "Orobanche, Pedicularis", "Lamiales"),
}
TOK = {"A": "dna", "S": "neutral", "C": "negative", "P": "animal", "W": "bract"}
KEY = {"A": "lotus-like aquatic habit", "S": "cactus-like stem succulent", "C": "carnivorous",
       "P": "parasitic", "W": "catkins, wind pollination"}

fig, ax = bio.canvas(28, 15.5)
TOP, BOT = 14.0, 2.2
marks = [dict(node=tip, kind="trait", text=v[0], token=TOK[v[0]], at=0.55, text_size="tiny")
         for tip, v in TRAIT.items() if v[0] and tip not in ("Droseraceae", "Nepenthaceae", "Fagaceae", "Betulaceae", "Juglandaceae")]
marks += [dict(node="Carn", kind="trait", text="C", token=TOK["C"], at=0.5, text_size="tiny"),
          dict(node="Fagales", kind="trait", text="W", token=TOK["W"], at=0.5, text_size="tiny")]
t = phylo.tree(ax, NEWICK, origin=(0.6, BOT), width=10.5, height=TOP - BOT, direction="right", root_edge=0.3,
               label_size="small", marks=marks,
               clades=[dict(node="Eudicots", token="plant", style="bar", label="Eudicots"),
                       dict(node="Superasterids", token="petal", style="bar", label="Superasterids"),
                       dict(node="Fabids", token="ovule", style="bar", label="Fabids")])
XG, XO = 20.4, 25.0
bio.label(ax, (XG, TOP + 0.8), "Examples", size="small", bold=True, ha="left")
bio.label(ax, (XO, TOP + 0.8), "Order", size="small", bold=True, ha="left")
for tip in t.tips():
    _, gen, order = TRAIT[tip.name]
    bio.label(ax, (XG, tip.xy[1]), gen.replace(" (stapeliads)", ""), size="small", ha="left", italic=True)
    bio.label(ax, (XO, tip.xy[1]), order, size="small", ha="left", color=P.muted())
x = 0.8
for k, (letter, text) in enumerate(KEY.items()):
    phylo.marker(ax, (x + 0.15, 0.9), "trait", token=TOK[letter])
    bio.label(ax, (x + 0.15, 1.45), letter, size="small", bold=True)
    bio.label(ax, (x + 0.55, 0.9), text, size="small", ha="left")
    x += 5.3
