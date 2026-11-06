# Caryophyllales, main families (APG IV; Soltis et al. 2018; Brockington et al. 2011, 2015; simplified).
# Columns of squares mark betalain pigments (B; anthocyanins in Caryophyllaceae and Molluginaceae),
# C4 photosynthesis (C4), CAM and carnivory (Cv) in each family (present in at least some members).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Polygonaceae,Plumbaginaceae),(Tamaricaceae,Frankeniaceae),((Droseraceae,Nepenthaceae),"
          "(Drosophyllaceae,(Ancistrocladaceae,Dioncophyllaceae)))Carnivorous)Noncore,"
          "(Simmondsiaceae,(Caryophyllaceae,(Amaranthaceae,(Aizoaceae,((Phytolaccaceae,Nyctaginaceae),"
          "(Molluginaceae,(Basellaceae,(Talinaceae,(Portulacaceae,Cactaceae))))))))Core))Caryophyllales;")
fig, ax = bio.canvas(32, 17)
t = phylo.tree(ax, NEWICK, origin=(1.0, 1.0), width=12.0, height=14.0, label_size="small", root_edge=0.4,
               clades=[dict(node="Noncore", token="neutral", style=("bar",), label="Non-core (Polygonineae)"),
                       dict(node="Core", token="rna", style=("bar",), label="Core Caryophyllales"),
                       dict(node="Carnivorous", token="positive", style=("branch",))])
TRAITS = {"Polygonaceae": [], "Plumbaginaceae": [], "Tamaricaceae": [], "Frankeniaceae": [],
          "Droseraceae": ["Cv"], "Nepenthaceae": ["Cv"], "Drosophyllaceae": ["Cv"], "Ancistrocladaceae": [],
          "Dioncophyllaceae": ["Cv"], "Simmondsiaceae": [], "Caryophyllaceae": [], "Amaranthaceae": ["B", "C4"],
          "Aizoaceae": ["B", "C4", "CAM"], "Phytolaccaceae": ["B"], "Nyctaginaceae": ["B", "C4"],
          "Molluginaceae": ["C4"], "Basellaceae": ["B"], "Talinaceae": ["B", "CAM"],
          "Portulacaceae": ["B", "C4", "CAM"], "Cactaceae": ["B", "CAM"]}
COLS = ["B", "C4", "CAM", "Cv"]
TOK = {"B": "petal", "C4": "plant", "CAM": "dna", "Cv": "rna"}
X0 = 25.6
for i, c in enumerate(COLS):
    bio.label(ax, (X0 + 1.3 * i, 15.6), c, size="small")
for tip in t.tips():
    y = tip.xy[1]
    for i, c in enumerate(COLS):
        if c in TRAITS[tip.name]:
            bio.box(ax, (X0 + 1.3 * i, y), 0.8, 0.45, token=TOK[c], radius=0.08)
        else:
            ax.plot([X0 + 1.3 * i - 0.2, X0 + 1.3 * i + 0.2], [y, y], color=P.muted(), lw=0.6)
KEY = ["B   betalains (others: anthocyanins)", "C4  C4 photosynthesis", "CAM crassulacean acid metabolism",
       "Cv  carnivory (green branches: carnivorous clade)"]
for i, k in enumerate(KEY):
    bio.label(ax, (1.0 + 7.2 * i, 0.2), k, size="tiny", ha="left")
