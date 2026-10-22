"""Frost diagram of manganese in acidic (pH 0) and basic (pH 14) solution, built from the Latimer
diagrams: the volt-equivalent N E0(X(N)/X(0)) is the running sum of z E0 of successive couples."""

import matplotlib.pyplot as plt

# (oxidation number, species, E0 of the couple joining it to the previous species below)
acid = [(0, "Mn", None), (2, r"Mn$^{2+}$", -1.18), (3, r"Mn$^{3+}$", 1.51),
        (4, r"MnO$_2$", 0.95), (6, r"MnO$_4^{2-}$", 2.26), (7, r"MnO$_4^-$", 0.56)]
base = [(0, "Mn", None), (2, r"Mn(OH)$_2$", -1.56), (3, r"Mn(OH)$_3$", 0.10),
        (4, r"MnO$_2$", -0.20), (6, r"MnO$_4^{2-}$", 0.60), (7, r"MnO$_4^-$", 0.56)]


def frost(latimer):
    pts, y, n_prev = [], 0.0, 0
    for n, name, e in latimer:
        if e is not None:
            y += (n - n_prev) * e
        pts.append((n, y, name))
        n_prev = n
    return pts


fig, ax = plt.subplots(figsize=(7, 4.8))
for data, col, lab, dy in [(acid, "C0", "acidic, pH 0", 0.25), (base, "C3", "basic, pH 14", -0.45)]:
    pts = frost(data)
    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o-", color=col, lw=1.6, label=lab)
    for n, y, name in pts:
        if n == 0 and col == "C3":
            continue
        ax.annotate(name, (n, y), xytext=(n + 0.08, y + dy), fontsize=9, color=col)
ax.axhline(0, color="0.6", lw=0.8, ls=":")
ax.set_xlabel("oxidation number $N$")
ax.set_ylabel(r"$N E^\circ$ / V")
ax.set_xticks(range(0, 8))
ax.set_xlim(-0.3, 7.8)
ax.set_ylim(-3.9, 6.0)
ax.set_title("Frost diagram of Mn: slope of a chord = $E^\\circ$ of that couple", fontsize=10)
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
