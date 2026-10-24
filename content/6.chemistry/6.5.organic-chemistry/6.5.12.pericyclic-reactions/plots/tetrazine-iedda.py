"""Inverse-electron-demand Diels-Alder reaction of a 1,2,4,5-tetrazine with an alkene (here
ethylene stands for a strained trans-cyclooctene or norbornene). Step 1: [4+2] cycloaddition across
C3 and C6 of the electron-poor tetrazine. Step 2: the bicyclic adduct loses N2 in a retro-[4+2]
reaction, which makes the ligation irreversible; the 4,5-dihydropyridazine then tautomerizes or is
oxidized to the pyridazine."""

exec(open("fixedmol.txt").read())

h = ring(6, start=90)  # h[0] top, h[1] upper left, h[2] lower left, h[3] bottom, h[4] lower right, h[5] upper right
s = Scheme()
# tetrazine: C3 at top, N2 upper left, N1 lower left, C6 bottom, N5 lower right, N4 upper right; drawn as the "diene" on the left
tz = fixed(s, "CC1=NN=C(C)N=N1", [(0.0, 1.9), h[0], h[1], h[2], h[3], (0.0, -1.9), (0.87 + 0.0, -0.5), (0.87, 0.5)])
alk = fixed(s, "C=C", [(1.9, -0.5), (1.9, 0.5)])
s.partial(tz.xy(1), alk.xy(1))
s.partial(tz.xy(4), alk.xy(0))
s.curly(tz.bond(1, 2), tz.bond(2, 3), bend=0.5)
s.curly(tz.bond(3, 4), (tz.xy(4) + alk.xy(0)) / 2, bend=0.5)
s.curly(alk.bond(0, 1), (alk.xy(1) + tz.xy(1)) / 2, bend=0.5)
s.text((0.6, -2.7), "tetrazine + alkene")
s.arrow((2.8, 0), (4.0, 0), above="[4+2]")
# bicyclic adduct (N=N bridge) and its retro-[4+2] loss of N2
add = fixed(s, "CC12CCC(C)(N=N1)N=N2", [(0.0, 1.9), h[0], h[5], h[4], h[3], (0.0, -1.9), (-0.25, -0.45), (-0.25, 0.45), h[2], h[1]], at=(5.6, 0))
s.curly(add.bond(1, 7), add.bond(6, 7), bend=0.6)
s.curly(add.bond(4, 6), add.bond(4, 8), bend=-0.6)
s.curly(add.bond(8, 9), add.bond(1, 9), bend=-0.6)
s.text((5.6, -2.7), "bicyclic adduct")
s.arrow((7.0, 0), (8.4, 0), above=r"$-$N$_2$", below="retro-[4+2]")
s.molecule("CC1=NN=C(C)CC1", at=(9.9, 0))
s.text((9.9, -2.7), "4,5-dihydropyridazine")
s.draw()
