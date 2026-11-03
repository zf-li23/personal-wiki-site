"""Establishment of a new beneficial mutation (Theorem 5.3.1). A: probability that a single new copy is not
lost, against its selective advantage s per copy. Line: the exact branching-process value for Poisson
offspring numbers, the root of 1 - pi = exp(-(1 + s) pi); dashed: Haldane's approximation 2s; dotted: Kimura's
diffusion formula for N = 500; dots: fraction of 20 000 simulated Wright-Fisher populations of N = 500 diploids
(genic selection) in which the mutation was fixed, with 95 % intervals. B: the number of copies of 60 new
mutations with s = 0.05 in a population of N = 5000 over their first 150 generations (log scale): most are lost
within a few generations (short grey lines ending at the bottom); the survivors grow roughly as e^(st) once
they exceed about 1/(2s) = 10 copies (dashed line)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8), gridspec_kw={"width_ratios": [1, 1.15]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)

s = np.linspace(0.002, 0.2, 200)
exact = np.array([brentq(lambda x: 1 - x - np.exp(-(1 + v) * x), 1e-12, 1) for v in s])
a.plot(s, exact, color=charts.line("dna"), lw=2, label="branching process (Poisson)")
a.plot(s, 2 * s, color=P.ink(), lw=1, ls="--", label="$2s$")
N = 500
a.plot(s, evo.kimura_u(1 / (2 * N), N, s), color=charts.line("rna"), lw=1.2, ls=":", label="Kimura, $N = 500$")
rng = np.random.default_rng(1)
for v in (0.01, 0.02, 0.05, 0.1, 0.15, 0.2):
    u, lo, hi = evo.fixation_probability(N, v, 1 / (2 * N), reps=20000, rng=rng)
    a.plot([v, v], [lo, hi], color=P.ink(), lw=0.9)
    a.scatter([v], [u], s=16, color=P.ink(), zorder=4)
a.set_xlim(0, 0.205)
a.set_ylim(0, 0.42)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "selective advantage $s$", "probability of establishment")
charts.title(a, "A  Most beneficial mutations are lost")

N, sv, T = 5000, 0.05, 150
rng = np.random.default_rng(4)
for j in range(60):
    k = [1]
    for t in range(T):
        p = k[-1] / (2 * N)
        n = rng.binomial(2 * N, p * (1 + sv) / (1 + sv * p))
        k.append(n)
        if n == 0 or n == 2 * N:
            break
    k = np.array(k, float)
    lost = k[-1] == 0
    y = np.where(k > 0, k, 0.6)
    b.plot(np.arange(len(k)), y, color=P.mix(P.muted(), P.surface(), 0.3) if lost else charts.line("rna"),
           lw=0.7 if lost else 1.4, zorder=2 if lost else 3)
b.axhline(1 / (2 * sv), color=P.ink(), lw=0.8, ls="--")
b.text(T * 0.99, 1 / (2 * sv) * 1.15, "$1/(2s)$ copies", ha="right", fontsize=FT["tiny"], color=P.ink())
b.set_yscale("log")
b.set_ylim(0.5, 2 * N)
b.set_xlim(0, T)
b.text(2, 0.62, "lost", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(b, "generation", "copies of the mutation")
charts.title(b, "B  60 new mutations, $s = 0.05$, $N = 5000$")
