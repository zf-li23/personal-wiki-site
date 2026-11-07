# Enterohepatic circulation of bile acids: a three-compartment model (g, hours).
#   liver L: dL/dt = S + R - kL L                     hepatic secretion kL = 2 /h (canalicular BSEP)
#   gallbladder G: receives half of hepatic output between meals and leaks slowly (kGf = 0.15 /h,
#                  interdigestive partial emptying); empties at kG = 2 /h during the hour after each
#                  meal (CCK), when all hepatic output goes to the gut
#   intestine I: dI/dt = (hepatic and gallbladder inflow) - kT I,  kT = 1 /h (transit to the ileum)
#   ileal reabsorption R = f kT I (ASBT; f = fraction recovered per pass), fecal loss (1 - f) kT I
#   synthesis from cholesterol (CYP7A1) under FXR/FGF19 feedback: S = Smax / (1 + (R/R50)^2),
#   Smax = 0.25 g/h (6 g/day), R50 = 0.30 g/h; the model gives a 3 g pool, about 8 cycles a day
#   and a synthesis of about 0.7 g/day (= fecal loss) at f = 0.97
# Meals at 7, 12 and 18 h. A: content of each compartment over two days (f = 0.97). B: steady state against f; when ileal recovery fails (resection,
# sequestrants), synthesis rises toward its maximum but cannot keep the pool, and fat absorption fails.
import matplotlib.pyplot as plt
import numpy as np

kL, kG, kGf, kT, Smax, R50 = 2.0, 2.0, 0.15, 1.0, 0.25, 0.30
MEALS = (7.0, 12.0, 18.0)


def meal(t):
    h = t % 24
    return any(m <= h < m + 1 for m in MEALS)


def run(f, days=10, dt=0.01, L=0.2, G=1.0, I=1.0):
    n = int(days * 24 / dt)
    rec = np.zeros((n, 3))
    secr = syn = 0.0
    for i in range(n):
        t = i * dt
        R = f * kT * I
        S = Smax / (1 + (R / R50) ** 2)
        out = kL * L
        if meal(t):
            toG, toI, gb = 0.0, out, kG * G
        else:
            toG, toI, gb = 0.5 * out, 0.5 * out, kGf * G
        L += dt * (S + R - out)
        G += dt * (toG - gb)
        I += dt * (toI + gb - kT * I)
        rec[i] = (L, G, I)
        if t >= (days - 1) * 24:
            secr += dt * out
            syn += dt * S
    return rec, secr, syn


rec, secr, syn = run(0.97)
dt = 0.01
t = np.arange(len(rec)) * dt
k = t >= t[-1] - 48
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.3))
tt = t[k] - (t[-1] - 48)
for j, (name, c) in enumerate((("liver", "#c0392b"), ("gallbladder", "#2a9d8f"), ("intestine", "#2f6fb5"))):
    axa.plot(tt, rec[k, j], color=c, lw=1.8, label=name)
axa.plot(tt, rec[k].sum(axis=1), color="0.3", lw=1.2, ls="--", label="total pool")
for d in (0, 24):
    for m in MEALS:
        axa.axvspan(d + m, d + m + 1, color="0.85", lw=0)
axa.set_xlabel("Time / h")
axa.set_ylabel("Bile acid / g")
axa.set_xlim(0, 48)
axa.set_title(f"A  Two days (pool secreted {secr / rec[-1].sum():.1f} times/day)", loc="left",
              fontsize=11, fontweight="bold")
axa.set_ylim(0, 3.9)
axa.legend(frameon=False, fontsize=8, loc="upper center", ncol=4)

fs = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97, 0.98])
pools, syns = [], []
for f in fs:
    r, s1, s2 = run(f, days=12)
    pools.append(r[-int(24 / dt):].sum(axis=1).mean())
    syns.append(s2)
axb.plot(fs * 100, pools, "o-", color="#2f6fb5", lw=2, ms=4, label="pool / g")
axb.plot(fs * 100, syns, "s-", color="#c0392b", lw=2, ms=4, label="synthesis / (g/day)")
axb.axvline(97, color="0.6", lw=0.8, ls=":")
axb.text(96.5, 5.6, "normal", ha="right", fontsize=8.5, color="0.4")
axb.set_xlabel("Ileal recovery per pass / %")
axb.set_ylabel("g or g/day")
axb.set_ylim(0, 7)
axb.set_title("B  Feedback cannot replace recovery", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left")
fig.tight_layout()
