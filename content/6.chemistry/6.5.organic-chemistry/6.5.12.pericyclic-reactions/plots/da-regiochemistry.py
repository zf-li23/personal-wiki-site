"""Regioselectivity of the Diels-Alder reaction from frontier-orbital coefficients (simple Hueckel
theory with heteroatom parameters: ether oxygen h = 2.0, k(C-O) = 0.8; carbonyl oxygen h = 1.0,
k(C=O) = 1.0). Lobe sizes follow the computed coefficients (numbers give |c|). The termini with the
larger coefficients bond to each other (dotted line): 1-methoxybutadiene (largest HOMO coefficient
at C4) with acrolein (largest LUMO coefficient at C-beta) gives the "ortho" (1,2) adduct;
2-methoxybutadiene (largest at C1) gives the "para" (1,4) adduct."""

exec(open("orbitals.txt").read())


def huckel(n, bonds, h):
    H = np.zeros((n, n))
    for i, j, k in bonds:
        H[i, j] = H[j, i] = -k
    for i, v in h.items():
        H[i, i] = -v
    return np.linalg.eigh(H)


_, v1 = huckel(5, [(0, 1, 0.8), (1, 2, 1), (2, 3, 1), (3, 4, 1)], {0: 2.0})  # O-C1=C2-C3=C4
_, v2 = huckel(5, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (1, 4, 0.8)], {4: 2.0})  # C1=C2(O)-C3=C4
_, va = huckel(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)], {3: 1.0})  # Cb=Ca-C=O
homo1, homo2, lumo = v1[1:5, 2], v2[:4, 2], va[:3, 2]


def lobe(ax, xy, c):
    porb(ax, xy, c, scale=0.25 + 0.9 * abs(c))


def draw(ax, diene_c, sub_at, sub_from, beta_right, title, text):
    top = [(1.3 * i, 1.7) for i in range(4)]
    atom_chain(ax, top)
    for p, c in zip(top, diene_c):
        lobe(ax, p, c)
        ax.text(p[0], 2.85, f"{abs(c):.2f}", ha="center", fontsize=8, color=ink())
    ax.plot(*zip(sub_from, sub_at), color=ink(), lw=1.4)
    right = sub_at[0] > sub_from[0]
    ax.text(sub_at[0] + (0.08 if right else -0.08), sub_at[1] + 0.1, "OMe", ha="left" if right else "right", va="center", fontsize=9, color=ink())
    xs = [3.9, 2.6, 1.3] if beta_right else [0.0, 1.3, 2.6]  # C-beta, C-alpha, carbonyl C
    bottom = [(x, -1.7) for x in xs]
    atom_chain(ax, bottom)
    for p, c in zip(bottom, lumo):
        lobe(ax, p, c)
        ax.text(p[0], -2.95, f"{abs(c):.2f}", ha="center", fontsize=8, color=ink())
    xo = xs[2] + (-0.6 if beta_right else 0.6)
    ax.plot([xs[2], xo + (0.15 if beta_right else -0.15)], [-1.7, -1.7], color=ink(), lw=1.4)
    ax.text(xo, -1.7, "O", ha="center", va="center", fontsize=9, color=ink())
    j = 3 if beta_right else 0
    ax.plot([top[j][0], bottom[0][0]], [1.0, -1.0], color=ink(), lw=1.2, ls=(0, (1, 2)))
    ax.text(-0.8, 1.7, "HOMO", ha="right", va="center", fontsize=9, color=ink())
    ax.text(-0.8, -1.7, "LUMO", ha="right", va="center", fontsize=9, color=ink())
    ax.text(1.95, -3.9, text, ha="center", fontsize=9, color=ink())
    ax.set_title(title, fontsize=10, color=ink())
    clean(ax, (-2.1, 4.7), (-4.3, 3.9))


fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
draw(axes[0], homo1, (-0.45, 2.3), (0, 1.7), True, "1-methoxybutadiene + acrolein", r"large C4 $\cdots$ large C$\beta$: ortho adduct")
draw(axes[1], homo2, (1.75, 2.35), (1.3, 1.7), False, "2-methoxybutadiene + acrolein", r"large C1 $\cdots$ large C$\beta$: para adduct")
fig.tight_layout()
