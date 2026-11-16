# Degree-day predictions along a latitudinal gradient (simplified climate, illustrative).
# Daily mean temperature T(phi, n) = M(phi) - A(phi) cos(2 pi (n - 15) / 365) with M = 22 - 0.56 (phi - 23) C and
# A = 7.6 + 0.43 (phi - 23) C, roughly matching the coast of eastern Asia between 20 and 50 N (Guangzhou to
# Harbin); degree-days above a threshold C = 10 C accumulate from 1 January.
# A: day of year on which a spring event requiring 150 degree-days (e.g. emergence of an insect) is reached,
#    in the present climate and with uniform warming of 1 and 2 C.
# B: number of generations per year of an insect with a thermal constant K = 400 degree-days per generation,
#    if it develops whenever T > C (no diapause).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
n = np.arange(1, 366)
lat = np.linspace(20, 50, 121)
C, F, K = 10.0, 150.0, 400.0


def temps(phi, warm=0.0):
    M = 22 - 0.56 * (phi - 23) + warm
    A = 7.6 + 0.43 * (phi - 23)
    return M - A * np.cos(2 * np.pi * (n - 15) / 365)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.3))
for warm, tok in ((0, "dna"), (1, "atp"), (2, "negative")):
    days = []
    gens = []
    for phi in lat:
        dd = np.cumsum(np.clip(temps(phi, warm) - C, 0, None))
        days.append(n[np.argmax(dd >= F)] if dd[-1] >= F else np.nan)
        gens.append(dd[-1] / K)
    lab = "present" if warm == 0 else "+%d °C" % warm
    a.plot(lat, days, color=P.edge(tok), lw=2, label=lab)
    b.plot(lat, gens, color=P.edge(tok), lw=2, label=lab)
    if warm == 0:
        d = np.array(days)
        ok = (lat >= 30) & (lat <= 45)
        slope = np.polyfit(lat[ok], d[ok], 1)[0]
a.text(21, 112, "about %.1f days later\nper degree of latitude\n(30–45° N)" % slope, fontsize=8, color=P.edge("dna"))
a.set_xlabel("Latitude / ° N")
a.set_ylabel("Day of year (150 degree-days > 10 °C)")
a.legend(frameon=False, fontsize=8, loc="lower right")
a.set_title("A  Date of a spring event", loc="left", fontweight="bold")
b.set_xlabel("Latitude / ° N")
b.set_ylabel("Generations per year (K = 400 °C d)")
b.legend(frameon=False, fontsize=8, loc="upper right")
b.set_title("B  Potential voltinism", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
