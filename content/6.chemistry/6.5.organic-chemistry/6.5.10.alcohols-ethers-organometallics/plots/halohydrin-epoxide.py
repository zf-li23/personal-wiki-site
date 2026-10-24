"""Intramolecular Williamson reaction: trans-2-chlorocyclohexanol in aqueous NaOH. Hydroxide removes
the hydroxy proton; the alkoxide, on the face opposite to chlorine, attacks the neighbouring carbon
from the back side and chloride leaves (SN2), giving cyclohexene oxide. In the cis isomer the
alkoxide and chlorine are on the same face and backside attack is impossible."""

from wikichem import Scheme

s = Scheme()
ch = s.molecule("O[C@@H]1CCCC[C@H]1Cl", at=(0, 0), lone_pairs=[0], show_h=[0])
ho = s.molecule("[OH-]", at=(-2.4, 1.4), lone_pairs=True)
s.curly(ho.atom(0), ch.h(0), bend=-0.4)
s.curly((ch.h(0).xy + ch.xy(0)) / 2, ch.atom(0), bend=-0.8)
s.text((0, -2.0), "trans-2-chlorocyclohexanol")
s.arrow((2.2, 0), (3.6, 0), below=r"$-$H$_2$O")
al = s.molecule("[O-][C@@H]1CCCC[C@H]1Cl", at=(5.6, 0), lone_pairs=[0, 7])
s.curly(al.atom(0), al.atom(6), bend=0.5)
s.curly(al.bond(6, 7), al.atom(7), bend=0.7)
s.arrow((7.8, 0), (9.2, 0), below=r"$-$Cl$^-$")
s.molecule("C1CCC2OC2C1", at=(10.8, 0))
s.text((10.8, -2.0), "cyclohexene oxide")
s.draw()
