"""Two-state Markov model of an epiallele, Eq. (18.1). A: simulated lineages (alpha = P(M -> U),
beta = P(U -> M) per generation). B: probability of the methylated state against generations, from fully
methylated and fully unmethylated starts, for an unstable epiallele and for single CG sites in Arabidopsis."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.15, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.25)

a = axs[0]
alpha, beta, T, n = 0.05, 0.02, 150, 5
for k in range(n):
    s = np.empty(T + 1, int)
    s[0] = 1
    for t in range(T):
        u = rng.random()
        s[t + 1] = (0 if u < alpha else 1) if s[t] == 1 else (1 if u < beta else 0)
    y0 = k * 1.4
    a.fill_between(np.arange(T + 1), y0, y0 + 0.9 * s, step="post", color=P.fill("dna"), lw=0)
    a.step(np.arange(T + 1), y0 + 0.9 * s, where="post", color=charts.line("dna"), lw=0.9)
    a.text(-3, y0 + 0.45, f"line {k + 1}", ha="right", va="center", fontsize=FT["tiny"], color=P.muted())
a.set_xlim(0, T)
a.set_yticks([])
a.spines["left"].set_visible(False)
charts.style_axes(a, "generation", None)
a.spines["left"].set_visible(False)
charts.title(a, "A  Lineages of one epiallele (filled: methylated)")
a.text(T, n * 1.4 - 0.25, f"α = {alpha}, β = {beta}", ha="right", fontsize=FT["tiny"], color=P.muted())

b = axs[1]
t = np.logspace(0, 5, 400)
for (al, be, tok, name) in ((0.05, 0.02, "dna", "epiallele: α = 0.05, β = 0.02"),
                            (6e-4, 3e-4, "receptor", "CG site: α = 6×10⁻⁴, β = 3×10⁻⁴")):
    pi, lam = be / (al + be), 1 - al - be
    c = charts.line(tok)
    b.plot(t, pi + lam**t * (1 - pi), color=c, lw=1.8, label=name)
    b.plot(t, pi + lam**t * (0 - pi), color=c, lw=1.4, ls="--")
    b.axhline(pi, color=c, lw=0.7, ls=":")
    b.text(1.3e5, pi + (0.025 if tok == "receptor" else -0.065), f"π = {pi:.2f}", ha="right", fontsize=FT["tiny"], color=c)
b.set_xscale("log")
b.set_ylim(-0.02, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(b, "generations t", "P(methylated)")
charts.title(b, "B  Approach to equilibrium, Eq. (18.1)")
