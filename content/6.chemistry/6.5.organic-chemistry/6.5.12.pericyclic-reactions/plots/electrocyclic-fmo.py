"""Frontier-orbital analysis of electrocyclic ring closure. Hueckel coefficients of the HOMO are
computed with numpy; the terminal p orbitals rotate by 90 degrees to form the new sigma bond.
Conrotatory: both termini turn the same way; disrotatory: opposite ways. The closure is allowed when
the two lobes that meet have the same phase (shaded = positive).
Figure 1: 1,3-butadiene, HOMO psi2 (thermal) and the excited-state HOMO psi3 (photochemical).
Figure 2: 1,3,5-hexatriene, HOMO psi3 (thermal) and psi4 (photochemical)."""

exec(open("orbitals.txt").read())


def panel(ax, pts, c, mode, title):
    """Draw the chain with its orbital lobes; mode None (planar polyene), 'con' or 'dis' (termini turned)."""
    atom_chain(ax, pts)
    n = len(pts)
    for i in range(1, n - 1):
        porb(ax, pts[i], c[i], scale=0.6, alpha=1.0 if mode is None else 0.35)
    if mode is None:
        porb(ax, pts[0], c[0], scale=0.6)
        porb(ax, pts[-1], c[-1], scale=0.6)
    else:
        # left terminus turns clockwise (its upper lobe now points right, towards the other end)
        porb(ax, pts[0], c[0], angle=0, scale=0.6)
        right_angle = 0 if mode == "con" else 180
        porb(ax, pts[-1], c[-1], angle=right_angle, scale=0.6)
        inward_left = np.sign(c[0])
        inward_right = -np.sign(c[-1]) if mode == "con" else np.sign(c[-1])
        good = inward_left == inward_right
        a = np.array(pts[0]) + (0.3, 0)
        b = np.array(pts[-1]) - (0.3, 0)
        bond_hint(ax, a, b, good=good)
        turn(ax, np.array(pts[0]) + (0, 0.05), clockwise=True)
        turn(ax, np.array(pts[-1]) + (0, 0.05), clockwise=(mode == "con"))
        ax.text((pts[0][0] + pts[-1][0]) / 2, min(p[1] for p in pts) - 0.95, "bonding: allowed" if good else "antibonding: forbidden",
                ha="center", fontsize=9, color=ink())
    ax.set_title(title, fontsize=10, color=ink())


def figure(n, pts, rows):
    e, v = huckel_chain(n)
    fig, axes = plt.subplots(len(rows), 3, figsize=(8.4, 2.9 * len(rows)))
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    for r, (k, label) in enumerate(rows):
        c = v[:, k]
        panel(axes[r, 0], pts, c, None, label)
        panel(axes[r, 1], pts, c, "con", "conrotatory")
        panel(axes[r, 2], pts, c, "dis", "disrotatory")
        for ax in axes[r]:
            clean(ax, (min(xs) - 0.9, max(xs) + 0.9), (min(ys) - 1.3, max(ys) + 0.9))
    fig.tight_layout()


# Figure 1: s-cis butadiene drawn as a U; C1 and C4 at the bottom.
butadiene = [(-1.1, 0.0), (-0.6, 0.9), (0.6, 0.9), (1.1, 0.0)]
figure(4, butadiene, [(1, r"$\psi_2$: HOMO, heat"), (2, r"$\psi_3$: HOMO*, light")])

# Figure 2: (Z)-hexatriene drawn as an open hexagon; C1 and C6 at the bottom.
ang = np.radians([240, 180, 120, 60, 0, 300])
hexatriene = [(1.1 * np.cos(t), 1.1 * np.sin(t)) for t in ang]
figure(6, hexatriene, [(2, r"$\psi_3$: HOMO, heat"), (3, r"$\psi_4$: HOMO*, light")])
