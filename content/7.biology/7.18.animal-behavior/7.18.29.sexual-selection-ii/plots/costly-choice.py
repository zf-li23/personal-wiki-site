"""Fisher's runaway with and without a direct cost of choosiness (after Lande 1981; Pomiankowski et al. 1991).

Male trait mean z and female preference mean y (theta = 0 is the naturally selected optimum of the trait),
additive genetic variances G (trait) and H (preference) and genetic covariance B. Selection gradient on the
trait beta = (y - z)/nu^2 - z/omega^2; direct selection on the preference -k y (a cost of being choosy that
grows with the strength of preference). Panel B also shows k = 0.005. Per generation: dz = G beta / 2, dy = (B beta - H k y) / 2.
G = 0.4, H = 0.4, B = 0.2, nu^2 = 1, omega^2 = 2 (line of equilibria y = 1.5 z).
A: trajectories in the (z, y) plane without a cost (k = 0, populations stop on the line of equilibria) and with
a small cost (k = 0.05, populations slide down the line to the origin). B: the preference over generations
for the population started at (z, y) = (1, 2.5).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
G, H, B, nu2, om2 = 0.4, 0.4, 0.2, 1.0, 2.0


def run(z, y, k, n=600):
    out = [(z, y)]
    for _ in range(n):
        beta = (y - z) / nu2 - z / om2
        z, y = z + G * beta / 2, y + (B * beta - H * k * y) / 2
        out.append((z, y))
    return np.array(out)


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 10.5, 7.6))
zz = np.linspace(-0.2, 2.2, 10)
pa.plot(zz, (1 + nu2 / om2) * zz, color=P.muted(), lw=3, alpha=0.5)
pa.text(2.1, 3.05, "line of equilibria", fontsize=FS["tiny"], color=P.muted(), ha="right", rotation=36)
starts = [(1.0, 2.5), (0.2, 2.0), (1.8, 1.0), (0.5, 0.0)]
for z0, y0 in starts:
    a = run(z0, y0, 0.0, 200)
    b = run(z0, y0, 0.05, 1500)
    pa.plot(a[:, 0], a[:, 1], color=Ch.line("dna"), lw=1.5)
    pa.plot(b[:, 0], b[:, 1], color=Ch.line("rna"), lw=1.2, ls=(0, (4, 2)))
    pa.plot([z0], [y0], "o", color=P.ink(), ms=3.5)
pa.plot([0], [0], "s", color=Ch.line("rna"), ms=5)
pa.text(0.05, -0.25, "natural optimum, no preference", fontsize=FS["tiny"], color=Ch.line("rna"), va="top")
pa.text(0.03, 3.3, "no cost of choice", fontsize=FS["small"], color=Ch.line("dna"))
pa.text(0.03, 3.0, "small cost of choice", fontsize=FS["small"], color=Ch.line("rna"))
pa.set_xlim(-0.3, 2.3)
pa.set_ylim(-0.6, 3.5)
Ch.style_axes(pa, "mean male trait $\\bar z$", "mean female preference $\\bar y$")
Ch.title(pa, "Trait and preference evolve together")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.0, 1.8, 11.0, 7.6))
for k, tok, ls, name in ((0.0, "dna", "-", "k = 0"), (0.05, "rna", (0, (4, 2)), "k = 0.05"),
                         (0.005, "protein", (0, (1, 1.5)), "k = 0.005")):
    r = run(1.0, 2.5, k, 1500)
    pb.plot(np.arange(len(r)), r[:, 1], color=Ch.line(tok), lw=1.6, ls=ls, label=name)
pb.set_xlim(0, 1500)
pb.set_ylim(0, 3.4)
Ch.style_axes(pb, "generation", "mean female preference $\\bar y$")
Ch.title(pb, "A cost of choice erodes the preference")
leg = pb.legend(fontsize=FS["tiny"], frameon=False, loc="center right")
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "B", (15.9, 10.2))
