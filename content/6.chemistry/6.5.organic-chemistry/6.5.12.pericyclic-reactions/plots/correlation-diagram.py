"""Orbital correlation diagrams for the butadiene / cyclobutene interconversion (Woodward-Hoffmann).
Each orbital is classified as symmetric (S) or antisymmetric (A) with respect to the symmetry element
kept along the path: the C2 axis for conrotation, the mirror plane for disrotation. Orbitals of the
same symmetry correlate (lowest with lowest, lines of equal symmetry do not cross). Conrotation
correlates the occupied psi1, psi2 with the occupied sigma, pi of cyclobutene: thermally allowed.
Disrotation correlates psi2 with pi*: a ground-state reactant would give a doubly excited product,
so the thermal reaction is forbidden (but allowed from the first excited state)."""

exec(open("orbitals.txt").read())

left = {"psi1": -1.62, "psi2": -0.62, "psi3": 0.62, "psi4": 1.62}
right = {"sigma": -2.3, "pi": -1.0, "pi*": 1.0, "sigma*": 2.3}
names = {"psi1": r"$\psi_1$", "psi2": r"$\psi_2$", "psi3": r"$\psi_3$", "psi4": r"$\psi_4$",
         "sigma": r"$\sigma$", "pi": r"$\pi$", "pi*": r"$\pi^*$", "sigma*": r"$\sigma^*$"}
sym = {
    "con": ({"psi1": "A", "psi2": "S", "psi3": "A", "psi4": "S"}, {"sigma": "S", "pi": "A", "pi*": "S", "sigma*": "A"}),
    "dis": ({"psi1": "S", "psi2": "A", "psi3": "S", "psi4": "A"}, {"sigma": "S", "pi": "S", "pi*": "A", "sigma*": "A"}),
}
fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.6))
for ax, (mode, title) in zip(axes, (("con", r"conrotatory (keeps $C_2$)"), ("dis", r"disrotatory (keeps $\sigma$)"))):
    sl, sr = sym[mode]
    for k, e in left.items():
        level(ax, 0, e, w=0.7, n=2 if k in ("psi1", "psi2") else 0)
        ax.text(-0.45, e, f"{names[k]} {sl[k]}", ha="right", va="center", fontsize=10, color=ink())
    for k, e in right.items():
        level(ax, 3, e, w=0.7)
        ax.text(3.45, e, f"{sr[k]} {names[k]}", ha="left", va="center", fontsize=10, color=ink())
    for s in ("S", "A"):
        lk = sorted([k for k in left if sl[k] == s], key=left.get)
        rk = sorted([k for k in right if sr[k] == s], key=right.get)
        for a, b in zip(lk, rk):
            color = "#d1495b" if (a == "psi2" and b == "pi*") or (a == "psi3" and b == "pi") else ink()
            ax.plot([0.35, 2.65], [left[a], right[b]], color=color, lw=1.2, ls=(0, (4, 2)))
    ax.axhline(0, xmin=0.05, xmax=0.95, color="0.6", lw=0.8, ls=":")
    ax.text(0, -3.1, "butadiene", ha="center", fontsize=10, color=ink())
    ax.text(3, -3.1, "cyclobutene", ha="center", fontsize=10, color=ink())
    ax.set_title(title, fontsize=10, color=ink())
    ax.set_xlim(-1.4, 4.4)
    ax.set_ylim(-3.4, 2.8)
    ax.axis("off")
axes[0].text(1.5, 2.6, "thermally allowed", ha="center", fontsize=9, color=ink())
axes[1].text(1.5, 2.6, "thermally forbidden", ha="center", fontsize=9, color="#d1495b")
fig.tight_layout()
