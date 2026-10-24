"""Suprafacial [1,5]-hydrogen shift in (Z)-1,3-pentadiene: the C5-H bond, the two pi bonds and the
forming C1-H bond make a six-membered cyclic transition state; the hydrogen moves across one face of
the diene (the reaction is degenerate here and is followed with deuterium labels)."""

exec(open("fixedmol.txt").read())

h = ring(6, start=90)  # h[0] top (the migrating H), h[1] upper left, ..., h[5] upper right
s = Scheme()
m = fixed(s, "[H]CC=CC=C", [h[0], h[1], h[2], h[3], h[4], h[5]])
s.partial(m.xy(0), m.xy(5))
s.curly(m.bond(0, 1), (m.xy(0) + m.xy(5)) / 2 + (0.0, 0.1), bend=-0.6)
s.curly(m.bond(2, 3), m.bond(1, 2), bend=-0.6)
s.curly(m.bond(4, 5), m.bond(3, 4), bend=-0.6)
s.text((0, -1.7), "(Z)-1,3-pentadiene")
s.arrow((1.7, 0), (3.1, 0), above="[1,5]-H")
fixed(s, "C=CC=CC[H]", [h[1], h[2], h[3], h[4], h[5], h[0]], at=(4.7, 0))
s.text((4.7, -1.7), "(Z)-1,3-pentadiene")
s.draw()
