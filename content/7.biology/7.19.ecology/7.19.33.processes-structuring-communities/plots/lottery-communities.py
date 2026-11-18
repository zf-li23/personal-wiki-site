"""Competitive lotteries for space in a finite community.

J = 1000 sites, eight species, one adult per site. Each year every adult dies with probability delta; each
vacant site is won by a juvenile of species i with probability B_i N_i / sum_j B_j N_j, where N_i is the
number of sites held and B_i the per capita fecundity that year (multinomial sampling). Scenarios:
neutral (all B_i = 1, delta = 0.2); one species with a 5 % higher constant fecundity (delta = 0.2);
fluctuating fecundities, ln B_i independent normal with sd 1.5 and means spaced 0.05 apart, with
long-lived adults (delta = 0.1, the storage effect of Eq. (23.6) in 7.19.23) or an annual life cycle
(delta = 1). A: relative abundances in one neutral run (drift). B: one run with fluctuating fecundities and
delta = 0.1. C: number of species still present, mean of 20 runs for each scenario.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)

J, S, T = 1000, 8, 3000
toks = ["dna", "enzyme", "protein", "negative", "plant", "highlight", "rna", "muted"]


def run(kind, delta, record=False):
    N = np.full(S, J // S)
    rich = np.empty(T)
    hist = np.empty((T, S)) if record else None
    mu = -0.05 * np.arange(S)
    for t in range(T):
        if kind == "neutral":
            B = np.ones(S)
        elif kind == "advantage":
            B = np.ones(S)
            B[0] = 1.05
        else:
            B = np.exp(mu + 1.5 * rng.standard_normal(S))
        deaths = rng.binomial(N, delta)
        N = N - deaths
        V = deaths.sum()
        w = B * (N + deaths)
        if w.sum() > 0 and V > 0:
            N = N + rng.multinomial(V, w / w.sum())
        rich[t] = (N > 0).sum()
        if record:
            hist[t] = N / J
    return rich, hist


fig, ax = bio.canvas(31.0, 10.0)

_, h = run("neutral", 0.2, record=True)
pa = C.axes_at(ax, (2.2, 1.6, 7.4, 6.8))
pa.stackplot(np.arange(T), h.T, colors=[Q.line_color(k) for k in toks], lw=0)
pa.set_xlim(0, T)
pa.set_ylim(0, 1)
C.style_axes(pa, "years", "fraction of sites")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Neutral lottery: drift", size="small", bold=True, ha="left")

_, h = run("fluct", 0.1, record=True)
pb = C.axes_at(ax, (12.4, 1.6, 7.4, 6.8))
pb.stackplot(np.arange(T), h.T, colors=[Q.line_color(k) for k in toks], lw=0)
pb.set_xlim(0, T)
pb.set_ylim(0, 1)
C.style_axes(pb, "years", "fraction of sites")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.2), "Fluctuating recruitment, long-lived adults", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.8, 1.6, 7.4, 6.8))
for (kind, delta, lab, tok) in [
    ("neutral", 0.2, "neutral, δ = 0.2", "muted"),
    ("advantage", 0.2, "one species 5 % more fecund", "negative"),
    ("fluct", 0.1, "fluctuating, δ = 0.1 (storage)", "plant"),
    ("fluct", 1.0, "fluctuating, δ = 1 (annual)", "enzyme"),
]:
    rr = np.mean([run(kind, delta)[0] for _ in range(20)], axis=0)
    pc.plot(np.arange(T), rr, color=Q.line_color(tok), lw=1.6, label=lab)
pc.set_xlim(0, T)
pc.set_ylim(0, 8.4)
C.style_axes(pc, "years", "species present (mean of 20 runs)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.3, 9.6))
bio.label(ax, (22.8, 9.2), "Richness under four lotteries", size="small", bold=True, ha="left")
