# Miami model (Lieth 1975): NPP_T = 3000/(1+exp(1.315-0.119 T)), NPP_P = 3000 (1-exp(-0.000664 P)),
# NPP = min(NPP_T, NPP_P), g dry matter m^-2 yr^-1. Boundary P*(T) where the two are equal.
# C: Rosenzweig (1968): log10 NPP = 1.66 log10 AET - 1.66.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P


def npp_t(T):
    return 3000 / (1 + np.exp(1.315 - 0.119 * T))


def npp_p(Pm):
    return 3000 * (1 - np.exp(-0.000664 * Pm))


fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.4, 4.2))
T = np.linspace(-15, 32, 300)
a.plot(T, npp_t(T), color=P.edge("negative"), lw=2, label="temperature, NPP$_T$")
a.set_xlabel("Mean annual temperature / °C", color=P.edge("negative"))
a.set_ylabel("NPP / g m⁻² yr⁻¹ (dry matter)")
a.set_ylim(0, 3100)
a2 = a.twiny()
Pm = np.linspace(0, 4000, 300)
a2.plot(Pm, npp_p(Pm), color=P.edge("dna"), lw=2)
a2.set_xlabel("Annual precipitation / mm", color=P.edge("dna"))
a.text(-13, 2700, "NPP$_T$", color=P.edge("negative"), fontsize=9)
a.text(-13, 2450, "NPP$_P$", color=P.edge("dna"), fontsize=9)
a.set_title("A  The two limits", loc="left", fontweight="bold", pad=34)

TT, PP = np.meshgrid(np.linspace(-15, 30, 181), np.linspace(0, 4000, 201))
Z = np.minimum(npp_t(TT), npp_p(PP))
cs = b.contourf(TT, PP, Z, levels=np.arange(0, 3001, 250), cmap="YlGn")
b.contour(TT, PP, Z, levels=[500, 1000, 1500, 2000, 2500], colors=[P.muted()], linewidths=0.5)
Tl = np.linspace(-15, 30, 200)
Pstar = -np.log(1 - npp_t(Tl) / 3000) / 0.000664
b.plot(Tl, Pstar, color=P.ink(), lw=1.6, ls="--")
b.text(-12, 2600, "temperature-\nlimited", fontsize=8, color=P.ink())
b.text(21, 250, "water-\nlimited", fontsize=8, color=P.ink())
cities = [("Harbin", 4.9, 530), ("Beijing", 12.9, 570), ("Urumqi", 7.3, 290), ("Wuhan", 17.0, 1270),
          ("Guangzhou", 22.6, 1830)]
for n, t_, p_ in cities:
    b.plot(t_, p_, "o", ms=4, color=P.ink(), mec="white", mew=0.6)
    off = (-48, 4) if n == "Guangzhou" else (3, 3)
    b.annotate(n, (t_, p_), xytext=off, textcoords="offset points", fontsize=7, color=P.ink())
b.set_ylim(0, 4000)
b.set_xlabel("Mean annual temperature / °C")
b.set_ylabel("Annual precipitation / mm")
cb = fig.colorbar(cs, ax=b, fraction=0.05, pad=0.02)
cb.set_label("NPP / g m⁻² yr⁻¹", fontsize=8)
b.set_title("B  NPP = min(NPP$_T$, NPP$_P$)", loc="left", fontweight="bold", pad=28)

aet = np.linspace(100, 1500, 200)
c.plot(aet, 10 ** (1.66 * np.log10(aet) - 1.66), color=P.edge("plant"), lw=2)
for v in (300, 1000):
    y = 10 ** (1.66 * np.log10(v) - 1.66)
    c.plot(v, y, "o", color=P.edge("plant"), ms=4)
    c.annotate(f"{y:.0f}", (v, y), xytext=(5, -10), textcoords="offset points", fontsize=8, color=P.ink())
c.set_xlabel("Actual evapotranspiration / mm yr⁻¹")
c.set_ylabel("NPP / g m⁻² yr⁻¹")
c.set_title("C  Rosenzweig (1968)", loc="left", fontweight="bold", pad=28)
for ax in (a, b, c):
    for s in ("right",):
        ax.spines[s].set_visible(False)
for ax in (b, c):
    ax.spines["top"].set_visible(False)
a2.spines["right"].set_visible(False)
fig.tight_layout()
