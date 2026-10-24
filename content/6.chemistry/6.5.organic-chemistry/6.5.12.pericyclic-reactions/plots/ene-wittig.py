"""Two further pericyclic reactions. Figure 1: the ene reaction: an alkene with an allylic hydrogen
(the ene) adds to an activated multiple bond (the enophile) through a six-membered transition state;
the double bond moves and the allylic hydrogen is transferred. Figure 2: the [2,3]-Wittig
rearrangement of an allyl ether carbanion through a five-membered transition state, giving a
homoallylic alkoxide."""

exec(open("fixedmol.txt").read())

h = ring(6, start=90)
s = Scheme()
ene = fixed(s, "[H]CC=C", [h[0], h[1], h[2], h[3]])
eno = fixed(s, "C=C", [h[4], h[5]], at=(0.5, 0))
s.partial(ene.xy(3), eno.xy(0))
s.partial(ene.xy(0), eno.xy(1))
s.curly(ene.bond(2, 3), (ene.xy(3) + eno.xy(0)) / 2, bend=0.5)
s.curly(eno.bond(0, 1), (eno.xy(1) + ene.xy(0)) / 2, bend=0.5)
s.curly(ene.bond(0, 1), ene.bond(1, 2), bend=0.6)
s.text((-0.2, -1.7), "ene")
s.text((1.4, -1.7), "enophile")
s.arrow((2.2, 0), (3.6, 0), above=r"$\Delta$")
fixed(s, "[H]CCCC=C", [h[0], h[5], h[4], h[3], h[2], h[1]], at=(5.2, 0))
s.draw()

p = ring(5, start=90)  # p[0] top, p[1] upper left, p[2] lower left, p[3] lower right, p[4] upper right
s = Scheme()
an = fixed(s, "C[CH-]OCC=C", [(-1.7, 0.75), p[1], p[0], p[4], p[3], p[2]], lone_pairs=(1,))
s.partial(an.xy(1), an.xy(5))
s.curly(an.atom(1), (an.xy(1) + an.xy(5)) / 2, bend=0.5)
s.curly(an.bond(4, 5), an.bond(3, 4), bend=0.5)
s.curly(an.bond(2, 3), an.atom(2), bend=0.6)
s.text((0, -1.5), "allyl ether carbanion")
s.arrow((1.6, 0), (3.0, 0), above="[2,3]")
fixed(s, "CC([O-])CC=C", [(-1.7 + 4.6, 0.75), np.array(p[1]) + (4.6, 0), np.array(p[0]) + (4.6, 0), np.array(p[2]) + (4.6, 0),
                          np.array(p[3]) + (4.6, 0), np.array(p[4]) + (4.6, 0)], lone_pairs=(2,))
s.text((4.6, -1.5), "homoallylic alkoxide")
s.draw()
