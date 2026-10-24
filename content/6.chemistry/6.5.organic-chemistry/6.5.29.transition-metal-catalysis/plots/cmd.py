"""Concerted metalation-deprotonation (CMD), the usual C-H activation step with Pd(II)
carboxylates (L = a ligand or the directing group). In a six-membered transition state the
acetate bound to palladium uses its other oxygen as an internal base: its lone pair takes the
arene proton while the C-H electrons form the new Pd-C bond. No Pd(IV) or free carbanion is
involved; acetic acid leaves and an arylpalladium(II) complex forms, which then enters a coupling
cycle. Electron-poor and acidic C-H bonds react fastest, unlike electrophilic palladation."""

exec(open("cycle.txt").read())

s = Scheme()
HEX = [(1.4, -0.2), (2.4, -0.2), (2.9, -1.07), (2.4, -1.94), (1.4, -1.94), (0.9, -1.07)]
ts = s.molecule("[Pd](*)OC(C)=O.[H]c1ccccc1",
                coords=[(0, 0), (-1.2, -0.4), (-0.5, 1.0), (0.3, 1.7), (0.1, 2.7), (1.3, 1.5), (1.7, 0.6)] + HEX,
                labels={1: "L"}, lone_pairs=[5])
s.partial(ts.atom(0), ts.atom(7))
s.curly(ts.atom(5), ts.atom(6), bend=-0.5)
s.curly(ts.bond(6, 7), ts.bond(0, 7), bend=0.6)
s.text((0.8, -2.8), "six-membered CMD TS", size=11)
s.arrow((3.6, 0), (5.0, 0), below="$-$AcOH")
s.molecule("[Pd](*)c1ccccc1", coords=[(0, 0), (-1.2, 0)] + [(1.3, 0), (1.8, 0.87), (2.8, 0.87), (3.3, 0), (2.8, -0.87), (1.8, -0.87)],
           at=(6.6, 0), labels={1: "L"})
s.draw()
