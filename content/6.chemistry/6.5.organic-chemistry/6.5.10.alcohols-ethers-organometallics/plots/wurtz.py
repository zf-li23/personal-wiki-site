"""Wurtz coupling of 1-bromopropane with sodium. Sodium transfers one electron into the C-Br bond,
which breaks into a propyl radical and NaBr; a second sodium atom reduces the radical to
propylsodium, a carbanion equivalent, which attacks a second molecule of 1-bromopropane by SN2,
giving hexane."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.text((-1.6, y + 0.9), "Na")
rb = s.molecule("BrCCC", at=(0.4, y - 0.2), lone_pairs=[0])
s.curly((-1.3, y + 0.9), rb.bond(0, 1), bend=-0.5, single=True)
s.curly(rb.bond(0, 1), rb.atom(0), bend=0.9, single=True)
s.arrow((2.0, y), (3.4, y), below=r"$-$NaBr")
s.molecule("[CH2]CC", at=(4.4, y))
s.arrow((5.4, y), (6.8, y), above="Na")
s.molecule("CC[CH2-]", at=(7.8, y), lone_pairs=[2])
s.text((7.8, y - 1.1), r"Na$^+$", size=11)

y = -3.0
an = s.molecule("CC[CH2-]", coords=[(-2.6, 0.5), (-1.73, 0), (-0.87, 0.5)], at=(0, y), lone_pairs=[2])
rb2 = s.molecule("CCCBr", coords=[(0, 1.73), (-0.5, 0.87), (0, 0), (1, 0)], at=(1.0, y), lone_pairs=[3])
s.curly(an.atom(2), rb2.atom(2), bend=-0.5)
s.curly(rb2.bond(2, 3), rb2.atom(3), bend=0.8)
s.arrow((3.2, y), (4.6, y), above=r"S$_{\mathrm{N}}$2", below=r"$-$NaBr")
s.molecule("CCCCCC", at=(6.8, y))
s.draw()
