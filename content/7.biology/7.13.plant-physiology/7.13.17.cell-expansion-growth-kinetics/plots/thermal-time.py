# Temperature and development rate. (A) Cardinal-temperature (beta) model of development rate (Yan & Hunt
# 1999) for a warm-season crop (Tb = 10, To = 30, Tmax = 42 C; illustrative) and the linear thermal-time
# approximation used for growing degree days. (B) Accumulated growing degree days GDD = sum max(0, Tmean -
# Tb) over a simulated season (sinusoidal mean temperature plus day-to-day noise); the dashed line is a
# requirement of 1400 C d for maturity, reached at the marked date; a season 2 C warmer reaches it earlier.
import matplotlib.pyplot as plt
import numpy as np

Tb, To, Tm = 10.0, 30.0, 42.0
T = np.linspace(0, 46, 500)


def beta(T):
    x = np.clip(T, Tb, Tm)
    return ((Tm - x) / (Tm - To)) * ((x - Tb) / (To - Tb)) ** ((To - Tb) / (Tm - To))


fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.plot(T, beta(T), color="#c0504d", lw=2.4, label="beta model")
a.plot(T, np.clip((T - Tb) / (To - Tb), 0, None), color="0.4", lw=1.4, ls="--", label="linear (thermal time)")
for x, name in ((Tb, "T_b"), (To, "T_opt"), (Tm, "T_max")):
    a.axvline(x, color="0.7", lw=0.8, ls=":")
    a.text(x, 1.12, name.replace("_", ""), ha="center", fontsize=9)
a.set_xlabel("Mean temperature T / °C")
a.set_ylabel("Development rate (relative to optimum)")
a.set_xlim(0, 46)
a.set_ylim(0, 1.2)
a.legend(frameon=False, fontsize=8.5, loc="center right")
a.set_title("A   Three cardinal temperatures", loc="left", fontsize=10)
rng = np.random.default_rng(0)
d = np.arange(0, 200)
Tmean = 19 + 8 * np.sin((d - 40) / 365 * 2 * np.pi * 1.6) + rng.normal(0, 2.5, d.size)
for dT, col, name in ((0, "#2f6fb5", "season"), (2, "#c0504d", "season + 2 °C")):
    gdd = np.cumsum(np.clip(Tmean + dT - Tb, 0, None))
    b.plot(d, gdd, color=col, lw=2.2, label=name)
    k = np.argmax(gdd >= 1400)
    b.plot(d[k], gdd[k], "o", color=col, ms=6)
    b.annotate(f"day {d[k]}", xy=(d[k], 1400), xytext=(d[k] - 22 + 10 * dT, 1650 + 120 * dT), fontsize=8.5, color=col,
               arrowprops=dict(arrowstyle="-", color=col, lw=0.8))
b.axhline(1400, color="0.5", lw=1, ls="--")
b.set_xlabel("Days after sowing / d")
b.set_ylabel("Growing degree days / °C d")
b.set_xlim(0, 200)
b.set_ylim(0, 2400)
b.legend(frameon=False, fontsize=8.5, loc="upper left")
b.set_title("B   Accumulated thermal time (Tb = 10 °C)", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
