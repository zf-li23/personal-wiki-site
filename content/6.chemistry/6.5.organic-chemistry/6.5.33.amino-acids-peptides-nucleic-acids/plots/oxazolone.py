"""Racemization during peptide coupling through a 5(4H)-oxazolone. Top: in an activated N-acyl
amino acid (here N-acetylalanine with a leaving group X, such as the O-acylisourea from DCC),
the carbonyl oxygen of the N-acyl group attacks the activated carbonyl carbon and X leaves,
closing the oxazolone ring. Bottom: the C4-H of the oxazolone is acidic (pKa about 9) because
its conjugate base is an aromatic oxazol-5-olate; a base removes it and the planar anion is
reprotonated on either face, so the stereocentre is lost. Amines still open the oxazolone to
the peptide, but as a mixture of epimers. Urethane protecting groups (Boc, Fmoc, Cbz) suppress
this pathway."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("CC(=O)N[C@@H](C)C(=O)*", at=(0.0, y), lone_pairs=[2], labels={8: "X"})
# atoms: 0 C,1 C,2 O,3 N,4 C alpha,5 CH3,6 C,7 O,8 X
s.curly(a.atom(2), a.atom(6), bend=-0.6)
s.curly(a.bond(6, 8), a.atom(8), bend=0.5)
s.text((0.0, y - 1.9), "activated N-acyl amino acid")
s.arrow((2.4, y), (3.8, y), above=r"$-$X$^-$", below=r"$-$H$^+$")
s.molecule("CC1=N[C@@H](C)C(=O)O1", at=(5.4, y))
s.text((5.4, y - 1.6), "5(4H)-oxazolone")

y = -5.4
ox = s.molecule("CC1=N[C@@H](C)C(=O)O1", at=(0.0, y), show_h=[3])
base = s.molecule("CCN(CC)CC", at=(-3.4, y + 0.8), lone_pairs=[2])
s.curly(base.atom(2), ox.h(3), bend=-0.4)
s.curly(ox.bond(3, ox.mol.GetNumAtoms() - 1), ox.bond(3, 5), bend=0.6)
s.curly(ox.bond(5, 6), ox.atom(6), bend=-0.6)
s.arrow((2.0, y), (3.4, y), kind="equilibrium")
s.molecule("CC1=NC(C)=C([O-])O1", at=(5.4, y))
s.text((5.4, y - 1.9), "aromatic anion\n(achiral)")
s.arrow((7.4, y), (8.8, y), above=r"H$^+$", kind="equilibrium")
s.molecule("CC1=NC(C)C(=O)O1", at=(10.8, y))
s.text((10.8, y - 1.9), "racemic\noxazolone")
s.draw()
