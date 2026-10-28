"""Cytogenetics figures: chromosome segregation in meiosis, nondisjunction and aneuploid gametes.

    from wikibio import cytogenetics as C

    C.round_cell(ax, (2, 3), 0.9)                                       # a meiocyte, spore or gamete
    C.chromosome_set(ax, (2, 3), [("dna", True), ("receptor", False)])   # replicated / unreplicated chromosomes
    out = C.meiosis_lineage(ax, (1.2, 4), [("dna", "receptor")],          # one pair of homologues
                            nondisjunction=("I", 0), names=[("X", "X")])  # MI nondisjunction of pair 0
    out["gametes"]          # [{"counts": [2], "text": "XX", "ploidy": "n + 1"}, ...]
    C.metaphase_I(ax, (6, 3), [("dna", "receptor"), ("dna", "receptor")], flips=[False, True],
                  alleles=[("A", "a"), ("B", "b")])                     # independent orientation of bivalents
    C.gamete_table(ax, (1, 1), eggs, sperm, outcome)                    # a small cross grid with text cells

    N = ["A", "B", "o", "C", "D", "E", "F", "G"]                        # lettered chromosome, "o" = centromere
    r = C.inversion_loop(ax, (1, 5), N, "D", "F", crossover=("D", "E"))  # loop + products (r["products"])
    C.lettered(ax, (1, 2), r["products"][0])                             # draw a lettered chromatid
    C.describe(r["products"][0], N)                                      # {"kind": "dicentric", "missing", "extra", ...}
    ch = C.translocation_cross(ax, (12, 5), (["A", "o", "B"], ["C", "D"], ["W", "o", "X"], ["Y", "Z"]))
    C.translocation_segregation(ch)                                      # alternate / adjacent-1 / adjacent-2 gametes
    C.nahr_products(a, i, b, j)                                          # crossover between misaligned repeats
    C.polyploid_pairing(ax, (20, 5), "quadrivalent")                     # or "bivalents"
    C.tetrasomic_gametes(2, alpha=1/7); C.trisomic_gametes("AAa")        # gamete frequencies

Conventions: paternal homologues are blue (``"dna"``), maternal red (``"receptor"``), as in
``genetics.homologous_pair``; a lineage runs left to right (meiocyte, two products of meiosis I, four
products of meiosis II), and an error is marked on the division where it occurs. The pairs of a cell are
listed in a fixed order, so gamete contents are comparable between panels. Functions are deterministic
and return the anchor points of what they draw. The rearrangement functions (lettered chromosomes,
inversion loops, translocation quadrivalents, NAHR, polyploid pairing) compute the products of
meiosis with pure functions, so that figures and their captions use the same rule.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

from . import palette as P
from .core import LINE, arrow, label
from .genetics import chromosome

MINUS = "−"


# ---------------------------------------------------------------------------------------------
# cells and chromosome sets


def round_cell(ax, center, r, token="cytoplasm", edge="membrane", lw=None, zorder=4):
    """A round cell outline (meiocyte, meiotic product, gamete) with a pale cytoplasm fill."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(edge), lw=lw or LINE * 0.9, zorder=zorder))
    return center


def _spec(item):
    """Normalise a chromosome spec: a token, (token, sister), or a dict for ``genetics.chromosome``."""
    if isinstance(item, str):
        return dict(token=item, sister=True)
    if isinstance(item, dict):
        return dict(item)
    tok, sister = item[0], item[1]
    d = dict(token=tok, sister=sister)
    if len(item) > 2:
        d["loci"] = item[2]
    return d


def chromosome_set(ax, center, chromosomes, length=0.8, width=0.26, spacing=None, centromere=0.35, zorder=8):
    """Chromosomes standing side by side, centred on ``center``.

    ``chromosomes``: a list of tokens (replicated chromosomes), (token, sister) pairs (``sister=False``
    draws one chromatid), (token, sister, loci) with ``genetics.chromosome`` loci, or dicts of
    ``genetics.chromosome`` arguments. Returns the x positions."""
    specs = [_spec(c) for c in chromosomes]
    n = len(specs)
    if n == 0:
        return []
    sp = spacing if spacing is not None else width * 1.35
    xs = [center[0] + (i - (n - 1) / 2) * sp for i in range(n)]
    for x, s in zip(xs, specs):
        s.setdefault("length", length)
        s.setdefault("width", width)
        s.setdefault("centromere", centromere)
        chromosome(ax, (x, center[1]), zorder=zorder, splay=0.12, **s)
    return xs


# ---------------------------------------------------------------------------------------------
# a meiotic lineage with optional nondisjunction


def _content(counts, names):
    if names is None:
        return None
    parts = []
    for k, c in enumerate(counts):
        parts += [names[k][i] for i in (0, 1) for _ in range(c[i])] if names[k] else []
    if not parts:
        return "O"
    text = "".join(parts)
    return f"${text}$" if any(ch in text for ch in "^_\\") else text


def _ploidy(counts):
    extra = sum(c[0] + c[1] for c in counts) - len(counts)
    if extra == 0 and all(c[0] + c[1] == 1 for c in counts):
        return "n"
    if extra == 0:
        return "n (unbalanced)"
    return f"n + {extra}" if extra > 0 else f"n {MINUS} {-extra}"


def meiosis_lineage(ax, origin, pairs, nondisjunction=None, names=None, dx=3.0, dy=1.25, r=0.78, gamete_r=0.62,
                    length=0.72, width=0.24, flips=None, labels=True, stage_labels=True, error_token="negative",
                    text_size="small", zorder=4):
    """A meiotic lineage: meiocyte (left) -> two products of meiosis I -> four products of meiosis II.

    ``pairs`` lists the homologue pairs as (token of homologue a, token of homologue b). In meiosis I
    homologue a goes to the upper product (``flips[k]`` sends it to the lower one); in meiosis II the
    sister chromatids of each chromosome go to the two daughters. ``nondisjunction``: None, ("I", k)
    (both homologues of pair k go to the upper product of meiosis I) or ("II", k, j) (both sisters of
    pair k go to the first daughter of product j, 0 = upper). ``names`` [(name a, name b), ...] (mathtext
    allowed) writes each gamete's content ("XX", "O") under it; ``labels`` writes the chromosome count
    relative to n ("n + 1", "n - 1", "n"). Returns {"primary", "secondary", "gametes": [{"xy", "counts",
    "text", "ploidy"}]}, gametes from top to bottom; ``counts[k]`` = (copies of a, copies of b).
    """
    x0, y0 = origin
    n = len(pairs)
    flips = list(flips) if flips is not None else [False] * n
    # meiocyte
    round_cell(ax, (x0, y0), r * 1.12, zorder=zorder)
    chroms = []
    for (ta, tb) in pairs:
        chroms += [(ta, True), (tb, True)]
    chromosome_set(ax, (x0, y0), chroms, length=length, width=width, spacing=width * 1.45, zorder=zorder + 3)
    # meiosis I: each secondary gets a list of (pair, homologue) replicated chromosomes
    sec = [[], []]
    for k in range(n):
        up, down = (1, 0) if flips[k] else (0, 1)
        if nondisjunction and nondisjunction[0] == "I" and nondisjunction[1] == k:
            sec[0] += [(k, 0), (k, 1)]
        else:
            sec[0].append((k, up))
            sec[1].append((k, down))
    sec_xy = [(x0 + dx, y0 + dy), (x0 + dx, y0 - dy)]
    for j in (0, 1):
        round_cell(ax, sec_xy[j], r, zorder=zorder)
        chromosome_set(ax, sec_xy[j], [(pairs[k][h], True) for k, h in sec[j]], length=length, width=width,
                       spacing=width * 1.45, zorder=zorder + 3)
        arrow(ax, (x0 + r * 1.2, y0 + (0.25 if j == 0 else -0.25)), (sec_xy[j][0] - r - 0.1, sec_xy[j][1]),
              kind="process", lw=LINE * 0.8, head=0.16, zorder=zorder + 1)
    # meiosis II
    gam = []
    gy = [y0 + dy + dy / 2, y0 + dy - dy / 2, y0 - dy + dy / 2, y0 - dy - dy / 2]
    for j in (0, 1):
        daughters = [[], []]
        for k, h in sec[j]:
            if nondisjunction and nondisjunction[0] == "II" and nondisjunction[1] == k and nondisjunction[2] == j:
                daughters[0] += [(k, h), (k, h)]
            else:
                daughters[0].append((k, h))
                daughters[1].append((k, h))
        for i in (0, 1):
            xy = (x0 + 2 * dx, gy[2 * j + i])
            round_cell(ax, xy, gamete_r, zorder=zorder)
            content = sorted(daughters[i])
            chromosome_set(ax, xy, [(pairs[k][h], False) for k, h in content], length=length * 0.9, width=width,
                           spacing=width * 1.25, zorder=zorder + 3)
            arrow(ax, (sec_xy[j][0] + r + 0.05, sec_xy[j][1] + (0.18 if i == 0 else -0.18)), (xy[0] - gamete_r - 0.1, xy[1]),
                  kind="process", lw=LINE * 0.8, head=0.16, zorder=zorder + 1)
            counts = [[0, 0] for _ in range(n)]
            for k, h in content:
                counts[k][h] += 1
            counts = [tuple(c) for c in counts]
            g = dict(xy=xy, counts=counts, text=_content(counts, names), ploidy=_ploidy(counts))
            gam.append(g)
            tx = xy[0] + gamete_r + 0.18
            if names is not None:
                label(ax, (tx, xy[1] + (0.14 if labels else 0)), g["text"], size=text_size, ha="left", zorder=zorder + 6)
            if labels:
                bad = g["ploidy"] != "n"
                label(ax, (tx, xy[1] - (0.2 if names is not None else 0)), g["ploidy"], size="tiny", ha="left",
                      color=P.edge(error_token) if bad else P.muted(), zorder=zorder + 6)
    if stage_labels:
        label(ax, (x0 + dx / 2, y0 + dy + r + 0.15), "Meiosis I", size="tiny", color=P.muted())
        label(ax, (x0 + 1.5 * dx, y0 + 2 * dy + 0.2), "Meiosis II", size="tiny", color=P.muted())
    if nondisjunction:
        if nondisjunction[0] == "I":
            at = (x0 + dx / 2 + 0.05, y0 - 0.1)
        else:
            j = nondisjunction[2]
            at = (x0 + 1.5 * dx + 0.05, sec_xy[j][1])
        ax.add_patch(Circle(at, 0.2, facecolor=P.fill(error_token), edgecolor=P.edge(error_token), lw=LINE * 0.7,
                            zorder=zorder + 5))
        label(ax, at, "!", size="small", bold=True, color=P.on_fill(), zorder=zorder + 6)
    return dict(primary=(x0, y0), secondary=sec_xy, gametes=gam)


# ---------------------------------------------------------------------------------------------
# metaphase I: independent orientation of bivalents


def metaphase_I(ax, center, pairs, flips=None, alleles=None, rx=1.9, ry=1.55, length=0.9, width=0.3, spindle=True,
                zorder=4):
    """A cell at metaphase I: bivalents on the plate (vertical, through ``center``), homologue a facing
    the left pole and b the right pole unless ``flips[k]``. ``alleles`` [("A", "a"), ...] labels homologue a
    and b of each pair on their outer sides (italic). Returns {"poles", "plate": [(y), ...]}."""
    x, y = center
    n = len(pairs)
    flips = list(flips) if flips is not None else [False] * n
    ax.add_patch(Ellipse(center, 2 * rx, 2 * ry, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"),
                         lw=LINE * 0.9, zorder=zorder))
    poles = [(x - rx * 0.82, y), (x + rx * 0.82, y)]
    step = length * 1.25
    ys = [y + (n - 1) / 2 * step - i * step for i in range(n)]
    mt = P.muted()
    off = width * 0.8
    for k, (pair, yy) in enumerate(zip(pairs, ys)):
        order = (1, 0) if flips[k] else (0, 1)
        for side, h in zip((-1, 1), order):
            loci = []
            if alleles:
                loci = [(0.75, alleles[k][h], "left" if side < 0 else "right")]
            chromosome(ax, (x + side * off, yy), length=length, centromere=0.4, width=width, token=pair[h],
                       anchor="centromere", splay=0.1, loci=loci, zorder=zorder + 4)
            if spindle:
                pole = poles[0] if side < 0 else poles[1]
                ax.plot([pole[0], x + side * off * 1.6], [pole[1], yy], color=mt, lw=0.6, zorder=zorder + 2)
    if spindle:
        for p in poles:
            ax.add_patch(Circle(p, 0.09, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6,
                                zorder=zorder + 5))
    ax.plot([x, x], [y - ry * 0.8, y + ry * 0.8], color=mt, lw=0.6, ls=(0, (2, 2)), zorder=zorder + 1)
    return dict(poles=poles, plate=ys)


# ---------------------------------------------------------------------------------------------
# a small cross grid


def gamete_table(ax, origin, rows, cols, outcome, cell=(1.7, 0.75), row_title=None, col_title=None, size="small",
                 token=None, zorder=6):
    """A grid of text cells: ``rows`` (e.g. egg types) down the left, ``cols`` (sperm types) across the top,
    ``outcome(i, j) -> (text, token or None)`` fills cell (i, j); a token tints the cell (e.g. "negative"
    for lethal, "highlight" for exceptional progeny). ``origin`` is the top-left corner of the body."""
    x0, y0 = origin
    w, h = cell
    for j, c in enumerate(cols):
        label(ax, (x0 + (j + 0.5) * w, y0 + 0.3), c, size=size, zorder=zorder + 1)
    for i, rlab in enumerate(rows):
        label(ax, (x0 - 0.15, y0 - (i + 0.5) * h), rlab, size=size, ha="right", zorder=zorder + 1)
        for j in range(len(cols)):
            text, tok = outcome(i, j)
            face = P.light(tok) if tok else P.surface()
            ax.add_patch(Rectangle((x0 + j * w, y0 - (i + 1) * h), w, h, facecolor=face, edgecolor=P.muted(), lw=0.7,
                                   zorder=zorder))
            label(ax, (x0 + (j + 0.5) * w, y0 - (i + 0.5) * h), text, size="tiny",
                  color=P.on_fill() if tok else None, zorder=zorder + 1)
    if col_title:
        label(ax, (x0 + len(cols) * w / 2, y0 + 0.75), col_title, size="small", color=P.muted())
    if row_title:
        label(ax, (x0 - 0.15, y0 + 0.3), row_title, size="small", ha="right", color=P.muted())
    return dict(width=len(cols) * w, height=len(rows) * h)


# ---------------------------------------------------------------------------------------------
# lettered chromosomes: rearrangements as sequences of segments
#
# A chromosome (or chromatid) is a list of items; an item is a segment name ("A", "B", ...) or a
# (name, token) pair that gives the segment's colour (the chromosome it came from). The item "o"
# (or ("o", token)) is a centromere. The pure functions below compute the products of crossing over
# in rearrangement heterozygotes from these lists, so that figures and text use the same rule.

CENTROMERE = "o"


def _name(item):
    return item[0] if isinstance(item, tuple) else item


def _tok(item, default):
    return item[1] if isinstance(item, tuple) else default


def with_token(genes, token):
    """Attach a colour token to every item of a lettered chromosome: ["A", "o", "B"] -> [("A", tok), ...]."""
    return [(_name(g), token) for g in genes]


def invert(genes, first, last):
    """The chromosome with the segment from ``first`` to ``last`` (names, inclusive) in reverse order."""
    names = [_name(g) for g in genes]
    i, j = names.index(first), names.index(last)
    i, j = min(i, j), max(i, j)
    return list(genes[:i]) + list(reversed(genes[i:j + 1])) + list(genes[j + 1:])


def crossover_products(a, b, left, right):
    """Products of one crossover between chromatid ``a`` and its paired homologue ``b`` at the point
    between the adjacent segments ``left`` and ``right`` of ``a``.

    Each chromatid is cut at that point (in ``b`` the same two segments are adjacent, in either order:
    inside an inversion they are reversed), and pieces from different chromatids are joined so that
    each product contains ``left`` on one side of the joint and ``right`` on the other. Returns the two
    recombinant chromatids: (a's ``left`` piece + b's ``right`` piece, b's ``left`` piece + a's ``right``
    piece). Outside a rearrangement this is ordinary reciprocal recombination; in an inversion loop it
    gives the dicentric and acentric (paracentric) or duplication-deficiency (pericentric) products."""
    na, nb = [_name(g) for g in a], [_name(g) for g in b]
    k = na.index(left)
    if na[k + 1] != right:
        raise ValueError(f"{left!r} and {right!r} are not adjacent in the first chromatid")
    a_left, a_right = list(a[:k + 1]), list(a[k + 1:])             # joint at the end / at the start
    il, ir = nb.index(left), nb.index(right)
    if abs(il - ir) != 1:
        raise ValueError(f"{left!r} and {right!r} are not adjacent in the second chromatid")
    if il < ir:      # same orientation
        b_left, b_right = list(b[:il + 1]), list(b[ir:])
    else:            # reversed (inside an inversion): the piece holding `right` ends at the joint
        b_right = list(reversed(b[:ir + 1]))       # now starts at the joint
        b_left = list(reversed(b[il:]))            # now ends at the joint
    return a_left + b_right, b_left + a_right


def nahr_products(a, i, b, j):
    """Non-allelic homologous recombination: a crossover between item ``i`` of chromatid ``a`` and
    item ``j`` of chromatid ``b`` (two copies of a repeat, misaligned). Returns (a[:i] + b[j:],
    b[:j] + a[i:]); with the repeats in direct orientation one product has a deletion and the other
    the reciprocal duplication."""
    return list(a[:i]) + list(b[j:]), list(b[:j]) + list(a[i:])


def describe(chromatid, reference):
    """Classify a lettered chromatid against the segments of ``reference`` (a list of the normal
    chromosomes' items): {"centromeres": n, "kind": "monocentric" | "dicentric" | "acentric",
    "missing": [...], "extra": [...], "balanced": bool}. A gamete is balanced if, summed over its
    chromosomes, every segment occurs exactly once (use ``gamete_balance``)."""
    names = [_name(g) for g in chromatid]
    nc = names.count(CENTROMERE)
    kind = {0: "acentric", 1: "monocentric"}.get(nc, "dicentric")
    ref = [_name(g) for g in reference if _name(g) != CENTROMERE]
    missing = [g for g in ref if g not in names]
    extra = sorted({g for g in names if g != CENTROMERE and names.count(g) > 1})
    return dict(centromeres=nc, kind=kind, missing=missing, extra=extra,
                balanced=(nc == 1 and not missing and not extra))


def gamete_balance(chromosomes, segments):
    """True if the chromosomes of a gamete together contain each name in ``segments`` exactly once."""
    names = [_name(g) for c in chromosomes for g in c if _name(g) != CENTROMERE]
    return all(names.count(s) == 1 for s in segments) and len(names) == len(segments)


def lettered(ax, xy, genes, token="dna", unit=0.42, height=0.34, ha="left", size="tiny", text=True, lw=None,
             zorder=8):
    """Draw a lettered chromatid horizontally: one cell per segment, labelled with its name, coloured by
    its token (``(name, token)`` items) or ``token``; "o" items are centromeres (a narrow waist with a
    dot). ``xy`` is the left end (``ha="left"``), centre or right end, at mid-height. Returns
    {"x0", "x1", "y", "x": {name: [centre x, ...]}, "centromeres": [x, ...]}."""
    lw = lw or LINE * 0.7
    cw = unit * 0.42
    widths = [cw if _name(g) == CENTROMERE else unit for g in genes]
    total = sum(widths)
    x, y = xy
    x0 = x if ha == "left" else x - total / 2 if ha == "center" else x - total
    out = dict(x0=x0, x1=x0 + total, y=y, x={}, centromeres=[])
    h = height
    cx = x0
    n = len(genes)
    for k, (g, w) in enumerate(zip(genes, widths)):
        name, tok = _name(g), _tok(g, token)
        if name == CENTROMERE:
            ax.add_patch(Rectangle((cx, y - h * 0.28), w, h * 0.56, facecolor=P.fill(tok), edgecolor="none",
                                   zorder=zorder))
            ax.plot([cx, cx + w], [y + h * 0.28, y + h * 0.28], color=P.edge(tok), lw=lw, zorder=zorder + 1)
            ax.plot([cx, cx + w], [y - h * 0.28, y - h * 0.28], color=P.edge(tok), lw=lw, zorder=zorder + 1)
            ax.add_patch(Circle((cx + w / 2, y), h * 0.2, facecolor=P.edge(tok), edgecolor="none", zorder=zorder + 2))
            out["centromeres"].append(cx + w / 2)
        else:
            rounded_l = k == 0 or _name(genes[k - 1]) == CENTROMERE
            rounded_r = k == n - 1 or _name(genes[k + 1]) == CENTROMERE
            hh = h if not (rounded_l and _name(genes[k - 1]) == CENTROMERE and k > 0) else h
            r = min(h / 2, w / 2) * 0.9
            if rounded_l or rounded_r:
                ax.add_patch(FancyBboxPatch((cx, y - hh / 2), w, hh, boxstyle=f"round,pad=0,rounding_size={r}",
                                            facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=zorder))
                # square off the side that joins a neighbouring segment
                for side, rounded in ((0, rounded_l), (1, rounded_r)):
                    if not rounded:
                        sx = cx if side == 0 else cx + w - r
                        ax.add_patch(Rectangle((sx, y - hh / 2), r, hh, facecolor=P.fill(tok), edgecolor="none",
                                               zorder=zorder + 0.5))
                        ax.plot([sx, sx + r], [y + hh / 2, y + hh / 2], color=P.edge(tok), lw=lw, zorder=zorder + 1)
                        ax.plot([sx, sx + r], [y - hh / 2, y - hh / 2], color=P.edge(tok), lw=lw, zorder=zorder + 1)
            else:
                ax.add_patch(Rectangle((cx, y - hh / 2), w, hh, facecolor=P.fill(tok), edgecolor="none", zorder=zorder))
                ax.plot([cx, cx + w], [y + hh / 2, y + hh / 2], color=P.edge(tok), lw=lw, zorder=zorder + 1)
                ax.plot([cx, cx + w], [y - hh / 2, y - hh / 2], color=P.edge(tok), lw=lw, zorder=zorder + 1)
            if k > 0 and _name(genes[k - 1]) != CENTROMERE:
                ax.plot([cx, cx], [y - hh / 2, y + hh / 2], color=P.edge(tok), lw=lw * 0.6, zorder=zorder + 1)
            if text:
                label(ax, (cx + w / 2, y), name, size=size, color=P.on_fill(), zorder=zorder + 2)
            out["x"].setdefault(name, []).append(cx + w / 2)
        cx += w
    return out


# ---------------------------------------------------------------------------------------------
# inversion heterozygotes


def _arc(cx, cy, r, t0, t1, n=80):
    t = np.radians(np.linspace(t0, t1, n))
    return np.c_[cx + r * np.cos(t), cy + r * np.sin(t)]


def inversion_loop(ax, origin, normal, first, last, crossover=None, unit=0.62, gap=0.34, tokens=("dna", "receptor"),
                   lw=None, size="small", zorder=8):
    """Synapsis in an inversion heterozygote: two paired homologues (one chromatid of each drawn) form
    a loop so that the inverted segment pairs gene by gene with its normal counterpart.

    ``normal``: the normal order, a list of names with "o" for the centromere; the segment from
    ``first`` to ``last`` is inverted on the second homologue. The normal homologue (``tokens[0]``)
    runs along the outside of the loop, the inverted one (``tokens[1]``) along the inside, crossing at
    the base. ``crossover`` = (left, right) marks a crossover between those adjacent segments of the
    normal order. ``origin`` is the left end, at the height between the two homologues. Returns
    {"normal": list, "inverted": list, "products": (two recombinants) or None, "right": x of the right end}."""
    lw = lw or LINE * 2.6
    names = [_name(g) for g in normal]
    i, j = names.index(first), names.index(last)
    inv = invert(normal, first, last)
    m = j - i + 1                      # items in the loop
    x0, y0 = origin
    nl = i                             # items left of the loop
    R = max(0.9, m * unit / (2 * np.pi * 0.8))
    ro, ri = R + gap / 2, R - gap / 2
    t_in, t_out = 238.0, -58.0         # clockwise from the left foot to the right foot
    foot = ro * np.cos(np.radians(58.0))
    xl = x0 + (nl + 0.4) * unit        # end of the left arm
    cx, cy = xl + foot + 0.3, y0 + R * 1.05
    xr = cx + foot + 0.3               # start of the right arm
    tail = len(names) - j - 1
    x_end = xr + (tail + 0.4) * unit
    xb0, xb1 = xl, xr
    c_n, c_i = P.edge(tokens[0]), P.edge(tokens[1])
    yt, yb = y0 + gap / 2, y0 - gap / 2
    # normal homologue: left arm (upper line) -> outer arc clockwise -> right arm (upper line)
    arc_n = _arc(cx, cy, ro, t_in, t_out)
    path_n = np.r_[[[x0, yt]], [[xl, yt]], arc_n, [[xr, yt]], [[x_end, yt]]]
    # inverted homologue: left arm (lower line) crosses to the right foot, inner arc anticlockwise,
    # crosses back from the left foot to the right arm
    arc_i = _arc(cx, cy, ri, t_out, t_in)
    path_i = np.r_[[[x0, yb]], [[xl, yb]], arc_i, [[xr, yb]], [[x_end, yb]]]
    for path, col, z in ((path_i, c_i, zorder), (path_n, c_n, zorder + 1)):
        ax.plot(path[:, 0], path[:, 1], color=col, lw=lw, solid_capstyle="round", solid_joinstyle="round", zorder=z)
    # segment labels: outside the normal, inside the inverted homologue
    thetas = np.linspace(170.0, 10.0, m) if m > 1 else np.array([90.0])
    pos = {}
    for k in range(m):
        nm = names[i + k]
        th = np.radians(thetas[k])
        pos[nm] = th
        for r, col, off in ((ro, c_n, 0.32), (ri, c_i, -0.32)):
            px, py = cx + (r + off) * np.cos(th), cy + (r + off) * np.sin(th)
            if nm == CENTROMERE:
                ax.add_patch(Circle((cx + r * np.cos(th), cy + r * np.sin(th)), gap * 0.42, facecolor=col,
                                    edgecolor=P.surface(), lw=0.6, zorder=zorder + 3))
            else:
                label(ax, (px, py), nm, size=size, color=col, zorder=zorder + 4)
    for side, (xa, xb_) in enumerate(((x0, xb0), (xb1, x_end))):
        items = names[:i] if side == 0 else names[j + 1:]
        if not items:
            continue
        xs = [xa + (k + 0.5) * unit for k in range(len(items))] if side == 0 else \
            [xa + (k + 0.6) * unit for k in range(len(items))]
        for nm, xx in zip(items, xs):
            for yy, col, off in ((yt, c_n, 0.32), (yb, c_i, -0.32)):
                if nm == CENTROMERE:
                    ax.add_patch(Circle((xx, yy), gap * 0.42, facecolor=col, edgecolor=P.surface(), lw=0.6,
                                        zorder=zorder + 3))
                else:
                    label(ax, (xx, yy + off), nm, size=size, color=col, zorder=zorder + 4)
            pos.setdefault(nm, ("arm", xx))
    products = None
    if crossover is not None:
        a, b = crossover
        products = crossover_products(normal, inv, a, b)
        if a in names[i:j + 1] and b in names[i:j + 1]:
            th = (pos[a] + pos[b]) / 2
            mx, my = cx + R * np.cos(th), cy + R * np.sin(th)
        else:
            xa_, xb2 = pos[a][1], pos[b][1]
            mx, my = (xa_ + xb2) / 2, y0
        d = gap * 0.95
        for s in (1, -1):
            ax.plot([mx - d * 0.6, mx + d * 0.6], [my - s * d * 0.6, my + s * d * 0.6], color=P.edge("highlight"),
                    lw=LINE * 1.3, solid_capstyle="round", zorder=zorder + 5)
    return dict(normal=list(normal), inverted=inv, products=products, right=x_end, top=cy + ro)


# ---------------------------------------------------------------------------------------------
# reciprocal translocations


def translocation_chromosomes(arms, tokens=("dna", "enzyme")):
    """The four chromosomes of a reciprocal-translocation heterozygote from its four arms.

    ``arms`` = (c1, d1, c2, d2): the centromeric and distal parts of chromosome 1 and of chromosome 2,
    each a list of names read from the telomere or centromere end towards the breakpoint for the
    centromeric parts (e.g. ["A", "o", "B"]) and from the breakpoint outwards for the distal parts
    (["C", "D"]). Returns {"N1": c1 + d1, "N2": c2 + d2, "T1": c1 + d2, "T2": c2 + d1} with colour
    tokens (chromosome 1 material ``tokens[0]``, chromosome 2 material ``tokens[1]``)."""
    c1, d1, c2, d2 = arms
    t1, t2 = tokens
    C1, D1, C2, D2 = with_token(c1, t1), with_token(d1, t1), with_token(c2, t2), with_token(d2, t2)
    return dict(N1=C1 + D1, N2=C2 + D2, T1=C1 + D2, T2=C2 + D1)


def translocation_segregation(chroms):
    """The three main segregation patterns of a translocation quadrivalent (``translocation_chromosomes``)
    with the chromosomes of the two kinds of gametes each produces and whether they are balanced:
    alternate (N1 + N2 | T1 + T2), adjacent-1 (homologous centromeres to opposite poles: N1 + T2 | T1 + N2)
    and adjacent-2 (homologous centromeres to the same pole: N1 + T1 | N2 + T2)."""
    segs = [_name(g) for g in chroms["N1"] + chroms["N2"] if _name(g) != CENTROMERE]
    pats = [("Alternate", (("N1", "N2"), ("T1", "T2"))), ("Adjacent-1", (("N1", "T2"), ("T1", "N2"))),
            ("Adjacent-2", (("N1", "T1"), ("N2", "T2")))]
    out = []
    for name, gametes in pats:
        gs = []
        for g in gametes:
            cs = [chroms[k] for k in g]
            gs.append(dict(names=g, chromosomes=cs, balanced=gamete_balance(cs, segs)))
        out.append(dict(pattern=name, gametes=gs))
    return out


def translocation_cross(ax, center, arms, tokens=("dna", "enzyme"), arm=2.6, gap=0.36, lw=None, size="small",
                        names=True, zorder=8):
    """The cross-shaped pairing (quadrivalent) of a reciprocal-translocation heterozygote at pachytene.

    The four arms of the cross are the four pairing regions: chromosome 1's centromeric part (left),
    its distal part (top), chromosome 2's centromeric part (right) and its distal part (bottom); each
    arm holds the two chromosomes that share that region, one chromatid of each drawn. N1 occupies the
    left and top arms, T2 top and right, N2 right and bottom, T1 bottom and left (``arms`` as in
    ``translocation_chromosomes``, listed outwards from the centre for the drawing). Returns the four
    chromosomes."""
    lw = lw or LINE * 2.6
    chroms = translocation_chromosomes(arms, tokens)
    x, y = center
    g = gap / 2
    c1, d1, c2, d2 = arms
    col = {1: P.edge(tokens[0]), 2: P.edge(tokens[1])}
    # (path corner, arms) for each chromosome; arm directions: left (-1,0), up (0,1), right (1,0), down (0,-1)
    L = arm
    paths = {
        "N1": ([(x - L, y + g), (x - g, y + g)], [(x - g, y + g), (x - g, y + L)], (1, 1)),
        "T2": ([(x + g, y + L), (x + g, y + g)], [(x + g, y + g), (x + L, y + g)], (1, 2)),
        "N2": ([(x + L, y - g), (x + g, y - g)], [(x + g, y - g), (x + g, y - L)], (2, 2)),
        "T1": ([(x - g, y - L), (x - g, y - g)], [(x - g, y - g), (x - L, y - g)], (2, 1)),
    }
    # colours: N1 = left(1) + top(1); T2 = top(1) + right(2); N2 = right(2) + bottom(2); T1 = bottom(2) + left(1)
    seg_cols = {"N1": (1, 1), "T2": (1, 2), "N2": (2, 2), "T1": (2, 1)}
    for key, (p, q, _) in paths.items():
        ca, cb = seg_cols[key]
        ax.plot([p[0][0], p[1][0]], [p[0][1], p[1][1]], color=col[ca], lw=lw, solid_capstyle="round", zorder=zorder)
        ax.plot([q[0][0], q[1][0]], [q[0][1], q[1][1]], color=col[cb], lw=lw, solid_capstyle="round", zorder=zorder)
    # labels along the arms (outwards from the centre)
    def put(items, direction, lines, tokcol):
        dxu, dyu = direction
        k = len(items)
        for idx, nm in enumerate(items):
            t = 1.0 + idx * (L - 1.35) / max(k - 1, 1) if k > 1 else (L + 0.6) / 2
            px, py = x + dxu * t, y + dyu * t
            for (ox, oy) in lines:
                if nm == CENTROMERE:
                    ax.add_patch(Circle((px + ox, py + oy), gap * 0.42, facecolor=tokcol, edgecolor=P.surface(), lw=0.6,
                                        zorder=zorder + 2))
            if nm != CENTROMERE:
                if dyu == 0:
                    label(ax, (px, py + g + 0.32), nm, size=size, color=tokcol, zorder=zorder + 3)
                    label(ax, (px, py - g - 0.32), nm, size=size, color=tokcol, zorder=zorder + 3)
                else:
                    label(ax, (px - g - 0.3, py), nm, size=size, color=tokcol, zorder=zorder + 3)
                    label(ax, (px + g + 0.3, py), nm, size=size, color=tokcol, zorder=zorder + 3)
    put(list(reversed([_name(v) for v in c1])), (-1, 0), [(0, g), (0, -g)], col[1])
    put([_name(v) for v in d1], (0, 1), [(-g, 0), (g, 0)], col[1])
    put([_name(v) for v in c2], (1, 0), [(0, g), (0, -g)], col[2])
    put([_name(v) for v in d2], (0, -1), [(-g, 0), (g, 0)], col[2])
    if names:
        o = L + 0.25
        label(ax, (x - o * 0.72, y + o * 0.72), "N1", size="small", color=P.muted())
        label(ax, (x + o * 0.72, y + o * 0.72), "T2", size="small", color=P.muted())
        label(ax, (x + o * 0.72, y - o * 0.72), "N2", size="small", color=P.muted())
        label(ax, (x - o * 0.72, y - o * 0.72), "T1", size="small", color=P.muted())
    return chroms


# ---------------------------------------------------------------------------------------------
# polyploid meiosis: pairing configurations and gamete frequencies


def polyploid_pairing(ax, center, kind="quadrivalent", length=4.4, gap=0.3, tokens=("dna", "dna", "receptor", "receptor"),
                      alleles=None, lw=None, size="small", zorder=8):
    """Four homologues of an autotetraploid at pachytene, one chromatid each: ``kind="bivalents"``
    (two pairs, 1+2 and 3+4) or ``"quadrivalent"`` (partner exchange: 1+2 and 3+4 pair on the left
    half, 1+3 and 2+4 on the right half, so homologues 2 and 3 cross in the middle). ``alleles``
    (four strings) are written at the left ends. Returns the y of the four left ends."""
    lw = lw or LINE * 2.2
    x, y = center
    h = length / 2
    ys = [y + 1.5 * gap + 0.35, y + 0.5 * gap + 0.35, y - 0.5 * gap - 0.35, y - 1.5 * gap - 0.35]
    if kind == "bivalents":
        ys = [y + 0.9 + gap / 2, y + 0.9 - gap / 2, y - 0.9 + gap / 2, y - 0.9 - gap / 2]
        for k in range(4):
            ax.plot([x - h, x + h], [ys[k], ys[k]], color=P.edge(tokens[k]), lw=lw, solid_capstyle="round", zorder=zorder)
    else:
        left = [y + 0.9 + gap / 2, y + 0.9 - gap / 2, y - 0.9 + gap / 2, y - 0.9 - gap / 2]
        right = [left[0], left[2], left[1], left[3]]     # 1 stays top, 2 goes down, 3 goes up, 4 stays
        right = [y + 0.9 + gap / 2, y - 0.9 + gap / 2, y + 0.9 - gap / 2, y - 0.9 - gap / 2]
        for k in range(4):
            xs = [x - h, x - 0.55, x + 0.55, x + h]
            yy = [left[k], left[k], right[k], right[k]]
            ax.plot(xs, yy, color=P.edge(tokens[k]), lw=lw, solid_capstyle="round", solid_joinstyle="round",
                    zorder=zorder + (1 if k in (1, 2) else 0))
        ys = left
    if alleles:
        for k in range(4):
            label(ax, (x - h - 0.3, ys[k]), alleles[k], size=size, ha="right", italic=True, zorder=zorder + 2)
    return ys


def tetrasomic_gametes(dose, alpha=0.0):
    """Gamete frequencies of an autotetraploid with ``dose`` copies (0..4) of allele A, under random
    chromosome segregation with a double-reduction rate ``alpha`` (0 for random chromosome
    segregation, 1/7 for random chromatid segregation). Returns {0: f(aa), 1: f(Aa), 2: f(AA)}."""
    from itertools import combinations
    chrom = [1] * dose + [0] * (4 - dose)
    out = {0: 0.0, 1: 0.0, 2: 0.0}
    pairs = list(combinations(range(4), 2))
    for p, q in pairs:                       # two different homologues
        out[chrom[p] + chrom[q]] += (1 - alpha) / len(pairs)
    for p in range(4):                       # two sister copies of one homologue
        out[2 * chrom[p]] += alpha / 4
    return out


def trisomic_gametes(genotype):
    """Gametes of a trisomic (three homologues, e.g. "AAa") under random 2 : 1 segregation of the
    trivalent: a dict {gamete string: probability}, disomic and monosomic gametes together."""
    from itertools import combinations
    out = {}
    for pair in combinations(range(3), 2):
        rest = [k for k in range(3) if k not in pair][0]
        for g in ("".join(sorted(genotype[k] for k in pair)), genotype[rest]):
            out[g] = out.get(g, 0.0) + 1 / 6
    return out


__all__ = ["round_cell", "chromosome_set", "meiosis_lineage", "metaphase_I", "gamete_table", "with_token", "invert",
           "crossover_products", "nahr_products", "describe", "gamete_balance", "lettered", "inversion_loop",
           "translocation_chromosomes", "translocation_segregation", "translocation_cross", "polyploid_pairing",
           "tetrasomic_gametes", "trisomic_gametes"]
