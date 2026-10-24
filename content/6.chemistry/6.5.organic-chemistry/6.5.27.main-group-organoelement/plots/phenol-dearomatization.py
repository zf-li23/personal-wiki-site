"""Oxidative dearomatization of p-cresol with PIDA (PhI(OAc)2) in methanol. First, ligand exchange:
the phenol replaces an acetate on iodine(III) (acetic acid is released), giving an
aryloxy-lambda3-iodane. Then methanol attacks the para carbon; the ring electrons shift so that
the C-O bond becomes a C=O bond, and the O-I bond breaks with iodine taking the electron pair
(reductive elimination from I(III) to iodobenzene, an excellent leaving group) together with
acetate. Loss of a proton from methanol gives 4-methoxy-4-methylcyclohexa-2,5-dien-1-one."""

from wikichem import Scheme

s = Scheme()
s.molecule("Cc1ccc(O)cc1", at=(0, 0))
s.arrow((1.8, 0), (3.6, 0), above="PhI(OAc)$_2$", below="$-$AcOH")
x = 6.4
# Kekule structure with C1(O)=C6, C2=C3, C4(Me)=C5
H = [(0, 0.0), (0.87, -0.5), (0.87, -1.5), (0, -2.0), (-0.87, -1.5), (-0.87, -0.5)]
m = s.molecule("O(I(*)OC(C)=O)C1C=CC(C)=CC=1",
               coords=[(0, 1.0), (1.0, 1.4), (1.6, 2.2), (2.0, 1.0), (3.0, 1.2), (3.4, 2.1), (3.6, 0.4)]
               + [H[0], H[1], H[2], H[3], (0, -3.0), H[4], H[5]],
               at=(x, 0.8), labels={2: "Ph"}, lone_pairs=[])
meoh = s.molecule("CO", coords=[(-2.2, -3.6), (-1.3, -3.1)], at=(x, 0.8), lone_pairs=[1])
s.curly(meoh.atom(1), m.atom(10), bend=0.4)
s.curly(m.bond(10, 12), m.bond(12, 13), bend=0.6)
s.curly(m.bond(7, 13), m.bond(0, 7), bend=-0.6)
s.curly(m.bond(0, 1), m.atom(1), bend=-0.6)
s.arrow((x + 4.0, -0.4), (x + 5.4, -0.4), below="$-$PhI, $-$AcOH")
s.molecule("COC1(C)C=CC(=O)C=C1", at=(x + 7.6, -0.4))
s.draw()
