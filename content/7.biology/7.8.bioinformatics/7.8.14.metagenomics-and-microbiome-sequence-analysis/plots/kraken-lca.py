# How a Kraken-style classifier labels one read. A: the read's 30 minimizers, coloured by the taxon stored for
# each in the database (the lowest common ancestor of all genomes containing it); 9 are not in the database.
# B: the hits placed on the taxonomy (counts in the boxes). The score of a root-to-leaf path is the sum of the
# hits on its nodes: 3 + 10 + 6 = 19 for Escherichia coli, 15 for Salmonella enterica, 3 for the two
# Bacillales species; the read is assigned to the leaf of the best path. With a confidence threshold of 0.7
# the label moves up the path until the hits in the clade below it reach 0.7 of all 30 minimizers: 6/30 for
# E. coli, 18/30 for the family, 21/30 for Bacteria, which becomes the label.
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 12.6)
seq = (["ecoli"] * 3 + ["none"] * 2 + ["entero"] * 4 + ["bact"] + ["entero"] * 3 + ["none"] * 3 + ["ecoli"] * 2
       + ["salm"] + ["entero"] * 3 + ["none"] * 2 + ["bact"] * 2 + ["ecoli"] + ["none"] * 2 + ["salm"])
tok = {"ecoli": "negative", "salm": "drug", "entero": "highlight", "bact": "dna", "none": "neutral"}
for i, s in enumerate(seq):
    x = 1.5 + i * 0.9
    ax.add_patch(Rectangle((x, 10.6), 0.8, 0.9, fc=P.fill(tok[s]) if s != "none" else "none",
                           ec=P.edge(tok[s]), lw=0.8))
bio.label(ax, (1.5 + 15 * 0.9, 12.1), "one read: 30 minimizers, each looked up in the database", size="small")
nodes = {"root": (14.5, 9.0, "root", "neutral", 0), "bact": (14.5, 7.2, "Bacteria", "dna", 3),
         "entero": (8.0, 5.0, "Enterobacteriaceae", "highlight", 10), "bacill": (21.0, 5.0, "Bacillales", "neutral", 0),
         "ecoli": (4.5, 2.6, "Escherichia coli", "negative", 6), "salm": (11.5, 2.6, "Salmonella enterica", "drug", 2),
         "bsub": (18.0, 2.6, "Bacillus subtilis", "neutral", 0), "saur": (24.5, 2.6, "Staphylococcus aureus", "neutral", 0)}
edges = [("root", "bact"), ("bact", "entero"), ("bact", "bacill"), ("entero", "ecoli"), ("entero", "salm"),
         ("bacill", "bsub"), ("bacill", "saur")]
for u, v in edges:
    (x0, y0), (x1, y1) = nodes[u][:2], nodes[v][:2]
    ax.plot([x0, x0, x1, x1], [y0 - 0.45, (y0 + y1) / 2, (y0 + y1) / 2, y1 + 0.45], color=P.muted(), lw=1.0)
for k, (x, y, name, t, hits) in nodes.items():
    italic = k in ("ecoli", "salm", "bsub", "saur")
    bio.box(ax, (x, y), 5.4 if italic else 4.4, 0.9, token=t, text=f"{name}: {hits}", size="small", italic=italic)
scores = {"ecoli": 19, "salm": 15, "bsub": 3, "saur": 3}
for k, sc in scores.items():
    x, y = nodes[k][:2]
    bio.label(ax, (x, y - 1.0), f"path score {sc}", size="tiny", bold=(k == "ecoli"))
bio.label(ax, (14.5, 0.6), "best path: score 19 of 30 minimizers, to the leftmost leaf; with confidence 0.7 the label is "
          "Bacteria (21/30 in its clade)", size="small")
bio.panel(ax, "A", (0.3, 12.2))
bio.panel(ax, "B", (0.3, 9.4))
