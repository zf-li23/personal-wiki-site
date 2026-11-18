# Velocity of climate change along a south-north transect that crosses a lowland plain and a mountain range.
# Mean annual temperature T(x) = 20 - 0.007 x - 6.5 h(x) (x in km, elevation h in km; latitudinal
# gradient 0.7 degC per 100 km, lapse rate 6.5 degC per km). Warming of 0.03 degC per year.
# A: elevation and the position of the 10 degC isotherm now and after 80 years of warming.
# B: climate velocity v = (dT/dt) / |dT/dx| along the transect, compared with the asymptotic spreading
#    speeds 2 sqrt(rD) of three hypothetical species (7.19.17).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
x = np.linspace(0, 1000, 4001)
h = 0.1 + 2.6 * np.exp(-((x - 700) / 70) ** 2) + 1.2 * np.exp(-((x - 800) / 50) ** 2)
T = 20 - 0.007 * x - 6.5 * h
dTdx = np.gradient(T, x)
v = 0.03 / np.abs(dTdx)

fig, (a, b) = plt.subplots(2, 1, figsize=(8.6, 6.2), sharex=True, gridspec_kw={"height_ratios": [1, 1.2]})
a.fill_between(x, 0, h, color=P.light("bone"), lw=0)
a.plot(x, h, color=P.edge("bone"), lw=1.4)
for dT, tok, lab in ((0, "dna", "10 °C isotherm today"), (0.03 * 80, "negative", "after 80 years (+2.4 °C)")):
    zone = np.abs(T + dT - 10) < 0.06
    a.plot(x[zone], h[zone], "o", color=P.fill(tok), ms=4, label=lab)
a.set_ylabel("Elevation / km")
a.set_ylim(0, 3.2)
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_title("A  A lowland plain and a mountain range", loc="left", fontweight="bold")

b.plot(x, v, color=P.ink(), lw=1.6)
for s, tok, lab in ((0.05, "plant", "slow disperser (a tree)"), (0.5, "highlight", "intermediate"),
                    (5.0, "dna", "fast disperser (a butterfly)")):
    col = P.edge(tok) if tok == "highlight" else P.fill(tok)
    b.axhline(s, color=col, lw=1.4, ls="--")
    b.text(5, s * 1.15, f"{lab}: 2√(rD) = {s:g} km/yr", fontsize=7.5, color=col)
b.set_yscale("log")
b.set_ylim(0.005, 100)
b.set_xlim(0, 1000)
b.set_xlabel("Distance along the transect (south to north) / km")
b.set_ylabel("Climate velocity / km yr$^{-1}$")
b.set_title("B  Velocity of climate change", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
