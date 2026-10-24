"""1,3-Dipolar cycloaddition of an organic azide with an alkyne (Huisgen): the 4 pi electrons of the
azide (an allyl-anion-like three-atom unit) and the 2 pi electrons of the alkyne shift round a
five-membered ring in one step, giving a 1,2,3-triazole. Heated without a catalyst it gives a mixture
of the 1,4- and 1,5-isomers; copper(I) catalysis gives only the 1,4-isomer (a stepwise mechanism)."""

exec(open("fixedmol.txt").read())

p = ring(5, start=180)  # p[0] left, then counter-clockwise: lower left, lower right, upper right, upper left
s = Scheme()
azide = fixed(s, "CN=[N+]=[N-]", [(p[1][0] - 0.8, p[1][1] - 0.6), p[1], p[0], p[4]], lone_pairs=(1, 3))
alkyne = fixed(s, "CC#C", [(p[2][0] + 0.85, p[2][1] - 0.65), p[2], p[3]], at=(0.35, 0))
s.partial(azide.xy(1), alkyne.xy(1))
s.partial(azide.xy(3), alkyne.xy(2))
s.curly(azide.atom(3), (azide.xy(3) + alkyne.xy(2)) / 2, bend=-0.4)
s.curly(alkyne.bond(1, 2), (alkyne.xy(1) + azide.xy(1)) / 2, bend=-0.5)
s.curly(azide.bond(1, 2), azide.atom(2), bend=-0.6)
s.text((0.2, -1.9), "azide + alkyne")
s.arrow((2.0, 0), (3.4, 0), above=r"$\Delta$")
s.molecule("Cn1nncc1C", at=(5.0, 0))
s.text((5.0, -1.9), "1,5-isomer")
s.text((6.6, 0), "+")
s.molecule("Cn1cc(C)nn1", at=(8.2, 0))
s.text((8.2, -1.9), "1,4-isomer")
s.draw()
