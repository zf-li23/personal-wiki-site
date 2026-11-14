"""wikibehav: animal-behaviour figures (7.18): orientation, rhythms, apparatus, collective motion, signal detection.

A standalone helper next to wikibio (its own entry in PLOT_HELPERS): editing it re-renders only the scripts that import it, not
every biology figure. It draws with the wikibio palette and fonts, so it mixes freely with ``bio.*`` and
``wikibio.behaviour`` (marginal value theorem, hawk-dove game) on one canvas.

    import wikibio as bio
    import wikibehav as wb
    from wikibio import quant

Orientation (compass bearings in degrees, clockwise from north: 0 = N, 90 = E)
    a = wb.vonmises(mean=200, kappa=2.5, n=24, seed=1)       sample headings (degrees, 0..360)
    mu, r = wb.mean_direction(a)                             mean bearing and mean resultant length r (0..1)
    r, z, p = wb.rayleigh(a)                                 Rayleigh test of uniformity (z = n r^2; Zar's p)
    V, u, p = wb.v_test(a, expected=180)                     V test: clustering around an expected bearing
    wb.emlen_funnel(ax, (4, 4), 3, scratches)                Emlen funnel from above: rim, ink pad, scratch marks
                                                              along the given bearings (``sectors=24`` adds sector lines)
    wb.circular_plot(ax, (4, 4), 3, a, token="dna", expected=180, expected_text="migratory direction")
        headings as dots stacked inward on the circle (``bin`` degrees), the mean vector (length r times the
        radius), an optional dashed expected bearing, N/E/S/W and an "r = ..., p ..." line below.
        Returns {"mean", "r", "z", "p", "tip"}.

Activity rhythms (double-plotted actograms)
    t, counts, onsets = wb.simulate_activity(days=20, tau=24.0, onset=18.0, alpha=10.0,
                                             taus=[(10, 24.6)], shifts=[(15, -3.0)], seed=0)
        binned activity counts (``bin`` hours, default 0.25) of an animal that starts activity at ``onset`` (hours
        after midnight of day 0) for ``alpha`` hours; ``taus`` = [(day, period)] changes the period from that day
        on (entrained 24 h, then free running), ``shifts`` = [(day, hours)] shifts onsets from that day on
        (+ delay, - advance). ``onsets`` are absolute hours, one per day.
    act = wb.Actogram(ax, (x0, y0, w, h), t, counts, light=(6, 18), dd_from=10, pulses=[(14, 20.0)])
        one row per day (day 1 on top), each row showing day k and day k + 1 (``double=False``: 24 h only);
        bars are activity, light hours are tinted pale yellow and dark hours grey, an LD bar above shows the light (yellow) and dark phases of
        the first day; ``dd_from`` = first day in constant darkness (``ll_from`` constant light); ``pulses`` =
        [(day, hour)] marks light pulses with a star. ``act.xy(day, hour)`` gives canvas points (day 0-based,
        hour 0..48), ``act.onsets(onsets, token)`` draws the onset lines (fitted tau made visible).

Apparatus (clean line drawings from above unless noted; walls in ink, floors pale; all return anchor points)
    wb.t_maze(ax, (5, 5), arm=2.5, stem=3.5, width=0.8, reward="right")      {"choice", "left", "right", "start"}
    wb.y_maze(ax, (5, 5), arm=3.0, width=0.8)                                {"choice", "left", "right", "start"}
    wb.plus_maze(ax, (5, 5), arm=2.5, width=0.7, closed=(1, 3))              elevated plus maze: open arms have no
                                                                             walls; {"center", "ends": {k: xy}}
    wb.radial_maze(ax, (5, 5), arm=3, n=8, baited=(0, 2, 5), visited=(2,))   8-arm radial maze with food wells
    wb.arm_maze(ax, center, n, arm, width, hub=None, rotation=90, arms=None, lengths=None, open_arms=())
        the general form: a regular n-gon hub (side ``hub``) with arms on sides ``arms`` (side k faces
        ``rotation + k * 360 / n`` degrees, counter-clockwise from +x)
    wb.water_maze(ax, (5, 5), 4, platform=(45, 0.5), path=wb.swim_path((45, 0.5), start=180, kind="search"))
        Morris water maze: pool, quadrant lines and labels, hidden (dashed) or visible platform, distal cues,
        optional swim path (pool units: radius 1, x = east, y = north). Returns {"center", "r", "platform",
        "to"} with ``to(points)`` mapping pool units to the canvas.
    wb.swim_path(platform, start=180, kind="direct" | "search" | "thigmotaxis", steps=500, seed=0)
    wb.operant_box(ax, (5, 4), w=7, h=4.5, lever=True, light=True, light_on=True, hopper=True, key=False)
        Skinner box in side view: front panel (right) with cue light, lever, pecking key, food magazine and the
        pellet dispenser outside, grid floor, optional speaker. Returns {"lever", "light", "key", "magazine",
        "dispenser", "floor", "speaker", "inside"} for callouts. Put the animal in with a literal icon id,
        e.g. ``bio.icon(ax, "phylopic/rat", at=box["inside"], height=1.2)`` (icon credits are read from the
        script itself, so the helper never draws icons).

Collective motion and navigation (simulations, all well under a second)
    pos, head = wb.couzin(n=40, steps=300, **wb.COUZIN_REGIMES["torus"], seed=0)
        Couzin et al. (2002) zone model in 2-D: repulsion within ``rr``, alignment out to ``ro``, attraction out
        to ``ra``, a rear blind angle ``blind``, turning rate ``turn`` (deg per unit time), angular noise.
        pos, head: arrays (steps + 1, n, 2). ``COUZIN_REGIMES`` = swarm / torus / parallel parameter sets.
    wb.polarization(head) -> (steps + 1,)       |mean heading|: 1 = all aligned
    wb.milling(pos, head) -> (steps + 1,)       |mean angular momentum about the centroid|: 1 = perfect mill
    wb.zones(ax, (3, 3), 0.6, 1.5, 2.6, heading=90, blind=90)   the three zones and the blind sector
    pi = wb.path_integration(steps=220, seed=3, error=0.0, displace=None, search=True)
        a desert-ant foray: correlated random walk out from the nest (0, 0), then the straight run home along the
        integrated vector (``error`` = s.d. of the heading error per step in degrees; ``displace`` = (dx, dy)
        releases the animal elsewhere, as in Wehner's displacement experiments, so it runs to a fictive nest),
        then expanding search loops. Keys: "outbound", "homing", "search", "vector", "release", "fictive".
    to = wb.fit([pts1, pts2], (x0, y0, w, h))    a map from simulation units into a canvas box (equal aspect)
    wb.trail(ax, to(path), token="rna", fade=True, arrows=3, start="o", end="*")
        a trajectory whose older part fades into the background; ``arrows`` direction heads along it
    wb.school(ax, pos, head, to, frame=-1, tail=25, token="dna", size=0.28)   trails + agents at one frame
    wb.agent(ax, xy, heading_vector, size=0.3, token="dna")                   one agent (a small dart)

Signal detection (on a quant.Plot)
    H, F = wb.sdt_rates(d=1.5, xc=0.75)             hit and false-alarm rates for a criterion at ``xc``
    d = wb.dprime(H, F); c = wb.bias(H, F)          d' = z(H) - z(F), c = -(z(H) + z(F)) / 2
    p = quant.Plot(ax, box, xlim=(-3.5, 5), ylim=(0, 0.48), xlabel="internal response")
    wb.sdt_panel(p, d=1.5, xc=0.75)                 noise and signal distributions, criterion, shaded hits and
                                                    false alarms, the d' bracket; returns (H, F)
    q = quant.Plot(ax, box, xlim=(0, 1), ylim=(0, 1), xlabel="false-alarm rate", ylabel="hit rate")
    wb.roc_panel(q, dprimes=(0.5, 1, 2), points=[(0.2, 0.6)])   ROC curves with the chance diagonal

Conventions: compass bearings clockwise from north for orientation and the water maze; canvas angles (counter-
clockwise from +x) for the arm mazes and agents. Text in figures is English only.
"""

import math

import numpy as np
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, Wedge
from scipy.stats import norm

from wikibio import palette as P
from wikibio.core import LINE, arrow, callout, label
from wikibio.quant import line_color


# ------------------------------------------------------------------ shared
def _bearing(deg):
    """Canvas unit vector of a compass bearing (clockwise from north)."""
    a = np.radians(deg)
    return np.sin(a), np.cos(a)


def _paper(strength=None):
    """A pale neutral floor / paper colour that stays quiet in both themes."""
    s = strength if strength is not None else (0.82 if P.is_dark() else 0.55)
    return P.mix(P.fill("neutral"), P.surface(), s)


def _tint(token, strength=None):
    s = strength if strength is not None else (0.8 if P.is_dark() else 0.6)
    return P.mix(P.fill(token), P.surface(), s)


def _fmt_p(p):
    if p < 0.001:
        return "p < 0.001"
    return f"p = {p:.3f}" if p < 0.01 else f"p = {p:.2f}"


def _compass(ax, center, r, size="tiny", gap=0.28, color=None):
    for text, b in (("N", 0), ("E", 90), ("S", 180), ("W", 270)):
        ux, uy = _bearing(b)
        label(ax, (center[0] + (r + gap) * ux, center[1] + (r + gap) * uy), text, size=size, color=color or P.muted())


# ------------------------------------------------------------------ orientation
def vonmises(mean, kappa, n, seed=0):
    """``n`` bearings (degrees, 0..360) from a von Mises distribution with mean ``mean`` and concentration ``kappa``."""
    rng = np.random.default_rng(seed)
    return np.degrees(rng.vonmises(math.radians(mean), kappa, n)) % 360


def mean_direction(angles):
    """(mean bearing in degrees, mean resultant length r in 0..1) of angles in degrees."""
    a = np.radians(np.asarray(angles, float))
    C, S = np.cos(a).mean(), np.sin(a).mean()
    return math.degrees(math.atan2(S, C)) % 360, float(math.hypot(C, S))


def rayleigh(angles):
    """Rayleigh test of circular uniformity: (r, z = n r^2, p) with Zar's (2010) approximation of p."""
    n = len(angles)
    _, r = mean_direction(angles)
    R = n * r
    z = R * R / n
    p = math.exp(math.sqrt(1 + 4 * n + 4 * (n * n - R * R)) - (1 + 2 * n))
    return r, z, float(min(1.0, max(0.0, p)))


def v_test(angles, expected):
    """V test (modified Rayleigh) for clustering around an expected bearing: (V, u, one-sided p)."""
    n = len(angles)
    mu, r = mean_direction(angles)
    V = n * r * math.cos(math.radians(mu - expected))
    u = V * math.sqrt(2.0 / n)
    return V, u, float(norm.sf(u))


def emlen_funnel(ax, center, r, scratches, inner=0.32, sectors=0, seed=0, compass=True, lw=0.7, zorder=8):
    """An Emlen funnel seen from above: the paper-lined wall, the ink pad at the bottom and one scratch mark per
    bearing in ``scratches`` (degrees; pass many per bird, e.g. ``vonmises(200, 2, 150)``). ``sectors`` > 0
    draws dashed sector boundaries as used for counting. Returns {"center", "r", "pad"}."""
    cx, cy = center
    rng = np.random.default_rng(seed)
    ax.add_patch(Circle(center, r, facecolor=_paper(), edgecolor=P.edge("neutral"), lw=LINE * 1.5, zorder=zorder))
    for f in (0.55, 0.78):  # faint rings: the sloping wall
        ax.add_patch(Circle(center, r * f, fill=False, edgecolor=P.mix(P.muted(), P.surface(), 0.55), lw=0.5,
                            zorder=zorder + 1))
    pad = P.mix(P.edge("neutral"), P.surface(), 0.25 if P.is_dark() else 0.1)
    ax.add_patch(Circle(center, r * inner, facecolor=pad, edgecolor=P.edge("neutral"), lw=LINE, zorder=zorder + 2))
    if sectors:
        for k in range(sectors):
            ux, uy = _bearing(k * 360 / sectors)
            ax.plot([cx + r * inner * ux, cx + r * ux], [cy + r * inner * uy, cy + r * uy], color=P.muted(), lw=0.45,
                    ls=(0, (2, 2)), zorder=zorder + 1)
    a = np.asarray(scratches, float) + rng.normal(0, 4, len(scratches))
    rad = r * (inner + 0.06 + (0.96 - inner - 0.06 - 0.14) * rng.random(len(a)))
    ln = r * (0.06 + 0.1 * rng.random(len(a)))
    wob = np.radians(rng.normal(0, 12, len(a)))  # marks are not perfectly radial
    segs = []
    for ai, ri, li, wi in zip(np.radians(a), rad, ln, wob):
        p0 = np.array([cx + ri * math.sin(ai), cy + ri * math.cos(ai)])
        d = np.array([math.sin(ai + wi), math.cos(ai + wi)])
        segs.append([p0, p0 + li * d])
    ax.add_collection(LineCollection(segs, colors=P.ink(), linewidths=lw, capstyle="round", zorder=zorder + 3))
    if compass:
        _compass(ax, center, r)
    return {"center": center, "r": r, "pad": r * inner}


def circular_plot(ax, center, r, angles, token="dna", bin=10, dot=None, expected=None, expected_text=None, mean=True,
                  compass=True, stats=True, size="tiny", zorder=10):
    """Individual headings on a circle with the mean vector (see the module doc). Returns {"mean", "r", "z", "p", "tip"}."""
    cx, cy = center
    col = line_color(token)
    ax.add_patch(Circle(center, r, fill=False, edgecolor=P.muted(), lw=0.9, zorder=zorder))
    guide = P.mix(P.muted(), P.surface(), 0.55)
    ax.plot([cx - r, cx + r], [cy, cy], color=guide, lw=0.5, zorder=zorder - 1)
    ax.plot([cx, cx], [cy - r, cy + r], color=guide, lw=0.5, zorder=zorder - 1)
    for b in range(0, 360, 90):
        ux, uy = _bearing(b)
        ax.plot([cx + r * ux, cx + (r + 0.12) * ux], [cy + r * uy, cy + (r + 0.12) * uy], color=P.muted(), lw=0.9,
                zorder=zorder)
    dr = dot if dot is not None else r * 0.03
    a = np.asarray(angles, float) % 360
    bins = np.floor(a / bin).astype(int)
    for b in np.unique(bins):
        k = int((bins == b).sum())
        ux, uy = _bearing((b + 0.5) * bin)
        for j in range(k):
            rr = r - dr * (1 + 2.15 * j)
            ax.add_patch(Circle((cx + rr * ux, cy + rr * uy), dr, facecolor=col, edgecolor=col, lw=0.4, zorder=zorder + 2))
    mu, rbar = mean_direction(a)
    _, z, p = rayleigh(a)
    ux, uy = _bearing(mu)
    tip = (cx + rbar * r * ux, cy + rbar * r * uy)
    if expected is not None:
        ex, ey = _bearing(expected)
        ax.plot([cx, cx + r * ex], [cy, cy + r * ey], color=P.muted(), lw=1.0, ls=(0, (3, 2)),
                zorder=zorder + 1)
        if expected_text:
            label(ax, (cx + (r + 0.75) * ex, cy + (r + 0.75) * ey), expected_text, size=size, color=P.muted(),
                  ha="left" if ex > 0.3 else "right" if ex < -0.3 else "center",
                  va="bottom" if ey > 0.3 else "top" if ey < -0.3 else "center")
    if mean and rbar > 0.02:
        arrow(ax, center, tip, kind="process", color=col, lw=1.8, head=min(0.3, r * 0.12), zorder=zorder + 3)
    ax.add_patch(Circle(center, r * 0.025, color=P.muted(), zorder=zorder + 4))
    if compass:
        _compass(ax, center, r + 0.05, gap=0.3)
    if stats:
        label(ax, (cx, cy - r - 0.75), f"n = {len(a)}, r = {rbar:.2f}, {_fmt_p(p)}", size=size, color=P.ink(), va="top")
    return {"mean": mu, "r": rbar, "z": z, "p": p, "tip": tip}


# ------------------------------------------------------------------ activity rhythms
def simulate_activity(days=20, tau=24.0, onset=18.0, alpha=10.0, bin=0.25, taus=(), shifts=(), rate=6.0,
                      rest_rate=0.08, seed=0):
    """Binned activity of a rhythmic animal: returns (t in hours from midnight of day 0, counts, onsets)."""
    rng = np.random.default_rng(seed)
    ons, o = [], float(onset)
    for k in range(days + 2):
        ons.append(o)
        per = tau
        for d, v in sorted(taus):
            if k >= d:
                per = v
        o += per
        for d, h in shifts:
            if k + 1 == d:
                o += h
    ons = np.array(ons)
    n = int(round(days * 24 / bin))
    t = np.arange(n) * bin
    active = np.zeros(n, bool)
    for s in ons:
        active |= (t >= s) & (t < s + alpha)
    gate = np.ones(n)
    state = 1
    for i in range(n):  # bouts: a two-state Markov chain inside the active phase
        if rng.random() < (0.12 if state else 0.35):
            state = 1 - state
        gate[i] = state
    lam = np.where(active, rate * (0.25 + 0.75 * gate), rest_rate)
    return t, rng.poisson(lam), ons[:days]


class Actogram:
    """A (double-plotted) actogram in the canvas box ``(x0, y0, w, h)``; see the module doc."""

    def __init__(self, ax, box, t, counts, bin=None, double=True, light=(6.0, 18.0), dd_from=None, ll_from=None,
                 pulses=(), token="ink", shade=True, ld_bar=True, day_ticks=5, xlabel="time of day / h", ylabel="day",
                 size="small", zorder=6):
        self.ax, self.box, self.double = ax, box, double
        t, counts = np.asarray(t, float), np.asarray(counts, float)
        bin = bin if bin is not None else float(t[1] - t[0])
        self.span = 48.0 if double else 24.0
        self.rows = int(math.ceil((t[-1] + bin) / 24 - 1e-9))
        x0, y0, w, h = box
        self.rh = h / self.rows
        self.z = zorder
        dark_fill = P.surface() if P.is_dark() else P.mix(P.muted(), P.surface(), 0.78)  # dark theme: the page itself

        def dark_spans(day):
            if dd_from is not None and day >= dd_from:
                return [(0, 24)]
            if (ll_from is not None and day >= ll_from) or light is None:
                return [] if light is not None or ll_from is not None else [(0, 24)]
            on, off = light
            return [(0, on), (off, 24)] if on < off else [(off, on)]

        halves = (0, 1) if double else (0,)
        if shade:  # light phases pale yellow, dark phases grey (reads the same way in both themes)
            ax.add_patch(Rectangle((x0, y0), w, h, facecolor=P.mix(P.fill("highlight"), P.surface(),
                                                                    0.8 if P.is_dark() else 0.78),
                                   edgecolor="none", zorder=zorder - 2))
            for k in range(self.rows):
                for hf in halves:
                    for a, b in dark_spans(k + hf):
                        X0, Y = self.xy(k, a + 24 * hf)
                        X1, _ = self.xy(k, b + 24 * hf)
                        ax.add_patch(Rectangle((X0, Y - 0.01), X1 - X0 + 0.01, self.rh + 0.02, facecolor=dark_fill,
                                               edgecolor="none", zorder=zorder - 1))  # overlap: no seams
        pos = counts > 0
        top = np.quantile(counts[pos], 0.98) if pos.any() else 1.0
        bw = bin / self.span * w
        polys = []
        for ti, ci in zip(t[pos], counts[pos]):
            day = int(ti // 24)
            hh = min(1.0, ci / top) * self.rh * 0.88
            for k, hour in ((day, ti - 24 * day), (day - 1, ti - 24 * day + 24)):
                if k < 0 or hour >= self.span:
                    continue
                X, Y = self.xy(k, hour)
                polys.append([(X, Y), (X + bw, Y), (X + bw, Y + hh), (X, Y + hh)])
        col = line_color(token)
        ax.add_collection(PolyCollection(polys, facecolors=col, edgecolors="none", zorder=zorder + 1))
        c = P.muted()
        ax.plot([x0, x0 + w, x0 + w, x0, x0], [y0, y0, y0 + h, y0 + h, y0], color=c, lw=0.7, zorder=zorder + 2)
        if double:
            ax.plot([x0 + w / 2] * 2, [y0, y0 + h], color=c, lw=0.6, zorder=zorder + 2)
        for hour in range(0, int(self.span) + 1, 12):
            X = x0 + hour / self.span * w
            ax.plot([X, X], [y0, y0 - 0.1], color=c, lw=0.8, zorder=zorder)
            label(ax, (X, y0 - 0.18), f"{hour}", size="tiny", color=c, va="top")
        for k in range(self.rows):
            if k == 0 or (k + 1) % day_ticks == 0:
                label(ax, (x0 - 0.12, self.xy(k, 0)[1] + self.rh / 2), f"{k + 1}", size="tiny", color=c, ha="right")
        if xlabel:
            label(ax, (x0 + w / 2, y0 - 0.62), xlabel, size=size, va="top")
        if ylabel:
            label(ax, (x0 - 0.65, y0 + h / 2), ylabel, size=size, rotation=90)
        if ld_bar:
            bh_, by = 0.28, y0 + h + 0.1
            ax.add_patch(Rectangle((x0, by), w, bh_, facecolor=P.fill("highlight"), edgecolor="none", zorder=zorder))
            barc = P.mix(P.muted(), P.surface(), 0.35) if P.is_dark() else P.ink()
            for hf in halves:
                for a, b in dark_spans(0):  # the regime of the first day
                    X0 = x0 + (a + 24 * hf) / self.span * w
                    X1 = x0 + (b + 24 * hf) / self.span * w
                    ax.add_patch(Rectangle((X0, by), X1 - X0, bh_, facecolor=barc, edgecolor="none", zorder=zorder + 1))
            ax.add_patch(Rectangle((x0, by), w, bh_, fill=False, edgecolor=c, lw=0.6, zorder=zorder + 2))
            self.ld_top = by + bh_
        else:
            self.ld_top = y0 + h
        for day, hour in pulses:
            for k, hr in ((day, hour), (day - 1, hour + 24)):
                if 0 <= k < self.rows and hr < self.span:
                    X, Y = self.xy(k, hr)
                    ax.plot([X], [Y + self.rh / 2], marker="*", ms=7, color=P.fill("highlight"),
                            markeredgecolor=P.edge("highlight"), markeredgewidth=0.6, zorder=zorder + 4)

    def xy(self, day, hour):
        """Canvas (x, y) of the bottom of row ``day`` (0-based) at ``hour`` (0..48 in a double plot)."""
        x0, y0, w, h = self.box
        return x0 + hour / self.span * w, y0 + h - (day + 1) * self.rh

    def line(self, days, hours, token="rna", lw=1.3, dashed=True):
        """A line through (day, hour) points at mid-row height (e.g. a fitted onset line)."""
        pts = np.array([self.xy(d, hr) for d, hr in zip(days, hours)])
        pts[:, 1] += self.rh / 2
        self.ax.plot(pts[:, 0], pts[:, 1], color=line_color(token), lw=lw, ls=(0, (3, 2)) if dashed else "-",
                     zorder=self.z + 3)

    def onsets(self, onsets, token="rna", lw=1.3, dashed=True, fit=True):
        """Onset lines in both halves; ``fit`` draws least-squares lines per run of constant slope instead of a
        polyline. Returns the onset hours relative to each row."""
        ons = np.asarray(onsets, float)
        k = np.arange(len(ons))
        rel = ons - 24 * k
        for shift in ((0, 24) if self.double else (0,)):
            rows = k if shift == 0 else k - 1
            m = (rows >= 0) & (rows < self.rows) & (rel + shift >= 0) & (rel + shift <= self.span)
            if m.sum() >= 2:
                self.line(rows[m], rel[m] + shift, token, lw=lw, dashed=dashed)
        return rel


# ------------------------------------------------------------------ apparatus
def arm_maze(ax, center, n=8, arm=3.0, width=0.7, hub=None, rotation=90.0, arms=None, lengths=None, open_arms=(),
             tint=None, lw=1.8, zorder=6):
    """A maze of arms on a regular n-gon hub (see the module doc). ``tint`` = {side: token} tints arm floors.
    Returns {"center", "ends": {k: xy}, "bases": {k: xy}, "dirs": {k: unit vector}}."""
    cx, cy = center
    s = hub if hub is not None else width
    a_ = s / (2 * math.tan(math.pi / n))
    R = s / (2 * math.sin(math.pi / n))
    arms = list(range(n)) if arms is None else list(arms)
    lengths = lengths or {}
    if not isinstance(lengths, dict):
        lengths = dict(zip(arms, lengths))
    tint = tint or {}
    floor, wall, edge = _paper(), P.ink(), P.muted()
    vert = []
    for k in range(n):
        ang = math.radians(rotation + (k - 0.5) * 360 / n)
        vert.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))
    vert = np.array(vert)  # side k runs from vert[k] to vert[k + 1]
    ax.add_patch(Polygon(vert, closed=True, facecolor=floor, edgecolor="none", zorder=zorder))
    out = {"center": center, "ends": {}, "bases": {}, "dirs": {}}
    walls, edges = [], []
    for k in range(n):
        phi = math.radians(rotation + k * 360 / n)
        u = np.array([math.cos(phi), math.sin(phi)])
        tvec = np.array([-u[1], u[0]])
        m = np.array([cx, cy]) + a_ * u
        v0, v1 = vert[k], vert[(k + 1) % n]
        if k not in arms:
            walls.append([v0, v1])
            continue
        L = lengths.get(k, arm)
        bm, bp = m - tvec * width / 2, m + tvec * width / 2
        em, ep = bm + u * L, bp + u * L
        ax.add_patch(Polygon([bm, em, ep, bp], closed=True, facecolor=_tint(tint[k]) if k in tint else floor,
                             edgecolor="none", zorder=zorder))
        if s > width + 1e-6:
            walls += [[v0, bm], [bp, v1]]
        (edges if k in open_arms else walls).extend([[bm, em], [bp, ep], [em, ep]])
        out["ends"][k] = tuple(m + u * (L - width * 0.45))
        out["bases"][k] = tuple(m)
        out["dirs"][k] = tuple(u)
    if edges:
        ax.add_collection(LineCollection(edges, colors=edge, linewidths=0.8, zorder=zorder + 1))
    ax.add_collection(LineCollection(walls, colors=wall, linewidths=lw, capstyle="round", joinstyle="round",
                                     zorder=zorder + 2))
    return out


def _food(ax, xy, r, baited=True, zorder=12):
    if baited:
        ax.add_patch(Circle(xy, r, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=zorder))
    else:
        ax.add_patch(Circle(xy, r, facecolor="none", edgecolor=P.muted(), lw=0.8, zorder=zorder))


def t_maze(ax, center, arm=2.5, stem=3.5, width=0.8, reward=None, start_box=True, labels=True, zorder=6):
    """A T-maze from above; ``center`` is the choice point; ``reward`` = "left" / "right" puts food at that end."""
    m = arm_maze(ax, center, n=4, arm=arm, width=width, rotation=0, arms=[0, 2, 3], lengths={0: arm, 2: arm, 3: stem},
                 zorder=zorder)
    out = {"choice": center, "right": m["ends"][0], "left": m["ends"][2], "start": m["ends"][3]}
    if start_box:  # the start-box door across the stem
        y = m["bases"][3][1] - stem + width * 1.1
        ax.plot([center[0] - width / 2, center[0] + width / 2], [y, y], color=P.muted(), lw=1.2, ls=(0, (2, 1.5)),
                zorder=zorder + 3)
        out["start"] = (center[0], (y + m["bases"][3][1] - stem) / 2)
    if reward:
        _food(ax, out[reward], width * 0.18)
    if labels:
        for key, d in (("left", (-1, 0)), ("right", (1, 0))):
            x, y = out[key]
            label(ax, (x, y + width * 0.75), key.capitalize(), size="tiny", color=P.muted(), va="bottom")
        label(ax, (out["start"][0] + width * 0.7, out["start"][1]), "start", size="tiny", color=P.muted(), ha="left")
    return out


def y_maze(ax, center, arm=3.0, width=0.8, reward=None, labels=True, zorder=6):
    """A Y-maze from above, start arm pointing down; returns {"choice", "left", "right", "start"}."""
    m = arm_maze(ax, center, n=3, arm=arm, width=width, rotation=270, zorder=zorder)
    out = {"choice": center, "start": m["ends"][0], "right": m["ends"][1], "left": m["ends"][2]}
    if reward:
        _food(ax, out[reward], width * 0.18)
    if labels:
        for key in ("left", "right"):
            x, y = out[key]
            label(ax, (x, y + width * 0.75), key.capitalize(), size="tiny", color=P.muted(), va="bottom")
        label(ax, (out["start"][0] + width * 0.7, out["start"][1]), "start", size="tiny", color=P.muted(), ha="left")
    return out


def plus_maze(ax, center, arm=2.5, width=0.7, closed=(1, 3), labels=True, zorder=6):
    """An elevated plus maze from above: walled ``closed`` arms (sides 0 = east, 1 = north, ...), open arms without
    walls. Returns {"center", "ends"}."""
    open_ = [k for k in range(4) if k not in closed]
    m = arm_maze(ax, center, n=4, arm=arm, width=width, rotation=0, open_arms=open_, zorder=zorder)
    if labels:
        k = open_[0] if open_ else 0
        x, y = m["ends"][k]
        ux, uy = m["dirs"][k]
        label(ax, (x + ux * width * 1.1 + (0 if ux else width * 0.8), y + uy * width * 1.1 + (width * 0.6 if ux else 0)),
              "open", size="tiny", color=P.muted(), va="bottom" if ux else "center", ha="center" if ux else "left")
        if closed:
            k = closed[0]
            x, y = m["ends"][k]
            ux, uy = m["dirs"][k]
            label(ax, (x + (width * 0.8 if not ux else 0), y + (width * 0.6 if ux else 0)), "closed", size="tiny",
                  color=P.muted(), ha="left" if not ux else "center", va="bottom" if ux else "center")
    return {"center": center, "ends": m["ends"]}


def radial_maze(ax, center, arm=3.0, n=8, width=0.6, hub=None, baited=None, visited=(), zorder=6):
    """An n-arm radial maze with a food well at each arm end: ``baited`` wells filled (default all), ``visited``
    arms tinted. Arm 0 points up, numbering clockwise. Returns {"center", "ends", "wells"}."""
    hub = hub if hub is not None else width * 1.45
    # arm k (clockwise from up) is side j = -k mod n counted counter-clockwise from 90 degrees
    side = {k: (-k) % n for k in range(n)}
    m = arm_maze(ax, center, n=n, arm=arm, width=width, hub=hub, rotation=90, tint={side[k]: "dna2" for k in visited},
                 zorder=zorder)
    baited = range(n) if baited is None else baited
    ends = {k: m["ends"][side[k]] for k in range(n)}
    for k in range(n):
        _food(ax, ends[k], width * 0.2, k in baited)
    return {"center": center, "ends": ends, "wells": ends}


def swim_path(platform=(45.0, 0.5), start=180.0, kind="search", steps=500, step=0.025, platform_r=0.08, seed=0):
    """A swim path in pool units (radius 1, x east, y north) from the wall at bearing ``start``: "direct" (a trained
    animal heads for the platform), "search" (a naive animal: a correlated random walk whose pull towards the
    platform grows), "thigmotaxis" (circling along the wall). Stops on the platform."""
    rng = np.random.default_rng(seed)
    pb, pd = platform
    target = pd * np.array(_bearing(pb))
    p = 0.92 * np.array(_bearing(start))
    h = math.atan2(-p[1], -p[0])  # facing the pool centre
    pts = [p.copy()]
    for i in range(steps):
        to = target - p
        want = math.atan2(to[1], to[0])
        if kind == "direct":
            pull, sd = 0.35, 0.12
        elif kind == "search":
            pull, sd = 0.22 * (i / steps) ** 2, 0.45
        else:  # thigmotaxis: keep a constant distance from the wall
            rr = np.hypot(*p)
            tang = math.atan2(p[1], p[0]) + math.pi / 2
            want = tang + 3.0 * (rr - 0.86)
            pull, sd = 0.4, 0.15
        d = (want - h + math.pi) % (2 * math.pi) - math.pi
        h += pull * d + rng.normal(0, sd)
        p = p + step * np.array([math.cos(h), math.sin(h)])
        rr = np.hypot(*p)
        if rr > 0.95:  # the wall: slide along it
            p = p * 0.95 / rr
            radial = math.atan2(p[1], p[0])
            h = radial + math.copysign(math.pi / 2, math.sin(h - radial)) + rng.normal(0, 0.1)
        pts.append(p.copy())
        if np.hypot(*(p - target)) < platform_r:
            break
    return np.array(pts)


def water_maze(ax, center, r, platform=(45.0, 0.5), platform_size=None, hidden=True, quadrants=True, cues=True,
               path=None, path_token="rna", labels=True, zorder=6):
    """A Morris water maze from above (see the module doc)."""
    cx, cy = center
    water = P.mix(P.fill("channel"), P.surface(), 0.78 if P.is_dark() else 0.62)
    ax.add_patch(Circle(center, r, facecolor=water, edgecolor=P.edge("channel"), lw=LINE * 1.6, zorder=zorder))
    to = lambda q: np.asarray(center, float) + r * np.asarray(q, float)  # noqa: E731
    if quadrants:
        g = P.mix(P.edge("channel"), P.surface(), 0.35)
        ax.plot([cx - r, cx + r], [cy, cy], color=g, lw=0.6, ls=(0, (3, 2)), zorder=zorder + 1)
        ax.plot([cx, cx], [cy - r, cy + r], color=g, lw=0.6, ls=(0, (3, 2)), zorder=zorder + 1)
        if labels:
            for text, b in (("NE", 45), ("NW", 315), ("SE", 135), ("SW", 225)):
                label(ax, tuple(to(0.8 * np.array(_bearing(b)))), text, size="tiny", color=P.muted())
    ps = platform_size if platform_size is not None else 0.17 * r
    pxy = tuple(to(platform[1] * np.array(_bearing(platform[0]))))
    ax.add_patch(Rectangle((pxy[0] - ps / 2, pxy[1] - ps / 2), ps, ps,
                           facecolor=P.mix(P.fill("neutral"), water, 0.45 if hidden else 0.0), edgecolor=P.edge("neutral"),
                           lw=1.0, ls=(0, (2, 1.2)) if hidden else "-", zorder=zorder + 2))
    if cues:  # distal visual cues on the room walls
        for b, tok, kind in ((320, "rna", "star"), (75, "protein", "tri"), (200, "positive", "square")):
            x, y = to(1.28 * np.array(_bearing(b)))
            s = r * 0.09
            if kind == "tri":
                pts = [(x, y + s * 1.1), (x - s, y - s * 0.7), (x + s, y - s * 0.7)]
            elif kind == "square":
                pts = [(x - s * 0.8, y - s * 0.8), (x + s * 0.8, y - s * 0.8), (x + s * 0.8, y + s * 0.8), (x - s * 0.8, y + s * 0.8)]
            else:
                pts = [(x + (s * 1.15 if j % 2 == 0 else s * 0.5) * math.sin(j * math.pi / 5),
                        y + (s * 1.15 if j % 2 == 0 else s * 0.5) * math.cos(j * math.pi / 5)) for j in range(10)]
            ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=zorder))
    if path is not None:
        trail(ax, to(path), token=path_token, arrows=0, start="o", end=None, lw=1.2, zorder=zorder + 4)
    return {"center": center, "r": r, "platform": pxy, "to": to}


def operant_box(ax, center, w=7.0, h=4.5, lever=True, light=True, light_on=True, hopper=True, pellet=True, key=False,
                speaker=False, grid=True, zorder=6):
    """A Skinner box in side view (see the module doc). Returns anchor points for callouts."""
    cx, cy = center
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    wall, c_neu, e_neu = P.ink(), P.fill("neutral"), P.edge("neutral")
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=_paper(0.85 if P.is_dark() else 0.75), edgecolor="none", zorder=zorder))
    pw = 0.32  # front panel thickness (right wall)
    ax.add_patch(Rectangle((x1 - pw, y0), pw, h, facecolor=c_neu, edgecolor=e_neu, lw=0.8, zorder=zorder + 1))
    ax.plot([x1 - pw, x0, x0, x1 - pw], [y1, y1, y0, y0], color=wall, lw=1.8, solid_joinstyle="miter", zorder=zorder + 2)
    out = {"inside": (cx - w * 0.12, y0 + h * 0.2)}
    fy = y0 + 0.28
    if grid:  # grid floor: rods in cross section
        k = int(w / 0.32)
        xs = np.linspace(x0 + 0.2, x1 - pw - 0.2, k)
        for x in xs:
            ax.add_patch(Circle((x, fy), 0.06, facecolor=P.muted(), edgecolor="none", zorder=zorder + 2))
        out["floor"] = (float(xs[len(xs) // 3]), fy)
        out["inside"] = (cx - w * 0.12, fy + 0.08)
    else:
        out["floor"] = (cx, y0)
    xp = x1 - pw
    if light:
        ly = y0 + h * 0.78
        fc = P.fill("highlight") if light_on else P.light("neutral")
        ax.add_patch(Wedge((xp, ly), 0.24, 90, 270, facecolor=fc, edgecolor=P.edge("highlight") if light_on else e_neu,
                           lw=0.8, zorder=zorder + 3))
        if light_on:
            for ang in (120, 150, 180, 210, 240):
                a = math.radians(ang)
                ax.plot([xp + 0.33 * math.cos(a), xp + 0.55 * math.cos(a)], [ly + 0.33 * math.sin(a), ly + 0.55 * math.sin(a)],
                        color=line_color("highlight"), lw=1.0, solid_capstyle="round", zorder=zorder + 3)
        out["light"] = (xp - 0.12, ly)
    if key:
        ky = y0 + h * 0.58
        ax.add_patch(Rectangle((xp - 0.07, ky - 0.3), 0.07, 0.6, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.7,
                               zorder=zorder + 3))
        out["key"] = (xp - 0.07, ky)
    if lever:
        ly = y0 + h * 0.36
        lw_, lt = min(0.9, w * 0.13), 0.12
        ax.add_patch(FancyBboxPatch((xp - lw_, ly - lt / 2), lw_, lt, boxstyle="round,pad=0,rounding_size=0.04",
                                    facecolor=P.light("neutral"), edgecolor=wall, lw=0.9, zorder=zorder + 3))
        out["lever"] = (xp - lw_ * 0.6, ly)
    if hopper:
        my, mh = fy + 0.12, 0.55
        ax.add_patch(Rectangle((xp - 0.02, my), pw * 0.8, mh, facecolor=P.mix(e_neu, P.surface(), 0.3), edgecolor=e_neu,
                               lw=0.8, zorder=zorder + 3))
        if pellet:
            ax.add_patch(Circle((xp + 0.1, my + 0.1), 0.08, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.6,
                                zorder=zorder + 4))
        out["magazine"] = (xp + 0.05, my + mh / 2)
        # pellet dispenser outside the front wall, with a delivery tube down to the magazine
        dx, dy = x1 + 0.75, y0 + h * 0.72
        ax.add_patch(FancyBboxPatch((dx - 0.4, dy - 0.3), 0.8, 0.9, boxstyle="round,pad=0,rounding_size=0.08",
                                    facecolor=c_neu, edgecolor=e_neu, lw=0.8, zorder=zorder + 1))
        for j, (px, py) in enumerate(((-0.15, 0.25), (0.12, 0.3), (0.0, 0.05), (-0.18, -0.05), (0.18, 0.02))):
            ax.add_patch(Circle((dx + px, dy + py), 0.07, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.5,
                                zorder=zorder + 2))
        tube = np.array([[dx, dy - 0.3], [dx, my + mh + 0.25], [xp + pw * 0.4, my + mh]])
        ax.plot(tube[:, 0], tube[:, 1], color=e_neu, lw=2.6, solid_capstyle="butt", solid_joinstyle="round", zorder=zorder)
        out["dispenser"] = (dx + 0.4, dy + 0.15)
    if speaker:
        sx, sy = x0 + 0.55, y1 - 0.45
        ax.add_patch(Rectangle((sx - 0.25, sy - 0.17), 0.5, 0.34, facecolor=c_neu, edgecolor=e_neu, lw=0.7, zorder=zorder + 3))
        for rr in (0.35, 0.5):
            t = np.linspace(-0.8, 0.8, 20)
            ax.plot(sx + 0.1 + rr * np.cos(t), sy + rr * np.sin(t) * 0.6, color=P.muted(), lw=0.8, zorder=zorder + 3)
        out["speaker"] = (sx, sy)
    return out


# ------------------------------------------------------------------ collective motion
COUZIN_REGIMES = {
    "swarm": {"ro": 1.05, "ra": 14.0},     # no alignment zone: a cohesive but unordered swarm
    "torus": {"ro": 2.5, "ra": 14.0},      # little alignment, wide attraction: a rotating mill
    "parallel": {"ro": 12.0, "ra": 14.0},  # wide alignment zone: a polarized, travelling group
}


def couzin(n=40, steps=300, rr=1.0, ro=2.0, ra=14.0, speed=3.0, turn=60.0, noise=3.0, blind=90.0, dt=0.1, spread=None,
           aligned=False, seed=0):
    """The Couzin et al. (2002) zone model in two dimensions; returns (pos, head), each (steps + 1, n, 2)."""
    rng = np.random.default_rng(seed)
    spread = spread if spread is not None else 1.2 * math.sqrt(n)
    rad = spread * np.sqrt(rng.random(n))
    th = rng.uniform(0, 2 * np.pi, n)
    pos = np.empty((steps + 1, n, 2))
    head = np.empty((steps + 1, n, 2))
    pos[0] = np.c_[rad * np.cos(th), rad * np.sin(th)]
    h0 = rng.normal(0, 0.3, n) if aligned else rng.uniform(0, 2 * np.pi, n)
    head[0] = np.c_[np.cos(h0), np.sin(h0)]
    cos_vis = math.cos(math.radians((360 - blind) / 2))
    max_turn = math.radians(turn) * dt
    sd = math.radians(noise)
    for s in range(steps):
        x, v = pos[s], head[s]
        d = x[None, :, :] - x[:, None, :]  # d[i, j] = x_j - x_i
        dist = np.hypot(d[..., 0], d[..., 1])
        np.fill_diagonal(dist, np.inf)
        u = d / dist[..., None]
        vis = np.einsum("ijk,ik->ij", u, v) >= cos_vis
        zr = (dist < rr) & vis
        zo = (dist >= rr) & (dist < ro) & vis
        za = (dist >= ro) & (dist < ra) & vis
        dr = -(u * zr[..., None]).sum(1)
        do = v + (v[None, :, :] * zo[..., None]).sum(1)
        da = (u * za[..., None]).sum(1)

        def unit(a):
            nrm = np.hypot(a[:, 0], a[:, 1])[:, None]
            return np.where(nrm > 1e-12, a / np.where(nrm > 1e-12, nrm, 1), 0)

        has_o, has_a = zo.any(1), za.any(1)
        want = np.where(has_o[:, None] & has_a[:, None], 0.5 * (unit(do) + unit(da)),
                        np.where(has_a[:, None], da, np.where(has_o[:, None], do, v)))
        want = np.where(zr.any(1)[:, None], dr, want)
        ang_v = np.arctan2(v[:, 1], v[:, 0])
        ang_w = np.arctan2(want[:, 1], want[:, 0])
        ang_w = np.where(np.hypot(want[:, 0], want[:, 1]) > 1e-12, ang_w, ang_v) + rng.normal(0, sd, n)
        diff = (ang_w - ang_v + np.pi) % (2 * np.pi) - np.pi
        new = ang_v + np.clip(diff, -max_turn, max_turn)
        head[s + 1] = np.c_[np.cos(new), np.sin(new)]
        pos[s + 1] = x + head[s + 1] * speed * dt
    return pos, head


def polarization(head):
    """Group polarization |(1/n) sum v_i| per time step (head: (..., n, 2))."""
    m = np.asarray(head, float).mean(-2)
    return np.hypot(m[..., 0], m[..., 1])


def milling(pos, head):
    """Group angular momentum |(1/n) sum r_ic x v_i| about the centroid (r_ic unit vectors), per time step."""
    pos, head = np.asarray(pos), np.asarray(head)
    r = pos - pos.mean(-2, keepdims=True)
    r = r / np.maximum(np.hypot(r[..., 0], r[..., 1]), 1e-12)[..., None]
    return np.abs((r[..., 0] * head[..., 1] - r[..., 1] * head[..., 0]).mean(-1))


def zones(ax, center, rr, ro, ra, heading=90.0, blind=90.0, tokens=("negative", "dna", "positive"), labels=True,
          size="tiny", zorder=6):
    """The repulsion / orientation / attraction zones around a focal agent (canvas heading in degrees, CCW from +x),
    with the rear blind sector left blank."""
    t1, t2 = heading - (360 - blind) / 2, heading + (360 - blind) / 2
    for (r_out, r_in), tok in zip(((ra, ro), (ro, rr), (rr, 0)), tokens[::-1]):
        ax.add_patch(Wedge(center, r_out, t1, t2, width=r_out - r_in, facecolor=_tint(tok, 0.72 if P.is_dark() else 0.45),
                           edgecolor=P.edge(tok), lw=0.8, zorder=zorder))
    hx, hy = math.cos(math.radians(heading)), math.sin(math.radians(heading))
    agent(ax, center, (hx, hy), size=rr * 0.45, token="ink", zorder=zorder + 3)
    if labels:  # along the heading, in front of the agent
        cx, cy = center
        tc = P.on_fill() if not P.is_dark() else P.ink()
        for r_, text in ((rr * 0.68, "repulsion"), ((rr + ro) / 2, "orientation"), ((ro + ra) / 2, "attraction")):
            label(ax, (cx + r_ * hx, cy + r_ * hy), text, size=size, color=tc, zorder=zorder + 4)
        label(ax, (cx - ra * 0.6 * hx, cy - ra * 0.6 * hy), "blind\nzone", size=size, color=P.muted(), zorder=zorder + 4)


def agent(ax, xy, heading, size=0.3, token="dna", zorder=14):
    """One agent drawn as a small dart pointing along ``heading`` (a vector)."""
    hx, hy = heading
    nrm = math.hypot(hx, hy) or 1.0
    u = np.array([hx, hy]) / nrm
    v = np.array([-u[1], u[0]])
    p = np.asarray(xy, float)
    pts = [p + u * size * 0.6, p - u * size * 0.4 + v * size * 0.32, p - u * size * 0.2, p - u * size * 0.4 - v * size * 0.32]
    col = line_color(token)
    ax.add_patch(Polygon(pts, closed=True, facecolor=col, edgecolor=col, lw=0.4, zorder=zorder))


def fit(points, box, pad=0.05):
    """A function mapping simulation coordinates into the canvas box (x0, y0, w, h), equal aspect, centred.
    ``points`` is an array (..., 2) or a list of such arrays giving the extent to fit."""
    arr = np.vstack([np.asarray(p, float).reshape(-1, 2) for p in (points if isinstance(points, (list, tuple)) else [points])])
    lo, hi = arr.min(0), arr.max(0)
    span = np.maximum(hi - lo, 1e-9)
    x0, y0, w, h = box
    s = min(w / span[0], h / span[1]) * (1 - 2 * pad)
    mid_d, mid_c = (lo + hi) / 2, np.array([x0 + w / 2, y0 + h / 2])

    def to(p):
        return (np.asarray(p, float) - mid_d) * s + mid_c

    to.scale = s
    return to


def trail(ax, pts, token="rna", lw=1.4, fade=True, arrows=0, head=0.22, start=None, end=None, zorder=12):
    """A trajectory in canvas units; with ``fade`` its older part blends into the background. ``arrows`` places
    that many direction heads along it; ``start`` / ``end`` = "o" (open circle), "." (dot) or "*" (star)."""
    pts = np.asarray(pts, float)
    col = line_color(token)
    segs = np.stack([pts[:-1], pts[1:]], axis=1)
    if fade and len(segs) > 1:
        f = np.linspace(0.85, 0.0, len(segs))
        cols = [P.mix(col, P.surface(), x) for x in f]
    else:
        cols = col
    ax.add_collection(LineCollection(segs, colors=cols, linewidths=lw, capstyle="round", joinstyle="round", zorder=zorder))
    if arrows:
        s = np.r_[0, np.cumsum(np.hypot(*np.diff(pts, axis=0).T))]
        for k in range(arrows):
            target = s[-1] * (k + 1) / (arrows + 1)
            i = int(np.clip(np.searchsorted(s, target), 2, len(pts) - 1))
            j = max(0, i - 3)
            c = P.mix(col, P.surface(), 0.85 * (1 - i / len(pts))) if fade else col
            arrow(ax, pts[j], pts[i], kind="process", color=c, lw=0, head=head, zorder=zorder + 1)
    for spec, p in ((start, pts[0]), (end, pts[-1])):
        if spec == "o":
            ax.add_patch(Circle(p, head * 0.45, facecolor=P.surface(), edgecolor=col, lw=1.0, zorder=zorder + 2))
        elif spec == ".":
            ax.add_patch(Circle(p, head * 0.4, facecolor=col, edgecolor=col, lw=0.5, zorder=zorder + 2))
        elif spec == "*":
            ax.plot([p[0]], [p[1]], marker="*", ms=8, color=col, markeredgecolor=col, zorder=zorder + 2)


def school(ax, pos, head, to, frame=-1, tail=25, token="dna", size=0.28, lw=0.8):
    """Trails of the last ``tail`` steps and the agents at ``frame`` of a ``couzin`` run, mapped by ``to``."""
    pos, head = np.asarray(pos), np.asarray(head)
    f = frame % len(pos)
    a = max(0, f - tail)
    for i in range(pos.shape[1]):
        trail(ax, to(pos[a:f + 1, i]), token=token, lw=lw, fade=True)
        agent(ax, to(pos[f, i]), head[f, i], size=size, token=token)


def path_integration(steps=220, step=1.0, turn_sd=0.45, seed=0, error=0.0, displace=None, search=True, loops=5):
    """A central-place forager's foray, homing run and search (see the module doc). Units: steps."""
    rng = np.random.default_rng(seed)
    h = rng.uniform(0, 2 * np.pi)
    p = np.zeros(2)
    est = np.zeros(2)
    out = [p.copy()]
    for _ in range(steps):
        h += rng.normal(0, turn_sd)
        d = step * np.array([math.cos(h), math.sin(h)])
        p = p + d
        e = math.radians(rng.normal(0, error)) if error else 0.0
        est = est + step * np.array([math.cos(h + e), math.sin(h + e)])
        out.append(p.copy())
    out = np.array(out)
    vec = -est
    rel = out[-1] + (np.asarray(displace, float) if displace is not None else 0.0)
    fict = rel + vec
    k = max(2, int(np.hypot(*vec) / step))
    homing = rel + np.linspace(0, 1, k + 1)[:, None] * vec
    res = {"outbound": out, "homing": homing, "vector": vec, "release": rel, "fictive": fict, "nest": np.zeros(2)}
    if search:
        pts = [fict]
        ang = math.atan2(vec[1], vec[0])
        size = 0.05 * max(np.hypot(*vec), 5 * step)
        for j in range(loops):
            ang += 2.39996  # golden angle: loops in all directions
            R = size * (1 + 0.5 * j)
            t = np.linspace(0, 2 * np.pi, 40)
            dir_, perp = np.array([math.cos(ang), math.sin(ang)]), np.array([-math.sin(ang), math.cos(ang)])
            loop = fict + R * ((1 - np.cos(t))[:, None] * dir_ * 0.6 + np.sin(t)[:, None] * perp * 0.4)
            pts.extend(loop[1:])
        res["search"] = np.array(pts)
    return res


# ------------------------------------------------------------------ signal detection
def sdt_rates(d=1.5, xc=0.75):
    """(hit rate, false-alarm rate) for noise ~ N(0, 1), signal ~ N(d, 1) and a criterion at ``xc``."""
    return float(norm.sf(xc - d)), float(norm.sf(xc))


def dprime(H, F):
    """Sensitivity d' = z(H) - z(F)."""
    return float(norm.ppf(H) - norm.ppf(F))


def bias(H, F):
    """Response bias c = -(z(H) + z(F)) / 2 (positive = conservative)."""
    return float(-(norm.ppf(H) + norm.ppf(F)) / 2)


def sdt_panel(p, d=1.5, xc=0.75, noise_token="neutral", signal_token="dna", fa_token="negative", labels=True,
              rates=True, size="tiny"):
    """Equal-variance signal detection on a ``quant.Plot`` (see the module doc). Returns (H, F)."""
    x = np.linspace(p.xlim[0], p.xlim[1], 400)
    fn, fs = norm.pdf(x), norm.pdf(x, d)
    m = x >= xc
    xm = np.r_[xc, x[m]]
    p.band(xm, np.zeros_like(xm), norm.pdf(xm, d), signal_token, alpha=0.4)
    p.band(xm, np.zeros_like(xm), norm.pdf(xm), fa_token, alpha=0.55)
    p.line(x, fn, noise_token if noise_token != "neutral" else "muted", lw=1.6)
    p.line(x, fs, signal_token, lw=1.8)
    top = norm.pdf(0)
    p.ax.plot([p.X(xc)] * 2, [p.Y(0), p.Y(min(p.ylim[1], top * 1.0))], color=P.ink(), lw=1.2, zorder=p.z + 4)
    H, F = sdt_rates(d, xc)
    if labels:
        p.text(xc + 0.08, top * 0.66, "criterion", ha="left", size=size)
        p.text(-1.2, top * 0.9, "noise", ha="right", token=noise_token if noise_token != "neutral" else "muted")
        p.text(d + 1.2, top * 0.9, "signal + noise", ha="left", token=signal_token)
        yb = top * 1.06
        p.ax.plot([p.X(0), p.X(d)], [p.Y(yb)] * 2, color=P.muted(), lw=0.8, zorder=p.z + 3)
        for xx in (0, d):
            p.ax.plot([p.X(xx)] * 2, [p.Y(yb) - 0.08, p.Y(yb) + 0.08], color=P.muted(), lw=0.8, zorder=p.z + 3)
        p.text(d / 2, yb, "d′", va="bottom", color=P.muted())
        xh = max(xc, d) + 0.55
        p.text(xh, norm.pdf(xh, d) * 0.45, "hits" + (f" {H:.2f}" if rates else ""), ha="left", token=signal_token,
               size=size)
        xf = xc + 0.3
        callout(p.ax, p.xy(xf, norm.pdf(xf) * 0.35), p.xy(d + 2.0, top * 0.3),
                "false alarms" + (f" {F:.2f}" if rates else ""), size=size)
    return H, F


def roc_panel(p, dprimes=(0.5, 1.0, 2.0), tokens=("dna", "protein", "rna"), points=(), labels=True, size="tiny"):
    """ROC curves (hit rate against false-alarm rate) for equal-variance Gaussian SDT on a unit-square
    ``quant.Plot``; ``points`` = [(F, H)] or [(F, H, token)] marks observed operating points."""
    p.line([0, 1], [0, 1], "muted", lw=0.9, dashed=True)
    c = np.linspace(-5, 6, 300)
    for k, d in enumerate(dprimes):
        tok = tokens[k % len(tokens)]
        F, H = norm.sf(c), norm.sf(c - d)
        p.line(F, H, tok, lw=1.7)
        if labels:
            i = int(np.argmin(np.abs(F - 0.22 + 0.04 * k)))
            p.text(F[i] + 0.03, H[i] - 0.02, f"d′ = {d:g}", ha="left", va="top", token=tok, size=size)
    for q in points:
        F, H = q[0], q[1]
        tok = q[2] if len(q) > 2 else "ink"
        p.points([F], [H], tok, r=0.09)
    if labels:
        p.text(0.62, 0.55, "chance", color=P.muted(), rotation=0, ha="left", size=size)


__all__ = ["vonmises", "mean_direction", "rayleigh", "v_test", "emlen_funnel", "circular_plot", "simulate_activity",
           "Actogram", "arm_maze", "t_maze", "y_maze", "plus_maze", "radial_maze", "water_maze", "swim_path", "operant_box",
           "COUZIN_REGIMES", "couzin", "polarization", "milling", "zones", "agent", "fit", "trail", "school",
           "path_integration", "sdt_rates", "dprime", "bias", "sdt_panel", "roc_panel"]
