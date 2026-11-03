"""Structured coalescent in the island model: 10 demes of N = 50 diploids, each lineage migrating with
probability m per generation to one of the other 9 demes, coalescence with probability 1/(2N) per generation
for two lineages in the same deme (discrete-generation simulation). A: coalescence times of two copies
sampled from the same deme and from different demes (4Nm = 1; 20 000 pairs each), in units of 2nN
generations, with the means 2nN and 2nN + (n - 1)/(2m) of Eq. (7.11) (vertical lines). B: F_ST from mean
coalescence times, (T_bar - T0)/T_bar with T_bar = T0/n + (n - 1) T1/n, against 4Nm: simulated (dots),
Eq. (7.11) for 10 demes (line), and 1/(1 + 4Nm) (dashed)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(13)
nd, N = 10, 50


def times(m, same, reps):
    T = np.zeros(reps)
    together = np.full(reps, same)
    alive = np.ones(reps, bool)
    t = 0
    while alive.any():
        t += 1
        idx = np.where(alive)[0]
        tog = together[idx]
        coal = tog & (rng.random(len(idx)) < 1 / (2 * N))
        T[idx[coal]] = t
        alive[idx[coal]] = False
        idx, tog = idx[~coal], tog[~coal]
        mv = rng.random((len(idx), 2)) < m
        moved = mv.any(1)
        # if together and one moves: separate; if apart and a mover lands in the other's deme (1/(n-1)): together
        land = rng.random(len(idx)) < (mv.sum(1) / (nd - 1))
        new = np.where(tog, ~moved, land)
        together[idx] = new
    return T


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
m = 1 / (4 * N)
T0, T1 = times(m, True, 20000), times(m, False, 20000)
scale = 2 * nd * N
bins = np.linspace(0, 6, 61)
a.hist(T0 / scale, bins=bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, alpha=0.8,
       label="same deme")
a.hist(T1 / scale, bins=bins, density=True, histtype="step", color=charts.line("rna"), lw=1.5,
       label="different demes")
a.axvline(1, color=charts.line("dna"), lw=1, ls=":")
a.axvline((scale + (nd - 1) / (2 * m)) / scale, color=charts.line("rna"), lw=1, ls=":")
a.set_xlim(0, 6)
a.set_yscale("log")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "coalescence time (units of $2nN$ generations)", "density")
charts.title(a, "A  Island model, $n = 10$, $4Nm = 1$")
x = np.logspace(-1.3, 1.3, 100)
mm = x / (4 * N)
t0 = 2 * nd * N
t1 = t0 + (nd - 1) / (2 * mm)
tb = t0 / nd + (nd - 1) * t1 / nd
b.semilogx(x, (tb - t0) / tb, color=charts.line("dna"), lw=1.8, label="Eq. (7.11), 10 demes")
b.semilogx(x, 1 / (1 + x), color=P.ink(), lw=1, ls="--", label="$1/(1 + 4Nm)$")
for v in (0.1, 0.5, 2, 8):
    mv = v / (4 * N)
    s0, s1 = times(mv, True, 3000).mean(), times(mv, False, 3000).mean()
    sb = s0 / nd + (nd - 1) * s1 / nd
    b.scatter([v], [(sb - s0) / sb], s=18, color=P.ink(), zorder=4)
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "$4Nm$", "$F_{\\mathrm{ST}}$")
charts.title(b, "B  $F_{\\mathrm{ST}}$ from coalescence times")
