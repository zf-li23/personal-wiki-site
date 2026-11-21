"""Group decisions: quorum responses and leadership by an informed minority.

A: a quorum response. The probability that an individual switches behavior (for example, from tandem running to
carrying nestmates to a new nest site) as a function of the number x of nestmates already at the site,
x^h / (x^h + T^h), with threshold T = 20 and steepness h. A steep response (large h) behaves like a vote with a
quorum. B: leadership without signals (after Couzin et al. 2005). Agents in a simple self-propelled-particle model
avoid neighbors within distance 1, align with neighbors within 4 and are attracted to those within 15; a
fraction of them (rounded to whole individuals) also has a preferred direction g, weighted by 0.4 against the
social tendency. Accuracy is the mean cosine between the displacement of the group's centroid over the last 100
of 300 steps and g (1: the group travels exactly in the direction g; 0: random), from 24 runs per point; a
larger group reaches high accuracy with a smaller proportion of informed individuals.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(7)
fig, ax = bio.canvas(24.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.7, 7.6, 7.2))
x = np.linspace(0, 60, 300)
for h, tok in ((1, "dna"), (3, "protein"), (8, "rna")):
    pa.plot(x, x ** h / (x ** h + 20.0 ** h), color=Ch.line(tok), lw=1.6)
    xt = {1: 45, 3: 37, 8: 27}[h]
    pa.text(xt + 1, xt ** h / (xt ** h + 20.0 ** h) - 0.02, f"h = {h}", fontsize=FS["tiny"], color=Ch.line(tok),
            ha="left", va="top")
pa.axvline(20, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(21, 0.05, "threshold T", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 60)
pa.set_ylim(0, 1.05)
Ch.style_axes(pa, "number already at the site x", "probability of switching")
bio.panel(ax, "A", (0.3, 9.8))


def run(n, frac, steps=300, omega=0.4):
    pos = rng.uniform(0, 0.6 * np.sqrt(n), (n, 2))
    th = rng.uniform(0, 2 * np.pi, n)
    v = np.c_[np.cos(th), np.sin(th)]
    informed = np.zeros(n, bool)
    informed[: int(round(frac * n))] = True
    g = np.array([1.0, 0.0])
    for s in range(steps):
        if s == steps - 100:
            c0 = pos.mean(0)
        d = pos[None, :, :] - pos[:, None, :]
        r = np.hypot(d[..., 0], d[..., 1])
        np.fill_diagonal(r, np.inf)
        u = d / r[..., None]
        rep = r < 1
        des = np.where(rep.any(1)[:, None], -(u * rep[..., None]).sum(1),
                       v + (v[None] * (r < 4)[..., None]).sum(1) + (u * ((r >= 4) & (r < 15))[..., None]).sum(1))
        des = des / np.maximum(np.hypot(des[:, 0], des[:, 1]), 1e-9)[:, None]
        des = np.where(informed[:, None], des + omega * g, des)
        ang = np.arctan2(des[:, 1], des[:, 0]) + rng.normal(0, 0.15, n)
        v = np.c_[np.cos(ang), np.sin(ang)]
        pos = pos + 0.3 * v
    m = pos.mean(0) - c0
    return m[0] / max(np.hypot(*m), 1e-9)


pb = Ch.axes_at(ax, (14.4, 1.7, 8.4, 7.2))
fracs = [0.0, 0.02, 0.05, 0.1, 0.2, 0.4]
for n, tok in ((10, "dna"), (50, "rna")):
    acc = [np.mean([run(n, f) for _ in range(24)]) for f in fracs]
    pb.plot(fracs, acc, "o-", ms=3.5, lw=1.5, color=Ch.line(tok))
    pb.text(*((0.115, 0.45) if n == 10 else (0.06, 0.86)), f"group of {n}", fontsize=FS["tiny"],
            color=Ch.line(tok), ha="left", va="center")
pb.set_xlim(-0.01, 0.42)
pb.set_ylim(-0.5, 1.05)
Ch.style_axes(pb, "proportion of informed individuals", "accuracy (mean cosine to g)")
bio.panel(ax, "B", (12.3, 9.8))
