"""Binary hydrides across the periodic table (periods 1-6, lanthanoids omitted), classified by bond type.
The 'hydride gap' (groups 6-11 except Pd and Cu) forms no stable binary hydrides under ordinary conditions."""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

rows = [
    "H . . . . . . . . . . . . . . . . He",
    "Li Be . . . . . . . . . . B C N O F Ne",
    "Na Mg . . . . . . . . . . Al Si P S Cl Ar",
    "K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr",
    "Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe",
    "Cs Ba La Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn",
]
kind = {}
for s in "Li Na K Rb Cs Ca Sr Ba".split():
    kind[s] = "ionic"
for s in "Be Mg Al Cu Zn Cd".split():
    kind[s] = "polymeric"
for s in "Sc Y La Ti Zr Hf V Nb Ta Pd".split():
    kind[s] = "metallic"
for s in "H B C N O F Si P S Cl Ga Ge As Se Br Sn Sb Te I Pb Bi Po".split():
    kind[s] = "molecular"
colors = {"ionic": "C0", "polymeric": "C4", "metallic": "C1", "molecular": "C2"}
names = {
    "ionic": "ionic (saline)",
    "polymeric": "intermediate / polymeric",
    "metallic": "metallic (interstitial)",
    "molecular": "molecular (covalent)",
}

fig, ax = plt.subplots(figsize=(11, 4.4))
for i, row in enumerate(rows):
    for j, sym in enumerate(row.split()):
        if sym == ".":
            continue
        k = kind.get(sym)
        face = colors[k] if k else "none"
        ax.add_patch(Rectangle((j, -i), 0.94, 0.94, facecolor=face, alpha=0.45 if k else None,
                               edgecolor="0.5", lw=0.6))
        ax.text(j + 0.47, -i + 0.47, sym, ha="center", va="center", fontsize=10)
for k, c in colors.items():
    ax.add_patch(Rectangle((0, 0), 0, 0, facecolor=c, alpha=0.45, label=names[k]))
ax.add_patch(Rectangle((0, 0), 0, 0, facecolor="none", edgecolor="0.5", label="no stable binary hydride"))
ax.text(7.97, -1.45, "hydride gap (groups 6-11)", ha="center", fontsize=9, style="italic")
ax.set_xlim(-0.1, 18.1)
ax.set_ylim(-5.2, 1.1)
ax.set_aspect("equal")
ax.axis("off")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=5, frameon=False, fontsize=9)
fig.tight_layout()
