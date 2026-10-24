# The hawk-dove game (Maynard Smith & Price 1973). (A) Two strategies contest a resource of value V: hawks
# escalate and risk an injury of cost C; doves display and retreat. The table gives the payoff to the focal
# player. (B) Expected payoffs against a population with hawk frequency p: hawks do better when rare, worse
# when common, so the payoffs cross at p* = V / C (here V = 2, C = 3). (C) Replicator dynamics
# dp/dt = p (1 - p) (W_H - W_D) carry every mixed population to p*, the evolutionarily stable state; the
# phase line (right) shows p = 0 and p = 1 as unstable and p* as stable.
import numpy as np

import wikibio as bio
from wikibio import behaviour as bh
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27.0, 10.2)
V, C = 2.0, 3.0
M = bh.hawk_dove(V, C)
PSTAR = V / C
HAWK, DOVE = "rna", "dna"

# ---- A: the contest and its payoff matrix --------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.1))
bio.icon(ax, "phylopic/pigeon", at=(2.6, 8.4), height=1.3, color=HAWK)
bio.icon(ax, "phylopic/pigeon", at=(6.2, 8.4), height=1.3, color=DOVE, flip=True)
bio.label(ax, (2.6, 7.35), "Hawk", size="normal", bold=True, color=quant.line_color(HAWK), va="top")
bio.label(ax, (2.6, 6.85), "escalates; wins or is injured", size="tiny", va="top", color=P.muted())
bio.label(ax, (6.2, 7.35), "Dove", size="normal", bold=True, color=quant.line_color(DOVE), va="top")
bio.label(ax, (6.2, 6.85), "displays; retreats from hawks", size="tiny", va="top", color=P.muted())
cells = [["$(V - C)/2$", "$V$"], ["$0$", "$V/2$"]]
bh.payoff_matrix(ax, (5.15, 3.75), ["Hawk", "Dove"], cells, w=2.1, h=1.0, tokens=[HAWK, DOVE])
bio.label(ax, (4.4, 1.55), "$V$: value of the resource,  $C$: cost of injury", size="tiny", color=P.muted())
bio.label(ax, (4.4, 1.05), f"$C > V$: no pure ESS;  here $V$ = {V:g}, $C$ = {C:g}", size="tiny", color=P.muted())

# ---- B: payoffs against the population ------------------------------------------------------------------
X0, Y0, W, H = 11.0, 1.6, 6.6, 6.9
pb = quant.Plot(ax, (X0, Y0, W, H), (0, 1), (-0.8, 2.2), xlabel="Hawk frequency $p$", ylabel="Expected payoff $W$",
                xticks=[0, 0.5, 1], yticks=[-0.5, 0, 0.5, 1, 1.5, 2])
bio.panel(ax, "B", (X0 - 1.5, 10.1))
p = np.linspace(0, 1, 200)
wh, wd = bh.fitness(M, p)
pb.hline(0, dashed=False, lw=0.6)
pb.span(0, PSTAR, "positive", strength=0.85)
pb.line(p, wh, HAWK, lw=2.4)
pb.line(p, wd, DOVE, lw=2.4)
pb.text(0.12, 2.0, "$W_{\\mathrm{H}} = p\\,(V - C)/2 + (1 - p)\\,V$", token=HAWK, ha="left", va="bottom")
pb.text(0.03, 1.03, "$W_{\\mathrm{D}} = (1 - p)\\,V/2$", token=DOVE, ha="left", va="bottom")
ws = float(bh.fitness(M, PSTAR)[0])
pb.line([PSTAR, PSTAR], [-0.8, ws], "ink", lw=0.9, dotted=True)
pb.points([PSTAR], [ws], "ink", r=0.13, zorder=pb.z + 6)
pb.text(PSTAR + 0.03, -0.62, "$p^* = V/C$", ha="left", va="center")
pb.text(PSTAR / 2, -0.3, "$W_{\\mathrm{H}} > W_{\\mathrm{D}}$:\nhawks spread", va="center", color=P.muted())
pb.text((1 + PSTAR) / 2, 1.2, "doves\nspread", va="center", color=P.muted())

# ---- C: replicator dynamics -------------------------------------------------------------------------------
X1 = 20.6
pc = quant.Plot(ax, (X1, Y0, 4.9, H), (0, 12), (0, 1), xlabel="Time (generations)", ylabel="Hawk frequency $p$",
                xticks=[0, 4, 8, 12], yticks=[0, 0.5, 1], ylabel_offset=0.75)
bio.panel(ax, "C", (X1 - 1.5, 10.1))
t = np.linspace(0, 12, 600)
for p0 in (0.02, 0.15, 0.35, 0.95, 0.99):
    traj = bh.replicator(M, p0, t)
    pc.line(t, traj, HAWK if p0 < PSTAR else DOVE, lw=1.6)
pc.hline(PSTAR, token="ink", dashed=True, lw=0.9)
pc.text(0.3, PSTAR + 0.03, "ESS  $p^* = V/C = 2/3$", ha="left", va="bottom")
bh.phase_line(ax, X1 + 4.9 + 0.6, Y0, Y0 + H, fixed=[0, PSTAR, 1], stable=[False, True, False],
              rhs=lambda q: q * (1 - q) * (V - C * q) / 2)
bio.label(ax, (X1 + 5.5, Y0 + H + 0.35), "$\\dot p$", size="small")
