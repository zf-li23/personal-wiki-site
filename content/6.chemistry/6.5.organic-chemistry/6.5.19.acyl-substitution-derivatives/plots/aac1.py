"""AAc1 hydrolysis of methyl 2,4,6-trimethylbenzoate in concentrated sulfuric acid. The two ortho
methyl groups block attack on the carbonyl carbon from above and below the ring plane, so the AAc2
path is closed. Protonated on the alkoxy oxygen, the ester loses methanol: the carbonyl oxygen lone
pair pushes and the C-O bond pair leaves with methanol, giving a linear acylium ion. Water adds to
the acylium carbon along its axis, where the ortho methyls do not interfere."""

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
ar = ring((0.0, 0.0), 90)  # ipso at the top, then counterclockwise
MES = [ar[0], ar[1], (-1.73, 1.0), ar[2], ar[3], (0.0, -2.0), ar[4], ar[5], (1.73, 1.0)]
est = s.molecule("O=C([OH+]C)c1c(C)cc(C)cc1C", coords=[(-0.87, 2.5), (0.0, 2.0), (0.87, 2.5), (1.74, 2.0)] + MES, lone_pairs=[0])
s.curly(est.atom(0), est.bond(0, 1), bend=0.8)
s.curly(est.bond(1, 2), est.atom(2), bend=-0.6)
_, x = row(s, [("arrow", r"$-$MeOH")], x=2.4, y=0.6)
acy = s.molecule("[O+]#Cc1c(C)cc(C)cc1C", coords=[(0.0, 3.0), (0.0, 2.0)] + MES, at=(x + 1.7, 0.0))
w = s.molecule("O", at=(x + 1.7, 4.2), lone_pairs=True)
s.curly(w.atom(0), acy.atom(1), bend=0.5)
s.curly(acy.bond(0, 1), acy.atom(0), bend=-0.9)
row(s, [("arrow", r"$-$H$^+$")], x=x + 3.6, y=0.6)
s.molecule("OC(=O)c1c(C)cc(C)cc1C", coords=[(-0.87, 2.5), (0.0, 2.0), (0.87, 2.5)] + MES, at=(x + 7.2, 0.0))
s.draw()
