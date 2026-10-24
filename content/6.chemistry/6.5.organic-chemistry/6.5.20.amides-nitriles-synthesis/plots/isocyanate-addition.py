"""Addition of an alcohol to an isocyanate (methyl isocyanate and methanol). The alcohol oxygen attacks
the central, strongly electrophilic carbon of N=C=O and the C=N pi pair moves onto nitrogen; proton
transfer from oxygen to nitrogen gives the carbamate (urethane). With an amine instead of the alcohol,
the same addition gives a substituted urea (bottom); diisocyanates and diols polymerize this way to
polyurethanes."""

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
me = s.molecule("CO", coords=[(-0.3, 2.3), (0.1, 1.4)], lone_pairs=[1])
ic = s.molecule("CN=C=O", coords=[(-1.8, 0.0), (-0.9, 0.0), (0.0, 0.0), (0.9, 0.0)], show_carbons=[2], lone_pairs=[1])
s.curly(me.atom(1), ic.atom(2), bend=-0.4)
s.curly(ic.bond(1, 2), ic.atom(1), bend=0.8)
row(s, [("arrow", None), "C[N-]C(=O)[OH+]C", ("arrow", "proton", "transfer"), "CNC(=O)OC"], x=1.6, y=0.0)
row(s, [("CN=C=O", {"show_carbons": [2]}), "+", "CN", ("arrow", None), "CNC(=O)NC"], x=-2.6, y=-2.4)
s.draw()
