"""Nucleophilic attack on a coordinated carbonyl and the Fischer synthesis of a carbene complex.
Phenyllithium adds its carbanion carbon to the electrophilic carbon of one CO of W(CO)6 and a pair
of C-O pi electrons moves onto oxygen, giving the lithium acyltungstate, drawn as its carbene-like resonance form (CO)5W=C(O-)Ph. Methylation of the acyl
oxygen with trimethyloxonium tetrafluoroborate (Meerwein's salt) gives (CO)5W=C(OMe)Ph."""

import math

exec(open("helpers.txt").read())


def ring(centre, start=90):
    return [(centre[0] + math.cos(math.radians(start - 60 * i)), centre[1] + math.sin(math.radians(start - 60 * i))) for i in range(6)]


s = Scheme()
w = s.molecule("[W]C#[O+]", coords=[(0, 0), (2.0, 0), (3.0, 0)], at=(0, 0), labels={0: "(CO)$_5$W", 2: "O"}, show_carbons=[1])
li = s.molecule("[Li]c1ccccc1", coords=[(1.6, 1.3)] + ring((3.33, 2.3), start=210), at=(0, 0))
s.curly(li.bond(0, 1), w.atom(1), bend=0.4)
s.curly(w.bond(1, 2), w.atom(2), bend=-0.6)
s.arrow((4.2, 0.0), (5.8, 0.0))

x = 7.6
core = [(0, 0), (1.9, 0), (2.45, 0.95)] + ring((2.45, -1.95))
s.molecule("[W]=C([O-])c1ccccc1", coords=core, at=(x, 0), labels={0: "(CO)$_5$W"}, lone_pairs=[2])
s.text((x + 3.6, 1.0), "Li$^+$", size=13)
s.arrow((x + 4.3, 0), (x + 5.9, 0), above="Me$_3$O$^+$ BF$_4^-$", below="$-$Me$_2$O, LiBF$_4$")

x2 = x + 7.7
core = [(0, 0), (1.9, 0), (2.45, 0.95), (3.45, 0.95)] + ring((2.45, -1.95))
s.molecule("[W]=C(OC)c1ccccc1", coords=core, at=(x2, 0), labels={0: "(CO)$_5$W", 3: "CH$_3$"})
s.draw()
