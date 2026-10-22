"""Normal boiling points: hydrides of groups 14-17 by period, and the n-alkanes by chain length (CRC Handbook values)."""

import numpy as np
import matplotlib.pyplot as plt

periods = [2, 3, 4, 5]
hydrides = {
    "group 14: CH4, SiH4, GeH4, SnH4": [-161.5, -111.9, -88.1, -51.8],
    "group 15: NH3, PH3, AsH3, SbH3": [-33.3, -87.8, -62.5, -17.0],
    "group 16: H2O, H2S, H2Se, H2Te": [100.0, -59.6, -41.3, -2.2],
    "group 17: HF, HCl, HBr, HI": [19.5, -85.0, -66.4, -35.6],
}
alkanes = [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7, 98.4, 125.6, 150.8, 174.1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))
for k, (label, bp) in enumerate(hydrides.items()):
    ax1.plot(periods, bp, "o-", color=f"C{k}", lw=1.5, label=label)
ax1.set_xticks(periods)
ax1.set_xlabel("period of the heavier atom")
ax1.set_ylabel(r"normal boiling point / $^\circ$C")
ax1.set_title("Hydrides: hydrogen bonding in NH3, H2O and HF", fontsize=10.5)
ax1.legend(fontsize=8.5, loc="upper center", ncol=1)
ax1.set_ylim(-180, 150)
ax1.grid(alpha=0.3)

n = np.arange(1, 11)
ax2.plot(n, alkanes, "o-", color="C0", lw=1.5, label="n-alkanes CnH2n+2")
ax2.plot([5, 5, 5], [36.1, 27.8, 9.5], "s", color="C3", ms=6)
for y, name in [(36.1, "n-pentane"), (27.8, "isopentane"), (9.5, "neopentane")]:
    ax2.annotate(name, (5, y), xytext=(5.4, y - 30 + (0 if name != "n-pentane" else 15)), fontsize=8.5,
                 arrowprops=dict(arrowstyle="-", color="0.5", lw=0.7))
ax2.set_xticks(n)
ax2.set_xlabel("number of carbon atoms $n$")
ax2.set_ylabel(r"normal boiling point / $^\circ$C")
ax2.set_title("Dispersion forces grow with size, fall with branching", fontsize=10.5)
ax2.grid(alpha=0.3)
ax2.legend(fontsize=9, loc="upper left")
fig.tight_layout()
