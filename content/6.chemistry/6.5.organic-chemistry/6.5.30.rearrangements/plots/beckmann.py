"""Beckmann rearrangement of (E)-acetophenone oxime in acid. The oxime oxygen is protonated (or
converted to a sulfonate). As water leaves from nitrogen, the phenyl group anti to the leaving group
migrates with its electron pair from carbon to the electron-poor nitrogen in one concerted step,
giving a nitrilium ion. Water adds to the nitrilium carbon; loss of a proton gives the imidic acid,
which tautomerizes to the amide, acetanilide."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
o = s.molecule("C/C(c1ccccc1)=N\\[OH2+]", at=(0.0, y))
s.curly(o.bond(1, 2), o.atom(8), bend=-0.6)
s.curly(o.bond(8, 9), o.atom(9), bend=0.6)
s.text((0.0, y - 3.0), "protonated (E)-oxime")
s.arrow((2.6, y), (4.0, y), above="Ph anti to OH$_2^+$", below=r"$-\,\mathrm{H_2O}$")
w = s.molecule("O", at=(6.0, y + 1.6), lone_pairs=True)
n = s.molecule("CC#[N+]c1ccccc1", at=(8.6, y))
s.curly(w.atom(0), n.atom(1), bend=-0.4)
s.curly(n.bond(1, 2), n.atom(2), bend=-0.6)
s.text((8.6, y - 3.0), "nitrilium ion")
s.arrow((11.2, y), (12.6, y), below=r"$-\,\mathrm{H^+}$")
s.molecule("CC(O)=Nc1ccccc1", at=(14.8, y))
s.text((14.8, y - 3.0), "imidic acid")
s.arrow((17.2, y), (18.6, y), above="tautomerism")
s.molecule("CC(=O)Nc1ccccc1", at=(21.0, y))
s.text((21.0, y - 3.0), "acetanilide")
s.draw()
