"""Quantitative panels inside biology figures: real matplotlib axes styled with the palette tokens.

A schematic drawn on a ``bio.canvas`` often needs a plot beside it (a rate curve, a gradient, an
oscillation). ``axes_at`` places a normal axes over a rectangle given in canvas units, and
``style_axes`` gives it the figure style (muted spines, ink labels, the wikibio font sizes).

    fig, ax = bio.canvas(16, 8)
    pax = charts.axes_at(ax, (9, 1, 6, 5))
    pax.plot(x, y, color=charts.line("enzyme"))
    charts.style_axes(pax, "[S] / mM", "v / (µM s⁻¹)")
"""

from . import palette as P
from .core import FONT


def axes_at(ax, rect, **kw):
    """A new axes covering ``rect = (x0, y0, w, h)`` in the data units of the canvas ``ax``.

    The rectangle is the plotting area itself (tick labels and axis labels lie outside it).
    """
    fig = ax.figure
    x0, y0, w, h = rect
    to_fig = ax.transData + fig.transFigure.inverted()
    (fx0, fy0), (fx1, fy1) = to_fig.transform([(x0, y0), (x0 + w, y0 + h)])
    new = fig.add_axes([fx0, fy0, fx1 - fx0, fy1 - fy0], **kw)
    new.set_facecolor("none")
    return new


def line(token):
    """Colour for a data line or marker of a token (its outline shade: visible on both themes)."""
    return P.edge(token)


def style_axes(ax, xlabel=None, ylabel=None, size="small", grid=False, box=False):
    """Apply the figure style to a quantitative axes: muted spines and ticks, ink labels, small fonts."""
    fs = FONT.get(size, size)
    for name, sp in ax.spines.items():
        if not box and name in ("top", "right"):
            sp.set_visible(False)
        else:
            sp.set_color(P.muted())
            sp.set_linewidth(0.8)
    ax.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=FONT["tiny"], width=0.7, length=3)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=fs, color=P.ink())
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=fs, color=P.ink())
    if grid:
        ax.grid(True, color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5)
        ax.set_axisbelow(True)
    return ax


def title(ax, text, size="small", loc="left"):
    """A small bold title above a quantitative axes."""
    ax.set_title(text, fontsize=FONT.get(size, size), color=P.ink(), loc=loc, weight="bold", pad=4)
