"""Quantitative panels drawn in canvas units: small plots that sit next to schematics on a ``bio.canvas``.

A ``Plot`` maps data coordinates into a box of the canvas and draws its own axes, ticks and labels
in palette colours, so a schematic and its model share one figure, one font scale and one theme.
Axis labels follow the "quantity / unit" convention (``"V / mV"``, ``"t / ms"``).

    from wikibio import quant
    p = quant.Plot(ax, (1, 1, 6, 3), xlim=(0, 50), ylim=(-80, 40), xlabel="t / ms", ylabel="V / mV",
                   xticks=[0, 25, 50], yticks=[-80, -40, 0, 40])
    p.line(t, v, "neuron", text="V", at=0.3)
    p.hline(-65, dashed=True)
    p.span(10, 11, "highlight", text="stimulus")

Line colours: ``line_color(token)`` is the token's outline in the light theme and its (brighter)
fill in the dark theme, so curves keep contrast on both backgrounds.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

from . import palette as P
from .core import LINE, label


def line_color(token):
    """A curve colour for ``token`` that reads on the page background in both themes."""
    if token in (None, "ink"):
        return P.ink()
    if token == "muted":
        return P.muted()
    return P.fill(token) if P.is_dark() else P.edge(token)


def _fmt(v):
    if isinstance(v, str):
        return v
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v))}".replace("-", "−")
    return f"{v:g}".replace("-", "−")


class Plot:
    """Axes in a canvas box ``(x0, y0, w, h)`` (canvas units) showing data in ``xlim`` × ``ylim``.

    ``ylog`` / ``xlog`` use base-10 log scales (limits and ticks are given in data values).
    Ticks are lists of values or ``(value, text)`` pairs; ``frame`` draws only the left and bottom
    spines (``"box"`` adds the other two, ``None`` none). ``grid=True`` adds faint guide lines.
    """

    def __init__(self, ax, box, xlim, ylim, xlabel=None, ylabel=None, xticks=None, yticks=None,
                 xlog=False, ylog=False, frame="l", grid=False, size="small", tick_size="tiny", zorder=6,
                 ylabel_offset=None, xlabel_offset=None):
        self.ax, self.box, self.xlim, self.ylim = ax, box, xlim, ylim
        self.xlog, self.ylog, self.z = xlog, ylog, zorder
        x0, y0, w, h = box
        c = P.muted()
        if grid:
            for v in (yticks or []):
                v = v[0] if isinstance(v, tuple) else v
                yy = self.Y(v)
                ax.plot([x0, x0 + w], [yy, yy], color=P.mix(c, P.surface(), 0.65), lw=0.5, zorder=zorder - 1)
        if frame:
            ax.plot([x0, x0, x0 + w], [y0 + h, y0, y0], color=c, lw=0.8, zorder=zorder, solid_joinstyle="miter")
            if frame == "box":
                ax.plot([x0, x0 + w, x0 + w], [y0 + h, y0 + h, y0], color=c, lw=0.8, zorder=zorder)
        tk = 0.1
        for v in (xticks or []):
            v, t = (v if isinstance(v, tuple) else (v, _fmt(v)))
            xx = self.X(v)
            ax.plot([xx, xx], [y0, y0 - tk], color=c, lw=0.8, zorder=zorder)
            label(ax, (xx, y0 - tk - 0.08), t, size=tick_size, color=c, va="top")
        for v in (yticks or []):
            v, t = (v if isinstance(v, tuple) else (v, _fmt(v)))
            yy = self.Y(v)
            ax.plot([x0, x0 - tk], [yy, yy], color=c, lw=0.8, zorder=zorder)
            label(ax, (x0 - tk - 0.08, yy), t, size=tick_size, color=c, ha="right")
        if xlabel:
            off = 0.55 if xticks else 0.2
            off = xlabel_offset if xlabel_offset is not None else off
            label(ax, (x0 + w / 2, y0 - off), xlabel, size=size, color=P.ink(), va="top")
        if ylabel:
            off = ylabel_offset if ylabel_offset is not None else (0.75 if yticks else 0.25)
            label(ax, (x0 - off, y0 + h / 2), ylabel, size=size, color=P.ink(), rotation=90, va="bottom")

    # coordinate maps -------------------------------------------------------------------------
    def _t(self, v, lim, log):
        v = np.asarray(v, float)
        if log:
            return (np.log10(v) - math.log10(lim[0])) / (math.log10(lim[1]) - math.log10(lim[0]))
        return (v - lim[0]) / (lim[1] - lim[0])

    def X(self, x):
        """Canvas x of data x."""
        return self.box[0] + self._t(x, self.xlim, self.xlog) * self.box[2]

    def Y(self, y):
        """Canvas y of data y."""
        return self.box[1] + self._t(y, self.ylim, self.ylog) * self.box[3]

    def xy(self, x, y):
        return float(self.X(x)), float(self.Y(y))

    # marks ----------------------------------------------------------------------------------
    def line(self, x, y, token="ink", lw=1.6, dashed=False, dotted=False, text=None, at=None, dx=0.08, dy=0.12,
             ha="left", va="center", clip=True, zorder=None, size="tiny", italic=False, color=None):
        """A curve. ``text`` is written in the curve's colour next to the point at fraction ``at`` of x."""
        x, y = np.asarray(x, float), np.asarray(y, float)
        if clip:  # hide what leaves the y range (a clamped curve would draw false flat segments)
            lo, hi = sorted(self.ylim)
            y = np.where((y < lo - 1e-9) | (y > hi + 1e-9), np.nan, y)
        col = color or line_color(token)
        ls = (0, (1, 1.8)) if dotted else (0, (4, 2.4)) if dashed else "-"
        self.ax.plot(self.X(x), self.Y(y), color=col, lw=lw, ls=ls, solid_capstyle="round", solid_joinstyle="round",
                     zorder=zorder or self.z + 1)
        if text:
            i = int(np.clip((at if at is not None else 0.5) * (len(x) - 1), 0, len(x) - 1))
            label(self.ax, (float(self.X(x[i])) + dx, float(self.Y(y[i])) + dy), text, size=size, color=col, ha=ha, va=va,
                  italic=italic, zorder=self.z + 3)
        return col

    def steps(self, x, y, token="ink", lw=1.4, **kw):
        """A staircase (post-step) line, e.g. a stepping trace."""
        x, y = np.asarray(x, float), np.asarray(y, float)
        xs = np.repeat(x, 2)[1:]
        ys = np.repeat(y, 2)[:-1]
        return self.line(xs, ys, token, lw=lw, **kw)

    def points(self, x, y, token="ink", r=0.07, hollow=False, zorder=None):
        """Markers of radius ``r`` (canvas units)."""
        col = line_color(token)
        for a, b in zip(np.atleast_1d(x), np.atleast_1d(y)):
            self.ax.add_patch(Circle(self.xy(a, b), r, facecolor=P.surface() if hollow else col, edgecolor=col,
                                     lw=0.9, zorder=zorder or self.z + 2))

    def bars(self, edges, heights, token="neutral", lw=0.6, alpha=1.0):
        """A histogram from bin ``edges`` and ``heights`` (filled with the token)."""
        for a, b, hgt in zip(edges[:-1], edges[1:], heights):
            if hgt <= 0:
                continue
            x0, x1 = self.X(a), self.X(b)
            y0, y1 = self.Y(self.ylim[0]), self.Y(min(hgt, self.ylim[1]))
            self.ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw,
                                        alpha=alpha if alpha < 0.999 else None, zorder=self.z))

    def band(self, x, y0, y1, token="neutral", alpha=0.35):
        """A shaded region between two curves."""
        x = np.asarray(x, float)
        top = np.c_[self.X(x), self.Y(np.clip(y1, *sorted(self.ylim)))]
        bot = np.c_[self.X(x), self.Y(np.clip(y0, *sorted(self.ylim)))][::-1]
        self.ax.add_patch(Polygon(np.vstack([top, bot]), closed=True, facecolor=line_color(token), edgecolor="none",
                                  alpha=alpha if alpha < 0.999 else None, zorder=self.z))

    def span(self, a, b, token="highlight", text=None, strength=0.55, text_y=None, size="tiny", color=None):
        """A vertical band over x in [a, b] (stimulus, phase), as a pale tint of the token."""
        x0, x1 = self.X(a), self.X(b)
        y0, h = self.box[1], self.box[3]
        if P.is_dark():  # pastel fills are bright on the dark surface: tint less
            strength = min(0.88, strength + 0.3)
        self.ax.add_patch(Rectangle((x0, y0), x1 - x0, h, facecolor=P.mix(P.fill(token), P.surface(), strength),
                                    edgecolor="none", zorder=self.z - 2))
        if text:
            label(self.ax, ((x0 + x1) / 2, text_y if text_y is not None else y0 + h + 0.15), text, size=size,
                  color=color or P.muted(), va="bottom")

    def hline(self, y, token="muted", dashed=True, lw=0.8, text=None, side="right", size="tiny", x=None):
        """A horizontal guide line across the plot, optionally labelled at one end."""
        x0, w = self.box[0], self.box[2]
        yy = float(self.Y(y))
        col = line_color(token)
        self.ax.plot([x0, x0 + w], [yy, yy], color=col, lw=lw, ls=(0, (3, 2)) if dashed else "-", zorder=self.z)
        if text:
            if x is not None:
                label(self.ax, (float(self.X(x)), yy + 0.12), text, size=size, color=col, ha="left", va="bottom")
            elif side == "right":
                label(self.ax, (x0 + w + 0.1, yy), text, size=size, color=col, ha="left")
            else:
                label(self.ax, (x0 + 0.08, yy + 0.12), text, size=size, color=col, ha="left", va="bottom")

    def vline(self, x, token="muted", dashed=True, lw=0.8, text=None, size="tiny", top=True):
        x0 = float(self.X(x))
        y0, h = self.box[1], self.box[3]
        col = line_color(token)
        self.ax.plot([x0, x0], [y0, y0 + h], color=col, lw=lw, ls=(0, (3, 2)) if dashed else "-", zorder=self.z)
        if text:
            label(self.ax, (x0, y0 + h + 0.12 if top else y0 + 0.12), text, size=size, color=col, va="bottom")

    def text(self, x, y, s, size="tiny", color=None, token=None, **kw):
        """Text at a data position."""
        return label(self.ax, self.xy(x, y), s, size=size, color=color or (line_color(token) if token else P.ink()), **kw)

    def legend(self, items, at, size="tiny", step=0.34, length=0.5):
        """A compact legend at canvas position ``at``: items are (text, token, style) with style "-", "--" or ":"."""
        x, y = at
        for k, (text, tok, style) in enumerate(items):
            yy = y - k * step
            ls = {"-": "-", "--": (0, (4, 2.4)), ":": (0, (1, 1.8))}[style]
            self.ax.plot([x, x + length], [yy, yy], color=line_color(tok), lw=1.6, ls=ls, zorder=self.z + 2)
            label(self.ax, (x + length + 0.12, yy), text, size=size, ha="left", zorder=self.z + 2)


def bracket(ax, a, b, text=None, side=1, tick=0.12, color=None, size="tiny", offset=0.15, lw=0.9, zorder=18):
    """A dimension bracket between canvas points a and b (ticks at both ends) with a label beside its middle.

    ``side`` (+1 / −1) chooses which side of the a→b line the ticks and the label go.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = (b - a) / (np.linalg.norm(b - a) or 1)
    n = np.array([-d[1], d[0]]) * side
    c = color or P.ink()
    ax.plot(*np.array([a + n * tick, a, b, b + n * tick]).T, color=c, lw=lw, zorder=zorder, solid_joinstyle="miter")
    if text:
        m = (a + b) / 2 - n * offset
        horizontal = abs(d[0]) > abs(d[1])
        if horizontal:
            label(ax, m, text, size=size, color=c, va="top" if n[1] > 0 else "bottom", zorder=zorder)
        else:
            label(ax, m, text, size=size, color=c, ha="right" if n[0] > 0 else "left", zorder=zorder)


def odeint_rk4(f, y0, t):
    """Fixed-step 4th-order Runge–Kutta on the time grid ``t`` (deterministic, no SciPy needed)."""
    y = np.empty((len(t), len(np.atleast_1d(y0))))
    y[0] = y0
    for i in range(len(t) - 1):
        h, ti, yi = t[i + 1] - t[i], t[i], y[i]
        k1 = f(ti, yi)
        k2 = f(ti + h / 2, yi + h / 2 * k1)
        k3 = f(ti + h / 2, yi + h / 2 * k2)
        k4 = f(ti + h, yi + h * k3)
        y[i + 1] = yi + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


__all__ = ["Plot", "bracket", "line_color", "odeint_rk4", "LINE"]
