# Effect of the O2 concentration on respiration and fermentation of stored produce (model, illustrative
# parameters). Aerobic CO2 release follows O2 with Michaelis-Menten kinetics (apparent Km = 2.5 % O2,
# reflecting diffusion into the tissue, RQ = 1); fermentative CO2 release is inhibited by O2,
# F = Fmax / (1 + (O2 / Ki)^2). Total CO2 has a minimum at a few % O2; fermentation is essentially gone at
# about 10 % O2 (extinction point). Right axis: RQ = total CO2 / O2 uptake.
import matplotlib.pyplot as plt
import numpy as np

o2 = np.linspace(0.05, 21, 800)
Vm, Km = 10.0, 2.5
Fm, Ki = 9.0, 1.2
aer = Vm * o2 / (Km + o2)
ferm = Fm / (1 + (o2 / Ki) ** 2)
tot = aer + ferm
rq = tot / aer
imin = np.argmin(tot)
iext = np.argmax(ferm < 0.02 * Fm)

fig, ax = plt.subplots(figsize=(8.6, 4.5))
ax.axvspan(2, 3, color="#4caf50", alpha=0.15, lw=0)
ax.text(2.5, 16.6, "CA storage", ha="center", fontsize=8)
ax.plot(o2, aer, color="#2f6fb5", lw=2, label="aerobic respiration")
ax.plot(o2, ferm, color="#d9822b", lw=2, label="fermentation")
ax.plot(o2, tot, color="0.15", lw=2.6, label="total CO₂ release")
ax.plot(o2[imin], tot[imin], "o", color="0.15", ms=6)
ax.annotate("minimum", (o2[imin], tot[imin]), (o2[imin] + 2, tot[imin] - 3.2), fontsize=9,
            arrowprops=dict(arrowstyle="-", color="0.4", lw=0.8))
ax.axvline(o2[iext], color="#d9822b", lw=0.8, ls=":")
ax.text(o2[iext] + 0.3, 15.0, "extinction point", fontsize=9, color="#b0661c")
ax.set_xlabel("O₂ concentration / %")
ax.set_ylabel("CO₂ release / (mg kg⁻¹ h⁻¹)")
ax.set_xlim(0, 21)
ax.set_ylim(0, 18)
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.spines["top"].set_visible(False)
ax2 = ax.twinx()
ax2.plot(o2, rq, color="#7a4fb3", lw=1.3, ls="--")
ax2.set_ylabel("RQ", color="#7a4fb3")
ax2.set_ylim(0, 6)
ax2.tick_params(axis="y", colors="#7a4fb3")
fig.tight_layout()
