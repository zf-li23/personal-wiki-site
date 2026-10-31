"""The two cores of robust adaptation found by Ma, Trusina, El-Samad, Lim and Tang (2009) in their
search of all three-node networks, with Michaelis-Menten links as in that study (node activities
between 0 and 1; a node without negative input is deactivated by a background enzyme of level 0.5).
The input I steps from 0.5 to 0.6 at t = 100. A: negative feedback with a buffer node,
A -> C -> B -| A; the buffer B is activated by C and deactivated by the background enzyme, both with
Michaelis constant K. When K is small both reactions are saturated, dB/dt is approximately
k(C - C*), B integrates the error of the output, and C returns to C* exactly. B: incoherent
feed-forward loop with a proportioner node, A -> C, A -> B -| C; B is made at a saturated rate
proportional to A and removed by an enzyme with Michaelis constant K_B. When K_B is large the
removal is first order, B is proportional to A, and the input cancels from the steady state of C.
C: adaptation precision (inverse of the relative change of the steady output per relative change of
the input) against the saturation parameter of each motif, K for the feedback (lower axis) and 1/K_B
for the feed-forward loop: precision is high only in the regime the mechanism requires."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P


def up(x, k, K, s):
    return s * k * (1 - x) / ((1 - x) + K)


def down(x, k, K, s):
    return s * k * x / (x + K)


def inp(t):
    return 0.5 if t < 100 else 0.6


def nfblb(t, y, K):
    A, B, C = y
    return [up(A, 2, 0.5, inp(t)) - down(A, 4, 0.5, B),
            up(B, 1, K, C) - down(B, 0.5, K, 0.5),
            up(C, 2, 0.5, A) - down(C, 2, 0.5, 0.5)]


def ifflp(t, y, KB):
    A, B, C = y
    return [up(A, 2, 0.5, inp(t)) - down(A, 2, 0.5, 0.5),
            up(B, 0.1, 0.01, A) - down(B, 0.2 * KB, KB, 0.5),
            up(C, 2, 0.001, A) - down(C, 4, 0.5, B)]


def run(f, p):
    s = solve_ivp(f, (0, 400), [0.3, 0.3, 0.3], args=(p,), method="LSODA", max_step=0.5, rtol=1e-8, atol=1e-10)
    return s.t, s.y[2]


def precision(f, p):
    t, C = run(f, p)
    O1 = C[t < 100][-1]
    return 1 / max(abs(C[-1] - O1) / O1 / 0.2, 1e-4)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.17, top=0.86)
toks = ["neutral", "highlight", "enzyme", "receptor"]

ax = axs[0]
for K, tok in zip((1.0, 0.1, 0.01, 0.001), toks):
    t, C = run(nfblb, K)
    ax.plot(t[t > 50], C[t > 50], color=charts.line(tok), lw=1.3, label=f"K = {K:g}")
ax.axvline(100, color=P.muted(), lw=0.5, ls=":")
ax.set_xlim(50, 400)
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, "time", "output C")
charts.title(ax, r"A  feedback A$\to$C$\to$B$\dashv$A")

ax = axs[1]
for KB, tok in zip((0.1, 1.0, 10.0, 100.0), toks):
    t, C = run(ifflp, KB)
    ax.plot(t[t > 50], C[t > 50], color=charts.line(tok), lw=1.3, label=rf"$K_{{\mathrm{{B}}}}$ = {KB:g}")
ax.axvline(100, color=P.muted(), lw=0.5, ls=":")
ax.set_xlim(50, 400)
ax.legend(frameon=False, fontsize=7, loc="lower right")
charts.style_axes(ax, "time", "output C")
charts.title(ax, r"B  feed-forward A$\to$C, A$\to$B$\dashv$C")

ax = axs[2]
sat = np.logspace(-3, 1, 9)
ax.loglog(sat, [precision(nfblb, s) for s in sat], "o-", color=charts.line("receptor"), ms=3, lw=1.1,
          label=r"feedback: $K$")
ax.loglog(sat, [precision(ifflp, 1 / s) for s in sat], "s-", color=charts.line("enzyme"), ms=3, lw=1.1,
          label=r"feed-forward: $1/K_{\mathrm{B}}$")
ax.axhline(10, color=P.muted(), lw=0.7, ls="--")
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, "saturation parameter", "precision")
charts.title(ax, "C  precision")
