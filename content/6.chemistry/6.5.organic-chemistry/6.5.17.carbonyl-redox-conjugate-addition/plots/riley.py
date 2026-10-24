"""Riley oxidation of cyclohexanone by selenium dioxide. The enol attacks the electrophilic
selenium (the oxygen lone pair pushes, the C=C pi pair forms the C-Se bond, and an Se=O pi pair
moves onto oxygen); proton transfer gives the beta-keto seleninic acid. A [2,3]-sigmatropic shift
moves oxygen from selenium onto the alpha carbon (a selenium(II) ester), and elimination of H2O and
Se(0) forms the second C=O bond of cyclohexane-1,2-dione."""

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
EN = "OC1=CCCCC1"
en = s.molecule(EN, at=(0.0, 0.0), rotate=turn(EN, 1, 2, 0), lone_pairs=[0])
se = s.molecule("O=[Se]=O", coords=[(-0.9, 0.0), (0.0, 0.0), (0.9, 0.0)], at=(en.xy(2)[0] + 0.3, en.xy(2)[1] + 1.6), lone_pairs=[2])
s.curly(en.atom(0), en.bond(0, 1), bend=-0.6)
s.curly(en.bond(1, 2), se.atom(1), bend=-0.5)
s.curly(se.bond(1, 2), se.atom(2), bend=-0.8)
row(s, [("arrow", "proton", "transfer"), "O=C1CCCCC1[Se](=O)O", ("arrow", "[2,3]"), "O=C1CCCCC1O[Se]O",
        ("arrow", r"$-$H$_2$O, $-$Se"), "O=C1CCCCC1=O"], x=2.0, y=0.4)
s.draw()
