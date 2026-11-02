"""Context dependence of a genetic module (model units).
A: retroactivity. A transcription factor X is made at rate k and removed at rate 1 (steady state 10);
it binds p_T downstream promoter sites (K_D = 10, fast binding, bound X protected from removal). After
X production is switched on at t = 0, the free X rises more slowly the more sites it must fill: half
times 0.69, 1.58 and 5.11 for p_T = 0, 20 and 100 (the slowdown factor of Formula 17.5.1 is 1, 3 and 11
at X = 0 and 1, 1.5 and 3.5 at the final level).
B: the same module driven by an oscillating production rate k(t) = 10(1 + 0.8 sin t): the load
attenuates and delays the signal: the amplitude of free X is 5.66, 4.40 and 2.19.
C: resource competition. Two genes share a pool of ribosomes; their outputs are proportional to
a_i/(1 + a_1 + a_2), where a_i is the ribosome demand of gene i. Inducing gene 2 lowers the output of
gene 1 although no regulatory link joins them (dotted: output of gene 2, relative to the whole
pool). Outputs are relative to gene 1 alone; in units of the pool the two outputs sum to at most 1."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
KD, kon = 10.0, 100.0
koff = KD * kon


def run(pT, kfun, T, t_eval):
    def rhs(t, z):
        X, C = z
        b = kon * X * (pT - C) - koff * C
        return [kfun(t) - X - b, b]

    return solve_ivp(rhs, (0, T), [0.0, 0.0], method="LSODA", t_eval=t_eval, rtol=1e-8, atol=1e-10)


fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.06, right=0.95, bottom=0.17, top=0.86, wspace=0.38)
toks = {0: "neutral", 20: "protein", 100: "negative"}

ax = axs[0]
t = np.linspace(0, 10, 500)
for pT, tok in toks.items():
    r = run(pT, lambda s: 10.0, 10, t)
    ax.plot(t, r.y[0], color=charts.line(tok), lw=1.5, label=f"p_T = {pT}")
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "time (1/gamma)", "free X")
charts.title(ax, "A  Load slows the response")

ax = axs[1]
t = np.linspace(0, 40, 2000)
for pT, tok in toks.items():
    r = run(pT, lambda s: 10.0 * (1 + 0.8 * np.sin(s)), 40, t)
    m = t > 20
    ax.plot(t[m], r.y[0][m], color=charts.line(tok), lw=1.4, label=f"p_T = {pT}")
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=3)
ax.set_ylim(0, 22)
charts.style_axes(ax, "time (1/gamma)", "free X")
charts.title(ax, "B  Load attenuates a signal")

ax = axs[2]
a2 = np.linspace(0, 10, 200)
for a1, tok in [(0.5, "positive"), (2.0, "protein")]:
    ax.plot(a2, a1 / (1 + a1 + a2) / (a1 / (1 + a1)), color=charts.line(tok), lw=1.5, label=f"gene 1, a_1 = {a1:g}")
ax.plot(a2, a2 / (1 + 2.0 + a2), ":", color=charts.line("highlight"), lw=1.5, label="gene 2 (a_1 = 2)")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "induction of gene 2 (demand a_2)", "relative output")
charts.title(ax, "C  Shared ribosomes couple genes")
