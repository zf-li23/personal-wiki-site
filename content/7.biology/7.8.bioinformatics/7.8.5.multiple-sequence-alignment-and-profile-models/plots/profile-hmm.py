# The architecture of a profile hidden Markov model (Krogh and colleagues 1994; the Plan7 form of HMMER),
# drawn for a model of four match columns. Match states M1-M4 (squares) emit residues with the position-
# specific probabilities of their alignment columns; insert states I0-I4 (diamonds) emit residues with
# background-like probabilities and can repeat (self-loops), modeling insertions relative to the family;
# delete states D1-D4 (circles) are silent and skip a column. Arrows are the allowed transitions: from M to
# M, I or D; from I to I or M; from D to D or M (Plan7 has no I-D or D-I transitions). The highlighted path
# aligns a sequence that has two inserted residues after column 2 and lacks column 4.
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 9.0)
K = 4
dx = 4.4
x0 = 4.4
yM, yI, yD = 3.6, 6.4, 1.0
r = 0.62


def pos(s):
    kind, k = s[0], int(s[1:]) if s[1:].isdigit() else None
    if s == "B":
        return (x0 - dx * 0.75, yM)
    if s == "E":
        return (x0 + dx * (K - 1) + dx * 0.75, yM)
    xk = x0 + dx * (k - 1)
    return {"M": (xk, yM), "D": (xk, yD), "I": (xk + dx / 2, yI)}[kind]


on = {("B", "M1"), ("M1", "M2"), ("M2", "I2"), ("I2", "I2"), ("I2", "M3"), ("M3", "D4"), ("D4", "E")}
edges = [("B", "M1"), ("B", "D1"), ("B", "I0")]
for k in range(1, K + 1):
    nxt = [f"M{k + 1}", f"D{k + 1}"] if k < K else ["E"]
    edges += [(f"M{k}", n) for n in nxt] + [(f"M{k}", f"I{k}")] * (k < K)
    edges += [(f"D{k}", n) for n in nxt]
for k in range(0, K):
    edges += [(f"I{k}", f"M{k + 1}")]
for a, b in edges:
    pa, pb = pos(a), pos(b) if b != "I0" else (x0 - dx / 2, yI)
    if a == "I0":
        pa = (x0 - dx / 2, yI)
    hot = (a, b) in on
    bio.arrow(ax, pa, pb, kind="process", shrink=0.72, color=C if False else (P.edge("negative") if hot else P.muted()),
              lw=2.0 if hot else 0.9, head=0.2)
for k in range(1, K + 1):
    x, _ = pos(f"M{k}")
    ax.add_patch(Rectangle((x - r, yM - r), 2 * r, 2 * r, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.2, zorder=10))
    bio.label(ax, (x, yM), f"M{k}", size="small", color=P.on_fill(), bold=True)
    ax.add_patch(Circle((x, yD), r * 0.9, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.2, zorder=10))
    bio.label(ax, (x, yD), f"D{k}", size="small", color=P.on_fill(), bold=True)
for k in range(0, K):
    x = x0 + dx * (k - 1) + dx / 2 if k > 0 else x0 - dx / 2
    if k > 0:
        x = x0 + dx * (k - 1) + dx / 2
    ax.add_patch(Polygon([(x, yI + r * 1.1), (x + r * 1.1, yI), (x, yI - r * 1.1), (x - r * 1.1, yI)],
                         facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.2, zorder=10))
    bio.label(ax, (x, yI), f"I{k}", size="small", color=P.on_fill(), bold=True)
    tok = P.edge("negative") if k == 2 else P.muted()
    ax.add_patch(__import__("matplotlib.patches", fromlist=["x"]).Arc((x, yI + r * 1.5), 0.9, 0.9, theta1=-60, theta2=240,
                                                                      color=tok, lw=2.0 if k == 2 else 0.9))
for s, txt in [("B", "Begin"), ("E", "End")]:
    x, y = pos(s)
    ax.add_patch(Rectangle((x - r, y - r * 0.7), 2 * r, 1.4 * r, facecolor=P.surface(), edgecolor=P.ink(), lw=1.0, zorder=10))
    bio.label(ax, (x, y), txt, size="tiny")
bio.label(ax, (23.4, 8.3), "insert: emits background-like residues", size="tiny", color=P.edge("dna"), ha="right")
bio.label(ax, (23.4, 4.75), "match: emits column-specific residues", size="tiny", color=P.edge("protein"), ha="right")
bio.label(ax, (23.4, 0.05), "delete: silent, skips a column", size="tiny", color=P.edge("neutral"), ha="right")
bio.label(ax, (12.0, 8.6), "path of a sequence with an insertion of two residues after column 2 and without column 4 (red)", size="tiny",
          color=P.edge("negative"))
