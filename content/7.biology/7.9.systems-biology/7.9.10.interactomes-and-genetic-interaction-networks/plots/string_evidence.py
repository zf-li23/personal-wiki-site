"""Combining evidence channels into one confidence score per protein pair (Formula 10.5.1; channel
scores are illustrative, not taken from a database). A: a small network of eight proteins; each
edge is labeled with its combined score S, computed from the channel scores after removing the
prior probability p = 0.041 that two random proteins are linked. Thick blue: S >= 0.7 (high
confidence); black: 0.4 <= S < 0.7 (medium); dashed grey: S < 0.4. B: the channels of the pair
A-B: no single channel exceeds 0.62, but four independent moderate channels combine to 0.93."""

import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G
import wikibio as bio
from wikibio import charts

P = bio.P
prior = 0.041
channels = ["neighborhood", "co-occurrence", "co-expression", "experiments", "databases", "text mining"]
pairs = {
    ("A", "B"): [0.0, 0.35, 0.48, 0.62, 0.0, 0.55],
    ("A", "C"): [0.0, 0.0, 0.30, 0.91, 0.90, 0.70],
    ("B", "C"): [0.0, 0.0, 0.25, 0.45, 0.0, 0.30],
    ("C", "D"): [0.0, 0.0, 0.0, 0.0, 0.0, 0.33],
    ("D", "E"): [0.45, 0.40, 0.20, 0.0, 0.0, 0.0],
    ("E", "F"): [0.0, 0.0, 0.0, 0.52, 0.0, 0.0],
    ("D", "F"): [0.0, 0.0, 0.18, 0.0, 0.0, 0.21],
    ("F", "G"): [0.0, 0.0, 0.62, 0.70, 0.80, 0.40],
    ("G", "H"): [0.0, 0.0, 0.0, 0.0, 0.0, 0.25],
    ("E", "G"): [0.0, 0.0, 0.35, 0.0, 0.0, 0.42],
}


def combine(s):
    s = np.asarray(s, float)
    s = np.clip((s - prior) / (1 - prior), 0, 1)       # remove the prior from each channel
    S = 1 - np.prod(1 - s)
    return S + prior * (1 - S)                          # add the prior back once


comb = {e: combine(v) for e, v in pairs.items()}
pos = {"A": (0.6, 2.4), "B": (0.0, 1.0), "C": (1.8, 1.6), "D": (3.2, 2.5), "E": (4.4, 1.6),
       "F": (4.0, 0.2), "G": (5.6, 0.5), "H": (6.6, 1.6)}

fig = plt.figure(figsize=(10.4, 3.6))
a = fig.add_axes([0.0, 0.02, 0.56, 0.9])
a.set_xlim(-0.5, 7.1)
a.set_ylim(-0.4, 3.0)
a.set_aspect("equal")
a.axis("off")
hi = [(u, v, f"{s:.2f}") for (u, v), s in comb.items() if s >= 0.7]
mid = [(u, v, f"{s:.2f}") for (u, v), s in comb.items() if 0.4 <= s < 0.7]
lo = [(u, v, f"{s:.2f}") for (u, v), s in comb.items() if s < 0.4]
G.draw(a, pos, lo, weights=True, vertices=False, edge_color=G.GREY, dashed=[e[:2] for e in lo])
G.draw(a, pos, mid, weights=True, vertices=False)
G.draw(a, pos, hi, weights=True, highlight={e[:2]: G.BLUE for e in hi})
a.set_title("A  Combined scores S", fontsize=9, loc="left", weight="bold", color=P.ink())

b = fig.add_axes([0.69, 0.18, 0.29, 0.7])
v = np.array(pairs[("A", "B")])
y = np.arange(len(channels) + 1)
vals = list(v) + [comb[("A", "B")]]
cols = [P.fill("neutral")] * len(channels) + [P.fill("dna")]
b.barh(y, vals, color=cols, edgecolor=[P.edge("neutral")] * len(channels) + [P.edge("dna")])
b.set_yticks(y, channels + ["combined"], fontsize=7)
b.invert_yaxis()
b.set_xlim(0, 1)
for yy, vv in zip(y, vals):
    b.text(vv + 0.02, yy, f"{vv:.2f}", va="center", fontsize=7, color=P.ink())
charts.style_axes(b, "score", None)
charts.title(b, "B  Channels of the pair A-B")
