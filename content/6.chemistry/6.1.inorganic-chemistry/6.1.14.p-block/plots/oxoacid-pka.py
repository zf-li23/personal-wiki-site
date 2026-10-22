"""Pauling's first rule for oxoacids (HO)kXOm: pKa1 is about 7 - 5m, where m is the number of
oxygen atoms not bonded to hydrogen. Values at 25 C; open markers: estimated values of very strong acids.
H3BO3 is a Lewis acid (B(OH)3 + H2O -> B(OH)4- + H+) and is shown for comparison."""

import numpy as np
import matplotlib.pyplot as plt

acids = [  # (m, pKa1, label, estimated)
    (0, 7.53, "HClO", False), (0, 8.6, "HBrO", False), (0, 10.6, "HIO", False),
    (0, 9.2, "As(OH)$_3$", False), (0, 9.8, "Si(OH)$_4$", False), (0, 7.7, "Te(OH)$_6$", False),
    (0, 9.27, "B(OH)$_3$", False),
    (1, 1.96, "HClO$_2$", False), (1, 1.86, "H$_2$SO$_3$", False), (1, 2.16, "H$_3$PO$_4$", False),
    (1, 2.25, "H$_3$AsO$_4$", False), (1, 3.25, "HNO$_2$", False), (1, 1.3, "H$_3$PO$_3$", False),
    (1, 1.2, "H$_3$PO$_2$", False), (1, 2.62, "H$_2$SeO$_3$", False),
    (2, -1.4, "HNO$_3$", False), (2, 0.78, "HIO$_3$", False), (2, -1.0, "HClO$_3$", True),
    (2, -3.0, "H$_2$SO$_4$", True), (3, -8.0, "HClO$_4$", True),
]
rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(7.5, 5))
m = np.linspace(-0.2, 3.2, 10)
ax.plot(m, 7 - 5 * m, color="0.5", lw=1.2, ls="--", label=r"$\mathrm{p}K_{\mathrm{a1}} = 7 - 5m$")
offsets = {}
for mm, pk, lab, est in acids:
    k = offsets.get(mm, 0)
    offsets[mm] = k + 1
    dx = 0.09 * ((k % 5) - 2)
    ax.plot(mm + dx, pk, "o", color="C0", mfc="none" if est else "C0", ms=6)
    side = 1 if k % 2 == 0 else -1
    ax.annotate(lab, (mm + dx, pk), xytext=(8 * side, 0), textcoords="offset points", fontsize=8,
                ha="left" if side > 0 else "right", va="center")
ax.set_xticks([0, 1, 2, 3])
ax.set_xlabel("number of non-hydroxyl oxygen atoms $m$")
ax.set_ylabel(r"$\mathrm{p}K_{\mathrm{a1}}$")
ax.set_xlim(-0.6, 3.6)
ax.legend(frameon=False)
fig.tight_layout()
