"""Contest duration under the war of attrition and two assessment rules (simulated contests, arbitrary units).

A: war of attrition between matched opponents (Theorem 25.2.1 of 7.18.25): each persistence time is exponential
with mean V/k, so the contest (the shorter of the two) lasts longer than t with probability exp(-2kt/V); shown
for two resource values, on a log scale where the curves are straight lines.
B, C: 300 contests between opponents with fighting ability (RHP) drawn uniformly from 1 to 3.
Self-assessment (energetic war of attrition): each contestant quits when its accumulated cost reaches a
threshold proportional to its own RHP, with noise; the weaker one quits first. Mutual assessment (sequential
assessment): both sample noisy information on the difference in RHP each step and the one estimated weaker
quits when the running mean differs from zero by more than 2.5 standard errors.
B: duration against the loser's RHP: strongly positive under self-assessment, weaker under mutual assessment
(where it arises because a strong loser can only have met a slightly stronger opponent).
C: duration against the difference in RHP: strongly negative under mutual assessment, but also negative under
self-assessment, a by-product of large differences usually involving weak losers (Taylor and Elwood 2003).
Contests of the mutual-assessment model still unresolved after 300 steps are stopped there (top row).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)
fig, ax = bio.canvas(33.0, 10.0)

# ---- A ----------------------------------------------------------------------------------------------------
pa = Ch.axes_at(ax, (2.4, 1.7, 7.6, 7.2))
t = np.linspace(0, 10, 200)
for V, tok in ((2.0, "dna"), (6.0, "rna")):
    pa.plot(t, np.exp(-2 * t / V), color=Ch.line(tok), lw=1.6)
    sim = np.minimum(rng.exponential(V, 400), rng.exponential(V, 400))
    ts = np.sort(sim)
    surv = 1 - np.arange(1, len(ts) + 1) / len(ts)
    pa.plot(ts[:-1], surv[:-1], ".", ms=1.6, color=Ch.line(tok), alpha=0.6)
    pa.text(7.2 if V > 3 else 2.6, np.exp(-2 * (7.2 if V > 3 else 2.6) / V) * 1.4, f"V/k = {V:g}",
            fontsize=FS["tiny"], color=Ch.line(tok))
pa.set_yscale("log")
pa.set_ylim(0.005, 1.1)
pa.set_xlim(0, 10)
Ch.style_axes(pa, "time t", "proportion of contests lasting > t")
bio.panel(ax, "A", (0.3, 9.8))

# ---- simulated contests ---------------------------------------------------------------------------------------
n = 300
r1, r2 = rng.uniform(1, 3, n), rng.uniform(1, 3, n)
lo, hi = np.minimum(r1, r2), np.maximum(r1, r2)
self_dur = lo * 10 * np.exp(rng.normal(0, 0.15, n))
mut_dur = np.empty(n)
for i in range(n):
    d, s = hi[i] - lo[i], 1.0
    tot, k = 0.0, 0
    while True:
        k += 1
        tot += d + rng.normal(0, s)
        if abs(tot / k) > 2.5 * s / np.sqrt(k) or k >= 300:
            break
    mut_dur[i] = k

for j, (xv, xl) in enumerate(((lo, "RHP of the loser"), (hi - lo, "difference in RHP"))):
    x0 = 13.6 + 10.6 * j
    p = Ch.axes_at(ax, (x0, 1.7, 7.6, 7.2))
    for dur, tok, name in ((self_dur, "rna", "self-assessment"), (mut_dur, "dna", "mutual assessment")):
        y = dur / np.median(dur)
        p.plot(xv, y, "o", ms=2.4, color=Ch.line(tok), mfc="none", mew=0.6)
        rho = np.corrcoef(np.argsort(np.argsort(xv)), np.argsort(np.argsort(dur)))[0, 1]
        p.text(0.0, 1.13 - 0.07 * (tok == "dna"), f"{name}: rank r = {rho:+.2f}", transform=p.transAxes,
               fontsize=FS["tiny"], color=Ch.line(tok), va="top")
    p.set_yscale("log")
    Ch.style_axes(p, xl, "contest duration / median")
    bio.panel(ax, "BC"[j], (x0 - 2.1, 9.8))
