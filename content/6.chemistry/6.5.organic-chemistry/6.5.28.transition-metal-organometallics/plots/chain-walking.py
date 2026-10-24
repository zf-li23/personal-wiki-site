"""Why hydrozirconation of an internal alkene gives a terminal alkylzirconium ([Zr] = Cp2ZrCl,
R = n-hexyl; oct-2-ene shown). Top: the secondary alkyl (Zr on C2) undergoes beta-hydride
elimination toward the methyl group: a C-H electron pair moves to zirconium (Zr-H) while the Zr-C
electrons form the C=C bond, giving a hydride complex of oct-1-ene. Bottom: the alkene reinserts
into Zr-H with the opposite regiochemistry, zirconium going to the less hindered terminal carbon.
Repeated elimination and reinsertion move the metal along the chain; the primary alkyl is the
most stable (least crowded) and accumulates."""

exec(open("helpers.txt").read())

s = Scheme()
z = s.molecule("[Zr]C(*)C[H]", coords=[(0, 0), (1.5, 0), (2.4, -0.6), (1.5, 1.4), (0.3, 1.6)], labels={0: "[Zr]", 2: "R"})
s.partial(z.atom(0), z.atom(4))
s.curly(z.bond(3, 4), between(z.atom(0), z.atom(4), 0.45), bend=0.5)
s.curly(z.bond(0, 1), z.bond(1, 3), bend=0.6)
s.arrow((3.4, 0.4), (4.8, 0.4), kind="equilibrium", above="$\\beta$-H elim.")
x = 7.2
h = s.molecule("[Zr][H].C=C*", coords=[(0, 0), (0, 1.25), (1.4, 0.62), (1.4, -0.62), (2.4, -1.2)], at=(x, 0.4),
               labels={0: "[Zr]", 4: "R"})
eta2(s, h.xy(0), h.atom(2), h.atom(3))
s.text((x + 0.6, -2.0), "oct-1-ene complex", size=11)

y = -4.6
h2 = s.molecule("[Zr][H].C=C*", coords=[(0, 0), (0, 1.25), (1.4, 0.62), (1.4, -0.62), (2.4, -1.2)], at=(0, y),
                labels={0: "[Zr]", 4: "R"})
eta2(s, h2.xy(0), h2.atom(2), h2.atom(3))
s.curly(h2.bond(0, 1), h2.atom(3), bend=-0.7)
s.curly(h2.bond(2, 3), between(h2.atom(0), h2.atom(2), 0.6), bend=0.5)
s.arrow((3.4, y), (4.8, y), kind="equilibrium", above="insertion")
s.molecule("[Zr]CC*", coords=[(0, 0), (1.4, 0), (1.9, 0.87), (2.9, 0.87)], at=(6.6, y), labels={0: "[Zr]", 3: "R"})
s.text((8.0, y - 1.2), "primary alkyl (n-octyl)", size=11)
s.draw()
