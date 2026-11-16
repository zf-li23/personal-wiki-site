# Survival as a joint function of temperature and salinity (simulated response surface, in the spirit of
# Haefner's (1970) experiments on the sand shrimp Crangon septemspinosa; parameters illustrative).
# s(T, S) = exp(-(T - 15)^2 / (2 * 7^2)) * exp(-(S - 25)^2 / (2 * w(T)^2)),
# w(T) = 9 exp(-(T - 15)^2 / (2 * 9^2)): the tolerated salinity range is widest at the optimal temperature
# and narrows as temperature departs from it. A: contours of percent survival. B: survival against
# salinity at three temperatures (sections through the surface).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P


def surv(T, S):
    w = 9 * np.exp(-(T - 15) ** 2 / (2 * 9 ** 2))
    return np.exp(-(T - 15) ** 2 / (2 * 7 ** 2)) * np.exp(-(S - 25) ** 2 / (2 * w ** 2))


T = np.linspace(0, 32, 321)
S = np.linspace(0, 50, 401)
TT, SS = np.meshgrid(T, S)
Z = 100 * surv(TT, SS)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.4), gridspec_kw={"width_ratios": [1.15, 1]})
levels = [10, 30, 50, 70, 90]
cols = [P.light("dna"), P.fill("channel"), P.fill("dna"), P.edge("channel"), P.edge("dna")]
a.contourf(TT, SS, Z, levels=levels + [101], colors=cols)
cs = a.contour(TT, SS, Z, levels=levels, colors=[P.ink()], linewidths=0.6)
a.clabel(cs, fmt="%d%%", fontsize=7, colors=[P.ink()])
for t0, tok in ((8, "negative"), (15, "positive"), (24, "atp")):
    a.axvline(t0, color=P.edge(tok), lw=1.2, ls="--")
a.set_xlabel("Temperature / °C")
a.set_ylabel("Salinity / ‰")
a.set_title("A  Percent survival", loc="left", fontweight="bold")

for t0, tok in ((8, "negative"), (15, "positive"), (24, "atp")):
    b.plot(S, 100 * surv(t0, S), color=P.edge(tok), lw=2, label="%d °C" % t0)
b.set_xlabel("Salinity / ‰")
b.set_ylabel("Survival / %")
b.set_ylim(0, 105)
b.set_xlim(0, 50)
b.legend(frameon=False, fontsize=8)
b.set_title("B  Sections at fixed temperature", loc="left", fontweight="bold")
for s in ("top", "right"):
    b.spines[s].set_visible(False)
fig.tight_layout()
