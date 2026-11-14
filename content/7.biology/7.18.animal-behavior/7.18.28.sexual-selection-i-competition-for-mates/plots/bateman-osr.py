"""Bateman gradients and the operational sex ratio.

A: a simulated breeding population of 60 males and 60 females. Each female mates with 1 to 3 males (more matings
are rarer) and chooses partners with a strong preference for some males (attractiveness drawn from a lognormal
distribution), so mating success is skewed among males. A female lays Poisson(20) eggs, slightly more if she
mates more than once; her eggs are shared equally among her partners. Reproductive success is regressed on
mating success after dividing both by their means (the standardized Bateman gradient), and the opportunity for
sexual selection I_s = Var(m) / mean(m)^2 is computed for each sex.
B: the operational sex ratio OSR = (N_m / N_f) (1 - t_m) / (1 - t_f) for an even adult sex ratio, where t is the
fraction of a breeding cycle an individual of each sex spends in "time out" (producing gametes, gestating, caring).
Females spend t_f = 0.8 of the cycle out of the mating pool; the OSR falls below 1 (more receptive females
than males, sex-role reversal) when males spend more time out than females.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)

nm = nf = 60
attract = rng.lognormal(0, 0.75, nm)
pm = attract / attract.sum()
mates_f = rng.choice([1, 2, 3], size=nf, p=[0.6, 0.3, 0.1])
male_ms = np.zeros(nm)
male_rs = np.zeros(nm)
female_rs = np.zeros(nf)
for f in range(nf):
    partners = rng.choice(nm, size=mates_f[f], replace=False, p=pm)
    eggs = rng.poisson(20 + 1.5 * (mates_f[f] - 1))
    female_rs[f] = eggs
    share = rng.multinomial(eggs, np.ones(mates_f[f]) / mates_f[f])
    for k, m in enumerate(partners):
        male_ms[m] += 1
        male_rs[m] += share[k]


def gradient(ms, rs):
    x, y = ms / ms.mean(), rs / rs.mean()
    b, a = np.polyfit(x, y, 1)
    return x, y, a, b


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 11.5, 7.6))
for ms, rs, tok, name, mk in ((male_ms, male_rs, "dna", "males", "o"), (female_rs * 0 + mates_f, female_rs, "rna",
                                                                         "females", "s")):
    x, y, a, b = gradient(ms, rs)
    jit = rng.uniform(-0.05, 0.05, len(x))
    pa.plot(x + jit, y, mk, color=Ch.line(tok), ms=3.2, alpha=0.75, mec="none")
    xx = np.linspace(0, x.max(), 50)
    pa.plot(xx, a + b * xx, color=Ch.line(tok), lw=1.8)
    i_s = ms.var() / ms.mean() ** 2
    ty = 0.93 if name == "males" else 0.85
    pa.text(0.03, ty, f"{name}: gradient {b:.2f}, $I_s$ = {i_s:.2f}", transform=pa.transAxes,
            fontsize=FS["small"], color=Ch.line(tok), ha="left")
pa.set_xlim(-0.2, None)
pa.set_ylim(-0.3, None)
Ch.style_axes(pa, "relative mating success (mates / mean)", "relative reproductive success")
Ch.title(pa, "Bateman gradients (simulated population)")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.4, 1.8, 10.6, 7.6))
tf = 0.8
tm = np.linspace(0.0, 0.95, 300)
osr = (1 - tm) / (1 - tf)
pb.plot(tm, osr, color=Ch.line("protein"), lw=1.9)
pb.axhline(1.0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.axvline(tf, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pb.fill_between(tm, 0, 6, where=tm > tf, color=P.mix(P.fill("rna"), P.surface(), 0.7), lw=0)
pb.text(0.25, 4.6, "males in excess:\nmales compete, females choose", fontsize=FS["tiny"], color=P.ink(), va="top")
pb.text(0.81, 1.5, "females in excess:\nsex-role reversal", fontsize=FS["tiny"], color=P.ink(), va="bottom",
        ha="left")
pb.text(tf + 0.01, 3.0, "$t_m = t_f$", fontsize=FS["tiny"], color=P.muted(), rotation=90)
pb.set_ylim(0, 5.5)
pb.set_xlim(0, 0.95)
Ch.style_axes(pb, "male time out $t_m$ (fraction of breeding cycle)", "operational sex ratio (males : females)")
Ch.title(pb, "OSR for an even adult sex ratio, $t_f$ = 0.8")
bio.panel(ax, "B", (16.3, 10.2))
