"""Surface tension and the stability of alveoli (Young-Laplace pressure P = 2 gamma / r of the
liquid lining). A: pressure needed to hold an alveolus open against its lining, against its radius,
for a constant tension of 50 mN/m (a lining like plasma, without surfactant) and for a lining with
pulmonary surfactant whose tension falls on compression, modeled as gamma = gamma_max (r/r_max)^4
with gamma_max = 25 mN/m at r_max = 120 um (about 1.6 mN/m at r = 60 um). With constant tension the
pressure rises as the alveolus shrinks, so a small alveolus empties into a larger one; with
surfactant it falls. B: two alveoli connected through a common airway, starting at radii of 95 and
105 um, exchange air at a rate proportional to their pressure difference (total volume conserved):
without surfactant the smaller collapses (atelectasis), with surfactant both return to the same
size."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.17, top=0.87)
gmax, rmax = 25e-3, 120e-6


def gamma(r, surf):
    return gmax * (r / rmax) ** 4 if surf else 50e-3 * np.ones_like(r)


ax = axs[0]
r = np.linspace(20e-6, 130e-6, 300)
for surf, tok, lab in ((False, "negative", "no surfactant, 50 mN/m"), (True, "positive", "with surfactant")):
    ax.plot(r * 1e6, 2 * gamma(r, surf) / r / 1e3, color=charts.line(tok), lw=1.8, label=lab)
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"alveolar radius / $\mu$m", "Laplace pressure / kPa")
charts.title(ax, r"A  $P = 2\gamma/r$")

ax = axs[1]
for surf, tok in ((False, "negative"), (True, "positive")):
    rr = np.array([95e-6, 105e-6])
    Vt = np.sum(rr**3)
    out = [rr.copy()]
    dt, k = 1e-3, 1.5e-14  # arbitrary conductance (m^3 per s per Pa)
    for _ in range(5000):
        p = 2 * gamma(rr, surf) / rr
        flow = -k * (p - p.mean())  # volume flow into each alveolus
        V = 4 / 3 * np.pi * rr**3 + flow * dt
        V = np.clip(V, 4 / 3 * np.pi * (5e-6) ** 3, None)
        rr = (3 * V / (4 * np.pi)) ** (1 / 3)
        rr = rr * (Vt / np.sum(rr**3)) ** (1 / 3)
        out.append(rr.copy())
    out = np.array(out) * 1e6
    t = np.arange(len(out)) * dt
    for j, ls in ((0, "-"), (1, "--")):
        ax.plot(t, out[:, j], color=charts.line(tok), lw=1.6, ls=ls)
ax.set_ylim(0, 135)
ax.text(1.5, 25, "without surfactant: one collapses", fontsize=bio.core.FONT["tiny"], color=charts.line("negative"))
ax.text(2.0, 108, "with surfactant: equal", fontsize=bio.core.FONT["tiny"], color=charts.line("positive"))
charts.style_axes(ax, "time / arbitrary units", r"radius / $\mu$m")
charts.title(ax, "B  Two connected alveoli")
