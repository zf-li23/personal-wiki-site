"""Luche reduction of cyclohex-2-en-1-one. In methanol, Ce3+ catalyses the formation of
methoxyborohydrides such as HB(OMe)3-, harder hydride donors than BH4-; methanol bound to the hard
Lewis acid Ce3+ is more acidic and hydrogen-bonds to the carbonyl oxygen (dashed). The hydride goes
to the carbonyl carbon (the hard site with the larger charge) rather than the beta carbon, and the
oxygen takes the proton from the activated methanol, giving the allylic alcohol."""

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
EN = "O=C1C=CCCC1"
en = s.molecule(EN, at=(0.0, 0.0), rotate=turn(EN, 1, 0, 90), lone_pairs=[0])
o, c = en.xy(0), en.xy(1)
bh = s.molecule("[H][B-](*)(*)*", coords=[(0.0, 0.0), (-1.0, 0.0), (-1.5, 0.87), (-1.5, -0.87), (-2.0, 0.0)],
                labels={2: "MeO", 3: "MeO", 4: "MeO"}, at=(c[0] - 1.1, c[1] + 0.5))
me = s.molecule("[H]OC", coords=[(0.0, 0.0), (0.85, 0.5), (1.85, 0.4)], at=(o[0] + 0.9, o[1] + 0.3), lone_pairs=[1])
ce = me.xy(1) + (0.1, 1.15)
s.text(ce, r"Ce$^{3+}$")
s.partial(me.atom(1), ce - (0.0, 0.35))
s.partial(en.atom(0), me.atom(0))
s.curly(bh.bond(0, 1), en.atom(1), bend=0.6)
s.curly(en.bond(0, 1), en.atom(0), bend=-0.9)
s.curly(me.bond(0, 1), me.atom(1), bend=0.9)
row(s, [("arrow", None), "OC1C=CCCC1"], x=3.8, y=-0.3)
s.draw()
