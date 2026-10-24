"""Simplified catalytic cycle of alkene hydrogenation with Wilkinson's catalyst (L = PPh3).
The precatalyst RhCl(PPh3)3 loses one phosphine; the 14-electron RhClL2 adds H2 (oxidative
addition, Rh(I) to Rh(III)); the alkene binds; migratory insertion of the alkene into Rh-H gives an
alkyl hydride (the turnover-limiting step); C-H reductive elimination releases the alkane and
returns Rh(I). Both hydrogens are delivered to the same face of the alkene (syn addition)."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.4
complex_at(s, "Rh", [(180, "Cl"), (90, "L"), (270, "L")], polar(R, 90) + np.array([0, -0.2]), ox="I", ox_angle=20)
complex_at(s, "Rh", [(180, "Cl"), (90, "L"), (270, "L"), (0, "H"), (35, "H", 0.15)], polar(R, 5), ox="III", ox_angle=140)
pi = complex_at(s, "Rh", [(180, "Cl"), (90, "L"), (270, "L"), (0, "H"), (35, "H", 0.15)], polar(R, -90) + np.array([0.6, 0]),
                ox="III", ox_angle=140)
alkene(s, pi, 215, subst="R", dist=1.35)
complex_at(s, "Rh", [(180, "Cl"), (90, "L"), (270, "L"), (0, "H"), (35, "CH$_2$CH$_2$R", 0.15)], polar(R, 180) + np.array([0.3, 0]),
           ox="III", ox_angle=140)
s.text(polar(R, 90) + np.array([0, 2.3]), "RhClL$_3$  $\\rightleftharpoons$  RhClL$_2$ + L", size=13)
cycle_arc(s, R, 72, 24, step="oxidative\naddition", enter="H$_2$")
cycle_arc(s, R, -18, -64, step="alkene\ncoordination", enter="RCH=CH$_2$")
cycle_arc(s, R, -114, -158, step="migratory insertion\n(rate-limiting)", step_r=R - 1.6)
cycle_arc(s, R, 160, 110, step="reductive\nelimination", leave="RCH$_2$CH$_3$", leave_at=0.6)
s.text((0, 0), "Wilkinson\nhydrogenation", size=14)
s.draw()
