"""Pinacol rearrangement of 2,3-dimethylbutane-2,3-diol in acid. Protonation of one hydroxyl group
(not shown) turns it into a good leaving group; loss of water gives a tertiary carbocation. A methyl
group on the neighbouring carbon migrates with its bonding pair (1,2-shift) to the cationic centre.
The new cation sits next to OH and is stabilized as a protonated carbonyl (oxocarbenium ion); loss
of the proton gives pinacolone, 3,3-dimethylbutan-2-one."""

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
p = s.molecule("CC(C)(O)C(C)(C)[OH2+]", at=(0.0, y), lone_pairs=[3])
s.curly(p.bond(4, 7), p.atom(7), bend=-0.8)
s.text((0.0, y - 2.0), "protonated pinacol")
s.arrow((1.9, y), (3.3, y), below=r"$-\,\mathrm{H_2O}$")
c = s.molecule("CC(C)(O)[C+](C)C", at=(5.1, y), lone_pairs=[3])
s.curly(c.bond(1, 0), c.atom(4), bend=-0.6)
s.text((5.1, y - 2.0), "tertiary cation")
s.arrow((6.9, y), (8.3, y), above="1,2-CH$_3$ shift")
r = s.molecule("C[C+](O)C(C)(C)C", at=(10.1, y), lone_pairs=[2])
s.curly(r.atom(2), r.bond(1, 2), bend=0.6)
s.arrow((11.9, y), (13.3, y))
s.molecule("CC(=[OH+])C(C)(C)C", at=(15.1, y), lone_pairs=[2])
s.text((12.6, y - 2.0), "oxocarbenium ion")
s.arrow((16.9, y), (18.3, y), below=r"$-\,\mathrm{H^+}$")
s.molecule("CC(=O)C(C)(C)C", at=(20.1, y))
s.text((20.1, y - 2.0), "pinacolone")
finish()
