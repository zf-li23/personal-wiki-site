"""Cossee-Arlman mechanism of Ziegler-Natta chain growth ([Ti] = the titanium centre on the TiCl3
surface or a cationic metallocene, P = the growing polymer chain, the open square = vacant site).
Left: ethylene binds at the vacant site cis to the Ti-P bond (d0 titanium cannot back-bond, so the
complex is weak and inserts at once). Middle: the chain migrates with the Ti-P electron pair to
the far alkene carbon while the pi electrons bond the near carbon to titanium (four-centre
transition state). Right: the chain is two carbons longer and the vacant site has moved to where
the chain was, ready for the next monomer."""

exec(open("cycle.txt").read())

s = Scheme()
t1 = complex_at(s, "Ti", [(180, "Cl"), (270, "Cl"), (90, "P")], (0, 0))
s.text((1.3, 0.0), "\u25a1", size=14)
s.arrow((2.2, 0), (3.6, 0), above="C$_2$H$_4$")
x = 5.4
m = s.molecule("[Ti](*)(*)*.C=C", coords=[(0, 0), (-1.2, 0), (0, -1.2), (0, 1.4), (1.9, 0.7), (1.9, -0.7)], at=(x, 0),
               labels={1: "Cl", 2: "Cl", 3: "P"})
p, q = m.xy(0) + np.array([0.35, 0.0]), (m.xy(4) + m.xy(5)) / 2 - np.array([0.1, 0.0])
s.partial(p, q)
s.curly(m.bond(0, 3), m.atom(4), bend=-0.4)
s.curly(m.bond(4, 5), (m.xy(0) + m.xy(5)) / 2, bend=-0.5)
s.arrow((x + 3.0, 0), (x + 4.4, 0), above="insertion")
x2 = x + 6.2
s.molecule("[Ti](*)(*)CC*", coords=[(0, 0), (-1.2, 0), (0, -1.2), (1.3, 0), (1.8, 0.87), (2.8, 0.87)], at=(x2, 0),
           labels={1: "Cl", 2: "Cl", 5: "P"})
s.text((x2, 1.3), "\u25a1", size=14)
s.draw()
