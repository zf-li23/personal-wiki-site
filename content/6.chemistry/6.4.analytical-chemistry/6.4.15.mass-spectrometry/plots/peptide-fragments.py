"""b/y fragment ladder of the tryptic peptide LVNELTEFAK (bovine serum albumin), [M+2H]2+ m/z 582.32:
cleavage of each amide bond gives an N-terminal b ion and a C-terminal y ion (singly charged,
monoisotopic). Top: the ladder; bottom: a schematic CID spectrum (intensities illustrative)."""

import numpy as np
import matplotlib.pyplot as plt

res = dict(A=71.03711, E=129.04259, F=147.06841, K=128.09496, L=113.08406, N=114.04293, T=101.04768, V=99.06841)
pep = "LVNELTEFAK"
mp, water = 1.007276, 18.010565
n = len(pep)
b = [sum(res[a] for a in pep[:i]) + mp for i in range(1, n)]
y = [sum(res[a] for a in pep[i:]) + water + mp for i in range(1, n)]  # y[i - 1] holds the last n - i residues

fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.4, 6.0), gridspec_kw={"height_ratios": [1, 1.6]})
# Ladder.
for k, aa in enumerate(pep):
    ax.text(k, 0, aa, ha="center", va="center", fontsize=14, family="monospace")
for i in range(1, n):
    x = i - 0.5
    ax.plot([x, x], [-0.35, 0.35], color="0.5", lw=0.8)
    ax.plot([x, x - 0.18], [0.35, 0.35], color="C0", lw=1.2)
    ax.plot([x, x + 0.18], [-0.35, -0.35], color="C3", lw=1.2)
    ax.text(x - 0.05, 0.55, f"b$_{{{i}}}$\n{b[i - 1]:.1f}", ha="center", va="bottom", fontsize=7.5, color="C0")
    ax.text(x + 0.05, -0.55, f"y$_{{{n - i}}}$\n{y[i - 1]:.1f}", ha="center", va="top", fontsize=7.5, color="C3")
ax.text(-0.9, 0, r"H$_2$N", ha="right", va="center", fontsize=10)
ax.text(n - 0.1, 0, "COOH", ha="left", va="center", fontsize=10)
ax.set_xlim(-1.6, n + 0.6)
ax.set_ylim(-1.6, 1.6)
ax.axis("off")

# Schematic MS/MS spectrum: y ions (C-terminal Lys keeps the charge) dominate.
yint = {1: 25, 2: 30, 3: 55, 4: 70, 5: 100, 6: 60, 7: 85, 8: 40, 9: 15}
bint = {2: 45, 3: 20, 4: 30, 6: 12, 7: 8}
for i in range(1, n):
    j = n - i  # number of residues in the y ion
    if j in yint:
        bx.vlines(y[i - 1], 0, yint[j], color="C3", lw=1.6)
        bx.text(y[i - 1], yint[j] + 2, f"y$_{{{j}}}$", ha="center", fontsize=8, color="C3")
    if i in bint:
        bx.vlines(b[i - 1], 0, bint[i], color="C0", lw=1.6)
        bx.text(b[i - 1], bint[i] + 2, f"b$_{{{i}}}$", ha="center", fontsize=8, color="C0")
prec = (sum(res[a] for a in pep) + water + 2 * mp) / 2
bx.vlines(prec, 0, 10, color="0.5", lw=1.2, ls="--")
bx.text(prec - 8, 12, "precursor\n$[\\mathrm{M}+2\\mathrm{H}]^{2+}$", ha="right", fontsize=7.5, color="0.4")
# Mark one residue step: y5 - y4 = Thr.
y4, y5 = y[n - 5], y[n - 6]
bx.annotate("", xy=(y4, 108), xytext=(y5, 108), arrowprops=dict(arrowstyle="<->", lw=0.8))
bx.text((y4 + y5) / 2, 111, f"T ({y5 - y4:.2f})", ha="center", fontsize=8)
bx.set_xlim(100, 1150)
bx.set_ylim(0, 122)
bx.set_xlabel("$m/z$")
bx.set_ylabel("relative intensity")
bx.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
