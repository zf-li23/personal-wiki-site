"""Population structure at equilibrium between drift, migration and mutation.
A: the island model, F_ST = 1 / (1 + 4 N m (n/(n-1))^2), against the number of migrants N m per generation,
for many demes (n large) and for two demes (n = 2, where the factor is 16). About one migrant per generation
keeps F_ST near 0.2 or below, whatever the deme size.
B: isolation by distance in a one-dimensional stepping-stone model, computed exactly from the recursion for
probabilities of identity by descent: a ring of 60 demes of N = 50 diploids, migration m = 0.1 per generation
(half to each neighbour, so the dispersal variance is sigma^2 = 0.1 deme spacings squared), mutation
mu = 1e-4 (infinite alleles). Dots: pairwise F_ST / (1 - F_ST) between demes d steps apart; line: the
prediction for a linear habitat, F_ST / (1 - F_ST) ~ a + d / (4 D sigma^2) with D = N demes per unit
(Rousset 1997), slope 0.05, which holds at distances small compared with the mutation-dispersal scale
sqrt(sigma^2 / (2 mu)) = 22 demes."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.28)

a = axs[0]
Nm = np.logspace(-2, 2, 300)
a.semilogx(Nm, 1 / (1 + 4 * Nm), color=charts.line("dna"), lw=2, label="many demes: $1/(1+4Nm)$")
a.semilogx(Nm, 1 / (1 + 16 * Nm), color=charts.line("rna"), lw=2, ls="--", label="two demes: $1/(1+16Nm)$")
a.axvline(1, color=P.muted(), lw=0.8, ls=":")
a.text(1.1, 0.9, "one migrant\nper generation", fontsize=FT["tiny"], color=P.muted(), va="top")
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "migrants per generation $N_e m$", "$F_{\\mathrm{ST}}$")
charts.title(a, "A  Island model")

b = axs[1]
n, N, m, mu = 60, 50, 0.1, 1e-4
M = np.zeros((n, n))
for i in range(n):
    M[i, i] = 1 - m
    M[i, (i - 1) % n] += m / 2
    M[i, (i + 1) % n] += m / 2
F = np.zeros((n, n))
for _ in range(40000):
    D = np.diag((1 - np.diag(F)) / (2 * N))
    F = (1 - mu) ** 2 * M @ (F + D) @ M.T
Fw = np.diag(F).mean()
d = np.arange(1, n // 2 + 1)
Fb = np.array([F[0, k] for k in d])
fst = (Fw - Fb) / (1 - Fb)
ratio = fst / (1 - fst)
b.scatter(d, ratio, s=14, color=charts.line("dna"), zorder=3, label="exact recursion")
sig2 = m
slope = 1 / (4 * N * sig2)
b.plot(d, ratio[0] + slope * (d - 1), color=charts.line("rna"), lw=1.6, ls="--",
       label="slope $1/(4D\\sigma^2) = 0.05$")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "distance $d$ (deme spacings)", "$F_{\\mathrm{ST}}/(1-F_{\\mathrm{ST}})$")
charts.title(b, "B  Isolation by distance, stepping-stone model")
