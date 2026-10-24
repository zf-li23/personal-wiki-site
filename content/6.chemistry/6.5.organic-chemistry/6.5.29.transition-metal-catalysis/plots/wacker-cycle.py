"""Catalytic cycle of the Wacker oxidation of ethylene to acetaldehyde. [PdCl4]2- exchanges a
chloride for ethylene; water attacks the coordinated alkene (anti hydroxypalladation from outside
the coordination sphere at high chloride concentration) and a proton is lost; the
2-hydroxyethyl-palladium undergoes beta-hydride elimination, reinsertion of the enol with the
opposite regiochemistry and a second beta-hydride elimination, releasing acetaldehyde, H+ and
Cl- and leaving Pd(0). CuCl2 reoxidizes Pd(0) to Pd(II); the CuCl formed is reoxidized by O2.
Net: CH2=CH2 + 1/2 O2 -> CH3CHO."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.4
complex_at(s, "Pd", [(180, "Cl"), (0, "Cl"), (90, "Cl"), (270, "Cl")], polar(R, 90) + np.array([0, -0.1]), ox="II")
s.text(polar(R, 90) + np.array([1.4, 0.9]), "2$-$", size=12)
pi = complex_at(s, "Pd", [(180, "Cl"), (90, "Cl"), (270, "Cl")], polar(R, 0) + np.array([-0.9, 0]), ox="II", ox_angle=135)
alkene(s, pi, 0)
s.text(polar(R, 0) + np.array([0.6, 1.3]), "$-$", size=12)
complex_at(s, "Pd", [(180, "Cl"), (90, "Cl"), (270, "OH$_2$"), (0, "CH$_2$CH$_2$OH")], polar(R, -90) + np.array([-0.2, 0]), ox="II")
s.text(polar(R, -90) + np.array([1.0, 1.2]), "$-$", size=12)
s.text(polar(R, 180) + np.array([0.6, 0]), "Pd(0)", size=15)
cycle_arc(s, R, 74, 24, step="ligand\nexchange", enter="C$_2$H$_4$", leave="Cl$^-$")
cycle_arc(s, R, -24, -62, step="anti hydroxy-\npalladation", enter="H$_2$O", leave="H$^+$", enter_at=0.2, leave_at=0.55)
cycle_arc(s, R, -114, -164, step="$\\beta$-H elimination,\nreinsertion,\n$\\beta$-H elimination", leave="CH$_3$CHO, H$^+$, Cl$^-$",
          step_r=R - 1.8, leave_at=0.5)
cycle_arc(s, R, 164, 106, step="reoxidation", enter="2 CuCl$_2$", leave="2 CuCl", enter_at=0.25, leave_at=0.75)
s.text((0, -0.2), "Wacker\n\n2 CuCl + $\\frac{1}{2}$O$_2$ + 2 HCl\n$\\to$ 2 CuCl$_2$ + H$_2$O", size=12)
s.draw()
