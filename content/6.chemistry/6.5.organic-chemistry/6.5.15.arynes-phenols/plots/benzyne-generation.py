"""Two neutral ways to make benzyne. (1) Kobayashi precursor: fluoride attacks the silicon of
2-(trimethylsilyl)phenyl triflate; the C-Si bond electrons form the in-plane bond of benzyne as the
triflate leaves (fluoride induced 1,2-elimination at room temperature). (2) Benzenediazonium-2-
carboxylate (from anthranilic acid and nitrous acid) fragments on warming: the carboxylate becomes
CO2, the C-C bond electrons form the in-plane bond, and N2 leaves."""

exec(open("helpers.txt").read())

s = Scheme()
k = s.molecule("[Si:7][C:1]1=[C:2]([O:8])[CH:3]=[CH:4][CH:5]=[CH:6]1", at=(0, 0),
               labels={7: r"SiMe$_3$", 8: "OTf"}, rotate=90)
f = s.molecule("[F-]", at=k.xy(7) + (0.9, -1.5), lone_pairs=True)
s.curly(f.atom(0), k.atom(7), bend=-0.4)
s.curly(k.bond(1, 7), k.bond(1, 2), bend=-0.9)
s.curly(k.bond(2, 8), k.atom(8), bend=-0.9)
s.arrow((3.0, 0), (4.2, 0), above="CsF, MeCN", below="r.t.")
s.molecule("C1#CC=CC=C1", at=(6.0, 0))
s.text((8.7, 0), r"+ Me$_3$SiF + TfO$^-$", size=11)
s.draw()

s = Scheme()
d = s.molecule("[O-:9][C:7](=O)[C:1]1=[C:2]([N+:8]#N)[CH:3]=[CH:4][CH:5]=[CH:6]1", at=(0, 0), lone_pairs=[9], rotate=90)
s.curly(d.atom(9), d.bond(9, 7), bend=0.8)
s.curly(d.bond(1, 7), d.bond(1, 2), bend=0.7)
s.curly(d.bond(2, 8), d.atom(8), bend=-0.7)
s.arrow((2.6, 0), (3.8, 0), above="heat")
s.molecule("C1#CC=CC=C1", at=(5.2, 0))
s.text((7.6, 0), r"+ CO$_2$ + N$_2$", size=11)
s.text((0, -2.6), "benzenediazonium-2-carboxylate", size=10)
s.draw()
