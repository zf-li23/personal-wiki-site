"""Genetics figures: pedigrees, Punnett squares, chromosomes, gene structure, SBOL Visual constructs, plasmid maps.

    from wikibio import genetics as G

    ped = G.Pedigree()                                       # NSGC standard pedigree nomenclature
    ped.person("I-1", "M", status="carrier", deceased=True)
    ped.person("I-2", "F")
    ped.person("II-1", "M", status="affected", proband=True)
    ped.union("I-1", "I-2", children=["II-1"])
    G.pedigree(ax, ped, origin=(1, 8))                       # automatic layout, generation numerals, numbers

    G.punnett(ax, (2, 8), "RrYy", "RrYy")                    # any 2^n x 2^n square, phenotype colours + ratio
    G.chromosome(ax, (3, 4), length=3, centromere=0.35)      # metaphase chromosome (two sister chromatids)
    G.ideogram(ax, (6, 8), G.HUMAN_X, length=6)              # G-banded ideogram (approximate hg38 bands)
    G.homologous_pair(ax, (9, 4), loci=[(0.2, ("A", "a"))])  # replicated homologues with alleles
    G.bivalent(ax, (12, 4), chiasma=0.6)                     # four chromatids, one chiasma (crossing over)
    G.karyotype(ax, (1, 9), extra={"21": 1})                 # human karyotype (47,XY,+21 here)
    G.gene(ax, 1, 3, exons=[...], cds=(...), scale=0.002)    # exon-intron structure in bp
    parts = G.construct(ax, 1, 2, ["promoter", "rbs", ("cds", "gfp"), "terminator"])   # SBOL Visual 3
    G.interaction(ax, parts[3], parts[1], kind="inhibition")
    G.plasmid(ax, (5, 5), 2.5, 2686, features=[...], sites=[...], name="pUC19")
    G.dividing_cell(ax, (3, 3), 2.6, 2.2, ["dna", "receptor"], stage="anaphase")   # mitosis / meiosis I

Coordinates are figure units (``wikibio.canvas``); sizes default to a 0.45 in/unit canvas. Gene
names are italic (``italic=True`` on labels); allele and genotype symbols are always italic.
"""

import itertools
import math
from collections import Counter

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, Wedge

from . import palette as P
from .core import FONT, LINE, arrow, label

# ---------------------------------------------------------------------------------------------
# shared helpers


def _place(desired, widths=None, gaps=0.0, weights=None):
    """Rigid blocks in a fixed order on a line: left edges as close as possible (weighted least
    squares) to ``desired`` subject to left[k+1] >= left[k] + widths[k] + gaps[k] (pool-adjacent-violators)."""
    n = len(desired)
    if n == 0:
        return []
    widths = [0.0] * n if widths is None else list(widths)
    gaps = [gaps] * n if np.isscalar(gaps) else list(gaps)
    weights = [1.0] * n if weights is None else list(weights)
    off = [0.0]
    for k in range(n - 1):
        off.append(off[-1] + widths[k] + gaps[k])
    blocks = []  # [sum of weights, weighted sum, count]
    for d, o, w in zip(desired, off, weights):
        blocks.append([w, w * (d - o), 1])
        while len(blocks) > 1 and blocks[-2][1] / blocks[-2][0] > blocks[-1][1] / blocks[-1][0]:
            w2, s2, c2 = blocks.pop()
            blocks[-1][0] += w2
            blocks[-1][1] += s2
            blocks[-1][2] += c2
    out = []
    for w, s, c in blocks:
        out += [s / w] * c
    return [y + o for y, o in zip(out, off)]


def _strong(token):
    """A saturated shade of a token for 'filled' symbols (affected, CDS bands): clear on white and on dark."""
    return P.fill(token) if P.is_dark() else P.mix(P.fill(token), P.edge(token), 0.55)


def _raw_dark(token, t=0.25):
    """A theme-independent dark shade of a token (bands on chromosomes keep their contrast in both themes)."""
    f, e, _ = P._token(token)
    return P._safe(P.mix(e, "#1f2937", t))


def _raw_light(token, t=0.55):
    f, e, _ = P._token(token)
    return P._safe(P.mix(f, "#ffffff", t))


def _italic(text):
    """Allele / genotype text as italic mathtext (unless the caller already wrote mathtext)."""
    if "$" in text or not text:
        return text
    return r"$\mathit{" + text.replace(" ", r"\ ").replace("_", r"\_") + "}$"


# ---------------------------------------------------------------------------------------------
# 1. Pedigrees (NSGC standard nomenclature, Bennett et al. 2008; 2022 update)

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


class Pedigree:
    """A pedigree: individuals, unions (couples) and their children.

    ``person(id, sex, status, ...)``: sex "M" (square), "F" (circle) or "U" (diamond: sex not
    specified / unassigned; write "AFAB", "AMAB", "UAAB" or a gender in ``note``). ``status``:

        "unaffected"      open symbol
        "affected"        filled symbol
        "carrier"         dot in the centre (heterozygote, not expected to manifest)
        "presymptomatic"  vertical line (asymptomatic / presymptomatic carrier, may manifest later)
        "half"            left half filled (textbook convention for heterozygotes; not NSGC)

    ``conditions``: several conditions as quadrant fills, a list of tokens (or None) in the order
    upper-left, upper-right, lower-right, lower-left (two entries: left half, right half).
    ``deceased`` slash, ``proband`` arrow with P, ``consultand`` arrow without P, ``adopted``
    brackets (``adopted="in"`` also dashes the line of descent: adopted into the family), ``text`` inside the symbol
    (a number of siblings "3", "P" for a pregnancy, "SB" for a stillbirth), ``note`` under the
    number (age, genotype, test result), ``kind="miscarriage"`` a small triangle (spontaneous abortion),
    ``x`` a fixed horizontal position (manual layout override), ``number`` an explicit individual number.

    ``union(a, b, children=[...], consanguineous=False, separated=False, twins=[...])``: a on the
    left, b on the right. Twins: ``twins=[("III-2", "III-3", "mz")]`` with "mz" (monozygotic),
    "dz" (dizygotic) or "unknown"; list twins next to each other in ``children``. For a union between
    two families (consanguinity), put the partners at the adjacent ends of their sibships.
    """

    def __init__(self):
        self.people = {}
        self.unions = []

    def person(self, pid, sex="U", status="unaffected", conditions=None, deceased=False, proband=False, consultand=False,
               adopted=False, text=None, note=None, kind="person", x=None, number=None, token=None):
        if status not in ("unaffected", "affected", "carrier", "presymptomatic", "half"):
            raise ValueError(f"unknown pedigree status {status!r}")
        if sex not in ("M", "F", "U"):
            raise ValueError("sex must be 'M', 'F' or 'U'")
        self.people[pid] = dict(id=pid, sex=sex, status=status, conditions=conditions, deceased=deceased, proband=proband,
                                consultand=consultand, adopted=adopted, text=text, note=note, kind=kind, x=x,
                                number=number, token=token)
        return pid

    def union(self, a, b=None, children=(), consanguineous=False, separated=False, twins=()):
        for p in (a, b, *children):
            if p is not None and p not in self.people:
                raise KeyError(f"pedigree: add person {p!r} before using it in a union")
        u = dict(a=a, b=b, children=list(children), consanguineous=consanguineous, separated=separated,
                 twins=[(t[0], t[1], t[2] if len(t) > 2 else "unknown") for t in twins])
        self.unions.append(u)
        return u

    # --- structure
    def parents(self, pid):
        for u in self.unions:
            if pid in u["children"]:
                return u
        return None

    def unions_of(self, pid):
        return [u for u in self.unions if pid in (u["a"], u["b"])]

    def generations(self):
        """Generation index of every person (0 = top), from unions: partners share a generation, children are one below."""
        gen = {}
        edges = {p: [] for p in self.people}
        for u in self.unions:
            ps = [p for p in (u["a"], u["b"]) if p is not None]
            for p in ps:
                for q in ps:
                    if p != q:
                        edges[p].append((q, 0))
                for c in u["children"]:
                    edges[p].append((c, 1))
                    edges[c].append((p, -1))
        for start in self.people:
            if start in gen:
                continue
            comp, stack = {start: 0}, [start]
            while stack:
                p = stack.pop()
                for q, d in edges[p]:
                    if q not in comp:
                        comp[q] = comp[p] + d
                        stack.append(q)
            lo = min(comp.values())
            gen.update({p: g - lo for p, g in comp.items()})
        return gen

    def rows(self, gen=None):
        """Left-to-right order of each generation: sibships under their parents, partners beside their spouse."""
        gen = gen or self.generations()
        n = max(gen.values()) + 1
        rows, placed = [[] for _ in range(n)], set()

        def emit(p):
            if p in placed:
                return
            placed.add(p)
            spouses = [(u, u["b"] if u["a"] == p else u["a"]) for u in self.unions_of(p)]
            for u, q in spouses:  # married-in partners written first in the union go to the left
                if q and q not in placed and self.parents(q) is None and gen[q] == gen[p] and u["a"] == q:
                    emit(q)
            rows[gen[p]].append(p)
            for u, q in spouses:
                if q and q not in placed and self.parents(q) is None and gen[q] == gen[p]:
                    emit(q)

        for p in self.people:
            if gen[p] == 0:
                emit(p)
        for g in range(n):
            done = set()
            for p in list(rows[g]):
                for u in self.unions_of(p):
                    if id(u) in done:
                        continue
                    done.add(id(u))
                    for c in u["children"]:
                        emit(c)
            for p in self.people:
                if g + 1 < n and gen[p] == g + 1 and p not in placed and self.parents(p) is None:
                    emit(p)
        return rows

    def layout(self, dx=1.0, iterations=80):
        """Horizontal positions (units of the figure) of everyone, and the rows. Parents are centred over
        their children's sibship, couples are adjacent, families do not overlap; ``x=`` overrides."""
        gen = self.generations()
        rows = self.rows(gen)
        x = {p: i * dx for row in rows for i, p in enumerate(row)}

        def partners(p, q):
            return any({u["a"], u["b"]} == {p, q} for u in self.unions)

        units = []
        for row in rows:
            us = []
            for p in row:
                if us and partners(us[-1][-1], p):
                    us[-1].append(p)
                else:
                    us.append([p])
            units.append(us)

        def mid(u):
            ps = [x[p] for p in (u["a"], u["b"]) if p is not None]
            return sum(ps) / len(ps)

        def sib_centre(u):
            # attach points on the sibship line: a twin pair hangs from one point
            xs = [x[c] for c in u["children"]]
            for t1, t2, _ in u["twins"]:
                xs = [v for v in xs if v not in (x[t1], x[t2])] + [(x[t1] + x[t2]) / 2]
            return (min(xs) + max(xs)) / 2

        def same_family(a, b):
            pa, pb = self.parents(a[0]), self.parents(b[0])
            return pa is not None and pa is pb

        for it in range(iterations):
            order = list(range(len(rows))) + list(range(len(rows) - 1, -1, -1))
            for g in order:
                us = units[g]
                desired, weights, widths, gaps = [], [], [], []
                for k, unit in enumerate(us):
                    left = x[unit[0]]
                    tot, wsum = 0.0, 0.0
                    for j, m in enumerate(unit):
                        off = j * dx
                        pu = self.parents(m)
                        if pu is not None:
                            tot += mid(pu) + (x[m] - sib_centre(pu)) - off
                            wsum += 1.0
                        if self.people[m]["x"] is not None:
                            tot += (self.people[m]["x"] - off) * 1e6
                            wsum += 1e6
                    for u in self.unions:
                        if u["children"] and (u["a"] in unit or u["b"] in unit):
                            ref = u["a"] if u["a"] in unit else u["b"]
                            tot += sib_centre(u) + (x[ref] - mid(u)) - unit.index(ref) * dx
                            wsum += 1.0
                    if wsum == 0:
                        tot, wsum = left * 0.05, 0.05
                    desired.append(tot / wsum)
                    weights.append(wsum)
                    widths.append((len(unit) - 1) * dx)
                    gaps.append(dx if k + 1 >= len(us) or same_family(unit, us[k + 1]) else dx * 1.3)
                lefts = _place(desired, widths, gaps, weights)
                for unit, L in zip(us, lefts):
                    for j, m in enumerate(unit):
                        x[m] = L + j * dx
        return x, gen, rows


def _shape_patch(sex, kind, x, y, s, **kw):
    if kind == "miscarriage":
        return Polygon([(x, y + 0.32 * s), (x - 0.36 * s, y - 0.3 * s), (x + 0.36 * s, y - 0.3 * s)], closed=True, **kw)
    if sex == "M":
        return Rectangle((x - s / 2, y - s / 2), s, s, **kw)
    if sex == "F":
        return Circle((x, y), s / 2, **kw)
    r = 0.6 * s
    return Polygon([(x, y + r), (x + r, y), (x, y - r), (x - r, y)], closed=True, **kw)


def _half_height(sex, kind, s):
    if kind == "miscarriage":
        return 0.32 * s, 0.3 * s
    return (0.6 * s, 0.6 * s) if sex == "U" else (s / 2, s / 2)


def symbol(ax, xy, sex="M", status="unaffected", size=0.5, token="protein", conditions=None, deceased=False,
           proband=False, consultand=False, adopted=False, text=None, kind="person", lw=None, zorder=12):
    """One NSGC pedigree symbol at ``xy`` (see ``Pedigree.person`` for the arguments); also used for legends."""
    x, y = xy
    s = size
    lw = lw or LINE * 0.95
    ink = P.ink()
    strong = _strong(token)
    face = _shape_patch(sex, kind, x, y, s, facecolor=strong if status == "affected" else P.surface(), edgecolor="none", zorder=zorder)
    ax.add_patch(face)
    sectors = []
    if status == "half":
        sectors.append((90, 270, token))
    if conditions:
        if len(conditions) == 2:
            spans = [(90, 270), (-90, 90)]
        else:
            spans = [(90, 180), (0, 90), (270, 360), (180, 270)]
        sectors += [(a, b, t) for (a, b), t in zip(spans, conditions) if t]
    for a, b, t in sectors:
        w = Wedge((x, y), s * 1.5, a, b, facecolor=_strong(t), edgecolor="none", zorder=zorder + 0.1)
        ax.add_patch(w)
        w.set_clip_path(face)
    if len(sectors) > 1 or (conditions and len(conditions) > 2):  # divide the quadrants
        hh = _half_height(sex, kind, s)[0]
        ax.plot([x, x], [y - hh, y + hh], color=ink, lw=lw * 0.6, zorder=zorder + 0.2)
        if conditions and len(conditions) > 2:
            ax.plot([x - hh, x + hh], [y, y], color=ink, lw=lw * 0.6, zorder=zorder + 0.2)
    if status == "carrier":
        cy = y - (0.04 * s if kind == "miscarriage" else 0)
        ax.add_patch(Circle((x, cy), 0.14 * s, facecolor=strong, edgecolor="none", zorder=zorder + 0.3))
    if status == "presymptomatic":
        top, bot = _half_height(sex, kind, s)
        ln, = ax.plot([x, x], [y - bot, y + top], color=strong, lw=lw * 1.7, solid_capstyle="butt", zorder=zorder + 0.3)
        ln.set_clip_path(face)
    ax.add_patch(_shape_patch(sex, kind, x, y, s, fill=False, edgecolor=ink, lw=lw, zorder=zorder + 0.5, joinstyle="miter"))
    if text:
        label(ax, (x, y), text, size="small" if s >= 0.45 else "tiny",
              color=P.on_fill() if status == "affected" else ink, zorder=zorder + 1)
    if deceased:
        e = 0.62 * s
        ax.plot([x - e, x + e], [y - e, y + e], color=ink, lw=lw, solid_capstyle="round", zorder=zorder + 0.6)
    if proband or consultand:
        r = {"M": 0.74, "F": 0.56, "U": 0.5}[sex] if kind != "miscarriage" else 0.4
        d = np.array([-1.0, -1.0]) / math.sqrt(2)
        tip = np.array([x, y]) + d * r * s
        tail = tip + d * 0.62 * s
        arrow(ax, tail, tip, kind="process", color=ink, lw=lw, head=0.2 * s / 0.5, zorder=zorder + 0.6)
        if proband:
            label(ax, (tail[0] - 0.13 * s, tail[1] + 0.02 * s), "P", size="small", ha="right", bold=True, zorder=zorder + 1)
    if adopted:
        hh = _half_height(sex, kind, s)[0] + 0.12 * s
        bx = hh + 0.06 * s
        for side in (-1, 1):
            xs = x + side * bx
            ax.plot([xs - side * 0.14 * s, xs, xs, xs - side * 0.14 * s], [y + hh, y + hh, y - hh, y - hh],
                    color=ink, lw=lw * 0.9, zorder=zorder + 0.6, solid_joinstyle="miter")
    return face


def pedigree(ax, ped, origin=(1.0, 8.0), dx=1.0, dy=1.7, size=0.5, token="protein", numbers=True, generations=True,
             gen_x=None, lw=None, zorder=10):
    """Draw a ``Pedigree`` with the NSGC conventions.

    ``origin``: the leftmost individual's x and the first generation's y; ``dx`` the spacing of
    individuals, ``dy`` of generations, ``size`` the symbol size, ``token`` the colour of affected
    symbols. Generations are numbered with Roman numerals on the left (at ``gen_x``), individuals with
    Arabic numerals below the symbols, left to right in each generation. Returns {id: (x, y)}.
    """
    lw = lw or LINE * 0.95
    ink = P.ink()
    xs, gen, rows = ped.layout(dx)
    shift = origin[0] - min(xs.values())
    pos = {p: (xs[p] + shift, origin[1] - gen[p] * dy) for p in ped.people}
    s = size

    def top(p):
        q = ped.people[p]
        return pos[p][1] + _half_height(q["sex"], q["kind"], s)[0]

    # relationship lines
    for u in ped.unions:
        a, b = u["a"], u["b"]
        if b is None:
            continue
        (xa, ya), (xb, yb) = pos[a], pos[b]
        if xa > xb:
            (xa, ya), (xb, yb), a, b = (xb, yb), (xa, ya), b, a
        x0, x1 = xa + (s / 2 if ped.people[a]["sex"] != "U" else 0.6 * s), xb - (s / 2 if ped.people[b]["sex"] != "U" else 0.6 * s)
        offs = (-0.06, 0.06) if u["consanguineous"] else (0.0,)
        for o in offs:
            ax.plot([x0, x1], [ya + o, yb + o], color=ink, lw=lw, zorder=zorder, solid_capstyle="butt")
        m = (x0 + x1) / 2
        if u["separated"]:
            for k in (-0.06, 0.06):
                ax.plot([m + k - 0.06, m + k + 0.06], [ya - 0.12, ya + 0.12], color=ink, lw=lw, zorder=zorder)

    # lines of descent
    for u in ped.unions:
        kids = u["children"]
        if not kids:
            continue
        a, b = u["a"], u["b"]
        if b is None:
            mx, my = pos[a][0], pos[a][1] - _half_height(ped.people[a]["sex"], "person", s)[1]
        else:
            mx = (pos[a][0] + pos[b][0]) / 2
            my = pos[a][1] - (0.06 if u["consanguineous"] else 0.0)
        ytop = min(top(c) for c in kids)
        ys = ytop + 0.42 * (my - ytop)
        twin_of = {}
        for t1, t2, zyg in u["twins"]:
            twin_of[t1] = twin_of[t2] = (t1, t2, zyg)
        attach = []
        seen = set()
        for c in kids:
            if c in twin_of:
                t1, t2, zyg = twin_of[c]
                if (t1, t2) in seen:
                    continue
                seen.add((t1, t2))
                xa = (pos[t1][0] + pos[t2][0]) / 2
                attach.append(xa)
                pts = []
                for t in (t1, t2):
                    ax.plot([xa, pos[t][0]], [ys, top(t)], color=ink, lw=lw, zorder=zorder, solid_capstyle="round")
                    pts.append((xa + 0.5 * (pos[t][0] - xa), ys + 0.5 * (top(t) - ys)))
                if zyg == "mz":
                    ax.plot([pts[0][0], pts[1][0]], [pts[0][1], pts[1][1]], color=ink, lw=lw, zorder=zorder)
                elif zyg == "unknown":
                    label(ax, ((pts[0][0] + pts[1][0]) / 2, pts[0][1] + 0.02), "?", size="small", va="center")
            else:
                attach.append(pos[c][0])
                dashed = ped.people[c]["adopted"] == "in"
                ax.plot([pos[c][0], pos[c][0]], [ys, top(c)], color=ink, lw=lw, zorder=zorder,
                        ls=(0, (3, 2)) if dashed else "-", solid_capstyle="butt")
        lo, hi = min(attach + [mx]), max(attach + [mx])
        if hi - lo > 1e-6:
            ax.plot([lo, hi], [ys, ys], color=ink, lw=lw, zorder=zorder, solid_capstyle="projecting")
        ax.plot([mx, mx], [my, ys], color=ink, lw=lw, zorder=zorder, solid_capstyle="butt")

    # symbols, numbers, notes
    for g, row in enumerate(rows):
        for i, p in enumerate(sorted(row, key=lambda q: pos[q][0])):
            q = ped.people[p]
            symbol(ax, pos[p], q["sex"], q["status"], size=s, token=q["token"] or token, conditions=q["conditions"],
                   deceased=q["deceased"], proband=q["proband"], consultand=q["consultand"], adopted=q["adopted"],
                   text=q["text"], kind=q["kind"], lw=lw, zorder=zorder + 2)
            yb = pos[p][1] - 0.6 * s - 0.08
            if numbers:
                label(ax, (pos[p][0], yb), str(q["number"] or i + 1), size="small", va="top", zorder=zorder + 3)
                yb -= 0.3
            if q["note"]:
                label(ax, (pos[p][0], yb), q["note"], size="tiny", va="top", color=P.muted(), zorder=zorder + 3)
    if generations:
        gx = gen_x if gen_x is not None else origin[0] - 1.1 * dx
        for g in range(len(rows)):
            label(ax, (gx, origin[1] - g * dy), ROMAN[g], size="normal", ha="right", bold=True)
    return pos


def pedigree_legend(ax, xy, entries, size=0.4, token="protein", spacing=0.62, columns=1, column_width=4.0):
    """A key: ``entries`` = [("Affected", dict(sex="M", status="affected")), ...]. A spec takes the
    ``symbol`` arguments, a list of specs draws several symbols side by side, and
    ``dict(couple="union"|"consanguineous")`` or ``dict(twins="mz"|"dz")`` draw line examples."""
    x0, y0 = xy
    per = math.ceil(len(entries) / columns)
    ink = P.ink()
    lw = LINE * 0.95
    most = max(len(sp) if isinstance(sp, (list, tuple)) else 1 for _, sp in entries)
    for k, (text, spec) in enumerate(entries):
        cx = x0 + (k // per) * column_width
        cy = y0 - (k % per) * spacing
        if isinstance(spec, dict) and "couple" in spec:
            offs = (-0.05, 0.05) if spec["couple"] == "consanguineous" else (0.0,)
            for o in offs:
                ax.plot([cx - 0.2, cx + 0.4], [cy + o, cy + o], color=ink, lw=lw)
        elif isinstance(spec, dict) and "twins" in spec:
            h = size * 1.05
            apex = (cx + 0.1, cy + h / 2)
            feet = [(cx - 0.16, cy - h / 2), (cx + 0.36, cy - h / 2)]
            for fx, fy in feet:
                ax.plot([apex[0], fx], [apex[1], fy], color=ink, lw=lw, solid_capstyle="round")
            if spec["twins"] == "mz":
                ax.plot([(apex[0] + feet[0][0]) / 2, (apex[0] + feet[1][0]) / 2], [cy, cy], color=ink, lw=lw)
        else:
            specs = spec if isinstance(spec, (list, tuple)) else [spec]
            for j, sp in enumerate(specs):
                sp = dict(sp)
                symbol(ax, (cx + 0.1 + j * (size + 0.22), cy), size=size, token=sp.pop("token", token), **sp)
        label(ax, (cx + 0.75 + (most - 1) * (size + 0.22), cy), text, size="small", ha="left")


# ---------------------------------------------------------------------------------------------
# 2. Punnett squares


def _loci(genotype):
    """'AaBb' -> [('A','a'), ('B','b')]; a list of pairs passes through (for multi-character alleles)."""
    if isinstance(genotype, str):
        g = genotype.replace(" ", "")
        if len(g) % 2:
            raise ValueError(f"genotype {genotype!r}: write two allele characters per locus, or pass a list of pairs")
        return [(g[i], g[i + 1]) for i in range(0, len(g), 2)]
    return [tuple(p) for p in genotype]


def _letter(allele):
    for ch in allele.replace("\\mathit", "").replace("\\mathrm", ""):
        if ch.isalpha():
            return ch
    return allele[:1]


def _dominant(allele):
    a = allele.split("^")[-1] if "^" in allele else allele
    return _letter(a).isupper()


def gametes(genotype):
    """All 2^n gametes (one allele per locus) of a genotype, in the conventional order (AB, Ab, aB, ab)."""
    return list(itertools.product(*_loci(genotype)))


def _join(locus_pairs):
    return "".join(a + b for a, b in locus_pairs)


def punnett(ax, origin, parent1, parent2, cell=1.0, phenotype=None, colors=None, titles=("", ""), legend=True,
            text_size=None, zorder=10):
    """A Punnett square: gametes of ``parent1`` across the top, of ``parent2`` down the left.

    ``origin`` is the top-left corner of the offspring grid. Genotypes are strings with two
    characters per locus ("RrYy"), or lists of allele pairs ([("X^A", "Y")], mathtext allowed).
    ``phenotype(loci) -> class`` (loci = [(a1, a2), ...]) or a dict {default class: name} names the
    classes; the default class writes R_ for a dominant allele and rr for the homozygous recessive.
    ``colors`` {class: token} or a list of tokens (assigned by decreasing frequency). ``legend``
    draws the classes with their frequencies and the ratio on the right. Returns {"cells": {...}, "classes": Counter}.
    """
    g1, g2 = gametes(parent1), gametes(parent2)
    n1, n2 = len(g1), len(g2)
    x0, y0 = origin
    c = cell

    def default_class(loci):
        out = ""
        for a, b in loci:
            if _dominant(a) or _dominant(b):
                d = a if _dominant(a) else b
                out += d + "_"
            else:
                out += a + b
        return out

    def ordered(pair):
        # alleles of one gene: dominant first (Aa); different symbols alphabetically (X^a Y)
        def key(al):
            base = al.split("^")[0] if "^" in al else al
            return (_letter(base).upper(), not _dominant(al), al)
        a, b = pair
        return (a, b) if key(a) <= key(b) else (b, a)

    cells, classes = {}, Counter()
    for i, ga in enumerate(g2):
        for j, gb in enumerate(g1):
            loci = [ordered((p, q)) for p, q in zip(gb, ga)]
            cls = default_class(loci)
            if callable(phenotype):
                cls = phenotype(loci)
            elif isinstance(phenotype, dict):
                cls = phenotype.get(cls, cls)
            cells[(i, j)] = (loci, cls)
            classes[cls] += 1
    ranked = [k for k, _ in sorted(classes.items(), key=lambda kv: (-kv[1], list(classes).index(kv[0])))]
    default_tokens = ["highlight", "positive", "dna", "receptor", "enzyme", "trna", "protein", "chloroplast", "metabolite"]
    if isinstance(colors, dict):
        tok = {k: colors.get(k, "neutral") for k in ranked}
    else:
        seq = list(colors) if colors else default_tokens
        tok = {k: seq[i % len(seq)] for i, k in enumerate(ranked)}
    # font size: fit the longest genotype in a cell (inches per unit from the canvas)
    fig = ax.get_figure()
    ipu = fig.get_size_inches()[0] / abs(ax.get_xlim()[1] - ax.get_xlim()[0])
    nchar = max(len(_join(v[0]).replace("^", "")) for v in cells.values())
    ts = text_size or min(FONT["normal"], 0.8 * c * ipu * 72 / (0.6 * nchar))
    pad = 0.045 * c
    for (i, j), (loci, cls) in cells.items():
        cx, cy = x0 + (j + 0.5) * c, y0 - (i + 0.5) * c
        ax.add_patch(FancyBboxPatch((cx - c / 2 + pad, cy - c / 2 + pad), c - 2 * pad, c - 2 * pad,
                                    boxstyle=f"round,pad=0,rounding_size={0.12 * c}", facecolor=P.fill(tok[cls]),
                                    edgecolor=P.edge(tok[cls]), lw=LINE * 0.8, zorder=zorder))
        label(ax, (cx, cy), _italic(_join(loci)), size=ts, color=P.on_fill(), zorder=zorder + 1)
    # gamete headers
    r = 0.33 * c
    for j, gb in enumerate(g1):
        cx, cy = x0 + (j + 0.5) * c, y0 + 0.5 * c
        ax.add_patch(Circle((cx, cy), r, facecolor=P.light("dna"), edgecolor=P.edge("dna"), lw=LINE * 0.8, zorder=zorder))
        label(ax, (cx, cy), _italic("".join(gb)), size=ts, color=P.on_fill(), zorder=zorder + 1)
    for i, ga in enumerate(g2):
        cx, cy = x0 - 0.5 * c, y0 - (i + 0.5) * c
        ax.add_patch(Circle((cx, cy), r, facecolor=P.light("receptor"), edgecolor=P.edge("receptor"), lw=LINE * 0.8, zorder=zorder))
        label(ax, (cx, cy), _italic("".join(ga)), size=ts, color=P.on_fill(), zorder=zorder + 1)
    t1 = (titles[0] + "  " if titles[0] else "") + _italic(_join(_loci(parent1))) if isinstance(parent1, str) else titles[0]
    t2 = (titles[1] + "  " if titles[1] else "") + _italic(_join(_loci(parent2))) if isinstance(parent2, str) else titles[1]
    label(ax, (x0 + n1 * c / 2, y0 + 0.88 * c + 0.12), t1, size="normal", va="bottom")
    label(ax, (x0 - 0.88 * c - 0.12, y0 - n2 * c / 2), t2, size="normal", rotation=90, ha="right")
    if legend:
        lx, ly = x0 + n1 * c + 0.6, y0 - 0.35
        total = sum(classes.values())
        g = math.gcd(*classes.values()) if len(classes) > 1 else classes[ranked[0]]
        for k, cls in enumerate(ranked):
            yy = ly - k * 0.62
            ax.add_patch(FancyBboxPatch((lx, yy - 0.2), 0.4, 0.4, boxstyle="round,pad=0,rounding_size=0.08",
                                        facecolor=P.fill(tok[cls]), edgecolor=P.edge(tok[cls]), lw=LINE * 0.8, zorder=zorder))
            label(ax, (lx + 0.6, yy), cls if any(ch == " " for ch in cls) or "$" in cls else _italic(cls), size="small", ha="left")
            xc = lx + 0.6 + 0.16 * max(len(k) for k in ranked) + 0.9
            label(ax, (xc, yy), f"{classes[cls]}/{total}", size="small", ha="right", color=P.muted())
        yy = ly - len(ranked) * 0.62 - 0.1
        label(ax, (lx, yy), "Ratio  " + " : ".join(str(classes[k] // g) for k in ranked), size="normal", ha="left", bold=True)
    return {"cells": cells, "classes": classes, "tokens": tok}


# ---------------------------------------------------------------------------------------------
# 3. Chromosomes

# Human chromosomes (GRCh38): length and centromere position in Mb (approximate, from the cytoband
# p/q boundaries). Used by ``karyotype``.
HUMAN_CHROMOSOMES = {
    "1": (248.9, 123.4), "2": (242.2, 93.9), "3": (198.3, 90.9), "4": (190.2, 50.0), "5": (181.5, 48.8),
    "6": (170.8, 59.8), "7": (159.3, 60.1), "8": (145.1, 45.2), "9": (138.4, 43.0), "10": (133.8, 39.8),
    "11": (135.1, 53.4), "12": (133.3, 35.5), "13": (114.4, 17.7), "14": (107.0, 17.2), "15": (102.0, 19.0),
    "16": (90.3, 36.8), "17": (83.3, 25.1), "18": (80.4, 18.5), "19": (58.6, 26.2), "20": (64.4, 28.1),
    "21": (46.7, 12.0), "22": (50.8, 15.0), "X": (156.0, 60.6), "Y": (57.2, 10.4),
}

# Human X chromosome G-bands at ~400-band resolution (GRCh38 cytoband, Mb, rounded): (name, start, end, stain).
HUMAN_X = [
    ("p22.33", 0.0, 4.4, "gneg"), ("p22.32", 4.4, 6.1, "gpos50"), ("p22.31", 6.1, 9.6, "gneg"),
    ("p22.2", 9.6, 17.4, "gpos50"), ("p22.13", 17.4, 19.2, "gneg"), ("p22.12", 19.2, 21.9, "gpos50"),
    ("p22.11", 21.9, 24.9, "gneg"), ("p21.3", 24.9, 29.3, "gpos100"), ("p21.2", 29.3, 31.5, "gneg"),
    ("p21.1", 31.5, 37.8, "gpos100"), ("p11.4", 37.8, 42.5, "gneg"), ("p11.3", 42.5, 47.6, "gpos75"),
    ("p11.23", 47.6, 50.1, "gneg"), ("p11.22", 50.1, 54.8, "gpos25"), ("p11.21", 54.8, 58.1, "gneg"),
    ("p11.1", 58.1, 61.0, "acen"), ("q11.1", 61.0, 63.8, "acen"), ("q11.2", 63.8, 65.4, "gneg"),
    ("q12", 65.4, 68.5, "gpos50"), ("q13.1", 68.5, 73.0, "gneg"), ("q13.2", 73.0, 74.7, "gpos50"),
    ("q13.3", 74.7, 76.8, "gneg"), ("q21.1", 76.8, 85.4, "gpos100"), ("q21.2", 85.4, 87.0, "gneg"),
    ("q21.31", 87.0, 92.7, "gpos100"), ("q21.32", 92.7, 94.3, "gneg"), ("q21.33", 94.3, 99.1, "gpos75"),
    ("q22.1", 99.1, 103.3, "gneg"), ("q22.2", 103.3, 104.5, "gpos50"), ("q22.3", 104.5, 109.4, "gneg"),
    ("q23", 109.4, 117.4, "gpos75"), ("q24", 117.4, 121.8, "gneg"), ("q25", 121.8, 129.5, "gpos100"),
    ("q26.1", 129.5, 131.3, "gneg"), ("q26.2", 131.3, 134.5, "gpos25"), ("q26.3", 134.5, 138.9, "gneg"),
    ("q27.1", 138.9, 141.2, "gpos75"), ("q27.2", 141.2, 143.0, "gneg"), ("q27.3", 143.0, 148.0, "gpos100"),
    ("q28", 148.0, 156.0, "gneg"),
]

STAIN = {"gneg": 0.0, "gpos25": 0.25, "gpos50": 0.5, "gpos75": 0.75, "gpos100": 1.0, "gvar": 0.6, "stalk": 0.15}


def g_bands(bands=None):
    """Cytoband rows [(name, start, end, stain)] as ``chromosome(bands=...)`` fractions [(f0, f1, darkness)],
    and the centromere fraction: ``bands, cen = G.g_bands(G.HUMAN_X)``."""
    bands = bands or HUMAN_X
    total = bands[-1][2]
    acen = [b for b in bands if b[3] == "acen"]
    cen = acen[0][2] / total if acen else 0.5
    return [(b0 / total, b1 / total, STAIN.get(st, 0.0)) for _, b0, b1, st in bands if st != "acen"], cen


def _rod_s(n=260):
    u = np.linspace(0, 1, n)
    return 0.5 - 0.5 * np.cos(np.pi * u)  # denser near the telomeres


def _endcap(s, L, hw):
    e = np.minimum(s, 1 - s) * L
    k = np.clip(e / max(hw, 1e-6), 0, 1)
    return np.sqrt(np.clip(1 - (1 - k) ** 2, 0, 1))


def _slice(arr, s, f0, f1):
    ss = np.r_[f0, s[(s > f0) & (s < f1)], f1]
    return np.c_[np.interp(ss, s, arr[:, 0]), np.interp(ss, s, arr[:, 1])]


def _chromatid(ax, cx, cy, s, hw, segments, bands=(), marks=(), xy=(0, 0), angle=0.0, lw=None, halo=False, zorder=8):
    """Draw one chromatid in a local frame (long axis vertical): centre line ``cx``(s), ``cy``(s), half
    width ``hw``(s), then moved to ``xy`` and rotated by ``angle``. ``segments`` [(f0, f1, token)]
    colour it (f = fraction from p-ter), ``bands`` [(f0, f1, darkness)] overlay G-bands, ``marks``
    [(f, token)] are locus stripes. Widths are horizontal in the local frame, so bands stay level."""
    lw = lw or LINE * 0.85
    left = _transform(np.c_[cx - hw, cy], xy, angle)
    right = _transform(np.c_[cx + hw, cy], xy, angle)

    def poly(f0, f1):
        return np.vstack([_slice(left, s, f0, f1), _slice(right, s, f0, f1)[::-1]])

    def tok_at(f):
        for f0, f1, t in segments:
            if f0 <= f <= f1:
                return t
        return segments[0][2]

    if halo:  # a background-coloured rim separates this chromatid from one passing behind it
        rim = np.vstack([left, right[::-1]])
        ax.add_patch(Polygon(rim, closed=True, fill=False, edgecolor=P.surface(), lw=lw + 3.0, zorder=zorder - 0.01,
                             joinstyle="round"))
    for f0, f1, t in segments:
        ax.add_patch(Polygon(poly(f0, f1), closed=True, facecolor=P.fill(t), edgecolor=P.fill(t), lw=0.3, zorder=zorder))
    for f0, f1, dk in bands:
        if dk <= 0:
            continue
        t = tok_at((f0 + f1) / 2)
        col = P.mix(P.fill(t), _raw_dark(t, 0.3), 0.85 * min(1.0, dk))
        ax.add_patch(Polygon(poly(f0, f1), closed=True, facecolor=col, edgecolor=col, lw=0.2, zorder=zorder + 0.1))
    for f, t in marks:
        w = 0.016
        ax.add_patch(Polygon(poly(max(0, f - w), min(1, f + w)), closed=True, facecolor=P.fill(t), edgecolor=P.edge(t),
                             lw=0.6, zorder=zorder + 0.15))
    for f0, f1, t in segments:
        for side in (left, right):
            q = _slice(side, s, f0, f1)
            ax.plot(q[:, 0], q[:, 1], color=P.edge(t), lw=lw, zorder=zorder + 0.2, solid_capstyle="round", solid_joinstyle="round")
    return left, right


def _transform(pts, xy, angle):
    a = math.radians(angle)
    c, s_ = math.cos(a), math.sin(a)
    return np.asarray(pts, float) @ np.array([[c, s_], [-s_, c]]) + np.asarray(xy, float)


def _anchor_shift(anchor, c, L):
    return {"center": 0.5 * L, "centromere": c * L, "top": 0.0, "bottom": L}[anchor]


def chromosome(ax, xy, length=3.0, centromere=0.4, width=0.6, token="chromatin", colors=None, bands=(), loci=(),
               sister=True, angle=0.0, anchor="center", splay=0.18, lw=None, zorder=8):
    """A condensed (metaphase) chromosome: two sister chromatids joined at the centromere (primary
    constriction); the p arm is on top (``centromere`` = fraction of the length from p-ter).

    ``colors``: per-chromatid colour segments, [[(f0, f1, token), ...], [...]] (e.g. after crossing
    over); ``bands`` [(f0, f1, darkness 0..1)] G-band pattern; ``loci`` [(f, text)] or
    [(f, text, "left"|"right")] locus stripes with italic allele labels. ``sister=False`` draws a
    single chromatid (an anaphase or G1 chromosome). ``anchor``: "center", "centromere", "top" or
    "bottom" is placed at ``xy``; ``angle`` rotates (degrees, anticlockwise). Returns anchor points.
    """
    L = length
    c = centromere
    s = _rod_s()
    cw = width / 2  # chromatid width
    sig = 0.3 * width / L
    g = np.exp(-(((s - c) / sig) ** 2))
    hw = cw / 2 * (1 - 0.45 * g) * _endcap(s, L, cw / 2)
    ylocal = _anchor_shift(anchor, c, L) - s * L
    far = np.abs(s - c) / max(c, 1 - c)
    # sister chromatids touch at the centromere and part slightly towards the telomeres
    off = cw / 2 * (1 - 0.45 * g) + 0.035 * (1 - g) + splay * cw * far**2 if sister else np.zeros_like(s)
    chromatids = [-1, 1] if sister else [0]
    segs = colors or [[(0.0, 1.0, token)]] * len(chromatids)
    marks = [(lc[0], "highlight") for lc in loci]
    for k, side in enumerate(chromatids):
        _chromatid(ax, side * off, ylocal, s, hw, segs[k % len(segs)], bands=bands, marks=marks, xy=xy, angle=angle,
                   lw=lw, zorder=zorder)
    out = {
        "top": _transform([[0, ylocal[0]]], xy, angle)[0], "bottom": _transform([[0, ylocal[-1]]], xy, angle)[0],
        "centromere": _transform([[0, _anchor_shift(anchor, c, L) - c * L]], xy, angle)[0], "loci": {},
    }
    for lc in loci:
        f, text = lc[0], lc[1]
        side = lc[2] if len(lc) > 2 else "right"
        sg = 1 if side == "right" else -1
        yl = _anchor_shift(anchor, c, L) - f * L
        edge_x = float(np.interp(f, s, off + hw)) if sister else cw / 2
        p0 = _transform([[sg * (edge_x + 0.06), yl]], xy, angle)[0]
        p1 = _transform([[sg * (edge_x + 0.28), yl]], xy, angle)[0]
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.muted(), lw=0.7, zorder=zorder + 1)
        label(ax, p1 + np.array([0.06 * sg, 0]), _italic(text), size="normal", ha="left" if sg > 0 else "right")
        out["loci"][text] = p0
    return out


def homologous_pair(ax, xy, length=3.0, centromere=0.35, width=0.55, tokens=("dna", "receptor"), loci=(), gap=0.35,
                    sister=True, labels=None, zorder=8):
    """A pair of homologous chromosomes side by side (paternal ``tokens[0]``, maternal ``tokens[1]``).
    ``loci`` [(f, ("A", "a"))]: allele labels on the outer sides. ``labels`` e.g. ("Paternal", "Maternal")
    under the chromosomes. Returns the two anchor dicts."""
    x, y = xy
    dxh = width / 2 + gap / 2
    a = chromosome(ax, (x - dxh, y), length, centromere, width, tokens[0], sister=sister,
                   loci=[(f, al[0], "left") for f, al in loci], zorder=zorder)
    b = chromosome(ax, (x + dxh, y), length, centromere, width, tokens[1], sister=sister,
                   loci=[(f, al[1], "right") for f, al in loci], zorder=zorder)
    if labels:
        for (px, _), t in zip(((x - dxh, 0), (x + dxh, 0)), labels):
            label(ax, (px, y - length / 2 - 0.3), t, size="small", va="top")
    return a, b


def bivalent(ax, xy, length=3.2, centromere=0.3, width=0.55, tokens=("dna", "receptor"), chiasma=0.6, separation=0.6,
             ramp=0.7, loci=(), zorder=8):
    """A bivalent (tetrad) in late prophase I: two homologues, four chromatids, with one chiasma at
    fraction ``chiasma`` where two non-sister chromatids have exchanged segments (the colours swap at
    the crossing). ``separation``: gap between the homologues away from the chiasma. ``loci`` as in
    ``homologous_pair``. ``chiasma=None`` gives synapsed homologues without exchange."""
    L, c = length, centromere
    s = _rod_s(320)
    cw = width / 2
    sig = 0.3 * width / L
    g = np.exp(-(((s - c) / sig) ** 2))
    hw = cw / 2 * (1 - 0.45 * g) * _endcap(s, L, cw / 2)
    s0 = chiasma if chiasma is not None else -1.0
    d = separation * np.tanh(np.abs(s - s0) * L / ramp) if chiasma is not None else np.full_like(s, separation * 0.25)
    k = cw / 2 + 0.018
    o = cw / 2 * (1 - 0.45 * g) + 0.018 * (1 - g)
    mA = -(d / 2 + k)
    ylocal = (0.5 - s) * L
    ta, tb = tokens
    outerA = mA - o
    outerB = -outerA
    if chiasma is None:
        innerA, innerB = mA + o, -(mA + o)
        segA, segB = [(0, 1, ta)], [(0, 1, tb)]
    else:
        sign = np.where(s < s0, -1.0, 1.0)
        innerA = sign * (-(mA + o))  # starts on the A side, crosses to the B side
        innerB = -innerA
        segA, segB = [(0, s0, ta), (s0, 1, tb)], [(0, s0, tb), (s0, 1, ta)]
    for xs, seg, z in ((outerA, [(0, 1, ta)], 0), (outerB, [(0, 1, tb)], 0), (innerB, segB, 0.4), (innerA, segA, 0.8)):
        _chromatid(ax, xs, ylocal, s, hw, seg, marks=[(lc[0], "highlight") for lc in loci], xy=xy, halo=z > 0,
                   zorder=zorder + z)
    for f, al in loci:
        yl = xy[1] + (0.5 - f) * L
        xo = float(np.interp(f, s, -outerA)) + cw / 2
        for sg, t in ((-1, al[0]), (1, al[1])):
            p0, p1 = xy[0] + sg * (xo + 0.06), xy[0] + sg * (xo + 0.28)
            ax.plot([p0, p1], [yl, yl], color=P.muted(), lw=0.7, zorder=zorder + 1)
            label(ax, (p1 + 0.06 * sg, yl), _italic(t), size="normal", ha="left" if sg > 0 else "right")
    cy = xy[1] + (0.5 - s0) * L if chiasma is not None else None
    return {"chiasma": (xy[0], cy) if cy is not None else None, "centromere": (xy[0], xy[1] + (0.5 - c) * L)}


def ideogram(ax, xy, bands=None, length=6.0, width=0.42, token="chromatin", labels="major", loci=(), name=None,
             arms=True, label_side="right", zorder=8):
    """A G-banded chromosome ideogram, p-ter at ``xy`` (top), drawn downwards.

    ``bands`` [(name, start, end, stain)] with stain gneg / gpos25..gpos100 / acen / gvar / stalk
    (default ``HUMAN_X``). ``labels``: "major" (one label per band group such as p21), "all",
    a list of band names, or None. ``loci`` [(gene, start, end)]: highlighted
    stripes with italic gene names on the side opposite the band labels. Returns a function mapping a coordinate (Mb) to y.
    """
    bands = bands or HUMAN_X
    total = bands[-1][2]
    x, y = xy
    L = length
    s = _rod_s(400)
    acen = [b for b in bands if b[3] == "acen"]
    cen = (acen[0][2] / total) if acen else None
    hw = np.full_like(s, width / 2)
    if acen:
        a0, a1 = acen[0][1] / total, acen[-1][2] / total
        for lo, hi, rising in ((a0, cen, False), (cen, a1, True)):
            m = (s >= lo) & (s <= hi)
            t = (s[m] - lo) / max(hi - lo, 1e-9)
            hw[m] = width / 2 * (0.42 + 0.58 * (t if rising else 1 - t))
    hw *= _endcap(s, L, width / 2)
    centre = np.c_[np.full_like(s, x), y - s * L]
    dark_acen = P.fill("negative")
    d = np.gradient(centre, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    nrm = np.c_[-d[:, 1], d[:, 0]]
    left, right = centre + nrm * hw[:, None], centre - nrm * hw[:, None]
    outline = np.vstack([left, right[::-1]])
    ax.add_patch(Polygon(outline, closed=True, facecolor=_raw_light(token, 0.6), edgecolor="none", zorder=zorder))
    for nm, b0, b1, st in bands:
        f0, f1 = b0 / total, b1 / total
        if st == "acen":
            col = dark_acen
        elif STAIN.get(st, 0) > 0:
            col = P.mix(_raw_light(token, 0.6), _raw_dark(token, 0.35), STAIN[st])
        else:
            continue
        poly = np.vstack([_slice(left, s, f0, f1), _slice(right, s, f0, f1)[::-1]])
        ax.add_patch(Polygon(poly, closed=True, facecolor=col, edgecolor=col, lw=0.2, zorder=zorder + 0.1))
    ax.add_patch(Polygon(outline, closed=True, fill=False, edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder + 0.3,
                         joinstyle="round"))

    def ymap(mb):
        return y - mb / total * L

    # band labels
    sg = 1 if label_side == "right" else -1
    picks = []
    if labels == "all":
        picks = [(b[0], (b[1] + b[2]) / 2) for b in bands]
    elif labels == "major":
        groups = {}
        for nm, b0, b1, st in bands:
            key = nm.split(".")[0]
            lo, hi = groups.get(key, (b0, b1))
            groups[key] = (min(lo, b0), max(hi, b1))
        picks = [(k, (lo + hi) / 2) for k, (lo, hi) in groups.items()]
    elif labels:
        want = set(labels)
        picks = [(b[0], (b[1] + b[2]) / 2) for b in bands if b[0] in want]
    if picks:
        ys = [ymap(m) for _, m in picks]
        order = np.argsort(ys)
        spread = _place([ys[i] for i in order], gaps=0.27)
        placed = dict(zip(order, spread))
        x0 = x + sg * (width / 2 + 0.08)
        x1 = x + sg * (width / 2 + 0.42)
        for i, (nm, m) in enumerate(picks):
            ax.plot([x0, x0 + sg * 0.12, x1 - sg * 0.06], [ys[i], ys[i], placed[i]], color=P.muted(), lw=0.6, zorder=zorder)
            label(ax, (x1, placed[i]), nm, size="tiny", ha="left" if sg > 0 else "right", color=P.muted())
    # loci: a stripe on the chromosome and a leader to the gene name on the other side
    s2 = -sg
    loc_y = []
    if loci:
        mids = [ymap((lc[1] + lc[2]) / 2) for lc in loci]
        order = np.argsort(mids)
        spread = dict(zip(order, _place([mids[i] for i in order], gaps=0.3)))
        xl = x + s2 * (width / 2 + 0.75)
        for i, lc in enumerate(loci):
            gname, b0, b1 = lc[:3]
            y0, y1 = ymap(b0), ymap(b1)
            if y0 - y1 < 0.05:
                y0, y1 = (y0 + y1) / 2 + 0.025, (y0 + y1) / 2 - 0.025
            ax.add_patch(Rectangle((x - width / 2 - 0.06, y1), width + 0.12, y0 - y1, facecolor=P.fill("highlight"),
                                   edgecolor=P.edge("highlight"), lw=0.7, zorder=zorder + 0.5))
            ym = (y0 + y1) / 2
            xe = x + s2 * (width / 2 + 0.08)
            ax.plot([xe, xe + s2 * 0.2, xl - s2 * 0.06], [ym, ym, spread[i]], color=P.muted(), lw=0.6, zorder=zorder)
            label(ax, (xl, spread[i]), gname, size="small", italic=True, ha="left" if s2 > 0 else "right")
            loc_y.append(spread[i])
    if arms and cen is not None:
        xa = x + s2 * (width / 2 + 0.3)
        for lo, hi, t in ((0.0, acen[0][1], "p"), (acen[-1][2], total, "q")):
            cands = np.linspace(ymap(lo) - 0.2, ymap(hi) + 0.2, 15)
            best = max(cands, key=lambda v: (min([abs(v - q) for q in loc_y] or [9]) > 0.32,
                                             -abs(v - ymap((lo + hi) / 2))))
            label(ax, (xa, best), t, size="normal", italic=True)
    if name:
        label(ax, (x, y - L - 0.3), name, size="normal", bold=True, va="top")
    return ymap


def karyotype(ax, origin, sex="XY", extra=None, scale=0.0105, width=0.3, token="chromatin", highlight=None,
              highlight_token="receptor", rows=None, pair_gap=0.2, slot=1.15, row_gap=0.75, lw=None, zorder=8):
    """A human karyotype (karyogram): homologous pairs in the standard order, centromeres aligned in each row.

    ``sex`` "XY" or "XX"; ``extra`` {chromosome: +k or -k} for aneuploidies ({"21": 1} gives
    47,XY,+21); chromosomes named in ``highlight`` use ``highlight_token``. ``scale`` is units per Mb.
    ``origin`` is the top-left corner. Chromosomes are plain (no bands: G-band data is included only
    for the X, see ``ideogram``). Returns the formula text (e.g. "47,XY,+21").
    """
    rows = rows or [["1", "2", "3", "4", "5"], ["6", "7", "8", "9", "10", "11", "12", "X"],
                    ["13", "14", "15", "16", "17", "18"], ["19", "20", "21", "22", "Y"]]
    extra = dict(extra or {})
    highlight = set(highlight or [])
    counts = {k: 2 for k in HUMAN_CHROMOSOMES}
    counts["X"], counts["Y"] = sex.count("X"), sex.count("Y")
    for k, v in extra.items():
        counts[k] += v
    x0, y = origin
    for row in rows:
        p_max = max(HUMAN_CHROMOSOMES[k][1] for k in row) * scale
        q_max = max(HUMAN_CHROMOSOMES[k][0] - HUMAN_CHROMOSOMES[k][1] for k in row) * scale
        ycen = y - p_max - 0.1
        cx = x0 + 0.1
        for k in row:
            if k == "Y" and counts["Y"] == 0 and sex == "XX":
                continue
            n = counts[k]
            Lk, ck = HUMAN_CHROMOSOMES[k]
            w_slot = max(slot, n * (width + pair_gap) + 0.15)
            start = cx + (w_slot - (n * width + (n - 1) * pair_gap)) / 2 + width / 2
            for j in range(n):
                chromosome(ax, (start + j * (width + pair_gap), ycen), length=Lk * scale, centromere=ck / Lk, width=width,
                           token=highlight_token if k in highlight else token, anchor="centromere", splay=0.12,
                           lw=lw or LINE * 0.65, zorder=zorder)
            label(ax, (cx + w_slot / 2, ycen - q_max - 0.18), k, size="small", va="top")
            if n:
                ax.plot([cx + 0.12, cx + w_slot - 0.12], [ycen - q_max - 0.1] * 2, color=P.muted(), lw=0.6)
            cx += w_slot
        y = ycen - q_max - row_gap
    total = sum(counts.values())
    sexes = "X" * counts["X"] + "Y" * counts["Y"]
    tail = "".join(f",{'+' if v > 0 else '-'}{k}" for k, v in extra.items() if k not in ("X", "Y"))
    return f"{total},{sexes}{tail}"


# ---------------------------------------------------------------------------------------------
# 4. Gene structure


def gene(ax, x, y, exons, cds=None, scale=0.002, origin=None, strand="+", height=0.42, token="dna", intron="hat",
         promoter=None, promoter_label="Promoter", tss=True, codons=("ATG", "TGA"), exon_numbers=True, name=None,
         polya_signal=None, flank=250, scale_bar=1000, labels=True, zorder=10):
    """An exon-intron gene model on a genomic axis (coordinates in bp; ``scale`` units per bp,
    ``origin`` the bp drawn at ``x``, default the leftmost feature).

    ``exons`` [(start, end)], ``cds`` (start, end) of the coding sequence: coding parts of exons are
    full height, UTRs thinner. ``intron``: "hat" (chevrons, as in transcript models) or "line"
    (straight genomic line with direction marks). ``promoter`` (start, end) box upstream; ``tss``
    bent arrow at the transcription start site; ``codons`` labels at the start and stop codons;
    ``polya_signal`` bp of the AAUAAA signal; ``strand`` "-" draws a gene transcribed right to left.
    Returns {"x": bp -> x, "exons": [(x0, x1)], "cds": (x0, x1), "tss": x}.
    """
    ex = sorted(exons)
    lo = min([e[0] for e in ex] + ([promoter[0]] if promoter else []))
    hi = max([e[1] for e in ex] + ([promoter[1]] if promoter else []))
    origin = lo - flank if origin is None else origin

    def X(bp):
        return x + (bp - origin) * scale

    fwd = strand == "+"
    ink = P.ink()
    h, hu = height, height * 0.55
    # genomic flanks
    ax.plot([X(lo - flank), X(ex[0][0])], [y, y], color=P.muted(), lw=LINE * 1.1, zorder=zorder, solid_capstyle="round")
    ax.plot([X(ex[-1][1]), X(hi + flank)], [y, y], color=P.muted(), lw=LINE * 1.1, zorder=zorder, solid_capstyle="round")
    # introns
    for (a0, a1), (b0, b1) in zip(ex, ex[1:]):
        xa, xb = X(a1), X(b0)
        if intron == "hat":
            ax.plot([xa, (xa + xb) / 2, xb], [y + hu / 2, y + h * 0.95, y + hu / 2], color=P.edge(token), lw=LINE * 0.9,
                    zorder=zorder, solid_joinstyle="miter")
        else:
            ax.plot([xa, xb], [y, y], color=P.edge(token), lw=LINE * 0.9, zorder=zorder)
            n = max(1, int((xb - xa) / 0.5))
            for k in range(n):
                cxp = xa + (k + 0.5) * (xb - xa) / n
                sgn = 1 if fwd else -1
                ax.plot([cxp - 0.06 * sgn, cxp + 0.04 * sgn, cxp - 0.06 * sgn], [y + 0.07, y, y - 0.07], color=P.edge(token),
                        lw=LINE * 0.8, zorder=zorder, solid_joinstyle="miter")
    # exons: UTR (thin) and CDS (full height)
    c0, c1 = cds if cds else (None, None)
    num_at = []
    for e0, e1 in ex:
        pieces = []
        if cds is None:
            pieces = [(e0, e1, False)]
        else:
            cuts = sorted({e0, e1, *[v for v in (c0, c1) if e0 < v < e1]})
            for a, b in zip(cuts, cuts[1:]):
                pieces.append((a, b, c0 <= a and b <= c1))
        big = max(pieces, key=lambda q: (q[2], q[1] - q[0]))
        num_at.append((X(big[0]), X(big[1]), big[2]))
        for a, b, coding in pieces:
            hh = h if coding else hu
            ax.add_patch(Rectangle((X(a), y - hh / 2), X(b) - X(a), hh,
                                   facecolor=_strong(token) if coding else P.light(token),
                                   edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder + 1, joinstyle="miter"))
    exon_x = [(X(a), X(b)) for a, b in ex]
    nums = range(1, len(ex) + 1) if fwd else range(len(ex), 0, -1)
    if exon_numbers:
        for (xa, xb, coding), k in zip(num_at, nums):
            if xb - xa > 0.3 and coding:
                label(ax, ((xa + xb) / 2, y), str(k), size="tiny", color=P.on_fill(), zorder=zorder + 2)
            else:
                label(ax, ((xa + xb) / 2, y - h / 2 - 0.08), str(k), size="tiny", va="top", zorder=zorder + 2)
    if promoter:
        p0, p1 = X(promoter[0]), X(promoter[1])
        ax.add_patch(FancyBboxPatch((p0, y - hu * 0.45), p1 - p0, hu * 0.9, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=LINE * 0.8, zorder=zorder + 1))
        if promoter_label:
            label(ax, ((p0 + p1) / 2, y - h / 2 - 0.12), promoter_label, size="small", va="top")
    t_x = X(ex[0][0]) if fwd else X(ex[-1][1])
    if tss:
        sgn = 1 if fwd else -1
        y0, y1 = y + h / 2, y + h / 2 + 0.55
        ax.plot([t_x, t_x], [y0, y1], color=ink, lw=LINE * 1.1, zorder=zorder + 2, solid_capstyle="butt")
        arrow(ax, (t_x - 0.006 * sgn, y1), (t_x + 0.55 * sgn, y1), kind="process", lw=LINE * 1.1, head=0.17, zorder=zorder + 2)
        if labels:
            label(ax, (t_x, y1 + 0.16), "TSS (+1)" if labels is True else str(labels), size="small", va="bottom")
    cds_x = None
    if cds:
        cds_x = (X(c0), X(c1))
        start_x, stop_x = (cds_x[0], cds_x[1]) if fwd else (cds_x[1], cds_x[0])
        if codons:
            for xx, t in ((start_x, codons[0]), (stop_x, codons[1])):
                ax.plot([xx, xx], [y - h / 2 - 0.05, y - h / 2 - 0.3], color=ink, lw=0.8, zorder=zorder + 2)
                label(ax, (xx, y - h / 2 - 0.35), t, size="tiny", va="top", bold=True)
    if polya_signal is not None:
        xp = X(polya_signal)
        ax.plot([xp, xp], [y + hu / 2 + 0.03, y + hu / 2 + 0.3], color=ink, lw=0.8, zorder=zorder + 2)
        label(ax, (xp, y + hu / 2 + 0.34), "AATAAA", size="tiny", va="bottom", bold=True)
    if name:
        label(ax, (X(lo - flank) - 0.15, y), name, size="normal", italic=True, ha="right")
    if scale_bar:
        bx = X(hi + flank) - scale_bar * scale
        by = y - h / 2 - 1.0
        ax.plot([bx, bx + scale_bar * scale], [by, by], color=ink, lw=LINE * 1.6, solid_capstyle="butt", zorder=zorder)
        txt = f"{scale_bar / 1000:g} kb" if scale_bar >= 1000 else f"{scale_bar:g} bp"
        label(ax, (bx + scale_bar * scale / 2, by - 0.12), txt, size="small", va="top")
    return {"x": X, "exons": exon_x, "cds": cds_x, "tss": t_x}


def transcript(ax, x, y, exons, cds=None, scale=0.002, height=0.36, token="mrna", cap=True, polya=True, utr_labels=True,
               zorder=10):
    """A mature (spliced) mRNA: the exons of ``exons`` joined end to end from ``x`` (5′) rightwards,
    CDS full height, UTRs thinner, 5′ cap (m7G) and poly(A) tail. Returns the x extent of every exon."""
    ex = sorted(exons)
    h, hu = height, height * 0.55
    cx = x
    out = []
    c0, c1 = cds if cds else (None, None)
    for e0, e1 in ex:
        cuts = sorted({e0, e1, *([v for v in (c0, c1) if e0 < v < e1] if cds else [])})
        for a, b in zip(cuts, cuts[1:]):
            coding = cds is not None and c0 <= a and b <= c1
            hh = h if coding else hu
            w = (b - a) * scale
            ax.add_patch(Rectangle((cx, y - hh / 2), w, hh, facecolor=_strong(token) if coding else P.light(token),
                                   edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder + 1, joinstyle="miter"))
            cx += w
        out.append((cx - (e1 - e0) * scale, cx))
    if cap:
        ax.plot([x - 0.18, x], [y, y], color=P.edge(token), lw=LINE * 1.3, zorder=zorder)
        ax.add_patch(Circle((x - 0.28, y), 0.11, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=zorder + 1))
        label(ax, (x - 0.2, y + 0.18), "m⁷G cap", size="tiny", va="bottom", ha="right")
    if polya:
        t = np.linspace(0, 1, 60)
        xs = cx + t * 0.9
        ax.plot(xs, y + 0.05 * np.sin(t * 6 * np.pi), color=P.edge(token), lw=LINE * 1.3, zorder=zorder)
        label(ax, (cx + 0.45, y - 0.16), "poly(A)", size="tiny", va="top")
    label(ax, (x - 0.55, y), "5′", size="tiny", ha="right")
    label(ax, (cx + (1.05 if polya else 0.15), y), "3′", size="tiny", ha="left")
    if utr_labels and cds:
        cs = [o for o, (e0, e1) in zip(out, ex)]
        def mx(bp):
            for (xa, xb), (e0, e1) in zip(cs, ex):
                if e0 <= bp <= e1:
                    return xa + (bp - e0) * scale
            return None
        a, b = mx(c0), mx(c1)
        if a is not None and b is not None:
            for x0_, x1_, t in ((x, a, "5′ UTR"), (a, b, "Coding sequence"), (b, cx, "3′ UTR")):
                label(ax, ((x0_ + x1_) / 2, y - h / 2 - 0.12), t, size="tiny", va="top", color=P.muted())
    return out


# ---------------------------------------------------------------------------------------------
# 5. SBOL Visual 3 glyphs and constructs

SBOL_WIDTH = {"promoter": 1.0, "rbs": 0.8, "cds": 2.4, "terminator": 0.8, "operator": 0.7, "insulator": 0.9,
              "ori": 0.8, "primer": 1.2, "recombination": 0.8, "region": 1.8, "spacer": 0.6, "polya": 1.0}
SBOL_TOKEN = {"rbs": "trna", "cds": "dna", "recombination": "antibody", "region": "neutral", "ori": None, "operator": None,
              "insulator": None}
SBOL_ALIASES = {"gene": "cds", "ribosome entry site": "rbs", "origin": "ori", "origin of replication": "ori",
                "primer binding site": "primer", "recombination site": "recombination", "engineered region": "region",
                "lox": "recombination", "frt": "recombination", "polya site": "polya"}


def glyph(ax, kind, x, y, unit=0.5, width=None, token=None, reverse=False, text=None, italic=None, zorder=12):
    """One SBOL Visual 3 glyph with its left edge at ``x`` on a backbone at height ``y``.

    kinds: promoter (bent arrow), rbs (semicircle), cds (pentagon arrow, coloured by ``token``),
    terminator (T), operator (box on the backbone), insulator (box in a box), ori (circle on the
    backbone), primer (half arrow), recombination (triangle), region (engineered region box),
    spacer (circle with a cross), polya (A-tail). ``reverse=True`` mirrors the glyph through the
    backbone (reverse strand). Returns a dict with x0, x1, centre, top and bottom.
    """
    kind = SBOL_ALIASES.get(kind, kind)
    if kind not in SBOL_WIDTH:
        raise ValueError(f"unknown SBOL glyph {kind!r}")
    u = unit
    W = (width if width is not None else SBOL_WIDTH[kind] * u)
    ink = P.ink()
    stroke = P.edge(token) if token and kind in ("promoter", "terminator", "primer", "polya") else ink
    tok = token or SBOL_TOKEN.get(kind)
    lw = LINE * 1.35

    def T(pts):
        p = np.asarray(pts, float)
        if reverse:
            p = np.c_[W - p[:, 0], -p[:, 1]]
        return p + [x, y]

    def line(pts, color=stroke, w=lw):
        q = T(pts)
        ax.plot(q[:, 0], q[:, 1], color=color, lw=w, zorder=zorder, solid_capstyle="round", solid_joinstyle="round")

    def poly(pts, face, edge, w=LINE * 0.95):
        ax.add_patch(Polygon(T(pts), closed=True, facecolor=face, edgecolor=edge, lw=w, zorder=zorder, joinstyle="round"))

    def face_of(t):
        return P.fill(t) if t else P.surface()

    def edge_of(t):
        return P.edge(t) if t else ink

    top, bot = 0.0, 0.0
    if kind == "promoter":
        sx, hy, tip = 0.12 * u, 0.95 * u, W - 0.08 * u
        line([(sx, 0), (sx, hy), (tip - 0.02 * u, hy)])
        line([(tip - 0.24 * u, hy + 0.2 * u), (tip, hy), (tip - 0.24 * u, hy - 0.2 * u)])
        top = hy + 0.2 * u
    elif kind == "terminator":
        m, hy = W / 2, 0.85 * u
        line([(m, 0), (m, hy)])
        line([(m - 0.32 * u, hy), (m + 0.32 * u, hy)])
        top = hy
    elif kind == "rbs":
        r = 0.32 * u
        t = np.linspace(0, np.pi, 40)
        poly(np.c_[W / 2 + r * np.cos(t), r * np.sin(t)], face_of(tok), edge_of(tok))
        top = r
    elif kind == "cds":
        hh, pt = 0.42 * u, min(0.45 * u, W * 0.4)
        poly([(0, -hh), (W - pt, -hh), (W, 0), (W - pt, hh), (0, hh)], P.fill(tok), P.edge(tok))
        top, bot = hh, -hh
    elif kind == "operator":
        a = 0.26 * u
        poly([(W / 2 - a, -a), (W / 2 + a, -a), (W / 2 + a, a), (W / 2 - a, a)], face_of(tok), edge_of(tok))
        top, bot = a, -a
    elif kind == "insulator":
        for a, f in ((0.34 * u, face_of(tok)), (0.18 * u, P.surface())):
            poly([(W / 2 - a, -a), (W / 2 + a, -a), (W / 2 + a, a), (W / 2 - a, a)], f, edge_of(tok))
        top, bot = 0.34 * u, -0.34 * u
    elif kind == "ori":
        r = 0.28 * u
        t = np.linspace(0, 2 * np.pi, 60)
        poly(np.c_[W / 2 + r * np.cos(t), r * np.sin(t)], face_of(tok), edge_of(tok))
        top, bot = r, -r
    elif kind == "spacer":
        r = 0.22 * u
        t = np.linspace(0, 2 * np.pi, 60)
        poly(np.c_[W / 2 + r * np.cos(t), r * np.sin(t)], face_of(tok), edge_of(tok))
        k = r * 0.7
        line([(W / 2 - k, -k), (W / 2 + k, k)], w=LINE * 0.8)
        line([(W / 2 - k, k), (W / 2 + k, -k)], w=LINE * 0.8)
        top, bot = r, -r
    elif kind == "primer":
        hy = 0.3 * u
        line([(0.05 * u, hy), (W - 0.05 * u, hy), (W - 0.32 * u, hy + 0.22 * u)])
        top = hy + 0.22 * u
    elif kind == "recombination":
        a = 0.3 * u
        poly([(W / 2 - a * 0.85, -a), (W / 2 - a * 0.85, a), (W / 2 + a, 0)], P.fill(tok), P.edge(tok))
        top, bot = a, -a
    elif kind == "region":
        hh = 0.36 * u
        poly([(0, -hh), (W, -hh), (W, hh), (0, hh)], P.fill(tok), P.edge(tok))
        top, bot = hh, -hh
    elif kind == "polya":
        q = T([(W / 2, 0.42 * u)])[0]
        label(ax, q, "AAAA", size="tiny", color=stroke, bold=True)
        top = 0.55 * u
    if reverse:
        top, bot = -bot, -top
    if text:
        it = (kind == "cds") if italic is None else italic
        if kind in ("cds", "region"):
            pt = min(0.45 * u, W * 0.4) if kind == "cds" else 0
            cxl = x + (W - pt) / 2 + (pt if reverse and kind == "cds" else 0)
            label(ax, (cxl, y), text, size="small", italic=it, color=P.on_fill(), zorder=zorder + 1)
        elif reverse:
            label(ax, (x + W / 2, y + 0.32 * u), text, size="small", italic=it, va="bottom")
        else:
            label(ax, (x + W / 2, y - 0.4 * u), text, size="small", italic=it, va="top")
    return {"kind": kind, "x0": x, "x1": x + W, "centre": x + W / 2, "top": y + top, "bottom": y + bot, "y": y,
            "reverse": reverse, "text": text}


def construct(ax, x, y, parts, unit=0.5, gap=0.14, backbone=True, ends=0.3, zorder=12):
    """Lay out SBOL Visual glyphs left to right on a backbone line.

    ``parts``: a list of kinds ("promoter"), tuples (kind, text[, token]) or dicts with keys kind,
    text, token, reverse, width, italic. Returns the list of glyph dicts (see ``glyph``), for
    ``interaction`` arcs and annotations.
    """
    out = []
    cx = x
    for p in parts:
        if isinstance(p, str):
            p = {"kind": p}
        elif isinstance(p, (tuple, list)):
            p = dict(zip(("kind", "text", "token"), p))
        g = glyph(ax, p["kind"], cx, y, unit=unit, width=p.get("width"), token=p.get("token"), reverse=p.get("reverse", False),
                  text=p.get("text"), italic=p.get("italic"), zorder=zorder)
        out.append(g)
        cx = g["x1"] + gap
    if backbone:
        ax.plot([x - ends, cx - gap + ends], [y, y], color=P.ink(), lw=LINE * 1.5, zorder=zorder - 1, solid_capstyle="round")
    return out


def interaction(ax, a, b, kind="inhibition", height=0.9, above=True, color=None, dashed=False, zorder=11):
    """An SBOL Visual interaction drawn as an angular arc from glyph ``a`` to glyph ``b`` (dicts from
    ``construct``, or x positions): up from ``a``, across, and down onto ``b`` with an SBGN head
    (inhibition, activation/stimulation, process, catalysis, necessary)."""
    c = color or P.ink()
    sgn = 1 if above else -1

    def anchor(g):
        if isinstance(g, dict):
            return g["centre"], (g["top"] if above else g["bottom"]), g["y"]
        return g, None, None

    xa, ta, ya = anchor(a)
    xb, tb, yb = anchor(b)
    base = ya if ya is not None else yb
    ta = ta if ta is not None else base
    tb = tb if tb is not None else base
    ylev = base + sgn * height
    ax.plot([xa, xa, xb], [ta + sgn * 0.08, ylev, ylev], color=c, lw=LINE, zorder=zorder, ls=(0, (3.2, 2.2)) if dashed else "-",
            solid_joinstyle="round", solid_capstyle="round")
    arrow(ax, (xb, ylev), (xb, tb + sgn * 0.1), kind=kind, color=c, dashed=dashed, zorder=zorder)
    return ylev


# ---------------------------------------------------------------------------------------------
# 6. Plasmid maps


def _polar(center, r, theta):
    return np.asarray(center, float) + r * np.array([math.cos(theta), math.sin(theta)])


def plasmid(ax, center, radius, size, features=(), sites=(), name=None, ring=0.3, ticks=None, label_gap=0.55,
            backbone_token="neutral", zorder=10):
    """A circular plasmid map: position 1 at the top, increasing clockwise.

    ``features``: dicts with name, start, end (bp), strand (+1 clockwise arrow, -1 anticlockwise,
    0 no arrowhead), token, italic (gene names), track (0 on the backbone, 1 inside, ...), label
    (False to omit), inside (label inside the ring; default for arcs longer than 28 degrees).
    ``sites``: [(enzyme, position)] restriction sites as ticks. Labels sit outside
    with leader lines, spread so they do not overlap. ``name`` and the size are written in the centre;
    ``ticks`` (e.g. 500) adds a bp scale inside. Returns {name: angle}.
    """
    cx, cy = center
    R = radius
    ink = P.ink()

    def ang(bp):
        return math.pi / 2 - 2 * math.pi * (bp - 1) / size

    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(cx + R * np.cos(t), cy + R * np.sin(t), color=P.edge(backbone_token), lw=LINE * 1.6, zorder=zorder)
    labels = []
    out = {}
    for f in features:
        tok = f.get("token", "dna")
        rr = R - f.get("track", 0) * (ring + 0.08)
        r0, r1 = rr - ring / 2, rr + ring / 2
        a0, a1 = ang(f["start"]), ang(f["end"])
        if a1 > a0:
            a1 -= 2 * math.pi
        strand = f.get("strand", 1)
        span = a0 - a1
        head = min(0.42 * ring / rr * 1.6, span * 0.6) if strand else 0
        if strand >= 0:
            body = np.linspace(a0, a1 + head, 80)
            outer = np.c_[cx + r1 * np.cos(body), cy + r1 * np.sin(body)]
            inner = np.c_[cx + r0 * np.cos(body[::-1]), cy + r0 * np.sin(body[::-1])]
            pts = [outer]
            if strand:
                pts.append([_polar(center, r1 + 0.06, a1 + head), _polar(center, rr, a1), _polar(center, r0 - 0.06, a1 + head)])
            pts.append(inner)
        else:
            body = np.linspace(a0 - head, a1, 80)
            outer = np.c_[cx + r1 * np.cos(body), cy + r1 * np.sin(body)]
            inner = np.c_[cx + r0 * np.cos(body[::-1]), cy + r0 * np.sin(body[::-1])]
            pts = [outer, inner, [_polar(center, r0 - 0.06, a0 - head), _polar(center, rr, a0), _polar(center, r1 + 0.06, a0 - head)]]
        ax.add_patch(Polygon(np.vstack(pts), closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.85,
                             zorder=zorder + 1 + f.get("track", 0) * 0.1, joinstyle="round"))
        am = (a0 + a1) / 2
        out[f["name"]] = am
        inside = f.get("inside", span > math.radians(28))
        if f.get("label", True) and inside:
            # long features: the label sits inside the ring, beside the arc's middle
            q = _polar(center, rr - ring / 2 - (0.6 if ticks else 0.3), am)
            c_ = math.cos(am)
            label(ax, q, f["name"], size="small", italic=f.get("italic", False),
                  ha="right" if c_ > 0.35 else "left" if c_ < -0.35 else "center",
                  va="center" if abs(c_) > 0.35 else ("top" if math.sin(am) > 0 else "bottom"))
        elif f.get("label", True):
            labels.append((am, f["name"], f.get("italic", False), "bold" if f.get("bold") else None, rr + ring / 2 + 0.06))
    for enz, pos in sites:
        a = ang(pos)
        p0, p1 = _polar(center, R - 0.12, a), _polar(center, R + ring / 2 + 0.08, a)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=ink, lw=LINE * 0.9, zorder=zorder + 3, solid_capstyle="butt")
        labels.append((a, f"{enz} ({pos})", False, "site", R + ring / 2 + 0.1))
        out[enz] = a
    # spread labels on each side
    Rl = R + ring / 2 + label_gap
    gap = 0.33
    for side in (1, -1):
        items = [it for it in labels if (math.cos(it[0]) >= 0) == (side > 0)]
        if not items:
            continue
        ys = [cy + Rl * math.sin(it[0]) for it in items]
        order = np.argsort(ys)
        spread = _place([ys[i] for i in order], gaps=gap)
        yy = dict(zip(order, spread))
        for i, (a, text, italic, style, r_anchor) in enumerate(items):
            yl = yy[i]
            dy = yl - cy
            xl = cx + side * max(math.sqrt(max(Rl**2 - dy**2, 0)), 0.35 * R)
            pa = _polar(center, r_anchor, a)
            pb = _polar(center, R + ring / 2 + 0.22, a)
            ax.plot([pa[0], pb[0], xl - side * 0.05], [pa[1], pb[1], yl], color=P.muted(), lw=0.6, zorder=zorder)
            label(ax, (xl, yl), text, size="tiny" if style == "site" else "small", italic=italic, bold=style == "bold",
                  ha="left" if side > 0 else "right", color=P.muted() if style == "site" else None)
    if ticks:
        for bp in range(0, size, ticks):
            a = ang(bp + 1)
            p0, p1 = _polar(center, R - ring / 2 - 0.06, a), _polar(center, R - ring / 2 - 0.16, a)
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.muted(), lw=0.7, zorder=zorder)
            if bp:
                q = _polar(center, R - ring / 2 - 0.3, a)
                rot = (math.degrees(a) - 90 + 180) % 360 - 180
                rot = rot - 180 if rot > 90 else rot + 180 if rot <= -90 else rot  # keep the numbers upright
                label(ax, q, f"{bp}", size="tiny", color=P.muted(), rotation=rot)
    if name:
        label(ax, (cx, cy + 0.2), name, size="title", bold=True, italic=False)
    label(ax, (cx, cy - 0.25), f"{size:,} bp", size="normal", color=P.muted())
    return out


# ---------------------------------------------------------------------------------------------
# 7. A dividing cell with chromosomes (mitosis / meiosis stages)


def _v_chromatid(ax, vertex, length, centromere, width, token, toward, spread=32.0, lw=None, zorder=8):
    """An anaphase chromatid pulled by its centromere: a V whose vertex (the centromere) leads towards
    the pole, arms trailing; ``toward`` is the direction of travel (degrees). The two arms are drawn as
    an outline underlay plus fills, so their union has a single clean contour."""
    lw = lw or LINE * 0.85
    cw = width / 2
    polys = []
    for arm, sg in ((centromere * length, -1), ((1 - centromere) * length, 1)):
        t = np.linspace(0, 1, 80)
        d = t * arm
        hw = cw / 2 * _endcap(t, arm, cw / 2) * (1 - 0.3 * np.exp(-((d / (0.35 * width)) ** 2)))
        hw = np.maximum(hw, 1e-3)
        local = np.vstack([np.c_[-hw, -d], np.c_[hw, -d][::-1]])
        local = _transform(local, (0, 0), sg * spread)
        polys.append(_transform(local, vertex, toward - 90))
    for q in polys:
        ax.add_patch(Polygon(q, closed=True, facecolor=P.edge(token), edgecolor=P.edge(token), lw=lw * 2, zorder=zorder,
                             joinstyle="round"))
    for q in polys:
        ax.add_patch(Polygon(q, closed=True, facecolor=P.fill(token), edgecolor="none", zorder=zorder + 0.1))


def dividing_cell(ax, center, rx, ry, chromosomes, stage="metaphase", spindle=True, chrom_length=0.9, chrom_width=0.32,
                  seed=2, zorder=4):
    """A dividing animal cell with condensed chromosomes; the spindle poles are left and right.

    ``chromosomes``: one entry per chromosome, a token or (token, centromere fraction); for
    ``stage="metaphase I"`` one entry per bivalent, a pair of tokens (homologue facing the left pole,
    homologue facing the right pole), optionally with a centromere fraction as a third item.
    ``stage``: "metaphase" (chromosomes on the metaphase plate, sister chromatids facing opposite
    poles), "metaphase I" (bivalents on the plate, homologues facing opposite poles), "anaphase"
    (separated sister chromatids moving to the poles, centromere first). Spindle microtubules run
    from the two centrosomes (pairs of centrioles) to the kinetochores. Returns the pole positions.
    """
    from .cell import cell as _cell

    _cell(ax, center, rx, ry, kind="animal", seed=seed, zorder=zorder)
    x, y = center
    poles = [(x - rx * 0.8, y), (x + rx * 0.8, y)]
    mt = P.muted()
    n = len(chromosomes)
    step = chrom_length * 1.08
    ys = [y + (n - 1) / 2 * step - i * step for i in range(n)]
    kin = []
    for item, yy in zip(chromosomes, ys):
        if stage == "metaphase I":
            t1, t2 = item[0], item[1]
            cf = item[2] if len(item) > 2 else 0.4
            for sg, t in ((-1, t1), (1, t2)):
                chromosome(ax, (x + sg * (chrom_width * 0.5 + 0.04), yy), length=chrom_length, centromere=cf, width=chrom_width,
                           token=t, anchor="centromere", splay=0.1, zorder=zorder + 4)
            kin.append(((x - chrom_width - 0.04, yy), (x + chrom_width + 0.04, yy)))
            continue
        tok, cf = (item, 0.4) if isinstance(item, str) else (item[0], item[1])
        if stage == "metaphase":
            chromosome(ax, (x, yy), length=chrom_length, centromere=cf, width=chrom_width, token=tok, anchor="centromere",
                       splay=0.1, zorder=zorder + 4)
            kin.append(((x - chrom_width * 0.5, yy), (x + chrom_width * 0.5, yy)))
        elif stage == "anaphase":
            off = rx * 0.36
            ya = y + (yy - y) * 0.7
            for sg in (-1, 1):
                _v_chromatid(ax, (x + sg * off, ya), chrom_length, cf, chrom_width, tok, toward=180 if sg < 0 else 0,
                             zorder=zorder + 4)
            kin.append(((x - off, ya), (x + off, ya)))
        else:
            raise ValueError(f"unknown stage {stage!r}")
    if spindle:
        for kl, kr in kin:
            for pole, k in ((poles[0], kl), (poles[1], kr)):
                ax.plot([pole[0], k[0]], [pole[1], k[1]], color=mt, lw=0.6, zorder=zorder + 3)
        for pole, sg in ((poles[0], -1), (poles[1], 1)):
            for a in np.linspace(-1.0, 1.0, 7):  # astral microtubules
                th = (0 if sg < 0 else math.pi) + math.pi + a
                ax.plot([pole[0], pole[0] + 0.36 * math.cos(th)], [pole[1], pole[1] + 0.36 * math.sin(th)], color=mt, lw=0.6,
                        zorder=zorder + 3)
            ax.add_patch(Circle(pole, 0.13, facecolor=P.light("highlight"), edgecolor="none", zorder=zorder + 4))
            for dx_, ang in ((-0.045, 0), (0.045, 90)):
                w, h = (0.06, 0.16) if ang == 0 else (0.16, 0.06)
                ax.add_patch(Rectangle((pole[0] + dx_ - w / 2, pole[1] - h / 2), w, h, facecolor=P.fill("highlight"),
                                       edgecolor=P.edge("highlight"), lw=0.6, zorder=zorder + 5))
    return {"poles": poles}


__all__ = [
    "Pedigree", "pedigree", "symbol", "pedigree_legend", "punnett", "gametes", "chromosome", "homologous_pair", "bivalent",
    "ideogram", "karyotype", "g_bands", "HUMAN_X", "HUMAN_CHROMOSOMES", "gene", "transcript", "glyph", "construct", "interaction",
    "plasmid", "dividing_cell",
]
