# Resistance evolution with a refuge (Formula 40.6.1): fitnesses w_RR = 1, w_RS = 1 - (1 - f)(1 - h) s (h = dominance of resistance),
# w_SS = 1 - (1 - f) s, random mating, s = 0.95, initial q = 0.001. A: trajectories; B: generations to q = 0.5.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
s, q0 = 0.95, 0.001


def traj(f, h, T=400):
    q, out = q0, [q0]
    for _ in range(T):
        pp = 1 - q
        wrr, wrs, wss = 1.0, 1 - (1 - f) * (1 - h) * s, 1 - (1 - f) * s
        wbar = q * q * wrr + 2 * pp * q * wrs + pp * pp * wss
        q = (q * q * wrr + pp * q * wrs) / wbar
        out.append(q)
    return np.array(out)


def gens(f, h, T=5000):
    q = traj(f, h, T)
    i = np.argmax(q >= 0.5)
    return i if q[i] >= 0.5 else np.nan


fig, ax = bio.canvas(22, 9.5)
A = charts.axes_at(ax, (2.0, 1.5, 9.2, 7.0))
for f, h, tok, ls in [(0, 0.5, "negative", "-"), (0.2, 0.5, "negative", "--"), (0, 0.0, "positive", "-"), (0.2, 0.0, "positive", "--")]:
    A.plot(traj(f, h, 400), color=P.edge(tok), lw=1.6, ls=ls, label=f"refuge {int(f * 100)}%, h = {h}")
A.set_xlabel("Generation")
A.set_ylabel("Resistance allele frequency")
A.set_xlim(0, 400)
A.legend(fontsize=7, frameon=False, loc="center right")
A.set_title("A  Spread of a resistance allele", fontsize=8, loc="left")
B = charts.axes_at(ax, (13.6, 1.5, 8.0, 7.0))
fs = np.linspace(0, 0.5, 26)
for h, tok in [(0.0, "positive"), (0.1, "enzyme"), (0.5, "negative")]:
    B.semilogy(fs * 100, [gens(f, h) for f in fs], "o-", ms=3, color=P.edge(tok), lw=1.4, label=f"h = {h}")
B.set_xlabel("Refuge (% of population untreated)")
B.set_ylabel("Generations to q = 0.5")
B.legend(fontsize=7, frameon=False, loc="upper left")
B.set_title("B  Delay of resistance", fontsize=8, loc="left")
