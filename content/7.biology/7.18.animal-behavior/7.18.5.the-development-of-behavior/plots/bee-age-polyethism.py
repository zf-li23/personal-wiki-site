"""Age polyethism in honey bees: an activator-inhibitor model (after Huang and Robinson 1992).

Each worker has a maturation variable x (think of juvenile hormone titre) that rises at an individual rate r_i
and is slowed by contact with foragers: dx/dt = r_i - c F, with F the fraction of workers that are foragers
(transmitted, e.g., by ethyl oleate). A worker starts foraging when x reaches 1. Nurses die at 0.01 per day,
foragers at 0.1 per day; 60 workers emerge per day. Illustrative parameters.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
dt, c, birth = 0.2, 0.32, 60.0


def rates(n):
    return (1 / 7.0) * np.exp(rng.normal(0, 0.25, n))


def step(st, t, rec, emerge=True):
    age, x, fr, r, born = st
    F = fr.mean() if len(fr) else 0.0
    x = x + np.where(fr, 0.0, np.maximum(r - c * F, 0.0)) * dt
    newf = (~fr) & (x >= 1)
    for a in age[newf]:
        rec.append((t, a))
    fr = fr | newf
    surv = rng.random(len(age)) > np.where(fr, 0.1, 0.01) * dt
    age, x, fr, r, born = age[surv] + dt, x[surv], fr[surv], r[surv], born[surv]
    if emerge:
        k = rng.poisson(birth * dt)
        age = np.r_[age, np.zeros(k)]
        x = np.r_[x, np.zeros(k)]
        fr = np.r_[fr, np.zeros(k, bool)]
        r = np.r_[r, rates(k)]
        born = np.r_[born, np.full(k, t)]
    return (age, x, fr, r, born), F


st = (np.zeros(0), np.zeros(0), np.zeros(0, bool), np.zeros(0), np.zeros(0))
rec = []
t = -250.0
while t < 0:
    st, _ = step(st, t, rec)
    t += dt
rec = []
T, FF = [], []
while t < 120:
    if abs(t - 50) < dt / 2:
        age, x, fr, r, born = st
        keep = ~fr
        st = (age[keep], x[keep], fr[keep], r[keep], born[keep])
    st, F = step(st, t, rec)
    T.append(t)
    FF.append(st[2].mean())
    t += dt
rec = np.array(rec)

fig, ax = bio.canvas(33.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 8.0, 7.2))
pa.plot(T, FF, color=C.line("rna"), lw=1.5)
pa.axvline(50, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(51, 0.05, "foragers\nremoved", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, 120)
pa.set_ylim(0, 0.6)
C.style_axes(pa, "time / days", "fraction of workers foraging")
bio.panel(ax, "A", (0.4, 9.7))

pb = C.axes_at(ax, (13.4, 1.6, 8.0, 7.2))
birth_t = rec[:, 0] - rec[:, 1]
bins = np.arange(0, 71, 5)
mid, mean = [], []
for a, b in zip(bins[:-1], bins[1:]):
    sel = (birth_t >= a) & (birth_t < b)
    if sel.sum() > 5:
        mid.append((a + b) / 2)
        mean.append(rec[sel, 1].mean())
pb.plot(mid, mean, "o-", color=C.line("dna"), lw=1.5, ms=3)
pb.axvline(50, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 70)
pb.set_ylim(0, 30)
C.style_axes(pb, "date of emergence / days", "mean age at onset of foraging / days")
bio.panel(ax, "B", (11.6, 9.7))

# C: single-cohort colony: 1500 bees of age 0, no emergence; compare with no interaction (c = 0)
pc = C.axes_at(ax, (24.4, 1.6, 8.0, 7.2))
for cc, tok, lab in [(0.32, "rna", "with inhibition"), (0.0, "neutral", "no inhibition")]:
    c = cc
    n = 1500
    st1 = (np.zeros(n), np.zeros(n), np.zeros(n, bool), rates(n), np.zeros(n))
    t1, ages, frac, rr = 0.0, [], [], []
    while t1 < 40:
        st1, _ = step(st1, t1, rr, emerge=False)
        t1 += dt
        ages.append(t1)
        frac.append(st1[2].mean())
    pc.plot(ages, frac, color=C.line(tok), lw=1.6)
    pc.text(ages[-1], frac[-1] + 0.03, lab, color=C.line(tok), fontsize=FS["tiny"], ha="right", va="bottom")
c = 0.32
pc.set_xlim(0, 40)
pc.set_ylim(0, 1.05)
C.style_axes(pc, "age of the cohort / days", "fraction foraging")
bio.panel(ax, "C", (22.6, 9.7))
