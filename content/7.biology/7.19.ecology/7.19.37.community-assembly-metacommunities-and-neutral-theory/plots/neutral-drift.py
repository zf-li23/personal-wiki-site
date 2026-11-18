"""Ecological drift in a neutral community (Moran process).

A: a closed community of J = 400 individuals, initially 20 species with 20 individuals each. At every
step one individual chosen at random dies and is replaced by the offspring of another individual
chosen at random among the survivors; J steps make one generation. Six independent runs: species are
lost one by one and the community drifts towards monodominance on a time scale of order J generations
(dashed: mean of the runs).
B: the same community with speciation: each replacement is a new species with probability
nu = 0.025, so theta = (J - 1) nu / (1 - nu) = 10.2. Richness rises from a single species and fluctuates
around the equilibrium expectation E[S] = sum_{i=0}^{J-1} theta / (theta + i) of the Ewens sampling
formula (dashed line), where loss by drift balances gain by speciation.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 12.0)


def run(J, nu, gens, init, record_every):
    sp = init.copy()
    nxt = sp.max() + 1
    out = []
    steps = gens * J
    deaths = rng.integers(J, size=steps)
    parents = rng.integers(J - 1, size=steps)
    newsp = rng.random(steps) < nu
    counts = np.bincount(sp, minlength=sp.max() + 1).tolist()
    rich = sum(1 for c in counts if c > 0)
    for s in range(steps):
        if s % record_every == 0:
            out.append(rich)
        d = deaths[s]
        old = sp[d]
        if newsp[s]:
            new = nxt
            nxt += 1
            counts.append(0)
        else:
            j = parents[s]
            j = j if j < d else j + 1
            new = sp[j]
        if new != old:
            counts[old] -= 1
            if counts[old] == 0:
                rich -= 1
            if counts[new] == 0:
                rich += 1
            counts[new] += 1
            sp[d] = new
    out.append(rich)
    return np.array(out)


J = 400
G = 1200
every = J // 4
init = np.repeat(np.arange(20), 20)
t = np.arange(G * J // every + 1) * every / J
t[0] = 1e-3
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
runs = []
toks = ["dna", "rna", "positive", "enzyme", "protein", "negative"]
for k in range(6):
    r = run(J, 0.0, G, init, every)
    runs.append(r)
    pa.step(t, r, where="post", color=Q.line_color(toks[k]), lw=1.0)
pa.plot(t, np.mean(runs, axis=0), color=P.ink(), lw=1.6, ls="--", label="mean of 6 runs")
pa.set_xscale("log")
pa.set_xlim(1, G)
pa.set_ylim(0, 21)
pa.set_yticks([0, 5, 10, 15, 20])
C.style_axes(pa, "time / generations", "number of species")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Drift without speciation (J = 400, 20 species)", size="small", bold=True, ha="left")

nu = 0.025
theta = (J - 1) * nu / (1 - nu)
ES = sum(theta / (theta + i) for i in range(J))
G2 = 400
r = run(J, nu, G2, np.zeros(J, int), every)
t2 = np.arange(len(r)) * every / J
pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
pb.step(t2, r, where="post", color=Q.line_color("dna"), lw=1.0, label="one simulation")
pb.axhline(ES, color=P.ink(), lw=1.4, ls="--", label=f"Ewens expectation E[S] = {ES:.1f}")
pb.set_xlim(0, G2)
pb.set_ylim(0, 60)
C.style_axes(pb, "time / generations", "number of species")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), f"Drift balanced by speciation (theta = {theta:.1f})", size="small", bold=True, ha="left")
