"""Bromination of phenol in water needs no Lewis acid. The oxygen lone pair pushes electrons through the
ring (like an enol), and the para carbon attacks Br2, breaking the Br-Br bond heterolytically; the
intermediate is a protonated cyclohexadienone (an oxonium ion with every atom having an octet). Loss of
the proton from C4 restores the ring. In water the reaction does not stop: the ortho positions react
in the same way, and 2,4,6-tribromophenol precipitates."""

exec(open("helpers.txt").read())

PH = "[OH:7][C:1]1=[CH:2][CH:3]=[CH:4][CH:5]=[CH:6]1"


def up(smiles, **kw):
    """Rotation that turns the C1-O7 bond of the molecule upward."""
    m = Scheme().molecule(smiles, **kw)  # layout only
    v = m.xy(7) - m.xy(1)
    return 90 - np.degrees(np.arctan2(v[1], v[0]))


s = Scheme()
p = s.molecule(PH, at=(0, 0), rotate=up(PH), lone_pairs=[7])
br2 = s.molecule("[Br:8][Br:9]", at=p.xy(4) + (0.5, -1.6))
s.curly(p.atom(7), p.bond(7, 1), bend=0.7)
s.curly(p.bond(1, 2), p.bond(2, 3), bend=0.7)
s.curly(p.bond(3, 4), br2.atom(8), bend=0.5)
s.curly(br2.bond(8, 9), br2.atom(9), bend=-0.8)
s.arrow((2.0, 0), (3.2, 0), below=r"$-$Br$^-$")
OX = "[OH+:7]=[C:1]1[CH:2]=[CH:3][CH:4]([Br:8])[CH:5]=[CH:6]1"
ox = s.molecule(OX, at=(5.0, 0), rotate=up(OX, show_h=[4]), show_h=[4])
s.text((5.0, -2.9), "protonated dienone", size=10)
s.arrow((6.8, 0), (8.0, 0), above=r"$-$H$^+$")
s.molecule("[OH:7][c:1]1ccc(Br)cc1", at=(9.6, 0), rotate=up("[OH:7][c:1]1ccc(Br)cc1"))
s.arrow((11.2, 0), (12.4, 0), above=r"2 Br$_2$", below=r"H$_2$O")
s.molecule("[OH:7][c:1]1c(Br)cc(Br)cc1Br", at=(14.2, 0), rotate=up("[OH:7][c:1]1c(Br)cc(Br)cc1Br"))
s.text((14.2, -2.9), "2,4,6-tribromophenol", size=10)
s.draw()
