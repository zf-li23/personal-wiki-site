"""A model of the second lineage decision of the mouse blastocyst: epiblast (Nanog high) versus primitive
endoderm (Gata6 high). Each inner cell carries a toggle switch, Nanog and Gata6 repressing each other; Nanog
cells secrete FGF4, which acts on their neighbours through FGFR and ERK, favouring Gata6 and repressing
Nanog. A: the network. B: the inner cell mass after the decision (positions of 26 cells; neighbours within
contact distance exchange FGF4): a salt-and-pepper mixture. C: Nanog and Gata6 in every cell over time;
the co-expressing state resolves into two classes. D: the fraction of primitive endoderm as a function of
FGF4 added to the medium, for wild-type ICMs and for ICMs that make no FGF4 (Fgf4 null): without FGF4 all
cells become epiblast, and enough exogenous FGF4 makes all of them primitive endoderm, as observed.
Five random seeds per point; equations in the text (Formula 5.6.1)."""
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 26
pts = []
while len(pts) < n:
    p = rng.uniform(-1, 1, 2)
    if np.hypot(*p) < 1 and all(np.hypot(*(p - q)) > 0.3 for q in pts):
        pts.append(p)
pts = np.array(pts)
Dm = np.hypot(*(pts[:, None] - pts[None]).transpose(2, 0, 1))
A = ((Dm < 0.48) & (Dm > 0)).astype(float)
A /= np.maximum(A.sum(1, keepdims=True), 1)


def run(Fext=0.0, fgf=1.0, T=60.0, dt=0.02, seed=0, keep=False):
    r = np.random.default_rng(seed)
    N = 1 + 0.1 * r.standard_normal(n)
    G = 1 + 0.1 * r.standard_normal(n)
    hist = []
    for k in range(int(T / dt)):
        E = fgf * (A @ N) + Fext
        dN = 2.0 / (1 + G**3) / (1 + (E / 1.2) ** 2) - N
        dG = 2.0 * (0.25 + E**2 / (1 + E**2)) / (1 + N**3) - G
        N = np.maximum(N + dt * dN + np.sqrt(dt) * 0.03 * r.standard_normal(n), 0)
        G = np.maximum(G + dt * dG + np.sqrt(dt) * 0.03 * r.standard_normal(n), 0)
        if keep and k % 10 == 0:
            hist.append((k * dt, N.copy(), G.copy()))
    return N, G, hist


fig, ax = bio.canvas(22, 14)
# A: network
bio.label(ax, (0.4, 13.6), "A  Network", size="small", bold=True, ha="left")
bio.box(ax, (2.2, 11.3), 2.0, 0.8, "positive", "Nanog", size="small")
bio.box(ax, (6.6, 11.3), 2.0, 0.8, "lipid", "Gata6", size="small")
bio.box(ax, (2.2, 8.6), 2.0, 0.8, "protein", "FGF4", size="small")
bio.box(ax, (6.6, 8.6), 2.0, 0.8, "enzyme", "FGFR-ERK", size="small")
bio.arrow(ax, (3.3, 11.5), (5.5, 11.5), kind="inhibition")
bio.arrow(ax, (5.5, 11.1), (3.3, 11.1), kind="inhibition")
bio.arrow(ax, (2.2, 10.85), (2.2, 9.05), kind="activation")
bio.arrow(ax, (3.25, 8.6), (5.55, 8.6), kind="activation")
bio.label(ax, (4.4, 8.25), "to neighbours", size="tiny", color=P.muted())
bio.arrow(ax, (6.6, 9.05), (6.6, 10.85), kind="activation")
bio.arrow(ax, (5.8, 9.05), (2.9, 10.85), kind="inhibition", dashed=True)
bio.label(ax, (2.2, 12.2), "epiblast", size="tiny", color=P.muted())
bio.label(ax, (6.6, 12.2), "primitive endoderm", size="tiny", color=P.muted())

# B: spatial outcome
N, G, hist = run(keep=True)
bio.label(ax, (11.4, 13.6), "B  Salt-and-pepper outcome", size="small", bold=True, ha="left")
cx, cy, sc = 15.6, 10.7, 2.3
for k, (x, y) in enumerate(pts):
    tk = "lipid" if G[k] > N[k] else "positive"
    ax.add_patch(Circle((cx + sc * x, cy + sc * y), 0.32, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=0.9, zorder=5))
for i in range(n):
    for j in range(i + 1, n):
        if A[i, j] > 0:
            ax.plot([cx + sc * pts[i, 0], cx + sc * pts[j, 0]], [cy + sc * pts[i, 1], cy + sc * pts[j, 1]], color=P.mix(P.muted(), P.surface(), 0.5),
                    lw=0.5, zorder=4)
bio.label(ax, (19.4, 12.6), f"epiblast {int((G <= N).sum())}", size="tiny", color=charts.line("positive"), ha="left")
bio.label(ax, (19.4, 12.1), f"primitive endoderm {int((G > N).sum())}", size="tiny", color=charts.line("lipid"), ha="left")

# C: time courses
c = charts.axes_at(ax, (1.6, 1.4, 8.2, 4.8))
t = np.array([h[0] for h in hist])
Ns = np.array([h[1] for h in hist])
Gs = np.array([h[2] for h in hist])
for k in range(n):
    c.plot(t, Ns[:, k], color=charts.line("positive"), lw=0.7, alpha=0.8)
    c.plot(t, Gs[:, k], color=charts.line("lipid"), lw=0.7, alpha=0.8)
c.set_xlim(0, 60)
charts.style_axes(c, "time (units of protein lifetime)", "expression")
charts.title(c, "C  Resolution of co-expression: Nanog (green), Gata6 (yellow)")

d = charts.axes_at(ax, (12.6, 1.4, 8.2, 4.8))
F = np.linspace(0, 1.6, 9)
for fgf, tk, lab in ((1.0, "dna", "wild type"), (0.0, "receptor", "Fgf4 null")):
    m = [np.mean([(lambda r: (r[1] > r[0]).mean())(run(f, fgf, T=40, seed=s)) for s in range(5)]) for f in F]
    d.plot(F, m, "-o", color=charts.line(tk), lw=1.6, ms=3.5, label=lab)
d.set_ylim(-0.03, 1.05)
charts.style_axes(d, "exogenous FGF4 (model units)", "fraction primitive endoderm")
charts.title(d, "D  FGF4 sets the proportion")
lg = d.legend(fontsize=7, frameon=False, loc="center right")
[tt.set_color(P.ink()) for tt in lg.get_texts()]
