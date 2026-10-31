"""Stochastic GTP-cap models of catastrophe and the search-and-capture optimum (26.4.2-26.4.3).

Cap model: dimers add to the tip at rate k (growth velocity v = k a, a = 8 nm/13 per dimer), every GTP
dimer hydrolyzes independently at rate r, and the tip catastrophes when its m outermost dimers are all
GDP. The tip is a Markov chain on the 2^m nucleotide states of those dimers; mean lifetimes and lifetime
distributions follow from its generator. For each m, r is chosen so that the catastrophe frequency is
0.01 s^-1 at 1.5 um/min. A: catastrophe frequency against growth velocity. In these models the cap is long and
catastrophe a rare event, so lifetimes stay exponential. B: lifetimes when catastrophe needs n sequential
steps of equal rate (mean 100 s; Gamma distribution): one step gives an exponential, three steps the
peaked distribution of aging microtubules (Gardner and colleagues 2011).
C: mean time for N = 500 microtubules nucleated at a pole to capture a kinetochore at distance x that
subtends a fraction p = 4e-4 of directions (vg = 10, vs = 20 um/min, no rescue), against the
catastrophe frequency; the optimum is f = vg/x."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
A_NM = 8.0 / 13.0


def generator(m, k, r):
    n = 2 ** m
    mask = n - 1
    Q = np.zeros((n, n))
    for s in range(1, n):  # state 0 (all GDP) is absorbing
        t = ((s << 1) | 1) & mask
        if t != s:
            Q[s, t] += k
        for j in range(m):
            if s >> j & 1:
                Q[s, s & ~(1 << j)] += r
        Q[s, s] = -Q[s].sum()
    return Q[1:, 1:]  # transient block


def mean_life(m, k, r):
    Qt = generator(m, k, r)
    start = np.zeros(Qt.shape[0])
    start[-1] = 1.0  # all GTP
    T = np.linalg.solve(-Qt, np.ones(Qt.shape[0]))
    return start @ T


def k_of_v(v):  # v in um/min
    return v * 1e3 / 60.0 / A_NM


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.86)
k0 = k_of_v(1.5)
vs = np.linspace(0.3, 4, 60)
toks = {1: "neutral", 2: "lipid_head", 3: "channel"}
rates = {}
for m in (1, 2, 3):
    r = brentq(lambda rr: mean_life(m, k0, rr) - 100.0, 1e-3, 1e3)
    rates[m] = r
    f = [1 / mean_life(m, k_of_v(v), r) for v in vs]
    axs[0].plot(vs, f, color=charts.line(toks[m]), lw=1.4, label=f"m = {m}, r = {r:.2g} s$^{{-1}}$")
ax = axs[0]
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"growth velocity / (µm min$^{-1}$)", r"catastrophe frequency / s$^{-1}$")
charts.title(ax, "A  Faster growth, rarer catastrophes")

ax = axs[1]
ts = np.linspace(0, 400, 300)
MEAN = 100.0
for n, tok in ((1, "neutral"), (3, "channel")):
    lam = n / MEAN
    dens = lam ** n * ts ** (n - 1) * np.exp(-lam * ts) / np.prod(np.arange(1, n))
    ax.plot(ts, dens, color=charts.line(tok), lw=1.4, label=f"{n} step" + ("s" if n > 1 else ""))
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "lifetime of the growth phase / s", r"probability density / s$^{-1}$")
charts.title(ax, "B  Aging: lifetimes from several steps")

ax = axs[2]
VG, VS, PT, N = 10.0, 20.0, 4e-4, 500
f = np.logspace(-1.5, 1, 300)  # per min
for x, ls in ((5.0, ":"), (10.0, "-"), (15.0, "--")):
    T = (1 + VG / VS) / f * np.exp(f * x / VG) / (PT * N)
    ax.plot(f, T, color=charts.line("channel"), lw=1.4, ls=ls, label=f"x = {x:g} µm")
    fo = VG / x
    ax.plot(fo, (1 + VG / VS) / fo * np.e / (PT * N), "o", color=charts.line("channel"), ms=4)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(3, 3000)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(ax, r"catastrophe frequency / min$^{-1}$", "mean capture time / min")
charts.title(ax, "C  Search and capture")
