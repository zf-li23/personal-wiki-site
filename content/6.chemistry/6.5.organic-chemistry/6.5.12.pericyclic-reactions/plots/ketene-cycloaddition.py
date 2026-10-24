"""[2+2] cycloaddition of dichloroketene (from trichloroacetyl chloride and zinc) with cyclopentene.
The alkene HOMO attacks the central (carbonyl) carbon of the ketene, using the in-plane C=O pi* orbital,
and the ketene C=C pi electrons close the second bond: one concerted but highly asynchronous step
(cis ring fusion, the alkene geometry is kept), giving 7,7-dichlorobicyclo[3.2.0]heptan-6-one."""

exec(open("fixedmol.txt").read())

s = Scheme()
# cyclopentene: 0 Ca (top), 1 Cb (bottom), then the CH2 groups to the left
alk = fixed(s, "C1=CCCC1", [(0, 0.5), (0, -0.5), (-0.95, -0.81), (-1.54, 0), (-0.95, 0.81)])
# ketene: 0 O, 1 carbonyl C, 2 alpha C, 3 Cl, 4 Cl (vertical, linear O=C=C)
k = fixed(s, "O=C=C(Cl)Cl", [(1.7, 1.5), (1.7, 0.5), (1.7, -0.5), (2.57, -1.0), (0.95, -1.2)])
s.partial(alk.xy(0), k.xy(1))
s.partial(alk.xy(1), k.xy(2))
s.curly(alk.bond(0, 1), (alk.xy(0) + k.xy(1)) / 2, bend=-0.6)
s.curly(k.bond(1, 2), (alk.xy(1) + k.xy(2)) / 2, bend=-0.6)
s.arrow((3.2, 0), (4.6, 0), above=r"$\Delta$")
s.molecule("O=C1C(Cl)(Cl)C2CCCC12", at=(6.9, 0))
s.text((6.9, -1.9), "cis-fused cyclobutanone")
s.draw()
