# A: Maas-Hoffman threshold-slope model of relative yield against soil salinity, Y = 100 - b (ECe - a) for
# ECe > a (ECe: electrical conductivity of the saturated-soil extract). Thresholds a (dS/m) and slopes b (% per
# dS/m) after Maas and Hoffman (1977) and Maas (1990): bean 1.0/19, maize 1.7/12, rice 3.0/12, wheat 6.0/7.1,
# cotton 7.7/5.2, barley 8.0/5.0. Top axis: approximate osmotic potential of the soil solution, -0.036 MPa per dS/m.
# B: Munns' two-phase model of growth after salt is added (illustrative): an immediate osmotic phase that slows
# growth of all genotypes, and a slower ionic phase that begins when Na+ in old leaves exceeds a toxic level;
# Na+ accumulates linearly at a rate set by the root's ability to exclude it.
import matplotlib.pyplot as plt
import numpy as np

fig, (a, b) = plt.subplots(1, 2, figsize=(12.5, 4.5))
crops = [("bean", 1.0, 19, "#8b1e3f"), ("maize", 1.7, 12, "#d9463b"), ("rice", 3.0, 12, "#d9a400"),
         ("wheat", 6.0, 7.1, "#2e9e5b"), ("cotton", 7.7, 5.2, "#3e7cb8"), ("barley", 8.0, 5.0, "#6e55a8")]
ec = np.linspace(0, 30, 600)
for n, th, sl, col in crops:
    y = np.clip(100 - sl * np.clip(ec - th, 0, None), 0, 100)
    a.plot(ec, y, color=col, lw=2.1, label=f"{n}: a = {th}, b = {sl}")
a.set_xlabel("Soil salinity $\\mathrm{EC_e}$ / (dS m$^{-1}$)")
a.set_ylabel("Relative yield / %")
a.set_xlim(0, 30)
a.set_ylim(0, 104)
a.legend(frameon=False, fontsize=8, loc="upper right")
a.set_title("A   Maas-Hoffman model", loc="left", fontsize=10)
top = a.secondary_xaxis("top", functions=(lambda x: -0.036 * x, lambda p: -p / 0.036))
top.set_xlabel("Osmotic potential of soil solution / MPa", fontsize=8.5)

t = np.linspace(0, 30, 600)
osm = 0.55  # growth retained in the osmotic phase
for name, J, col, ls in [("control (no salt)", None, "0.45", ":"), ("Na⁺ includer", 2.4, "#d9463b", "-"),
                         ("Na⁺ excluder", 0.6, "#2e9e5b", "--")]:
    if J is None:
        g = np.ones_like(t)
    else:
        na = J * t  # Na+ in old leaves, arbitrary units; toxic threshold 20
        ion = np.clip(1 - 0.06 * np.clip(na - 20, 0, None), 0.0, 1)
        g = np.where(t < 0.05, 1.0, osm * ion)
    b.plot(t, 100 * g, color=col, lw=2.2, ls=ls, label=name)
b.axvline(20 / 2.4, color="#d9463b", lw=0.7, ls="--")
b.text(20 / 2.4 + 0.4, 80, "old leaves of the includer\nreach toxic Na⁺", fontsize=8, color="#d9463b")
b.text(1.0, 60, "osmotic phase", fontsize=8.5, color="0.35")
b.text(12.8, 38, "ionic phase", fontsize=8.5, color="0.35")
b.set_xlabel("Time after salt is added / d")
b.set_ylabel("Shoot growth rate / % of control")
b.set_ylim(0, 110)
b.legend(frameon=False, fontsize=8.3, loc="lower right", bbox_to_anchor=(1.0, 0.06))
b.set_title("B   Two-phase growth response (schematic model)", loc="left", fontsize=10)
fig.tight_layout()
