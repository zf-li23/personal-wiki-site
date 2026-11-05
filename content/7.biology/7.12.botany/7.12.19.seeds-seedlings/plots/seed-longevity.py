# Seed longevity under the Ellis-Roberts viability equation (Ellis & Roberts 1980, barley constants):
# v = Ki - p / sigma,  log10(sigma) = KE - CW log10(m) - CH T - CQ T^2  (sigma in days).
# (A) Survival curves for several storage environments (moisture content m in % fresh weight,
# temperature T in degrees C); dots mark p50 = Ki * sigma. (B) p50 (years) over moisture content and
# temperature; the genebank condition (-18 C, 5 %) is marked.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

KE, CW, CH, CQ = 9.983, 5.896, 0.040, 0.000428
Ki = 2.0


def sigma(m, T):
    return 10 ** (KE - CW * np.log10(m) - CH * T - CQ * T ** 2)


fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw=dict(width_ratios=[1.15, 1]))
conds = [(15, 30), (12, 20), (12, 5), (8, 20), (8, 5), (5, -18)]
cols = plt.cm.plasma(np.linspace(0.12, 0.85, len(conds)))
days = np.logspace(0, 8, 400)
for (m, T), c in zip(conds, cols):
    s = sigma(m, T)
    v = norm.cdf(Ki - days / s) * 100
    a.plot(days / 365.25, v, color=c, lw=2, label=f"{m} %, {T} °C")
    a.plot(Ki * s / 365.25, 50, "o", color=c, ms=5)
a.set_xscale("log")
a.set_xlim(1e-2, 1e5)
a.set_ylim(0, 102)
a.set_xlabel("Storage time / years")
a.set_ylabel("Viability / %")
a.set_title("A   Survival curves", loc="left", fontsize=11)
a.axhline(50, color="0.6", lw=0.6, ls=":")
a.legend(title="Moisture, temperature", fontsize=8, title_fontsize=8, frameon=False, loc="lower left")

mm = np.linspace(5, 25, 200)
TT = np.linspace(-20, 40, 200)
M, TG = np.meshgrid(mm, TT)
p50 = Ki * sigma(M, TG) / 365.25
levels = 10.0 ** np.arange(-3, 5)
cs = b.contourf(M, TG, np.log10(p50), levels=np.arange(-3, 4.6, 0.5), cmap="viridis")
cl = b.contour(M, TG, p50, levels=levels, colors="w", linewidths=0.6)
b.clabel(cl, fmt=lambda x: f"{x:g} y", fontsize=7)
b.plot(5.4, -17.2, "*", color="#ff4d4d", ms=13, mec="w", mew=0.6, clip_on=False, zorder=5)
b.annotate("genebank", (5.4, -17.2), (8.0, -16.0), fontsize=8, color="w", arrowprops=dict(arrowstyle="-", color="w", lw=0.6))
b.set_xlabel("Seed moisture content / %")
b.set_ylabel("Storage temperature / °C")
b.set_title("B   Time to 50 % viability", loc="left", fontsize=11)
cb = fig.colorbar(cs, ax=b, ticks=range(-3, 5))
cb.set_label("log10 p50 / years")
fig.tight_layout()
