"""Choosing a nest site: recruitment, abandonment and stop signals (after Seeley and colleagues 2012 and Pais and
colleagues 2013).

Fractions of scouts committed to site A, psi_A, or site B, psi_B, and uncommitted, psi_U = 1 - psi_A - psi_B:
d psi_A/dt = gamma_A psi_U - alpha_A psi_A + rho_A psi_U psi_A - sigma psi_A psi_B, and symmetrically for B, with
discovery gamma = v, abandonment alpha = 1/v and recruitment by dancing rho = v for a site of quality v, and
stop signals of strength sigma delivered by scouts of one site to dancers for the other (cross-inhibition).
Small random fluctuations are added (Euler-Maruyama, noise 0.02).
A: two equal sites (v = 4) without stop signals: support splits and the swarm deadlocks. B: the same with stop
signals (sigma = 10): random fluctuations are amplified and the swarm commits to one site. C: unequal sites
(v_A = 4.4, v_B = 4) with stop signals: the better site wins.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT


def run(vA, vB, s, T=30.0, dt=0.01, noise=0.02, seed=2):
    rng = np.random.default_rng(seed)
    a = b = 0.0
    out = []
    for _ in range(int(T / dt)):
        u = 1 - a - b
        da = (vA * u - a / vA + vA * u * a - s * a * b) * dt + noise * np.sqrt(dt) * rng.normal()
        db = (vB * u - b / vB + vB * u * b - s * a * b) * dt + noise * np.sqrt(dt) * rng.normal()
        a, b = min(max(a + da, 0), 1), min(max(b + db, 0), 1)
        if a + b > 1:
            tot = a + b
            a, b = a / tot, b / tot
        out.append((a, b))
    return np.arange(len(out)) * dt, np.array(out)


fig, ax = bio.canvas(33.0, 10.0)
cases = [(4.0, 4.0, 0.0, "equal sites, no stop signals"), (4.0, 4.0, 10.0, "equal sites, stop signals"),
         (4.4, 4.0, 10.0, "site A better, stop signals")]
for i, (vA, vB, s, title) in enumerate(cases):
    pa = Ch.axes_at(ax, (2.2 + 10.8 * i, 1.8, 8.4, 7.0))
    t, x = run(vA, vB, s)
    pa.plot(t, x[:, 0], color=Ch.line("dna"), lw=1.6)
    pa.plot(t, x[:, 1], color=Ch.line("rna"), lw=1.6)
    pa.plot(t, 1 - x.sum(1), color=P.muted(), lw=1.0, ls=(0, (3, 2)))
    pa.set_ylim(0, 1.02)
    pa.set_xlim(0, t[-1])
    Ch.style_axes(pa, "time", "fraction of scouts" if i == 0 else None)
    Ch.title(pa, title)
    bio.panel(ax, "ABC"[i], (0.3 + 10.8 * i, 9.8))
bio.label(ax, (4.5, 0.25), "committed to A", size="tiny", color=Ch.line("dna"), bold=True)
bio.label(ax, (9.0, 0.25), "committed to B", size="tiny", color=Ch.line("rna"), bold=True)
bio.label(ax, (13.5, 0.25), "uncommitted", size="tiny", color=P.muted(), bold=True)
