"""Species selection without selection within species (Section 3.3.4). Lineages evolve a trait z
(for example log body size) by unbiased random change (Brownian motion, sigma^2 = 0.04 per Myr), and
speciate at rate 0.3 per Myr; extinction occurs at rate 0.3 per Myr in the control, and at rate
0.3 exp(-z) in the second case, so that large-bodied lineages persist longer. A: the mean trait of the
living species over 30 Myr (lines: 5 replicate clades each, starting from 30 species with z = 0). In the
control the mean wanders around 0; with trait-dependent extinction it rises steadily, although no
lineage has any tendency to become larger. B: the trait distribution of living species after 30 Myr,
pooled over the replicates."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
lam, mu0, sig, dt, T, CAP = 0.3, 0.3, 0.2, 0.05, 30.0, 3000


def run(dependent):
    z = np.zeros(30)
    times, means = [0.0], [0.0]
    for i in range(int(T / dt)):
        z = z + sig * np.sqrt(dt) * rng.standard_normal(z.size)
        mu = mu0 * np.exp(-z) if dependent else np.full(z.size, mu0)
        keep = rng.random(z.size) > mu * dt
        born = rng.random(z.size) < lam * dt
        z = np.concatenate([z[keep], z[born & keep]])
        if z.size == 0:
            return times, means, z
        if z.size > CAP:
            z = rng.choice(z, CAP, replace=False)
        times.append((i + 1) * dt)
        means.append(z.mean())
    return times, means, z


fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw={"width_ratios": [1.3, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.3)
finals = {False: [], True: []}
for dep, tok, name in ((False, "neutral", "extinction independent of z"), (True, "dna", "extinction decreases with z")):
    for r in range(5):
        tt, mm, zf = run(dep)
        a.plot(tt, mm, color=charts.line(tok), lw=1.1, label=name if r == 0 else None)
        finals[dep].append(zf)
a.axhline(0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
charts.style_axes(a, "time (Myr)", "mean trait of living species")
charts.title(a, "A  Mean over species")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
bins = np.linspace(-3.5, 3.5, 36)
for dep, tok in ((False, "neutral"), (True, "dna")):
    zz = np.concatenate(finals[dep]) if finals[dep] else np.array([])
    b.hist(zz, bins=bins, density=True, histtype="stepfilled", alpha=0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
charts.style_axes(b, "trait $z$ after 30 Myr", "density")
charts.title(b, "B  Living species at the end")
