"""Why 4-nitrophenol is a much stronger acid than phenol: resonance structures of the 4-nitrophenoxide
ion. The negative charge of the phenoxide oxygen is delocalized onto the ortho and para carbons
(as in phenoxide itself); from the para carbon it moves on to an oxygen of the nitro group (the
nitronate structure, negative charge on the electronegative O). A meta nitro group cannot take part
in this delocalization and acts only through its -I effect."""

exec(open("helpers.txt").read())

NO2 = "[N+:8](=[O:9])[O-:10]"
F0 = f"[O-:7][C:1]1=[CH:2][CH:3]=[C:4]({NO2})[CH:5]=[CH:6]1"
F1 = f"[O:7]=[C:1]1[CH-:2][CH:3]=[C:4]({NO2})[CH:5]=[CH:6]1"
F2 = f"[O:7]=[C:1]1[CH:2]=[CH:3][C-:4]({NO2})[CH:5]=[CH:6]1"
F3 = "[O:7]=[C:1]1[CH:2]=[CH:3][C:4](=[N+:8]([O-:9])[O-:10])[CH:5]=[CH:6]1"

probe = Scheme().molecule(F0)  # layout only: turn the C1-O bond upward
v = probe.xy(7) - probe.xy(1)
s = Scheme()
dx = 3.8
a = s.molecule(F0, at=(0, 0), rotate=90 - np.degrees(np.arctan2(v[1], v[0])), lone_pairs=[7])
s.curly(a.atom(7), a.bond(7, 1), bend=0.7)
s.curly(a.bond(1, 2), a.atom(2), bend=0.7)
b = s.molecule(F1, at=(dx, 0), like=a, lone_pairs=[2])
s.curly(b.atom(2), b.bond(2, 3), bend=0.7)
s.curly(b.bond(3, 4), b.atom(4), bend=0.7)
c = s.molecule(F2, at=(2 * dx, 0), like=a, lone_pairs=[4])
s.curly(c.atom(4), c.bond(4, 8), bend=0.7)
s.curly(c.bond(8, 9), c.atom(9), bend=0.7)
s.molecule(F3, at=(3 * dx, 0), like=a)
for i in (1, 2, 3):
    s.arrow((dx * (i - 0.5) - 0.3, 0), (dx * (i - 0.5) + 0.3, 0), kind="resonance")
s.text((3 * dx, -2.9), "charge on the nitro O", size=10)
s.draw()
