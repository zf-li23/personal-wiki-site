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

Conventions: paternal homologues are blue (``"dna"``), maternal red (``"receptor"``), as in
``genetics.homologous_pair``; a lineage runs left to right (meiocyte, two products of meiosis I, four
products of meiosis II), and an error is marked on the division where it occurs. The pairs of a cell are
listed in a fixed order, so gamete contents are comparable between panels. Functions are deterministic
and return the anchor points of what they draw. Later extensions (inversion loops, translocation
crosses, polyploid pairing) belong in this module.
"""

from matplotlib.patches import Circle, Ellipse, Rectangle

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


__all__ = ["round_cell", "chromosome_set", "meiosis_lineage", "metaphase_I", "gamete_table"]
