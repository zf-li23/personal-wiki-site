# Kinetics of mRNA synthesis and first-order decay, dm/dt = k_syn - k_deg m.
# A: approach to a new steady state after transcription is switched on (solid) and decay after it is switched
# off (dashed), for half-lives of 3 min (typical bacterial mRNA), 30 min (short-lived eukaryotic mRNA, e.g. of
# a transcription factor) and 8 h (median mammalian mRNA); the time to reach half of the change equals the
# half-life, whatever the synthesis rate.
# B: a change in stability alone (as for transferrin-receptor mRNA, 20-fold): the half-life drops from 4 h to
# 12 min at t = 0 (iron added) and returns to 4 h at t = 4 h (iron removed). The fall is fast and the recovery
# slow, because each response is set by the new degradation rate.
# C: metabolic labeling (e.g. 4-thiouridine): the labeled fraction of an mRNA grows as 1 - exp(-(k_deg + mu) t),
# independent of k_syn, so half-lives can be read from the labeling curve; mu = dilution by growth (doubling
# time 24 h).
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(26.0, 8.8)
LN2 = np.log(2)

# --- A ---
bio.panel(ax, "A", (0.1, 8.65))
t = np.logspace(-1, np.log10(48 * 60), 500)  # min
pa = Q.Plot(ax, (1.6, 1.6, 6.6, 5.4), xlim=(0.1, 48 * 60), ylim=(0, 1.02), xlog=True, xlabel="time after switch",
            ylabel="m / m* (on)  or  m / m₀ (off)",
            xticks=[(1, "1 min"), (10, "10 min"), (60, "1 h"), (600, "10 h")], yticks=[0, 0.5, 1])
for th, tok, name, at in ((3, "bacterium", "t½ = 3 min", 0.2), (30, "rna", "t½ = 30 min", 0.45), (480, "dna", "t½ = 8 h", 0.78)):
    k = LN2 / th
    pa.line(t, 1 - np.exp(-k * t), tok)
    pa.legend([(name, tok, "-")], at=(1.4 + 2.3 * [3, 30, 480].index(th), 7.75))
    pa.line(t, np.exp(-k * t), tok, dashed=True)
pa.hline(0.5, text=None)
bio.label(ax, (4.9, 7.3), "solid: switched on · dashed: switched off", size="tiny", color=P.muted())

# --- B ---
bio.panel(ax, "B", (9.3, 8.65))
k_slow, k_fast = LN2 / 240, LN2 / 12  # per min
ksyn = k_slow * 1.0
tt = np.linspace(-60, 600, 800)
m = np.empty_like(tt)
m0 = 1.0
for i, x in enumerate(tt):
    if x < 0:
        m[i] = 1.0
    elif x < 240:
        mstar = ksyn / k_fast
        m[i] = mstar + (1 - mstar) * np.exp(-k_fast * x)
    else:
        mstar = ksyn / k_fast
        m4 = mstar + (1 - mstar) * np.exp(-k_fast * 240)
        m[i] = 1.0 + (m4 - 1.0) * np.exp(-k_slow * (x - 240))
pb = Q.Plot(ax, (10.8, 1.6, 6.0, 6.2), xlim=(-60, 600), ylim=(0, 1.05), xlabel="t / h", ylabel="TfR-like mRNA (relative)",
            xticks=[(0, "0"), (120, "2"), (240, "4"), (360, "6"), (480, "8"), (600, "10")], yticks=[0, 0.5, 1])
pb.span(0, 240, "negative", text="high iron: t½ 12 min", strength=0.7)
pb.line(tt, m, "receptor")
pb.hline(1 / 20, text="1/20", side="right")

# --- C ---
bio.panel(ax, "C", (18.3, 8.65))
mu = LN2 / (24 * 60)
tc = np.linspace(0, 12 * 60, 300)
pc = Q.Plot(ax, (19.8, 1.6, 5.6, 6.2), xlim=(0, 12 * 60), ylim=(0, 1.02), xlabel="labeling time / h",
            ylabel="labeled fraction of the mRNA", xticks=[(0, "0"), (180, "3"), (360, "6"), (540, "9"), (720, "12")],
            yticks=[0, 0.5, 1])
for th, tok, name, at in ((30, "rna", "t½ = 30 min", 0.12), (240, "positive", "t½ = 4 h", 0.35), (960, "dna", "t½ = 16 h", 0.7)):
    k = LN2 / th + mu
    pc.line(tc, 1 - np.exp(-k * tc), tok, text=name, at=at, dx=0.1, dy=-0.35, ha="left")
bio.label(ax, (22.6, 8.3), r"$1-\mathrm{e}^{-(k_{\mathrm{deg}}+\mu)t}$", size="small")
