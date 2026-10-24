"""Catalytic cycle of rhodium-catalysed hydroformylation (Heck-Breslow mechanism, L = PPh3). The
16-electron HRh(CO)L2 binds the alkene, which inserts into Rh-H with rhodium going to the terminal
carbon (anti-Markovnikov; bulky phosphines favour this and so the linear aldehyde); CO binds and
the alkyl migrates to CO (migratory insertion), giving an acyl complex; H2 adds (oxidative
addition, Rh(I) to Rh(III)) and reductive elimination releases the aldehyde RCH2CH2CHO."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.6
complex_at(s, "Rh", [(180, "L"), (0, "L"), (90, "H"), (270, "CO")], polar(R, 90), ox="I")
complex_at(s, "Rh", [(180, "L"), (0, "L"), (90, "CH$_2$CH$_2$R", 0.1), (270, "CO")], polar(R, 0) + np.array([-0.4, 0]), ox="I", ox_angle=140)
complex_at(s, "Rh", [(180, "L"), (0, "L"), (90, "COCH$_2$CH$_2$R", 0.1), (270, "CO")], polar(R, -90), ox="I")
complex_at(s, "Rh", [(180, "L"), (0, "L"), (90, "COCH$_2$CH$_2$R", 0.1), (270, "CO"), (215, "H", 0.1), (35, "H", 0.1)],
           polar(R, 180) + np.array([0.6, 0]), ox="III", ox_angle=140)
cycle_arc(s, R, 74, 24, step="alkene binding,\n1,2-insertion", enter="RCH=CH$_2$", step_r=R - 1.6)
cycle_arc(s, R, -22, -66, step="CO binding,\nCO insertion", enter="CO", step_r=R - 1.6)
cycle_arc(s, R, -114, -156, step="oxidative\naddition", enter="H$_2$")
cycle_arc(s, R, 160, 108, step="reductive\nelimination", leave="RCH$_2$CH$_2$CHO", leave_at=0.6)
s.text((0, 0), "hydroformylation", size=14)
s.draw()
