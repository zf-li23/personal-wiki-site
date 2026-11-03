"""Passive and driven trends (Section 32.5.1), after Futuyma and Kirkpatrick (2017), Fig. 20.21. A clade
starts with one species with trait value 1 (for example log body size above the minimum viable size).
Each species changes by random steps (variance 0.1 per Myr), speciates at rate 0.15 and goes extinct at
rate 0.1 per Myr. A: passive trend: steps are unbiased, but the trait cannot fall below 0 (a reflecting
boundary, such as a minimum body size). The variance expands, so the mean and the maximum rise while
many species remain near the ancestral value and the minimum stays near the boundary. B: driven trend:
steps are biased upward (mean +0.03 per Myr) and the whole distribution shifts. Dots: living species
every 2 Myr; lines: mean, minimum and maximum."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(8)
lam, mu, dt, T = 0.15, 0.1, 0.1, 60.0


def run(bias, wall):
    while True:
        z = np.array([1.0])
        rec = []
        for i in range(int(T / dt)):
            z = z + bias * dt + 0.1 * np.sqrt(dt) * rng.standard_normal(z.size) * np.sqrt(10)
            if wall:
                z = np.abs(z)
            keep = rng.random(z.size) > mu * dt
            born = rng.random(z.size) < lam * dt
            z = np.concatenate([z[keep], z[born & keep]])
            if z.size == 0:
                break
            if z.size > 1500:
                z = rng.choice(z, 1500, replace=False)
            if i % 20 == 0:
                rec.append(((i + 1) * dt, z.copy()))
        if z.size > 30:
            return rec


fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.6), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.08)
for ax, bias, wall, title, tok in ((axes[0], 0.0, True, "A  Passive trend (boundary at 0)", "dna"),
                                   (axes[1], 0.03, True, "B  Driven trend (upward bias)", "rna")):
    rec = run(bias, wall)
    for t, z in rec:
        sub = z if z.size < 150 else rng.choice(z, 150, replace=False)
        ax.plot(np.full(sub.size, t), sub, "o", ms=1.6, alpha=0.4, color=charts.line(tok))
    ts = [t for t, _ in rec]
    ax.plot(ts, [z.mean() for _, z in rec], color=P.ink(), lw=1.8, label="mean")
    ax.plot(ts, [z.min() for _, z in rec], color=P.muted(), lw=1.2, ls="--", label="minimum, maximum")
    ax.plot(ts, [z.max() for _, z in rec], color=P.muted(), lw=1.2, ls="--")
    ax.axhline(0, color=charts.line("negative"), lw=1)
    charts.style_axes(ax, "time (Myr)", "trait (e.g. log body size)" if ax is axes[0] else None)
    charts.title(ax, title)
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
