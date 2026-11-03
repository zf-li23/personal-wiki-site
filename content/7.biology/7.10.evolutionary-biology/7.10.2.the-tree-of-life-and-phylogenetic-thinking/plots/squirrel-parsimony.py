"""Inferring a phylogeny by parsimony (Example 2.4.1). A: sequences of a short stretch of a
hemoglobin gene (hypothetical) in four squirrels: the ground squirrel (Spermophilus, outgroup) and three
species of Sciurus. Only sites 3 and 9 vary. B: the three possible rooted trees of the ingroup. On tree 1
the change T to A at site 3 (red bar) happens once, in the common ancestor of the eastern and western gray
squirrels; trees 2 and 3 need it twice. The change A to T at site 9 (blue bar) happens once on every tree.
Tree 1 requires 2 changes, trees 2 and 3 require 3, so parsimony chooses tree 1 (after Futuyma and
Kirkpatrick 2017, Fig. 2.10)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(26, 9.0)
bio.panel(ax, "A", (0.2, 8.9))
SEQ = [("1 Ground (outgroup)", "ATTAATGAA"), ("2 Fox", "ATTAATGAT"), ("3 Eastern gray", "ATAAATGAA"),
       ("4 Western gray", "ATAAATGAA")]
x0, y0 = 4.2, 7.6
for j in range(9):
    bio.label(ax, (x0 + 0.42 * j + (0.3 if j >= 3 else 0) + (0.3 if j >= 6 else 0), y0 + 0.65), str(j + 1), size="tiny",
              color=P.muted())
for i, (name, s) in enumerate(SEQ):
    y = y0 - 0.62 * i
    bio.label(ax, (x0 - 0.35, y), name, size="small", ha="right", italic=False)
    for j, c in enumerate(s):
        x = x0 + 0.42 * j + (0.3 if j >= 3 else 0) + (0.3 if j >= 6 else 0)
        vary = j in (2, 8)
        bio.label(ax, (x, y), c, size="small", bold=vary, color=(P.edge("negative") if j == 2 else P.edge("dna")) if (vary and c != SEQ[0][1][j]) else None)

bio.panel(ax, "B", (0.2, 5.3))
TREES = [("(1,(2,(3,4)G)I)R;", "Tree 1: 2 changes", [("G", "negative"), ("2", "dna")]),
         ("(1,(3,(2,4)G)I)R;", "Tree 2: 3 changes", [("3", "negative"), ("4", "negative"), ("2", "dna")]),
         ("(1,(4,(2,3)G)I)R;", "Tree 3: 3 changes", [("4", "negative"), ("3", "negative"), ("2", "dna")])]
for k, (nw, title, marks) in enumerate(TREES):
    ox = 1.2 + 8.4 * k
    phylo.tree(ax, nw, origin=(ox, 0.9), width=5.6, height=3.0, direction="up", label_size="small", root_edge=0.3,
               marks=[dict(node=n, kind="trait", at=0.5, token=tok, size=0.26) for n, tok in marks])
    bio.label(ax, (ox + 2.8, 5.0), title, size="small", bold=True)
bio.label(ax, (17.0, 7.6), "red bar: site 3, T to A", size="small", ha="left", color=P.edge("negative"))
bio.label(ax, (17.0, 7.0), "blue bar: site 9, A to T", size="small", ha="left", color=P.edge("dna"))
bio.label(ax, (17.0, 6.4), "tips: 1 ground, 2 fox, 3 eastern gray, 4 western gray", size="tiny", ha="left",
          color=P.muted())
