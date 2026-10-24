"""Catalytic cycles of the Sonogashira coupling (L = PPh3). Left, the palladium cycle: oxidative
addition of the aryl or vinyl halide, transmetalation of the alkynyl group from copper, and
reductive elimination of the arylalkyne. Right, the copper cycle: Cu(I) binds the terminal alkyne,
which makes the C-H proton acidic enough for the amine base to remove it, giving a copper
acetylide that hands the alkynyl group to palladium."""

exec(open("cycle.txt").read())

s = Scheme()
R = 4.8
P = (0.0, 0.0)
complex_at(s, "Pd", [(180, "L"), (0, "L")], polar(R, 90, P), ox="0")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "Ar"), (270, "X")], polar(R, -30, P), ox="II")
complex_at(s, "Pd", [(180, "L"), (0, "L"), (90, "Ar"), (270, "C$\\equiv$CR")], polar(R, -150, P), ox="II")
cycle_arc(s, R, 74, -6, step="oxidative\naddition", enter="ArX", centre=P)
cycle_arc(s, R, -58, -122, step="transmetalation", centre=P, step_r=R - 1.4)
cycle_arc(s, R, -174, -254, step="reductive\nelimination", leave="Ar$-$C$\\equiv$CR", centre=P, leave_at=0.6)
s.text(P, "Pd cycle", size=14)

C = (12.0, -2.6)
r = 3.2
s.text(polar(r, 0, C) + np.array([0.6, 0]), "CuX", size=14)
s.text(polar(r, 180, C) + np.array([-0.2, 0]), "Cu$-$C$\\equiv$CR", size=14)
cycle_arc(s, r, 20, 160, step="deprotonation", enter="HC$\\equiv$CR, R$_3$N", leave="R$_3$NH$^+$X$^-$", centre=C,
          step_r=r - 1.1, species_r=r + 1.4)
s.text(C, "Cu cycle", size=14)
# the copper acetylide goes to palladium, CuX comes back: the lower arc of the copper cycle
cycle_arc(s, r, 200, 340, step="alkynyl to Pd,\nCuX returns", centre=C, step_r=r - 1.1)
s.arrow(polar(r, 205, C) + np.array([-0.6, -0.4]), polar(R, -70, P) + np.array([1.0, -0.6]))
s.draw()
