"""Alkylation of a terminal alkyne (pent-1-yne). (1) Amide ion removes the acidic sp C-H proton (the
conjugate acid NH3 is a much weaker acid than the alkyne). (2) The acetylide ion attacks the carbon of
bromomethane from the back side (SN2) and bromide leaves: a new C-C bond, hex-2-yne."""

from wikichem import Scheme

ZIG = [(0, 0), (0.87, 0.5), (1.73, 0)]  # propyl zigzag, then the linear alkyne

s = Scheme()
alk = s.molecule("CCC[C:1]#[C:2][H:5]", coords=ZIG + [(2.73, 0), (3.73, 0), (4.73, 0)])
nh2 = s.molecule("[NH2-]", at=alk.xy(5) + (1.4, 0.0), lone_pairs=True)
s.curly(nh2.atom(0), alk.atom(5), bend=0.5)
s.curly(alk.bond(2, 5), alk.atom(2), bend=0.9)
s.arrow((7.4, 0), (8.4, 0), below=r"$-$NH$_3$")
x = 9.2
ac = s.molecule("CCC[C:1]#[C-:2]", coords=[(x + a, b) for a, b in ZIG + [(2.73, 0), (3.73, 0)]], lone_pairs=[2])
mebr = s.molecule("[CH3:3][Br:4]", coords=[(x + 5.4, 0), (x + 6.4, 0)], lone_pairs=[4])
s.curly(ac.atom(2), mebr.atom(3), bend=0.4)
s.curly(mebr.bond(3, 4), mebr.atom(4), bend=-0.6)
s.text((x + 4.4, -1.0), "SN2", size=10)
s.arrow((x + 7.6, 0), (x + 8.8, 0), below=r"$-$Br$^-$")
x2 = x + 9.6
s.molecule("CCCC#CC", coords=[(x2 + a, b) for a, b in ZIG + [(2.73, 0), (3.73, 0), (4.73, 0)]])
s.text((x2 + 2.4, -1.0), "hex-2-yne", size=10)
s.draw()
