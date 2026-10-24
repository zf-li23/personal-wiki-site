"""Reductive elimination from cis-dimethylpalladium(II), cis-PdMe2L2 (16 e, d8). The two methyl
groups must be cis: the electrons of one Pd-C bond form the new C-C bond while the other Pd-C
pair returns to the metal, through a three-centre transition state with retention at carbon.
Ethane leaves and Pd(0)L2 (14 e) remains."""

exec(open("helpers.txt").read())

s = Scheme()
c, lab = spokes("Pd", [(180, "L"), (270, "L")])
c += [(1.6, 0.0), (0.0, 1.6)]
pd = s.molecule("[Pd](*)(*)(C)C", coords=c, at=(0, 0), labels=lab, show_carbons=[3, 4])
s.curly(pd.bond(0, 3), between(pd.atom(3), pd.atom(4), 0.5), bend=-0.5)
s.curly(pd.bond(0, 4), pd.atom(0), bend=0.7)
s.partial(pd.atom(3), pd.atom(4))
s.text((0, -2.1), "Pd(II), 16 e", size=12)
s.arrow((2.6, 0.3), (4.2, 0.3))
complex_at(s, "Pd", [(180, "L"), (0, "L")], at=(6.0, 0.3))
s.text((6.0, -2.1), "Pd(0), 14 e", size=12)
s.plus((7.7, 0.3))
s.molecule("CC", coords=[(0, 0), (1.1, 0)], at=(9.0, 0.3), show_carbons=[0, 1])
s.draw()
