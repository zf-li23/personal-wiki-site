"""Groups 1 and 2: melting points of the metals and their chlorides, standard electrode potentials,
and the crystal radius of M+ compared with its limiting molar conductivity in water (25 C).
Data: CRC Handbook (melting points, E0, conductivities); Shannon radii for coordination number 6."""

import numpy as np
import matplotlib.pyplot as plt

g1 = ["Li", "Na", "K", "Rb", "Cs"]
g2 = ["Be", "Mg", "Ca", "Sr", "Ba"]
x = np.arange(5)
mp_metal1 = [180.5, 97.8, 63.5, 39.3, 28.4]
mp_metal2 = [1287, 650, 842, 777, 727]
mp_cl1 = [610, 801, 771, 718, 646]
mp_cl2 = [399, 714, 775, 874, 961]
e1 = [-3.040, -2.71, -2.931, -2.98, -3.026]
e2 = [-1.847, -2.372, -2.868, -2.899, -2.912]
r1 = [76, 102, 138, 152, 167]
lam1 = [38.7, 50.1, 73.5, 77.8, 77.2]

fig, axes = plt.subplots(2, 2, figsize=(10, 7.4))
ax = axes[0, 0]
ax.plot(x, mp_metal1, "o-", color="C0", label="group 1")
ax.plot(x, mp_metal2, "s-", color="C3", label="group 2")
ax.set_ylabel(r"melting point / $^\circ$C")
ax.set_title("(a) metals", fontsize=10)
ax.legend(frameon=False)

ax = axes[0, 1]
ax.plot(x, mp_cl1, "o-", color="C0", label=r"MCl")
ax.plot(x, mp_cl2, "s-", color="C3", label=r"MCl$_2$")
ax.set_ylabel(r"melting point / $^\circ$C")
ax.set_title("(b) chlorides", fontsize=10)
ax.legend(frameon=False, loc="lower right")

ax = axes[1, 0]
ax.plot(x, e1, "o-", color="C0", label=r"M$^+$/M")
ax.plot(x, e2, "s-", color="C3", label=r"M$^{2+}$/M")
ax.set_ylabel(r"$E^\circ$ / V")
ax.set_title("(c) standard electrode potentials", fontsize=10)
ax.legend(frameon=False, loc="upper right")

ax = axes[1, 1]
ax.plot(x, r1, "o-", color="C0", label="crystal radius of M$^+$ / pm")
ax.set_ylabel("crystal radius / pm", color="C0")
ax2 = ax.twinx()
ax2.plot(x, lam1, "^--", color="C2", label=r"$\lambda^\circ$(M$^+$)")
ax2.set_ylabel(r"$\lambda^\circ$ / (S cm$^2$ mol$^{-1}$)", color="C2")
ax.set_title("(d) bigger ion, faster ion: hydration shells", fontsize=10)

for a, labels in [(axes[0, 0], None), (axes[0, 1], None), (axes[1, 0], None), (axes[1, 1], None)]:
    a.set_xticks(x)
    if a is axes[1, 1]:
        a.set_xticklabels(g1)
    else:
        a.set_xticklabels([f"{p}/{q}" for p, q in zip(g1, g2)], fontsize=9)
fig.tight_layout()
