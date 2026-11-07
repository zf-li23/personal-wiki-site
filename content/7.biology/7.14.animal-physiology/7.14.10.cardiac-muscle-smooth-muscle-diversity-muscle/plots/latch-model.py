# The latch state of smooth muscle: the Hai-Murphy four-state cross-bridge model (1988), rate constants as
# published for swine carotid artery (per second): K2 = K5 = 0.5 (myosin light-chain phosphatase, MLCP),
# K3 = 0.4 (attachment of phosphorylated myosin), K4 = 0.1 (detachment of phosphorylated cross-bridges),
# K7 = 0.01 (detachment of dephosphorylated "latch" bridges); K1 = K6 = MLCK activity (Ca2+-calmodulin dependent).
#   M  <-> Mp   (K1, K2)       Mp <-> AMp  (K3, K4)       AMp <-> AM (K5, K6)       AM -> M (K7)
# Force is proportional to attached bridges AMp + AM; ATP is used by each phosphorylation (K1 M + K6 AM) and
# by each cycle of a phosphorylated bridge (K4 AMp); latch bridges detach slowly without cycling.
# (A) stimulation: MLCK activity 0.55 /s for 5 s, then 0.15 /s (Ca2+ falls but stays above rest): light-chain
#     phosphorylation peaks at about 0.5 and falls to about 0.23 while force keeps rising to about 0.9 (latch);
# (B) steady states over MLCK activity: force against phosphorylation is steep and saturating;
# (C) ATP use against force, with the latch (K7 = 0.01 /s) and in a variant in which dephosphorylated bridges
#     detach as fast as phosphorylated ones (K7 = 0.1 /s): the latch holds force at a fraction of the cost.
import matplotlib.pyplot as plt
import numpy as np

K2 = K5 = 0.5
K3, K4 = 0.4, 0.1


def deriv(s, K1, K7):
    M, Mp, AMp, AM = s
    K6 = K1
    return np.array([
        -K1 * M + K2 * Mp + K7 * AM,
        K1 * M - (K2 + K3) * Mp + K4 * AMp,
        K3 * Mp - (K4 + K5) * AMp + K6 * AM,
        K5 * AMp - (K6 + K7) * AM,
    ])


def steady(K1, K7):
    A = np.array([[-K1, K2, 0, K7],
                  [K1, -(K2 + K3), K4, 0],
                  [0, K3, -(K4 + K5), K1],
                  [1, 1, 1, 1.0]])
    return np.linalg.solve(A, np.array([0, 0, 0, 1.0]))


def atp(s, K1):
    M, Mp, AMp, AM = s
    return K1 * M + K1 * AM + K4 * AMp


dt = 0.01
t = np.arange(-2, 60, dt)
s = steady(0.0001, 0.01)
rec = []
for ti in t:
    K1 = 0.0 if ti < 0 else (0.55 if ti < 5 else 0.15)
    s = s + dt * deriv(s, K1, 0.01)
    rec.append(s.copy())
rec = np.array(rec)
fmax = steady(10.0, 0.01)
Fnorm = fmax[2] + fmax[3]
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))
a.plot(t, (rec[:, 1] + rec[:, 2]), color="#2f6fb5", lw=2.2, label="light-chain phosphorylation")
a.plot(t, (rec[:, 2] + rec[:, 3]) / Fnorm, color="#c0504d", lw=2.2, label="force (attached bridges)")
a.plot(t, rec[:, 3] / Fnorm, color="#c0504d", lw=1.2, ls=":", label="latch bridges (AM)")
a.axvspan(0, 5, color="0.6", alpha=0.18, lw=0)
a.text(2.5, 1.02, "high Ca²⁺", ha="center", fontsize=8.5, color="0.45")
a.set_xlabel("Time after stimulation / s")
a.set_ylabel("Fraction (force relative to maximum)")
a.set_ylim(0, 1.1)
a.legend(frameon=False, fontsize=8.5, loc="center right")
a.set_title("A   Phosphorylation falls, force stays", loc="left", fontsize=10)

K1s = np.logspace(-2.5, 1, 120)
for K7, col, name in ((0.01, "#c0504d", "with latch (K7 = 0.01 s⁻¹)"), (0.1, "#7a5fb0", "no latch (K7 = K4)")):
    st = np.array([steady(k, K7) for k in K1s])
    F = (st[:, 2] + st[:, 3]) / Fnorm
    b.plot(st[:, 1] + st[:, 2], F, color=col, lw=2.2, label=name)
    c.plot(F, [atp(x, k) for x, k in zip(st, K1s)], color=col, lw=2.2, label=name)
b.set_xlabel("Light-chain phosphorylation (steady state)")
b.set_ylabel("Force (relative)")
b.set_ylim(0, 1.15)
b.legend(frameon=False, fontsize=8.5, loc="lower right")
b.set_title("B   Steady states", loc="left", fontsize=10)
c.set_xlabel("Force (relative)")
c.set_ylabel("ATP use / (myosin⁻¹ s⁻¹)")
c.set_xlim(0, 1.05)
c.set_ylim(0, 0.5)
c.legend(frameon=False, fontsize=8.5, loc="upper left")
c.set_title("C   The cost of holding force", loc="left", fontsize=10)
for x in (a, b, c):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
