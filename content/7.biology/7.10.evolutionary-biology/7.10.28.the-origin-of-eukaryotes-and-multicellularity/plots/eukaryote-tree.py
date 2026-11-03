"""Major groups of eukaryotes (cladogram after Burki et al. 2020; polytomies for unresolved relationships).
Filled dots: complex multicellularity; open dots: simple multicellular or aggregative forms; star: primary
plastid; triangles: secondary plastids."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(22, 12)
NW = ("((((Animals,Choanoflagellates)Holozoa,Fungi,Breviates_and_apusomonads)Obazoa,Amoebozoa)Amorphea,"
      "CRuMs,((Land_plants_and_green_algae,Red_algae,Glaucophytes)Archaeplastida,Cryptista,"
      "(Stramenopiles,Alveolata,Rhizaria)SAR,Haptista)Diaphoretickes,Discoba,Metamonada,"
      "Hemimastigophora_and_Provora)Eukaryotes;")
t = phylo.tree(ax, NW, origin=(1.0, 0.8), width=9.0, height=10.6, label_size="small",
               clades=[dict(node="Amorphea", token="animal", style="branch"),
                       dict(node="Diaphoretickes", token="plant", style="branch")])
multi = {"Animals": True, "Fungi": True, "Land plants and green algae": True, "Red algae": True,
         "Stramenopiles": True, "Amoebozoa": False, "Alveolata": False, "Rhizaria": False, "Discoba": False}
for name, full in multi.items():
    x, y = t.node(name).xy
    ax.plot([x + 7.6], [y], "o", ms=8, color=P.edge("highlight"), markerfacecolor=P.edge("highlight") if full else "none",
            mew=1.5, zorder=12)
x, y = t.node("Archaeplastida").xy
ax.plot([x - 0.3], [y], marker="*", ms=14, color=P.edge("positive"), zorder=13)
for name in ("Cryptista", "Stramenopiles", "Alveolata", "Rhizaria", "Haptista"):
    xx, yy = t.node(name).xy
    ax.plot([xx + 8.2], [yy], marker="^", ms=7, color=P.edge("rna"), zorder=12)
ax.plot([18.6], [1.2], "o", ms=8, color=P.edge("highlight")); bio.label(ax, (18.9, 1.2), "complex multicellular", size="tiny", ha="left")
ax.plot([18.6], [0.7], "o", ms=8, color=P.edge("highlight"), markerfacecolor="none", mew=1.5)
bio.label(ax, (18.9, 0.7), "simple / aggregative", size="tiny", ha="left")
ax.plot([18.6], [1.7], "^", ms=7, color=P.edge("rna")); bio.label(ax, (18.9, 1.7), "secondary plastid", size="tiny", ha="left")
ax.plot([18.6], [2.2], "*", ms=12, color=P.edge("positive")); bio.label(ax, (18.9, 2.2), "primary plastid", size="tiny", ha="left")
