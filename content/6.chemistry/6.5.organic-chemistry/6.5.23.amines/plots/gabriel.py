"""Gabriel synthesis, alkylation step: the phthalimide anion (pKa of phthalimide 8.3) attacks the
alpha carbon of bromoethane from the back (SN2), giving N-ethylphthalimide and bromide."""

from wikichem import Scheme

s = Scheme()
imide = s.molecule("O=C1c2ccccc2C(=O)[N-:1]1", at=(0, 0), lone_pairs=[1])
n = imide.xy(1)
bromo = s.molecule("C[CH2:2][Br:3]", at=(n[0] + 2.4, n[1] + 0.3), flip=True)
s.curly(imide.atom(1), bromo.atom(2), bend=-0.4)
s.curly(bromo.bond(2, 3), bromo.atom(3), bend=-0.6)
x = bromo.xy(3)[0] + 0.9
s.arrow((x, 0), (x + 1.4, 0), above="DMF")
s.molecule("O=C1c2ccccc2C(=O)N1CC", at=(x + 4.0, 0))
s.plus((x + 6.6, 0))
s.molecule("[Br-]", at=(x + 7.4, 0))
s.draw()
