"""1,2-Migratory insertion of ethylene into a metal-hydride bond. The coordinated alkene and the
cis hydride lie in one plane; through a four-centre transition state the hydrogen moves (with the
M-H electron pair) to one alkene carbon while the pi electrons bond the other carbon to the
metal: syn addition of M and H across the double bond, giving an ethyl complex with one fewer
ligand electron pair (a vacant site). The reverse reaction is beta-hydride elimination."""

exec(open("helpers.txt").read())

s = Scheme()
c = [(0.0, 0.0), (-1.3, 0.0), (0.0, -1.0), (0.0, 1.4), (1.9, 0.7), (1.9, -0.7)]
m = s.molecule("[Rh](*)(*)([H])", coords=c[:4], at=(0, 0), labels={0: "M", 1: "L", 2: "L"})
ene = s.molecule("C=C", coords=c[4:], at=(0, 0), show_carbons=[])
eta2(s, m.xy(0), ene.atom(0), ene.atom(1))
s.curly(m.bond(0, 3), ene.atom(0), bend=-0.4)
s.curly(ene.bond(0, 1), between(m.atom(0), ene.atom(1), 0.6), bend=-0.7)
s.arrow((3.0, 0), (4.6, 0))
x = 6.2
ts = s.molecule("[Rh](*)(*)[H].C=C", coords=[(0, 0), (-1.3, 0), (0, -1.0), (0, 1.25), (1.45, 0.75), (1.45, -0.55)],
                at=(x, 0), labels={0: "M", 1: "L", 2: "L"})
s.partial(ts.atom(3), ts.atom(4))
s.partial(ts.atom(0), ts.atom(5))
s.text((x + 0.6, -1.9), "four-centre TS", size=11)
s.arrow((x + 2.4, 0), (x + 4.0, 0))
x2 = x + 5.6
s.molecule("[Rh](*)(*)CC[H]", coords=[(0, 0), (-1.3, 0), (0, -1.0), (1.2, 0.0), (1.8, 1.0), (1.2, 1.85)],
           at=(x2, 0), labels={0: "M", 1: "L", 2: "L"})
s.draw()
