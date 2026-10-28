"""Two quantitative sex-determining systems. A: complementary sex determination (honey bee csd): expected
fraction of diploid males among the diploid offspring of a queen, for k equally frequent csd alleles in the
population, with random mating (1/k, line; points: simulation of 2000 colonies with one or 15 drones) and with
brother-sister mating (1/4). B: temperature-dependent sex determination: logistic reaction norm
P(male) = 1 / (1 + exp(beta (T - Tp))) with pivotal temperature Tp = 29 degrees C (illustrative; turtles with warm
females)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
a = axs[0]
ks = np.arange(2, 41)
a.plot(ks, 1 / ks, color=charts.line("protein"), lw=2, label="random mating: 1/k")
a.axhline(0.25, color=charts.line("negative"), lw=1.6, ls="--", label="brother-sister mating: 1/4")
for drones, tok, mk in ((1, "dna", "o"), (15, "enzyme", "s")):
    sim = []
    for k in ks[::3]:
        f = []
        for _ in range(2000):
            q = rng.choice(k, 2, replace=False)
            dr = rng.integers(0, k, drones)
            # each diploid egg: one queen allele (random), father = random drone
            ql = q[rng.integers(0, 2, 400)]
            fl = dr[rng.integers(0, drones, 400)]
            f.append(np.mean(ql == fl))
        sim.append(np.mean(f))
    a.plot(ks[::3], sim, mk, color=charts.line(tok), ms=4, label=f"simulation, {drones} drone{'s' if drones > 1 else ''}")
a.set_ylim(0, 0.55)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "number of $\\it{csd}$ alleles $k$", "diploid males among diploid offspring")
charts.title(a, "A  Complementary sex determination")
b = axs[1]
T = np.linspace(24, 34, 200)
for beta, tok in ((1.0, "neutral"), (2.5, "drug"), (6.0, "negative")):
    b.plot(T, 1 / (1 + np.exp(beta * (T - 29))), color=charts.line(tok), lw=2, label=f"$\\beta$ = {beta:g} " + "°C$^{-1}$")
b.axvline(29, color=P.muted(), lw=0.8, ls=":")
b.text(29.2, 0.92, "pivotal\ntemperature", fontsize=FT["tiny"], color=P.muted())
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "incubation temperature T / °C", "fraction of males")
charts.title(b, "B  Temperature-dependent sex determination")
