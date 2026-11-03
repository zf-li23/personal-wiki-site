"""A Wright-Fisher genealogy drawn with wikibio.evolution.genealogy: 10 haploid gene copies over 16
generations (oldest at the top), each linked to the parental copy it was drawn from, the lineages ancestral
to the last generation in ink. Right: the number of distinct ancestors of the 10 copies of the last generation
against generations back: this genealogy (steps), the mean over 2000 simulated Wright-Fisher populations of 10
copies (dots), and the coalescent expectation from exponential waiting times with rate k(k - 1)/2 per 10
generations (line, computed by integrating the death process of lineages)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(24, 10)
out = evo.genealogy(ax, (0.5, 0.6), 10, 16, width=11, height=8.6, p0=0.5, rng=np.random.default_rng(11))
ax.text(0.6, 9.55, "A  Wright–Fisher population, 10 gene copies", fontsize=FT["small"], color=P.ink(), weight="bold")
ax.annotate("", xy=(12.0, 9.0), xytext=(12.0, 1.0), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.9))
ax.text(12.3, 5.0, "time", rotation=90, va="center", fontsize=FT["tiny"], color=P.muted())

par, n, G = out["parents"], 10, 16
anc = list(range(n))
counts = [n]
for g in range(G - 1, 0, -1):
    anc = sorted(set(par[g][anc]))
    counts.append(len(anc))
b = charts.axes_at(ax, (15.0, 1.3, 8.4, 7.6))
b.step(np.arange(len(counts)), counts, where="post", color=P.ink(), lw=1.4, label="this genealogy")
rng = np.random.default_rng(2)
T = 40
mean = np.zeros(T)
for r in range(2000):
    a = np.arange(n)
    for t in range(T):
        mean[t] += len(a)
        a = np.unique(rng.integers(0, n, len(a)))
mean /= 2000
b.scatter(np.arange(T)[::2], mean[::2], s=10, color=charts.line("rna"), zorder=4, label="Wright–Fisher, mean")
Q = np.zeros((n + 1, n + 1))
for k in range(2, n + 1):
    rate = k * (k - 1) / 2 / n
    Q[k, k] = -rate
    Q[k, k - 1] = rate
tt = np.linspace(0, T, 200)
e = [expm(Q * x)[n] @ np.arange(n + 1) for x in tt]
b.plot(tt, e, color=charts.line("dna"), lw=1.6, label="coalescent")
b.set_xlim(0, T)
b.set_ylim(0, 10.5)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "generations back", "ancestral lineages")
charts.title(b, "B  Lineages of the last generation")
