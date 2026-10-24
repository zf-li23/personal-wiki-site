"""Elementary steps of radical reactions with fishhook arrows (one arrow per electron).
(1) Hydrogen atom transfer: a chlorine atom abstracts H from methane.
(2) Halogen atom transfer: a methyl radical abstracts Cl from Cl2.
Steps (1) and (2) are the two propagation steps of methane chlorination.
(3) Radical addition to a C=C bond and its reverse, beta-scission."""

import numpy as np
from wikichem import Scheme


def up(p, dy):
    """A point shifted vertically, to start or end a fishhook beside a bond."""
    return np.asarray(p.xy if hasattr(p, "xy") else p, float) + (0.0, dy)


# (1) Cl. + H-CH3 -> H-Cl + .CH3
s = Scheme()
cl = s.molecule("[Cl]", at=(0, 0))
hc = s.molecule("[H]C", coords=[(2.1, 0), (3.6, 0)], show_carbons=[1])
new = (cl.xy(0) + hc.xy(0)) / 2
s.curly(cl.atom(0), up(new, 0.22), bend=0.7, single=True)
s.curly(up(hc.bond(0, 1), 0.14), up(new, 0.24), bend=-0.6, single=True)
s.curly(up(hc.bond(0, 1), -0.14), hc.atom(1), bend=-0.9, single=True)
s.arrow((4.6, 0), (6.0, 0))
s.molecule("[H]Cl", coords=[(6.5, 0), (7.7, 0)])
s.plus((8.4, 0))
s.molecule("[CH3]", at=(9.4, 0), show_carbons=[0])
s.text((4.6, -1.3), r"$\Delta H = D(\mathrm{H{-}CH_3}) - D(\mathrm{H{-}Cl}) = 439 - 432 = +7$ kJ mol$^{-1}$", size=10)
s.draw()

# (2) .CH3 + Cl-Cl -> CH3-Cl + Cl.
s = Scheme()
me = s.molecule("[CH3]", at=(0, 0), show_carbons=[0])
cc = s.molecule("ClCl", coords=[(2.2, 0), (3.6, 0)])
new = (me.xy(0) + cc.xy(0)) / 2
s.curly(me.atom(0), up(new, 0.22), bend=0.7, single=True)
s.curly(up(cc.bond(0, 1), 0.14), up(new, 0.24), bend=-0.6, single=True)
s.curly(up(cc.bond(0, 1), -0.14), cc.atom(1), bend=-0.9, single=True)
s.arrow((4.5, 0), (5.9, 0))
s.molecule("CCl", coords=[(6.4, 0), (7.8, 0)], show_carbons=[0])
s.plus((8.6, 0))
s.molecule("[Cl]", at=(9.5, 0))
s.text((4.6, -1.3), r"$\Delta H = D(\mathrm{Cl{-}Cl}) - D(\mathrm{H_3C{-}Cl}) = 243 - 350 = -107$ kJ mol$^{-1}$", size=10)
s.draw()

# (3) R. + CH2=CH2 <=> R-CH2-CH2.  (addition / beta-scission)
s = Scheme()
me = s.molecule("[CH3]", at=(0, 0), show_carbons=[0])
alk = s.molecule("C=C", coords=[(2.3, 0), (3.9, 0)], show_carbons=[0, 1])
new = (me.xy(0) + alk.xy(0)) / 2
s.curly(me.atom(0), up(new, 0.22), bend=0.7, single=True)
s.curly(up(alk.bond(0, 1), 0.2), up(new, 0.26), bend=-0.6, single=True)
s.curly(up(alk.bond(0, 1), -0.2), alk.atom(1), bend=-0.9, single=True)
s.arrow((4.9, 0), (6.7, 0), above="addition", below=r"$\beta$-scission", kind="equilibrium")
s.molecule("CC[CH2]", at=(8.6, 0), show_carbons=[0, 1, 2])
s.draw()
