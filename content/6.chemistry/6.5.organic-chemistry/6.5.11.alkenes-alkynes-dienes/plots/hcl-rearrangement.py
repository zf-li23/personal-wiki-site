"""Carbocation rearrangement during electrophilic addition: 3-methylbut-1-ene and HCl. The pi bond
takes the proton at the CH2 end (secondary cation, Markovnikov). Chloride can capture this cation
(2-chloro-3-methylbutane), or a hydride on the neighbouring tertiary carbon shifts with its electron
pair (1,2-hydride shift) to give the more stable tertiary cation, which gives 2-chloro-2-methylbutane."""

from wikichem import Scheme

s = Scheme()
alkene = s.molecule("[CH2:1]=[CH:2][CH:3](C)C", at=(0, 0))
hcl = s.molecule("Cl", at=alkene.xy(1) + (1.3, 1.3), show_h=[0], lone_pairs=True)
s.curly(alkene.bond(1, 2), hcl.h(0), bend=-0.4)
s.curly((hcl.xy(0) + hcl.h(0).xy) / 2, hcl.atom(0), bend=-0.9)
s.arrow((2.4, 0), (3.6, 0))
sec = s.molecule("[CH3:1][CH2:2][CH:3](C)C", at=(5.4, 0), show_h=[3])
s.text(sec.xy(2) + (0, 0.42), "+")
h = sec.h(3)
s.curly((sec.xy(3) + h.xy) / 2, sec.bond(2, 3), bend=-1.2)
s.text((5.4, -1.5), "secondary cation", size=10)
s.arrow((7.6, 0), (9.4, 0), above="1,2-H shift")
tert = s.molecule("[CH3:1][CH2:2][CH:3](C)C", at=(11.4, 0))
s.text(tert.xy(3) + (0.42, 0.1), "+")
s.text((11.4, -1.5), "tertiary cation", size=10)
s.arrow((5.4, -2.0), (5.4, -3.2), below=r"Cl$^-$")
s.arrow((11.4, -2.0), (11.4, -3.2), below=r"Cl$^-$")
s.molecule("CC(Cl)C(C)C", at=(5.4, -4.6))
s.molecule("CCC(C)(C)Cl", at=(11.4, -4.6))
s.text((5.4, -6.0), "2-chloro-3-methylbutane", size=10)
s.text((11.4, -6.0), "2-chloro-2-methylbutane (rearranged)", size=10)
s.draw()
