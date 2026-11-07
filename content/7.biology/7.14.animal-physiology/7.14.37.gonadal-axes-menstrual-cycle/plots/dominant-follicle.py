# Selection of a single dominant follicle by competition for FSH (illustrative model, time in days).
#   Follicle diameters s_i (mm), a cohort of 10 antral follicles of 2-5 mm at the start of the cycle.
#   FSH responsiveness R_i = r_i (1 + a s_i^2 / (s_i^2 + K^2)): estradiol made by a follicle raises its own
#   FSH receptors (local positive feedback); r_i differ slightly between follicles.
#   ds_i/dt = g (FSH R_i + LH h(s_i) - theta)   growth above the threshold, atresia (shrinkage) below it;
#   h(s) = s^6 / (s^6 + KL^6): granulosa cells of large follicles acquire LH receptors and need less FSH
#   FSH = F0 / (1 + (E / KE)^2),  E = sum_i (s_i / 10)^3   systemic negative feedback: a shared resource.
# A: diameters; B: serum FSH and the FSH threshold theta / R_i of the eventual dominant follicle
# and of the runner-up (the "FSH window").
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

rng = np.random.default_rng(3)
N = 10
s0 = np.sort(rng.uniform(2.0, 5.0, N))
r = 1.0 + 0.04 * rng.standard_normal(N)
a, K, g, theta, F0, KE = 3.0, 10.0, 3.0, 1.0, 1.4, 1.5
LH, KL = 0.8, 11.0  # basal LH supports large follicles whose granulosa cells have acquired LH receptors


def resp(s):
    return r * (1.0 + a * s**2 / (s**2 + K**2))


def fsh(s):
    E = np.sum((np.maximum(s, 0.0) / 10.0) ** 3)
    return F0 / (1.0 + (E / KE) ** 2)


def rhs(t, s):
    s = np.maximum(s, 0.0)
    ds = g * (fsh(s) * resp(s) + LH * s**6 / (s**6 + KL**6) - theta)
    ds = np.where(s > 0.5, ds, np.maximum(ds, 0.0))  # fully atretic follicles stay at the floor
    return np.minimum(ds, 2.0)  # growth of the dominant follicle is at most about 2 mm per day


t = np.linspace(0, 14, 1401)
sol = solve_ivp(rhs, (0, 14), s0, t_eval=t, max_step=0.02)
S = np.maximum(sol.y, 0.5)
F = np.array([fsh(S[:, k]) for k in range(S.shape[1])])
dom = np.argmax(S[:, -1])
second = np.argsort(S[:, -1])[-2]

fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 4.4))
for i in range(N):
    col = "#c0392b" if i == dom else "0.55"
    axa.plot(t, S[i], color=col, lw=2.2 if i == dom else 1.1)
axa.set_xlabel("Day of follicular phase")
axa.set_ylabel("Follicle diameter / mm")
axa.set_title("A  One follicle becomes dominant", loc="left", fontsize=11, fontweight="bold")
axa.text(13.8, S[dom, -1] - 1.5, "dominant", ha="right", color="#c0392b", fontsize=9)
axa.text(13.8, 2.0, "atresia", ha="right", color="0.4", fontsize=9)

axb.plot(t, F, color="#2c6fbb", lw=2.2, label="serum FSH")
thr_dom = np.array([(theta - LH * S[dom, k] ** 6 / (S[dom, k] ** 6 + KL**6)) / resp(S[:, k])[dom] for k in range(S.shape[1])])
thr_2 = np.array([(theta - LH * S[second, k] ** 6 / (S[second, k] ** 6 + KL**6)) / resp(S[:, k])[second] for k in range(S.shape[1])])
axb.plot(t, thr_dom, color="#c0392b", lw=1.6, ls="--", label="FSH threshold, dominant")
axb.plot(t, thr_2, color="0.45", lw=1.6, ls=":", label="FSH threshold, runner-up")
axb.set_xlabel("Day of follicular phase")
axb.set_ylabel("Relative level")
axb.set_title("B  The closing FSH window", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper right")
fig.tight_layout()
