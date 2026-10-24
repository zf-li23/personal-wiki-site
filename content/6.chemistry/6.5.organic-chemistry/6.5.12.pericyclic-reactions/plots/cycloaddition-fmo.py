"""Frontier-orbital analysis of suprafacial cycloadditions. One component lies above the other and
the new bonds form between the end atoms (dotted lines). [2+2]: the HOMO of one ethylene and the
LUMO of the other match at one end but not at the other, so the thermal suprafacial reaction is
forbidden; with one alkene excited, its singly occupied pi* (HOMO*) meets the LUMO of the other
in phase at both ends. [4+2]: both the diene HOMO / dienophile LUMO and the diene LUMO / dienophile
HOMO combinations are in phase at both ends: thermally allowed."""

exec(open("orbitals.txt").read())


def component(ax, x0, y, c, label):
    pts = [(x0 + 1.2 * i, y) for i in range(len(c))]
    atom_chain(ax, pts)
    for p, ci in zip(pts, c):
        porb(ax, p, ci, scale=0.62)
    ax.text(pts[-1][0] + 0.6, y, label, ha="left", va="center", fontsize=9, color=ink())
    return pts


def pair(ax, top, bottom, ltop, lbot, title):
    n, m = len(top), len(bottom)
    x_top = 0.0
    x_bot = 0.0 if n == m else 1.2 * (n - m) / 2
    # The overall sign of an orbital is arbitrary: flip the lower one so that the left ends match.
    if -np.sign(top[0]) != np.sign(bottom[0]):
        bottom = -np.asarray(bottom)
    pt = component(ax, x_top, 1.6, top, ltop)
    pb = component(ax, x_bot, -1.6, bottom, lbot)
    for (i, j) in ((0, 0), (n - 1, m - 1)):
        # lobe facing down on the top component and facing up on the bottom component
        sign_top = -np.sign(top[i])
        sign_bot = np.sign(bottom[j])
        bond_hint(ax, np.array(pt[i]) - (0, 0.55), np.array(pb[j]) + (0, 0.55), good=sign_top == sign_bot)
    ax.set_title(title, fontsize=10, color=ink())
    clean(ax, (-0.8, 6.3), (-2.6, 2.6))


fig, axes = plt.subplots(2, 2, figsize=(8.4, 6.6))
e2, v2 = huckel_chain(2)
e4, v4 = huckel_chain(4)
pair(axes[0, 0], v2[:, 0], v2[:, 1], "HOMO", "LUMO", "[2+2], heat: forbidden")
pair(axes[0, 1], v2[:, 1], v2[:, 1], "HOMO* (excited)", "LUMO", r"[2+2], $h\nu$: allowed")
pair(axes[1, 0], v4[:, 1], v2[:, 1], "diene HOMO", "dienophile LUMO", "[4+2], heat: allowed")
pair(axes[1, 1], v4[:, 2], v2[:, 0], "diene LUMO", "dienophile HOMO", "[4+2], heat: allowed")
fig.tight_layout()
