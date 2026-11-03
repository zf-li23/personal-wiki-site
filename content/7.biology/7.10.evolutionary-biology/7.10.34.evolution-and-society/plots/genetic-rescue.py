"""Drift in small populations and genetic rescue (Section 34.5.2). A: expected heterozygosity relative to
its initial value, H_t/H_0 = (1 - 1/(2 N_e))^t, for effective sizes 10, 50 and 500. B: simulation of
an isolated population of N_e = 15 (500 neutral loci, initial heterozygosity about 0.3): heterozygosity
declines and the inbreeding coefficient F = 1 - H_t/H_0 rises; at generation 30, 4 immigrants from a
large outbred population (blue) restore much of the lost variation, compared with no immigration (grey).
Under inbreeding depression, fitness is expected to fall with F and to recover after the rescue."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(12)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.28)
t = np.arange(0, 101)
for Ne, tok in ((10, "negative"), (50, "rna"), (500, "dna")):
    a.plot(t, (1 - 1 / (2 * Ne)) ** t, color=charts.line(tok), lw=2, label=f"$N_e$ = {Ne}")
a.set_ylim(0, 1.02)
charts.style_axes(a, "generations", r"$H_t/H_0$")
charts.title(a, "A  Loss of heterozygosity")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
L, N, G = 500, 15, 60
src = np.clip(rng.beta(0.5, 0.5, L), 0.05, 0.95)
H0 = np.mean(2 * src * (1 - src))
for rescue, tok, lab in ((False, "neutral", "no immigration"), (True, "dna", "4 immigrants at generation 30")):
    reps = []
    for r in range(30):
        p = src.copy()
        H = []
        for g in range(G):
            if rescue and g == 30:
                p = (2 * N * p + 2 * 4 * src) / (2 * N + 8)
            p = rng.binomial(2 * N, p) / (2 * N)
            H.append(np.mean(2 * p * (1 - p)) / H0)
        reps.append(H)
    b.plot(np.arange(1, G + 1), np.mean(reps, axis=0), color=charts.line(tok), lw=2, label=lab)
b.axvline(30, color=P.muted(), lw=0.7, ls=":")
b.set_ylim(0, 1.02)
charts.style_axes(b, "generations", r"$H_t/H_0 = 1 - F$")
charts.title(b, "B  Genetic rescue ($N_e$ = 15)")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
