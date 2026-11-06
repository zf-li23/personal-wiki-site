# A minimal three-gene repressilator for the Arabidopsis clock (in the spirit of Pokhilko et al. 2012):
# morning genes CCA1/LHY (L) repress the evening-complex genes (E: ELF4, LUX), the evening complex
# represses the day-phase PRR genes (P: PRR9/7/5), and the PRRs repress CCA1/LHY.
# Each gene: mRNA m and protein x,
#   dm/dt = v (1 + a_light L(t)) / (1 + x_rep^n) - d_m m,   dx/dt = d_p (m - x)  [protein of E also
#   degraded faster in light, 1 + a_E L(t)]; light induces L and P transcription (acute light input).
# Parameters were chosen so that the free-running period is about 24.6 h in constant light and longer
# (about 26.5 h) in constant darkness, and so that the mRNA phases under 12 h light : 12 h dark fall
# in the order morning (L) < day (P) < evening (E). Units are arbitrary; the model is illustrative.
# Panel B: free-running period as a function of the strength of constant light (Aschoff-type rule).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

DM, DP, VL, VP, VE, AL, AP, AE, N = 0.989, 0.228, 6.81, 7.76, 7.124, 0.203, 1.355, 0.408, 2.0


def rhs(t, y, light):
    mL, xL, mP, xP, mE, xE = y
    L = light(t)
    return [VL * (1 + AL * L) / (1 + xP**N) - DM * mL, DP * (mL - xL),
            VP * (1 + AP * L) / (1 + xE**N) - DM * mP, DP * (mP - xP),
            VE / (1 + xL**N) - DM * mE, DP * (mE - (1 + AE * L) * xE)]


def ld(t):
    return 1.0 if (t % 24) < 12 else 0.0


y0 = [1, 1, 0.5, 0.5, 0.2, 0.2]
ent = solve_ivp(rhs, (0, 24 * 12), y0, args=(ld,), max_step=0.05, dense_output=True)
yE = ent.sol(24 * 12)

# A: two LD days, then constant light
T_LD, T_LL = 48, 120


def lightA(t):
    return ld(t) if t < T_LD else 1.0


sa = solve_ivp(rhs, (0, T_LD + T_LL), yE, args=(lightA,), max_step=0.05, dense_output=True)
t = np.linspace(0, T_LD + T_LL, 3000)
Y = sa.sol(t)

# B: free-running period under constant light of different intensity (light input scaled 0..1)
def period(level):
    sol = solve_ivp(rhs, (0, 24 * 14), yE, args=(lambda s: level,), max_step=0.05, dense_output=True)
    pk = first_peak_after(sol, 24 * 6, 24 * 14)
    return np.diff(pk).mean()


def first_peak_after(sol, t0, t1):
    tt = np.linspace(t0, t1, 8000)
    x = sol.sol(tt)[0]
    pk, _ = find_peaks(x)
    return tt[pk]


levels = np.linspace(0, 1, 11)
periods = [period(v) for v in levels]

fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.0), gridspec_kw=dict(width_ratios=[1.7, 1]))
for i in range(0, T_LD, 24):
    a.axvspan(i + 12, i + 24, color="0.5", alpha=0.18, lw=0)
a.axvspan(T_LD, T_LD + T_LL, color="#e0a030", alpha=0.06, lw=0)
for idx, col, lab in ((0, "#e0a030", "CCA1/LHY mRNA (morning)"), (2, "#d9463b", "PRR mRNA (day)"),
                      (4, "#3b4fc0", "Evening complex mRNA")):
    y = Y[idx]
    a.plot(t, (y - y.min()) / (y.max() - y.min()), color=col, lw=2.0, label=lab)
pk, _ = find_peaks(Y[0])
for p in t[pk]:
    a.axvline(p, color="#e0a030", lw=0.6, ls=":")
a.text(T_LD + 2, 1.12, "constant light: free-running period about 24.6 h", fontsize=9)
a.text(2, 1.12, "12 h light : 12 h dark", fontsize=9)
a.set_xlim(0, T_LD + T_LL)
a.set_ylim(-0.05, 1.25)
a.set_xticks(range(0, T_LD + T_LL + 1, 24))
a.set_xlabel("Time / h")
a.set_ylabel("Relative mRNA level")
a.legend(frameon=False, fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
a.set_title("A   Entrainment and free run", loc="left", fontsize=10)

b.plot(levels, periods, "o-", color="black", lw=1.8, ms=5)
b.axhline(24, color="0.5", lw=0.8, ls=":")
b.set_xlabel("Constant light (relative strength of light input)")
b.set_ylabel("Free-running period / h")
b.set_title("B   Brighter light, shorter period", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
