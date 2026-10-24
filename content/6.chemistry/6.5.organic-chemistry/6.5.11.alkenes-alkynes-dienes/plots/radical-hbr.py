"""Radical chain addition of HBr to propene (peroxide effect). Initiation: the weak O-O bond of a
peroxide breaks homolytically and the alkoxyl radical abstracts H from HBr. Propagation: Br adds to
the CH2 end to give the more stable secondary radical, which abstracts H from HBr and regenerates
Br: anti-Markovnikov 1-bromopropane. Fishhook arrows move single electrons."""

from wikichem import Scheme


s = Scheme()
# initiation (as equations)
s.text((-0.6, 1.6), "initiation:")
s.text((1.4, 0.6), r"RO$-$OR")
s.arrow((2.6, 0.6), (3.9, 0.6), above=r"$h\nu$ or $\Delta$")
s.text((5.0, 0.6), r"2 RO$^{\bullet}$")
s.text((10.2, 0.6), r"RO$^{\bullet}$ + H$-$Br  $\rightarrow$  RO$-$H + Br$^{\bullet}$")

# propagation step 1: the bromine atom adds to the terminal carbon
y = -1.9
s.text((-0.6, y + 1.0), "propagation:")
br = s.molecule("[Br]", at=(0.2, y))
alkene = s.molecule("C=CC", at=(2.3, y - 0.3))
s.curly(br.atom(0), alkene.atom(0), bend=-0.6, single=True)
s.curly(alkene.bond(0, 1), alkene.atom(0), bend=0.9, single=True)
s.curly(alkene.bond(0, 1), alkene.atom(1), bend=-0.9, single=True)
s.arrow((3.6, y), (4.9, y))
s.molecule("BrC[CH]C", at=(6.3, y))
s.text((6.3, y - 1.3), "secondary radical")

# propagation step 2: hydrogen atom transfer from HBr regenerates the bromine atom
s.text((9.0, y), r"+ H$-$Br")
s.arrow((10.0, y), (11.2, y))
s.molecule("BrCCC", at=(12.6, y))
s.text((14.9, y), r"+ Br$^{\bullet}$")
s.text((12.6, y - 1.3), "1-bromopropane")
s.draw()
