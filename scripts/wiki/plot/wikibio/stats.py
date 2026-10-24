"""Biostatistics for figures: survival analysis, dose-response fits and their canvas drawings.

Every number a figure shows is computed here from the (simulated) data, never typed in:

    from wikibio import stats, quant
    km = stats.kaplan_meier(time, event)                  # steps, Greenwood CI (log-log), median
    lr = stats.logrank(time, event, group)                # chi2, df, p
    cox = stats.cox_ph(time, event, x)                    # one covariate: beta, HR, 95 % CI, Wald p
    p = quant.Plot(ax, box, (0, 60), (0, 1), ...)
    stats.draw_km(p, km, "negative", ci=True)             # step curve, CI band, censoring ticks
    stats.risk_table(ax, p, [(km_a, "Control", "negative"), ...], times=[0, 20, 40, 60], y=0.8)

    fit = stats.fit_4pl(dose, response)                   # bottom, top, EC50, Hill slope + CIs
    stats.draw_4pl(p, fit, "drug", band=True)             # fitted curve, 95 % confidence band
    stats.dilution_series(ax, (1, 5), n=6, token="drug")  # tubes of a serial dilution (schematic)

Survival times are in any unit; ``event`` is 1 for an observed event and 0 for a censored time.
"""

import math

import numpy as np
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path
from scipy import optimize
from scipy import stats as _st

from . import palette as P
from .core import LINE, label
from .quant import line_color

# ------------------------------------------------------------------ survival analysis


class KM:
    """A Kaplan-Meier estimate: step ``times`` (starting at 0), survival ``S`` and its ``lo``/``hi``
    95 % pointwise bounds after each step; ``censored`` (times) and ``S_censored`` (height of their ticks);
    ``median`` (None if S never falls to 0.5) with its 95 % CI ``median_ci``; the raw data in ``data``."""

    def at(self, t):
        """S(t) of the step function (right-continuous)."""
        i = np.searchsorted(self.times, t, side="right") - 1
        return float(self.S[max(i, 0)])

    def n_at_risk(self, t):
        """Number still at risk just before time t (time >= t)."""
        return int((self.data[0] >= t).sum())


def kaplan_meier(time, event, alpha=0.05):
    """Product-limit estimator with Greenwood variance and log(-log) confidence bounds.

    The median survival time is the first time S <= 0.5; its CI (Brookmeyer-Crowley style) is the
    set of times at which the CI band of S contains 0.5.
    """
    time, event = np.asarray(time, float), np.asarray(event, int)
    z = _st.norm.ppf(1 - alpha / 2)
    ts = np.unique(time[event == 1])
    S, gw = 1.0, 0.0
    times, Ss, lo, hi = [0.0], [1.0], [1.0], [1.0]
    for t in ts:
        n = (time >= t).sum()
        d = ((time == t) & (event == 1)).sum()
        S *= 1 - d / n
        if n > d:
            gw += d / (n * (n - d))
        times.append(t)
        Ss.append(S)
        if 0 < S < 1:
            v = gw / math.log(S) ** 2
            lo.append(S ** math.exp(z * math.sqrt(v)))
            hi.append(S ** math.exp(-z * math.sqrt(v)))
        else:
            lo.append(S)
            hi.append(S)
    km = KM()
    km.times, km.S, km.lo, km.hi = map(np.array, (times, Ss, lo, hi))
    cens = np.sort(time[event == 0])
    km.censored = cens
    km.S_censored = np.array([km.at(t) for t in cens])
    km.data = (time, event)

    def first_below(y):
        k = np.flatnonzero(y <= 0.5)
        return float(km.times[k[0]]) if len(k) else None

    km.median = first_below(km.S)
    km.median_ci = (first_below(km.lo), first_below(km.hi))
    return km


def logrank(time, event, group):
    """Log-rank (Mantel-Cox) test of equal survival among the groups: returns dict(chi2, df, p, O, E)."""
    time, event, group = np.asarray(time, float), np.asarray(event, int), np.asarray(group)
    gs = list(dict.fromkeys(group.tolist()))
    k = len(gs)
    O, E, V = np.zeros(k), np.zeros(k), np.zeros((k, k))
    for t in np.unique(time[event == 1]):
        at = time >= t
        n = at.sum()
        d = ((time == t) & (event == 1)).sum()
        nj = np.array([(at & (group == g)).sum() for g in gs], float)
        dj = np.array([((time == t) & (event == 1) & (group == g)).sum() for g in gs], float)
        O += dj
        E += d * nj / n
        if n > 1:
            f = d * (n - d) / (n - 1) / n
            V += f * (np.diag(nj) - np.outer(nj, nj) / n)
    dev = (O - E)[:-1]
    chi2 = float(dev @ np.linalg.solve(V[:-1, :-1], dev))
    return dict(chi2=chi2, df=k - 1, p=float(_st.chi2.sf(chi2, k - 1)), O=O, E=E, groups=gs)


def cox_ph(time, event, x, alpha=0.05):
    """Cox proportional-hazards model with one covariate (Breslow ties), by Newton-Raphson.

    Returns dict(beta, se, hr, hr_ci, p) with a Wald test; ``x`` is e.g. 0/1 for control/treated.
    """
    time, event, x = np.asarray(time, float), np.asarray(event, int), np.asarray(x, float)
    b = 0.0
    for _ in range(50):
        U = I = 0.0
        for t in np.unique(time[event == 1]):
            r = time >= t
            d = (time == t) & (event == 1)
            w = np.exp(b * x[r])
            m1 = (w * x[r]).sum() / w.sum()
            m2 = (w * x[r] ** 2).sum() / w.sum()
            nd = d.sum()
            U += x[d].sum() - nd * m1
            I += nd * (m2 - m1**2)
        step = U / I
        b += step
        if abs(step) < 1e-10:
            break
    se = 1 / math.sqrt(I)
    z = _st.norm.ppf(1 - alpha / 2)
    return dict(beta=b, se=se, hr=math.exp(b), hr_ci=(math.exp(b - z * se), math.exp(b + z * se)),
                p=float(2 * _st.norm.sf(abs(b / se))))


def _step_xy(t, y, t_end):
    xs = np.r_[np.repeat(t, 2)[1:], t_end]
    ys = np.repeat(y, 2)
    return xs, ys


def draw_km(plot, km, token="ink", ci=True, t_end=None, lw=1.8, tick=0.13, ci_alpha=0.22, text=None, text_at=None):
    """Draw a Kaplan-Meier estimate on a ``quant.Plot``: the step curve, its CI band and censoring ticks.

    The curve stops at the last observation (``t_end`` defaults to it). ``text`` is written in the
    curve's colour at data position ``text_at`` = (t, S). Returns the curve colour.
    """
    t_end = float(km.data[0].max()) if t_end is None else t_end
    xs, ys = _step_xy(km.times, km.S, t_end)
    if ci:
        _, lo = _step_xy(km.times, km.lo, t_end)
        _, hi = _step_xy(km.times, km.hi, t_end)
        plot.band(xs, lo, hi, token, alpha=ci_alpha)
    col = plot.line(xs, ys, token, lw=lw)
    for t, s in zip(km.censored, km.S_censored):
        if t <= t_end:
            X, Y = plot.xy(t, s)
            plot.ax.plot([X, X], [Y - tick / 2, Y + tick], color=col, lw=1.1, zorder=plot.z + 2, solid_capstyle="butt")
    if text:
        plot.text(*text_at, text, color=col, size="small", ha="left")
    return col


def risk_table(ax, plot, rows, times, y, step=0.42, title="Number at risk", size="tiny", label_x=None):
    """A number-at-risk table under a KM plot: ``rows`` are (km, name, token); counts are aligned with
    the plot's x positions of ``times``; the first row is at canvas height ``y``, then ``step`` lower.
    Group names sit left of the plot frame (or at ``label_x``)."""
    x0 = plot.box[0]
    label(ax, (label_x if label_x is not None else x0 - 0.6, y + step * 0.95), title, size="small", ha="right" if label_x is None else "left",
          bold=True, va="center")
    for k, (km, name, tok) in enumerate(rows):
        yy = y - k * step
        col = line_color(tok)
        label(ax, (label_x if label_x is not None else x0 - 0.6, yy), name, size=size, color=col,
              ha="right" if label_x is None else "left", bold=True)
        for t in times:
            label(ax, (float(plot.X(t)), yy), str(km.n_at_risk(t)), size=size, color=col)


# ------------------------------------------------------------------ dose-response


def four_pl(x, bottom, top, log_ec50, hill):
    """Four-parameter logistic (increasing for hill > 0): bottom + (top - bottom) / (1 + (EC50/x)^hill)."""
    x = np.asarray(x, float)
    return bottom + (top - bottom) / (1 + 10 ** ((log_ec50 - np.log10(x)) * hill))


class Fit4PL:
    """Result of ``fit_4pl``: ``params`` (bottom, top, log10 EC50, hill), covariance ``cov``, residual SD
    ``sigma``, ``df``, the data ``x``, ``y``; ``ci[name]`` = (estimate, lo, hi) for "bottom", "top",
    "EC50" (back-transformed from log10, hence asymmetric) and "hill"."""

    def predict(self, x):
        return four_pl(x, *self.params)

    def band(self, x, alpha=0.05):
        """Pointwise confidence band of the mean curve (delta method, t quantile)."""
        x = np.asarray(x, float)
        eps = 1e-6
        J = np.empty((len(x), 4))
        for j in range(4):
            dp = np.zeros(4)
            dp[j] = eps * max(1.0, abs(self.params[j]))
            J[:, j] = (four_pl(x, *(self.params + dp)) - four_pl(x, *(self.params - dp))) / (2 * dp[j])
        se = np.sqrt(np.einsum("ij,jk,ik->i", J, self.cov, J))
        q = _st.t.ppf(1 - alpha / 2, self.df)
        y = self.predict(x)
        return y - q * se, y + q * se


def fit_4pl(x, y, p0=None, alpha=0.05):
    """Least-squares 4PL fit (scipy ``curve_fit``) on log10 EC50; returns a ``Fit4PL``."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    if p0 is None:
        p0 = [y.min(), y.max(), float(np.median(np.log10(x))), 1.0]
    par, cov = optimize.curve_fit(four_pl, x, y, p0=p0, maxfev=20000)
    f = Fit4PL()
    f.params, f.cov, f.x, f.y = np.asarray(par), cov, x, y
    f.df = len(x) - 4
    f.sigma = float(np.sqrt(((y - f.predict(x)) ** 2).sum() / f.df))
    q = _st.t.ppf(1 - alpha / 2, f.df)
    se = np.sqrt(np.diag(cov))
    f.ci = {}
    for j, name in enumerate(("bottom", "top", "logEC50", "hill")):
        f.ci[name] = (par[j], par[j] - q * se[j], par[j] + q * se[j])
    e, lo, hi = f.ci["logEC50"]
    f.ci["EC50"] = (10**e, 10**lo, 10**hi)
    return f


def draw_4pl(plot, fit, token="ink", band=True, points=True, lw=1.8, band_alpha=0.25, r=0.06, n=200):
    """Draw a 4PL fit on a log-x ``quant.Plot``: confidence band, fitted curve and data points."""
    xx = np.logspace(math.log10(plot.xlim[0]), math.log10(plot.xlim[1]), n)
    if band:
        lo, hi = fit.band(xx)
        plot.band(xx, lo, hi, token, alpha=band_alpha)
    col = plot.line(xx, fit.predict(xx), token, lw=lw)
    if points:
        plot.points(fit.x, fit.y, token, r=r, hollow=True)
    return col


def dilution_series(ax, origin, n=6, token="drug", dx=1.0, w=0.46, h=1.25, factor="1:3", fill_frac=0.62, text=True, zorder=10):
    """A row of ``n`` tubes of a serial dilution starting at ``origin`` (bottom-left of the first tube):
    the liquid fades from the token's fill towards the page colour, and curved transfer arrows carry
    the dilution ``factor``. Returns the tube centres (bottom of each tube)."""
    from .core import arrow as _arrow

    x0, y0 = origin
    out = []
    for i in range(n):
        x = x0 + i * dx
        t = i / max(n - 1, 1)
        liquid = P.mix(P.fill(token), P.surface(), 0.12 + 0.78 * t)
        # tube: straight walls, round bottom
        r = w / 2
        th = np.linspace(np.pi, 2 * np.pi, 30)
        wall = np.r_[[[x, y0 + h]], np.c_[x + r + r * np.cos(th), y0 + r + r * np.sin(th)], [[x + w, y0 + h]]]
        lh = h * fill_frac
        th2 = np.linspace(np.pi, 2 * np.pi, 30)
        liq = np.r_[[[x, y0 + lh]], np.c_[x + r + r * np.cos(th2), y0 + r + r * np.sin(th2)], [[x + w, y0 + lh]]]
        ax.add_patch(PathPatch(Path(liq, closed=False), facecolor=liquid, edgecolor="none", zorder=zorder))
        ax.add_patch(PathPatch(Path(wall), fill=False, edgecolor=P.muted(), lw=LINE * 0.8, zorder=zorder + 1,
                               capstyle="round"))
        ax.plot([x - 0.06, x + w + 0.06], [y0 + h, y0 + h], color=P.muted(), lw=LINE * 0.9, zorder=zorder + 1,
                solid_capstyle="round")
        out.append((x + r, y0))
        if i < n - 1:
            _arrow(ax, (x + r + 0.1, y0 + h + 0.22), (x + dx + r - 0.1, y0 + h + 0.22), kind="process", bend=-0.35,
                   lw=0.9, head=0.14, color=P.muted())
    if text and factor:
        label(ax, (x0 + (n - 1) * dx / 2 + w / 2, y0 + h + 0.75), f"serial {factor} dilution", size="tiny", color=P.muted())
    return out


def well_plate(ax, origin, values, cell=0.3, token="drug", gap=0.06, zorder=10):
    """A schematic microplate: a grid of wells (rows of ``values`` in 0..1) shaded by response
    from the page colour to the token's fill. Returns the plate box (x, y, w, h)."""
    v = np.asarray(values, float)
    rows, cols = v.shape
    x0, y0 = origin
    W, H = cols * cell + 2 * gap + 0.1, rows * cell + 2 * gap + 0.1
    ax.add_patch(FancyBboxPatch((x0, y0), W, H, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.mix(P.fill("neutral"), P.surface(), 0.72) if P.is_dark() else P.fill("neutral"),
                                edgecolor=P.edge("neutral"), lw=LINE * 0.8, zorder=zorder))
    from matplotlib.patches import Circle

    for i in range(rows):
        for j in range(cols):
            c = (x0 + gap + 0.05 + (j + 0.5) * cell, y0 + H - gap - 0.05 - (i + 0.5) * cell)
            ax.add_patch(Circle(c, cell * 0.4, facecolor=P.mix(P.surface(), P.fill(token), float(np.clip(v[i, j], 0, 1))),
                                edgecolor=P.edge("neutral"), lw=0.5, zorder=zorder + 1))
    return (x0, y0, W, H)


def fmt_p(p):
    """A p value as text: "p = 0.032", "p = 4.1 × 10⁻⁵", or "p < 10⁻¹⁰"."""
    if p < 1e-10:
        return "$p < 10^{-10}$"
    if p >= 0.001:
        return f"$p = {p:.3f}$"
    m, e = f"{p:.1e}".split("e")
    return f"$p = {m} \\times 10^{{{int(e)}}}$"


__all__ = ["KM", "kaplan_meier", "logrank", "cox_ph", "draw_km", "risk_table", "four_pl", "Fit4PL", "fit_4pl",
           "draw_4pl", "dilution_series", "well_plate", "fmt_p"]
