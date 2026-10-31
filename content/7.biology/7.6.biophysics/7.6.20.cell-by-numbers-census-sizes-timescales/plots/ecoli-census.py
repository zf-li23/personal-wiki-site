"""A molecular census of one E. coli cell (B/r, 40 min doubling time, 37 C): numbers of molecules per
average cell on a logarithmic axis. Macromolecules from the classic compilation of Neidhardt (1990);
water and inorganic ions are estimates from a wet mass of about 1 pg (70 % water) and about 0.3 M total
ions. Open diamonds: the back-of-the-envelope estimates of Example 20.1.2 (proteins from the dry mass,
ribosomes from the fraction of protein mass in ribosomal proteins, lipids from the membrane area,
water from the wet mass)."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rows = [
    ("water", 2.3e10, "neutral"),
    ("inorganic ions", 2e8, "na"),
    ("phospholipids", 2.2e7, "lipid_head"),
    ("lipopolysaccharide", 1.4e6, "carbohydrate"),
    ("proteins", 2.4e6, "protein"),
    ("tRNA", 2.0e5, "trna"),
    ("ribosomes", 1.9e4, "rrna"),
    ("glycogen granules", 4.4e3, "carbohydrate"),
    ("mRNA", 1.4e3, "mrna"),
    ("DNA (genome equivalents)", 2.1, "dna"),
    ("peptidoglycan sacculus", 1.0, "cell_wall"),
]
est = {"proteins": 3e6, "ribosomes": 2.0e4, "phospholipids": 2.4e7, "water": 2.3e10}
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def sci(n):
    e = int(np.floor(np.log10(n)))
    if e < 3:
        return f"{n:g}"
    m = n / 10 ** e
    return f"{m:.2g} × 10{str(e).translate(SUP)}"


fig, ax = plt.subplots(figsize=(8.6, 4.4))
ys = np.arange(len(rows))[::-1]
for y, (name, n, tok) in zip(ys, rows):
    ax.barh(y, np.log10(n) + 0.5, left=-0.5, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.text(max(np.log10(n), np.log10(est.get(name, 1))) + 0.25, y, sci(n), va="center",
            fontsize=7, color=P.ink())
    if name in est:
        ax.plot([np.log10(est[name])], [y], marker="D", ms=6.5, mfc="none", mec=P.ink(), mew=1.2, zorder=5)
ax.set_yticks(ys)
ax.set_yticklabels([r[0] for r in rows], fontsize=7.5)
ax.set_xlim(-0.5, 11.6)
ax.set_xticks(range(0, 12, 2))
ax.set_xticklabels(["1", "10²", "10⁴", "10⁶", "10⁸", "10¹⁰"])
charts.style_axes(ax, "molecules per cell")
ax.plot([], [], marker="D", ls="none", mfc="none", mec=P.ink(), mew=1.2, label="estimate (Example 20.1.2)")
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
