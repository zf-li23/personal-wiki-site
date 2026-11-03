"""A mutation-accumulation experiment, simulated (Formula 4.4.2). 400 lines founded from one genotype are
propagated for 50 generations without selection. Each generation a line gains a Poisson number of new
mutations with mean U = 0.4 per genome; each lowers fitness by s, with s exponentially distributed with
mean 0.02, and effects add (illustrative values). A: fitness of 20 lines (grey) and the mean over all
400 (dots), with the expected decline 1 - U E[s] t. B: the variance of fitness among lines (line) and its
expectation U E[s^2] t (dashed), both rising linearly. The slopes give the Bateman-Mukai estimates U >= (dM)^2 / dV and E[s] <= dV / dM; with
exponential effects they recover half of the true U and twice the true E[s]."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(11)
L, T, U, ms = 400, 50, 0.4, 0.02
w = np.ones((T + 1, L))
for t in range(T):
    k = rng.poisson(U, L)
    w[t + 1] = w[t] - np.array([rng.exponential(ms, n).sum() for n in k])
g = np.arange(T + 1)
M, V = w.mean(1), w.var(1)
dM = -np.polyfit(g, M, 1)[0]
dV = np.polyfit(g, V, 1)[0]
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
for j in range(20):
    a.plot(g, w[:, j], color=P.muted(), lw=0.6, alpha=0.7)
a.plot(g[::5], M[::5], "o", color=charts.line("negative"), ms=4, label="mean of 400 lines")
a.plot(g, 1 - U * ms * g, color=charts.line("negative"), lw=1.4, label=r"$1 - U\,\mathbb{E}[s]\,t$")
a.set_ylim(0.4, 1.02)
charts.style_axes(a, "generation", "fitness relative to the founder")
charts.title(a, "A  Fitness declines")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
b.plot(g, V, color=charts.line("dna"), lw=1.6)
b.plot(g, U * 2 * ms ** 2 * g, color=P.muted(), lw=1.0, ls=(0, (3, 2)))
b.text(5, V.max() * 0.95, f"slopes: $\\Delta M = {dM:.4f}$, $\\Delta V = {dV:.5f}$ per generation\n"
       f"Bateman–Mukai: $U \\geq {dM ** 2 / dV:.2f}$ (true {U}),\n$\\mathbb{{E}}[s] \\leq {dV / dM:.3f}$ (true {ms})",
       fontsize=FT["tiny"], color=P.ink(), va="top")
charts.style_axes(b, "generation", "variance among lines")
charts.title(b, "B  Variance among lines increases")
