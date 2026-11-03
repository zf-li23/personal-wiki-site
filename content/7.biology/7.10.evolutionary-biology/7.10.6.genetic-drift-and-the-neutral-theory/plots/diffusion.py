"""Diffusion approximation. A: fixation probability u(p) = (1 - exp(-4 N s p)) / (1 - exp(-4 N s)) against the
initial frequency for 4Ns = -4, 0, 2, 5 and 20 (lines); dots: fraction fixed among 4000 simulated Wright-Fisher
populations of N = 50 (genic selection). B: neutral mean time until fixation or loss, -4N (p ln p + q ln q),
and mean time to fixation of the alleles that are fixed, -4N q ln q / p, in units of N generations; dots:
2000 simulated populations of N = 50 per initial frequency."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
N = 50
p = np.linspace(0.001, 0.999, 300)
rng = np.random.default_rng(3)
for S, tok in ((-4, "negative"), (0, "neutral"), (2, "dna"), (5, "enzyme"), (20, "rna")):
    s = S / (4 * N)
    u = p if S == 0 else (1 - np.exp(-S * p)) / (1 - np.exp(-S))
    a.plot(p, u, color=charts.line(tok), lw=1.6, label=f"$4Ns = {S}$")
    for p0 in (0.1, 0.3, 0.5, 0.7, 0.9):
        f, lo, hi = evo.fixation_probability(N, s, p0, reps=4000, rng=rng)
        a.scatter([p0], [f], s=10, color=charts.line(tok), zorder=4)
a.set_xlim(0, 1)
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "initial frequency $p$", "fixation probability $u(p)$")
charts.title(a, "A  Fixation probability")

q = 1 - p
b.plot(p, -4 * (p * np.log(p) + q * np.log(q)), color=charts.line("dna"), lw=1.8, label="fixation or loss")
b.plot(p, -4 * q * np.log(q) / p, color=charts.line("rna"), lw=1.8, ls="--", label="fixation, if fixed")
for p0 in (0.05, 0.2, 0.4, 0.6, 0.8, 0.95):
    k = np.full(2000, int(round(p0 * 2 * N)))
    T = np.zeros(2000)
    alive = np.ones(2000, bool)
    t = 0
    while alive.any():
        t += 1
        k[alive] = rng.binomial(2 * N, k[alive] / (2 * N))
        done = alive & ((k == 0) | (k == 2 * N))
        T[done] = t
        alive &= ~done
    b.scatter([p0], [T.mean() / N], s=12, color=charts.line("dna"), zorder=4)
    b.scatter([p0], [T[k == 2 * N].mean() / N], s=12, color=charts.line("rna"), zorder=4)
b.set_xlim(0, 1)
b.set_ylim(0, 4.3)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "initial frequency $p$", "mean time ($N_{\\mathrm{e}}$ generations)")
charts.title(b, "B  Neutral absorption times")
