"""The enolate of cyclohexanone as an ambident nucleophile. Top: the hard oxygen end attacks the
silicon of chlorotrimethylsilane (strong Si-O bond) and chloride leaves, giving the silyl enol ether
(O-attack). Bottom: the soft carbon end, pushed by the oxygen lone pair, attacks iodomethane in an
SN2 reaction, giving 2-methylcyclohexanone (C-attack)."""

from wikichem import Scheme

s = Scheme()
y = 0.0
e = s.molecule("[O-]C1=CCCCC1", at=(0, y), lone_pairs=[0])
tms = s.molecule("Cl[Si](C)(C)C", at=(2.4, y + 1.0), lone_pairs=[0])
s.curly(e.atom(0), tms.atom(1), bend=-0.4)
s.curly(tms.bond(0, 1), tms.atom(0), bend=-0.6)
s.text((0, y - 2.0), "O-attack (hard electrophile)")
s.arrow((4.2, y), (5.6, y), below=r"$-$Cl$^-$")
s.molecule("C[Si](C)(C)OC1=CCCCC1", at=(8.2, y))
s.text((8.2, y - 2.0), "silyl enol ether")

y = -5.6
e2 = s.molecule("[O-]C1=CCCCC1", at=(0, y), lone_pairs=[0])
mei = s.molecule("CI", at=(-0.1, y + 2.4), lone_pairs=[1])
s.curly(e2.atom(0), e2.bond(0, 1), bend=0.6)
s.curly(e2.bond(1, 2), mei.atom(0), bend=-0.4)
s.curly(mei.bond(0, 1), mei.atom(1), bend=0.5)
s.text((0, y - 2.0), "C-attack (soft electrophile)")
s.arrow((4.2, y), (5.6, y), below=r"$-$I$^-$")
s.molecule("O=C1CCCCC1C", at=(8.2, y))
s.text((8.2, y - 2.0), "C-alkylation product")
s.draw()
