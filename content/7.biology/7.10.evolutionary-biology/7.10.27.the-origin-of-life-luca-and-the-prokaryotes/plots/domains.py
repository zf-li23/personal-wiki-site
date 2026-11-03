"""Three-domain tree (A) versus two-domain tree (B), cladograms; B places eukaryotes within Archaea as sister
to the Asgard archaea, with the mitochondrion from an alphaproteobacterium (dashed arrow)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8))
bio.panel(ax, "B", (12.2, 8.8))
A = "(Bacteria,(Archaea,Eukarya)n1)r;"
phylo.tree(ax, A, origin=(1.2, 2.0), width=6.0, height=5.0, root_edge=0.5, label_size="small",
           clades=[dict(tips=["Bacteria"], token="positive", style="branch"),
                   dict(tips=["Archaea"], token="rna", style="branch"),
                   dict(tips=["Eukarya"], token="dna", style="branch")])
bio.label(ax, (5.5, 1.2), "three domains (Woese et al. 1990)", size="small", color=P.muted())
B = "((Alphaproteobacteria,Other_bacteria)bac,(Other_archaea,(TACK_archaea,(Other_Asgard_archaea,(Heimdallarchaeia,Eukaryotes)he)asg)t)arc)r;"
t = phylo.tree(ax, B, origin=(13.0, 1.6), width=5.6, height=6.4, root_edge=0.5, label_size="small",
               clades=[dict(node="bac", token="positive", style="branch"),
                       dict(node="arc", token="rna", style="branch"),
                       dict(tips=["Eukaryotes"], token="dna", style="branch")])
xa, ya = t.node("Alphaproteobacteria").xy
xe, ye = t.node("Eukaryotes").xy
bio.arrow(ax, (xa + 3.6, ya), (xe + 2.8, ye - 0.15), kind="process", dashed=True, bend=-0.35,
          color=P.edge("positive"))
bio.label(ax, (xa + 3.1, (ya + ye) / 2 + 0.6), "mitochondrion", size="tiny", ha="left", color=P.edge("positive"))
bio.label(ax, (17.5, 0.9), "two domains: eukaryotes within the Archaea", size="small", color=P.muted())
