"""Acid-base steps written with curved arrows. (a) Protonation of acetone by the hydronium ion: the
oxygen lone pair takes the proton and the O-H bonding pair stays on water. The protonated ketone is
a resonance hybrid with a carbocation contributor, which is why protonation activates the carbonyl
carbon toward nucleophiles. (b) A Lewis acid-base reaction without a proton: the ether oxygen
donates a lone pair into the empty p orbital of boron trifluoride."""

from wikichem import Scheme

s = Scheme(scale=0.46)

# (a) acetone + H3O+ -> protonated acetone <-> carbocation contributor
y = 0.0
s.text((-2.4, y), "(a)")
acetone = s.molecule("CC(C)=O", at=(0.0, y), rotate=-90, lone_pairs=[3])
h3o = s.molecule("[OH3+]", at=(3.3, y), explicit_h=True, rotate=90, lone_pairs=True)
left_h = min((1, 2, 3), key=lambda k: h3o.xy(k)[0])  # the hydrogen facing acetone
s.curly(acetone.atom(3), h3o.atom(left_h), bend=-0.5)
s.curly(h3o.bond(0, left_h), h3o.atom(0), bend=-0.9)
s.arrow((4.8, y), (6.2, y), kind="equilibrium")
p = s.molecule("CC(C)=[OH+]", at=(7.8, y), rotate=-90, lone_pairs=[3])
s.curly(p.bond(1, 3), p.atom(3), bend=-0.6)
s.arrow((9.4, y), (10.6, y), kind="resonance")
s.molecule("C[C+](C)O", at=(12.2, y), rotate=-90, lone_pairs=[3])
s.text((5.5, y - 0.8), r"$+\ \mathrm{H_2O}$", size=10)

# (b) Et2O + BF3 -> Et2O-BF3
y = -4.0
s.text((-2.4, y), "(b)")
ether = s.molecule("CCOCC", at=(0.0, y), lone_pairs=[2])
bf3 = s.molecule("FB(F)F", at=(2.9, y), rotate=-90)
s.curly(ether.atom(2), bf3.atom(1), bend=0.35)
s.arrow((4.8, y), (6.2, y))
s.molecule("CC[O+](CC)[B-](F)(F)F", at=(8.4, y), lone_pairs=[2])
s.text((0.0, y - 1.6), "Lewis base")
s.text((2.9, y - 1.6), "Lewis acid")
s.draw()
