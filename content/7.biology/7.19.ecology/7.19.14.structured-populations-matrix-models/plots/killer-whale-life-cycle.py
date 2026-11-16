"""Life cycle graph of the stage-classified killer whale model (Brault and Caswell 1993).

Nodes are the four stages of females (1 yearling, 2 juvenile, 3 reproductive adult, 4 post-reproductive
adult); each arrow j -> i is a non-zero entry a_ij of the projection matrix, labeled with its value: loops
are the probabilities of surviving and remaining in a stage, forward arrows the probabilities of surviving
and moving to the next stage, and the arrows back to stage 1 are fecundities (female yearlings per female
per year, including the survival of the calf to its first census). Stage 4 has no path back to stage 1, so
the matrix is reducible; the subgraph of stages 1-3 is strongly connected and has loops of lengths 1 and 2,
so its matrix is primitive.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 9.0)
xs = [3.0, 9.5, 16.0, 22.5]
y = 4.6
names = ["1  yearling", "2  juvenile", "3  reproductive", "4  post-repro."]
toks = ["atp", "enzyme", "dna", "protein"]
for x, nm, tok in zip(xs, names, toks):
    bio.box(ax, (x, y), 3.6, 1.3, token=tok, text=nm, size="small")


def lab(xy, text):
    bio.label(ax, xy, text, size="small", color=P.ink())


# forward transitions
for k, val in enumerate(["0.9775", "0.0736", "0.0452"]):
    bio.arrow(ax, (xs[k] + 1.85, y), (xs[k + 1] - 1.85, y), kind="process")
    lab(((xs[k] + xs[k + 1]) / 2, y + 0.45), val)
# loops (survive and stay)
for k, val in [(1, "0.9111"), (2, "0.9534"), (3, "0.9804")]:
    x = xs[k]
    bio.arrow(ax, (x - 0.8, y + 0.7), (x + 0.8, y + 0.7), kind="process", bend=0.9)
    lab((x, y + 1.6), val)
# fecundities back to stage 1
bio.arrow(ax, (xs[1], y - 0.7), (xs[0] + 0.4, y - 0.7), kind="process", bend=0.3, color=P.edge("rna"))
lab(((xs[0] + xs[1]) / 2 + 0.6, y - 0.95), "0.0043")
bio.arrow(ax, (xs[2], y - 0.7), (xs[0] - 0.4, y - 0.7), kind="process", bend=0.22, color=P.edge("rna"))
lab(((xs[0] + xs[2]) / 2, y - 2.5), "0.1132")
bio.label(ax, (22.5, 1.6), "fecundities: arrows back to stage 1", size="tiny", color=P.edge("rna"))
