# Traditional "pseudocoelomate" phyla (highlighted) on the current protostome tree (simplified; after
# Laumer et al. 2019, Marletaz et al. 2019).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Nematoda,Nematomorpha)Nematoida,((Priapulida,(Kinorhyncha,Loricifera))Scalidophora,(Tardigrada,(Onychophora,Arthropoda))))Ecdysozoa,"
          "((Chaetognatha,(Gnathostomulida,(Micrognathozoa,(Rotifera,Acanthocephala)Syndermata))Gnathifera),"
          "((Platyhelminthes,Gastrotricha)Rouphozoa,((Entoprocta,Cycliophora),(Mollusca,Annelida,Nemertea,Lophophorata))))Spiralia)Protostomia;")
PSEUDO = ["Nematoda", "Nematomorpha", "Priapulida", "Kinorhyncha", "Loricifera", "Rotifera", "Acanthocephala", "Gastrotricha",
          "Entoprocta", "Cycliophora", "Gnathostomulida"]
fig, ax = bio.canvas(16, 15.0)
phylo.tree(ax, NEWICK, origin=(0.8, 1.2), width=8.2, height=13.0, root_edge=0.5, label_size="small",
           marks=[dict(node=t, kind="dot", token="highlight", at=1.0, size=0.32) for t in PSEUDO],
           clades=[dict(node="Ecdysozoa", token="atp", style="bar", label="Ecdysozoa"),
                   dict(node="Spiralia", token="positive", style="bar", label="Spiralia")])
phylo.marker(ax, (1.0, 0.45), "dot", token="highlight", size=0.32)
bio.label(ax, (1.5, 0.45), 'Phyla once placed among the "pseudocoelomates" (Aschelminthes)', size="small", ha="left")
