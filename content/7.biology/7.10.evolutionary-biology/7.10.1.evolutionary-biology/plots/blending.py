"""Why blending inheritance was a problem for natural selection (Formula 1.3.1). A population of
N = 2000 individuals mates at random for 10 generations, without selection or mutation.
Blending: each offspring has the mean of its two parents' trait values. Particulate (Mendelian): the trait
is the sum of 20 additive loci (alleles 0 or 1, frequency 0.5), each parent transmits one allele per locus.
A: phenotypic variance over generations (dots: simulation; line: 2^-t under blending).
B: trait distributions in generations 0 and 5. Blending destroys variation; Mendelian inheritance keeps it."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)
N, L, T = 2000, 20, 10

# particulate: diploid genotypes (N, 2, L)
G = rng.integers(0, 2, size=(N, 2, L))
z_m = [G.sum(axis=(1, 2)).astype(float)]
var_m = [z_m[0].var()]
z_b = [z_m[0].copy()]
var_b = [z_b[0].var()]
for t in range(T):
    mom, dad = rng.integers(0, N, N), rng.integers(0, N, N)
    pick_m = rng.integers(0, 2, size=(N, L))
    pick_d = rng.integers(0, 2, size=(N, L))
    idx = np.arange(L)
    G = np.stack([G[mom[:, None], pick_m, idx[None, :]], G[dad[:, None], pick_d, idx[None, :]]], axis=1)
    z_m.append(G.sum(axis=(1, 2)).astype(float))
    var_m.append(z_m[-1].var())
    zb = z_b[-1]
    z_b.append(0.5 * (zb[rng.integers(0, N, N)] + zb[rng.integers(0, N, N)]))
    var_b.append(z_b[-1].var())

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw={"width_ratios": [1, 1.2]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.28)
g = np.arange(T + 1)
a.plot(g, var_m, "o", ms=4, color=charts.line("positive"), label="particulate (Mendelian)")
a.plot(g, var_b, "o", ms=4, color=charts.line("negative"), label="blending")
a.plot(g, var_b[0] * 0.5 ** g, color=charts.line("negative"), lw=1.2)
a.axhline(var_m[0], color=charts.line("positive"), lw=1.2)
a.set_ylim(0, 11.5)
charts.style_axes(a, "generation $t$", "variance of the trait")
charts.title(a, "A  Variance without selection")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())

bins = np.arange(4.5, 36, 1.0)
b.hist(z_m[0], bins=bins, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, density=True, label="generation 0 (both)")
b.hist(z_m[5], bins=bins, histtype="step", color=charts.line("positive"), lw=1.6, density=True, label="generation 5, particulate")
b.hist(z_b[5], bins=np.arange(4.5, 36, 0.25), histtype="step", color=charts.line("negative"), lw=1.6, density=True,
       label="generation 5, blending")
charts.style_axes(b, "trait value", "density")
charts.title(b, "B  Distributions")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
