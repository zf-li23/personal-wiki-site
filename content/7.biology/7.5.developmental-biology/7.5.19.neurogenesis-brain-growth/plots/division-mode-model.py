"""How the schedule of division modes sets the number of cortical neurons (the Q-fraction model of Takahashi,
Nowakowski and Caviness, Formula 19.3.1). (A) In the mouse dorsal cortex about 11 cell cycles span neurogenesis
(E11-E17); the fraction Q of daughters that leave the cycle and become neurons rises from about 0 to 1 (here a
logistic curve with Q = 0.5 at cycle 8). The progenitor pool P grows while Q < 1/2 and shrinks after; neurons
accumulate mostly in the last cycles. (B) Neurons per founder progenitor when the same schedule is preceded by
extra symmetric proliferative cycles (Q = 0): each extra cycle doubles the output, which is the basis of the
radial unit hypothesis for the expansion of the primate cortex; a schedule stretched to 28 cycles (with the
same shape) gives far more neurons than one stretched to 11."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT


def run(Q):
    P, N, Ps, Ns = 1.0, 0.0, [1.0], [0.0]
    for q in Q:
        N += 2 * q * P
        P = 2 * (1 - q) * P
        Ps.append(P)
        Ns.append(N)
    return np.array(Ps), np.array(Ns)


k = np.arange(1, 12)
Q = 1 / (1 + np.exp(-(k - 8) / 1.1))
Q[-1] = 1.0
Ps, Ns = run(Q)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.32)
a.plot(k, Q, "o-", color=charts.line("receptor"), lw=1.5, ms=4, label="Q (leaving fraction)")
a.axhline(0.5, color=P_.muted(), lw=0.7, ls=":")
a.set_ylim(0, 1.05)
a2 = a.twinx()
a2.plot(np.arange(0, 12), Ps, "s-", color=charts.line("protein"), lw=1.4, ms=3.5, label="progenitors P")
a2.plot(np.arange(0, 12), Ns, "^-", color=charts.line("antibody"), lw=1.4, ms=3.5, label="neurons (cumulative)")
charts.style_axes(a, "cell cycle of neurogenesis", "Q")
charts.style_axes(a2, None, "cells per founder", box=True)
h1, l1 = a.get_legend_handles_labels()
h2, l2 = a2.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.title(a, "A  Mouse schedule (11 cycles)")

extra = np.arange(0, 9)
out = [run(np.r_[np.zeros(e), Q])[1][-1] for e in extra]
b.semilogy(extra, out, "o-", color=charts.line("protein"), lw=1.5, ms=4, label="extra symmetric cycles first")
b.semilogy(extra, out[0] * 2.0 ** extra, color=P_.muted(), lw=0.8, ls="--", label=r"$\propto 2^{n}$")
for n_c, tok in ((28, "drug"),):
    kk = np.arange(1, n_c + 1)
    Qs = 1 / (1 + np.exp(-(kk - 8 * n_c / 11) / (1.1 * n_c / 11)))
    Qs[-1] = 1.0
    b.axhline(run(Qs)[1][-1], color=charts.line(tok), lw=1.0, ls="-.", label=f"same shape over {n_c} cycles")
charts.style_axes(b, "extra symmetric cycles before neurogenesis", "neurons per founder")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
charts.title(b, "B  Delaying neurogenesis")
