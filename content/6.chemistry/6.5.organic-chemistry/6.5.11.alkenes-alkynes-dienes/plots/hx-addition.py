"""Electrophilic addition of HBr to propene. Step 1 (slow): the C=C pi bond takes the proton and the
H-Br bond breaks heterolytically; the proton goes to the CH2 end so that the secondary cation forms.
Step 2 (fast): bromide attacks the carbocation."""

from wikichem import Scheme

s = Scheme()
alkene = s.molecule("CC=C", at=(0, 0), rotate=0)
hbr = s.molecule("Br", at=(2.3, 0.9), lone_pairs=True, explicit_h=True, rotate=180)
s.curly(alkene.bond(1, 2), hbr.atom(1), bend=-0.45)
s.curly(hbr.bond(0, 1), hbr.atom(0), bend=1.0)
s.arrow((3.5, 0.2), (5.0, 0.2), above="slow")
cation = s.molecule("CCC", at=(6.6, 0))
s.text(cation.xy(1) + (0, 0.42), "+")
bromide = s.molecule("[Br-]", at=(8.6, 0.9), lone_pairs=True)
s.curly(bromide.atom(0), cation.atom(1), bend=0.4)
s.arrow((9.6, 0.2), (11.1, 0.2), above="fast")
s.molecule("CC(Br)C", at=(12.6, 0), lone_pairs=False)
s.text((0.3, -1.3), "propene")
s.text((6.6, -1.3), "2-propyl cation")
s.text((12.6, -1.3), "2-bromopropane")
s.draw()
