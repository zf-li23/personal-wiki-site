# The gap-gene network and a gene-circuit model of it (Formula 15.2.1). A: inputs and interactions: Bicoid activates
# hunchback; Caudal activates knirps and giant; Tailless represses the trunk gap genes at the poles; strong mutual
# repression between non-adjacent gap genes (hb-kni, Kr-gt, thick bars) and weaker repression between neighbours.
# B: the steady state of the four-gene circuit on 100 nuclei along the axis (dimensionless rates, sigmoid response,
# weak diffusion), driven by an exponential Bicoid gradient (decay length 0.2 L), a posterior Caudal ramp and terminal
# Tailless: hb, Kr, kni and gt form ordered, abutting domains. C, D: removing Kr or kni from the circuit lets the
# neighbouring domains expand into the vacated region, as in the mutants.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N = 100
x = np.linspace(0, 1, N)
dx = x[1] - x[0]
bcd = np.exp(-x / 0.2)
cad = 1 / (1 + np.exp(-(x - 0.58) / 0.08))
tll = 1 / (1 + np.exp((x - 0.1) / 0.015)) + 1 / (1 + np.exp(-(x - 0.86) / 0.015))
# order: hb, Kr, kni, gt; W[a, b] = effect of b on a
W = np.array([[3, 0, -6, 0], [-6, 2, -3, -6], [-8, -2, 2, -5], [0, -6, -2, 2]], float)
mb = np.array([12, 0, 0, 0.])
mc = np.array([0, 0, 5, 7.])
mt = np.array([0, -8, -8, -8.])
h = np.array([-2.5, 1.0, -1.5, -5])
Dg = 0.0005


def phi(u):
    return 0.5 * (1 + u / np.sqrt(1 + u * u))


def run(mask):
    g = np.zeros((4, N))
    dt = 0.02
    for _ in range(2500):
        u = W @ g + np.outer(mb, bcd) + np.outer(mc, cad) + np.outer(mt, tll) + h[:, None]
        lap = np.zeros_like(g)
        lap[:, 1:-1] = g[:, 2:] - 2 * g[:, 1:-1] + g[:, :-2]
        lap[:, 0] = 2 * (g[:, 1] - g[:, 0])
        lap[:, -1] = 2 * (g[:, -2] - g[:, -1])
        g += dt * (mask[:, None] * phi(u) - g + Dg * lap / dx ** 2)
    return g


names = ["hb", "Kr", "kni", "gt"]
toks = ["channel", "positive", "highlight", "drug"]
fig, ax = bio.canvas(24.0, 13.0)

# A: network
bio.panel(ax, "A", (0.2, 12.8))
pos = {"Bcd": (2.0, 11.4), "Cad": (8.6, 11.4), "Tll": (5.3, 1.3), "hb": (2.0, 8.0), "Kr": (4.2, 5.2), "kni": (6.4, 8.0),
       "gt": (8.6, 5.2)}
cols = {"Bcd": "receptor", "Cad": "positive", "Tll": "neutral", "hb": "channel", "Kr": "positive", "kni": "highlight",
        "gt": "drug"}
for k, p in pos.items():
    bio.box(ax, p, 1.7, 0.8, token=cols[k] if k not in ("Cad",) else "cl", text=k, size="small", italic=k in names)
A = lambda a, b, kind="activation", bend=0.0, lw=1.3: bio.arrow(ax, a, b, kind=kind, bend=bend, lw=lw, shrink=0.0)
A((2.0, 11.0), (2.0, 8.45))
A((8.4, 11.0), (6.7, 8.45))
A((8.6, 11.0), (8.6, 5.65))
A((2.9, 8.15), (5.5, 8.15), "inhibition", lw=2.6)
A((5.5, 7.85), (2.9, 7.85), "inhibition", lw=2.6)
A((5.1, 5.35), (7.7, 5.35), "inhibition", lw=2.6)
A((7.7, 5.05), (5.1, 5.05), "inhibition", lw=2.6)
A((2.4, 7.55), (3.6, 5.65), "inhibition")
A((6.0, 7.55), (4.8, 5.65), "inhibition", lw=1.0)
A((8.2, 5.65), (7.0, 7.55), "inhibition", lw=1.0)
for tgt in ("Kr", "kni", "gt"):
    bx, by = pos[tgt]
    A((5.3, 1.75), (bx, by - 0.45), "inhibition", lw=1.0, bend=0.05)
bio.label(ax, (5.3, 12.4), "maternal inputs", size="tiny", color=P.muted())
bio.label(ax, (5.3, 0.4), "terminal input", size="tiny", color=P.muted())

panels = [("B", "wild type", np.ones(4)), ("C", "Kr mutant", np.array([1, 0, 1, 1.])), ("D", "kni mutant", np.array([1, 1, 0, 1.]))]
for k, (letter, title, mask) in enumerate(panels):
    y = 9.0 - k * 4.0
    g = run(mask)
    pa = C.axes_at(ax, (12.6, y, 10.6, 3.0))
    pa.plot(x, bcd, color=P.muted(), lw=1.0, ls=(0, (3, 2)))
    for gg, n, t in zip(g, names, toks):
        if mask[names.index(n)]:
            pa.plot(x, gg, color=C.line(t), lw=1.8)
            on = x[gg > 0.5]
            if len(on):
                pa.text(on.mean(), 1.08, n, color=C.line(t), fontsize=bio.core.FONT["tiny"], ha="center", style="italic")
    pa.set_xlim(0, 1)
    pa.set_ylim(0, 1.25)
    pa.set_yticks([0, 1])
    C.style_axes(pa, "x / L" if k == 2 else None, "level")
    if k < 2:
        pa.set_xticklabels([])
    bio.panel(ax, letter, (11.2, y + 3.6))
    bio.label(ax, (11.9, y + 3.3), title, size="small", bold=True, ha="left", italic=k > 0)
bio.label(ax, (18.0, 12.75), "dashed: Bicoid", size="tiny", color=P.muted())
