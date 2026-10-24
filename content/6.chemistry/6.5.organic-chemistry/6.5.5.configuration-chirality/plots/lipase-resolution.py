"""Lipase-catalysed kinetic resolution of racemic 1-phenylethanol with vinyl acetate (for example
Candida antarctica lipase B). Top: the active-site serine (its proton taken by the histidine of the
catalytic triad, not drawn) adds to the ester carbonyl group; the tetrahedral intermediate expels the
enolate of vinyl alcohol, which tautomerises to acetaldehyde, so acylation of the enzyme is
irreversible. Bottom: the acyl-enzyme transfers the acetyl group to the alcohol. The (R) enantiomer
fits the active site with its large (phenyl) and medium (methyl) groups in the right pockets and
reacts much faster; the (S) alcohol is left behind, and the two are separated as alcohol and ester."""

from wikichem import Scheme

s = Scheme()
SER = {0: "Ser"}
y = 0.0
ser = s.molecule("*CO", at=(-2.3, y - 0.3), labels=SER, lone_pairs=[2], flip=True)
va = s.molecule("CC(=O)OC=C", at=(2.0, y + 0.2), lone_pairs=[2])
s.curly(ser.atom(2), va.atom(1), bend=-0.5)
s.curly(va.bond(1, 2), va.atom(2), bend=-0.7)
s.text((0.4, y - 2.0), "serine + vinyl acetate")
s.arrow((4.2, y), (5.6, y), above="2 steps")
s.molecule("*COC(C)=O", at=(7.6, y), labels=SER)
s.text((7.6, y - 2.0), "acyl-enzyme")
s.plus((9.6, y))
s.molecule("CC=O", at=(11.2, y))
s.text((11.2, y - 2.0), "acetaldehyde")

y = -5.0
ac = s.molecule("*COC(C)=O", at=(-0.6, y + 0.6), labels=SER, lone_pairs=[5])
al = s.molecule("O[C@H](C)c1ccccc1", at=(2.4, y - 0.4), lone_pairs=[0], rotate=-60)
s.curly(al.atom(0), ac.atom(3), bend=-0.5)
s.curly(ac.bond(3, 5), ac.atom(5), bend=-0.7)
s.text((0.8, y - 2.6), "(R)-1-phenylethanol: fast")
s.arrow((4.8, y), (6.2, y), above="2 steps")
s.molecule("CC(=O)O[C@H](C)c1ccccc1", at=(9.4, y))
s.text((9.4, y - 2.6), "(R)-acetate")
s.plus((12.0, y))
s.molecule("*CO", at=(14.0, y), labels=SER)
s.text((6.4, y - 3.6), "(S)-1-phenylethanol reacts slowly and remains as the alcohol")
s.draw()
