# Cohort production and the Allen curve (Proposition 43.2.1), simulated cohort:
# N(t) = 1000 exp(-0.8 t) per 100 m^2, w(t) = 300 (1 - exp(-0.5 t))^3 g, t = 0..6 years.
# Production = integral of N dw = Delta B + elimination.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
t = np.linspace(0, 6, 601)
N = 1000 * np.exp(-0.8 * t)
w = 300 * (1 - np.exp(-0.5 * t)) ** 3
prod = np.trapezoid(N, w)
Bend = N[-1] * w[-1]
elim = prod - (Bend - N[0] * w[0])

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.3))
a.plot(t, N, color=P.edge("dna"), lw=2, label="survivors N")
a.set_xlabel("Age / years")
a.set_ylabel("Survivors N (per 100 m²)", color=P.edge("dna"))
a2 = a.twinx()
a2.plot(t, w, color=P.edge("rna"), lw=2)
a2.set_ylabel("Mean mass w / g", color=P.edge("rna"))
a.set_title("A  Survival and growth", loc="left", fontweight="bold")
a.spines["top"].set_visible(False)
a2.spines["top"].set_visible(False)

b.fill_between(w, 0, N, color=P.fill("dna"), alpha=0.35, lw=0, label=f"eliminated by mortality ≈ {elim/1000:.1f} kg")
b.fill_between([0, w[-1]], 0, N[-1], color=P.fill("dna"), alpha=0.9, lw=0,
               label=f"biomass of survivors at age 6 = {Bend/1000:.1f} kg")
b.plot(w, N, color=P.ink(), lw=2)
for age in (1, 2, 3, 4):
    i = np.argmin(abs(t - age))
    b.plot(w[i], N[i], "o", ms=4, color=P.ink())
    b.annotate(f"age {age}", (w[i], N[i]), xytext=(5, 5), textcoords="offset points", fontsize=7.5, color=P.ink())
b.text(110, 600, f"production = area under curve\n≈ {prod/1000:.1f} kg per 100 m²", fontsize=8.5, color=P.ink())
b.set_xlabel("Mean mass w / g")
b.set_ylabel("Survivors N (per 100 m²)")
b.set_xlim(0, 300)
b.set_ylim(0, 1050)
b.legend(frameon=False, fontsize=8, loc="center right")
b.set_title("B  Allen curve", loc="left", fontweight="bold")
for s in ("top", "right"):
    b.spines[s].set_visible(False)
fig.tight_layout()
