"""Reciprocity strategies in the iterated donation game with errors.

Each round a player either cooperates (pays c = 1, partner gains b = 3) or defects; after each round there is a
further round with probability w = 0.95, and every intended move is reversed by mistake with probability e. A
strategy is the probability of cooperating in the first round and after each outcome (own move, partner's move):
ALLD (always defect), TFT (copy the partner's last move), GTFT (generous TFT: like TFT but forgive a defection with
probability 1/3) and WSLS (win-stay, lose-shift: repeat the last move after a payoff of b - c or b, switch after
-c or 0). Expected payoffs over the whole game are computed exactly from the Markov chain of outcomes, and the
frequencies change by the discrete replicator equation.
A: with e = 0.01, starting from 90% ALLD and 10% TFT and a trace of the other two: TFT invades ALLD and is then
displaced by more forgiving strategies. B: the same with e = 0.05. C: the average payoff per round in a
population of a single strategy, against the error rate: errors make TFT pairs fall into alternating retaliation.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
b, c, w = 3.0, 1.0, 0.95
# (first, CC, CD, DC, DD): probability of cooperating; state = (own last, partner's last)
S = {"ALLD": (0, 0, 0, 0, 0), "TFT": (1, 1, 0, 1, 0), "GTFT": (1, 1, 1 / 3, 1, 1 / 3), "WSLS": (1, 1, 0, 0, 1)}
names = ["ALLD", "TFT", "GTFT", "WSLS"]
toks = {"ALLD": "negative", "TFT": "dna", "GTFT": "positive", "WSLS": "protein"}
u = np.array([b - c, -c, b, 0.0])  # payoff to player 1 in states CC, CD, DC, DD


def payoff(s1, s2, e):
    f = lambda q: q * (1 - e) + (1 - q) * e  # noqa: E731
    p1 = [f(x) for x in s1]
    p2 = [f(x) for x in s2]
    # player 2 sees states mirrored: CD for player 1 is DC for player 2
    mirror = [1, 3, 2, 4]
    v0 = np.array([p1[0] * p2[0], p1[0] * (1 - p2[0]), (1 - p1[0]) * p2[0], (1 - p1[0]) * (1 - p2[0])])
    M = np.zeros((4, 4))
    for i in range(4):
        a, bb = p1[i + 1], p2[mirror[i]]
        M[i] = [a * bb, a * (1 - bb), (1 - a) * bb, (1 - a) * (1 - bb)]
    tot = v0 @ np.linalg.inv(np.eye(4) - w * M) @ u
    return tot * (1 - w)  # average payoff per round


def run(e, x0, gens=400):
    A = np.array([[payoff(S[i], S[j], e) for j in names] for i in names])
    x = np.array(x0, float)
    xs = [x.copy()]
    for _ in range(gens):
        f = A @ x + 2.0  # baseline fitness keeps it positive
        x = x * f / (x @ f)
        xs.append(x.copy())
    return np.array(xs)


fig, ax = bio.canvas(33.0, 10.0)
x0 = [0.9, 0.09, 0.005, 0.005]
for k, (e, letter) in enumerate(((0.01, "A"), (0.05, "B"))):
    pa = Ch.axes_at(ax, (2.2 + 10.6 * k, 1.8, 8.2, 7.0))
    xs = run(e, x0)
    for j, n in enumerate(names):
        pa.plot(xs[:, j], color=Ch.line(toks[n]), lw=1.6)
    Ch.style_axes(pa, "generations", "frequency" if k == 0 else None)
    Ch.title(pa, f"error rate e = {e:g}")
    pa.set_ylim(0, 1.02)
    pa.set_xlim(0, 400)
    bio.panel(ax, letter, (0.3 + 10.6 * k, 9.8))
for j, n in enumerate(names):
    bio.label(ax, (3.5 + 2.2 * j, 0.25), n, size="tiny", color=Ch.line(toks[n]), bold=True)

pc = Ch.axes_at(ax, (24.4, 1.8, 8.0, 7.0))
es = np.linspace(0.0, 0.2, 60)
for n in names:
    pc.plot(es, [payoff(S[n], S[n], e) for e in es], color=Ch.line(toks[n]), lw=1.6)
pc.axhline(b - c, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pc.text(0.2, b - c + 0.05, "full cooperation b − c", fontsize=FS["tiny"], color=P.muted(), ha="right", va="bottom")
pc.set_xlim(0, 0.2)
pc.set_ylim(-0.1, 2.3)
Ch.style_axes(pc, "error rate e", "payoff per round against itself")
bio.panel(ax, "C", (22.3, 9.8))
