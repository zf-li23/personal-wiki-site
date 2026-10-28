"""Inbreeding coefficient by path counting. The child (IV-1) of first cousins III-1 and III-2 has two common
ancestors, I-1 and I-2. Each inbreeding loop runs from one parent of the child up to a common ancestor and down
to the other parent and contains n = 5 individuals (III-1, II-2, I-k, II-3, III-2), contributing (1/2)^5; so
F = 2 (1/2)^5 = 1/16."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(16.5, 8.6)
p = G.Pedigree()
p.person("I1", "M"); p.person("I2", "F")
p.person("II1", "F"); p.person("II2", "M"); p.person("II3", "F"); p.person("II4", "M")
p.union("I1", "I2", children=["II2", "II3"])
p.person("III1", "M"); p.person("III2", "F")
p.union("II1", "II2", children=["III1"])
p.union("II3", "II4", children=["III2"])
p.person("IV1", "U", text="?")
p.union("III1", "III2", children=["IV1"], consanguineous=True)
pos = G.pedigree(ax, p, origin=(3.0, 7.6), dx=1.9, dy=2.0, size=0.6)
path = ["III1", "II2", "I1", "II3", "III2"]
for a, b in zip(path, path[1:]):
    (x0, y0), (x1, y1) = pos[a], pos[b]
    bio.arrow(ax, (x0 - 0.35, y0 + (0.4 if y1 > y0 else -0.4)), (x1 - 0.35, y1 - (0.45 if y1 > y0 else -0.45)),
              kind="process", color=P.edge("receptor"), lw=1.6, head=0.2, bend=0.0)
path2 = ["III1", "II2", "I2", "II3", "III2"]
for a, b in zip(path2, path2[1:]):
    (x0, y0), (x1, y1) = pos[a], pos[b]
    bio.arrow(ax, (x0 + 0.35, y0 + (0.4 if y1 > y0 else -0.4)), (x1 + 0.35, y1 - (0.45 if y1 > y0 else -0.45)),
              kind="process", color=P.edge("dna"), lw=1.6, head=0.2, dashed=True)
bio.label(ax, (11.8, 7.4), "loop through I-1: $(1/2)^5$", size="small", color=P.edge("receptor"), ha="left")
bio.label(ax, (11.8, 6.8), "loop through I-2: $(1/2)^5$", size="small", color=P.edge("dna"), ha="left")
bio.label(ax, (11.8, 6.0), "$F = 2\\,(1/2)^5 = 1/16$", size="normal", bold=True, ha="left")
