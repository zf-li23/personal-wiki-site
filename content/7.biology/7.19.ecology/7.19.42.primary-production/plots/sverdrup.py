# Sverdrup's critical depth (Proposition 42.5.2).
# A: depth-integrated gross photosynthesis a I0 (1-exp(-K D))/K and losses r D (per unit biomass, a = 1),
#    K = 0.1 m^-1, I0 = 20, Ic = 1.3 mol photons m^-2 d^-1.
# B: schematic seasonal cycle at ~50 N: I0(t) = 25 - 20 cos(2 pi (t+10)/365) (5 in winter, 45 in summer),
#    mixed layer depth from 250 m (winter) to 25 m (summer); D_cr solved numerically.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio

P = bio.P
K, Ic = 0.1, 1.3


def dcr(I0):
    f = lambda D: D / (1 - np.exp(-K * D)) - I0 / (K * Ic)
    return brentq(f, 1e-6, 1e5)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.4))
I0 = 20.0
D = np.linspace(0.1, 250, 500)
gain = I0 * (1 - np.exp(-K * D)) / K
loss = Ic * D
a.plot(D, gain, color=P.edge("plant"), lw=2, label="integrated photosynthesis")
a.plot(D, loss, color=P.edge("negative"), lw=2, label="integrated losses")
Dc = dcr(I0)
zc = np.log(I0 / Ic) / K
a.axvline(zc, color=P.muted(), lw=0.9, ls=":")
a.axvline(Dc, color=P.ink(), lw=1.0, ls="--")
a.text(zc + 2, 30, f"compensation\ndepth {zc:.0f} m", fontsize=7.5, color=P.ink())
a.text(Dc + 2, 30, f"critical\ndepth {Dc:.0f} m", fontsize=7.5, color=P.ink())
a.fill_between(D, loss, gain, where=gain > loss, color=P.fill("positive"), alpha=0.35, lw=0)
a.set_xlabel("Mixed layer depth D / m")
a.set_ylabel("Per unit biomass (relative units)")
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A  The critical depth criterion", loc="left", fontweight="bold")

day = np.arange(0, 366)
I0t = 25 - 20 * np.cos(2 * np.pi * (day + 10) / 365)
Dcr = np.array([dcr(v) for v in I0t])
mld = 137.5 + 112.5 * np.cos(2 * np.pi * (day - 40) / 365)
mld = np.where((day > 40) & (day < 220), np.maximum(25, 250 - (day - 40) * 2.6), mld)
mld = np.clip(mld, 25, 250)
b.plot(day, Dcr, color=P.edge("plant"), lw=2, label="critical depth")
b.plot(day, mld, color=P.edge("dna"), lw=2, label="mixed layer depth")
b.fill_between(day, 0, 400, where=mld < Dcr, color=P.fill("positive"), alpha=0.25, lw=0,
               label="net growth possible")
i = np.argmax(mld < Dcr)
b.annotate("bloom begins", (day[i], mld[i]), xytext=(day[i] + 25, 330), fontsize=8, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
b.set_ylim(400, 0)
b.set_xlim(0, 365)
b.set_xticks([0, 59, 120, 181, 243, 304, 365], ["Jan", "Mar", "May", "Jul", "Sep", "Nov", ""])
b.set_ylabel("Depth / m")
b.legend(frameon=False, fontsize=8, loc="lower right")
b.set_title("B  Seasonal cycle (schematic)", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
