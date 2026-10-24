"""Ketones from carboxylic acids and two equivalents of an organolithium. The first equivalent
deprotonates the acid (not drawn); the C-Li electrons of the second add to the carbonyl carbon of
lithium benzoate and the C=O electrons go to oxygen, giving the dilithium salt of a gem-diol. This
tetrahedral intermediate carries two negative charges and cannot expel O2-, so it does not collapse
to the ketone while organolithium is present (no second addition to a tertiary alcohol). Aqueous
acid in the workup gives the hydrate, which loses water to acetophenone."""

from wikichem import Scheme

s = Scheme()
cb = s.molecule("[O-]C(=O)c1ccccc1", at=(0, 0), lone_pairs=[2])
me = s.molecule("C[Li]", coords=[(2.4, 1.4), (3.3, 1.9)])
s.curly(me.bond(0, 1), cb.atom(1), bend=0.5)
s.curly(cb.bond(1, 2), cb.atom(2), bend=0.6)
s.text((-1.9, 1.4), "Li$^+$", size=12)
s.arrow((3.6, 0), (5.0, 0))
x = 7.6
s.molecule("CC([O-])([O-])c1ccccc1", at=(x, 0))
s.text((x, -2.0), "2 Li$^+$, stable at $-78\\,^\\circ$C", size=11)
s.arrow((x + 2.6, 0), (x + 4.0, 0), above="H$_3$O$^+$")
x2 = x + 6.4
s.molecule("CC(O)(O)c1ccccc1", at=(x2, 0))
s.arrow((x2 + 2.4, 0), (x2 + 3.8, 0), above="$-$H$_2$O")
s.molecule("CC(=O)c1ccccc1", at=(x2 + 6.0, 0))
s.draw()
