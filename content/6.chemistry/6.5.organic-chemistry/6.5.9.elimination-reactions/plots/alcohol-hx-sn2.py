"""SN2 reaction of butan-1-ol with hydrobromic acid. Protonation turns the hydroxy group into water,
a good leaving group; bromide then attacks the CH2 carbon from the back side as water leaves, without
a primary carbocation, giving 1-bromobutane."""

from wikichem import Scheme

s = Scheme()
alc = s.molecule("CCCCO", at=(0, 0), lone_pairs=[4])
hbr = s.molecule("Br", at=(2.6, 0.8), explicit_h=True, lone_pairs=[0], rotate=180)
s.curly(alc.atom(4), hbr.atom(1), bend=-0.5)
s.curly(hbr.bond(0, 1), hbr.atom(0), bend=-0.8)
s.arrow((3.9, 0), (5.1, 0), kind="equilibrium")
ox = s.molecule("CCCC[OH2+]", at=(8.4, -0.3))
c3 = ox.xy(3)
br = s.molecule("[Br-]", at=(c3[0] - 1.6, c3[1] + 1.0), lone_pairs=True)
s.curly(br.atom(0), ox.atom(3), bend=0.3)
s.curly(ox.bond(3, 4), ox.atom(4), bend=0.8)
s.arrow((11.0, 0), (12.2, 0))
s.molecule("CCCCBr", at=(13.9, 0))
s.plus((16.5, 0))
s.text((17.4, 0), r"H$_2$O")
s.draw()
