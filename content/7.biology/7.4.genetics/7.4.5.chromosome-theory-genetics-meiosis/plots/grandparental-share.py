"""How much of a gamete's autosomal genome comes from one grandparent? Simulation of 20 000 human gametes
under independent assortment alone (no crossing over) and with crossing over (Haldane model: Poisson
crossovers on each transmitted chromatid, with the approximate sex-averaged map length of each autosome
scaled to male and female map lengths). Shares are weighted by physical length (hg38)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
Mb = np.array([248.96, 242.19, 198.30, 190.21, 181.54, 170.81, 159.35, 145.14, 138.39, 133.80, 135.09, 133.28,
               114.36, 107.04, 101.99, 90.34, 83.26, 80.37, 58.62, 64.44, 46.71, 50.82])
cM = np.array([286, 269, 223, 214, 204, 192, 187, 168, 167, 181, 158, 175, 126, 120, 141, 134, 128, 117, 107, 108,
               62, 73.0])
rng = np.random.default_rng(0)


def share(scale, reps, cross=True):
    out = np.empty(reps)
    for r in range(reps):
        tot = 0.0
        for L, M in zip(Mb, cM * scale / 100):
            if not cross:
                tot += L * rng.integers(0, 2)
                continue
            pts = np.sort(rng.random(rng.poisson(M)))
            seg = np.diff(np.r_[0, pts, 1])
            start = rng.integers(0, 2)
            tot += L * seg[(np.arange(len(seg)) + start) % 2 == 0].sum()
        out[r] = tot / Mb.sum()
    return out


fig, ax = plt.subplots(figsize=(7.2, 3.8))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.16, top=0.95)
bins = np.linspace(0, 1, 81)
for lab, scale, cross, tok in (("no crossing over", 1, False, "neutral"), ("male meiosis (about 27 crossovers)", 0.77, True, "dna"),
                               ("female meiosis (about 44 crossovers)", 1.23, True, "receptor")):
    x = share(scale, 20000, cross)
    ax.hist(x, bins=bins, density=True, histtype="step", lw=1.8, color=charts.line(tok),
            label=f"{lab}: SD = {x.std():.3f}")
ax.set_xlim(0.1, 0.9)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "fraction of the gamete's autosomal DNA from the grandfather", "density")
