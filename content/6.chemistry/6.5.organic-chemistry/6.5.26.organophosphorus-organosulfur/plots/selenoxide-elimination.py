"""Selenoxide syn elimination, the selenium version of the thermal sulfoxide elimination (Ph =
phenyl). 2-(Phenylselanyl)cyclohexanone is oxidized by hydrogen peroxide to the selenoxide, which
eliminates already at room temperature: the selenoxide oxygen takes a hydrogen on the adjacent
ring carbon through a five-membered cyclic transition state (Ei mechanism, Se and H leave from
the same side), the C-H electrons form the C=C bond and the C-Se bond breaks toward selenium.
Products: cyclohex-2-en-1-one and benzeneselenenic acid PhSeOH."""

from wikichem import Scheme

s = Scheme()
s.molecule("O=C1CCCCC1[Se]*", at=(0, 0), labels={8: "Ph"})
s.arrow((2.0, 0), (3.6, 0), above="H$_2$O$_2$")
x = 5.6
m = s.molecule("[O-][Se+](*)C1C([H])CCCC1=O",
               coords=[(0, 0.85), (0.81, 0.26), (1.8, 0.6), (0.5, -0.69), (-0.5, -0.69), (-0.81, 0.26), (-1.0, -1.556),
                       (-0.5, -2.42), (0.5, -2.42), (1.0, -1.556), (2.0, -1.556)],
               at=(x, 0.6), lone_pairs=[0], labels={2: "Ph"})
s.curly(m.atom(0), m.atom(5), bend=0.5)
s.curly(m.bond(4, 5), m.bond(3, 4), bend=0.6)
s.curly(m.bond(1, 3), m.atom(1), bend=-0.5)
s.text((x, -2.6), "five-membered cyclic TS", size=11)
s.arrow((x + 2.6, 0), (x + 4.0, 0), above="Ei, syn")
x2 = x + 6.0
s.molecule("O=C1C=CCCC1", at=(x2, 0))
s.plus((x2 + 1.8, 0))
s.molecule("*[Se]O", coords=[(0, 0), (1.0, 0), (1.5, 0.87)], at=(x2 + 2.8, 0), labels={0: "Ph"})
s.draw()
