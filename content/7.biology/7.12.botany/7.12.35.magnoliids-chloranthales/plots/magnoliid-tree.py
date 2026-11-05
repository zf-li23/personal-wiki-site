# Relationships of the magnoliids and Chloranthales at family level (APG IV; Soltis et al. 2018; Massoni
# et al. 2014). Magnoliids comprise two pairs of sister orders, Canellales + Piperales and Magnoliales +
# Laurales; Chloranthales are sister to the magnoliids in most plastid analyses but unplaced in APG IV.
# Marks: ethereal-oil cells; perigynous flowers (floral cup) in Laurales; scattered vascular bundles and
# reduced flowers in Piperales; loss of vessels in Winteraceae (and in Sarcandra, Chloranthaceae).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Chloranthaceae,(((Canellaceae,Winteraceae)Canellales,((Saururaceae,Piperaceae),Aristolochiaceae)Piperales)CP,"
          "((Myristicaceae,(Magnoliaceae,((Degeneriaceae,Himantandraceae),(Eupomatiaceae,Annonaceae))))Magnoliales,"
          "(Calycanthaceae,((Siparunaceae,(Gomortegaceae,Atherospermataceae)),(Hernandiaceae,(Monimiaceae,Lauraceae))))"
          "Laurales)ML)Magnoliids)Root;")
fig, ax = bio.canvas(26, 15)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=11.5, height=13.2, label_size="small", root_edge=0.5,
               clades=[dict(node="Canellales", token="neutral", style=("bar", "branch"), label="Canellales"),
                       dict(node="Piperales", token="rna", style=("bar", "branch"), label="Piperales"),
                       dict(node="Magnoliales", token="petal", style=("bar", "branch"), label="Magnoliales"),
                       dict(node="Laurales", token="plant", style=("bar", "branch"), label="Laurales"),
                       dict(tips=["Chloranthaceae"], token="atp", style=("bar", "branch"),
                            label="Chloranthales (position uncertain)")],
               marks=[dict(node="Magnoliids", kind="star", at=0.5, token="highlight", text="1"),
                      dict(node="Laurales", kind="trait", at=0.5, token="plant", text="2"),
                      dict(node="Piperales", kind="trait", at=0.5, token="rna", text="3"),
                      dict(node="Winteraceae", kind="loss", at=0.5, text="4")])
KEY = ["1  Magnoliids: oil cells, P-type sieve-element plastids",
       "2  Perigynous flowers (floral cup); valvate anthers (most)",
       "3  Scattered vascular bundles; flowers reduced",
       "4  Loss of vessels"]
for i, k in enumerate(KEY):
    bio.label(ax, (17.4, 4.4 - i * 0.9), k, size="small", ha="left")
