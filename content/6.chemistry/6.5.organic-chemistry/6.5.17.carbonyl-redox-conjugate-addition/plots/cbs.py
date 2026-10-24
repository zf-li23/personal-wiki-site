"""CBS reduction of acetophenone with the (S)-oxazaborolidine catalyst (B-methyl, from
(S)-alpha,alpha-diphenylprolinol; the two phenyl groups on the ring carbon are written as labels).
Borane is bound to the ring nitrogen, which makes it a better hydride donor and the ring boron a
stronger Lewis acid; the ketone binds to the ring boron (dashed bond) through the oxygen lone pair
that keeps its small methyl group next to the B-methyl and its large phenyl group away from the
catalyst. A B-H bond pair is delivered to the carbonyl carbon through a six-membered ring, giving
the (R)-alcohol after workup; the catalyst is released and binds the next borane."""

from wikichem import Scheme

import math


def extent(smiles, **kw):
    """Horizontal extent of a structure as it would be drawn (laid out on a scratch scheme)."""
    c = Scheme().molecule(smiles, **kw).coords
    return c[:, 0].min(), c[:, 0].max()


def row(s, items, x=0.0, y=0.0, gap=0.7, arrow=1.5):
    """Lay out structures, plus signs and reaction arrows from left to right; returns the placed molecules and the end x."""
    placed = []
    for it in items:
        if isinstance(it, tuple) and it[0] == "arrow":
            s.arrow((x + 0.1, y), (x + 0.1 + arrow, y), above=it[1], below=it[2] if len(it) > 2 else None)
            x += arrow + 0.2
        elif it == "+":
            s.plus((x + 0.45, y))
            x += 0.9
        else:
            smi, kw = (it, {}) if isinstance(it, str) else it
            lo, hi = extent(smi, **kw)
            m = s.molecule(smi, at=(x + gap - lo, y), **kw)
            placed.append(m)
            x += gap + (hi - lo) + gap
    return placed, x


def turn(smiles, i, j, target, **kw):
    """The rotate= value that makes the bond from atom i to atom j point at the target angle (degrees)."""
    m = Scheme().molecule(smiles, **kw)
    d = m.xy(j) - m.xy(i)
    return target - math.degrees(math.atan2(d[1], d[0]))


def ring(centre, start, n=6, r=None):
    """Corner coordinates of a regular n-gon with unit edges, starting at angle start (degrees), counterclockwise."""
    r = r or 1 / (2 * math.sin(math.pi / n))
    return [(centre[0] + r * math.cos(math.radians(start + 360 * k / n)), centre[1] + r * math.sin(math.radians(start + 360 * k / n)))
            for k in range(n)]

s = Scheme()
cat = s.molecule("C[B]1OC(*)(*)[CH]2CCC[N+]12[BH2-][H]",
                 coords=[(-1.4, 0.35), (-0.5, 0.0), (-0.81, -0.95), (0.0, -1.54), (-0.55, -2.4), (0.55, -2.4), (0.81, -0.95),
                         (1.85, -1.15), (2.3, -0.25), (1.5, 0.4), (0.5, 0.0), (0.75, 1.15), (0.45, 2.05)],
                 labels={4: "Ph", 5: "Ph"})
ket = s.molecule("CC(=O)*", coords=[(-1.3, 2.55), (-0.4, 2.1), (-0.6, 1.1), (0.0, 3.0)], labels={3: "Ph"}, lone_pairs=[2])
s.partial(ket.atom(2), cat.atom(1))
s.curly(cat.bond(11, 12), ket.atom(1), bend=0.5)
s.curly(ket.bond(1, 2), ket.atom(2), bend=0.8)
row(s, [("arrow", r"then H$_3$O$^+$"), "C[C@@H](O)c1ccccc1"], x=3.2, y=0.2)
s.text((5.4, -1.6), "(R)-1-phenylethanol", size=11)
s.draw()
