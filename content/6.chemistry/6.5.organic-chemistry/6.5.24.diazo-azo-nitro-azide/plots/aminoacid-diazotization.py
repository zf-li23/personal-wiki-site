"""Diazotization of (S)-alanine with retention of configuration. The carboxylate, held next to the
diazonium group, displaces N2 from the back side (first inversion), giving a strained alpha-lactone;
water then opens the lactone at the same carbon, again from the back side (second inversion). Two
inversions add up to retention: (S)-alanine gives (S)-lactic acid. Neighbouring-group participation."""

from wikichem import Scheme

s = Scheme()
dz = s.molecule("[N+](#N)[C@@H](C)C(=O)[O-]", at=(0, 0), lone_pairs=[6])
s.curly(dz.atom(6), dz.atom(2), bend=-0.6)
s.curly(dz.bond(0, 2), dz.atom(0), bend=0.6)
s.text((0, -1.8), "(S)-diazonium")
s.arrow((2.2, 0), (3.6, 0), below=r"$-$N$_2$")
lac = s.molecule("O1[C@H](C)C1=O", at=(5.0, 0))
w = s.molecule("O", at=(lac.xy(1)[0] - 0.3, lac.xy(1)[1] + 1.8), lone_pairs=True)
s.curly(w.atom(0), lac.atom(1), bend=0.4)
s.curly(lac.bond(0, 1), lac.atom(0), bend=0.6)
s.text((5.0, -1.8), r"$\alpha$-lactone")
s.arrow((6.6, 0), (8.0, 0), below=r"$-$H$^+$")
s.molecule("O[C@@H](C)C(=O)O", at=(9.8, 0))
s.text((9.8, -1.8), "(S)-lactic acid")
s.draw()
