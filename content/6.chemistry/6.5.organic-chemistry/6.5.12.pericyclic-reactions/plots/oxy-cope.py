"""Anionic oxy-Cope rearrangement. The potassium alkoxide of hexa-1,5-dien-3-ol (KH, 18-crown-6)
undergoes the [3,3] shift some 10^10 times faster than the neutral alcohol: the C3-C4 bond, weakened
by the adjacent alkoxide, breaks as the C1-C6 bond forms through the chair-like cyclic array. The
product is an enolate, which is protonated at work-up to give hex-5-enal; the strong C=O bond makes
the reaction irreversible."""

exec(open("fixedmol.txt").read())

h = ring(6, start=0)

s = Scheme()
# atoms of C=CC([O-])CC=C: 0 C1, 1 C2, 2 C3, 3 O, 4 C4, 5 C5, 6 C6; the new bond C1-C6
ox = fixed(s, "C=CC([O-])CC=C", [h[5], h[0], h[1], (1.0, 1.75), h[2], h[3], h[4]], lone_pairs=(3,))
s.partial(ox.xy(0), ox.xy(6))
s.curly(ox.bond(5, 6), (ox.xy(0) + ox.xy(6)) / 2, bend=0.5)
s.curly(ox.bond(2, 4), ox.bond(4, 5), bend=-0.6)
s.curly(ox.bond(0, 1), ox.bond(1, 2), bend=-0.5)
s.text((0, -1.75), "alkoxide (K$^+$, 18-crown-6)")
s.arrow((1.9, 0), (3.3, 0), above="[3,3]", below="fast")
# atoms of [O-]C=CCCC=C: 0 O, 1 C3, 2 C2, 3 C1, 4 C6, 5 C5, 6 C4
fixed(s, "[O-]C=CCCC=C", [(1.0, 1.75), h[1], h[0], h[5], h[4], h[3], h[2]], at=(5.0, 0))
s.text((5.0, -1.75), "enolate")
s.arrow((6.7, 0), (8.1, 0), above=r"H$_3$O$^+$")
s.molecule("O=CCCCC=C", at=(10.9, 0))
s.text((10.9, -1.75), "hex-5-enal")
s.draw()
