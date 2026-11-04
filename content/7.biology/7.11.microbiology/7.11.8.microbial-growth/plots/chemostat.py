# The chemostat in practice: washout and competition for the limiting nutrient.
# A: the apparatus (schematic): a medium reservoir with the limiting nutrient at s0, a pump setting the flow
#    F, a stirred, aerated culture vessel of volume V and an overflow; dilution rate D = F / V.
# B: response of a culture at steady state (D = 0.4 per h) to a step change of the pump at t = 0, from the
#    chemostat equations with Monod kinetics (mu_max = 1.0 per h, Ks = 0.1 mM, s0 = 5 mM, yield 0.09 g per
#    mmol): to D = 0.8 per h the biomass settles at a new, slightly lower steady state after a transient;
#    to D = 1.05 per h, above the critical dilution rate D_c = mu_max s0 / (Ks + s0) = 0.98 per h, the
#    cells are diluted faster than they can grow and wash out, decaying as exp(-(D - mu(s0)) t).
# C: two species limited by the same nutrient (Monod curves): species 1 (mu_max = 0.6 per h, Ks = 0.02 mM)
#    is a scavenger, species 2 (mu_max = 1.2 per h, Ks = 0.5 mM) grows fast only at high concentration.
#    The break-even concentration R* = Ks D / (mu_max - D) at which each species grows exactly at the
#    dilution rate is marked for D = 0.3 and D = 0.65 per h (species 1 cannot grow at all faster than 0.6 per h).
# D: competition in the chemostat started from equal small inocula: the species with the lower R* at the
#    chosen D excludes the other; which species wins depends on D (the R* curves cross at D = 0.575 per h).
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(14.0, 4.2))
gs = fig.add_gridspec(1, 4, width_ratios=[1.15, 1.1, 1.0, 1.1], wspace=0.42)

# ---- A: apparatus --------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(0, 11)
ax.set_ylim(0, 10.5)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   The chemostat")
glass = dict(facecolor="none", edgecolor=P.ink(), lw=1.2)
med = P.mix(P.fill("carbohydrate"), P.surface(), 0.55)
cult = P.mix(P.fill("bacterium"), P.surface(), 0.45)
# reservoir
ax.add_patch(Rectangle((0.4, 5.6), 2.4, 3.4, facecolor=med, edgecolor="none"))
ax.add_patch(FancyBboxPatch((0.4, 5.6), 2.4, 3.9, boxstyle="round,pad=0,rounding_size=0.2", **glass))
bio.label(ax, (1.6, 6.9), "fresh\nmedium\n$s_0$", size="small")
# pump
ax.add_patch(plt.Circle((4.3, 8.6), 0.55, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.1))
bio.label(ax, (4.3, 8.6), "P", size="small", bold=True, color=P.on_fill())
bio.label(ax, (4.3, 9.55), "pump: flow $F$", size="tiny")
ax.plot([2.3, 2.3, 3.75], [8.0, 8.6, 8.6], color=P.ink(), lw=1.0)
ax.plot([4.85, 6.4, 6.4], [8.6, 8.6, 6.6], color=P.ink(), lw=1.0)
bio.arrow(ax, (6.4, 7.2), (6.4, 6.4), kind="process", lw=1.0, head=0.18)
# vessel
ax.add_patch(Rectangle((4.6, 1.2), 3.6, 3.7, facecolor=cult, edgecolor="none"))
ax.add_patch(FancyBboxPatch((4.6, 1.2), 3.6, 4.9, boxstyle="round,pad=0,rounding_size=0.25", **glass))
rng = np.random.default_rng(3)
for _ in range(26):
    x, y = rng.uniform(4.9, 7.9), rng.uniform(1.5, 4.6)
    ax.add_patch(plt.Circle((x, y), 0.07, color=P.edge("bacterium"), lw=0))
ax.plot([6.4, 6.4], [6.1, 1.9], color=P.muted(), lw=1.0)
ax.plot([5.9, 6.9], [1.9, 1.9], color=P.muted(), lw=2.2)
bio.label(ax, (6.4, 0.6), "culture vessel, volume $V$", size="tiny")
# overflow at the liquid surface
ax.plot([8.2, 9.9, 9.9], [4.75, 4.75, 3.2], color=P.ink(), lw=1.0)
bio.arrow(ax, (9.9, 3.6), (9.9, 2.6), kind="process", lw=1.0, head=0.18)
bio.label(ax, (9.9, 1.7), "overflow:\ncells and\nmedium", size="tiny")
# air
ax.plot([5.2, 5.2], [6.6, 1.6], color=P.muted(), lw=0.9, ls=(0, (3, 2)))
bio.label(ax, (5.0, 6.9), "air", size="tiny", color=P.muted())
bio.label(ax, (2.1, 3.6), "$D = F/V$", size="normal")
bio.label(ax, (2.1, 2.6), "growth rate\nset by $D$", size="tiny", color=P.muted())

# ---- model ------------------------------------------------------------------------------------------
mu_max, Ks, s0, Y = 1.0, 0.1, 5.0, 0.09
Dc = mu_max * s0 / (Ks + s0)


def run(D, x0, sv0, T):
    def f(_, u):
        x, s = u
        mu = mu_max * s / (Ks + s)
        return [(mu - D) * x, D * (s0 - s) - mu * x / Y]

    sol = solve_ivp(f, (0, T), [x0, sv0], max_step=0.05, rtol=1e-8, atol=1e-12)
    return sol.t, sol.y


D0 = 0.4
s_star = Ks * D0 / (mu_max - D0)
x_star = Y * (s0 - s_star)
ax = fig.add_subplot(gs[0, 1])
for D, tok, name in ((0.8, "positive", "step to $D$ = 0.8 h$^{-1}$"), (1.05, "negative", "step to $D$ = 1.05 h$^{-1}$ > $D_{\\mathrm{c}}$")):
    t, (x, s) = run(D, x_star, s_star, 24)
    ax.plot(t, x, color=charts.line(tok), lw=2.0, label=name)
ax.axhline(x_star, color=P.muted(), lw=0.7, ls=":")
ax.text(23.5, x_star * 1.03, "initial steady state", ha="right", fontsize=6.8, color=P.muted())
ax.set_ylim(0, 0.52)
ax.legend(fontsize=6.8, frameon=False, loc="lower left")
charts.style_axes(ax, "time after the step / h", "biomass $x$ / (g L$^{-1}$)")
charts.title(ax, "B   Steady state and washout")

# ---- C: R* of two species -----------------------------------------------------------------------------
sp = [(0.6, 0.02, "dna", "species 1 (scavenger)"), (1.2, 0.5, "drug", "species 2 (fast at high $s$)")]
ax = fig.add_subplot(gs[0, 2])
s = np.linspace(0, 1.6, 400)
for m, k, tok, name in sp:
    ax.plot(s, m * s / (k + s), color=charts.line(tok), lw=2.0, label=name)
for D, ls in ((0.3, "--"), (0.65, ":")):
    ax.axhline(D, color=P.muted(), lw=0.8, ls=ls)
    ax.text(1.58, D + 0.015, f"$D$ = {D}", ha="right", va="bottom", fontsize=6.8, color=P.muted())
    for m, k, tok, _ in sp:
        if m <= D:
            continue
        r = k * D / (m - D)
        ax.plot([r], [D], "o", ms=4, color=charts.line(tok))
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 1.0)
ax.legend(fontsize=6.8, frameon=False, loc="upper left")
charts.style_axes(ax, "nutrient $s$ / mM", "growth rate $\\mu$ / h$^{-1}$")
charts.title(ax, "C   Break-even concentration $R^*$")

# ---- D: competition ---------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 3])


def compete(D, T=120):
    def f(_, u):
        x1, x2, sv = u
        m1 = sp[0][0] * sv / (sp[0][1] + sv)
        m2 = sp[1][0] * sv / (sp[1][1] + sv)
        return [(m1 - D) * x1, (m2 - D) * x2, D * (s0 - sv) - (m1 * x1 + m2 * x2) / Y]

    sol = solve_ivp(f, (0, T), [1e-3, 1e-3, s0], method="LSODA", max_step=0.1, rtol=1e-8, atol=1e-14)
    return sol.t, sol.y


for D, ls in ((0.3, "-"), (0.65, "--")):
    t, (x1, x2, _) = compete(D)
    ax.plot(t, x1, color=charts.line(sp[0][2]), lw=1.8, ls=ls)
    ax.plot(t, x2, color=charts.line(sp[1][2]), lw=1.8, ls=ls)
ax.set_yscale("log")
ax.set_ylim(1e-6, 1)
ax.plot([], [], color=P.muted(), ls="-", label="$D$ = 0.3 h$^{-1}$: species 1 wins")
ax.plot([], [], color=P.muted(), ls="--", label="$D$ = 0.65 h$^{-1}$: species 2 wins")
ax.legend(fontsize=6.8, frameon=False, loc="center right")
charts.style_axes(ax, "time / h", "biomass / (g L$^{-1}$)")
charts.title(ax, "D   Competitive exclusion")
