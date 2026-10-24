"""Why aryl amines are weak bases. Top: the nitrogen lone pair of aniline is delocalised into the
ring; the resonance structures put negative charge on the ortho and para carbons (one ortho
structure shown). Protonation on nitrogen removes this delocalisation, so aniline is about 10^6 times
less basic than cyclohexylamine. Bottom: in 4-nitroaniline the para nitro group accepts the lone
pair directly through the ring, which lowers the basicity much further (pKa of the conjugate acid
1.0, against 2.47 for 3-nitroaniline, where only the inductive effect operates)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
a = s.molecule("Nc1ccccc1", at=(0, y), lone_pairs=[0])
s.curly(a.atom(0), a.bond(0, 1), bend=0.6)
s.curly(a.bond(1, 2), a.atom(2), bend=0.6)
s.arrow((1.6, y), (3.0, y), kind="resonance")
o = s.molecule("[NH2+]=C1[CH-]C=CC=C1", at=(4.6, y), like=a, lone_pairs=[2])
s.curly(o.atom(2), o.bond(2, 3), bend=0.6)
s.curly(o.bond(3, 4), o.atom(4), bend=0.6)
s.text((4.6, y - 2.0), "ortho")
s.arrow((6.2, y), (7.6, y), kind="resonance")
s.molecule("[NH2+]=C1C=C[CH-]C=C1", at=(9.2, y), like=a)
s.text((9.2, y - 2.0), "para")

y = -5.0
n = s.molecule("Nc1ccc(cc1)[N+](=O)[O-]", at=(0, y), lone_pairs=[0, 8])
s.curly(n.atom(0), n.bond(0, 1), bend=0.6)
s.curly(n.bond(1, 6), n.bond(5, 6), bend=0.6)
s.curly(n.bond(4, 5), n.bond(4, 7), bend=0.6)
s.curly(n.bond(7, 8), n.atom(8), bend=0.6)
s.arrow((2.6, y), (4.0, y), kind="resonance")
s.molecule("[NH2+]=C1C=CC(C=C1)=[N+]([O-])[O-]", at=(6.6, y), like=n)
s.text((3.3, y - 2.6), "4-nitroaniline: push-pull resonance")
s.draw()
