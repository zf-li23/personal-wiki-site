# Three-level negative-feedback model of the HPA axis (time in hours):
#   dR/dt = (c(t) + s(t)) / (1 + ((F + D) / KR)^2) - kR R                 CRH
#   dA/dt = a R / (1 + (F + D) / KA) - kA A                           ACTH
#   dF/dt = b A - kF F                                                cortisol (nmol/L)
# c(t): circadian drive from the suprachiasmatic nucleus (maximal before waking), s(t): a 1-h stress,
# D: dexamethasone (acts only on feedback, not measured as cortisol). Half-lives: ACTH 10 min, cortisol
# 70 min, dexamethasone 5 h. Parameters are illustrative.
# A: two days with a stress at 14:00 on day 2. B: 1 mg dexamethasone at 23:00; morning cortisol in a
# normal axis, a pituitary ACTH adenoma (Cushing disease: feedback 4x weaker, drive higher) and an
# autonomous adrenal tumour (cortisol secretion independent of ACTH).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

KR0, KA0, A_GAIN, B_GAIN = 600.0, 800.0, 25.0, 400.0
kR, kA, kF, kD = np.log(2) / 0.1, np.log(2) / (10 / 60), np.log(2) / (70 / 60), np.log(2) / 5.0


def drive(t):
    return 0.15 + np.exp(2.5 * (np.cos(2 * np.pi * (t - 6.0) / 24.0) - 1.0))


def model(t_end, stress=None, dex_at=None, KR=KR0, KA=KA0, gain=1.0, auto=None, y0=None, t0=0.0):
    a, b = A_GAIN, B_GAIN

    def rhs(t, y):
        R, A, F, D = y
        s = 3.0 if (stress is not None and stress <= t < stress + 1.0) else 0.0
        dR = gain * (drive(t + t0) + s) / (1.0 + ((F + D) / KR) ** 2) - kR * R
        dA = a * R / (1.0 + (F + D) / KA) - kA * A
        dF = (auto if auto is not None else b * A) - kF * F
        return [dR, dA, dF, -kD * D]

    t = np.linspace(0, t_end, int(t_end * 30) + 1)
    y0 = [0.05, 0.5, 100.0, 0.0] if y0 is None else list(y0)
    if dex_at is None:
        sol = solve_ivp(rhs, (0, t_end), y0, t_eval=t, max_step=0.02)
        return sol.t, sol.y
    t1 = t[t <= dex_at]
    s1 = solve_ivp(rhs, (0, dex_at), y0, t_eval=t1, max_step=0.02)
    y1 = s1.y[:, -1].copy()
    y1[3] += 6000.0  # dexamethasone, in cortisol-equivalent feedback units
    t2 = t[t > dex_at]
    s2 = solve_ivp(rhs, (dex_at, t_end), y1, t_eval=t2, max_step=0.02)
    return np.concatenate([s1.t, s2.t]), np.hstack([s1.y, s2.y])


fig, (axa, axb) = plt.subplots(1, 2, figsize=(12, 4.4), gridspec_kw=dict(width_ratios=[1.5, 1]))

# A: warm up 3 days, then show 2 days (clock time 0-48 h)
_, yw = model(72.0)
t, y = model(48.0, stress=24.0 + 14.0, y0=yw[:, -1])
axa.plot(t, y[2], color="#c0392b", lw=2, label="cortisol")
axa2 = axa.twinx()
axa2.plot(t, y[1], color="#2c6fbb", lw=1.4, ls="--", label="ACTH")
axa2.set_ylabel("ACTH / relative units", color="#2c6fbb")
axa.axvspan(38, 39, color="0.85", lw=0)
axa.text(37.6, axa.get_ylim()[1] * 0.97, "stress", ha="right", va="top", fontsize=8.5, color="0.35")
for d in (0, 24):
    axa.axvspan(d + 23 - 24 if d else -1, d + 7, color="0.93", lw=0, zorder=0)
axa.set_xlim(0, 48)
axa.set_xticks(range(0, 49, 6))
axa.set_xticklabels([f"{h % 24:02d}" for h in range(0, 49, 6)])
axa.set_xlabel("Clock time / h (shaded: night)")
axa.set_ylabel("Plasma cortisol / (nmol/L)", color="#c0392b")
axa.set_title("A  Circadian rhythm and a stress response", loc="left", fontsize=11, fontweight="bold")

# B: dexamethasone suppression; clock time 18:00 -> 12:00 next day
for kw, col, lab in (
    (dict(), "#2c6fbb", "normal"),
    (dict(KR=1000.0, KA=1600.0, gain=2.0), "#2e8b57", "pituitary adenoma"),
    (dict(auto=600.0 * kF), "#c0392b", "adrenal tumour"),
):
    _, yw = model(66.0, **kw)  # warm-up ending at 18:00
    for dex, ls in ((None, ":"), (5.0, "-")):
        tt, yy = model(18.0, dex_at=dex, y0=yw[:, -1], t0=18.0, **kw)
        axb.plot(tt + 18.0, yy[2], color=col, lw=2 if dex else 1.2, ls=ls, label=lab if dex else None)
axb.axvline(23, color="0.6", lw=0.8)
axb.text(23.3, 1000, "dexamethasone", fontsize=8.5, va="top", color="0.35")
axb.axhline(50, color="0.6", lw=0.8, ls="--")
axb.text(35.8, 58, "50 nmol/L", ha="right", fontsize=8, color="0.4")
axb.set_xticks(range(18, 37, 3))
axb.set_xticklabels([f"{h % 24:02d}" for h in range(18, 37, 3)])
axb.set_xlim(18, 36)
axb.set_ylim(0, 1050)
axb.set_xlabel("Clock time / h (dotted: no dexamethasone)")
axb.set_ylabel("Plasma cortisol / (nmol/L)")
axb.set_title("B  Dexamethasone suppression test", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.0, 0.88))
fig.tight_layout()
