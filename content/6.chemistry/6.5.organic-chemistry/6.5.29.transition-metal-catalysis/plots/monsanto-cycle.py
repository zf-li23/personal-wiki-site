"""Catalytic cycle of the Monsanto acetic acid process. The 16-electron anion [RhI2(CO)2]- adds
methyl iodide by SN2-type oxidative addition (the turnover-limiting step, Rh(I) to Rh(III)); the
methyl migrates to an adjacent CO (migratory insertion), giving an acyl complex with a vacant site
that is filled by CO; reductive elimination of acetyl iodide returns Rh(I). Outside the cycle HI
converts methanol into methyl iodide and water hydrolyses acetyl iodide to acetic acid,
regenerating HI."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.6
complex_at(s, "Rh", [(180, "I"), (0, "CO"), (90, "I"), (270, "CO")], polar(R, 90), ox="I")
s.text(polar(R, 90) + np.array([1.6, 1.0]), "$-$", size=13)
complex_at(s, "Rh", [(180, "I"), (0, "CO"), (90, "CH$_3$"), (270, "CO"), (215, "I", 0.1), (35, "I", 0.1)], polar(R, 0) + np.array([-0.4, 0]),
           ox="III", ox_angle=140)
s.text(polar(R, 0) + np.array([1.2, 1.3]), "$-$", size=13)
complex_at(s, "Rh", [(180, "I"), (0, "COCH$_3$"), (90, "I"), (270, "CO"), (215, "I", 0.1)], polar(R, -90) + np.array([0.2, 0]),
           ox="III", ox_angle=140)
s.text(polar(R, -90) + np.array([2.2, 1.0]), "$-$", size=13)
complex_at(s, "Rh", [(180, "I"), (0, "COCH$_3$"), (90, "I"), (270, "CO"), (215, "I", 0.1), (35, "CO", 0.1)], polar(R, 180) + np.array([0.6, 0]),
           ox="III", ox_angle=140)
s.text(polar(R, 180) + np.array([2.4, 1.4]), "$-$", size=13)
cycle_arc(s, R, 74, 24, step="oxidative addition\n(rate-limiting)", enter="CH$_3$I", step_r=R - 1.6)
cycle_arc(s, R, -22, -66, step="migratory\ninsertion")
cycle_arc(s, R, -114, -156, step="CO\ncoordination", enter="CO")
cycle_arc(s, R, 160, 108, step="reductive\nelimination", leave="CH$_3$COI", leave_at=0.6)
s.text((0, 0), "Monsanto\n\nCH$_3$OH + HI $\\to$ CH$_3$I + H$_2$O\nCH$_3$COI + H$_2$O $\\to$ CH$_3$COOH + HI", size=11)
s.draw()
