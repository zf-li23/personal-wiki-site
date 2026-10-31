# Folding against aggregation, and the kinetics of amyloid formation.
# A: kinetic competition after dilution of an unfolded protein (concentration c0) out of denaturant:
#    dU/dt = -k_f U - k_a U^2, with folding first order and aggregation second order and irreversible.
#    The native yield is Y = (k_f / (k_a c0)) ln(1 + k_a c0 / k_f); k_f = 1 /s. A holdase chaperone that
#    binds unfolded chains lowers the effective k_a and restores the yield.
# B, C: nucleated polymerization with secondary nucleation (moment equations of Knowles et al. 2009 and
#    Cohen et al. 2013), with rate constants of the order measured for the amyloid-beta 42 peptide:
#    dP/dt = k_n m^2 + k_2 m^2 M,  dM/dt = 2 k_+ m P,  m = m_tot - M  (P: fibril number, M: fibril mass),
#    k_+ = 3e6 /M/s, k_n = 1e-7 /M/s, k_2 = 1.3e4 /M^2/s.
#    B: fibril mass against time (logarithmic) at m_tot = 5 uM: sigmoidal with a lag phase; without secondary nucleation
#    the lag is far longer; preformed seeds (1 % of the mass) abolish the lag. C: half time against total
#    monomer concentration: slope -1.5 with secondary nucleation, -1 with primary nucleation alone.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))

kf = 1.0
c0 = np.logspace(-8, -4, 200)  # M
for ka, tok in ((1e5, "dna"), (1e6, "neutral"), (1e7, "rna")):
    x = ka * c0 / kf
    axs[0].semilogx(c0 * 1e6, np.log1p(x) / x, color=charts.line(tok), lw=1.8, label="k_a = 10" + "⁵⁶⁷"[int(np.log10(ka)) - 5] + " M⁻¹ s⁻¹")
charts.style_axes(axs[0], "protein concentration c₀ / µM", "native yield")
axs[0].legend(fontsize=7.5, frameon=False, loc="lower left")
axs[0].text(0.03, 0.9, "k_f = 1 s⁻¹", fontsize=8, color=P.muted())
axs[0].set_ylim(0, 1.03)
charts.title(axs[0], "A   Folding competes with aggregation")

kp, kn, k2 = 3e6, 1e-7, 1.3e4


def rhs(t, y, m0, sec):
    Pn, M = y
    m = m0 - M
    return [kn * m**2 + (k2 * m**2 * M if sec else 0.0), 2 * kp * m * Pn]


def run(m0, sec=True, seed=0.0, T=4e5):
    # seeds: a mass fraction of fibrils of 2000 monomers each
    y0 = [seed * m0 / 2000.0, seed * m0]
    s = solve_ivp(rhs, (0, T), y0, args=(m0, sec), rtol=1e-8, atol=1e-22, method="LSODA", dense_output=True)
    t = np.r_[0.0, np.geomspace(1.0, T, 6000)]
    return t, s.sol(t)[1] / m0


m0 = 5e-6
for lab, kw, tok in (("primary and secondary nucleation", dict(), "rna"),
                     ("primary nucleation only", dict(sec=False), "neutral"),
                     ("seeded (1 % fibrils)", dict(seed=0.01), "dna")):
    t, M = run(m0, T=1.5e6, **kw)
    axs[1].semilogx(t[1:] / 3600, M[1:], color=charts.line(tok), lw=1.8, label=lab)
axs[1].set_xlim(0.01, 400)
axs[1].set_ylim(-0.02, 1.05)
charts.style_axes(axs[1], "time / h", "fraction of monomer in fibrils")
axs[1].legend(fontsize=7.5, frameon=False, loc="center left", bbox_to_anchor=(0.0, 0.62))
charts.title(axs[1], "B   Sigmoidal growth, 5 µM")

ms = np.logspace(np.log10(1e-6), np.log10(2e-5), 9)
for sec, tok, lab in ((True, "rna", "with secondary nucleation"), (False, "neutral", "primary only")):
    th = []
    for m in ms:
        t, M = run(m, sec=sec, T=2e6)
        th.append(t[np.argmax(M > 0.5)])
    th = np.array(th)
    axs[2].loglog(ms * 1e6, th / 3600, "o-", ms=4, color=charts.line(tok), lw=1.2, label=lab)
    slope = np.polyfit(np.log(ms), np.log(th), 1)[0]
    axs[2].text(ms[3] * 1e6, th[3] / 3600 * (0.45 if sec else 1.5), f"slope {slope:.2f}", fontsize=8,
                color=charts.line(tok))
charts.style_axes(axs[2], "total monomer m_tot / µM", "half time / h")
axs[2].legend(fontsize=7.5, frameon=False, loc="upper right")
charts.title(axs[2], "C   Scaling of the half time")
fig.tight_layout()
