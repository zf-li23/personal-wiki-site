"""How a boronic acid warhead (as in bortezomib; R is the rest of the inhibitor) inhibits a serine
or threonine protease. The hydroxy oxygen of the active-site residue (Enz-CH2-OH) adds to the
empty p orbital of trigonal boron; after loss of a proton the boron is tetrahedral and negatively
charged, a stable mimic of the tetrahedral intermediate of amide hydrolysis. The addition is
reversible, so the inhibition is covalent but reversible."""

from wikichem import Scheme

s = Scheme()
ser = s.molecule("*CO[H]", coords=[(-2.6, 0.6), (-1.6, 0.6), (-0.9, -0.1), (-0.9, -1.1)], lone_pairs=[2], labels={0: "Enz"})
b = s.molecule("*B(O)O", coords=[(1.6, 1.1), (1.0, 0.2), (1.6, -0.6), (0.0, 0.6)], labels={0: "R"})
s.curly(ser.atom(2), b.atom(1), bend=-0.5)
s.arrow((2.6, 0), (4.0, 0), above="$-$H$^+$")
x = 6.4
s.molecule("*CO[B-](*)(O)O", coords=[(-2.2, 0.6), (-1.2, 0.6), (-0.5, -0.1), (0.5, -0.1), (0.5, 0.9), (1.5, -0.1), (0.5, -1.1)],
           at=(x, 0), labels={0: "Enz", 4: "R"})
s.text((x, -2.0), "tetrahedral boronate", size=11)
s.draw()
