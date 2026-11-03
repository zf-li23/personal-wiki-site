"""The pull of the Recent (Section 31.1.2), simulated. Taxa originate and go extinct at the same constant
rate (0.1 per taxon per Myr), so true diversity (grey) fluctuates around a constant level. Each taxon
leaves fossils as a Poisson process at rate 0.3 per Myr while it lives. Diversity per 5-Myr bin is
then counted by the range-through method, from the first to the last fossil occurrence (blue), and
again after every taxon alive today is extended from its last fossil to the present (orange), as
happens when living taxa are listed as present in every interval since their last fossil. The
second count rises toward the present although true diversity does not. A: the counts; B: the
fraction of true diversity recovered by each count."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)
T, lam, mu, q, N0 = 200.0, 0.1, 0.1, 0.3, 1000
# simulate taxa: list of (start, end); time runs 0 (past) .. T (present)
starts, ends = list(np.zeros(N0)), list(rng.exponential(1 / mu, N0))
i = 0
while i < len(starts):
    s, e = starts[i], min(ends[i], T)
    n = rng.poisson(lam * (e - s))
    for b in np.sort(rng.uniform(s, e, n)):
        starts.append(b)
        ends.append(b + rng.exponential(1 / mu))
    i += 1
    if len(starts) > 300000:
        break
starts, ends = np.array(starts), np.array(ends)
alive_end = np.minimum(ends, T)
bins = np.arange(0, T + 1e-9, 5.0)
mid = (bins[:-1] + bins[1:]) / 2
true = np.array([np.sum((starts < b1) & (alive_end > b0)) for b0, b1 in zip(bins[:-1], bins[1:])])
first, last, extant = [], [], []
for s, e, ee in zip(starts, alive_end, ends):
    k = rng.poisson(q * (e - s))
    if k == 0:
        continue
    occ = rng.uniform(s, e, k)
    first.append(occ.min()); last.append(occ.max()); extant.append(ee >= T)
first, last, extant = map(np.array, (first, last, extant))
rt = np.array([np.sum((first < b1) & (last >= b0)) for b0, b1 in zip(bins[:-1], bins[1:])])
last_rec = np.where(extant, T, last)
rr = np.array([np.sum((first < b1) & (last_rec >= b0)) for b0, b1 in zip(bins[:-1], bins[1:])])
keep = mid > 40  # discard the start-up interval
age = T - mid
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.28)
a.plot(age[keep], true[keep], color=P.muted(), lw=2, label="true diversity")
a.plot(age[keep], rt[keep], color=charts.line("dna"), lw=1.8, label="range-through, fossils only")
a.plot(age[keep], rr[keep], color=charts.line("rna"), lw=1.8, label="range-through, living taxa extended")
a.set_xlim(160, 0)
charts.style_axes(a, "time (Myr ago)", "taxa per 5-Myr bin")
charts.title(a, "A  Counted and true diversity")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
b.plot(age[keep], rt[keep] / true[keep], color=charts.line("dna"), lw=1.8)
b.plot(age[keep], rr[keep] / true[keep], color=charts.line("rna"), lw=1.8)
b.axhline(1, color=P.muted(), lw=0.8, ls=":")
b.set_xlim(160, 0)
b.set_ylim(0, 1.1)
charts.style_axes(b, "time (Myr ago)", "fraction of true diversity counted")
charts.title(b, "B  Completeness")
