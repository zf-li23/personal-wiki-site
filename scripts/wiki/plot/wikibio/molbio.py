"""Molecular biology scenes: nucleic-acid ladders, transcription bubble, tRNA, ribosome, replication machinery.

Nucleic acids are drawn as backbones (thick lines in the strand's token) with bases as short ticks
coloured by ``P.NUCLEOTIDE``; paired bases meet half-way (``ladder``), unpaired ones are stubs.

    top = molbio.track(x, y)                                   a polyline as an (n, 2) array
    molbio.backbone(ax, top, "dna")                            the sugar-phosphate backbone
    molbio.ladder(ax, top, bottom, "ACGT…")                    base pairs between two strands
    molbio.stubs(ax, pts, direction, "ACGU…")                  unpaired bases
    molbio.bubble_profile(x, x0, x1, h)                        smooth opening of a duplex (for bubbles, forks)
    molbio.polymerase(ax, center, w, h, "enzyme", "RNA polymerase")
    molbio.trna(ax, (x, y), "CGU", aa="Ala")                    tRNA standing on its anticodon
    molbio.ribosome(ax, center, width)                          sectioned ribosome; returns E/P/A site x positions
    molbio.codons(ax, x0, y, "AUGGCU…")                         an mRNA as coloured base boxes
    molbio.peptide(ax, points, ["Met", "Ala"])                  a chain of amino-acid beads
    molbio.helicase / clamp / ssb                               replication proteins
    molbio.central_dogma(ax, (x, y))                            DNA -> RNA -> protein summary

Strand polarity is the caller's responsibility: label 5′ and 3′ with ``end_labels``.
"""

import math
import zlib

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, arrow, blob, label, smooth_closed

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G", "U": "A", "N": "N"}
RNA_COMPLEMENT = {"A": "U", "T": "A", "U": "A", "G": "C", "C": "G", "N": "N"}


def sequence(n, seed="seq", alphabet="ACGT"):
    """A deterministic pseudo-random sequence of length n (seeded by a string)."""
    rng = np.random.default_rng(zlib.crc32(seed.encode()))
    return "".join(rng.choice(list(alphabet), n))


def complement(seq, rna=False):
    """Base-wise complement (not reversed): position i pairs with position i."""
    table = RNA_COMPLEMENT if rna else COMPLEMENT
    return "".join(table[c] for c in seq)


def track(x, y):
    """Stack x and y samples into an (n, 2) point array."""
    x = np.asarray(x, float)
    y = np.broadcast_to(np.asarray(y, float), x.shape)
    return np.c_[x, y]


def bubble_profile(x, x0, x1, h, ramp=0.7):
    """Displacement h inside [x0, x1] with smooth cosine ramps of length ``ramp`` at both ends, 0 outside."""
    x = np.asarray(x, float)
    up = np.clip((x - x0) / ramp, 0, 1)
    down = np.clip((x1 - x) / ramp, 0, 1)
    w = np.minimum(up, down)
    return h * (0.5 - 0.5 * np.cos(np.pi * w))


def backbone(ax, pts, token="dna", lw=LINE * 2.2, zorder=10, dashed=False, shade="edge"):
    """A strand's sugar-phosphate backbone along points; ``shade="fill"`` uses the lighter fill colour
    (e.g. newly made DNA next to the parental strands)."""
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=P.edge(token) if shade == "edge" else P.fill(token), lw=lw, solid_capstyle="round", solid_joinstyle="round",
            ls=(0, (3, 2)) if dashed else "-", zorder=zorder)


def _resample(pts, spacing):
    p = np.asarray(pts, float)
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    t = np.arange(spacing / 2, s[-1], spacing)
    return np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])], t


def ladder(ax, a, b, seq_a, seq_b=None, lw=LINE * 1.25, zorder=9):
    """Base pairs between corresponding points of two strands: each half tick in its base's colour.

    ``a`` and ``b`` are equal-length point arrays (the base positions); ``seq_b`` defaults to the
    complement of ``seq_a``.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    seq_b = seq_b or complement(seq_a)
    for i, (p, q) in enumerate(zip(a, b)):
        m = (p + q) / 2
        ca = P.NUCLEOTIDE.get(seq_a[i % len(seq_a)], P.NUCLEOTIDE["N"])
        cb = P.NUCLEOTIDE.get(seq_b[i % len(seq_b)], P.NUCLEOTIDE["N"])
        ax.plot([p[0], m[0]], [p[1], m[1]], color=ca, lw=lw, solid_capstyle="butt", zorder=zorder)
        ax.plot([m[0], q[0]], [m[1], q[1]], color=cb, lw=lw, solid_capstyle="butt", zorder=zorder)


def stubs(ax, pts, direction, seq, length=0.17, lw=LINE * 1.25, zorder=9):
    """Unpaired bases: ticks of ``length`` from each point towards ``direction`` (a vector or per-point array)."""
    p = np.asarray(pts, float)
    d = np.asarray(direction, float)
    if d.ndim == 1:
        d = np.broadcast_to(d, p.shape)
    d = d / np.linalg.norm(d, axis=1)[:, None]
    for i, (q, v) in enumerate(zip(p, d)):
        ax.plot([q[0], q[0] + v[0] * length], [q[1], q[1] + v[1] * length],
                color=P.NUCLEOTIDE.get(seq[i % len(seq)], P.NUCLEOTIDE["N"]), lw=lw, solid_capstyle="butt", zorder=zorder)


def sample(pts, spacing=0.17):
    """Evenly spaced base positions along a polyline (returns points and their arc-length positions)."""
    return _resample(pts, spacing)


def end_labels(ax, pts, start="5′", end="3′", offset=0.28, size="tiny", color=None):
    """Polarity labels just beyond both ends of a strand (``None`` skips one)."""
    p = np.asarray(pts, float)
    for text, q, r in ((start, p[0], p[min(3, len(p) - 1)]), (end, p[-1], p[max(-4, -len(p))])):
        if text:
            d = q - r
            d = d / (np.linalg.norm(d) or 1)
            label(ax, q + d * offset, text, size=size, color=color, bold=True)


def wavy(a_pts, amplitude=0.07, wavelength=0.55):
    """A gently waving copy of a polyline (single-stranded RNA look)."""
    p = np.asarray(a_pts, float)
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    t = np.linspace(0, s[-1], max(40, int(s[-1] * 40)))
    q = np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])]
    d = np.gradient(q, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    n = np.c_[-d[:, 1], d[:, 0]]
    fade = np.clip(t / 0.4, 0, 1) * np.clip((t[-1] - t) / 0.4, 0, 1)
    return q + n * (amplitude * np.sin(2 * np.pi * t / wavelength) * fade)[:, None]


# ---------------------------------------------------------------------------------------------
# proteins and complexes


def polymerase(ax, center, w, h, token="enzyme", text=None, alpha=0.9, seed=None, size="small", text_at=None, zorder=5):
    """A large polymerase (or any big complex) as a soft blob, drawn behind the nucleic acids it holds."""
    s = zlib.crc32((seed or text or token).encode()) % 10_000
    o = blob(center, w / 2, h / 2, wobble=0.06, seed=s, k=9)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE,
                           alpha=alpha if alpha < 0.999 else None, zorder=zorder))
    hl = blob((center[0] - w * 0.27, center[1] + h * 0.3), w * 0.12, h * 0.06, wobble=0.05, seed=s + 1, k=7, angle=0.5)
    ax.add_patch(PathPatch(Path(hl, closed=True), facecolor=P.light(token), edgecolor="none", alpha=0.45, zorder=zorder + 0.1))
    if text:
        label(ax, text_at or (center[0], center[1] + h * 0.33), text, size=size, color=P.on_fill(), bold=True, zorder=zorder + 0.2)
    return o


def helicase(ax, center, h=1.0, w=0.55, token="positive", text=None, angle=0.0, zorder=14):
    """A ring helicase (hexamer) seen from the side: two lobes above and below the strand it encircles."""
    x, y = center
    th = math.radians(angle)
    n = np.array([-math.sin(th), math.cos(th)])
    for k, side in enumerate((1, -1)):
        c = np.array([x, y]) + n * side * h * 0.3
        for j in range(3):
            off = (j - 1) * w * 0.3
            u = np.array([math.cos(th), math.sin(th)])
            q = c + u * off
            ax.add_patch(Ellipse(q, w * 0.42, h * 0.42, angle=angle, facecolor=P.fill(token) if j != 1 else P.light(token),
                                 edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder - (0.5 if side < 0 else -0.5)))
    if text:
        label(ax, (x, y + h * 0.75), text, size="tiny", bold=True)


def clamp(ax, center, h=0.62, w=0.32, token="antibody", zorder=13):
    """A sliding clamp (β clamp / PCNA) around the duplex: a ring seen edge-on (two halves)."""
    x, y = center
    for side, z in ((1, zorder - 2), (-1, zorder + 0.5)):
        ax.add_patch(Ellipse((x, y + side * h * 0.28), w, h * 0.42, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.8, zorder=z))


def ssb(ax, pts, token="neutral", r=0.13, every=2, zorder=12):
    """Single-strand binding proteins coating a stretch of single-stranded DNA."""
    for q in np.asarray(pts, float)[::every]:
        ax.add_patch(Circle(q, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder))


def enzyme(ax, center, w, h, token, text, size="tiny", zorder=13, alpha=1.0):
    """A small labelled enzyme blob (ligase, primase, …); text sits inside."""
    s = zlib.crc32(text.encode()) % 10_000
    o = blob(center, w / 2, h / 2, wobble=0.08, seed=s, k=8)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9,
                           alpha=alpha if alpha < 0.999 else None, zorder=zorder))
    label(ax, center, text, size=size, color=P.on_fill(), bold=True, zorder=zorder + 0.5)
    return o


# ---------------------------------------------------------------------------------------------
# translation


def codons(ax, x0, y, seq, dx=0.36, h=0.34, codon_gap=0.0, letters=True, zorder=11):
    """An mRNA drawn as coloured base boxes from 5′ (x0) rightwards; returns the box centre x positions."""
    xs = []
    for i, b in enumerate(seq):
        x = x0 + i * dx + (i // 3) * codon_gap
        xs.append(x)
        ax.add_patch(FancyBboxPatch((x - dx * 0.44, y - h / 2), dx * 0.88, h, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.NUCLEOTIDE.get(b, P.NUCLEOTIDE["N"]), edgecolor="none", zorder=zorder))
        if letters:
            label(ax, (x, y), b, size="tiny", color=P.on_fill(), bold=True, zorder=zorder + 1)
    return np.array(xs)


def trna(ax, at, anticodon, aa=None, dx=0.36, height=2.3, token="trna", aa_tok=None, charged=True, zorder=14):
    """A tRNA standing on its anticodon: ``at`` = (x, y) of the anticodon's centre (its bottom row of bases).

    ``anticodon`` is written 3′→5′ from left to right, so letter k sits on top of codon base k.
    The acceptor stem ends at the top right in the CCA 3′ end; ``aa`` adds an amino-acid bead there
    (coloured by side-chain class unless ``aa_tok`` is given). ``dx`` must match the codon spacing.
    Returns the point of the 3′ end (where the amino acid or peptide is attached).
    """
    x, y = at
    w = dx * 3
    # anticodon loop with the three bases
    for k, b in enumerate(anticodon):
        bx = x + (k - 1) * dx
        ax.add_patch(FancyBboxPatch((bx - dx * 0.44, y - 0.17), dx * 0.88, 0.34, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.NUCLEOTIDE.get(b, P.NUCLEOTIDE["N"]), edgecolor="none", zorder=zorder + 1))
        label(ax, (bx, y), b, size="tiny", color=P.on_fill(), bold=True, zorder=zorder + 2)
    H = height
    # cloverleaf silhouette: anticodon arm, central body with D (left) and T (right) arms, acceptor stem
    pts = [(-w * 0.5, 0.22), (-w * 0.14, 0.34), (-w * 0.13, H * 0.4), (-w * 0.46, H * 0.44), (-w * 0.48, H * 0.6),
           (-w * 0.16, H * 0.6), (-w * 0.1, H * 0.98), (w * 0.1, H * 1.0), (w * 0.15, H * 0.64), (w * 0.46, H * 0.66),
           (w * 0.48, H * 0.48), (w * 0.14, H * 0.42), (w * 0.14, 0.34), (w * 0.5, 0.22), (w * 0.5, 0.05), (-w * 0.5, 0.05)]
    o = smooth_closed(np.array(pts) + [x, y + 0.1], n=240)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    hl = blob((x - w * 0.03, y + H * 0.78), w * 0.05, H * 0.12, wobble=0.04, seed=3, k=6)
    ax.add_patch(PathPatch(Path(hl, closed=True), facecolor=P.light(token), edgecolor="none", alpha=0.6, zorder=zorder + 0.1))
    # CCA 3' end
    tip = np.array([x + w * 0.05, y + 0.1 + H * 1.0])
    end = tip + np.array([0.12, 0.22])
    ax.plot([tip[0], end[0]], [tip[1], end[1]], color=P.edge(token), lw=LINE * 1.6, solid_capstyle="round", zorder=zorder)
    if aa and charged:
        tok = aa_tok or aa_token(aa)
        ax.add_patch(Circle(end + (0.05, 0.25), 0.26, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder + 1))
        label(ax, end + (0.05, 0.25), aa, size=5.6, color=P.on_fill(), bold=True, zorder=zorder + 2)
        return end + (0.05, 0.25)
    return end


AA_TOKEN = {"hydrophobic": "channel", "polar": "positive", "positive": "negative", "negative": "metabolite"}
_THREE = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E", "Gly": "G", "His": "H",
          "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F", "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W",
          "Tyr": "Y", "Val": "V"}
# side-chain class per residue, from the site-wide table in palette
AA_CLASS = {three: cls for three, one in _THREE.items() for cls, (_, members) in P.AMINO_ACID_CLASS.items() if one in members}


def aa_token(name):
    """Token for an amino acid by its side-chain class (as in ``P.AMINO_ACID_CLASS``)."""
    return AA_TOKEN[AA_CLASS.get(name, "polar")]


def peptide(ax, points, names, r=0.26, zorder=15):
    """A peptide as beads (N-terminus first) placed along a polyline from its N end to the last residue."""
    p = np.asarray(points, float)
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    n = len(names)
    t = np.linspace(0, s[-1], n) if n > 1 else np.array([0.0])
    centres = np.c_[np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])]
    ax.plot(centres[:, 0], centres[:, 1], color=P.muted(), lw=LINE, zorder=zorder - 0.5)
    for c, name in zip(centres, names):
        tok = aa_token(name)
        ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder))
        label(ax, c, name, size=5.6, color=P.on_fill(), bold=True, zorder=zorder + 1)
    return centres


def ribosome(ax, center, width=6.0, height=None, token="rrna", zorder=4):
    """A ribosome in section with the mRNA running between the subunits at height center[1].

    ``height`` is the height of the large subunit above the mRNA (default 0.57 × width).
    Returns a dict: ``sites`` {"E", "P", "A"} -> x of each site's middle codon base (spaced
    width / 5, so width = 15 × base spacing puts one codon per site), ``top`` (y of the large
    subunit's top) and ``bottom`` (y of the small subunit's bottom). Sites run 5′→3′ as E, P, A.
    """
    x, y = center
    w = width
    hl = height or w * 0.57
    large = smooth_closed(np.array([(-0.5, 0.12), (-0.47, 0.62), (-0.32, 0.93), (0.0, 1.0), (0.32, 0.93), (0.48, 0.66),
                                    (0.5, 0.12), (0.25, 0.08), (-0.25, 0.08)]) * [w, hl] + [x, y])
    hs = w * 0.2
    small = smooth_closed(np.array([(-0.42, -0.1), (-0.38, -0.62), (-0.15, -0.95), (0.15, -0.95), (0.38, -0.62),
                                    (0.42, -0.1), (0.15, -0.06), (-0.15, -0.06)]) * [w, hs] + [x, y])
    ax.add_patch(PathPatch(Path(small, closed=True), facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE, zorder=zorder))
    ax.add_patch(PathPatch(Path(large, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=zorder))
    return {"sites": {"E": x - w * 0.2, "P": x, "A": x + w * 0.2}, "top": y + hl, "bottom": y - hs * 0.95}


# ---------------------------------------------------------------------------------------------
# summary diagram


def central_dogma(ax, at, gap=3.6, h=0.62, size="normal", reverse=True):
    """The central dogma: DNA -> RNA -> protein with replication and (dashed) reverse transcription."""
    x, y = at
    nodes = [("DNA", "dna"), ("RNA", "rna"), ("Protein", "protein")]
    xs = [x + i * gap for i in range(3)]
    for (t, tok), xx in zip(nodes, xs):
        ax.add_patch(FancyBboxPatch((xx - 0.85, y - h / 2), 1.7, h, boxstyle=f"round,pad=0,rounding_size={h / 2}",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE, zorder=10))
        label(ax, (xx, y), t, size=size, bold=True, color=P.on_fill(), zorder=11)
    for (a, b), t in (((xs[0], xs[1]), "Transcription"), ((xs[1], xs[2]), "Translation")):
        arrow(ax, (a + 0.95, y), (b - 0.95, y), kind="process")
        label(ax, ((a + b) / 2, y + 0.3), t, size="small", va="bottom")
    # replication: a loop above DNA
    t = np.linspace(math.radians(210), math.radians(-30), 60)
    cx, cy, r = xs[0], y + h / 2 + 0.38, 0.42
    loop = np.c_[cx + r * np.cos(t) * 1.4, cy + r * np.sin(t)]
    ax.plot(loop[:-4, 0], loop[:-4, 1], color=P.ink(), lw=LINE, zorder=9)
    arrow(ax, loop[-6], loop[-1], kind="process", head=0.2)
    label(ax, (cx, cy + r + 0.12), "Replication", size="small", va="bottom")
    if reverse:
        arrow(ax, (xs[1] - 0.6, y - h / 2 - 0.05), (xs[0] + 0.6, y - h / 2 - 0.05), kind="process", bend=0.2, dashed=True,
              color=P.muted())
        label(ax, ((xs[0] + xs[1]) / 2, y - h / 2 - 0.62), "Reverse transcription", size="small", color=P.muted(), va="top")
    return xs
