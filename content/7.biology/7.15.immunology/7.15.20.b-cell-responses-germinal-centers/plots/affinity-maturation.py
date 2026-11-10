# Stochastic model of affinity maturation in one germinal center.
# State: a population of GC B cells, each with a clone label and an affinity a = log10(K_A / M^-1).
# One cycle (~12 h) = light-zone selection, then dark-zone proliferation with somatic hypermutation.
#   Selection: a cell captures antigen in proportion to its occupancy K c / (1 + K c), where c is the
#   free antigen concentration on FDCs, which falls over time (consumption, masking by antibody).
#   Tfh help is limited: at most N_sel cells are selected per cycle, sampled with weight = captured antigen.
#   Proliferation: each selected cell divides twice; each daughter's V region (~300 bp) acquires
#   Poisson(0.3) mutations (~1e-3 per bp per division). Each mutation is lethal (loss of a functional BCR)
#   with probability 0.3; otherwise it changes a by a normal amount with a negative mean (most changes
#   are harmful), and gains shrink as a approaches the ceiling a_max.
# Control: the same mutation process with selection that ignores affinity.
# All parameters are illustrative orders of magnitude, not fitted values.
import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(0)

N_SEL = 500          # cells receiving Tfh help per cycle
CYCLES = 42          # 21 days at 2 cycles per day
A0, AMAX = 6.0, 10.0
N_CLONES = 40


def antigen(t_day):
    return 10 ** (-6.0 - 3.0 * t_day / 21.0)  # free antigen falls from 1 uM to 1 nM


def run(select_by_affinity):
    a = A0 + 0.25 * rng.standard_normal(N_SEL * 4)
    clone = rng.integers(0, N_CLONES, a.size)
    hist, mean_a, n_clones, simpson = [], [], [], []
    for k in range(CYCLES + 1):
        t = k / 2
        hist.append(np.histogram(a, bins=np.linspace(4, 11, 57))[0] / a.size)
        mean_a.append(a.mean())
        counts = np.bincount(clone, minlength=N_CLONES)
        n_clones.append((counts > 0).sum())
        f = counts / counts.sum()
        simpson.append(1 / np.sum(f ** 2))
        if k == CYCLES:
            break
        c = antigen(t)
        K = 10 ** a
        w = K * c / (1 + K * c) if select_by_affinity else np.ones_like(a)
        n = min(N_SEL, a.size)
        idx = rng.choice(a.size, size=n, replace=False, p=w / w.sum())
        a_s, c_s = np.repeat(a[idx], 4), np.repeat(clone[idx], 4)
        m = rng.poisson(0.3, a_s.size)
        alive = np.ones(a_s.size, bool)
        for j in range(m.max(initial=0)):
            hit = m > j
            lethal = hit & (rng.random(a_s.size) < 0.3)
            alive &= ~lethal
            d = rng.normal(-0.05, 0.25, a_s.size)
            d = np.where(d > 0, d * np.clip((AMAX - a_s) / (AMAX - A0), 0, 1), d)
            a_s = np.where(hit & ~lethal, a_s + d, a_s)
        a, clone = a_s[alive], c_s[alive]
    return np.array(hist), np.array(mean_a), np.array(n_clones), np.array(simpson)


H, ma, nc, sp = run(True)
_, ma0, nc0, sp0 = run(False)
days = np.arange(CYCLES + 1) / 2

fig, ax = bio.canvas(26, 9.6)

# ---- A: affinity distribution over time ---------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.4))
hx = charts.axes_at(ax, (1.7, 1.6, 7.4, 6.6))
hx.imshow(H.T, origin="lower", aspect="auto", extent=(0, 21, 4, 11), cmap="viridis", interpolation="nearest")
hx.plot(days, ma, color="white", lw=1.2, ls="--")
hx.set_xticks([0, 7, 14, 21])
charts.style_axes(hx, "Time / days", "Affinity, log₁₀(K_A / M⁻¹)")
charts.title(hx, "Distribution of BCR affinity (with selection)")

# ---- B: mean affinity -----------------------------------------------------------------------------------
bio.panel(ax, "B", (9.9, 9.4))
pb = quant.Plot(ax, (11.6, 1.6, 5.6, 6.6), (0, 21), (5, 10), xlabel="Time / days", ylabel="Mean log₁₀ K_A",
                xticks=[0, 7, 14, 21], yticks=[5, 6, 7, 8, 9, 10], grid=True)
pb.line(days, ma, "dna", lw=1.8, text="mutation + selection", at=0.35, dy=0.3, va="bottom")
pb.line(days, ma0, "negative", lw=1.5, dashed=True, text="mutation only", at=0.55, dy=-0.25, va="top")
pb.line(days, -np.log10([antigen(t) for t in days]), "muted", lw=1.0, dotted=True)
pb.text(20.5, 8.75, "−log₁₀ c (antigen)", ha="right", va="top", color=P.muted())

# ---- C: clonal diversity ----------------------------------------------------------------------------------
bio.panel(ax, "C", (18.3, 9.4))
pc = quant.Plot(ax, (20.0, 1.6, 5.6, 6.6), (0, 21), (0, 42), xlabel="Time / days", ylabel="Clones in the GC",
                xticks=[0, 7, 14, 21], yticks=[0, 10, 20, 30, 40], grid=True)
pc.line(days, nc, "dna", lw=1.8, text="clones present", at=0.25, dy=0.3, va="bottom", ha="left")
pc.line(days, sp, "rna", lw=1.5, text="effective number (1/Σf²)", at=0.45, dy=-0.3, va="top", ha="left")
pc.line(days, sp0, "negative", lw=1.0, dashed=True, text="no selection", at=0.8, dy=0.3, va="bottom")
