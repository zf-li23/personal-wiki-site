"""Catalytic cycle of the Suzuki-Miyaura coupling (L = phosphine, X = halide). Oxidative addition
of ArX to Pd(0); the base replaces the halide by hydroxide (or alkoxide); the hydroxopalladium
complex reacts with the arylboronic acid (transmetalation through a Pd-O-B bridge, boric acid
leaves); after cis arrangement of the two aryl groups, reductive elimination gives the biaryl and
Pd(0). With other organometallic partners (R'ZnX: Negishi, R'SnR3: Stille, R'MgX: Kumada) only
the transmetalation step changes."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.4
complex_at(s, "Pd", [(180, "L"), (0, "L")], polar(R, 90), ox="0")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "Ar"), (270, "X")], polar(R, 0) + np.array([-0.3, 0]), ox="II")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "Ar"), (270, "OH")], polar(R, -90), ox="II")
complex_at(s, "Pd", [(270, "L"), (0, "L"), (90, "Ar"), (180, "Ar$'$")], polar(R, 180) + np.array([0.3, 0]), ox="II", ox_angle=135)
cycle_arc(s, R, 74, 22, step="oxidative\naddition", enter="ArX")
cycle_arc(s, R, -22, -70, step="ligand\nexchange", enter="OH$^-$", leave="X$^-$")
cycle_arc(s, R, -110, -158, step="transmetalation", enter="Ar$'$B(OH)$_2$", leave="B(OH)$_3$", step_r=R - 1.5)
cycle_arc(s, R, 158, 106, step="reductive\nelimination", leave="Ar$-$Ar$'$", leave_at=0.6)
s.text((0, 0), "Suzuki$-$Miyaura", size=14)
s.draw()
