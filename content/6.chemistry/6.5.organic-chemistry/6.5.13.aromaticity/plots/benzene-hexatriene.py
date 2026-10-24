"""Hueckel pi levels of benzene (cyclic, n = 6) and hexa-1,3,5-triene (chain, n = 6), in units of |beta|
relative to alpha (energy upward). Dots are the six pi electrons; numbers give the nodal planes.
Total pi energy: benzene 6 alpha + 8 beta, hexatriene 6 alpha + 6.988 beta."""

import numpy as np
import matplotlib.pyplot as plt

ink = plt.rcParams["text.color"]
ring = np.diag(np.ones(5), 1) + np.diag(np.ones(5), -1)
ring[0, 5] = ring[5, 0] = 1
chain = np.diag(np.ones(5), 1) + np.diag(np.ones(5), -1)
fig, ax = plt.subplots(figsize=(6.4, 4.6))
for x0, mat, name, nodes in ((0, ring, "benzene", [0, 1, 1, 2, 2, 3]), (3, chain, "hexatriene", [0, 1, 2, 3, 4, 5])):
    x = np.sort(np.linalg.eigvalsh(mat))[::-1]  # bonding (x > 0) first
    e = -x  # energy upward in units of |beta|
    groups = {}
    for k, val in enumerate(e):
        groups.setdefault(round(val, 6), []).append(k)
    electrons = 6
    for val, ks in groups.items():
        m = len(ks)
        for j, k in enumerate(ks):
            cx = x0 + (j - (m - 1) / 2) * 0.75
            ax.hlines(val, cx - 0.3, cx + 0.3, color="C0" if val < 0 else "C3", lw=2.5)
            occ = min(2, electrons)
            electrons -= occ
            for q in range(occ):
                ax.plot(cx + (q - 0.5) * 0.18, val + 0.09, "o", ms=4, color=ink)
            ax.text(cx, val - 0.18, str(nodes[k]), ha="center", va="center", fontsize=7, color="0.5")
        ax.text(x0 + 1.05, val, f"{val:+.3f}", va="center", fontsize=8)
    total = 2 * sum(x[:3])
    ax.text(x0, -2.75, f"{name}\n" + r"$E_\pi = 6\alpha + %.3f\beta$" % total, ha="center", va="top", fontsize=9)
ax.axhline(0, color="0.6", lw=0.8, ls="--")
ax.text(4.9, 0.06, r"$\alpha$", fontsize=9, va="bottom")
ax.set_xlim(-1.2, 5.2)
ax.set_ylim(-3.5, 2.4)
ax.set_xticks([])
ax.set_ylabel(r"$(E - \alpha)/|\beta|$")
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
