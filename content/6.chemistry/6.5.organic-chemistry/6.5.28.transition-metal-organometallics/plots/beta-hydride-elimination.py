"""Beta-hydride elimination from a coordinatively unsaturated alkylpalladium(II) complex
L(Cl)Pd-CH2CH2CH3 (14 e, with a vacant site cis to the alkyl). The Pd-C-C-H unit is syn-coplanar;
the C-H electron pair moves to palladium, forming Pd-H, and the Pd-C electron pair becomes the
new C=C pi bond. The product is a hydridopalladium complex of propene, the reverse of a
1,2-insertion."""

exec(open("helpers.txt").read())

s = Scheme()
coords = [(0, 0), (-1.3, 0), (0, -1.25), (1.6, 0), (1.6, 1.6), (2.7, 2.2), (0.25, 1.6)]
pd = s.molecule("[Pd](*)(Cl)CC(C)[H]", coords=coords, at=(0, 0), labels={1: "L"})
s.partial(pd.atom(0), pd.atom(6))
s.curly(pd.bond(4, 6), between(pd.atom(0), pd.atom(6), 0.45), bend=0.5)
s.curly(pd.bond(0, 3), pd.bond(3, 4), bend=0.6)
s.text((0.5, -2.2), "14 e (16 e with the agostic C-H)", size=11)
s.arrow((3.6, 0.3), (5.2, 0.3))
x = 7.0
prod = s.molecule("[Pd](*)(Cl)[H].C=CC", coords=[(0, 0), (-1.3, 0), (0, -1.25), (0, 1.25), (1.4, -0.62), (1.4, 0.62), (2.4, 1.2)],
                  at=(x, 0), labels={1: "L"})
eta2(s, prod.xy(0), prod.atom(4), prod.atom(5))
s.text((x + 0.3, -2.2), "16 e", size=11)
s.draw()
