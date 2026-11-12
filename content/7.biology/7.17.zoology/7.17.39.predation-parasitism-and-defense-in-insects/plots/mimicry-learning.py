# Learning model of Batesian mimicry (Eq. 39.5): long-run attack probability on the shared pattern,
# q* = m / (m + (1 - m) beta/alpha), as a function of the proportion m of palatable mimics, for
# beta/alpha = 1, 4, 16. B: expected mimics killed (m q*) and models killed ((1 - m) q*) per 100 encounters.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22, 9.5)
m = np.linspace(0, 1, 400)
A = charts.axes_at(ax, (2.0, 1.5, 8.8, 7.0))
B = charts.axes_at(ax, (13.0, 1.5, 8.6, 7.0))
for r, tok, ls in [(1, "negative", "-"), (4, "enzyme", "--"), (16, "positive", "-.")]:
    q = m / (m + (1 - m) * r)
    A.plot(m, q, color=P.edge(tok), lw=1.8, ls=ls, label=f"beta/alpha = {r}")
    B.plot(m, 100 * m * q, color=P.edge(tok), lw=1.8, ls=ls)
    B.plot(m, 100 * (1 - m) * q, color=P.edge(tok), lw=1.0, ls=ls, alpha=0.6)
A.set_xlabel("Proportion of mimics among prey with the pattern, m")
A.set_ylabel("Long-run attack probability, q*")
A.set_title("A  Protection declines as mimics become common", fontsize=8, loc="left")
A.legend(fontsize=7, frameon=False, loc="upper left")
B.set_xlabel("Proportion of mimics, m")
B.set_ylabel("Killed per 100 encounters")
B.set_title("B  Mimics killed (thick) and models killed (thin)", fontsize=8, loc="left")
