"""Four kinds of biological network and the meaning of their edges. A: a transcriptional regulatory
network (directed, signed): the arabinose and lactose systems of E. coli, with activation (green)
and repression (red). B: a protein-interaction network (undirected): physical binding, with a hub.
C: a metabolic network drawn as a bipartite graph of metabolites (circles) and reactions (blue),
the first steps of glycolysis with ATP and ADP as co-substrates. D: a genetic-interaction network
(undirected, signed): negative interactions (red, dashed: synthetic sickness or lethality) and
positive ones (green)."""

import wikigraph as G

fig, axes = G.panels(4, 4.2, 3.6, titles=["A  Transcriptional regulation", "B  Protein interaction",
                                          "C  Metabolism", "D  Genetic interaction"])

# A: CRP and AraC activate araBAD (a feed-forward loop), LacI represses lacZYA
ax = axes[0]
pos = {"CRP": (2.1, 3.2), "AraC": (0.7, 1.7), "araB": (2.1, 0.3), "LacI": (3.9, 1.7), "lacZ": (3.4, 0.3)}
G.draw(ax, pos, [("CRP", "AraC"), ("CRP", "araB"), ("AraC", "araB"), ("CRP", "lacZ"), ("LacI", "lacZ")],
       directed=True, radius=0.42,
       highlight={("CRP", "AraC"): G.GREEN, ("CRP", "araB"): G.GREEN, ("AraC", "araB"): G.GREEN,
                  ("CRP", "lacZ"): G.GREEN, ("LacI", "lacZ"): G.RED},
       vertex_labels={"araB": "araBAD", "lacZ": "lacZYA"})

# B: an undirected interaction graph with one hub
ax = axes[1]
pos = G.circle([f"P{i}" for i in range(1, 9)], radius=1.55, center=(2.1, 1.7))
pos["H"] = (2.1, 1.7)
edges = [("H", f"P{i}") for i in range(1, 9)] + [("P1", "P2"), ("P2", "P3"), ("P5", "P6"), ("P7", "P8"), ("P8", "P1")]
G.draw(ax, pos, edges, vertex_color={"H": G.AMBER}, radius=0.3)

# C: bipartite metabolite-reaction graph
ax = axes[2]
pos = {"Glc": (0.2, 3.2), "HK": (1.3, 3.2), "G6P": (2.4, 3.2), "PGI": (3.6, 3.2), "F6P": (3.6, 0.4),
       "PFK": (2.4, 0.4), "FBP": (1.0, 0.4), "ATP": (1.0, 1.8), "ADP": (2.7, 1.8)}
edges = [("Glc", "HK"), ("HK", "G6P"), ("G6P", "PGI"), ("PGI", "F6P"), ("F6P", "PFK"), ("PFK", "FBP"),
         ("ATP", "HK"), ("HK", "ADP"), ("ATP", "PFK"), ("PFK", "ADP")]
G.draw(ax, pos, edges, directed=True, radius=0.36,
       vertex_color={"HK": G.BLUE, "PGI": G.BLUE, "PFK": G.BLUE},
       vertex_labels={"FBP": "F16BP"})

# D: signed genetic interactions among six genes
ax = axes[3]
pos = {"g1": (0.6, 3.0), "g2": (2.1, 3.0), "g3": (3.6, 3.0), "g4": (0.6, 0.5), "g5": (2.1, 0.5), "g6": (3.6, 0.5)}
neg = [("g1", "g2"), ("g1", "g4"), ("g2", "g5"), ("g3", "g6")]
posi = [("g4", "g5"), ("g2", "g3")]
G.draw(ax, pos, neg + posi, radius=0.3,
       highlight={**{e: G.RED for e in neg}, **{e: G.GREEN for e in posi}}, dashed=set(neg))
