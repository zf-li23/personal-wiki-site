"""Establishment of a small founding population with and without an Allee effect.

Birth-death process with per capita death rate d = 0.8 and per capita birth rate b = 1 (no Allee effect)
or b n / (n + theta) with theta = 5 (mate limitation: at density n only a fraction n/(n + theta) of females
find mates). In the deterministic version with the Allee effect, the population declines below the
threshold n_A = theta d / (b - d) = 20 and grows above it. A: per capita growth rate of the deterministic
models against n. B: probability that a founding population of size N0 reaches 300 individuals before
extinction, computed exactly for the embedded jump chain (gambler's-ruin formula with state-dependent
step probabilities p_n = lambda_n / (lambda_n + mu_n)); points are 1000 simulations each (seed 0) for
selected N0. Demographic stochasticity turns the sharp deterministic threshold into a sigmoid curve.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
b, d, theta, cap = 1.0, 0.8, 5.0, 300
rng = np.random.default_rng(0)


def birth(n, allee):
    return b * n * (n / (n + theta) if allee else 1.0)


def reach_prob(allee):
    n = np.arange(1, cap)
    lam = birth(n, allee)
    mu = d * n
    rho = np.cumprod(mu / lam)  # rho_k = prod_{j<=k} mu_j / lam_j
    s = np.r_[1.0, rho]  # s_0 = 1, s_k = rho_k
    cum = np.cumsum(s)
    # P(reach cap before 0 | start N0) = sum_{k=0}^{N0-1} s_k / sum_{k=0}^{cap-1} s_k
    return cum[:-1] / cum[-1]


def sim(n0, allee, runs=1000):
    ok = 0
    for _ in range(runs):
        n = n0
        while 0 < n < cap:
            lam, mu = birth(n, allee), d * n
            n += 1 if rng.random() < lam / (lam + mu) else -1
        ok += n == cap
    return ok / runs


fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 11.0, 6.8))
n = np.linspace(0.1, 80, 400)
pa.plot(n, b - d + 0 * n, color=Q.line_color("dna"), lw=1.6, label="no Allee effect")
pa.plot(n, b * n / (n + theta) - d, color=Q.line_color("negative"), lw=1.6, label="mate limitation (theta = 5)")
pa.axhline(0, color=P.muted(), lw=0.8)
nA = theta * d / (b - d)
pa.axvline(nA, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.text(nA + 1, -0.6, f"Allee threshold n_A = {nA:.0f}", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 80)
pa.set_ylim(-0.8, 0.3)
C.style_axes(pa, "population size n", "per capita growth rate")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Deterministic per capita growth", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (18.0, 1.6, 11.0, 6.8))
N0 = np.arange(1, 81)
for allee, tok, lab in [(False, "dna", "no Allee effect"), (True, "negative", "Allee effect")]:
    pr = reach_prob(allee)[:80]
    pb.plot(N0, pr, color=Q.line_color(tok), lw=1.7, label=lab)
    sel = [2, 10, 20, 30, 50]
    pb.plot(sel, [sim(s, allee) for s in sel], "o", ms=3.5, color=Q.line_color(tok))
pb.axvline(nA, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.set_ylim(0, 1)
pb.set_xlim(0, 80)
C.style_axes(pb, "founding population N0", "P(reach 300 before extinction)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (16.5, 9.6))
bio.label(ax, (18.0, 9.2), "Probability of establishment", size="small", bold=True, ha="left")
