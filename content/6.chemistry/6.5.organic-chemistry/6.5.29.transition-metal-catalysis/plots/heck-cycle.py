"""Catalytic cycle of the Mizoroki-Heck reaction (neutral pathway, L = PPh3, X = Br or I).
Pd(0)L2 adds the aryl halide (oxidative addition); one phosphine is replaced by the alkene, which
inserts into the Pd-Ar bond (syn 1,2-migratory insertion, the aryl going to the less substituted
carbon); syn beta-hydride elimination releases the E-alkene product; the base removes HX from the
hydridopalladium halide (formally a reductive elimination) and regenerates Pd(0)L2."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.6
complex_at(s, "Pd", [(180, "L"), (0, "L")], polar(R, 90), ox="0")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "Ar"), (270, "X")], polar(R, 18), ox="II")
pi = complex_at(s, "Pd", [(180, "L"), (90, "Ar"), (270, "X")], polar(R, -54) + np.array([-0.4, 0]), ox="II", ox_angle=135)
alkene(s, pi, 0, subst="R")
complex_at(s, "Pd", [(180, "L"), (90, "CH(R)CH$_2$Ar", 0.1), (270, "X")], polar(R, -126), ox="II", ox_angle=20)
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "H"), (270, "X")], polar(R, 162), ox="II")
cycle_arc(s, R, 80, 34, step="oxidative\naddition", enter="ArX")
cycle_arc(s, R, 4, -36, step="alkene\ncoordination", enter="CH$_2$=CHR", leave="L")
cycle_arc(s, R, -72, -108, step="syn migratory\ninsertion")
cycle_arc(s, R, -142, -184, step="syn $\\beta$-H\nelimination", enter="L", leave="ArCH=CHR (E)", enter_at=0.75, leave_at=0.25)
cycle_arc(s, R, 148, 102, step="base-assisted\nreductive\nelimination", enter="base", leave="base·HX")
s.text((0, 0), "Heck", size=15)
s.draw()
