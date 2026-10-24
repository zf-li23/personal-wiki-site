"""SN1 reaction of 2-bromo-3-methylbutane in water with rearrangement. Ionization gives a secondary
carbocation; a hydrogen on the neighbouring carbon moves with its bonding pair (1,2-hydride shift)
and gives the more stable tertiary cation, which water captures: the main product is
2-methylbutan-2-ol, not the unrearranged 3-methylbutan-2-ol."""

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
sm = s.molecule("CC(Br)C(C)C", at=(0.0, y), rotate=90, lone_pairs=[2])
s.curly(sm.bond(1, 2), sm.atom(2), bend=-0.9)
s.arrow((1.8, y), (3.2, y), above="slow", below=r"$-\,\mathrm{Br^-}$")
sec = s.molecule("C[CH+]C(C)C", at=(5.0, y), show_h=[2])
s.curly((sec.xy(2) + sec.h(2).xy) / 2, sec.atom(1), bend=-0.6)
s.text((5.0, y - 2.0), "secondary cation")
s.arrow((6.8, y), (8.2, y), above="1,2-H shift")
ter = s.molecule("CC[C+](C)C", at=(9.9, y))
s.text((9.9, y - 2.0), "tertiary cation")
s.arrow((11.6, y), (13.2, y), above=r"H$_2$O", below=r"$-\,\mathrm{H^+}$")
s.molecule("CCC(C)(C)O", at=(14.9, y), lone_pairs=[5])
s.text((14.9, y - 2.0), "2-methylbutan-2-ol")
s.text((0.0, y - 2.0), "2-bromo-3-methylbutane")
finish()
