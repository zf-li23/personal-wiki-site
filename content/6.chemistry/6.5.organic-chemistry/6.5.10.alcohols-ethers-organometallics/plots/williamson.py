"""Planning a Williamson ether synthesis of tert-butyl methyl ether. Top: tert-butoxide attacks the
unhindered carbon of iodomethane from the back side (SN2) and iodide leaves, giving the ether.
Bottom: with the roles reversed, methoxide cannot reach the tertiary carbon of 2-bromo-2-methylpropane;
it acts as a base on a beta hydrogen instead (E2), and the product is 2-methylpropene."""

from wikichem import Scheme

s = Scheme()
y = 0.0
tb = s.molecule("CC(C)(C)[O-]", at=(0, y), lone_pairs=[4])
mi = s.molecule("CI", at=(2.4, y + 0.3), lone_pairs=[1])
s.curly(tb.atom(4), mi.atom(0), bend=-0.4)
s.curly(mi.bond(0, 1), mi.atom(1), bend=-0.7)
s.arrow((3.8, y), (5.2, y), above=r"S$_{\mathrm{N}}$2")
s.molecule("CC(C)(C)OC", at=(6.8, y))
s.plus((8.4, y))
s.molecule("[I-]", at=(9.2, y), lone_pairs=True)
s.text((3.0, y - 1.6), "good: SN2 at a methyl carbon")

y = -4.0
me = s.molecule("C[O-]", at=(-0.6, y + 1.2), lone_pairs=[1])
tb2 = s.molecule("CC(C)(C)Br", at=(2.0, y), show_h=[0], lone_pairs=[4])
s.curly(me.atom(1), tb2.h(0), bend=-0.4)
s.curly((tb2.h(0).xy + tb2.xy(0)) / 2, tb2.bond(0, 1), bend=-0.7)
s.curly(tb2.bond(1, 4), tb2.atom(4), bend=0.7)
s.arrow((3.8, y), (5.2, y), above="E2")
s.molecule("C=C(C)C", at=(6.6, y))
s.text((8.9, y), r"+  CH$_3$OH  +  Br$^-$")
s.text((3.0, y - 1.8), "bad: a tertiary halide only eliminates")
s.draw()
