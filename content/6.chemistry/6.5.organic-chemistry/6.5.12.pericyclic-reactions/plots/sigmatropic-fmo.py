"""Frontier-orbital analysis of sigmatropic shifts. The migrating sigma bond is imagined as broken
into two radicals; the HOMO of the odd-carbon radical (Hueckel, numpy) is combined with the orbital
of the migrating group. (a) [1,5]-H: the end lobes of the pentadienyl HOMO have the same phase, so
H can move on one face (suprafacial, allowed). (b) [1,3]-H: the allyl HOMO has opposite phases at
the ends; a suprafacial shift is forbidden (the antarafacial path is geometrically impossible).
(c) [1,3]-C: a migrating carbon can use both lobes of its p orbital, bonding to C1 with one lobe
and to C3 with the other: suprafacial with inversion at the migrating carbon. (d) [3,3]: two allyl
radical HOMOs stacked one above the other match at both ends (suprafacial-suprafacial, allowed)."""

exec(open("orbitals.txt").read())


def chain(ax, n, y=0.0, x0=0.0):
    e, v = huckel_chain(n)
    c = v[:, (n - 1) // 2]  # singly occupied nonbonding MO of the odd radical
    pts = [(x0 + 1.1 * i, y) for i in range(n)]
    atom_chain(ax, pts)
    for p, ci in zip(pts, c):
        porb(ax, p, ci, scale=0.62)
    return pts, c


fig, axes = plt.subplots(2, 2, figsize=(8.6, 5.8))

ax = axes[0, 0]
pts, c = chain(ax, 5)
h = (2.2, 1.55)
sorb(ax, h, 1)
for k in (0, 4):
    bond_hint(ax, np.array(pts[k]) + (0, 0.6), np.array(h) + (-0.25 if k == 0 else 0.25, -0.1), good=np.sign(c[k]) > 0)
ax.set_title("(a) [1,5]-H, suprafacial: allowed", fontsize=10, color=ink())
clean(ax, (-0.8, 5.2), (-1.3, 2.2))

ax = axes[0, 1]
pts, c = chain(ax, 3, x0=0.6)
h = (1.7, 1.55)
sorb(ax, h, 1)
for k in (0, 2):
    bond_hint(ax, np.array(pts[k]) + (0, 0.6), np.array(h) + (-0.25 if k == 0 else 0.25, -0.1), good=np.sign(c[k]) > 0)
ax.set_title("(b) [1,3]-H, suprafacial: forbidden", fontsize=10, color=ink())
clean(ax, (-0.8, 4.2), (-1.3, 2.2))

ax = axes[1, 0]
pts, c = chain(ax, 3, x0=0.6)
m = (1.7, 1.55)
porb(ax, m, 1.0, angle=180, scale=0.75)  # migrating carbon: positive lobe towards C1, negative lobe towards C3
ax.text(m[0], m[1] + 0.45, "C", ha="center", fontsize=9, color=ink())
bond_hint(ax, np.array(pts[0]) + (0, 0.6), np.array(m) + (-0.6, -0.1), good=np.sign(c[0]) > 0)
bond_hint(ax, np.array(pts[2]) + (0, 0.6), np.array(m) + (0.6, -0.1), good=np.sign(c[2]) < 0)
ax.set_title("(c) [1,3]-C, suprafacial with inversion", fontsize=10, color=ink())
clean(ax, (-0.8, 4.2), (-1.3, 2.4))

ax = axes[1, 1]
pts1, c1 = chain(ax, 3, y=1.0, x0=0.6)
pts2, c2 = chain(ax, 3, y=-1.6, x0=0.6)
# the lower allyl is drawn with its sign flipped where needed so that C1-C1' is bonding
flip = -1 if (-np.sign(c1[0]) != np.sign(c2[0])) else 1
if flip < 0:
    for p in list(ax.patches)[-3:]:
        p.remove()
    for p, ci in zip(pts2, -c2):
        porb(ax, p, ci, scale=0.62)
    c2 = -c2
for k in (0, 2):
    bond_hint(ax, np.array(pts1[k]) - (0, 0.55), np.array(pts2[k]) + (0, 0.55), good=(-np.sign(c1[k])) == np.sign(c2[k]))
ax.text(3.6, 1.0, "allyl", fontsize=9, color=ink(), va="center")
ax.text(3.6, -1.6, "allyl", fontsize=9, color=ink(), va="center")
ax.set_title("(d) [3,3], suprafacial on both: allowed", fontsize=10, color=ink())
clean(ax, (-0.8, 4.6), (-2.5, 1.9))
fig.tight_layout()
