"""Drift and selection. A: substitution rate of slightly deleterious mutations relative to the neutral rate,
the average of 2N u(s) over an exponential distribution of selective disadvantages with mean s_bar (genic
selection, Kimura's u for a new mutation, N_e = N), against N, for s_bar = 1e-5, 1e-4 and 1e-3.
B: fixation probability of a new underdominant mutation (fitnesses 1, 1 - s_h, 1) relative to a neutral one,
2N u(1/2N), from the diffusion formula u(p) = int_0^p G / int_0^1 G with G(x) = exp(4 N s_h x (1 - x)),
against N s_h (N = 1000); dots: simulated Wright-Fisher populations of N = 50 (40 000 per point)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.15, top=0.9, wspace=0.3)


def rel_u(N, s):
    """2N u(1/2N) for genic selection with coefficient s (s < 0 deleterious)."""
    S = 4 * N * s
    with np.errstate(over="ignore", invalid="ignore"):
        u = np.where(np.abs(S) < 1e-9, 1 / (2 * N), (1 - np.exp(-2 * s)) / (1 - np.exp(-S)))
    return 2 * N * u


Ns = np.logspace(2, 7.5, 120)
for sb, tok in ((1e-5, "dna"), (1e-4, "enzyme"), (1e-3, "rna")):
    xs = sb * np.logspace(-7, 1.6, 6000)              # disadvantages, integrated against the exponential density
    dens = np.exp(-xs / sb) / sb
    k = [np.trapezoid(dens * rel_u(N, -xs), xs) + xs[0] / sb for N in Ns]
    a.semilogx(Ns, k, color=charts.line(tok), lw=1.8, label=f"$\\bar s = 10^{{{int(np.log10(sb))}}}$")
a.axhline(1, color=P.muted(), lw=0.8, ls=":")
a.set_ylim(0, 1.05)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "effective population size $N$", "substitution rate / $\\mu$")
charts.title(a, "A  Slightly deleterious mutations")

N = 1000
x = np.linspace(0, 6, 60)
rel = []
for v in x:
    sh = v / N
    G = lambda y: np.exp(4 * N * sh * y * (1 - y))
    rel.append(2 * N * quad(G, 0, 1 / (2 * N))[0] / quad(G, 0, 1, limit=200)[0])
b.semilogy(x, rel, color=charts.line("negative"), lw=1.8, label="diffusion, $N = 1000$")
rng = np.random.default_rng(7)
n = 50
for v in (0.5, 1, 2, 3):
    sh = v / n
    k = np.ones(40000, int)
    fixed = 0
    while len(k):
        pp = k / (2 * n)
        w11, w12, w22 = 1.0, 1 - sh, 1.0
        wb = pp * pp * w22 + 2 * pp * (1 - pp) * w12 + (1 - pp) ** 2 * w11
        pn = (pp * pp * w22 + pp * (1 - pp) * w12) / wb
        k = rng.binomial(2 * n, pn)
        fixed += int((k == 2 * n).sum())
        k = k[(k > 0) & (k < 2 * n)]
    b.scatter([v], [max(fixed, 0.5) / 40000 * 2 * n], s=16, color=P.ink(), zorder=4)
b.scatter([], [], s=16, color=P.ink(), label="simulated, $N = 50$")
b.axhline(1, color=P.muted(), lw=0.8, ls=":")
b.set_xlim(0, 6)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "$N s_{\\mathrm{h}}$", "fixation probability / neutral")
charts.title(b, "B  Crossing a valley by drift")
