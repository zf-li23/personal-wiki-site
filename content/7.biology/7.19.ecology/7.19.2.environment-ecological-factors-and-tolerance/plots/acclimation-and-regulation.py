# A: Thermal tolerance polygon of a eurythermal fish (stylized after the goldfish data of Fry, Brett and
#    Clawson 1942). Upper and lower incipient lethal temperatures rise linearly with acclimation temperature,
#    U = 26 + 0.4 Ta and L = -10.5 + 0.65 Ta (fitted through 2.5-34 C at Ta = 20 C and 9-38 C at Ta = 30 C),
#    L is bounded below by the freezing point (0 C) and U above by an ultimate upper limit of 41 C.
#    The enclosed area (in C^2) is a measure of thermal tolerance.
# B: Regulators and conformers: internal state against external state (schematic). A conformer follows the
#    environment (slope 1); a perfect regulator holds the internal state at its set point between the limits
#    of regulation; a partial regulator has slope beta = 0.3.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.3))

Ta = np.linspace(0, 40, 401)
U = np.minimum(26 + 0.4 * Ta, 41.0)
L = np.clip(-10.5 + 0.65 * Ta, 0, None)
ok = U > L
a.fill_between(Ta[ok], L[ok], U[ok], color=P.light("dna"), lw=0)
a.plot(Ta[ok], U[ok], color=P.edge("negative"), lw=2, label="upper lethal temperature")
a.plot(Ta[ok], L[ok], color=P.edge("dna"), lw=2, label="lower lethal temperature")
a.plot([0, 41], [0, 41], color=P.muted(), lw=0.8, ls=":")
a.text(36.5, 34.0, "Ta = lethal", fontsize=7.5, color=P.muted(), rotation=40)
for t0, lo, hi in ((20, 2.5, 34), (30, 9, 38)):
    a.plot([t0, t0], [lo, hi], color=P.ink(), lw=1, ls="--")
    a.plot([t0, t0], [lo, hi], "o", color=P.ink(), ms=4)
    a.text(t0 + 0.6, (lo + hi) / 2, "%g–%g °C" % (lo, hi), fontsize=7.5, color=P.ink())
area = np.trapezoid(np.clip(U - L, 0, None), Ta)
a.text(4, 36, "tolerance zone\narea ≈ %.0f °C²" % area, fontsize=8, color=P.edge("dna"))
a.set_xlim(0, 42)
a.set_ylim(0, 45)
a.set_xlabel("Acclimation temperature Ta / °C")
a.set_ylabel("Lethal temperature / °C")
a.legend(frameon=False, fontsize=8, loc="lower right")
a.set_title("A  Tolerance polygon", loc="left", fontweight="bold")

x = np.linspace(0, 40, 401)
setp, lo, hi = 25.0, 8.0, 34.0
reg = np.where(x < lo, setp - (lo - x), np.where(x > hi, setp + (x - hi), setp))
part = setp + 0.3 * (x - setp)
b.plot(x, x, color=P.edge("rna"), lw=2, label="conformer")
b.plot(x, reg, color=P.edge("dna"), lw=2, label="regulator")
b.plot(x, part, color=P.edge("enzyme"), lw=2, ls="--", label="partial regulator")
b.axvspan(lo, hi, color=P.light("neutral"), lw=0, alpha=0.6)
b.text((lo + hi) / 2, 3, "range of regulation", ha="center", fontsize=8, color=P.muted())
b.set_xlim(0, 40)
b.set_ylim(0, 40)
b.set_xlabel("External state (temperature, osmolality)")
b.set_ylabel("Internal state")
b.legend(frameon=False, fontsize=8, loc="upper left")
b.set_title("B  Regulation and conformity", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
