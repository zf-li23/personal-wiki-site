"""Benzyne as a dienophile: Diels-Alder reaction with furan. The low-lying in-plane pi bond of benzyne
and the diene of furan react in one concerted [4+2] step (three curved arrows around the cyclic
transition state), giving 1,4-epoxy-1,4-dihydronaphthalene (oxabenzonorbornadiene)."""

exec(open("helpers.txt").read())

BZ = "[C:1]1#[C:2][CH:3]=[CH:4][CH:5]=[CH:6]1"
FU = "[O:7]1[CH:8]=[CH:9][CH:10]=[CH:11]1"


def facing(smiles, ks, ring, angle):
    """Rotation that makes the midpoint of atoms ks point in direction ``angle`` from the ring centre."""
    m = Scheme().molecule(smiles)  # layout only
    v = np.mean([m.xy(k) for k in ks], axis=0) - ring_centre(m, ring)
    return angle - np.degrees(np.arctan2(v[1], v[0]))


s = Scheme()
bz = s.molecule(BZ, at=(0, 0), rotate=facing(BZ, [1, 2], [1, 2, 3, 4, 5, 6], 0))
fu = s.molecule(FU, at=(3.3, 0), rotate=facing(FU, [7], [7, 8, 9, 10, 11], 180))
top_b = 1 if bz.xy(1)[1] > bz.xy(2)[1] else 2
top_f = 8 if fu.xy(8)[1] > fu.xy(11)[1] else 11
bot_b, bot_f = 3 - top_b, 19 - top_f
s.curly(bz.bond(1, 2), fu.atom(top_f), bend=0.6)
s.curly(fu.bond(top_f, top_f + (1 if top_f == 8 else -1)), fu.bond(9, 10), bend=-0.6)
s.curly(fu.bond(bot_f, bot_f + (1 if bot_f == 8 else -1)), bz.atom(bot_b), bend=0.6)
s.arrow((4.6, 0), (5.8, 0))
s.molecule("C1=CC2OC1c1ccccc12", at=(7.6, 0))
s.text((7.6, -1.8), "1,4-epoxy-1,4-dihydronaphthalene", size=10)
s.draw()
