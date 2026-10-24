"""Catalytic cycle of the Buchwald-Hartwig amination with a bulky monophosphine L (for example a
dialkylbiarylphosphine). Monoligated Pd(0)L adds the aryl halide; the amine binds to the
three-coordinate arylpalladium halide; the strong base (NaOtBu) removes the N-H proton and the
halide, giving an amido complex; C-N reductive elimination releases the arylamine. A competing
beta-hydride elimination from the amido complex (when the amine has alpha C-H bonds) gives the
reduced arene and an imine."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.4
complex_at(s, "Pd", [(180, "L")], polar(R, 90) + np.array([0.3, 0]), ox="0")
complex_at(s, "Pd", [(180, "L"), (90, "Ar"), (270, "X")], polar(R, 0) + np.array([-0.3, 0]), ox="II")
complex_at(s, "Pd", [(180, "L"), (90, "Ar"), (270, "X"), (0, "HNR$_2$")], polar(R, -90) + np.array([-0.4, 0]), ox="II")
complex_at(s, "Pd", [(270, "L"), (90, "Ar"), (180, "NR$_2$")], polar(R, 180) + np.array([0.5, 0]), ox="II", ox_angle=20)
cycle_arc(s, R, 76, 22, step="oxidative\naddition", enter="ArX")
cycle_arc(s, R, -22, -66, step="amine\ncoordination", enter="HNR$_2$")
cycle_arc(s, R, -114, -158, step="deprotonation", enter="NaO$t$Bu", leave="NaX + $t$BuOH", step_r=R - 1.5)
cycle_arc(s, R, 158, 104, step="C$-$N reductive\nelimination", leave="Ar$-$NR$_2$", leave_at=0.6)
s.text((0, 0), "Buchwald$-$Hartwig", size=14)
s.draw()
