# Saturable carrier uptake and the length of intestine needed to absorb a glucose load (plug-flow model).
# A chyme parcel moves along the small intestine at 1 cm/min (300 cm in 5 h). Luminal glucose C (mM)
# in the parcel falls as the epithelium takes it up:
#   dC/dt = -[Vmax C / (Km + C) + k_p C]
# Vmax = 1.0 mM/min is the carrier-mediated (SGLT1) uptake expressed per volume of chyme, Km = 5 mM is
# an apparent constant that includes the unstirred layer, and k_p = 0.003 /min is the passive
# (paracellular, solvent-drag) component. A: uptake rate against luminal concentration. B: luminal
# glucose along the intestine for three loads; small loads are absorbed in the proximal jejunum, large
# loads spread distally, recruiting more of the gut's reserve capacity.
import matplotlib.pyplot as plt
import numpy as np

Vmax, Km, kp, v = 1.0, 5.0, 0.003, 1.0
C = np.linspace(0, 300, 300)
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.2))
axa.plot(C, Vmax * C / (Km + C), color="#2f6fb5", lw=2, label="carrier (SGLT1)")
axa.plot(C, kp * C, color="#d9822b", lw=2, label="passive")
axa.plot(C, Vmax * C / (Km + C) + kp * C, color="0.2", lw=2, ls="--", label="total")
axa.set_xlabel("Luminal glucose / mM")
axa.set_ylabel("Uptake / (mM per min)")
axa.set_title("A  Saturable plus passive uptake", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="lower right")

dt = 0.1
for C0, col in ((50, "#2a9d8f"), (150, "#2f6fb5"), (300, "#c0392b")):
    c, xs, cs = float(C0), [0.0], [float(C0)]
    t = 0.0
    while t < 300:
        c = max(c - dt * (Vmax * c / (Km + c) + kp * c), 0.0)
        t += dt
        xs.append(v * t)
        cs.append(c)
    xs = np.array(xs)
    cs = np.array(cs)
    axb.plot(xs, cs, color=col, lw=2, label=f"load {C0} mM")
    idx = np.argmax(cs < 0.05 * C0)
    if idx > 0:
        axb.plot(xs[idx], cs[idx], "o", color=col, ms=4)
axb.axvspan(0, 25, color="0.85", lw=0)
axb.text(12, 8, "duodenum", ha="center", va="bottom", fontsize=8, rotation=90, color="0.4")
axb.set_xlabel("Distance from pylorus / cm")
axb.set_ylabel("Luminal glucose / mM")
axb.set_xlim(0, 300)
axb.set_title("B  Where the load is absorbed", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper right")
fig.tight_layout()
