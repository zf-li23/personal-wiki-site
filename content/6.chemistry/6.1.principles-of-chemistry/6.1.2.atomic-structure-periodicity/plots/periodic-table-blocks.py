"""Periodic table coloured by block, with IUPAC and traditional A/B group labels."""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
           "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
           "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi "
           "Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds "
           "Rg Cn Nh Fl Mc Lv Ts Og").split()
COLORS = {"s": "C0", "p": "C1", "d": "C2", "ds": "C4", "f": "C3"}


def position(Z):
    """Return (period row, column 1-18 or f-row column, block)."""
    if Z == 1:
        return 1, 1, "s"
    if Z == 2:
        return 1, 18, "s"
    starts = [(3, 2), (11, 3), (19, 4), (37, 5), (55, 6), (87, 7)]
    for z0, period in reversed(starts):
        if Z >= z0:
            k = Z - z0  # index within the period
            break
    if period <= 3:
        col = k + 1 if k < 2 else k + 11
    elif period <= 5:
        col = k + 1
    else:
        if k < 2:
            col = k + 1
        elif k < 17:  # La..Lu or Ac..Lr: f rows
            return period + 2, k + 1, "f"   # placed below the main table
        else:
            col = k - 14 + 1
    if col <= 2:
        block = "s"
    elif col <= 10:
        block = "d"
    elif col <= 12:
        block = "ds"
    else:
        block = "p"
    return period, col, block


fig, ax = plt.subplots(figsize=(12, 7.2))
for Z, sym in enumerate(SYMBOLS, start=1):
    row, col, block = position(Z)
    x = col if block != "f" else col + 1  # f rows start under group 3
    y = -row if block != "f" else -row - 0.4
    ax.add_patch(Rectangle((x - 0.47, y - 0.47), 0.94, 0.94, facecolor=COLORS[block],
                           alpha=0.35, edgecolor="0.5", lw=0.6))
    ax.text(x, y + 0.12, sym, ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(x, y - 0.26, str(Z), ha="center", va="center", fontsize=6)

# placeholders in group 3 for the f series
for row, text in [(6, "57-71"), (7, "89-103")]:
    ax.add_patch(Rectangle((3 - 0.47, -row - 0.47), 0.94, 0.94, facecolor=COLORS["f"],
                           alpha=0.18, edgecolor="0.5", lw=0.6, ls="--"))
    ax.text(3, -row, text, ha="center", va="center", fontsize=6.5)

AB = ["IA", "IIA", "IIIB", "IVB", "VB", "VIB", "VIIB", "VIII", "VIII", "VIII", "IB", "IIB",
      "IIIA", "IVA", "VA", "VIA", "VIIA", "0"]
for g in range(1, 19):
    top = 1 if g in (1, 18) else (2 if g in (2,) or g >= 13 else 4)
    ax.text(g, -top + 0.72, f"{g}\n{AB[g - 1]}", ha="center", va="bottom", fontsize=7.5)
for p in range(1, 8):
    ax.text(0.2, -p, str(p), ha="center", va="center", fontsize=9)
ax.text(0.2, -0.3, "period", ha="center", fontsize=7)
ax.text(3.4, -8.4, "lanthanoids", ha="right", va="center", fontsize=8)
ax.text(3.4, -9.4, "actinoids", ha="right", va="center", fontsize=8)

for k, (name, label) in enumerate([("s", "s block"), ("p", "p block"), ("d", "d block"),
                                   ("ds", "ds block"), ("f", "f block")]):
    ax.add_patch(Rectangle((3.4 + 1.85 * k - 0.3, -2.0 - 0.25), 0.6, 0.5, facecolor=COLORS[name],
                           alpha=0.35, edgecolor="0.5", lw=0.6))
    ax.text(3.4 + 1.85 * k + 0.4, -2.0, label, va="center", fontsize=8.5)

ax.set_xlim(-0.4, 18.6)
ax.set_ylim(-10.0, 0.4)
ax.set_aspect("equal")
ax.axis("off")
fig.tight_layout()
