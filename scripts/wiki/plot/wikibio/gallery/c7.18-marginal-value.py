# Optimal patch use: the marginal value theorem (Charnov 1976). (A) A bee forages in patches of flowers
# separated by a travel time tau; inside a patch the gain rate falls as nectar is depleted, so its time budget
# alternates travel and residence. (B) Cumulative gain g(t) = G (1 - exp(-r t)) in one patch; the residence
# time t* that maximizes the long-term rate R = g(t) / (tau + t) is where the line from (-tau, 0) is tangent
# to g. A longer travel time gives a longer optimal stay. (C) The same optimum seen as rates: R(t) peaks
# exactly where the marginal gain rate g'(t) has fallen to R* (leave when the patch is no better than average).
import numpy as np

import wikibio as bio
from wikibio import behaviour as bh
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27.0, 10.2)
G, RATE = 10.0, 0.08
g = bh.gain(G, RATE)
TAUS, TOKS = (5.0, 20.0), ("dna", "rna")
opt = [bh.mvt_optimum(g, tau, 60) for tau in TAUS]

# ---- A: patches and the time budget ------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.1))
c1, c2, c3 = (1.8, 7.3), (6.5, 7.6), (4.4, 4.0)
bh.patch(ax, c1, 1.15, n=5, depleted=4, seed=1)
bh.patch(ax, c2, 1.15, n=5, depleted=2, seed=2)
bh.patch(ax, c3, 1.15, n=5, depleted=0, seed=3)
bio.label(ax, (c1[0], c1[1] - 1.4), "left behind", size="tiny", color=P.muted(), va="top")
bio.label(ax, (c2[0] + 0.1, c2[1] - 1.4), "being depleted", size="tiny", color=P.muted(), va="top")
bio.label(ax, (c3[0], c3[1] - 1.4), "next patch (full)", size="tiny", color=P.muted(), va="top")
bio.arrow(ax, (c1[0] + 1.25, c1[1] + 0.25), (c2[0] - 1.3, c2[1] + 0.15), kind="process", dashed=True, bend=-0.18,
          color=quant.line_color("dna"), lw=1.3)
bio.label(ax, ((c1[0] + c2[0]) / 2, 6.85), "travel  τ", size="small", color=quant.line_color("dna"))
bio.arrow(ax, (c2[0] - 0.4, c2[1] - 1.85), (c3[0] + 1.05, c3[1] + 0.6), kind="process", dashed=True, bend=-0.15,
          color=quant.line_color("dna"), lw=1.3)
bio.icon(ax, "phylopic/honey-bee", at=(c2[0] + 0.75, c2[1] + 1.05), height=0.85, color="atp", rotate=-15)
bio.label(ax, (c2[0] + 1.35, c2[1] - 0.2), "residence\n$t$", size="small", ha="left", color=quant.line_color("positive"))
# time budget
y = 1.35
bio.label(ax, (0.4, y + 0.55), "Time budget", size="tiny", ha="left", color=P.muted())
seg = []
for k in range(3):
    seg += [(0.75, "dna2", "τ"), (1.35, "positive", "t")]
bh.timeline(ax, 0.4, y, seg)
bio.label(ax, (4.6, y - 0.55), "$R = \\dfrac{g(t)}{\\tau + t}$  per cycle", size="small", va="top")

# ---- B: gain curve and tangent construction --------------------------------------------------------------------
X0, Y0, W, H = 11.0, 1.6, 7.4, 6.9
pb = quant.Plot(ax, (X0, Y0, W, H), (-25, 60), (0, 11), xlabel="time / s", ylabel="Energy gained in the patch  $g(t)$",
                xticks=[0, 20, 40, 60], yticks=[0, 5, 10])
bio.panel(ax, "B", (X0 - 1.5, 10.1))
pb.span(-25, 0, "neutral", strength=0.82)
pb.text(-12.5, 10.6, "travel (−τ to 0)", va="top", color=P.muted())
pb.text(30, 10.6, "residence in patch", va="top", color=P.muted())
res = bh.mvt_panel(pb, g, TAUS, TOKS)
pb.hline(G, dashed=True, text="$G$", side="right")
for (tau, ts, rs), tok, dx, dy in zip(res, TOKS, (2.5, 1.5), (-1.5, -0.9)):
    gx = float(g(ts))
    pb.text(ts + dx, gx + dy, f"τ = {tau:g} s:  $t^*$ = {ts:.1f} s", token=tok, ha="left", va="center")
    pb.text(-tau, -0.35, f"−{tau:g}", token=tok, va="top")
pb.text(58, 1.2, f"$g(t) = G\\,(1 - \\mathrm{{e}}^{{-rt}})$,  $r$ = {RATE:g} s⁻¹", ha="right", color=P.muted())

# ---- C: rates -----------------------------------------------------------------------------------------------
X1 = 21.0
pc = quant.Plot(ax, (X1, Y0, 5.6, H), (0, 60), (0, 0.85), xlabel="Residence time $t$ / s", ylabel="Rate / s⁻¹",
                xticks=[0, 20, 40, 60], yticks=[0, 0.2, 0.4, 0.6, 0.8], ylabel_offset=0.85)
bio.panel(ax, "C", (X1 - 1.5, 10.1))
t = np.linspace(0.01, 60, 400)
pc.line(t, g.d(t), "ink", lw=1.6, dashed=True)
pc.text(3.5, 0.74, "marginal rate $g'(t)$", ha="left")
for (tau, ts, rs), tok, at in zip(res, TOKS, (0.95, 0.95)):
    pc.line(t, g(t) / (tau + t), tok, lw=2.2)
    pc.points([ts], [rs], tok, r=0.12, zorder=pc.z + 5)
    pc.line([ts, ts], [0, rs], tok, lw=0.9, dotted=True)
    above = tau < 10
    pc.text(ts + 4, rs + (0.03 if above else -0.04), f"$R(t)$, τ = {tau:g} s", token=tok, ha="left",
            va="bottom" if above else "top")
pc.text(12.5, 0.47, "optimum: $g'(t^*) = R^*$", ha="left")
