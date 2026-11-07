# A minimal model of a sinoatrial-node pacemaker cell and its autonomic modulation (illustrative parameters).
#   C dV/dt = -(I_CaL + I_K + I_f + I_b + I_KACh),  C = 1 uF/cm2, currents in uA/cm2, V in mV, t in ms
#   I_CaL = g_Ca d_inf(V) f (V - E_Ca)   L-type Ca2+ current (upstroke), inactivation f (tau 40 ms)
#   I_K   = g_K x (V - E_K)              delayed rectifier (repolarization), activation x (tau 420 ms)
#   I_f   = g_f y (V - E_f)              "funny" current through HCN channels, E_f = -25 mV, activated by
#                                         hyperpolarization: y_inf = 1/(1 + exp((V - V_half)/8)), tau 600 ms
#   I_b   = g_b (V - E_b)                background inward current
#   I_KACh = g_KACh (V - E_K)            ACh-activated K+ current (GIRK)
# Sympathetic (NE, cAMP): V_half of I_f +8 mV and g_Ca x 1.5. Parasympathetic (ACh): V_half -7 mV and
# g_KACh = 0.004. The Ca2+ clock (Ca2+ release and Na+/Ca2+ exchange) is not modelled separately.
# A: membrane potential (intrinsic rate of the isolated node about 110 /min). B: firing rate when each
# mechanism acts alone or together, and with I_f blocked.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

BASE = dict(gCa=0.2, gK=0.15, gf=0.04, Vh=-65.0, gb=0.005, gKACh=0.0)
ECa, EK, Ef, Eb = 50.0, -85.0, -25.0, -20.0


def simulate(T=6000.0, **kw):
    p = dict(BASE)
    p.update(kw)

    def rhs(t, s):
        V, f, x, y = s
        d = 1 / (1 + np.exp(-(V + 28) / 5))
        I = (p["gCa"] * d * f * (V - ECa) + p["gK"] * x * (V - EK) + p["gf"] * y * (V - Ef)
             + p["gb"] * (V - Eb) + p["gKACh"] * (V - EK))
        return [-I, (1 / (1 + np.exp((V + 38) / 5)) - f) / 40.0, (1 / (1 + np.exp(-(V + 25) / 7)) - x) / 420.0,
                (1 / (1 + np.exp((V - p["Vh"]) / 8)) - y) / 600.0]

    sol = solve_ivp(rhs, (0, T), [-60.0, 1.0, 0.0, 0.2], max_step=0.5)
    return sol.t, sol.y[0]


def rate(t, V, t0=2500.0):
    up = t[1:][(V[:-1] < -10) & (V[1:] >= -10)]
    up = up[up > t0]
    return 60000.0 / np.mean(np.diff(up)) if len(up) > 1 else 0.0


NE = dict(Vh=-57.0, gCa=0.3)
ACH = dict(Vh=-72.0, gKACh=0.004)
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.6, 1]})
for kw, c, lab in ((NE, "#c0392b", "norepinephrine"), ({}, "0.2", "control"), (ACH, "#2f6fb5", "acetylcholine")):
    t, V = simulate(**kw)
    k = (t >= 3000) & (t <= 5500)
    axa.plot(t[k] - 3000, V[k], color=c, lw=1.8, label=f"{lab} ({rate(t, V):.0f} /min)")
axa.axhline(-40, color="0.6", lw=0.8, ls=":")
axa.text(2490, -38.5, "threshold", ha="right", fontsize=8, color="0.45")
axa.set_xlim(0, 2500)
axa.set_ylim(-80, 40)
axa.set_xlabel("Time / ms")
axa.set_ylabel("Membrane potential / mV")
axa.set_title("A  Diastolic depolarization sets the rate", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right", ncol=3)

cases = [("control", {}), ("NE: I$_f$ shift", dict(Vh=-57.0)), ("NE: I$_{CaL}$ x1.5", dict(gCa=0.3)), ("NE: both", NE),
         ("ACh: I$_f$ shift", dict(Vh=-72.0)), ("ACh: I$_{K,ACh}$", dict(gKACh=0.004)), ("ACh: both", ACH),
         ("I$_f$ blocked", dict(gf=0.0))]
rates = [rate(*simulate(**kw)) for _, kw in cases]
cols = ["0.3"] + ["#c0392b"] * 3 + ["#2f6fb5"] * 3 + ["#7a4fb3"]
y = np.arange(len(cases))[::-1]
axb.barh(y, rates, color=cols, height=0.65)
for yi, r in zip(y, rates):
    axb.text(r + 2, yi, f"{r:.0f}", va="center", fontsize=8.5)
axb.set_yticks(y)
axb.set_yticklabels([c for c, _ in cases], fontsize=9)
axb.set_xlabel("Firing rate / min$^{-1}$")
axb.set_xlim(0, 170)
axb.set_title("B  Dissecting the mechanisms", loc="left", fontsize=11, fontweight="bold")
for a in (axa, axb):
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
fig.tight_layout()
