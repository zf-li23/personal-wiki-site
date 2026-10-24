"""Nucleophilic catalysis of acylation by 4-(dimethylamino)pyridine (DMAP). The ring nitrogen of
DMAP, more nucleophilic than the alcohol, attacks acetic anhydride (addition-elimination, shown as
one step) and gives an N-acetylpyridinium ion, whose positive charge is spread onto the
dimethylamino group. This ion is a far stronger acylating agent than the anhydride: the alcohol
adds to it and the neutral DMAP leaves, so DMAP is regenerated after deprotonation."""

from wikichem import Scheme

s = Scheme()
y1, y2 = 0.0, -5.0  # the two rows
dmap = s.molecule("CN(C)c1ccncc1", at=(0, y1), rotate=-90, lone_pairs=[6])
anh = s.molecule("CC(=O)OC(C)=O", at=(4.4, y1 + 0.6), lone_pairs=[2])
s.curly(dmap.atom(6), anh.atom(1), bend=0.4)
s.curly(anh.bond(1, 3), anh.atom(3), bend=0.8)
s.text((0, y1 - 1.9), "DMAP")
s.arrow((6.4, y1), (7.8, y1), above="add.-elim.")
s.molecule("CC(=O)[n+]1ccc(N(C)C)cc1", at=(10.6, y1), rotate=-30)
s.plus((13.6, y1))
s.molecule("CC(=O)[O-]", at=(14.6, y1))
s.text((10.6, y1 - 1.9), "N-acetylpyridinium ion")

roh = s.molecule("CCO", at=(-1.2, y2 - 1.2), lone_pairs=[2])
acyl = s.molecule("CC(=O)[n+]1ccc(N(C)C)cc1", at=(2.4, y2), rotate=-30, lone_pairs=[2])
s.curly(roh.atom(2), acyl.atom(1), bend=0.4)
s.curly(acyl.bond(1, 2), acyl.atom(2), bend=-0.8)
s.arrow((5.6, y2), (7.0, y2), above="add.-elim.", below=r"$-\mathrm{H}^+$")
s.molecule("CCOC(C)=O", at=(8.9, y2))
s.plus((10.4, y2))
s.molecule("CN(C)c1ccncc1", at=(12.6, y2), rotate=-90)
s.text((8.9, y2 - 1.7), "ethyl acetate")
s.text((12.6, y2 - 1.7), "DMAP (regenerated)")
s.draw()
