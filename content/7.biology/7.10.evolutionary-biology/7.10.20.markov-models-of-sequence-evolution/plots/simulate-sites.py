"""Simulating a continuous-time Markov chain of nucleotide substitution (HKY85 with kappa = 5 and
frequencies T 0.1, C 0.2, A 0.3, G 0.4, scaled to one substitution per unit time). A: the histories of
six sites started in A along a branch of length 2, simulated by drawing exponential waiting times and
jumps (each horizontal segment is a nucleotide; vertical ticks are substitutions). B: the proportion of
4000 sites started in A that are in each state at time t: simulated by waiting times (dots) or by
drawing the end state directly from the row of P(t) (crosses), compared with the exact transition
probabilities p_Aj(t) (lines); both converge to the stationary frequencies (right margin)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
NUC = "TCAG"
pi = np.array([0.1, 0.2, 0.3, 0.4])
kappa = 5.0
Q = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        if i != j:
            ts = {i, j} in ({0, 1}, {2, 3})
            Q[i, j] = (kappa if ts else 1.0) * pi[j]
np.fill_diagonal(Q, -Q.sum(1))
Q /= -(pi * np.diag(Q)).sum()
rng = np.random.default_rng(3)


def path(x, T):
    t, out = 0.0, [(0.0, x)]
    while True:
        t += rng.exponential(1 / -Q[x, x])
        if t > T:
            return out
        w = Q[x].copy()
        w[x] = 0
        x = rng.choice(4, p=w / w.sum())
        out.append((t, x))


fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.0), gridspec_kw={"width_ratios": [1.1, 1]})
fig.subplots_adjust(left=0.06, right=0.97, bottom=0.15, top=0.9, wspace=0.25)
T = 2.0
for s in range(6):
    h = path(2, T) + [(T, None)]
    for (t0, x0), (t1, _) in zip(h[:-1], h[1:]):
        a.plot([t0, t1], [s, s], color=P.NUCLEOTIDE[NUC[x0]], lw=6, solid_capstyle="butt")
        if t0 > 0:
            a.plot([t0, t0], [s - 0.3, s + 0.3], color=P.ink(), lw=0.8)
for k, ch in enumerate(NUC):
    a.plot([], [], color=P.NUCLEOTIDE[ch], lw=6, label=ch)
a.set_yticks(range(6), [f"site {s + 1}" for s in range(6)])
a.set_xlim(0, T)
a.set_ylim(-0.7, 6.2)
a.legend(frameon=False, ncol=4, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center",
         bbox_to_anchor=(0.5, 1.0))
charts.style_axes(a, "time $t$ (expected substitutions per site)")
charts.title(a, "A  Site histories by waiting times")

tg = np.linspace(0, 3, 200)
Pt = np.array([expm(Q * t)[2] for t in tg])
tt = np.linspace(0.25, 3, 12)
nsite = 4000
for j, ch in enumerate(NUC):
    b.plot(tg, Pt[:, j], color=P.NUCLEOTIDE[ch], lw=1.5)
    b.text(3.05, pi[j], ch, color=P.NUCLEOTIDE[ch], fontsize=FT["small"], va="center")
sim_w = np.zeros((len(tt), 4))
sim_p = np.zeros((len(tt), 4))
for k, t in enumerate(tt):
    ends = [path(2, t)[-1][1] for _ in range(nsite)]
    sim_w[k] = np.bincount(ends, minlength=4) / nsite
    sim_p[k] = rng.multinomial(nsite, expm(Q * t)[2]) / nsite
for j, ch in enumerate(NUC):
    b.plot(tt, sim_w[:, j], "o", ms=3.5, color=P.NUCLEOTIDE[ch])
    b.plot(tt + 0.04, sim_p[:, j], "x", ms=4, color=P.NUCLEOTIDE[ch])
b.plot([], [], "o", ms=3.5, color=P.muted(), label="waiting-time simulation")
b.plot([], [], "x", ms=4, color=P.muted(), label="sampled from $P(t)$")
b.plot([], [], color=P.muted(), label="exact $p_{\\mathrm{A}j}(t)$")
b.set_xlim(0, 3.2)
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "time $t$", "proportion of sites")
charts.title(b, "B  Two simulation methods agree")
