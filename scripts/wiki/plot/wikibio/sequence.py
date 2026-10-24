"""Sequence figures: alignments, sequence logos, genome-browser tracks, read pileups and dot plots.

Residues use the fixed schemes of the palette: nucleotides ``P.NUCLEOTIDE`` (A green, C blue, G orange,
T/U red) and amino acids by property ``P.AMINO_ACID_CLASS``. All functions draw on a ``bio.canvas`` axes in
its data units and return the geometry needed to annotate further.

    from wikibio import sequence
    sequence.alignment(ax, {"Human": "KCAQCHTVE", "Yeast": "RCLQCHTVE"}, at=(2, 6))
    sequence.logo(ax, counts, at=(1, 1), height=2.0)                  # counts: L x 4 (A, C, G, T)
    gb = sequence.Browser(ax, (1_200_000, 1_215_000), 2.0, 18.0, chrom="chr7")
    gb.axis(9.5); gb.gene(8.6, [(1_201_000, 1_201_400), (1_204_000, 1_204_300)], strand="+", name="geneA")
    gb.signal(6.5, 1.2, coverage, label="RNA-seq"); gb.peaks(5.6, [(1_200_800, 1_201_300)], label="Peaks")
    sequence.pileup(ax, "ACGT…", [(3, "GTTAC…"), …], at=(1, 4))
    sequence.dotplot(ax, seq_a, seq_b, at=(1, 1), size=5, window=7)
"""

import math

import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path
from matplotlib.textpath import TextPath

from . import palette as P
from .core import FONT, LINE, label

_label = label  # Browser methods take a ``label=`` argument

MONO = "DejaVu Sans Mono"
LOGO_FONT = "DejaVu Sans"

# Clustal conservation groups (strong ":" and weak "." similarity)
STRONG = ("STA", "NEQK", "NHQK", "NDEQ", "QHRK", "MILV", "MILF", "HY", "FYW")
WEAK = ("CSA", "ATV", "SAG", "STNK", "STPA", "SGND", "SNDEQK", "NDEQHK", "NEQHRK", "FVLIM", "HFY")


def residue_colour(ch, scheme="nucleotide"):
    """The scheme colour of a residue (``None`` for gaps and unknown letters)."""
    c = ch.upper()
    if scheme == "nucleotide":
        return P.NUCLEOTIDE.get(c)
    for colour, members in P.AMINO_ACID_CLASS.values():
        if c in members:
            return colour
    return None


def soft(colour, t=0.45):
    """A pastel cell background from a scheme colour; it stays pastel in both themes, so text on it is
    ``P.on_fill()``."""
    return P.mix(colour, "#ffffff", t)


def guess_scheme(seqs):
    letters = set("".join(seqs).upper()) - set("-.N")
    return "nucleotide" if letters <= set("ACGTU") else "protein"


def _cell(ax, x, y, w, h, colour, zorder=5, edge=None):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=colour, edgecolor=edge or "none", lw=0.5 if edge else 0,
                           zorder=zorder))


# ---------------------------------------------------------------------------------------------
# alignment


def column_stats(seqs, scheme):
    """Per column: (consensus residue, identity fraction among all rows, Clustal mark '*', ':', '.' or ' ')."""
    out = []
    n = len(seqs)
    for col in zip(*seqs):
        res = [c.upper() for c in col if c not in "-."]
        if not res:
            out.append(("-", 0.0, " "))
            continue
        vals, counts = np.unique(res, return_counts=True)
        k = int(np.argmax(counts))
        cons, ident = vals[k], counts[k] / n
        s = set(res)
        if len(res) == n and len(s) == 1:
            mark = "*"
        elif scheme == "protein" and len(res) == n and any(s <= set(g) for g in STRONG):
            mark = ":"
        elif scheme == "protein" and len(res) == n and any(s <= set(g) for g in WEAK):
            mark = "."
        else:
            mark = " "
        out.append((cons, ident, mark))
    return out


def alignment(ax, seqs, at=(0.0, 0.0), cell=(0.34, 0.44), scheme="auto", color_by="identity", min_identity=0.5,
              consensus=True, marks=None, conservation=True, ruler=True, start=1, ruler_step=10, highlight=(),
              name_gap=0.25, size="small", bar_height=0.6, bar_token=None, zorder=5):
    """A multiple sequence alignment block, top-left residue cell at ``at`` (its left edge, top edge).

    ``seqs`` is a dict name → aligned sequence (equal lengths, "-" for gaps) or a list of sequences.
    ``color_by`` "identity" colours a residue only if it equals the column consensus and the column
    identity is at least ``min_identity`` (Jalview's percentage identity); "residue" colours every residue.
    Below the rows: the Clustal marks (``marks``; proteins by default: * identical, : strongly similar,
    . weakly similar), the ``consensus`` row and ``conservation`` bars (identity). ``ruler`` numbers columns
    from ``start``. ``highlight=[(first, last, "label")]`` boxes columns (0-based, inclusive).
    Returns a dict with ``x(i)`` (column centre), ``rows`` (y of each row), ``top`` and ``bottom``.
    """
    names = list(seqs) if isinstance(seqs, dict) else [None] * len(seqs)
    rows = list(seqs.values()) if isinstance(seqs, dict) else list(seqs)
    L = len(rows[0])
    if any(len(r) != L for r in rows):
        raise ValueError("aligned sequences must have equal length")
    scheme = guess_scheme(rows) if scheme == "auto" else scheme
    marks = (scheme == "protein") if marks is None else marks
    cw, ch = cell
    x0, ytop = at
    stats = column_stats(rows, scheme)
    fs = FONT.get(size, size)
    cx = [x0 + (i + 0.5) * cw for i in range(L)]
    y = ytop
    geom = {"x": lambda i: x0 + (i + 0.5) * cw, "top": ytop, "left": x0, "right": x0 + L * cw}
    if ruler:
        for i in range(L):
            pos = start + i
            if pos % ruler_step == 0 or i == 0:
                label(ax, (cx[i], y + 0.22), str(pos), size="tiny", color=P.muted(), va="bottom", zorder=zorder)
                ax.plot([cx[i], cx[i]], [y + 0.03, y + 0.17], color=P.muted(), lw=0.7, zorder=zorder)
    ys = []
    for r, (name, seq) in enumerate(zip(names, rows)):
        yc = y - ch * (r + 0.5)
        ys.append(yc)
        if name:
            label(ax, (x0 - name_gap, yc), name, size=size, ha="right", italic=" " in name and name[0].isupper()
                  and name.split()[0][1:].islower(), zorder=zorder)
        for i, c in enumerate(seq):
            cons, ident, _ = stats[i]
            col = residue_colour(c, "nucleotide" if scheme == "nucleotide" else "protein")
            coloured = col is not None and (color_by == "residue" or (c.upper() == cons and ident >= min_identity))
            if coloured:
                _cell(ax, cx[i], yc, cw, ch, soft(col), zorder=zorder)
            ax.text(cx[i], yc, c, fontsize=fs, family=MONO, ha="center", va="center",
                    color=P.on_fill() if coloured else (P.muted() if c in "-." else P.ink()), zorder=zorder + 1)
    y = ytop - ch * len(rows)
    geom["rows"] = ys
    if marks:
        y -= ch * 0.75
        for i in range(L):
            if stats[i][2] != " ":
                ax.text(cx[i], y, stats[i][2], fontsize=fs, family=MONO, ha="center", va="center", color=P.ink(), zorder=zorder + 1)
        y -= ch * 0.25
    if consensus:
        yc = y - ch * 0.7
        label(ax, (x0 - name_gap, yc), "Consensus", size=size, ha="right", bold=True, zorder=zorder)
        for i in range(L):
            cons, ident, _ = stats[i]
            sym = cons if ident >= min_identity else "."
            col = residue_colour(sym, "nucleotide" if scheme == "nucleotide" else "protein") if ident >= min_identity else None
            if col:
                _cell(ax, cx[i], yc, cw, ch, soft(col, 0.2), zorder=zorder)
            ax.text(cx[i], yc, sym, fontsize=fs, family=MONO, weight="bold", ha="center", va="center",
                    color=P.on_fill() if col else P.muted(), zorder=zorder + 1)
        y = yc - ch * 0.5
    if conservation:
        tok = bar_token or ("dna" if scheme == "nucleotide" else "protein")
        yb = y - 0.12 - bar_height
        label(ax, (x0 - name_gap, yb + bar_height / 2), "Identity", size=size, ha="right", color=P.muted(), zorder=zorder)
        ax.plot([x0, x0 + L * cw], [yb, yb], color=P.muted(), lw=0.6, zorder=zorder)
        for i in range(L):
            h = stats[i][1] * bar_height
            if h > 0:
                ax.add_patch(Rectangle((cx[i] - cw * 0.4, yb), cw * 0.8, h, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                       lw=0.5, zorder=zorder))
        y = yb
    for first, last, text in highlight:
        a, b = x0 + first * cw, x0 + (last + 1) * cw
        top, bot = ytop + 0.02, ytop - ch * len(rows) - 0.02
        ax.add_patch(Rectangle((a, bot), b - a, top - bot, fill=False, edgecolor=P.edge("highlight"), lw=1.6, zorder=zorder + 3))
        if text:
            label(ax, ((a + b) / 2, top + (0.62 if ruler else 0.2)), text, size="tiny", bold=True, color=P.edge("highlight"),
                  va="bottom", zorder=zorder + 3)
    geom["bottom"] = y
    return geom


# ---------------------------------------------------------------------------------------------
# sequence logo


def information(matrix, kind="counts", pseudocount=0.0, small_sample=True, background=None):
    """Per-position probabilities and information content (bits) of a counts / probability matrix (L × A)."""
    m = np.asarray(matrix, float)
    A = m.shape[1]
    if kind == "counts":
        n = m.sum(axis=1, keepdims=True)
        p = (m + pseudocount) / (n + pseudocount * A)
    else:
        n = None
        p = m / m.sum(axis=1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        if background is None:
            H = -np.nansum(np.where(p > 0, p * np.log2(p), 0.0), axis=1)
            R = np.log2(A) - H
        else:
            q = np.asarray(background, float)
            R = np.nansum(np.where(p > 0, p * np.log2(p / q), 0.0), axis=1)  # relative entropy
    if small_sample and n is not None:
        R = R - (A - 1) / (2 * math.log(2) * n[:, 0])  # Schneider et al. (1986) correction
    return p, np.clip(R, 0, None)


_glyphs = {}


def _glyph(ch, family=LOGO_FONT):
    key = (ch, family)
    if key not in _glyphs:
        tp = TextPath((0, 0), ch, size=100, prop=FontProperties(family=family, weight="bold"))
        ext = tp.get_extents()
        _glyphs[key] = (tp.vertices.copy(), tp.codes.copy(), ext)
    return _glyphs[key]


def letter(ax, ch, x, y, w, h, colour, zorder=6, family=LOGO_FONT):
    """Draw a letter as a filled glyph stretched into the box (x, y) – (x + w, y + h)."""
    if h <= 1e-4:
        return
    v, c, ext = _glyph(ch, family)
    gw, gh = ext.width, ext.height
    v = (v - [ext.x0, ext.y0]) * [w / gw, h / gh] + [x, y]
    ax.add_patch(PathPatch(Path(v, c), facecolor=colour, edgecolor="none", zorder=zorder))


def logo(ax, matrix, at=(0.0, 0.0), col_width=0.5, height=2.0, alphabet="ACGT", kind="counts", ic=True,
         small_sample=True, pseudocount=0.0, background=None, axis=True, start=1, numbers=True, gap=0.04,
         colours=None, title=None, zorder=6):
    """A sequence logo with its bottom-left corner at ``at``. ``matrix`` is L × len(alphabet) counts
    (``kind="counts"``) or probabilities. With ``ic=True`` each stack is as tall as the information content
    (``height`` units = log2 of the alphabet size: 2 bits for DNA) and letters are scaled by their
    probability, the most frequent on top; ``ic=False`` draws a probability logo (stacks of height 1).
    Returns a dict with ``x(i)``, ``ic`` (bits per position) and ``p``.
    """
    p, R = information(matrix, kind, pseudocount, small_sample, background)
    L, A = p.shape
    maxbits = math.log2(A)
    unit = height / (maxbits if ic else 1.0)
    x0, y0 = at
    scheme = "nucleotide" if set(alphabet) <= set("ACGTU") else "protein"
    for i in range(L):
        stack = p[i] * (R[i] if ic else 1.0)
        order = np.argsort(stack)
        yy = y0
        for k in order:
            h = stack[k] * unit
            col = (colours or {}).get(alphabet[k]) or residue_colour(alphabet[k], scheme) or P.muted()
            letter(ax, alphabet[k], x0 + i * col_width + gap / 2, yy, col_width - gap, h, col, zorder=zorder)
            yy += h
    if axis:
        xa = x0 - 0.12
        ax.plot([xa, xa], [y0, y0 + height], color=P.ink(), lw=0.8, solid_capstyle="butt", zorder=zorder)
        ticks = range(int(maxbits) + 1) if ic else (0, 0.5, 1)
        for t in ticks:
            yt = y0 + t * unit
            ax.plot([xa - 0.08, xa], [yt, yt], color=P.ink(), lw=0.8, zorder=zorder)
            label(ax, (xa - 0.13, yt), f"{t:g}", size="tiny", ha="right", zorder=zorder)
        label(ax, (xa - (0.55 if ic else 0.75), y0 + height / 2), "bits" if ic else "probability", size="small", rotation=90, zorder=zorder)
        ax.plot([x0, x0 + L * col_width], [y0, y0], color=P.ink(), lw=0.8, solid_capstyle="butt", zorder=zorder)
    if numbers:
        for i in range(L):
            label(ax, (x0 + (i + 0.5) * col_width, y0 - 0.2), str(start + i), size="tiny",
                  color=P.muted(), zorder=zorder)
    if title:
        label(ax, (x0 + L * col_width / 2, y0 + height + 0.3), title, size="small", bold=True, zorder=zorder)
    return {"x": lambda i: x0 + (i + 0.5) * col_width, "ic": R, "p": p, "right": x0 + L * col_width}


# ---------------------------------------------------------------------------------------------
# genome browser


def _nice_step(span, target=6):
    raw = span / target
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def nice_ceil(v):
    """Round a data maximum up to 1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8 or 10 × a power of ten (track scales)."""
    if v <= 0:
        return 0.0
    mag = 10 ** math.floor(math.log10(v))
    for m in (1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if v <= m * mag * (1 + 1e-9):
            return float(f"{m * mag:.6g}")
    return 10 * mag


def format_bp(pos, step):
    """'1.25 Mb', '6,532 kb', '820 bp' depending on the tick step."""
    if step >= 100_000:
        dec = max(0, -int(math.floor(math.log10(step / 1e6) + 1e-9)))
        return f"{pos / 1e6:,.{dec}f} Mb"
    if step >= 100:
        dec = max(0, -int(math.floor(math.log10(step / 1e3) + 1e-9)))
        return f"{pos / 1e3:,.{dec}f} kb"
    return f"{pos:,.0f} bp"


class Browser:
    """Genome-browser tracks for a region ``(start, end)`` (bp) mapped onto x0..x1 of the canvas.
    Each method takes the track's baseline ``y``; ``label=`` writes the track name left of x0."""

    def __init__(self, ax, region, x0, x1, chrom=None, label_gap=0.3):
        self.ax = ax
        self.start, self.end = region
        self.x0, self.x1 = x0, x1
        self.chrom = chrom
        self.gap = label_gap

    def x(self, pos):
        return self.x0 + (np.asarray(pos, float) - self.start) / (self.end - self.start) * (self.x1 - self.x0)

    def track_label(self, y, text, size="small", color=None):
        label(self.ax, (self.x0 - self.gap, y), text, size=size, ha="right", color=color or P.ink())

    def axis(self, y, step=None, label_text=True, scale_bar=None):
        """A coordinate ruler with ticks every ``step`` bp (automatic: kb or Mb labels). ``scale_bar=bp``
        draws a scale bar instead, labelled in kb."""
        ax = self.ax
        if scale_bar:
            xb = self.x1 - (self.x(self.start + scale_bar) - self.x0)
            ax.plot([xb, self.x1], [y, y], color=P.ink(), lw=2.0, solid_capstyle="butt")
            label(ax, ((xb + self.x1) / 2, y + 0.2), format_bp(scale_bar, scale_bar), size="tiny", va="bottom")
            if self.chrom:
                self.track_label(y, self.chrom)
            return
        step = step or _nice_step(self.end - self.start)
        ax.plot([self.x0, self.x1], [y, y], color=P.ink(), lw=0.9, solid_capstyle="butt")
        t = math.ceil(self.start / step) * step
        while t <= self.end:
            xt = self.x(t)
            ax.plot([xt, xt], [y, y + 0.12], color=P.ink(), lw=0.9)
            label(ax, (xt, y + 0.2), format_bp(t, step), size="tiny", va="bottom")
            t += step
        if self.chrom and label_text:
            self.track_label(y, self.chrom, color=P.muted())

    def gene(self, y, exons, strand="+", name=None, cds=None, token="dna", height=0.34, italic=True, chevrons=0.55,
             name_pos="above", zorder=8):
        """A gene model: exons as boxes (UTRs thinner, coding exons full height when ``cds=(start, end)``
        is given), introns as a line with chevrons showing the ``strand``, and an arrow at the TSS."""
        ax = self.ax
        exons = sorted(exons)
        a, b = exons[0][0], exons[-1][1]
        ax.plot([self.x(a), self.x(b)], [y, y], color=P.edge(token), lw=LINE * 0.9, zorder=zorder, solid_capstyle="butt")
        sgn = 1 if strand == "+" else -1
        # chevrons on the introns
        for (s0, e0), (s1, e1) in zip(exons[:-1], exons[1:]):
            xa, xb = self.x(e0), self.x(s1)
            k = int((xb - xa) / chevrons)
            for j in range(k):
                xc = xa + (j + 0.5) * (xb - xa) / k
                d = 0.07 * sgn
                ax.plot([xc - d, xc + d, xc - d], [y + 0.07, y, y - 0.07], color=P.edge(token), lw=0.8, zorder=zorder,
                        solid_joinstyle="miter")
        for s, e in exons:
            parts = [(s, e, height * 0.55)]
            if cds:
                c0, c1 = cds
                parts = []
                for u0, u1, hh in ((s, min(e, c0), height * 0.55), (max(s, c0), min(e, c1), height), (max(s, c1), e, height * 0.55)):
                    if u1 > u0:
                        parts.append((u0, u1, hh))
            else:
                parts = [(s, e, height)]
            for u0, u1, hh in parts:
                ax.add_patch(Rectangle((self.x(u0), y - hh / 2), self.x(u1) - self.x(u0), hh, facecolor=P.fill(token),
                                       edgecolor=P.edge(token), lw=0.7, zorder=zorder + 1))
        # TSS arrow
        tss = a if strand == "+" else b
        xt = self.x(tss)
        ax.plot([xt, xt, xt + 0.35 * sgn], [y + height / 2, y + height / 2 + 0.3, y + height / 2 + 0.3], color=P.ink(), lw=0.9,
                zorder=zorder + 2, solid_joinstyle="miter")
        tip = np.array([xt + 0.45 * sgn, y + height / 2 + 0.3])
        ax.add_patch(PathPatch(Path([tip, tip + [-0.12 * sgn, 0.07], tip + [-0.12 * sgn, -0.07], tip], closed=True),
                               facecolor=P.ink(), edgecolor="none", zorder=zorder + 2))
        if name:
            if name_pos == "above":
                label(ax, ((self.x(a) + self.x(b)) / 2, y + height / 2 + 0.3), name, size="small", italic=italic, va="center")
            else:
                label(ax, (self.x(b) + 0.15, y), name, size="small", italic=italic, ha="left")
        return (self.x(a), self.x(b))

    def signal(self, y, height, values, positions=None, token="rna", label=None, ymax=None, scale=True, zorder=6):
        """A filled signal track (coverage, ChIP signal) of ``values`` at ``positions`` (bp; default: evenly over
        the region), baseline ``y``. ``scale`` writes the data range, as genome browsers do: "[0-120]"."""
        ax = self.ax
        v = np.asarray(values, float)
        pos = np.linspace(self.start, self.end, len(v)) if positions is None else np.asarray(positions, float)
        top = ymax or nice_ceil(float(v.max())) or 1.0
        xs = self.x(pos)
        ys = y + np.clip(v / top, 0, 1) * height
        poly = np.vstack([[xs[0], y], np.c_[xs, ys], [xs[-1], y]])
        ax.add_patch(PathPatch(Path(np.vstack([poly, poly[:1]]), closed=True), facecolor=P.fill(token), edgecolor="none", zorder=zorder))
        ax.plot(xs, ys, color=P.edge(token), lw=0.8, zorder=zorder + 0.5)
        ax.plot([self.x0, self.x1], [y, y], color=P.muted(), lw=0.5, zorder=zorder + 0.5)
        if label:
            self.track_label(y + height / 2, label)
        if scale:
            _label(ax, (self.x0 + 0.05, y + height), f"[0-{top:g}]", size="tiny", ha="left", va="top", color=P.muted(), zorder=zorder + 1)
        return xs, ys

    def peaks(self, y, intervals, token="highlight", height=0.22, label=None, scores=None, zorder=7):
        """Called peaks (BED intervals) as boxes; ``scores`` (0..1) shade them from pale to full."""
        ax = self.ax
        for k, (s, e) in enumerate(intervals):
            f = P.fill(token) if scores is None else P.mix(P.fill(token), P.surface(), 0.75 * (1 - scores[k]))
            w = max(self.x(e) - self.x(s), 0.04)
            ax.add_patch(Rectangle((self.x(s), y - height / 2), w, height, facecolor=f, edgecolor=P.edge(token), lw=0.6, zorder=zorder))
        if label:
            self.track_label(y, label)

    def highlight(self, start, end, y0, y1, token="highlight", zorder=1):
        """A pale vertical band across tracks (a region of interest)."""
        self.ax.add_patch(Rectangle((self.x(start), y0), self.x(end) - self.x(start), y1 - y0,
                                    facecolor=P.mix(P.fill(token), P.surface(), 0.78), edgecolor="none", zorder=zorder))


# ---------------------------------------------------------------------------------------------
# read pileup


def _pack(reads):
    rows_end = []
    rows = []
    for r in sorted(range(len(reads)), key=lambda i: reads[i][0]):
        s, seq = reads[r][0], reads[r][1]
        for k, end in enumerate(rows_end):
            if s > end:
                rows_end[k] = s + len(seq)
                rows.append((r, k))
                break
        else:
            rows_end.append(s + len(seq))
            rows.append((r, len(rows_end) - 1))
    return dict(rows), len(rows_end)


def pileup(ax, reference, reads, at=(0.0, 0.0), cell=0.2, row=0.24, ref_start=1, coverage=True, cov_height=0.8,
           letters=None, ruler_step=10, token="neutral", zorder=6):
    """Short reads stacked under a reference, mismatches highlighted in the nucleotide colours.

    ``reads`` are ``(offset, sequence)`` or ``(offset, sequence, strand)`` with 0-based offsets into
    ``reference``; "-" in a read is a deletion. The reference row's top-left corner is ``at``; the
    coverage histogram (``coverage=True``) sits above it. ``letters`` writes every base (default: only
    when a cell is wide enough). Returns a dict with ``x(i)``, ``bottom``, ``depth`` (per position) and
    the per-position mismatch ``alt`` counts.
    """
    x0, ytop = at
    L = len(reference)
    letters = cell >= 0.17 if letters is None else letters
    fs = min(FONT["tiny"], 0.8 * cell * _inches_per_unit(ax) * 72) if letters else 0
    depth = np.zeros(L)
    alt = np.zeros(L)
    for rd in reads:
        s, seq = rd[0], rd[1]
        for j, c in enumerate(seq):
            i = s + j
            if 0 <= i < L and c != "-":
                depth[i] += 1
                alt[i] += c.upper() != reference[i].upper()
    y = ytop
    if coverage:
        top = depth.max() or 1
        yb = y + 0.15
        for i in range(L):
            h = depth[i] / top * cov_height
            ax.add_patch(Rectangle((x0 + i * cell, yb), cell, h, facecolor=P.fill(token), edgecolor="none", zorder=zorder))
            if alt[i] / max(depth[i], 1) >= 0.2:
                ax.add_patch(Rectangle((x0 + i * cell, yb), cell, alt[i] / top * cov_height, facecolor=_alt_colour(reads, reference, i),
                                       edgecolor="none", zorder=zorder + 0.5))
        label(ax, (x0 - 0.25, yb + cov_height / 2), "Coverage", size="small", ha="right")
        label(ax, (x0 + 0.05, yb + cov_height), f"[0-{top:g}]", size="tiny", ha="left", va="top", color=P.muted(), zorder=zorder + 1)
    # reference row
    yr = y - row / 2
    for i, c in enumerate(reference):
        col = residue_colour(c, "nucleotide")
        _cell(ax, x0 + (i + 0.5) * cell, yr, cell, row * 0.9, soft(col, 0.35) if col else P.light(token), zorder=zorder)
        if letters:
            ax.text(x0 + (i + 0.5) * cell, yr, c, fontsize=fs, family=MONO, ha="center", va="center", color=P.on_fill(), zorder=zorder + 1)
        if (ref_start + i) % ruler_step == 0:
            label(ax, (x0 + (i + 0.5) * cell, y + (cov_height + 0.35 if coverage else 0.15)), f"{ref_start + i:,}", size="tiny",
                  color=P.muted(), va="bottom")
    label(ax, (x0 - 0.25, yr), "Reference", size="small", ha="right")
    rows, nrows = _pack(reads)
    y0 = y - row * 1.35
    for r, rd in enumerate(reads):
        s, seq = rd[0], rd[1]
        strand = rd[2] if len(rd) > 2 else "+"
        k = rows[r]
        yc = y0 - k * row - row / 2
        a, b = x0 + s * cell, x0 + (s + len(seq)) * cell
        h = row * 0.72
        tipw = min(cell * 0.9, (b - a) / 4)
        if strand == "+":
            pts = [(a, yc - h / 2), (b - tipw, yc - h / 2), (b, yc), (b - tipw, yc + h / 2), (a, yc + h / 2)]
        else:
            pts = [(a + tipw, yc - h / 2), (b, yc - h / 2), (b, yc + h / 2), (a + tipw, yc + h / 2), (a, yc)]
        # read bodies recede (mixed towards the background) so that mismatches stand out in both themes
        body = P.mix(P.fill(token), P.surface(), 0.2 if strand == "+" else 0.45)
        ax.add_patch(PathPatch(Path(pts + [pts[0]], closed=True), facecolor=body,
                               edgecolor="none", zorder=zorder))
        for j, c in enumerate(seq):
            i = s + j
            if not 0 <= i < L:
                continue
            xc = x0 + (i + 0.5) * cell
            if c == "-":
                ax.add_patch(Rectangle((xc - cell / 2, yc - h / 2), cell, h, facecolor=P.surface(), edgecolor="none", zorder=zorder + 0.3))
                ax.plot([xc - cell / 2, xc + cell / 2], [yc, yc], color=P.ink(), lw=0.8, zorder=zorder + 0.5)
            elif c.upper() != reference[i].upper():
                col = residue_colour(c, "nucleotide") or P.muted()
                _cell(ax, xc, yc, cell, h, col, zorder=zorder + 0.5)
                if letters:
                    ax.text(xc, yc, c, fontsize=fs, family=MONO, weight="bold", ha="center", va="center", color=P.on_fill(), zorder=zorder + 1)
    bottom = y0 - nrows * row
    label(ax, (x0 - 0.25, (y0 + bottom) / 2), "Reads", size="small", ha="right")
    return {"x": lambda i: x0 + (i + 0.5) * cell, "bottom": bottom, "depth": depth, "alt": alt}


def _inches_per_unit(ax):
    fig = ax.figure
    x0, x1 = ax.get_xlim()
    return fig.get_figwidth() * ax.get_position().width / abs(x1 - x0)


def _alt_colour(reads, reference, i):
    counts = {}
    for rd in reads:
        j = i - rd[0]
        if 0 <= j < len(rd[1]):
            c = rd[1][j].upper()
            if c != reference[i].upper() and c != "-":
                counts[c] = counts.get(c, 0) + 1
    if not counts:
        return P.muted()
    return residue_colour(max(counts, key=counts.get), "nucleotide") or P.muted()


# ---------------------------------------------------------------------------------------------
# dot plot

_COMP = str.maketrans("ACGTUacgtu", "TGCAAtgcaa")


def revcomp(seq):
    return seq.translate(_COMP)[::-1]


def dotplot(ax, seq_x, seq_y, at=(0.0, 0.0), size=5.0, window=1, mismatches=0, reverse=False, names=("", ""),
            letters=None, token="dna", rev_token="rna", ticks=None, zorder=6):
    """A dot plot of ``seq_x`` (left to right) against ``seq_y`` (top to bottom), in a square of side ``size``
    with its bottom-left corner at ``at``. A dot marks a window of length ``window`` starting there that
    matches with at most ``mismatches`` differences; ``reverse=True`` also marks reverse-complement
    matches (inverted repeats, DNA) in ``rev_token``. ``letters`` writes the residues along the axes
    (default for sequences up to 40). Returns the match matrix (forward)."""
    nx, ny = len(seq_x), len(seq_y)
    x0, y0 = at
    cw, chh = size / nx, size / ny
    sx, sy = seq_x.upper(), seq_y.upper()

    def matches(a, b):
        A = np.frombuffer(a.encode(), dtype=np.uint8)
        B = np.frombuffer(b.encode(), dtype=np.uint8)
        eq = (A[:, None] == B[None, :]).astype(int)
        if window == 1:
            return eq > 0
        # windowed: count mismatches along diagonals
        out = np.zeros((len(a) - window + 1, len(b) - window + 1), bool)
        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                out[i, j] = window - sum(eq[i + k, j + k] for k in range(window)) <= mismatches
        return out

    fwd = matches(sx, sy)
    ax.add_patch(Rectangle((x0, y0), size, size, facecolor=P.surface(), edgecolor=P.muted(), lw=0.8, zorder=zorder - 1))

    def draw(M, tok, rev):
        for i, j in zip(*np.nonzero(M)):
            if rev:
                # reverse-complement window of seq_y starting at j corresponds to seq_y positions ny-1-j-(window-1)..
                jj = ny - window - j
                ii = i
                xs, ys = ii + (window - 1) / 2, jj + (window - 1) / 2
            else:
                xs, ys = i + (window - 1) / 2, j + (window - 1) / 2
            ax.add_patch(Rectangle((x0 + xs * cw + cw * 0.1, y0 + size - (ys + 1) * chh + chh * 0.1), cw * 0.8, chh * 0.8,
                                   facecolor=P.edge(tok), edgecolor="none", zorder=zorder))

    draw(fwd, token, False)
    if reverse:
        draw(matches(sx, revcomp(sy)), rev_token, True)
    letters = (max(nx, ny) <= 40) if letters is None else letters
    fs = FONT["tiny"]
    if letters:
        for i, c in enumerate(seq_x):
            ax.text(x0 + (i + 0.5) * cw, y0 + size + 0.15, c, fontsize=fs, family=MONO, ha="center", va="bottom", color=P.ink())
        for j, c in enumerate(seq_y):
            ax.text(x0 - 0.12, y0 + size - (j + 0.5) * chh, c, fontsize=fs, family=MONO, ha="right", va="center", color=P.ink())
    off = 0.55 if letters else (0.75 if ticks else 0.25)
    if names[0]:
        label(ax, (x0 + size / 2, y0 + size + (0.55 if letters else 0.25)), names[0], size="small", va="bottom")
    if names[1]:
        label(ax, (x0 - off, y0 + size / 2), names[1], size="small", rotation=90, ha="right")
    if ticks:
        for t in range(0, nx + 1, ticks):
            label(ax, (x0 + t * cw, y0 - 0.15), str(t), size="tiny", color=P.muted(), va="top")
        for t in range(0, ny + 1, ticks):
            label(ax, (x0 - 0.12, y0 + size - t * chh), str(t), size="tiny", color=P.muted(), ha="right")
    return fwd
