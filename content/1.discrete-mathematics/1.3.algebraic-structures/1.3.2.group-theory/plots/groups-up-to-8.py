"""All groups of order at most 8 up to isomorphism, 14 in all, with the result that decides each order.
Prime orders (2, 3, 5, 7) admit only the cyclic group (Lagrange's theorem: every element other than e
generates the whole group). Order 4: Z_4 or the Klein group, according to whether an element of order 4
exists. Order 6: Z_6 and the non-abelian S_3. Order 8: three abelian groups (by the structure theorem
for finite abelian groups) and two non-abelian ones, the dihedral group D_4 and the quaternion group Q_8."""

import matplotlib.pyplot as plt

rows = [
    (1, [r"\{e\}"], [], "trivial"),
    (2, [r"\mathbb{Z}_2"], [], "prime order"),
    (3, [r"\mathbb{Z}_3"], [], "prime order"),
    (4, [r"\mathbb{Z}_4", r"\mathbb{Z}_2 \times \mathbb{Z}_2"], [], "element of order 4 or not"),
    (5, [r"\mathbb{Z}_5"], [], "prime order"),
    (6, [r"\mathbb{Z}_6"], [r"S_3"], r"$\mathbb{Z}_6 \cong \mathbb{Z}_2 \times \mathbb{Z}_3$"),
    (7, [r"\mathbb{Z}_7"], [], "prime order"),
    (8, [r"\mathbb{Z}_8", r"\mathbb{Z}_4 \times \mathbb{Z}_2", r"\mathbb{Z}_2^3"], [r"D_4", r"Q_8"],
     "abelian: structure theorem"),
]
fig, ax = plt.subplots(figsize=(10, 5.6))
ax.text(0.1, 8.9, "order", fontsize=12, weight="bold")
ax.text(1.0, 8.9, "abelian", fontsize=12, weight="bold")
ax.text(5.9, 8.9, "non-abelian", fontsize=12, weight="bold")
ax.text(7.9, 8.9, "decided by", fontsize=12, weight="bold")
ax.plot([0, 11.4], [8.6, 8.6], color="0.6", lw=1.0)
for k, (n, ab, nab, why) in enumerate(rows):
    y = 8 - k
    if k % 2 == 0:
        ax.add_patch(plt.Rectangle((0, y - 0.45), 11.4, 0.9, fc="0.5", alpha=0.07, lw=0))
    ax.text(0.3, y, f"${n}$", fontsize=13, va="center")
    for i, g in enumerate(ab):
        ax.text(1.0 + 1.55 * i, y, f"${g}$", fontsize=13, va="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="C0", alpha=0.2, ec="C0"))
    for i, g in enumerate(nab):
        ax.text(5.9 + 0.9 * i, y, f"${g}$", fontsize=13, va="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="C1", alpha=0.25, ec="C1"))
    ax.text(7.9, y, why, fontsize=10, va="center", color="0.45")
ax.text(5.7, -0.2, "14 groups in all; the smallest non-abelian group is $S_3$, of order 6", ha="center", fontsize=11)
ax.set_xlim(0, 11.4); ax.set_ylim(-0.6, 9.3); ax.axis("off")
