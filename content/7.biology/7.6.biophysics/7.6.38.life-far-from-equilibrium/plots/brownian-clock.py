# Precision and cost of a Brownian clock: a ring of N states traversed with forward rate k+ and backward
# rate k-, the cycle affinity A = N ln(k+/k-) dissipated per revolution. A: the relative variance of the
# number of completed cycles, times their mean, eps^2 M = coth(A/2N)/N, against A for several N. The
# thermodynamic uncertainty relation gives eps^2 M >= 2 kBT/A (dashed); a finite number of states adds
# the floor 1/N. B: distribution of the time to complete ten cycles (time in units of the mean period)
# for three clocks, from 10,000 simulated runs each: more states and more dissipation make the clock regular.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
A = np.logspace(-0.5, 4, 400)
for N, tok in ((1, "rna"), (3, "atp"), (10, "enzyme"), (30, "dna"), (100, "protein")):
    ax.plot(A, 1 / np.tanh(A / (2 * N)) / N, color=charts.line(tok), lw=1.8, label=f"$N$ = {N}")
ax.plot(A, 2 / A, color=P.ink(), lw=1.2, ls="--", label="TUR $2k_{\\mathrm{B}}T/\\mathcal{A}$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_ylim(3e-4, 10)
ax.legend(fontsize=7.5, frameon=False, loc="lower left", ncol=2)
charts.style_axes(ax, "dissipation per cycle $\\mathcal{A}/k_{\\mathrm{B}}T$", "relative variance per cycle $\\varepsilon^2 M$")
charts.title(ax, "A   States and free energy both limit precision")

ax = axs[1]
M = 10
for N, Aff, tok in ((3, 10, "rna"), (30, 30, "enzyme"), (30, 300, "dna")):
    x = Aff / N
    # rates with k+ - k- = N (mean period 1)
    km = N / (np.exp(x) - 1)
    kp = km * np.exp(x)
    reps = 10000
    pos = np.zeros(reps, int)
    t = np.zeros(reps)
    done = np.zeros(reps, bool)
    T = np.zeros(reps)
    while not done.all():
        idx = np.where(~done)[0]
        t[idx] += rng.exponential(1 / (kp + km), idx.size)
        pos[idx] += np.where(rng.random(idx.size) < kp / (kp + km), 1, -1)
        hit = idx[pos[idx] >= N * M]
        T[hit] = t[hit]
        done[hit] = True
    ax.hist(T, bins=np.linspace(5, 15, 60), density=True, histtype="step", lw=1.6, color=charts.line(tok),
            label=f"$N$ = {N}, $\\mathcal{{A}}$ = {Aff} $k_{{\\mathrm{{B}}}}T$: CV {T.std() / T.mean():.3f}")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "time to complete 10 cycles / mean period", "probability density")
charts.title(ax, "B   Ten ticks of three clocks")
fig.tight_layout()
