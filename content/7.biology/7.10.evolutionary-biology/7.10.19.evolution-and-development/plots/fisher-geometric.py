"""Fisher's geometric model. A: probability that a random mutation of size r is beneficial against
x = r sqrt(n) / (2d) for n = 3, 10, 50 (Monte Carlo) with the large-n approximation 1 - Phi(x) and the exact
n = 3 result. B: contribution to adaptation, E[2 s ; s > 0] against x (Gaussian fitness, n = 50)."""
import numpy as np
from scipy.stats import norm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8))
bio.panel(ax, "B", (12.2, 8.8))
pa = charts.axes_at(ax, (2.0, 1.6, 9.0, 6.6))
pb = charts.axes_at(ax, (14.2, 1.6, 9.0, 6.6))
d = 1.0
M = 20000


def unit(n, m):
    g = rng.standard_normal((m, n))
    return g / np.linalg.norm(g, axis=1, keepdims=True)


xs = np.linspace(0.05, 3.0, 14)
for n, tok in ((3, "rna"), (10, "dna"), (50, "positive")):
    ps = []
    for x in xs:
        r = 2 * d * x / np.sqrt(n)
        u = unit(n, M)
        z = np.zeros(n)
        z[0] = d                     # optimum at the origin, phenotype at distance d
        new = np.linalg.norm(z + r * u, axis=1)
        ps.append(np.mean(new < d))
    pa.plot(xs, ps, "o", ms=4.5, color=charts.line(tok), label=f"n = {n} (simulation)", zorder=5)
xx = np.linspace(0, 3, 200)
pa.plot(xx, 1 - norm.cdf(xx), color=P.ink(), lw=1.5, label=r"$1-\Phi(x)$ (large $n$)")
r3 = 2 * d * xx / np.sqrt(3)
pa.plot(xx, np.clip(0.5 * (1 - r3 / (2 * d)), 0, None), color=charts.line("rna"), lw=1.2, ls=(0, (3, 2)),
        label="exact, n = 3")
pa.set_xlim(0, 3)
pa.set_ylim(0, 0.55)
charts.style_axes(pa, r"scaled mutation size $x = r\sqrt{n}/(2d)$", "probability beneficial")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())

# B: Gaussian fitness w = exp(-|z|^2 / 2), s = w'/w - 1; contribution = E[2 s ; s > 0]
n = 50
d = 0.3
xs2 = np.linspace(0.05, 3.0, 30)
contrib = []
for x in xs2:
    r = 2 * d * x / np.sqrt(n)
    u = unit(n, M)
    z = np.zeros(n)
    z[0] = d
    new = np.linalg.norm(z + r * u, axis=1)
    s = np.exp(-(new ** 2 - d ** 2) / 2) - 1
    contrib.append(np.mean(np.where(s > 0, 2 * s, 0.0)))
contrib = np.array(contrib) / max(contrib)
pb.plot(xs2, contrib, color=charts.line("dna"), lw=1.8)
k = int(np.argmax(contrib))
pb.plot([xs2[k]], [contrib[k]], "o", color=charts.line("negative"), ms=6)
pb.text(xs2[k] + 0.1, contrib[k] + 0.02, f"maximum near x = {xs2[k]:.1f}", fontsize=FT["tiny"], color=P.ink())
pb.set_xlim(0, 3)
pb.set_ylim(0, 1.1)
charts.style_axes(pb, r"scaled mutation size $x$", "relative contribution to adaptation")
