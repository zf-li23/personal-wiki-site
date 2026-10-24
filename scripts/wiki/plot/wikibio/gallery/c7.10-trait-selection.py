# Three modes of natural selection on a quantitative trait z (standardized: mean 0, SD 1), each from a
# simulated cohort of 600 individuals (seeds 21, 22, 23) whose survival is a Bernoulli draw with the true
# fitness function (dashed). Top: survival in bins of 0.5 SD (dots, 95 % Wilson intervals) and the
# maximum-likelihood logistic regression on z and z^2 (solid). Bottom: the trait distribution before
# selection (grey) and among survivors (green), with the selection differential S = mean shift. The
# Lande-Arnold (1983) gradients come from regressing relative fitness on z (beta) and on z and z^2/2
# (gamma): directional selection gives beta > 0, stabilizing gamma < 0, disruptive gamma > 0. For
# directional selection the offspring mean follows the breeder's equation R = h^2 S (h^2 = 0.5, dashed).
# Examples: beak depth of Geospiza fortis in the 1977 drought on Daphne Major (directional), human birth
# weight (stabilizing), bimodal beak size of G. fortis at El Garrapatero (disruptive).
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import evolution as evo
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25.0, 13.2)
n, h2 = 600, 0.5
zz = np.linspace(-3.2, 3.2, 400)
modes = [
    ("directional", dict(theta=0.0, strength=1.6), 21, "Directional", "beak depth, drought 1977", "phylopic/darwin-finch"),
    ("stabilizing", dict(theta=0.0, width=1.0), 22, "Stabilizing", "human birth weight", "phylopic/human"),
    ("disruptive", dict(theta=0.0, width=0.75, strength=0.85), 23, "Disruptive", "beak size, El Garrapatero",
     "phylopic/darwin-finch"),
]
edges = np.arange(-3.0, 3.01, 0.4)
before_tok, after_tok = "neutral", "positive"

for k, (mode, kw, seed, title, example, icon_id) in enumerate(modes):
    x0 = 1.6 + k * 8.0
    rng = np.random.default_rng(seed)
    z = rng.normal(0, 1, n)
    alive = rng.random(n) < evo.fitness(z, mode, **kw)
    la = evo.lande_arnold(z, alive)
    coef, se, pred = evo.logistic_fit(z, alive, degree=2)

    # header
    bio.panel(ax, "ABC"[k], (x0 - 1.4, 13.05))
    bio.label(ax, (x0, 12.45), title, size="normal", bold=True, ha="left")
    bio.label(ax, (x0, 11.85), example, size="tiny", ha="left", color=P.muted())
    if icon_id == "phylopic/human":
        bio.icon(ax, "phylopic/human", at=(x0 + 6.1, 12.0), height=1.3, color="animal")
    else:
        bio.icon(ax, "phylopic/darwin-finch", at=(x0 + 5.9, 12.0), height=0.95, color="animal", flip=k == 2)

    # fitness: binned survival with Wilson intervals, fitted and true curves
    pf = quant.Plot(ax, (x0, 7.75, 6.4, 3.3), (-3.2, 3.2), (0, 1.05), ylabel="survival" if k == 0 else None,
                    yticks=[0, 0.5, 1] if k == 0 else [(0, ""), (0.5, ""), (1, "")], xticks=[(v, "") for v in (-2, 0, 2)])
    pf.line(zz, evo.fitness(zz, mode, **kw), "muted", lw=1.2, dashed=True)
    pf.line(zz, pred(zz), after_tok, lw=1.9)
    for a, b in zip(edges[:-1], edges[1:]):
        m = (z >= a) & (z < b)
        if m.sum() < 10:
            continue
        lo, hi = evo.wilson(int(alive[m].sum()), int(m.sum()))
        X = float(pf.X((a + b) / 2))
        ax.plot([X, X], [pf.Y(lo), pf.Y(hi)], color=P.ink(), lw=0.8, zorder=pf.z + 2)
        pf.points([(a + b) / 2], [alive[m].mean()], "ink", r=0.07)
    if k == 0:
        pf.legend([("logistic fit", after_tok, "-"), ("true fitness", "muted", "--")], at=(x0 + 0.25, 10.75))

    # distributions before and after selection
    hb, _ = np.histogram(z, edges)
    ha, _ = np.histogram(z[alive], edges)
    pd = quant.Plot(ax, (x0, 2.65, 6.4, 4.4), (-3.2, 3.2), (0, 130), xlabel="trait $z$ / SD",
                    ylabel="individuals" if k == 0 else None, xticks=[-2, 0, 2],
                    yticks=[0, 50, 100] if k == 0 else [(0, ""), (50, ""), (100, "")])
    pd.bars(edges, hb, before_tok, lw=0.5, alpha=0.45 if P.is_dark() else 1.0)  # pale grey glares on the dark surface
    pd.bars(edges, ha, after_tok, lw=0.5)
    m0, m1 = z.mean(), z[alive].mean()
    v0, v1 = z.var(), z[alive].var()
    for mval, tok in ((m0, "muted"), (m1, after_tok)):
        X = float(pd.X(mval))
        ax.plot([X, X], [pd.Y(0), pd.Y(118)], color=quant.line_color(tok), lw=1.1, ls=(0, (3, 2)), zorder=pd.z + 2)
    S = m1 - m0
    if abs(S) > 0.08:
        bio.arrow(ax, pd.xy(m0, 122), pd.xy(m1, 122), kind="process", head=0.16, lw=1.1, color=quant.line_color(after_tok))
    pd.text((m0 + m1) / 2 + (0.15 if abs(S) <= 0.08 else 0), 124, f"$S = {S:+.2f}$".replace("-", "−"), va="bottom",
            ha="center" if abs(S) > 0.08 else "left", token=after_tok)
    if mode == "directional":
        # offspring: same shape, mean shifted by R = h^2 S (breeder's equation, infinitesimal model)
        R = h2 * S
        dens = evo.normal_pdf(zz, m0 + R, np.sqrt(v0)) * n * 0.4
        pd.line(zz, dens, "dna", lw=1.5, dashed=True)
        pd.text(-3.0, 112, f"offspring: $R = h^2 S = {R:.2f}$", token="dna", ha="left")
        for j, (tok, name) in enumerate(((before_tok, "before selection"), (after_tok, "survivors"))):
            x, y = pd.xy(-3.0, 96 - j * 12)
            ax.add_patch(Rectangle((x, y - 0.12), 0.35, 0.24, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5,
                                   alpha=0.45 if (P.is_dark() and tok == before_tok) else None, zorder=pd.z + 2))
            bio.label(ax, (x + 0.48, y), name, size="tiny", ha="left")
    # statistics
    bio.label(ax, (x0, 1.4), f"$\\beta = {la['beta']:.2f} \\pm {la['beta_se']:.2f}$     "
              f"$\\gamma = {la['gamma']:.2f} \\pm {la['gamma_se']:.2f}$".replace("-", "−"), size="small", ha="left")
    bio.label(ax, (x0, 0.85), f"survival {alive.mean():.0%},  variance among survivors {v1 / v0:.2f} × before",
              size="tiny", ha="left", color=P.muted())

