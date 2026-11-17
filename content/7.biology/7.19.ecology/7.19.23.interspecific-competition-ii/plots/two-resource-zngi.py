"""Tilman's graphical theory of competition for two essential resources.

Model (simulated parameters): dR_k/dt = D (S_k - R_k) - sum_i c_ik mu_i(R) N_i, dN_i/dt = N_i (mu_i(R) - D),
with Liebig growth mu_i = min_k R_k / (K_ik + R_k) (mu_max = 1), D = 0.25, so that R*_ik = K_ik / 3.
Species A: R*_A1 = 1, R*_A2 = 3, consumption vector c_A = (0.3, 1); species B: R*_B1 = 3, R*_B2 = 1,
c_B = (1, 0.3). A: the zero net growth isocline (ZNGI) of species A alone is a right angle with corner
(R*_A1, R*_A2); from the supply point S the resources are drawn down along the consumption vector to
the equilibrium on the isocline (simulated path from S = (8, 6)). B: the isoclines of A and B cross at
(3, 3). Rays from the crossing along the consumption vectors (dashed) bound the region of coexistence.
Regions: 1 neither species; 2 only A can live; 3 both can live but A wins (R1 relatively scarce, A has
the lower R*_1); 4 stable coexistence (each species consumes more of the resource that limits it);
5 B wins; 6 only B. Lines: simulated resource trajectories from supply points (dots) in regions 2, 3, 4 and 5, with
both species introduced; squares: final resource levels, colored by the surviving species (black:
both). C: populations from S = (9, 7) (region 4).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 12.0)
D = 0.25
Ks = {"A": (3.0, 9.0), "B": (9.0, 3.0)}
cons = {"A": (0.3, 1.0), "B": (1.0, 0.3)}
col = {"A": Q.line_color("dna"), "B": Q.line_color("rna")}
rs = {k: (v[0] / 3, v[1] / 3) for k, v in Ks.items()}


def make(S, which=("A", "B")):
    def f(t, y):
        R = y[:2]
        out = [D * (S[0] - R[0]), D * (S[1] - R[1])]
        dn = []
        for j, sp in enumerate(which):
            n = y[2 + j]
            m = min(R[0] / (Ks[sp][0] + R[0]), R[1] / (Ks[sp][1] + R[1]))
            out[0] -= cons[sp][0] * m * n
            out[1] -= cons[sp][1] * m * n
            dn.append(n * (m - D))
        return out + dn
    return f


def zngi(p, sp, lim=10):
    x, y = rs[sp]
    p.plot([x, x, lim], [lim, y, y], color=col[sp], lw=1.9, label=f"species {sp} ZNGI")


pa = C.axes_at(ax, (2.2, 1.8, 8.6, 8.6))
zngi(pa, "A")
S = (8.0, 6.0)
s = solve_ivp(make(S, ("A",)), (0, 300), [*S, 0.05], rtol=1e-8, max_step=0.5)
pa.plot(s.y[0], s.y[1], color=P.ink(), lw=1.0)
pa.plot(*S, "o", color=P.ink(), ms=5)
pa.text(S[0] + 0.2, S[1] + 0.2, "supply point S", fontsize=FS["tiny"], color=P.ink())
pa.plot(s.y[0, -1], s.y[1, -1], "s", color=col["A"], ms=5)
pa.annotate("", xy=(s.y[0, -1] - 0.9, s.y[1, -1] - 3.0), xytext=(s.y[0, -1], s.y[1, -1]),
            arrowprops=dict(arrowstyle="-|>", color=col["A"], lw=1.2))
pa.text(s.y[0, -1] - 1.2, s.y[1, -1] - 2.2, "consumption\nvector", fontsize=FS["tiny"], color=col["A"], ha="right")
pa.text(0.3, 1.2, "A declines", fontsize=FS["tiny"], color=P.muted())
pa.text(5.5, 8.8, "A increases", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 10)
pa.set_ylim(0, 10)
C.style_axes(pa, "resource 1, $R_1$", "resource 2, $R_2$")
bio.panel(ax, "A", (0.3, 11.6))
bio.label(ax, (2.2, 11.2), "One consumer, two essential resources", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.4, 1.8, 8.6, 8.6))
zngi(pb, "A")
zngi(pb, "B")
X = (3.0, 3.0)
for sp in "AB":
    v = np.array(cons[sp])
    end = np.array(X) + 9 * v / v.max()
    pb.plot([X[0], end[0]], [X[1], end[1]], color=col[sp], lw=0.9, ls=(0, (4, 2)))
for txt, xy in [("1", (0.4, 0.4)), ("2", (2.0, 6.5)), ("3", (4.2, 9.2)), ("4", (7.0, 6.8)), ("5", (9.2, 4.2)), ("6", (6.5, 2.0))]:
    pb.text(*xy, txt, fontsize=FS["small"], color=P.ink(), ha="center", va="center", weight="bold")
for Sp in [(9.0, 7.0), (4.5, 9.5), (9.5, 4.0), (2.0, 8.5)]:
    s = solve_ivp(make(Sp), (0, 1500), [*Sp, 0.05, 0.05], rtol=1e-8, max_step=1.0)
    pb.plot(s.y[0], s.y[1], color=P.ink(), lw=0.8)
    pb.plot(*Sp, "o", color=P.ink(), ms=4)
    win = "A" if s.y[2, -1] > 1e-3 and s.y[3, -1] < 1e-3 else ("B" if s.y[3, -1] > 1e-3 and s.y[2, -1] < 1e-3 else None)
    pb.plot(s.y[0, -1], s.y[1, -1], "s", ms=5, color=col[win] if win else P.ink(), zorder=5)
pb.set_xlim(0, 10)
pb.set_ylim(0, 10)
C.style_axes(pb, "resource 1, $R_1$", "resource 2, $R_2$")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (11.6, 11.6))
bio.label(ax, (13.4, 11.2), "Two consumers: six regions", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (24.6, 1.8, 8.0, 8.6))
Sp = (9.0, 7.0)
t = np.linspace(0, 400, 800)
s = solve_ivp(make(Sp), (0, 400), [*Sp, 0.05, 0.05], t_eval=t, rtol=1e-8, max_step=1.0)
pc.plot(t, s.y[2], color=col["A"], lw=1.8, label="species A")
pc.plot(t, s.y[3], color=col["B"], lw=1.8, label="species B")
pc.set_xlim(0, 400)
pc.set_ylim(0, None)
C.style_axes(pc, "time (days)", "density")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "C", (23.2, 11.6))
bio.label(ax, (24.6, 11.2), "Coexistence, S = (9, 7)", size="small", bold=True, ha="left")
