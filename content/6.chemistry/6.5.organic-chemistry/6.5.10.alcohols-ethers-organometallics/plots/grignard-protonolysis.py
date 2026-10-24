"""The Grignard reagent as a strong base. Top: the C-Mg bonding pair takes a proton from water and
the O-H bonding pair stays on oxygen, giving methane and HOMgBr. Bottom: a terminal alkyne
(pKa about 25) is deprotonated in the same way by ethylmagnesium bromide, giving ethane and an
alkynyl Grignard reagent."""

from wikichem import Scheme

s = Scheme()
y = 0.0
g = s.molecule("C[Mg]Br", at=(0, y))
w = s.molecule("O", at=(2.2, y + 0.4), explicit_h=True, lone_pairs=[0])
s.curly(g.bond(0, 1), w.atom(1), bend=-0.5)
s.curly(w.bond(0, 1), w.atom(0), bend=-0.7)
s.arrow((3.4, y), (4.8, y))
s.text((6.6, y), r"CH$_4$  +  HOMgBr")

y = -2.8
g2 = s.molecule("CC[Mg]Br", at=(0, y))
al = s.molecule("C#CCCC", at=(3.2, y + 0.4), show_h=[0])
s.curly(g2.bond(1, 2), al.h(0), bend=-0.5)
s.curly((al.h(0).xy + al.xy(0)) / 2, al.atom(0), bend=-0.8)
s.arrow((5.4, y), (6.8, y))
s.text((8.0, y), r"C$_2$H$_6$  +")
s.molecule("Br[Mg]C#CCCC", at=(10.6, y))
s.draw()
