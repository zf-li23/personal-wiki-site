"""Endo and exo approach in the Diels-Alder reaction of butadiene with acrolein (oblique projection;
the diene lies above the dienophile). Primary orbital interactions (dotted) form the two new sigma
bonds. In the endo transition state the carbonyl group lies under the diene and its pi* lobe on the
carbonyl carbon overlaps in phase with the HOMO lobe at C3 of the diene (secondary orbital
interaction, dashed); in the exo transition state the carbonyl points away and has no such contact."""

exec(open("orbitals.txt").read())

_, vd = huckel_chain(4)
homo = vd[:, 1]  # (+, +, -, -)
# acrolein LUMO coefficients from 6.5.12 (Hueckel, carbonyl O h = 1, k = 1): C-beta, C-alpha, C(O), O
lumo = np.array([-0.657, 0.228, 0.577, -0.429])


def P(x, y, z):
    """Oblique projection: depth y goes up and to the right."""
    return np.array([x + 0.45 * y, z + 0.35 * y])


def vlobe(ax, p, c, s=0.55):
    porb(ax, p, c, angle=90, scale=0.25 + 0.75 * abs(c) / 0.6 * s)


def scene(ax, endo):
    zt, zb = 1.5, -1.5
    diene = [(0.0, 0.0), (0.7, 1.2), (2.1, 1.2), (2.8, 0.0)]  # C1..C4, s-cis
    top = [P(x, y, zt) for x, y in diene]
    sign = -1 if endo else 1
    dien = [(0.7, 0.0), (2.1, 0.0)]  # C-beta under C1, C-alpha under C4
    co = (2.9, 1.0 * (1 if endo else -1))  # carbonyl carbon: under the diene (endo) or away (exo)
    ox = (3.6, 1.9 * (1 if endo else -1))
    bot = [P(x, y, zb) for x, y in dien + [co, ox]]
    atom_chain(ax, top)
    atom_chain(ax, bot[:3])
    ax.plot(*zip(bot[2], bot[3]), color=ink(), lw=1.4)
    ax.text(*(bot[3] + (0.2, 0.0)), "O", fontsize=9, color=ink(), va="center")
    for p, c in zip(top, homo):
        vlobe(ax, p, c)
    for p, c in zip(bot[:3], lumo[:3]):
        vlobe(ax, p, c)
    for a, b in ((top[0], bot[0]), (top[3], bot[1])):
        ax.plot(*zip(a - (0, 0.55), b + (0, 0.5)), color=ink(), lw=1.1, ls=(0, (1, 2)))
    if endo:
        ax.plot(*zip(top[2] - (0, 0.45), bot[2] + (0, 0.45)), color="#d1495b", lw=1.4, ls=(0, (4, 2)))
        ax.text(*(P(3.1, 1.2, 0) + (0.25, 0)), "secondary\norbital\ninteraction", fontsize=8, color="#d1495b", va="center")
    ax.text(*(P(1.4, 0.4, zt) + (0, 1.25)), "diene HOMO", ha="center", fontsize=9, color=ink())
    ax.text(*(P(1.4, 0.0, zb) - (0, 1.35)), "dienophile LUMO", ha="center", fontsize=9, color=ink())
    ax.set_title("endo (favoured)" if endo else "exo", fontsize=10, color=ink())
    clean(ax, (-1.0, 5.6), (-3.8, 3.6))


fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.4))
scene(axes[0], True)
scene(axes[1], False)
fig.tight_layout()
