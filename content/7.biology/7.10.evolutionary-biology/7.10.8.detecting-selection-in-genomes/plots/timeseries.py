"""Inferring s from an allele-frequency time series. A: a Wright-Fisher population of N = 100 diploids (201
states for the number of copies) with genic selection s = 0.05 per copy, starting at frequency 0.1, followed
for 100 generations (line), and samples of 40 chromosomes every 10 generations (dots, Wilson 95 % intervals).
B: log likelihood of the samples against s by the forward algorithm of a hidden Markov model: hidden state =
number of copies, transition = Wright-Fisher matrix with selection (applied 10 times between samples),
emission = binomial sampling; the initial distribution is uniform over states. Dotted: maximum-likelihood
estimate; shaded: log likelihood within 1.92 of the maximum (approximate 95 % interval); solid: true s."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(51)
N, s0, T, step, ns = 100, 0.05, 100, 10, 40
M = 2 * N
k = np.arange(M + 1)
traj = [0.1]
x = 0.1
for t in range(T):
    x = rng.binomial(M, x * (1 + s0) / (1 + s0 * x)) / M
    traj.append(x)
times = np.arange(0, T + 1, step)
obs = np.array([rng.binomial(ns, traj[t]) for t in times])


def loglik(s):
    pr = k / M
    psel = pr * (1 + s) / (1 + s * pr)
    W = binom.pmf(k[None, :], M, psel[:, None])
    W10 = np.linalg.matrix_power(W, step)
    alpha = np.full(M + 1, 1 / (M + 1)) * binom.pmf(obs[0], ns, pr)
    ll = np.log(alpha.sum())
    alpha /= alpha.sum()
    for o in obs[1:]:
        alpha = (alpha @ W10) * binom.pmf(o, ns, pr)
        c = alpha.sum()
        ll += np.log(c)
        alpha /= c
    return ll


ss = np.linspace(-0.04, 0.16, 81)
ll = np.array([loglik(v) for v in ss])
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
a.plot(np.arange(T + 1), traj, color=charts.line("dna"), lw=1.5, label="population frequency")
for t, o in zip(times, obs):
    lo, hi = evo.wilson(o, ns)
    a.plot([t, t], [lo, hi], color=charts.line("rna"), lw=1)
a.scatter(times, obs / ns, s=16, color=charts.line("rna"), zorder=4, label="samples of 40")
a.set_xlim(-2, T + 2)
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "generation", "allele frequency")
charts.title(a, "A  Time series, $s = 0.05$, $N = 100$")
b.plot(ss, ll - ll.max(), color=P.ink(), lw=1.6)
inside = ll >= ll.max() - 1.92
b.fill_between(ss, -12, 0.5, where=inside, color=P.mix(P.surface(), P.muted(), 0.25), lw=0)
b.axvline(ss[np.argmax(ll)], color=P.ink(), lw=0.9, ls=":")
b.axvline(s0, color=charts.line("rna"), lw=1.2)
b.set_ylim(-12, 0.5)
b.set_xlim(ss[0], ss[-1])
charts.style_axes(b, "selection coefficient $s$", "log likelihood (relative)")
charts.title(b, "B  Likelihood from a hidden Markov model")
