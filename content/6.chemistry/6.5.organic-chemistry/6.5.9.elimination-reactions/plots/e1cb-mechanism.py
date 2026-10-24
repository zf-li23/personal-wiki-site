"""E1cB dehydration of 4-hydroxy-4-methylpentan-2-one (the aldol of acetone) in aqueous base.
Step 1 (fast, reversible): hydroxide removes the acidic proton alpha to the carbonyl group and gives
the enolate (the conjugate base, drawn here as the carbanion resonance form). Step 2 (slow): the
carbanion pushes out hydroxide from the beta carbon, a poor leaving group that is expelled only
because the anion is so close by, giving the conjugated enone 4-methylpent-3-en-2-one."""

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
sm = s.molecule("CC(=O)CC(C)(C)O", at=(0.0, y), lone_pairs=[7], show_h=[3])
oh = s.molecule("[OH-]", at=(-0.4, y - 2.3), lone_pairs=True)
h = sm.h(3)
s.curly(oh.atom(0), h, bend=-0.3)
s.curly((sm.xy(3) + h.xy) / 2, sm.atom(3), bend=0.9)
s.arrow((2.2, y), (3.6, y), above="fast", below=r"$-\,\mathrm{H_2O}$", kind="equilibrium")
an = s.molecule("CC(=O)[CH-]C(C)(C)O", at=(6.0, y), lone_pairs=[3, 7])
s.curly(an.atom(3), an.bond(3, 4), bend=-1.2)
s.curly(an.bond(4, 7), an.atom(7), bend=0.6)
s.text((6.0, y - 2.1), "enolate (carbanion form)")
s.arrow((8.3, y), (9.7, y), above="slow")
s.molecule("CC(=O)C=C(C)C", at=(11.6, y))
s.plus((13.4, y))
s.molecule("[OH-]", at=(14.3, y), lone_pairs=True)
finish()
