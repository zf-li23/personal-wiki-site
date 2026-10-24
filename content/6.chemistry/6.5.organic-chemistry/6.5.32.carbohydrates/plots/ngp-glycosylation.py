"""Neighbouring-group participation in glycosylation, drawn on a model glycosyl bromide with an
acetyl ester on C2 cis to the bromide (as in 2-O-acetyl-alpha-glucosyl bromide). The carbonyl
oxygen of the C2 ester displaces bromide (or captures the oxocarbenium ion as it forms) from the
face it sits on, giving a cis-fused bicyclic 1,3-dioxolan-2-ylium (acyloxonium) ion. That face of
C1 is now blocked, so the acceptor alcohol can only attack C1 from the opposite face: the new
glycosidic bond is trans to the C2 substituent (1,2-trans, beta for gluco and galacto donors)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
d = s.molecule("Br[C@H]1OCCC[C@H]1OC(C)=O", at=(0.0, y), lone_pairs=[10])
s.curly(d.atom(10), d.atom(1), bend=-0.5)
s.curly(d.bond(0, 1), d.atom(0), bend=0.6)
s.text((0.0, y - 2.2), "2-O-acetyl glycosyl bromide")
s.arrow((2.4, y), (3.8, y), above=r"Ag$^+$", below=r"$-$AgBr")
ion = s.molecule("CC1=[O+][C@H]2OCCC[C@H]2O1", at=(6.0, y))
me = s.molecule("CO", at=(8.4, y + 1.6), lone_pairs=True)
s.curly(me.atom(1), ion.atom(3), bend=0.4)
s.curly(ion.bond(2, 3), ion.atom(2), bend=-0.6)
s.text((6.0, y - 2.2), "acyloxonium ion")
s.arrow((8.8, y - 0.6), (10.2, y - 0.6), above=r"$-$H$^+$")
s.molecule("CO[C@@H]1OCCC[C@H]1OC(C)=O", at=(12.4, y))
s.text((12.4, y - 2.9), "1,2-trans glycoside")
s.draw()
