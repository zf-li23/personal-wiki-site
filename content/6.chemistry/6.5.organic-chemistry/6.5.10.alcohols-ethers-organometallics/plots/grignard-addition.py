"""Grignard reagents as carbon nucleophiles. The polar C-Mg bond (carbon partly negative) supplies the
electron pair. Top: methylmagnesium bromide adds to the carbonyl carbon of acetone; the pi electrons
move onto oxygen, giving a magnesium alkoxide that aqueous acid protonates to 2-methylpropan-2-ol.
Bottom: with carbon dioxide the same addition gives a carboxylate, and acid work-up gives a
carboxylic acid with one more carbon atom."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

from wikichem import Scheme

s = Scheme(scale=0.46)
CLEAR = 0.32  # hand-drawn bonds stop short of a text label
EXTRA = []  # hand-drawn wedges, hashes and dots, added to the axes after s.draw()


def reach(*points):
    """Make sure the figure bounds include these points (an empty text marks them)."""
    for p in points:
        s.text(p, "")


def bond(a, b, kind="plain", clear_a=False, clear_b=True, dashed=False, order=1):
    """A bond drawn by hand from a to b; kind: plain, wedge or hash (narrow end at a)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    if clear_a:
        a = a + CLEAR * u
    if clear_b:
        b = b - CLEAR * u
    n = np.array([-u[1], u[0]])
    reach(a, b)
    if dashed:
        s.partial(a, b)
        return

    def draw(ax, ink):
        if kind == "wedge":
            ax.add_patch(Polygon([a, b + 0.1 * n, b - 0.1 * n], closed=True, color=ink, lw=0))
        elif kind == "hash":
            for t in np.linspace(0.15, 1, 7):
                p = a + t * (b - a)
                w = 0.1 * t
                ax.plot([p[0] - w * n[0], p[0] + w * n[0]], [p[1] - w * n[1], p[1] + w * n[1]], color=ink, lw=1.1)
        else:
            for o in ([0.0] if order == 1 else [-0.08, 0.08]):
                p, q = a + o * n, b + o * n
                ax.plot([p[0], q[0]], [p[1], q[1]], color=ink, lw=1.4, solid_capstyle="round")

    EXTRA.append(draw)


def label(at, text, size=None):
    s.text(at, text, size=size)


def centre(c, groups):
    """Draw a stereocentre at c; groups: (offset, text, kind)."""
    c = np.asarray(c, float)
    for off, text, kind in groups:
        p = c + np.asarray(off, float)
        bond(c, p, kind, clear_b=text is not None)
        if text is not None:
            label(p, text)


def pt(x, y):
    return np.array([x, y], float)


def dots(c, d):
    """A lone pair drawn beside a text label: centre c, unit direction d."""
    c, d = np.asarray(c, float), np.asarray(d, float)
    t = np.array([-d[1], d[0]])
    reach(c)

    def draw(ax, ink):
        for k in (-1, 1):
            p = c + 0.06 * k * t
            ax.plot(*p, marker="o", ms=1.8, color=ink)

    EXTRA.append(draw)


def lobe(c, w=1.1, h=0.55):
    """An unshaded orbital lobe (ellipse) centred at c."""
    c = np.asarray(c, float)
    reach(c - pt(w / 2, h / 2), c + pt(w / 2, h / 2))
    EXTRA.append(lambda ax, ink: ax.add_patch(Ellipse(tuple(c), w, h, fill=False, color=ink, lw=1.1)))


def fixed(smiles, coords, at=(0, 0), lone_pairs=()):
    """Place a structure at hand-chosen atom coordinates (SMILES order, in bond lengths)."""
    return s.molecule(smiles, coords=coords, at=at, lone_pairs=list(lone_pairs))


def finish():
    fig, ax = s.draw()
    ink = plt.rcParams["text.color"]
    for f in EXTRA:
        f(ax, ink)


y = 0.0
rm = s.molecule("C[Mg]Br", at=(-0.6, y + 0.2))
s.label(rm.atom(0), r"$\delta^-$", angle=90, dist=0.45, size=9)
s.label(rm.atom(1), r"$\delta^+$", angle=90, dist=0.5, size=9)
ket = s.molecule("CC(=O)C", at=(2.4, y), rotate=-90, lone_pairs=[2])
s.curly(rm.bond(0, 1), ket.atom(1), bend=0.5)
s.curly(ket.bond(1, 2), ket.atom(2), bend=0.9)
s.arrow((4.3, y), (5.7, y), above="ether")
s.molecule("CC(C)(C)[O-]", at=(7.3, y), lone_pairs=[4])
s.text((8.0, y - 1.3), r"$^+$MgBr", size=11)
s.arrow((9.6, y), (11.0, y), above=r"H$_3$O$^+$")
s.molecule("CC(C)(C)O", at=(12.6, y))

y = -4.0
rm2 = s.molecule("CC[Mg]Br", at=(-0.9, y + 0.2))
co2 = s.molecule("O=C=O", at=(2.6, y - 0.2), lone_pairs=[0], show_carbons=[1])
s.curly(rm2.bond(1, 2), co2.atom(1), bend=0.5)
s.curly(co2.bond(0, 1), co2.atom(0), bend=0.8)
s.arrow((4.3, y), (5.7, y), above="ether")
s.molecule("CCC(=O)[O-]", at=(7.2, y))
s.text((8.4, y - 1.5), r"$^+$MgBr", size=11)
s.arrow((9.6, y), (11.0, y), above=r"H$_3$O$^+$")
s.molecule("CCC(=O)O", at=(12.6, y))
finish()
