"""Frontier-orbital energies in Diels-Alder reactions (schematic). The smaller HOMO-LUMO gap between
the two components dominates (arrow). Normal electron demand: a donor-substituted diene (raised HOMO)
and an acceptor-substituted dienophile (lowered LUMO). A Lewis acid bound to the carbonyl of the
dienophile lowers its LUMO further. Inverse electron demand: an electron-poor diene such as a
1,2,4,5-tetrazine (very low LUMO) and an electron-rich or strained dienophile."""

exec(open("orbitals.txt").read())

cases = [
    ("butadiene + ethene", (-9.1, 1.0), (-10.5, 1.8)),
    ("normal demand", (-8.3, 1.3), (-10.9, 0.0)),
    ("with a Lewis acid", (-8.3, 1.3), (-11.8, -1.0)),
    ("inverse demand", (-10.6, -1.6), (-8.6, 2.2)),
]
fig, axes = plt.subplots(1, 4, figsize=(9.6, 4.2), sharey=True)
for ax, (title, (hd, ld), (hp, lp)) in zip(axes, cases):
    level(ax, 0, hd, w=0.8, n=2, color="C0")
    level(ax, 0, ld, w=0.8, color="C0")
    level(ax, 2, hp, w=0.8, n=2, color="C3")
    level(ax, 2, lp, w=0.8, color="C3")
    g1, g2 = ld - hp, lp - hd  # diene LUMO - dienophile HOMO, dienophile LUMO - diene HOMO
    for (x0, y0, x1, y1, g) in ((0.4, hd, 1.6, lp, g2), (0.4, ld, 1.6, hp, g1)):
        main = g <= min(g1, g2) + 1e-9
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="<->", lw=1.8 if main else 0.8, ls="-" if main else ":", color=ink()))
    ax.text(0, -13.0, "diene", ha="center", color="C0", fontsize=9)
    ax.text(2, -13.0, "dienophile", ha="center", color="C3", fontsize=9)
    ax.set_title(title, fontsize=9.5, color=ink())
    ax.set_xlim(-0.8, 2.8)
    ax.set_ylim(-13.6, 3.2)
    ax.set_xticks([])
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
axes[0].set_ylabel("orbital energy / eV (schematic)")
fig.tight_layout()
