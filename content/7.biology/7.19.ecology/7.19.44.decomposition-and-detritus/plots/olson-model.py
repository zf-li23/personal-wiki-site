# Olson's model (Proposition 44.5.1).
# A: X(t)/X0 = exp(-k t) for k = 3, 0.8, 0.2, 0.03 /yr; circles at ln2/k, squares at 3/k.
# B: dX/dt = L - k X from X0 = 0 with L = 10, 4, 3, 1.5 t/ha/yr; steady state L/k (dotted).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
cases = [("tropical forest", 3.0, 10.0, "thylakoid"), ("temperate deciduous", 0.8, 4.0, "golgi"),
         ("boreal forest", 0.2, 3.0, "enzyme"), ("tundra", 0.03, 1.5, "dna")]
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.4))
t = np.logspace(-2, np.log10(300), 600)
for name, k, L, tok in cases:
    a.plot(t, 100 * np.exp(-k * t), color=P.edge(tok), lw=2, label=f"{name}, k = {k:g} yr⁻¹")
    a.plot(np.log(2) / k, 50, "o", color=P.edge(tok), ms=5)
    a.plot(3 / k, 100 * np.exp(-3), "s", color=P.edge(tok), ms=5)
a.axhline(50, color=P.muted(), lw=0.7, ls=":")
a.axhline(5, color=P.muted(), lw=0.7, ls=":")
a.set_xscale("log")
a.set_xlim(0.01, 300)
a.set_ylim(0, 102)
a.set_xlabel("Time / years (log scale)")
a.set_ylabel("Mass remaining / %")
a.legend(frameon=False, fontsize=7.5, loc="lower left")
a.set_title("A  Decay of a litter cohort", loc="left", fontweight="bold")

for name, k, L, tok in cases:
    X = L / k * (1 - np.exp(-k * t))
    b.plot(t, X, color=P.edge(tok), lw=2, label=f"{name}: L/k = {L/k:.3g} t ha⁻¹")
    b.axhline(L / k, color=P.edge(tok), lw=0.7, ls=":")
    b.plot(3 / k, 0.95 * L / k, "s", color=P.edge(tok), ms=5)
b.set_xscale("log")
b.set_xlim(0.01, 300)
b.set_xlabel("Time / years (log scale)")
b.set_ylabel("Litter on the ground / t ha⁻¹")
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_title("B  Accumulation to steady state", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
