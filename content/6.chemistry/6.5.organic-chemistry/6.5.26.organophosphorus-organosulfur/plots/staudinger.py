"""Staudinger reduction of an alkyl azide (R = methyl here; the phenyl groups on phosphorus are
written Ph). Top: the phosphorus lone pair attacks the terminal nitrogen of the azide and the
N-N pi electrons move onto the central nitrogen, giving a zwitterionic phosphazide. Bottom: the
phosphazide closes to a four-membered ring that falls apart, like the oxaphosphetane of the
Wittig reaction, into dinitrogen and the iminophosphorane (aza-ylide); water then converts the
iminophosphorane into the amine and triphenylphosphine oxide."""

from wikichem import Scheme

s = Scheme()
PH = {1: "Ph", 2: "Ph", 3: "Ph"}
p = s.molecule("P(C)(C)C", coords=[(0, 0), (-0.87, 0.5), (-0.87, -0.5), (0, -1.0)], at=(0, 0),
               lone_pairs=[0], labels=PH)
az = s.molecule("C[N-][N+]#N", coords=[(4.6, 0), (3.6, 0), (2.6, 0), (1.6, 0)], at=(0, 0), lone_pairs=[1])
s.curly(p.atom(0), az.atom(3), bend=-0.5)
s.curly(az.bond(2, 3), az.atom(2), bend=-0.6)
s.arrow((5.6, 0), (7.0, 0))
s.molecule("C[N-]N=N[P+](C)(C)C",
           coords=[(1.0, 0.87), (1.0, -0.13), (0.13, -0.63), (0.13, -1.63), (-0.74, -2.13), (-1.61, -1.63), (-1.24, -3.0), (-0.24, -3.0)],
           at=(9.0, 1.0), lone_pairs=[1], labels={5: "Ph", 6: "Ph", 7: "Ph"})
s.text((9.0, -3.2), "phosphazide", size=12)

y = -6.5
ring = s.molecule("CN1N=NP1(C)(C)C",
                  coords=[(-1.0, 0.0), (0.0, 0.0), (0.0, 1.2), (1.2, 1.2), (1.2, 0.0), (2.1, 0.45), (2.1, -0.45), (1.2, -1.0)],
                  at=(0, y), labels={5: "Ph", 6: "Ph", 7: "Ph"})
s.curly(ring.bond(3, 4), ring.bond(2, 3), bend=-0.8)
s.curly(ring.bond(1, 2), ring.bond(1, 4), bend=-0.8)
s.arrow((3.2, y), (4.6, y), above="$-\\mathrm{N_2}$")
s.molecule("CN=P(C)(C)C", coords=[(-1.0, 0), (0, 0), (1.0, 0), (1.5, 0.87), (2.0, 0), (1.5, -0.87)], at=(6.6, y),
           labels={3: "Ph", 4: "Ph", 5: "Ph"})
s.arrow((9.4, y), (10.8, y), above="H$_2$O")
s.molecule("CN", at=(11.8, y))
s.plus((13.5, y))
s.molecule("O=P(C)(C)C", coords=[(-1.0, 0), (0, 0), (0.5, 0.87), (1.0, 0), (0.5, -0.87)], at=(15.3, y),
           labels={2: "Ph", 3: "Ph", 4: "Ph"})
s.draw()
