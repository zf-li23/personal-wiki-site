"""Skeletal structures and curved-arrow mechanisms for plot scripts (RDKit coordinates, matplotlib ink).

Plot scripts import it as ``from wikichem import Scheme`` (render_plot.py puts this folder on the path).
Everything is drawn in black, which the renderer turns into light ink for the dark theme, so the
drawings follow both themes like any other plot.

    from wikichem import Scheme

    s = Scheme()
    hydroxide = s.molecule("[OH-]", at=(0, 0), lone_pairs=True)
    ester = s.molecule("CC(=O)OC", at=(2.2, 0), lone_pairs=[2])
    s.curly(hydroxide.atom(0), ester.atom(1))           # lone pair attacks the carbonyl carbon
    s.curly(ester.bond(1, 2), ester.atom(2))            # the C=O pi bond moves onto oxygen
    s.arrow((4.6, 0), (5.8, 0), above="slow")
    s.draw()

Atoms are numbered in SMILES order from 0, or by atom-map number when the SMILES has them
(``[CH3:1]``): ``atom(1)`` then means the atom mapped 1, and map numbers are not drawn.
Coordinates are in bond lengths; ``at`` places the molecule's centre.

Radicals come from the SMILES (``[CH3]``, ``C=C[CH2]``) and are drawn as a single dot; a fishhook
leaving such an atom starts at its dot. ``show_h=[k]`` draws the hydrogens of atom k as atoms, so an
arrow can take one of them: ``mol.h(k)`` (``mol.h(k, 1)`` for the second). ``s.label(mol.atom(k), "δ+")``
writes a small label beside an atom (partial charges, numbering), and ``s.orbital(mol.atom(k))`` draws
a p orbital on it (``angle`` of the axis in degrees, ``phase=-1`` shades the other lobe).

Cyclic transition states and other hand-made geometries: ``s.molecule(smiles, coords=[(x, y), ...])``
places the atoms at the given coordinates (SMILES order, bond lengths, shifted by ``at``; explicit
``[H]`` atoms are kept and need coordinates too), and ``s.partial(p, q)`` draws a dashed forming or
breaking bond between two atoms or points. ``singlet=[k]`` draws the two unpaired electrons of a
carbene written ``[C]`` / ``Cl[C]Cl`` as a lone pair (singlet) instead of two dots (triplet).
``like=mol`` reuses the layout of an earlier molecule with the same atoms in the same SMILES order,
so resonance structures line up: ``b = s.molecule("C=C[CH2]", ...); s.molecule("[CH2]C=C", at=(4, 0), like=b)``
needs the atoms listed in the same order, e.g. ``"[CH2:1][CH:2]=[CH2:3]"`` against ``"[CH2:1]=[CH:2][CH2:3]"``.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, PathPatch, Polygon
from matplotlib.path import Path
from rdkit import Chem
from rdkit.Chem import rdDepictor

INK = "black"  # replaced in draw() by the theme's text colour
LINE = 1.4  # bond line width in points
FONT = 12  # atom label size in points at the default scale
DOUBLE_GAP = 0.16  # distance between the lines of a multiple bond, in bond lengths
LABEL_CLEAR = 0.27  # how far bonds stop short of an atom label
VALENCE_ELECTRONS = {"B": 3, "C": 4, "N": 5, "O": 6, "F": 7, "Si": 4, "P": 5, "S": 6, "Cl": 7, "Br": 7, "I": 7}


class Point:
    """An arrow endpoint: an atom (optionally its lone pair) or the middle of a bond."""

    def __init__(self, xy, pairs=()):
        self.xy = np.asarray(xy, dtype=float)
        self.pairs = list(pairs)  # lone-pair unit vectors an arrow may start from


class Placed:
    """A molecule drawn at a position; hands out arrow endpoints by atom number."""

    def __init__(self, mol, coords, labelled, pairs, radicals):
        self.mol = mol
        self.coords = coords
        self.labelled = labelled
        self.pairs = pairs  # atom index -> list of lone-pair unit vectors
        self.radicals = radicals  # atom index -> list of unit vectors of single electrons
        maps = {a.GetAtomMapNum(): a.GetIdx() for a in mol.GetAtoms() if a.GetAtomMapNum()}
        self._index = (lambda k: maps[k]) if maps else (lambda k: k)

    def xy(self, k):
        return self.coords[self._index(k)]

    def atom(self, k, pair=None):
        """The atom numbered k. An arrow leaving it starts from the drawn lone pair facing its target, or the i-th with ``pair=i``."""
        i = self._index(k)
        pairs = self.pairs.get(i, []) + self.radicals.get(i, [])
        return Point(self.coords[i], [pairs[pair]] if pair is not None else pairs)

    def h(self, k, n=0):
        """The n-th hydrogen drawn on atom k (the molecule must be placed with ``show_h`` including k)."""
        i = self._index(k)
        hs = [a.GetIdx() for a in self.mol.GetAtomWithIdx(i).GetNeighbors() if a.GetSymbol() == "H"]
        if not hs:
            raise ValueError(f"atom {k} has no drawn hydrogens: place the molecule with show_h=[{k}]")
        return Point(self.coords[hs[n]])

    def bond(self, j, k):
        return Point((self.xy(j) + self.xy(k)) / 2)


class Scheme:
    """A canvas of molecules, curved arrows, reaction arrows and text, drawn by ``draw()``."""

    def __init__(self, scale=0.42):
        self.scale = scale  # inches per bond length
        self.items = []  # callables drawing onto an axes
        self.points = []  # every coordinate used, for the figure bounds

    # ---------------------------------------------------------------- molecules

    def molecule(self, smiles, at=(0, 0), rotate=0, flip=False, lone_pairs=False, show_carbons=(), explicit_h=False, show_h=(),
                 coords=None, singlet=(), like=None):
        """Place a structure. ``lone_pairs``: True for every N, O, S and halogen, or a list of atom numbers;
        ``explicit_h``: draw hydrogens as atoms with bonds (Lewis structures) instead of folding them into labels;
        ``show_h``: atom numbers whose hydrogens alone are drawn as atoms (for arrows to or from one H)."""
        if like is not None:  # resonance structures: reuse the layout of an earlier drawing of the same atoms
            coords = like.coords - like.coords.mean(axis=0)
        params = Chem.SmilesParserParams()
        params.removeHs = coords is None  # with given coordinates, written [H] atoms stay atoms
        mol = Chem.MolFromSmiles(smiles, params)
        if mol is None:
            raise ValueError(f"RDKit cannot parse SMILES {smiles!r}")
        maps = {a.GetAtomMapNum(): a.GetIdx() for a in mol.GetAtoms() if a.GetAtomMapNum()}
        idx = (lambda k: maps.get(k, k)) if maps else (lambda k: k)
        if coords is not None:
            Chem.Kekulize(mol, clearAromaticFlags=True)
            xy = np.asarray(coords, dtype=float)
            if xy.shape != (mol.GetNumAtoms(), 2):
                raise ValueError(f"coords needs one (x, y) per atom: {mol.GetNumAtoms()} for {smiles!r}")
            if flip:
                xy[:, 0] = -xy[:, 0]
            t = math.radians(rotate)
            xy = xy @ np.array([[math.cos(t), math.sin(t)], [-math.sin(t), math.cos(t)]]) + np.asarray(at, dtype=float)
            return self._place(mol, xy, lone_pairs, show_carbons, idx, singlet)
        if explicit_h:
            # Lewis structures draw every hydrogen as an atom with its own bond; they are numbered after the heavy atoms.
            mol = Chem.AddHs(mol)
        elif show_h:
            mol = Chem.AddHs(mol, onlyOnAtoms=tuple(idx(k) for k in show_h))
        Chem.Kekulize(mol, clearAromaticFlags=True)
        rdDepictor.SetPreferCoordGen(True)
        rdDepictor.Compute2DCoords(mol)
        conf = mol.GetConformer()
        xy = np.array([[conf.GetAtomPosition(i).x, conf.GetAtomPosition(i).y] for i in range(mol.GetNumAtoms())])
        lengths = [np.linalg.norm(xy[b.GetBeginAtomIdx()] - xy[b.GetEndAtomIdx()]) for b in mol.GetBonds()]
        xy = (xy - xy.mean(axis=0)) / (np.mean(lengths) if lengths else 1.0)
        if flip:
            xy[:, 0] = -xy[:, 0]
        t = math.radians(rotate)
        xy = xy @ np.array([[math.cos(t), math.sin(t)], [-math.sin(t), math.cos(t)]]) + np.asarray(at, dtype=float)
        Chem.WedgeMolBonds(mol, conf)
        return self._place(mol, xy, lone_pairs, show_carbons, idx, singlet)

    def _place(self, mol, xy, lone_pairs, show_carbons, idx, singlet):
        labelled = {a.GetIdx() for a in mol.GetAtoms() if _needs_label(a) or a.GetIdx() in {idx(k) for k in show_carbons}}
        wanted = set()
        if lone_pairs is True:
            wanted = {a.GetIdx() for a in mol.GetAtoms() if a.GetSymbol() in ("N", "O", "S", "F", "Cl", "Br", "I")}
        elif lone_pairs:
            wanted = {idx(k) for k in lone_pairs}
        paired = {idx(k) for k in singlet}
        pairs, radicals = {}, {}
        for a in mol.GetAtoms():
            i, rad = a.GetIdx(), a.GetNumRadicalElectrons()
            if i not in wanted and not rad:
                continue
            n = _lone_pair_count(a) if i in wanted else 0
            if i in paired:  # a singlet carbene: its two nonbonding electrons form one more pair
                n, rad = n + rad // 2, rad % 2
            dirs = _gap_directions(mol, xy, i, n + rad)
            if n:
                pairs[i] = dirs[:n]
            if rad:
                radicals[i] = dirs[n:]

        placed = Placed(mol, xy, labelled, pairs, radicals)
        self.points.extend(xy)
        # keep lone pairs and radical dots inside the figure
        self.points.extend(xy[i] + 0.55 * d for group in (pairs, radicals) for i, dirs in group.items() for d in dirs)
        self.items.append(lambda ax: _draw_molecule(ax, placed))
        return placed

    # ------------------------------------------------------------------- arrows

    def curly(self, start, end, bend=0.5, single=False):
        """A curved electron-pushing arrow (``single=True``: one-electron fishhook)."""
        p2 = _endpoint(end, toward=None)
        p0 = _endpoint(start, toward=p2)
        d = p2 - p0
        normal = np.array([-d[1], d[0]])
        p1 = (p0 + p2) / 2 + bend * normal
        self.points.extend([p0, p1, p2])
        self.items.append(lambda ax: _draw_curly(ax, p0, p1, p2, single))

    def arrow(self, start, end, above=None, below=None, kind="forward"):
        """A reaction arrow; ``kind``: forward, equilibrium, resonance or retro. Labels are short English text or formulas."""
        a, b = np.asarray(start, float), np.asarray(end, float)
        self.points.extend([a, b])
        self.items.append(lambda ax: _draw_arrow(ax, a, b, above, below, kind))

    def text(self, at, s, size=None):
        """Free text (English, or a formula in $...$), centred at ``at``."""
        p = np.asarray(at, float)
        self.points.append(p)
        self.items.append(lambda ax: ax.text(*p, s, ha="center", va="center", fontsize=size or FONT * self.scale / 0.42, color=INK))

    def plus(self, at):
        self.text(at, "+")

    def partial(self, p, q):
        """A dashed partial bond (forming or breaking) between two atoms or points."""
        a = p.xy if isinstance(p, Point) else np.asarray(p, float)
        b = q.xy if isinstance(q, Point) else np.asarray(q, float)
        self.points.extend([a, b])
        self.items.append(lambda ax: ax.plot(*zip(a, b), color=INK, lw=LINE * 0.9, ls=(0, (3, 3))))

    def label(self, point, s, angle=None, dist=0.5, size=None):
        """A small label beside an atom or point (``δ+``, ``δ−``, a number); ``angle`` in degrees, default up and to the right."""
        p = point.xy if isinstance(point, Point) else np.asarray(point, float)
        t = math.radians(45 if angle is None else angle)
        q = p + dist * np.array([math.cos(t), math.sin(t)])
        self.points.append(q)
        self.items.append(lambda ax: ax.text(*q, s, ha="center", va="center", fontsize=size or 0.75 * FONT * self.scale / 0.42, color=INK))

    def orbital(self, point, angle=90, phase=1, size=0.55):
        """A p orbital on an atom: two lobes along ``angle`` (degrees); the lobe on the ``phase`` side is shaded."""
        p = point.xy if isinstance(point, Point) else np.asarray(point, float)
        t = math.radians(angle)
        u = np.array([math.cos(t), math.sin(t)])
        lobes = [(p + s * 0.5 * size * u, s == phase) for s in (1, -1)]
        self.points.extend(c + s * 0.5 * size * u for (c, _), s in zip(lobes, (1, -1)))
        self.items.append(lambda ax: _draw_orbital(ax, lobes, size, angle))

    # --------------------------------------------------------------------- draw

    def draw(self, margin=0.6):
        """Create the figure (left open for the renderer) and return (fig, ax)."""
        pts = np.array(self.points) if self.points else np.zeros((1, 2))
        lo, hi = pts.min(axis=0) - margin, pts.max(axis=0) + margin
        size = (hi - lo) * self.scale
        fig, ax = plt.subplots(figsize=(max(size[0], 1.0), max(size[1], 0.6)))
        ax.set_xlim(lo[0], hi[0])
        ax.set_ylim(lo[1], hi[1])
        ax.set_aspect("equal")
        ax.axis("off")
        fig.subplots_adjust(0, 0, 1, 1)
        global _font, INK
        _font = FONT * self.scale / 0.42
        INK = plt.rcParams["text.color"]  # the renderer sets it per theme (light: black)
        for item in self.items:
            item(ax)
        return fig, ax


_font = FONT


def _needs_label(atom):
    # Charged and radical carbons stay bare vertices, as in skeletal formulas; the sign and dot are drawn beside them.
    return atom.GetSymbol() != "C" or atom.GetIsotope() > 0 or atom.GetDegree() == 0


def _label_text(atom, xy, mol):
    """Element symbol with its hydrogens, written away from the bonds (HO- on the left when bonds point right)."""
    sym = atom.GetSymbol()
    if atom.GetIsotope():
        sym = f"$^{{{atom.GetIsotope()}}}$" + sym
    h = atom.GetTotalNumHs()
    hs = "" if h == 0 else ("H" if h == 1 else f"H$_{h}$")
    nbrs = [xy[n.GetIdx()] - xy[atom.GetIdx()] for n in atom.GetNeighbors()]
    left = bool(nbrs) and np.mean([v[0] for v in nbrs]) > 0.3
    charge = atom.GetFormalCharge()
    sup = "" if charge == 0 else ("+" if charge == 1 else "\N{MINUS SIGN}" if charge == -1 else f"{abs(charge)}{'+' if charge > 0 else chr(0x2212)}")
    return sym, hs, left, sup


def _lone_pair_count(atom):
    v = VALENCE_ELECTRONS.get(atom.GetSymbol())
    if v is None:
        return 0
    used = sum(b.GetBondTypeAsDouble() for b in atom.GetBonds()) + atom.GetTotalNumHs()
    return int(max(0, v - atom.GetFormalCharge() - used - atom.GetNumRadicalElectrons()) // 2)


def _gap_directions(mol, xy, i, n):
    """n unit vectors spread through the largest gaps between the atom's bonds (lone pairs, then radical electrons)."""
    atom = mol.GetAtomWithIdx(i)
    if n == 0:
        return []
    angles = sorted(math.atan2(*(xy[nb.GetIdx()] - xy[i])[::-1]) for nb in atom.GetNeighbors())
    if atom.GetTotalNumHs() and not angles:
        angles = [0.0]
    elif atom.GetTotalNumHs():
        angles.append(angles[0] + math.pi)  # the written H takes the side opposite the first bond
        angles.sort()
    if not angles:
        start = [math.pi / 2, -math.pi / 2, 0, math.pi]
        return [np.array([math.cos(a), math.sin(a)]) for a in start[:n]]
    gaps = []
    for k, a in enumerate(angles):
        b = angles[(k + 1) % len(angles)] + (2 * math.pi if k + 1 == len(angles) else 0)
        gaps.append((b - a, a))
    gaps.sort(reverse=True)
    out = []
    for k in range(n):
        width, a = gaps[k % len(gaps)]
        share = k // len(gaps) + 1
        parts = n // len(gaps) + (1 if k % len(gaps) < n % len(gaps) else 0)
        ang = a + width * share / (parts + 1)
        out.append(np.array([math.cos(ang), math.sin(ang)]))
    return out


def _draw_molecule(ax, placed):
    mol, xy = placed.mol, placed.coords
    ring_info = mol.GetRingInfo()
    for bond in mol.GetBonds():
        i, j = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        a, b = xy[i].copy(), xy[j].copy()
        u = (b - a) / np.linalg.norm(b - a)
        if i in placed.labelled:
            a = a + LABEL_CLEAR * u
        if j in placed.labelled:
            b = b - LABEL_CLEAR * u
        order = bond.GetBondTypeAsDouble()
        n = np.array([-u[1], u[0]])
        direction = bond.GetBondDir()
        if direction == Chem.BondDir.BEGINWEDGE:
            ax.add_patch(Polygon([a, b + 0.09 * n, b - 0.09 * n], closed=True, color=INK, lw=0))
            continue
        if direction == Chem.BondDir.BEGINDASH:
            for t in np.linspace(0.12, 1, 7):
                p = a + t * (b - a)
                w = 0.09 * t
                ax.plot([p[0] - w * n[0], p[0] + w * n[0]], [p[1] - w * n[1], p[1] + w * n[1]], color=INK, lw=LINE * 0.8, solid_capstyle="butt")
            continue
        if order == 2:
            rings = [r for r in ring_info.AtomRings() if i in r and j in r]
            if rings:
                centre = xy[list(rings[0])].mean(axis=0)
                side = 1 if np.dot(centre - (a + b) / 2, n) > 0 else -1
                _line(ax, a, b)
                inset = 0.14 * (b - a)
                _line(ax, a + inset + side * DOUBLE_GAP * n, b - inset + side * DOUBLE_GAP * n)
            else:
                _line(ax, a + DOUBLE_GAP / 2 * n, b + DOUBLE_GAP / 2 * n)
                _line(ax, a - DOUBLE_GAP / 2 * n, b - DOUBLE_GAP / 2 * n)
        elif order == 3:
            for s in (-1, 0, 1):
                _line(ax, a + s * DOUBLE_GAP * n, b + s * DOUBLE_GAP * n)
        else:
            _line(ax, a, b)
    for i in placed.labelled:
        atom = mol.GetAtomWithIdx(i)
        sym, hs, left, sup = _label_text(atom, xy, mol)
        ax.text(*xy[i], sym, ha="center", va="center", fontsize=_font, color=INK)
        half = 0.13 * len(sym.replace("$", "")) + 0.02
        if hs:
            ax.text(xy[i][0] + (-half if left else half), xy[i][1], hs, ha="right" if left else "left", va="center", fontsize=_font, color=INK)
        if sup:
            ax.text(xy[i][0] + half + (0 if left or not hs else 0.3) + 0.06, xy[i][1] + 0.24, sup, ha="left", va="center", fontsize=_font * 0.75, color=INK)
    for i, dirs in placed.pairs.items():
        for d in dirs:
            c = xy[i] + _pair_radius(d) * d
            t = np.array([-d[1], d[0]])
            for s in (-1, 1):
                p = c + s * 0.06 * t
                ax.plot(*p, marker="o", ms=1.8, color=INK, mec=INK, mfc=INK)
    for i, dirs in placed.radicals.items():
        for d in dirs:
            ax.plot(*(xy[i] + _pair_radius(d) * d), marker="o", ms=2.4, color=INK, mec=INK, mfc=INK)
    for atom in mol.GetAtoms():
        i, charge = atom.GetIdx(), atom.GetFormalCharge()
        if not charge or i in placed.labelled:
            continue
        # an unlabelled (carbon) vertex: write the sign in the open space, beside any dot or lone pair there
        d = -sum((xy[n.GetIdx()] - xy[i]) / np.linalg.norm(xy[n.GetIdx()] - xy[i]) for n in atom.GetNeighbors())
        d = d / np.linalg.norm(d) if np.linalg.norm(d) > 1e-6 else np.array([0.0, 1.0])
        if i in placed.radicals or i in placed.pairs:
            t = math.radians(50)
            d = np.array([d[0] * math.cos(t) - d[1] * math.sin(t), d[0] * math.sin(t) + d[1] * math.cos(t)])
        sign = ("+" if charge > 0 else "\N{MINUS SIGN}") if abs(charge) == 1 else f"{abs(charge)}{'+' if charge > 0 else chr(0x2212)}"
        ax.text(*(xy[i] + 0.36 * d), sign, ha="center", va="center", fontsize=_font * 0.8, color=INK)


def _draw_orbital(ax, lobes, size, angle):
    for centre, shaded in lobes:
        ax.add_patch(Ellipse(centre, size, 0.55 * size, angle=angle, fill=shaded, facecolor=INK if shaded else "none",
                             edgecolor=INK, alpha=None, lw=LINE * 0.7, zorder=0))
        if shaded:
            ax.patches[-1].set_facecolor((*plt.matplotlib.colors.to_rgb(INK), 0.3))


def _line(ax, a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=LINE, solid_capstyle="round")


def _endpoint(point, toward):
    if not isinstance(point, Point):
        return np.asarray(point, float)
    if toward is not None and point.pairs:
        d = toward - point.xy
        best = max(point.pairs, key=lambda v: float(np.dot(v, d)))
        return point.xy + _pair_radius(best) * best  # start at the lone pair facing the target
    return point.xy


def _pair_radius(d):
    # Labels are wider than tall: dots beside a label sit further out than dots above it.
    return 0.34 + 0.2 * abs(d[0])


def _draw_curly(ax, p0, p1, p2, single):
    # Stop short of the target so the head does not sit on the atom label.
    tangent = p2 - p1
    tangent = tangent / np.linalg.norm(tangent)
    end = p2 - 0.2 * tangent
    path = Path([p0, p1, end], [Path.MOVETO, Path.CURVE3, Path.CURVE3])
    ax.add_patch(PathPatch(path, fill=False, color=INK, lw=LINE * 0.9))
    back = end - 0.2 * tangent
    n = np.array([-tangent[1], tangent[0]])
    # A fishhook (one electron) has a single barb on the outside of the curve.
    head = [end, back + 0.11 * n, back + 0.02 * n] if single else [end, back + 0.09 * n, back - 0.09 * n]
    ax.add_patch(Polygon(head, closed=True, color=INK, lw=0))


def _draw_arrow(ax, a, b, above, below, kind):
    u = (b - a) / np.linalg.norm(b - a)
    n = np.array([-u[1], u[0]])

    def head(tip, direction, half=None):
        back = tip - 0.22 * direction
        m = np.array([-direction[1], direction[0]])
        pts = [tip, back + 0.1 * m, back - 0.1 * m] if half is None else [tip, back + half * 0.16 * m, back]
        ax.add_patch(Polygon(pts, closed=True, color=INK, lw=0))

    if kind == "equilibrium":
        for s, (p, q) in ((1, (a, b)), (-1, (b, a))):
            off = s * 0.1 * n
            _line(ax, p + off, q + off)
            head(q + off, (q - p) / np.linalg.norm(q - p), half=s)
    elif kind == "resonance":
        _line(ax, a, b)
        head(b, u)
        head(a, -u)
    elif kind == "retro":
        for s in (-1, 1):
            _line(ax, a + s * 0.07 * n, b - 0.15 * u + s * 0.07 * n)
        _line(ax, b - 0.25 * u + 0.17 * n, b)
        _line(ax, b - 0.25 * u - 0.17 * n, b)
    else:
        _line(ax, a, b - 0.1 * u)
        head(b, u)
    mid = (a + b) / 2
    if above:
        ax.text(*(mid + 0.28 * n), above, ha="center", va="bottom", fontsize=_font * 0.85, color=INK)
    if below:
        ax.text(*(mid - 0.28 * n), below, ha="center", va="top", fontsize=_font * 0.85, color=INK)
