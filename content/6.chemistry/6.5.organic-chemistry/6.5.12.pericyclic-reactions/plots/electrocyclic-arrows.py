"""Curved arrows for the 6-electron electrocyclic ring closure of (Z)-1,3,5-hexatriene to
1,3-cyclohexadiene: the three pi bonds shift round the ring and a sigma bond forms between C1 and C6.
The arrows only book-keep the electrons; the stereochemistry (disrotatory under heat) follows from
the orbital symmetry of the HOMO."""

exec(open("fixedmol.txt").read())

h = ring(6, start=270 - 30)  # C1 lower left ... C6 lower right; the gap C1-C6 is at the bottom
order = [h[0], h[5], h[4], h[3], h[2], h[1]]
s = Scheme()
tri = fixed(s, "C=CC=CC=C", [h[5], h[4], h[3], h[2], h[1], h[0]])
s.partial(tri.xy(0), tri.xy(5))
s.curly(tri.bond(4, 5), mid(tri, 0, 5), bend=0.5)
s.curly(tri.bond(2, 3), tri.bond(3, 4), bend=-0.5)
s.curly(tri.bond(0, 1), tri.bond(1, 2), bend=-0.5)
s.text((0, -1.7), "(Z)-1,3,5-hexatriene")
s.arrow((1.6, 0), (3.0, 0), above="heat", below="disrotatory")
diene = fixed(s, "C1=CC=CCC1", [h[4], h[3], h[2], h[1], h[0], h[5]], at=(4.6, 0))
s.text((4.6, -1.7), "1,3-cyclohexadiene")
s.draw()
