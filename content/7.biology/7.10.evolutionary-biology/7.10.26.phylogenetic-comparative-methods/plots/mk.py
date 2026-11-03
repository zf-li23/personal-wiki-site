"""The Mk model for a binary character and ancestral state reconstruction. A binary character (state 0,
open; state 1, filled) was simulated on a dated tree of 12 species (root age 1) under the symmetric
Mk model with rate q = 1.5 per unit time. A: the tree with the observed tip states and, at each
internal node, the marginal posterior probability of state 1 (pie charts) computed by the pruning
algorithm at the maximum likelihood rate with equal root probabilities. B: the log likelihood of q
(profile; ML estimate dotted, approximate 95 % interval shaded); the data are compatible with a wide
range of rates, as is typical for a single character on a small tree."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(31)
# tree as nested tuples (left, right, node_time); tips are ints with time 1
T = ((((0, 1, 0.75), 2, 0.5), ((3, 4, 0.8), (5, (6, 7, 0.9), 0.6), 0.4), 0.2),
     (((8, 9, 0.7), 10, 0.55), 11, 0.35), 0.0)


def ntime(nd):
    return 1.0 if not isinstance(nd, tuple) else nd[2]


def Pmat(q, t):
    e = np.exp(-2 * q * t)
    return np.array([[0.5 + 0.5 * e, 0.5 - 0.5 * e], [0.5 - 0.5 * e, 0.5 + 0.5 * e]])


def simulate(nd, state, q, out):
    if not isinstance(nd, tuple):
        out[nd] = state
        return
    for ch in nd[:2]:
        p = Pmat(q, ntime(ch) - nd[2])[state]
        simulate(ch, rng.choice(2, p=p), q, out)


tipstate = {}
simulate(T, rng.integers(2), 1.5, tipstate)


def partial(nd, q, clamp=None):
    if not isinstance(nd, tuple):
        v = np.zeros(2)
        v[tipstate[nd]] = 1
        return v
    v = np.ones(2)
    for ch in nd[:2]:
        v *= Pmat(q, ntime(ch) - nd[2]) @ partial(ch, q, clamp)
    if clamp is not None and clamp[0] is nd:
        m = np.zeros(2)
        m[clamp[1]] = 1
        v = v * m
    return v


def loglik(q, clamp=None):
    return np.log(0.5 * partial(T, q, clamp).sum())


qs = np.linspace(0.05, 8, 300)
ll = np.array([loglik(q) for q in qs])
qhat = qs[ll.argmax()]
internals = []


def collect(nd):
    if isinstance(nd, tuple):
        internals.append(nd)
        collect(nd[0])
        collect(nd[1])


collect(T)
post = {}
for nd in internals:
    l1 = np.exp(loglik(qhat, (nd, 1)))
    l0 = np.exp(loglik(qhat, (nd, 0)))
    post[id(nd)] = l1 / (l0 + l1)
ypos = {}


def tips(nd):
    return [nd] if not isinstance(nd, tuple) else tips(nd[0]) + tips(nd[1])


for k, tp in enumerate(tips(T)):
    ypos[tp] = k


def gety(nd):
    if not isinstance(nd, tuple):
        return ypos[nd]
    y = (gety(nd[0]) + gety(nd[1])) / 2
    ypos[id(nd)] = y
    return y


gety(T)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.0), gridspec_kw=dict(width_ratios=[1.3, 1]))
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.14, top=0.9, wspace=0.2)
c1, c0 = charts.line("dna"), P.surface()


def yof(nd):
    return ypos[nd] if not isinstance(nd, tuple) else ypos[id(nd)]


def draw(nd):
    if not isinstance(nd, tuple):
        return
    for ch in nd[:2]:
        a.plot([X * nd[2], X * nd[2]], [yof(nd), yof(ch)], color=P.muted(), lw=1.0)
        a.plot([X * nd[2], X * ntime(ch)], [yof(ch), yof(ch)], color=P.muted(), lw=1.0)
        draw(ch)


X = 11.0
draw(T)
a.set_aspect("equal")
for nd in internals:
    p = post[id(nd)]
    xy = (X * nd[2], yof(nd))
    if p > 0.001:
        a.add_patch(Wedge(xy, 0.33, 90, 90 + 360 * p, facecolor=c1, edgecolor=P.ink(), lw=0.5, zorder=5))
    if p < 0.999:
        a.add_patch(Wedge(xy, 0.33, 90 + 360 * p, 450, facecolor=c0, edgecolor=P.ink(), lw=0.5, zorder=5))
for tp in tips(T):
    a.scatter([X], [ypos[tp]], s=40, marker="s", color=c1 if tipstate[tp] else c0, edgecolors=P.ink(),
              linewidths=0.6, zorder=5)
    a.text(X + 0.4, ypos[tp], f"sp. {tp + 1}", fontsize=FT["tiny"], color=P.ink(), va="center")
a.set_xlim(-0.5, X + 2.0)
a.set_ylim(-0.8, 11.8)
a.axis("off")
charts.title(a, f"A  Marginal reconstruction at $\\hat q = {qhat:.2f}$")
b.plot(qs, ll - ll.max(), color=charts.line("dna"), lw=1.8)
b.fill_between(qs, -6, 0.2, where=ll - ll.max() > -1.92, color=P.fill("dna"), alpha=0.35, lw=0)
b.axvline(qhat, color=P.ink(), lw=0.8, ls=":")
b.axhline(-1.92, color=P.muted(), lw=0.8, ls="--")
b.set_ylim(-6, 0.2)
charts.style_axes(b, "transition rate $q$", "log likelihood $-\\,\\ell_{\\max}$")
charts.title(b, "B  Likelihood of the rate")
