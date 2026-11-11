"""The Ca2+ sensor of release and the geometry of Ca2+ nanodomains.

A: five-site sequential binding model of the release sensor (Schneggenburger and Neher 2000):
V0 <-> V1 <-> ... <-> V5 -> fused, forward rates (5-j) kon [Ca], backward rates (j+1) koff b^j,
fusion rate gamma from V5. kon = 9e7 /M/s, koff = 9500 /s, b = 0.25, gamma = 6000 /s.
For a step of intracellular [Ca2+] the peak release rate per vesicle is computed by integrating the
linear ODE; on log-log axes the slope is close to 5 at low [Ca2+] and the curve saturates above
~50 uM. The dashed line has slope 4.
B: steady-state [Ca2+] around one open Ca2+ channel (single-channel current 0.3 pA) in the
linearized buffer approximation (Neher 1986), c(r) = c0 + i / (4 pi z F D r) exp(-r / lambda),
lambda = sqrt(D / (kon_B [B])), D = 220 um^2/s, with no mobile buffer, 10 mM EGTA
(kon 1e7 /M/s) or 10 mM BAPTA (kon 4e8 /M/s).
C: release rate predicted by the sensor model at the local [Ca2+] of panel B, relative to the rate
without exogenous buffer, as a function of the channel-sensor distance: EGTA spares nanodomain
coupling (< 30 nm) but suppresses microdomain coupling (> 100 nm); BAPTA suppresses both.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio

P = bio.P
kon, koff, b, gam = 9e7, 9500.0, 0.25, 6000.0


def generator(ca):
    """Rate matrix (columns = from-state) for states V0..V5 and the fused state."""
    Q = np.zeros((7, 7))
    for j in range(5):
        f = (5 - j) * kon * ca
        r = (j + 1) * koff * b**j
        Q[j + 1, j] += f
        Q[j, j] -= f
        Q[j, j + 1] += r
        Q[j + 1, j + 1] -= r
    Q[6, 5] += gam
    Q[5, 5] -= gam
    return Q


t = np.linspace(0, 0.02, 801)  # s


def peak_rate(ca):
    Q = generator(ca)
    x0 = np.zeros(7)
    x0[0] = 1.0
    step = expm(Q * (t[1] - t[0]))
    x, best = x0, 0.0
    for _ in t:
        best = max(best, gam * x[5])
        x = step @ x
    return best


cas = np.logspace(-2, 2.3, 50)  # uM
rates = np.array([peak_rate(c * 1e-6) for c in cas])

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
ax.loglog(cas, rates, color=P.edge("ca"), lw=2.2, label="five-site model")
ref = rates[5] * (cas / cas[5]) ** 4
ax.loglog(cas, ref, color=P.muted(), lw=1.0, ls="--", label="slope 4")
ax.set_xlim(0.3, 200)
ax.set_ylim(1e-4, rates.max() * 3)
ax.set_xlabel("Intracellular [Ca$^{2+}$] step / $\\mu$M")
ax.set_ylabel("Peak release rate / (s$^{-1}$ per vesicle)")
ax.set_title("A  Cooperativity of the sensor", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

# --- nanodomain profiles
F, D, z, i = 96485.0, 220e-12, 2, 0.3e-12
r = np.linspace(5e-9, 300e-9, 300)
c0 = 0.05e-3  # mol/m^3 = 0.05 uM


def profile(kB):
    lam = np.inf if kB == 0 else np.sqrt(D / kB)
    return c0 + i / (4 * np.pi * z * F * D * r) * np.exp(-r / lam)  # mol/m^3 = mM


bufs = [("no exogenous buffer", 0.0, P.edge("ca")),
        ("10 mM EGTA", 1e7 * 1e-2, P.edge("protein")),
        ("10 mM BAPTA", 4e8 * 1e-2, P.edge("negative"))]
ax = axs[1]
prof = {}
for name, kB, c in bufs:
    cr = profile(kB) * 1e3  # uM
    prof[name] = cr
    ax.semilogy(r * 1e9, cr, color=c, lw=2.0, label=name)
ax.axvspan(10, 30, color=P.light("highlight"), zorder=0)
ax.text(20, 200, "nano-\ndomain", ha="center", va="top", fontsize=8, color=P.ink())
ax.axvspan(100, 300, color=P.light("neutral"), zorder=0)
ax.text(200, 30, "microdomain", ha="center", fontsize=8, color=P.ink())
ax.set_ylim(0.1, 300)
ax.set_xlabel("Distance from the channel / nm")
ax.set_ylabel("[Ca$^{2+}$] / $\\mu$M")
ax.set_title("B  Ca$^{2+}$ around one open channel", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="center right")

ax = axs[2]
lr = np.log(rates)
lc = np.log(cas)


def rate_at(cr):
    return np.exp(np.interp(np.log(np.clip(cr, cas[0], cas[-1])), lc, lr))


base = rate_at(prof["no exogenous buffer"])
for name, kB, c in bufs[1:]:
    rel = rate_at(prof[name]) / base
    rel[rel < 1e-6] = np.nan
    ax.semilogy(r * 1e9, rel, color=c, lw=2.0, label=name)
ax.axvspan(10, 30, color=P.light("highlight"), zorder=0)
ax.axvspan(100, 300, color=P.light("neutral"), zorder=0)
ax.set_ylim(1e-6, 2)
ax.set_xlabel("Channel-sensor distance / nm")
ax.set_ylabel("Release rate relative to control")
ax.set_title("C  What a buffer reveals", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left")
for a in axs:
    a.grid(True, alpha=0.3, which="both")
fig.tight_layout()
