"""The logic of East's experiment on corolla length in tobacco, simulated (seed 5): two inbred lines differing
at n = 5 unlinked additive loci (each increasing allele adds 4 mm; parental means 40 and 80 mm) with
environmental standard deviation 3 mm. A: parents and F1 are genetically uniform, so their spread is purely
environmental; the F2 is far more variable because the loci segregate (V_F2 - V_F1 = n a^2/2, the
segregation variance used by the Castle-Wright estimator). B: F3 families raised from F2 plants with short,
intermediate and long corollas: their means follow the parents (the variation is heritable), and each
family is less variable than the whole F2 because each F2 plant is homozygous at some of the loci."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(5)
n, eff, base, sd = 5, 4.0, 40.0, 3.0
x = np.linspace(20, 100, 500)


def kde(v):
    return stats.gaussian_kde(v, bw_method=0.25)(x)


def f2_genotypes(m):
    return rng.integers(0, 2, (m, n)) + rng.integers(0, 2, (m, n))  # number of increasing alleles per locus


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.15, top=0.88, wspace=0.2)
a = axs[0]
m = 4000
groups = [("$P_1$", np.full(m, base), "dna"), ("$P_2$", np.full(m, base + 2 * n * eff), "rna"),
          ("$F_1$", np.full(m, base + n * eff), "enzyme")]
G2 = f2_genotypes(m)
f2 = base + eff * G2.sum(1) + rng.normal(0, sd, m)
for lab, g, tok in groups:
    v = g + rng.normal(0, sd, m)
    a.plot(x, kde(v), color=charts.line(tok), lw=2, label=f"{lab}: SD {v.std():.1f} mm")
a.plot(x, kde(f2), color=charts.line("protein"), lw=2.2, label=f"$F_2$: SD {f2.std():.1f} mm")
a.set_yticks([])
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "corolla length / mm", "density")
charts.title(a, "A  Segregation inflates the $F_2$ variance")
b = axs[1]
tot = G2.sum(1)
resid = np.abs(f2 - base - eff * tot)
picks = [int(np.argmin(np.where(tot == t, resid, np.inf))) for t in (2, 5, 8)]
b.fill_between(x, kde(f2) / kde(f2).max() * 0.5, color=P.mix(P.surface(), P.muted(), 0.25), lw=0, label="$F_2$")
for idx, tok, name in zip(picks, ("dna", "enzyme", "rna"), ("short", "intermediate", "long")):
    g = G2[idx]
    k = 400
    # selfing an F2 plant: each locus with genotype 1 segregates 0/1/2 as 1:2:1; homozygous loci breed true
    kids = np.where(g == 1, rng.integers(0, 2, (k, n)) + rng.integers(0, 2, (k, n)), g)
    v = base + eff * kids.sum(1) + rng.normal(0, sd, k)
    dens = kde(v)
    b.plot(x, dens / dens.max(), color=charts.line(tok), lw=2,
           label=f"$F_3$ from {name} $F_2$ ({f2[idx]:.0f} mm): mean {v.mean():.0f}, SD {v.std():.1f}")
    b.axvline(f2[idx], color=charts.line(tok), lw=0.8, ls=":")
b.set_yticks([])
b.set_ylim(0, 1.45)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "corolla length / mm", "relative density")
charts.title(b, "B  $F_3$ families follow their $F_2$ parents")
