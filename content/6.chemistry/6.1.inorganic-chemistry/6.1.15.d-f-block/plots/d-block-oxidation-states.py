"""Oxidation states of the 3d elements in their compounds (large filled circles: the most common
states; small open circles: less common states). Below: melting points of the 3d, 4d and 5d metals
(CRC Handbook), which peak in the middle of each series where most d electrons take part in bonding."""

import matplotlib.pyplot as plt

els = "Sc Ti V Cr Mn Fe Co Ni Cu Zn".split()
common = {"Sc": [3], "Ti": [4], "V": [4, 5], "Cr": [3, 6], "Mn": [2, 4, 7], "Fe": [2, 3],
          "Co": [2, 3], "Ni": [2], "Cu": [1, 2], "Zn": [2]}
other = {"Sc": [], "Ti": [2, 3], "V": [2, 3], "Cr": [2, 4, 5], "Mn": [3, 5, 6], "Fe": [4, 5, 6],
         "Co": [4], "Ni": [3, 4], "Cu": [3], "Zn": []}
mp = {
    "3d": ("Sc Ti V Cr Mn Fe Co Ni Cu Zn", [1541, 1668, 1910, 1907, 1246, 1538, 1495, 1455, 1085, 420]),
    "4d": ("Y Zr Nb Mo Tc Ru Rh Pd Ag Cd", [1522, 1855, 2477, 2623, 2157, 2334, 1964, 1555, 962, 321]),
    "5d": ("La Hf Ta W Re Os Ir Pt Au Hg", [920, 2233, 3017, 3422, 3186, 3033, 2446, 1768, 1064, -39]),
}

fig, (ax, bx) = plt.subplots(2, 1, figsize=(8, 8.2), gridspec_kw={"height_ratios": [1.15, 1]})
for i, e in enumerate(els):
    ax.plot([i] * len(common[e]), common[e], "o", color="C3", ms=11)
    ax.plot([i] * len(other[e]), other[e], "o", mfc="none", mec="C0", ms=7)
ax.plot(range(0, 6), [3, 4, 5, 6, 7, 6], color="0.6", lw=0.8, ls=":")
ax.text(4.1, 7.25, "highest state = group number up to Mn", fontsize=8, color="0.4")
ax.set_xticks(range(10))
ax.set_xticklabels(els)
ax.set_yticks(range(0, 9))
ax.set_ylim(0.3, 8)
ax.set_ylabel("oxidation state")
ax.set_title("(a) oxidation states of the 3d elements", fontsize=10)
ax.grid(axis="y", lw=0.4, alpha=0.5)

for k, (row, (names, t)) in enumerate(mp.items()):
    bx.plot(range(10), t, "o-", color=f"C{k}", label=row)
    for j, s in enumerate(names.split()):
        if s in ("W", "Hg", "Cr", "Mn", "Zn", "Os"):
            bx.annotate(s, (j, t[j]), xytext=(4, 4), textcoords="offset points", fontsize=8, color=f"C{k}")
bx.set_xticks(range(10))
bx.set_xticklabels([f"{g}" for g in range(3, 13)])
bx.set_xlabel("group")
bx.set_ylabel(r"melting point / $^\circ$C")
bx.set_title("(b) melting points of the d-block metals", fontsize=10)
bx.legend(frameon=False)
fig.tight_layout()
