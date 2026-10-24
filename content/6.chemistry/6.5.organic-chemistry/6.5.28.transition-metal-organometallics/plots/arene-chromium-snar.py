"""Nucleophilic aromatic substitution on (eta6-chlorobenzene)tricarbonylchromium. The Cr(CO)3 group
withdraws electron density from the ring (as strongly as a para nitro group). Methoxide adds to the
ipso carbon on the face opposite to chromium; the ring pi electrons move onto the metal-bound
cyclohexadienyl system, giving an anionic eta5-cyclohexadienyl complex (a Meisenheimer-type
intermediate). Chloride then leaves and the eta6-arene complex of anisole forms; the metal is
removed afterwards by light or mild oxidation."""

exec(open("helpers.txt").read())

s = Scheme()
HEX = [(1.0, 0), (0.5, -0.87), (-0.5, -0.87), (-1.0, 0), (-0.5, 0.87), (0.5, 0.87)]


STEMS = []  # eta6 bonds from the ring centres to chromium, drawn on the axes at the end


def chromium(xy):
    centre = np.asarray(xy, float)
    s.text(centre + np.array([0, -2.1]), "Cr(CO)$_3$", size=12)
    STEMS.append((centre[0], centre[1] - 0.15, centre[1] - 1.8))


ar = s.molecule("Clc1ccccc1", coords=[(2.0, 0)] + HEX, lone_pairs=[])
chromium((0, 0))
me = s.molecule("C[O-]", coords=[(2.4, 2.0), (1.7, 1.3)], lone_pairs=[1])
s.curly(me.atom(1), ar.atom(1), bend=0.4)
s.curly(ar.bond(1, 2), (0.3, -0.3), bend=-0.5)
s.arrow((3.0, 0), (4.4, 0))
x = 6.4
mz = s.molecule("ClC1(OC)C=CC=CC1", coords=[(1.7, -0.7), HEX[0], (1.7, 0.7), (2.6, 0.9)] + HEX[1:], at=(x, 0))
s.text((x - 1.4, 1.0), "$-$", size=14)
chromium((x, -0.1))
s.text((x, -3.0), "anionic $\\eta^5$ complex", size=11)
s.arrow((x + 3.2, 0), (x + 4.6, 0), above="$-$Cl$^-$")
x2 = x + 6.8
s.molecule("COc1ccccc1", coords=[(2.5, 0.87), (2.0, 0)] + HEX, at=(x2, 0))
chromium((x2, 0))
fig, ax = s.draw()
for x0, y0, y1 in STEMS:
    ax.plot([x0, x0], [y0, y1], color="k", lw=1.4)
