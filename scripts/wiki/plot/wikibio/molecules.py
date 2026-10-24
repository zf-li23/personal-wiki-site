"""Nucleic acids, proteins, receptors and small species.

    dna(ax, a, b, style="helix" | "duplex" | "line")    double-stranded DNA from a to b (5'→3' on top strand)
    strand(ax, a, b, token="mrna", wave=0.08)            single-stranded RNA (wavy)
    protein(ax, center, w, h, token, text)               an organic blob (deterministic shape per text)
    receptor(ax, x, y, kind="gpcr" | "rtk" | "channel")  a membrane protein sitting in a membrane at height y
    ion(ax, center, "ca")  /  molecule(ax, center, token, text)
"""

import math
import zlib

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, PathPatch
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label


def _frame(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    return a, u, np.array([-u[1], u[0]]), L


def dna(ax, a, b, style="helix", width=0.42, turns=None, ends=True, token="dna", token2="dna2", zorder=9):
    """Double-stranded DNA from a to b; ``ends`` labels 5'/3' on both strands."""
    a, u, n, L = _frame(a, b)
    if style == "helix":
        turns = turns or max(1, L / 1.6)
        t = np.linspace(0, L, max(60, int(L * 40)))
        ph = 2 * np.pi * turns * t / L
        s1 = a + np.outer(t, u) + np.outer(np.sin(ph) * width / 2, n)
        s2 = a + np.outer(t, u) + np.outer(np.sin(ph + np.pi) * width / 2, n)
        for k in range(int(turns * 10)):
            tt = (k + 0.5) / (turns * 10) * L
            p = 2 * np.pi * turns * tt / L
            if abs(math.cos(p)) < 0.25:
                continue
            y1, y2 = math.sin(p) * width / 2, math.sin(p + math.pi) * width / 2
            c = P.NUCLEOTIDE["ACGT"[k % 4]]
            q1, q2 = a + u * tt + n * y1, a + u * tt + n * y2
            ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color=c, lw=LINE * 1.3, solid_capstyle="butt", zorder=zorder)
        # draw strands front/back: split by depth (cos > 0 is in front)
        for s, tok, off in ((s1, token, 0.0), (s2, token2, np.pi)):
            front = np.cos(ph + off) > 0
            for seg_front in (False, True):
                mask = front == seg_front
                pts = np.where(mask[:, None], s, np.nan)
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok) if seg_front else P.fill(tok), lw=LINE * (2.6 if seg_front else 2.0),
                        solid_capstyle="round", zorder=zorder + (2 if seg_front else -1))
        top, bot = a + n * width / 2, a - n * width / 2
    elif style in ("duplex", "line"):
        gap = width / 2 if style == "duplex" else 0.0
        top, bot = a + n * gap, a - n * gap
        for start, tok in ((top, token), (bot, token2)) if style == "duplex" else ((a, token),):
            end = start + u * L
            ax.plot([start[0], end[0]], [start[1], end[1]], color=P.edge(tok), lw=LINE * 2.0, solid_capstyle="round", zorder=zorder)
        if style == "duplex":
            for k, tt in enumerate(np.arange(0.15, L - 0.1, 0.18)):
                q1, q2 = top + u * tt, bot + u * tt
                ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color=P.NUCLEOTIDE["ACGT"[k % 4]], lw=LINE * 1.2, solid_capstyle="butt", zorder=zorder - 1)
    else:
        raise ValueError(f"unknown dna style {style!r}")
    if ends:
        e = u * 0.28
        label(ax, top - e + n * 0.12, "5′", size="tiny")
        label(ax, top + u * L + e + n * 0.12, "3′", size="tiny")
        if style != "line":
            label(ax, bot - e - n * 0.12, "3′", size="tiny")
            label(ax, bot + u * L + e - n * 0.12, "5′", size="tiny")


def strand(ax, a, b, token="mrna", wave=0.08, waves=None, ends=True, cap=False, polya=False, zorder=9):
    """A single-stranded nucleic acid (mRNA by default) as a gentle wave from a (5′) to b (3′)."""
    a, u, n, L = _frame(a, b)
    waves = waves or max(2, L / 0.9)
    t = np.linspace(0, L, max(60, int(L * 40)))
    pts = a + np.outer(t, u) + np.outer(wave * np.sin(2 * np.pi * waves * t / L), n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(token), lw=LINE * 2.0, solid_capstyle="round", zorder=zorder)
    if cap:
        ax.add_patch(Circle(a - u * 0.1, 0.09, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=zorder + 1))
    if polya:
        label(ax, a + u * L + u * 0.45, "AAAA", size="tiny", color=P.edge(token))
    if ends:
        label(ax, a - u * (0.32 if not cap else 0.45) + n * 0.15, "5′", size="tiny")
        if not polya:
            label(ax, a + u * L + u * 0.28 + n * 0.15, "3′", size="tiny")
    return pts


def protein(ax, center, w, h, token="protein", text=None, size="small", wobble=0.1, angle=0.0, italic=False, zorder=12):
    """A protein as a soft organic blob; the outline is deterministic for a given ``text``."""
    seed = zlib.crc32((text or token).encode()) % 10_000
    o = blob(center, w / 2, h / 2, wobble=wobble, seed=seed, k=8, angle=math.radians(angle))
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=zorder))
    hl = blob((center[0] - w * 0.12, center[1] + h * 0.14), w * 0.22, h * 0.14, wobble=0.05, seed=seed + 1, k=6)
    ax.add_patch(PathPatch(Path(hl, closed=True), facecolor=P.light(token), edgecolor="none", alpha=0.6, zorder=zorder + 0.5))
    if text:
        label(ax, center, text, size=size, italic=italic, color=P.on_fill(), zorder=zorder + 1)
    return o


def domains(ax, x, y, parts, height=0.35, zorder=12):
    """A protein drawn as a row of domains: ``parts=[("SH2", 1.2, "receptor"), ("kinase", 2.0, "enzyme")]``."""
    cx = x
    for name, length, token in parts:
        ax.add_patch(FancyBboxPatch((cx, y - height / 2), length, height, boxstyle=f"round,pad=0,rounding_size={height * 0.45}",
                                    facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
        label(ax, (cx + length / 2, y), name, size="tiny", color=P.on_fill(), zorder=zorder + 1)
        cx += length + 0.05
    return cx


def receptor(ax, x, y, kind="gpcr", token=None, membrane_half=0.37, text=None, zorder=11):
    """A membrane protein centred at (x, y) in a membrane of half-thickness ``membrane_half``.

    gpcr: seven transmembrane helices; rtk: one helix with extracellular and kinase domains;
    channel: two subunits around a pore.
    """
    tok = token or {"gpcr": "receptor", "rtk": "enzyme", "channel": "channel"}[kind]
    mh = membrane_half
    if kind == "gpcr":
        for i in range(7):
            xx = x + (i - 3) * 0.17
            ax.add_patch(FancyBboxPatch((xx - 0.07, y - mh - 0.05), 0.14, 2 * mh + 0.1, boxstyle="round,pad=0,rounding_size=0.06",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.7, zorder=zorder))
        for i in range(6):
            x0, x1 = x + (i - 3) * 0.17, x + (i - 2) * 0.17
            yy = y + (mh + 0.05) * (1 if i % 2 else -1)
            t = np.linspace(0, np.pi, 20)
            ax.plot(np.linspace(x0, x1, 20), yy + np.sign(yy - y) * 0.09 * np.sin(t), color=P.edge(tok), lw=LINE * 0.9, zorder=zorder)
    elif kind == "rtk":
        ax.add_patch(FancyBboxPatch((x - 0.06, y - mh - 0.04), 0.12, 2 * mh + 0.08, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.7, zorder=zorder))
        protein(ax, (x, y + mh + 0.45), 0.55, 0.75, tok, wobble=0.06, zorder=zorder)
        protein(ax, (x, y - mh - 0.42), 0.6, 0.6, tok, wobble=0.06, zorder=zorder)
    elif kind == "channel":
        for side in (-1, 1):
            ax.add_patch(FancyBboxPatch((x + side * 0.22 - 0.15, y - mh - 0.12), 0.3, 2 * mh + 0.24, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, zorder=zorder))
    else:
        raise ValueError(f"unknown receptor kind {kind!r}")
    if text:
        label(ax, (x, y - mh - (1.05 if kind == "rtk" else 0.38)), text, size="small")


ION_TEXT = {"ca": "Ca²⁺", "na": "Na⁺", "k": "K⁺", "cl": "Cl⁻", "h": "H⁺", "mg": "Mg²⁺"}


def ion(ax, center, kind, r=0.2, text=True, zorder=13):
    """An ion as a small disc (ca, na, k, cl, h, mg); its symbol is written beside it (``text=False`` to omit)."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(kind), edgecolor=P.edge(kind), lw=0.8, zorder=zorder))
    if text:
        label(ax, (center[0] + r + 0.05, center[1]), ION_TEXT[kind], size="tiny", ha="left", zorder=zorder + 1)


def molecule(ax, center, token="metabolite", text=None, r=0.2, size="tiny", zorder=13):
    """A small molecule (SBGN 'simple chemical'): a disc, optionally labelled inside."""
    ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=zorder))
    if text:
        label(ax, center, text, size=size, color=P.on_fill(), zorder=zorder + 1)
