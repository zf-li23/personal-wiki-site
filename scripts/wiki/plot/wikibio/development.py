"""Developmental biology figures: morphogen gradients, rows of cells with fates, early embryos, Drosophila embryos.

    gradient(x, c0, lam)                        exponential profile c0 exp(-x / lam) (synthesis-diffusion-degradation)
    boundaries(c0, lam, thresholds)             positions where the profile crosses each threshold
    cell_row(ax, x0, x1, y, fates, tokens)      a row of epithelial cells coloured by fate
    embryo(ax, center, r, stage)                zygote, 2-cell, 4-cell, 8-cell, morula, blastocyst (with zona pellucida)
    fly = FlyEmbryo(ax, center, length, height) a Drosophila embryo outline (anterior left); expression patterns with
        fly.domain(a, b, token), fly.stripes(centres, width, token), fly.gradient(func, token),
        fly.gradients([(func, token), …]) in fractions of egg length
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob


def gradient(x, c0=1.0, lam=0.2):
    """Steady state of synthesis at x = 0, diffusion D and first-order decay k: c0 exp(-x / lam), lam = sqrt(D / k)."""
    return c0 * np.exp(-np.asarray(x, float) / lam)


def boundaries(c0, lam, thresholds):
    """x at which c0 exp(-x / lam) equals each threshold: lam ln(c0 / T)."""
    return [lam * math.log(c0 / t) for t in thresholds]


def cell_row(ax, x0, x1, y, fates, tokens, h=0.7, gap=0.06, nuclei=True, dashed=False, zorder=8):
    """A row of len(fates) cells between x0 and x1; ``fates`` index into ``tokens``. Returns the cell centres."""
    n = len(fates)
    w = (x1 - x0) / n
    out = []
    for i, f in enumerate(fates):
        cx = x0 + (i + 0.5) * w
        tok = tokens[f]
        ax.add_patch(FancyBboxPatch((cx - w / 2 + gap / 2, y - h / 2), w - gap, h, boxstyle=f"round,pad=0,rounding_size={min(w, h) * 0.25}",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LINE * 0.8, ls=(0, (3, 2)) if dashed else "-",
                                    zorder=zorder))
        if nuclei:
            ax.add_patch(Circle((cx, y), min(w, h) * 0.17, facecolor=P.edge(tok), edgecolor="none", zorder=zorder + 0.5))
        out.append((cx, y))
    return out


def _zona(ax, center, r, zorder):
    zona = P.mix(P.fill("bone"), P.surface(), 0.45 if P.is_dark() else 0.3)
    ax.add_patch(Circle(center, r * 1.14, facecolor=zona, edgecolor=P.edge("bone"), lw=LINE * 0.9, zorder=zorder))
    ax.add_patch(Circle(center, r * 1.02, facecolor=P.fill("extracellular"), edgecolor=P.edge("bone"), lw=LINE * 0.6, zorder=zorder + 0.1))


def _cell(ax, xy, rx, ry, token, zorder, angle=0.0, nucleus=True, seed=0):
    o = blob(xy, rx, ry, wobble=0.03, seed=seed, k=8, angle=angle)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 0.9, zorder=zorder))
    if nucleus:
        ax.add_patch(Circle(xy, min(rx, ry) * 0.28, facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE * 0.6, zorder=zorder + 0.1))


def embryo(ax, center, r=1.0, stage="zygote", token="animal", icm="positive", troph="receptor", zorder=8):
    """An early mammalian embryo inside its zona pellucida.

    stage: "zygote" (two pronuclei, two polar bodies), "2-cell", "4-cell", "8-cell", "morula" (compacted),
    "blastocyst" (trophectoderm around the blastocoel, inner cell mass at one pole).
    Returns the centre of the inner cell mass for a blastocyst, else ``center``.
    """
    x, y = center
    _zona(ax, center, r, zorder)
    z = zorder + 1
    if stage == "zygote":
        ax.add_patch(Circle(center, r * 0.95, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=z))
        for dx in (-0.25, 0.25):
            ax.add_patch(Circle((x + dx * r, y), r * 0.2, facecolor=P.light("nucleolus"), edgecolor=P.edge("nucleolus"), lw=LINE * 0.8, zorder=z + 1))
        for k, a in enumerate((70, 95)):
            t = math.radians(a)
            ax.add_patch(Circle((x + r * 1.0 * math.cos(t), y + r * 1.0 * math.sin(t) - 0.02), r * 0.09, facecolor=P.fill(token),
                                edgecolor=P.edge(token), lw=LINE * 0.6, zorder=z + 0.5))
        return center
    if stage in ("2-cell", "4-cell", "8-cell"):
        n = int(stage[0])
        if n == 2:
            pos, rr = [(-0.47, 0), (0.47, 0)], (0.48, 0.62)
        elif n == 4:
            pos, rr = [(-0.42, 0.4), (0.42, 0.4), (-0.42, -0.4), (0.42, -0.4)], (0.44, 0.44)
        else:
            pos = [(0.62 * math.cos(math.radians(a)), 0.62 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
            pos += [(-0.16, 0.08), (0.18, -0.1)]
            rr = (0.34, 0.34)
        for k, (dx, dy) in enumerate(pos):
            _cell(ax, (x + dx * r, y + dy * r), rr[0] * r, rr[1] * r, token, z + (0.2 if k >= 6 else 0), seed=k)
        return center
    if stage == "morula":
        ax.add_patch(Circle(center, r * 0.93, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, zorder=z))
        # compacted blastomeres: faint cell outlines, flattened against each other
        pts = [(0, 0)] + [(0.45 * math.cos(math.radians(a)), 0.45 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
        pts += [(0.78 * math.cos(math.radians(a + 15)), 0.78 * math.sin(math.radians(a + 15))) for a in range(0, 360, 36)]
        for k, (dx, dy) in enumerate(pts):
            ax.add_patch(Circle((x + dx * r, y + dy * r), r * 0.07, facecolor=P.light(token), edgecolor=P.edge(token), lw=0.5, zorder=z + 0.2))
        ax.add_patch(Circle(center, r * 0.93, facecolor="none", edgecolor=P.edge(token), lw=LINE, zorder=z + 0.3))
        return center
    if stage == "blastocyst":
        # trophectoderm: a ring of flattened cells; blastocoel inside; inner cell mass at the top pole
        ax.add_patch(Circle(center, r * 0.95, facecolor=P.fill(troph), edgecolor=P.edge(troph), lw=LINE, zorder=z))
        ax.add_patch(Circle(center, r * 0.8, facecolor=P.fill("vacuole"), edgecolor=P.edge(troph), lw=LINE * 0.8, zorder=z + 0.1))
        for a in range(0, 360, 30):
            t = math.radians(a)
            p, q = (x + r * 0.8 * math.cos(t), y + r * 0.8 * math.sin(t)), (x + r * 0.95 * math.cos(t), y + r * 0.95 * math.sin(t))
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(troph), lw=LINE * 0.6, zorder=z + 0.2)
        c = (x, y + r * 0.45)
        o = blob(c, r * 0.48, r * 0.3, wobble=0.05, seed=9, k=8)
        ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(icm), edgecolor=P.edge(icm), lw=LINE * 0.9, zorder=z + 0.3))
        for dx in (-0.22, 0.0, 0.22):
            ax.add_patch(Circle((c[0] + dx * r, c[1] - 0.02 * r), r * 0.06, facecolor=P.edge(icm), edgecolor="none", zorder=z + 0.4))
        return c
    raise ValueError(f"unknown stage {stage!r}")


class FlyEmbryo:
    """A Drosophila embryo (lateral view, anterior left, dorsal up) for gene-expression patterns.

    Positions are fractions of egg length from the anterior pole (0 = anterior, 1 = posterior).
    """

    def __init__(self, ax, center, length=6.0, height=2.2, token="animal", zorder=8):
        self.ax, self.center, self.L, self.H, self.z = ax, np.asarray(center, float), length, height, zorder
        t = np.linspace(0, 2 * np.pi, 240)
        # slightly egg-shaped: flatter dorsal side, fuller posterior
        xs = length / 2 * np.cos(t)
        ys = height / 2 * np.sin(t) * (1 - 0.08 * np.sin(t)) * (1 + 0.06 * np.cos(t))
        self.outline = np.c_[xs, ys] + self.center
        self.clip = PathPatch(Path(self.outline, closed=True), transform=ax.transData, facecolor="none", edgecolor="none")
        ax.add_patch(self.clip)
        ax.add_patch(PathPatch(Path(self.outline, closed=True), facecolor=P.light(token), edgecolor="none", zorder=zorder))
        self.edge = PathPatch(Path(self.outline, closed=True), facecolor="none", edgecolor=P.edge(token), lw=LINE, zorder=zorder + 3)
        ax.add_patch(self.edge)

    def x(self, f):
        """Canvas x of a position given as a fraction of egg length."""
        return self.center[0] - self.L / 2 + f * self.L

    def _band(self, a, b, token, alpha=1.0, fill=None):
        x0, x1 = self.x(a), self.x(b)
        y0, y1 = self.center[1] - self.H, self.center[1] + self.H
        p = Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], closed=True, facecolor=fill or P.fill(token), edgecolor="none",
                    alpha=alpha if alpha < 0.999 else None, zorder=self.z + 1)
        self.ax.add_patch(p)
        p.set_clip_path(self.clip)
        return p

    def domain(self, a, b, token, soft=0.0):
        """An expression domain from a to b (fractions); ``soft`` > 0 fades its edges over that width."""
        if soft <= 0:
            return self._band(a, b, token)
        n = 8
        for k in range(n):
            t = (k + 0.5) / n
            self._band(a - soft + soft * k / n, a - soft + soft * (k + 1) / n, token, fill=P.mix(P.light(token), P.fill(token), t))
            self._band(b + soft - soft * (k + 1) / n, b + soft - soft * k / n, token, fill=P.mix(P.light(token), P.fill(token), t))
        return self._band(a, b, token)

    def stripes(self, centres, width, token):
        """Narrow stripes (pair-rule, segment polarity) centred at the given fractions."""
        for c in centres:
            self._band(c - width / 2, c + width / 2, token)

    def gradient(self, func, token, n=80, floor=0.03):
        """A graded pattern: func(f) in 0..1 mixes the embryo's base tint towards the token's colour.

        Bands where func < ``floor`` are left out, so several gradients can share one embryo.
        """
        self.gradients([(func, token)], n=n, floor=floor)

    def gradients(self, items, n=80, floor=0.03):
        """Several graded patterns blended in one pass: ``items`` = [(func, token), …]."""
        base = P.light("animal")
        for k in range(n):
            a, b = k / n, (k + 1) / n
            col, any_on = base, False
            for func, token in items:
                v = float(np.clip(func((a + b) / 2), 0, 1))
                if v >= floor:
                    col, any_on = P.mix(col, P.edge(token), v), True
            if any_on:
                self._band(a, b + 0.002, items[0][1], fill=col)
