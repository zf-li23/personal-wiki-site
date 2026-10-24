"""Cobalt-catalysed [2+2+2] cyclotrimerization of alkynes (Vollhardt; CpCo shown with the alkyne
substituents omitted). Two alkynes bound to CpCo couple oxidatively (Co(I) to Co(III)) to a
cobaltacyclopentadiene; a third alkyne adds across the metallacycle (insertion, or a [4+2]
cycloaddition to the diene) and reductive elimination releases benzene and returns CpCo. With a
nitrile as the third component the product is a pyridine."""

exec(open("cycle.txt").read())

s = Scheme()
co = complex_at(s, "Co", [(90, "Cp")], (0, 0))
alkene(s, co, 225, dist=1.3)
alkene(s, co, 315, dist=1.3)
s.text((0, -2.6), "CpCo(alkyne)$_2$", size=11)
s.arrow((2.0, 0), (3.6, 0), above="oxidative", below="coupling")
x = 5.8
s.molecule("[Co]1(*)C=CC=C1", coords=[(0, 0.6), (0, 1.8), (0.95, -0.1), (0.59, -1.2), (-0.59, -1.2), (-0.95, -0.1)], at=(x, 0),
           labels={1: "Cp"})
s.text((x, -2.4), "cobaltacyclopentadiene", size=11)
s.arrow((x + 1.8, 0), (x + 3.4, 0), above="HC$\\equiv$CH")
x2 = x + 5.2
s.molecule("c1ccccc1", at=(x2, 0))
s.plus((x2 + 1.8, 0))
s.text((x2 + 3.0, 0), "CpCo", size=13)
s.draw()
