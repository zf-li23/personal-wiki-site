"""Curved arrows for the Diels-Alder reaction of s-cis butadiene with ethylene: in one step the two
pi bonds of the diene and the pi bond of the dienophile shift round a six-membered ring; two new
sigma bonds form at C1 and C4 of the diene and a new pi bond appears between C2 and C3."""

exec(open("fixedmol.txt").read())

h = ring(6, start=90)  # h[0] top, h[1] upper left, h[2] lower left, h[3] bottom, h[4] lower right, h[5] upper right
s = Scheme()
diene = fixed(s, "C=CC=C", [h[0], h[1], h[2], h[3]])
alkene = fixed(s, "C=C", [h[4], h[5]], at=(0.55, 0))
s.partial(diene.xy(0), alkene.xy(1))
s.partial(diene.xy(3), alkene.xy(0))
s.curly(diene.bond(0, 1), diene.bond(1, 2), bend=0.5)
s.curly(diene.bond(2, 3), (diene.xy(3) + alkene.xy(0)) / 2, bend=0.5)
s.curly(alkene.bond(0, 1), (alkene.xy(1) + diene.xy(0)) / 2, bend=0.5)
s.text((0.3, -1.75), "s-cis diene + dienophile")
s.arrow((2.1, 0), (3.5, 0), above="heat")
fixed(s, "C1=CCCCC1", [h[1], h[2], h[3], h[4], h[5], h[0]], at=(5.2, 0))
s.text((5.2, -1.75), "cyclohexene")
s.draw()
