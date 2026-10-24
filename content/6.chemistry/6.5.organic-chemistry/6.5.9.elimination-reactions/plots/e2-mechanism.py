"""E2 elimination of 2-bromo-2-methylpropane with ethoxide, drawn with the H-C-C-Br unit in the
plane of the paper and antiperiplanar. In one step the base removes the beta hydrogen, the C-H
bonding pair becomes the new pi bond and bromide leaves; the C-H sigma orbital overlaps best with
the C-Br sigma* orbital when the two bonds are anti."""

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


cb, ca = pt(-0.65, 0), pt(0.65, 0)
bond(cb, ca, clear_b=False)
hb = cb + pt(-0.45, 1.05)
label(hb, "H")
bond(cb, hb)
centre(cb, [((-1.0, -0.45), "H", "wedge"), ((-0.35, -1.1), "H", "hash")])
brp = ca + pt(0.45, -1.05)
label(brp, "Br")
bond(ca, brp)
centre(ca, [((1.0, 0.45), r"CH$_3$", "wedge"), ((0.35, 1.1), r"CH$_3$", "hash")])

eto = pt(-3.1, 1.6)
label(eto, "EtO")
label(eto + pt(0.55, 0.32), "$-$", size=10)
dots(eto + pt(0.55, -0.05), (1, 0))
s.curly(eto + pt(0.65, 0.05), hb + pt(-0.25, 0.05), bend=-0.35)
s.curly((cb + hb) / 2 + pt(0.12, -0.02), (cb + ca) / 2 + pt(0.1, 0.12), bend=-0.9)
s.curly((ca + brp) / 2 + pt(0.12, 0.05), brp + pt(0.4, 0.05), bend=0.8)
s.text((0.0, -2.2), "H and Br antiperiplanar")

s.arrow((2.6, 0), (4.0, 0))
s.molecule("C=C(C)C", at=(5.4, 0))
s.plus((6.8, 0))
label(pt(7.8, 0), "EtOH")
s.plus((8.8, 0))
s.molecule("[Br-]", at=(9.8, 0), lone_pairs=True)
s.text((5.4, -2.2), "2-methylpropene")
finish()
