"""Genetic hitchhiking (Formulas 5.4.1 and 5.4.2). A: deterministic two-locus recursion for a haploid population
(selection, then recombination with fraction r). The beneficial allele A2 (advantage s = 0.05) starts at
frequency 0.001 on a chromosome that carries the neutral allele B2, which is absent elsewhere; B2 rises with it,
to fixation when r = 0 and less as r grows, because recombination moves B2 onto chromosomes without A2.
B: heterozygosity left at a neutral site at distance x from the selected site just after a sweep, relative to
before, from Eq. (5.8), 1 - (2N)^(-2r/s) with r = 1e-8 per bp per generation and 2N = 2e4, for three values of
s (solid lines). Dots: mean over 40 forward Wright-Fisher simulations of a sweep (2N = 2000 haplotypes,
s = 0.05, 21 neutral sites at linkage equilibrium, one crossover position per offspring drawn with probability
at most 0.004 Morgan from the selected site), relative to an unlinked site, with the prediction for 2N = 2000
(dashed). In A the curve for r = 0 coincides with that of A2."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)

s, T = 0.05, 400
cols = ["dna", "enzyme", "protein", "rna", "negative"]
for r, tok in zip((0.0, 0.002, 0.005, 0.01, 0.03), cols):
    x = np.array([0.0, 0.0, 0.0, 0.0])          # haplotypes A1B1, A1B2, A2B1, A2B2
    x[3] = 0.001
    x[0] = 0.999
    pa, pb = [x[2] + x[3]], [x[1] + x[3]]
    for t in range(T):
        w = np.array([1, 1, 1 + s, 1 + s])
        x = x * w / (x * w).sum()
        D = x[0] * x[3] - x[1] * x[2]
        x = x + r * D * np.array([-1, 1, 1, -1])
        pa.append(x[2] + x[3])
        pb.append(x[1] + x[3])
    a.plot(pb, color=charts.line(tok), lw=1.4, label=f"$B_2$, $r = {r}$")
a.plot(pa, color=P.ink(), lw=2.2, label="$A_2$ (selected)")
a.set_xlim(0, T)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "generation", "allele frequency")
charts.title(a, "A  A neutral allele rides along")

xkb = np.linspace(0, 400, 400)
r = xkb * 1e3 * 1e-8
for sv, tok in ((0.001, "dna"), (0.01, "enzyme"), (0.1, "rna")):
    b.plot(xkb, 1 - (2e4) ** (-2 * r / sv), color=charts.line(tok), lw=1.8, label=f"$s = {sv}$, $2N = 2\\times10^4$")

# forward simulation: 2N haplotypes, selected site at the centre of a 2*R map, neutral sites on one side
rng = np.random.default_rng(2)
n2, sv, L = 2000, 0.05, 21
dist = np.append(np.linspace(0, 0.004, L - 1), 0.5)  # recombination fraction to the selected site; last: unlinked
ratio = np.zeros(L)
done = 0
while done < 40:
    H = (rng.random((n2, L)) < 0.5).astype(np.int8)
    sel = np.zeros(n2, bool)
    sel[0] = True
    h0 = 2 * H.mean(0) * (1 - H.mean(0))
    ok = True
    for t in range(3000):
        fit = np.where(sel, 1 + sv, 1.0)
        par = rng.choice(n2, size=(n2, 2), p=fit / fit.sum())
        child_sel = sel[par[:, 0]]
        cut = rng.random(n2)                             # one crossover point; sites with dist > cut switch parent
        cross = cut < 0.004
        cut[~cross] = 1.0
        newH = H[par[:, 0]].copy()
        rows = np.where(cross)[0]
        if len(rows):
            mask = dist[None, :] > cut[rows, None]
            newH[rows] = np.where(mask, H[par[rows, 1]], H[par[rows, 0]])
        free = rng.random(n2) < 0.5                      # the unlinked site comes from either parent
        newH[free, -1] = H[par[free, 1], -1]
        H, sel = newH, child_sel
        f = sel.mean()
        if f == 0:
            ok = False
            break
        if f == 1:
            break
    if not ok:
        continue
    pj = H.mean(0)
    ratio += 2 * pj * (1 - pj) / h0
    done += 1
ratio /= done
ratio = ratio[:-1] / ratio[-1]                       # relative to the unlinked site (removes ordinary drift)
dist = dist[:-1]
b.scatter(dist / 1e-8 / 1e3, ratio, s=14, color=P.ink(), zorder=4, label="simulated, $s = 0.05$, $2N = 2000$")
xx = dist / 1e-8 / 1e3
b.plot(np.linspace(0, xx[-1], 200), 1 - 2000 ** (-2 * np.linspace(0, dist[-1], 200) / sv), color=P.ink(), lw=0.9,
       ls="--")
b.set_xlim(0, 400)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "distance from the selected site (kb)", "$H_{\\mathrm{after}}/H_{\\mathrm{before}}$")
charts.title(b, "B  The footprint of a sweep")
