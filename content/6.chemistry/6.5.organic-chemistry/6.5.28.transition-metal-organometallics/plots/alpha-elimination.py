"""Formation of a Schrock carbene by alpha-hydrogen abstraction (Np = neopentyl CH2CMe3). In
Ta(CH2CMe3)5 the crowding brings two neopentyl groups together: the Ta-C electrons of one group
take an alpha-hydrogen of its neighbour (four-centre transition state, Ta, C, H, C) while the C-H
electrons of that neighbour form the Ta=C pi bond. Neopentane leaves and the tantalum(V)
alkylidene (Me3CCH2)3Ta=CHCMe3 remains; the oxidation state of tantalum does not change."""

exec(open("helpers.txt").read())

s = Scheme()
ta = s.molecule("[Ta](*)(*)(*)(C(*)[H])C*",
                coords=[(0, 0), (-1.2, 0.6), (-1.2, -0.6), (0, -1.3), (1.2, 0.8), (1.6, 1.8), (2.0, 0.2), (1.3, -0.7), (2.3, -1.2)],
                labels={0: "Ta", 1: "Np", 2: "Np", 3: "Np", 5: "$t$-Bu", 8: "$t$-Bu"})
s.partial(ta.atom(6), ta.atom(7))
s.curly(ta.bond(0, 7), ta.atom(6), bend=0.6)
s.curly(ta.bond(4, 6), ta.bond(0, 4), bend=0.6)
s.text((0.5, -2.4), "four-centre TS", size=11)
s.arrow((3.4, 0), (4.8, 0), below="$-$CMe$_4$")
x = 6.8
s.molecule("[Ta](*)(*)(*)=C*", coords=[(0, 0), (-1.2, 0.6), (-1.2, -0.6), (0, -1.3), (1.4, 0.4), (2.0, 1.3)], at=(x, 0),
           labels={0: "Ta", 1: "Np", 2: "Np", 3: "Np", 5: "$t$-Bu"})
s.text((x + 0.5, -2.4), "Schrock alkylidene, Ta(V)", size=11)
s.draw()
