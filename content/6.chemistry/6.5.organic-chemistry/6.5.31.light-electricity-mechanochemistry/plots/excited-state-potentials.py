"""Excited-state redox potentials of Ru(bpy)3(2+) (vs SCE, MeCN). Excitation adds E00 (about 2.1 eV,
from the 0-0 energy of the 3MLCT state) to both the reducing and the oxidizing power:
E(Ru3+/*Ru2+) = E(Ru3+/Ru2+) - E00 and E(*Ru2+/Ru+) = E(Ru2+/Ru+) + E00.
Left: the two ground-state couples; right: the two excited-state couples, with representative
substrates drawn at their reduction or oxidation potentials."""

import matplotlib.pyplot as plt

E00 = 2.10


def volts(e):
    """A signed potential with a true minus sign."""
    return f"{e:+.2f} V".replace("-", "\u2212")


ground = {"Ru$^{3+}$/Ru$^{2+}$": 1.29, "Ru$^{2+}$/Ru$^{+}$": -1.33}
excited = {"Ru$^{3+}$/*Ru$^{2+}$": 1.29 - E00, "*Ru$^{2+}$/Ru$^{+}$": -1.33 + E00}
substrates = [(-1.46, "PhCOCH$_2$Br (reduction)"), (-0.62, "BrCH(CO$_2$Et)$_2$ (reduction)"),
              (0.80, "N-methylacridane (oxidation)")]

fig, ax = plt.subplots(figsize=(8.2, 5.4))
ax.axhline(0, color="0.8", lw=0.8)
for x, couples, title in [(0.0, ground, "ground state"), (1.6, excited, "excited state (T$_1$, $^3$MLCT)")]:
    for name, e in couples.items():
        ax.plot([x, x + 0.9], [e, e], lw=2.2, color="C0" if "3+" in name else "C3")
        ax.text(x + 0.95, e, f"{name}  {volts(e)}", va="center", fontsize=9)
    ax.text(x + 0.45, 2.15, title, ha="center", fontsize=10)
for (a, b), c in [((1.29, 1.29 - E00), "C0"), ((-1.33, -1.33 + E00), "C3")]:
    ax.annotate("", (1.55, b), (0.95, a), arrowprops=dict(arrowstyle="-|>", color=c, lw=1.2, ls="--"))
ax.text(1.12, 0.55, r"$-E_{0,0}$", color="C0", fontsize=9, ha="right")
ax.text(1.12, -1.0, r"$+E_{0,0}$", color="C3", fontsize=9, ha="left")
for e, label in substrates:
    ax.plot([3.7, 3.9], [e, e], color="0.35", lw=1.6)
    ax.text(3.95, e, f"{label}  {volts(e)}", va="center", fontsize=8, color="0.35")
ax.set_xlim(-0.2, 6.2)
ax.set_ylim(-2.0, 2.4)
ax.set_xticks([])
ax.set_ylabel(r"$E$ / V vs SCE")
ax.invert_yaxis()
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
ax.text(0.0, -1.85, "more reducing", fontsize=8, color="0.4")
ax.text(0.0, 1.85, "more oxidizing", fontsize=8, color="0.4")
fig.tight_layout()
