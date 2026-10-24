"""The S-to-N acyl shift of native chemical ligation. Thiol exchange has joined the C-terminal
thioester of peptide 1 to the side-chain thiol of the N-terminal cysteine of peptide 2. The free
amino group then adds to the thioester carbonyl through a five-membered ring, and the tetrahedral
intermediate collapses with loss of the thiolate (now the cysteine side chain), giving a native
peptide bond. The shift is irreversible because the amide is far more stable than the thioester."""

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
p = ring((0.0, 0.0), 90, n=5)  # C(acyl) at the top, then S, CH2, CH, N
te = s.molecule("*C(=O)SCC(N)C(=O)*",
                coords=[(-0.9, 1.6), p[0], (0.55, 2.0), p[1], p[2], p[3], p[4], (1.9, -0.75), (2.4, 0.1), (2.4, -1.6)],
                labels={0: "Pep$_1$", 9: "Pep$_2$"}, lone_pairs=[2, 6])
s.curly(te.atom(6), te.atom(1), bend=0.4)
s.curly(te.bond(1, 2), te.atom(2), bend=0.8)
row(s, [("arrow", None, r"via tetrahedral" + "\n" + "intermediate")], x=3.2, y=0.2)
s.molecule("*C(=O)NC(CS)C(=O)*", at=(7.6, 0.2), labels={0: "Pep$_1$", 9: "Pep$_2$"})
s.draw()
