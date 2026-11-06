# Where the members of the broad Saxifragaceae (Engler) went in APG IV. An order-level tree of the core
# eudicots (simplified: only orders that received former Saxifragaceae plus a few landmarks); dots mark
# orders containing former members, with the APG IV families named on the right.
import wikibio as bio
from wikibio import phylo

NEWICK = ("(Gunnerales,((Saxifragales,(Vitales,((Celastrales,Oxalidales)COM,Rosales)Fabids,"
          "(Geraniales,Sapindales)Malvids)Rosids)Superrosids,"
          "(Caryophyllales,((Cornales,Ericales),((Vahliales,(Solanales,Lamiales))Lamiids,"
          "(Aquifoliales,(Escalloniales,Asterales))Campanulids)))Superasterids)Pentapetalae)Core;")
HIT = ["Saxifragales", "Celastrales", "Oxalidales", "Geraniales", "Cornales", "Vahliales", "Solanales",
       "Aquifoliales", "Escalloniales", "Asterales"]
FAM = {"Saxifragales": "Saxifragaceae s.s., Grossulariaceae, Iteaceae, Penthoraceae, Tetracarpaeaceae",
       "Celastrales": r"Celastraceae ($\it{Parnassia}$, $\it{Brexia}$)",
       "Oxalidales": r"Cunoniaceae ($\it{Bauera}$)",
       "Geraniales": r"Francoaceae ($\it{Francoa}$)",
       "Cornales": r"Hydrangeaceae ($\it{Hydrangea}$, $\it{Philadelphus}$, $\it{Deutzia}$)",
       "Vahliales": r"Vahliaceae ($\it{Vahlia}$)",
       "Solanales": r"Montiniaceae ($\it{Montinia}$)",
       "Aquifoliales": r"Phyllonomaceae ($\it{Phyllonoma}$)",
       "Escalloniales": r"Escalloniaceae ($\it{Escallonia}$, $\it{Eremosyne}$)",
       "Asterales": r"Argophyllaceae ($\it{Argophyllum}$)"}
fig, ax = bio.canvas(34, 15)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.6), width=10.5, height=13.6, label_size="small", root_edge=0.4,
               clades=[dict(node="Superrosids", token="petal", style="bar", label="Superrosids"),
                       dict(node="Superasterids", token="plant", style="bar", label="Superasterids")],
               marks=[dict(node=[n], kind="dot", at=1.0, token="highlight", size=0.32) for n in HIT])
tips = [n.name for n in phylo.parse(NEWICK).leaves()]
ys = {name: 0.6 + 13.6 * (len(tips) - 1 - i) / (len(tips) - 1) for i, name in enumerate(tips)}
for n in HIT:
    bio.label(ax, (19.0, ys[n]), FAM[n], size="small", ha="left", italic=False)
bio.label(ax, (19.0, 14.6), "Former members of the broad Saxifragaceae (APG IV family)", size="normal",
          ha="left", bold=True)
