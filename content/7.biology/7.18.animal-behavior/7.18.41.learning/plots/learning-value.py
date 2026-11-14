# When does learning pay? A simple version of Stephens' (1991) model of the value of learning.
# The environment has two states, and the best action matches the current state. Within a lifetime of
# T = 20 periods the state persists from one period to the next with probability p (within-generation
# predictability); the state at birth equals the state the parent was born into with probability q
# (between-generation predictability). A fixed (innate) strategy performs the action that was best at the
# parent's birth for the whole life; a learner samples the state and then always performs the action that
# was best in the previous period, at a cost c per period (the mean payoff is a fraction of periods with
# the right action). A: the region of the (p, q) plane where learning beats the innate strategy, for
# c = 0.05 and c = 0.15. B: payoffs along two slices (q = 0.6 and q = 0.95) for c = 0.05.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
T = 20
t = np.arange(T)


def innate(p, q):
    m = np.mean((1 + (2 * p - 1) ** t) / 2)  # P(state at time t equals the state at birth)
    return q * m + (1 - q) * (1 - m)


def learner(p, c):
    return (0.5 + (T - 1) * p) / T - c


def boundary(p, c):
    m = np.mean((1 + (2 * p - 1) ** t) / 2)
    return (learner(p, c) - (1 - m)) / (2 * m - 1)


ps = np.linspace(0.5, 1.0, 201)[1:]
fig, ax = bio.canvas(21.0, 9.6)

pa = quant.Plot(ax, (2.0, 1.8, 7.2, 6.6), (0.5, 1.0), (0.5, 1.0), xlabel="Within-life predictability p",
                ylabel="Between-generation predictability q", xticks=[0.5, 0.75, 1.0], yticks=[0.5, 0.75, 1.0])
bio.panel(ax, "A", (0.2, 9.4))
for c, tok, dash in ((0.05, "dna", False), (0.15, "rna", True)):
    qb = np.array([boundary(p, c) for p in ps])
    if c == 0.05:
        pa.band(ps, np.full_like(ps, 0.5), np.clip(qb, 0.5, 1.0), "positive", alpha=0.28)
    inside = np.where((qb > 0.5) & (qb < 1.0), qb, np.nan)
    pa.line(ps, inside, tok, lw=2.0, dashed=dash)
pa.text(0.8, 0.66, "learning favored", size="small", token="positive")
pa.text(0.535, 0.93, "innate", ha="left", size="small", color=P.muted())
pa.text(0.575, 0.53, "c = 0.05", ha="left", token="dna")
pa.text(0.69, 0.78, "c = 0.15", ha="left", token="rna")

pb = quant.Plot(ax, (12.6, 1.8, 7.6, 6.6), (0.5, 1.0), (0.4, 1.0), xlabel="Within-life predictability p",
                ylabel="Mean payoff", xticks=[0.5, 0.75, 1.0], yticks=[0.4, 0.6, 0.8, 1.0])
bio.panel(ax, "B", (10.8, 9.4))
pb.line(ps, [learner(p, 0.05) for p in ps], "positive", lw=2.0, text="learner", at=0.55, dy=0.25, ha="right")
pb.line(ps, [innate(p, 0.95) for p in ps], "dna", lw=1.8, text="innate, q = 0.95", at=0.86, dy=0.1, dx=-0.15, ha="right")
pb.line(ps, [innate(p, 0.6) for p in ps], "rna", lw=1.8, dashed=True, text="innate, q = 0.6", at=0.75, dy=-0.25)
