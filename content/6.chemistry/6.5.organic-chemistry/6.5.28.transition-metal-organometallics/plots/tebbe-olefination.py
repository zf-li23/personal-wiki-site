"""Methylenation of an ester with the Tebbe reagent, which releases Cp2Ti=CH2 (a Schrock
carbene). Left: [2+2] cycloaddition of the Ti=C bond with the C=O bond: the nucleophilic carbene
carbon bonds to the carbonyl carbon while the carbonyl oxygen bonds to titanium, giving an
oxatitanacyclobutane. Right: the ring breaks the other way (retro-[2+2]), driven by the strong
Ti=O bond, giving the enol ether and Cp2Ti=O. The ester OR' group stays on carbon; an ylide could
not do this because esters are not electrophilic enough and enolize."""

exec(open("helpers.txt").read())

s = Scheme()
ti = s.molecule("[Ti](*)(*)=C", coords=[(0, 0), (-1.0, 0.7), (-1.0, -0.7), (1.0, 0)], labels={0: "Ti", 1: "Cp", 2: "Cp"})
es = s.molecule("O=C(*)O*", coords=[(0, 1.5), (1.0, 1.5), (1.6, 2.3), (1.6, 0.7), (2.6, 0.7)], labels={2: "R", 4: "R'"},
                lone_pairs=[0])
s.curly(ti.bond(0, 3), es.atom(1), bend=-0.4)
s.curly(es.bond(0, 1), between(es.atom(0), ti.atom(0), 0.55), bend=-0.6)
s.arrow((3.2, 0.7), (4.6, 0.7))
x = 6.6
ring = s.molecule("[Ti]1(*)(*)CC(*)(O*)O1",
                  coords=[(0, 0), (-1.0, 0.7), (-1.0, -0.7), (1.0, 0), (1.0, 1.0), (1.6, 1.8), (1.9, 0.6), (2.8, 0.2), (0, 1.0)],
                  at=(x, 0), labels={0: "Ti", 1: "Cp", 2: "Cp", 5: "R", 7: "R'"})
s.curly(ring.bond(0, 3), ring.bond(3, 4), bend=0.5)
s.curly(ring.bond(4, 8), ring.bond(0, 8), bend=0.5)
s.text((x + 0.5, -1.4), "oxatitanacyclobutane", size=11)
s.arrow((x + 3.4, 0.4), (x + 4.8, 0.4))
x2 = x + 6.6
s.molecule("C=C(*)O*", coords=[(0, 0), (1.0, 0), (1.5, 0.87), (1.5, -0.87), (2.5, -0.87)], at=(x2, 0.4), labels={2: "R", 4: "R'"})
s.plus((x2 + 3.4, 0.4))
s.molecule("[Ti](*)(*)=O", coords=[(0, 0), (-1.0, 0.7), (-1.0, -0.7), (1.0, 0)], at=(x2 + 5.0, 0.4), labels={0: "Ti", 1: "Cp", 2: "Cp"})
s.draw()
