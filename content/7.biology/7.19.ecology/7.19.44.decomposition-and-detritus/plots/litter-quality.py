# A: litter as three fractions decaying independently (soluble 10/yr, cellulose+hemicellulose 0.8/yr,
#    lignin and other recalcitrant compounds 0.1/yr) for 5%, 15%, 30% lignin (soluble 25%, 15%, 10%).
# B: net N mineralization per unit litter C decomposed, M/F = 1/r_L - e/r_m (Proposition 44.3.1),
#    microbial C:N r_m = 8, carbon use efficiency e = 0.3 and 0.4.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))
t = np.linspace(0, 6, 601)
ks = (10.0, 0.8, 0.1)
for (lig, sol), tok in zip(((0.05, 0.25), (0.15, 0.15), (0.30, 0.10)), ("plant", "antibody", "animal")):
    cel = 1 - lig - sol
    X = sol * np.exp(-ks[0] * t) + cel * np.exp(-ks[1] * t) + lig * np.exp(-ks[2] * t)
    k1 = -np.log(X[100])
    a.plot(t, X * 100, color=P.edge(tok), lw=2, label=f"{lig*100:.0f}% lignin (first-year k = {k1:.2f} yr⁻¹)")
    a.plot(t, 100 * np.exp(-k1 * t), color=P.edge(tok), lw=0.9, ls="--")
a.set_xlabel("Time / years")
a.set_ylabel("Mass remaining / %")
a.set_ylim(0, 100)
a.set_xlim(0, 6)
a.legend(frameon=False, fontsize=7.5)
a.set_title("A  Litter chemistry", loc="left", fontweight="bold")

rL = np.linspace(5, 120, 400)
rm = 8.0
b.axhline(0, color=P.muted(), lw=0.8)
for e, tok in ((0.3, "dna"), (0.4, "protein")):
    M = 1 / rL - e / rm
    b.plot(rL, M * 1000, color=P.edge(tok), lw=2, label=f"e = {e}: critical C:N = {rm/e:.0f}")
    b.plot(rm / e, 0, "o", color=P.edge(tok), ms=5)
b.fill_between(rL, -60, 0, color=P.fill("negative"), alpha=0.15, lw=0)
b.text(80, -15, "net immobilization", fontsize=8, color=P.ink(), ha="center")
b.text(60, 40, "net mineralization", fontsize=8, color=P.ink(), ha="center")
b.set_ylim(-60, 160)
b.set_xlim(5, 120)
b.set_xlabel("Litter C:N ratio")
b.set_ylabel("Net N mineralization / mg N per g C decomposed")
b.legend(frameon=False, fontsize=8)
b.set_title("B  Critical C:N ratio", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
