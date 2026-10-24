"""Transmetalation in a Negishi coupling. The electron pair of the Zn-C bond of phenylzinc chloride
attacks palladium while the bromide on palladium bridges to zinc (four-centre transition state);
the phenyl group ends up on palladium and ZnBrCl leaves. Ar = aryl group from the oxidative
addition step; L = phosphine."""

exec(open("helpers.txt").read())

s = Scheme()
c, lab = spokes("Pd", [(90, "L"), (270, "L"), (180, "Ar")])
c += [(1.5, 0.0)]
pd = s.molecule("[Pd](*)(*)(*)Br", coords=c, at=(0, 0), labels=lab, lone_pairs=[4])
zn = s.molecule("[Zn](*)Cl", coords=[(1.5, 1.7), (0.35, 1.7), (2.8, 1.7)], at=(0, 0), labels={1: "Ph"})
s.curly(zn.bond(0, 1), pd.atom(0), bend=0.5)
s.curly(pd.atom(4), zn.atom(0), bend=-0.5)
s.text((0.3, -2.2), "Pd(II), 16 e", size=11)
s.arrow((3.6, 0.5), (5.2, 0.5))
x = 7.0
complex_at(s, "Pd", [(90, "L"), (270, "L"), (180, "Ar"), (0, "Ph")], at=(x, 0))
s.text((x, -2.2), "Pd(II), 16 e", size=11)
s.plus((x + 2.2, 0))
s.text((x + 3.5, 0), "ZnBrCl", size=12)
s.draw()
