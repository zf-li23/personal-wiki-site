# Osmoconformers and osmoregulators as a one-compartment flux balance (illustrative parameters).
# Internal osmolality Ci (mOsm/kg) relaxes passively toward the medium Co with permeance P, and an active
# transport flux Ja (ion uptake > 0, ion extrusion < 0) opposes deviations from a set point:
#   P (Co - Ci) + Ja(Ci) = 0,   Ja = Jmax tanh(G (Cset - Ci) / Jmax)   (saturating, gain G near the set point)
# Conformer: Ja = 0.  Hyper-regulator (shore-crab-like): uptake only (Ja >= 0), set point 750.
# Hyper-hypo-regulator (teleost-like): uptake and extrusion, low permeance, set point 320.
# B: thermodynamic minimum power of the pumps, |Ja| * RT |ln(Co/Ci)| (arbitrary units), for the teleost with
# its normal permeance and with half of it: the cost vanishes at the isosmotic point and grows with the
# gradient, and lowering permeability is the cheapest way to reduce it.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq


def steady(Co, P, Jmax, G, Cset, uptake_only=False):
    def ja(Ci):
        if Jmax == 0:
            return 0.0
        j = Jmax * np.tanh(G * (Cset - Ci) / Jmax)
        return max(j, 0.0) if uptake_only else j

    f = lambda Ci: P * (Co - Ci) + ja(Ci)
    Ci = brentq(f, 1e-6, 3000.0)
    return Ci, ja(Ci)


Co = np.linspace(5, 1200, 400)
models = [
    ("Osmoconformer (Ci = Co)", dict(P=1.0, Jmax=0.0, G=1.0, Cset=0.0), "#7a7a7a", ":"),
    ("Hyper-regulator", dict(P=1.0, Jmax=450.0, G=4.0, Cset=750.0, uptake_only=True), "#2f6fb5", "-"),
    ("Hyper-hypo-regulator", dict(P=0.25, Jmax=220.0, G=30.0, Cset=320.0), "#c0392b", "-"),
]

fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.3))
for name, p, c, ls in models:
    Ci = [steady(x, **p)[0] for x in Co]
    axa.plot(Co, Ci, color=c, lw=2, ls=ls, label=name)
axa.axvline(1000, color="#9e9e9e", lw=0.8)
axa.text(1005, 60, "seawater", fontsize=8.5, rotation=90, va="bottom")
axa.axvline(10, color="#9e9e9e", lw=0.8)
axa.text(25, 960, "fresh water", fontsize=8.5, rotation=90, va="top")
axa.set_xlim(0, 1200)
axa.set_ylim(0, 1200)
axa.set_xlabel("Medium osmolality Co (mOsm/kg)")
axa.set_ylabel("Body fluid osmolality Ci (mOsm/kg)")
axa.set_title("A  Steady state of the flux balance", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.06, 0.92))

Co2 = np.linspace(10, 1200, 400)
for P, c, lab in [(0.25, "#c0392b", "normal permeance"), (0.125, "#e08a3c", "permeance halved")]:
    cost = []
    for x in Co2:
        Ci, J = steady(x, P=P, Jmax=220.0, G=30.0, Cset=320.0)
        cost.append(abs(J) * abs(np.log(x / Ci)))
    axb.plot(Co2, cost, color=c, lw=2, label=lab)
axb.axvline(320, color="#9e9e9e", lw=0.8, ls="--")
axb.text(330, 5, "isosmotic", fontsize=8.5, rotation=90, va="bottom")
axb.set_xlim(0, 1200)
axb.set_ylim(bottom=0)
axb.set_xlabel("Medium osmolality Co (mOsm/kg)")
axb.set_ylabel("Minimum pump power (arb. units)")
axb.set_title("B  Cost of regulation (teleost model)", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper center")
for ax in (axa, axb):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
