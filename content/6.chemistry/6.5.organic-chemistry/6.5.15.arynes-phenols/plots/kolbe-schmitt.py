"""Kolbe-Schmitt carboxylation of sodium phenoxide. The ortho carbon of the phenoxide attacks the
carbon of CO2 (the oxygen lone pair pushes into the ring; Na+ holds the phenoxide oxygen and CO2
together, favouring ortho attack); a proton shift restores the aromatic ring and gives salicylate
(salicylic acid after acidification)."""

exec(open("helpers.txt").read())

s = Scheme()
ph = s.molecule("[O-:1][C:2]1=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(0, 0), lone_pairs=[1], rotate=60)
out = ph.xy(3) - ring_centre(ph, [2, 3, 4, 5, 6, 7])
co2 = s.molecule("[O:9]=[C:8]=O", at=ph.xy(3) + 2.0 * out / np.linalg.norm(out) + (0, 0.4), rotate=90)
s.text(ph.xy(1) + (-0.9, -0.6), r"Na$^+$", size=11)
s.curly(ph.atom(1), ph.bond(1, 2), bend=-0.9)
s.curly(ph.bond(2, 3), co2.atom(8), bend=-0.4)
s.curly(co2.bond(8, 9), co2.atom(9), bend=0.7)
s.arrow((2.8, 0), (4.0, 0))
s.molecule("O=[C:2]1[CH:3](C(=O)[O-])[CH:4]=[CH:5][CH:6]=[CH:7]1", at=(6.0, 0))
s.arrow((8.2, 0), (9.6, 0), above="H shift")
s.molecule("[O-]C(=O)c1ccccc1O", at=(12.0, 0))
s.text((12.0, -2.4), "salicylate", size=10)
s.draw()
