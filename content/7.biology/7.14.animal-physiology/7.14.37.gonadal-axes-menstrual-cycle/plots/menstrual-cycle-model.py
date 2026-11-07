# A minimal model of the human menstrual cycle (time in days; all quantities in relative units).
# Its structure follows the published models of Selgrade, Harris-Clark and colleagues in a reduced form;
# parameters are illustrative.
#   FSH:  dFSH/dt = kF / (1 + E/KEf + (Inh/KI)^2) - cF FSH          estradiol and inhibin suppress FSH
#   LH pool (pituitary) RP and serum LH:
#         synthesis  = (V0 + V1 E^4/(KEs^4 + E^4)) / (1 + P/Kp)    estradiol builds the pool, progesterone blocks
#         release    = (k0 + k1 E^n/(KEr^n + E^n) / (1 + (P/KPr)^2)) RP, n = 40
#                      a steep estradiol threshold opens release: negative feedback turns into positive
#         dRP/dt = synthesis - release ; dLH/dt = release - cL LH
#   Follicle F:  dF/dt = gF (F + f0) max(FSH (1 + (F/Fk)^2) - th0, 0) (1 - F/Fmax) - 0.05 F
#                (FSH threshold; FSH sensitivity grows with the follicle: local positive feedback)
#   Ovulation:   when LH reaches a threshold, the dominant follicle is committed (event) and luteinizes
#                over about a day (compartment Fo, which still secretes estradiol).
#   Corpus luteum: three-stage chain L1 -> L2 -> L3 -> regression (lifespan about 12-14 days).
#   E = e0 + eF (F + Fo) + eL (L2 + L3) ; P = p0 + pL (0.25 L1 + L2 + L3)/2 ; Inh = iF F + iL (L2 + L3)
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

p = dict(kF=3.0, KEf=1.5, KI=1.0, cF=3.0, V0=0.5, V1=10.0, KEs=1.2, Kp=1.0, k0=0.3, k1=200.0, KEr=2.2, nr=40,
         cL=16.0, KPr=0.6, gF=1.2, th0=0.55, Fk=1.0, Fmax=4.0, f0=0.02, tau=3.0, e0=0.3, eF=1.0, eL=0.6,
         p0=0.05, pL=2.0, iF=0.4, iL=1.0, LHov=0.5, seed=0.1, tov=1.0)


def obs(y):
    FSH, RP, LH, F, L1, L2, L3, Fo = y
    E = p["e0"] + p["eF"] * (F + Fo) + p["eL"] * (L2 + L3)
    P = p["p0"] + p["pL"] * (0.25 * L1 + L2 + L3) / 2
    Inh = p["iF"] * F + p["iL"] * (L2 + L3)
    return E, P, Inh


def rhs(t, y):
    FSH, RP, LH, F, L1, L2, L3, Fo = y
    E, P, Inh = obs(y)
    dFSH = p["kF"] / (1 + E / p["KEf"] + (Inh / p["KI"]) ** 2) - p["cF"] * FSH
    syn = (p["V0"] + p["V1"] * E**4 / (p["KEs"] ** 4 + E**4)) / (1 + P / p["Kp"])
    gate = E ** p["nr"] / (p["KEr"] ** p["nr"] + E ** p["nr"])
    rel = (p["k0"] + p["k1"] * gate / (1 + (P / p["KPr"]) ** 2)) * RP
    drive = FSH * (1 + (F / p["Fk"]) ** 2) - p["th0"]
    dF = p["gF"] * max(drive, 0.0) * (F + p["f0"]) * max(1 - F / p["Fmax"], 0.0) - 0.05 * F
    tau = p["tau"]
    rupt = Fo / p["tov"]  # the ovulating follicle luteinizes over about a day
    return [dFSH, syn - rel, rel - p["cL"] * LH, dF, rupt - L1 / tau, (L1 - L2) / tau, (L2 - L3) / tau, -rupt]


def run(T):
    y, t0, ts, ys, ovs = [0.3, 1.0, 0.1, 0.05, 0.0, 0.0, 0.0, 0.0], 0.0, [], [], []

    def ev(t, y):
        return y[2] - p["LHov"]

    ev.terminal, ev.direction = True, 1
    while t0 < T:
        te = np.arange(np.ceil(t0 * 20) / 20, T, 0.05)
        te = te[(te >= t0) & (te <= T)]
        s = solve_ivp(rhs, (t0, T), y, max_step=0.05, events=ev, t_eval=te)
        ts.append(s.t)
        ys.append(s.y)
        if s.status != 1:
            break
        t0 = s.t_events[0][0] + 1e-6
        y = s.y_events[0][0].copy()
        ovs.append(t0)
        y[7] += y[3]  # the LH surge commits the dominant follicle to ovulation
        y[3] = p["seed"]
        y[2] = p["LHov"] + 1e-6
    return np.concatenate(ts), np.hstack(ys), np.array(ovs)


t, y, ovs = run(150.0)
# show two cycles, aligned so that day 0 is menses onset (progesterone withdrawal) before the 4th ovulation
E, P, Inh = np.array([obs(y[:, i]) for i in range(y.shape[1])]).T
o3 = ovs[3]
win = (t > o3 - 40) & (t < o3 + 40)
Pw = np.where(win)[0]
# menses = time progesterone falls below 0.3 of its luteal maximum after the 3rd ovulation
after = (t > ovs[2]) & (t < o3)
pmax = P[after].max()
idx = np.where(after & (P < 0.3 * pmax) & (t > t[after][np.argmax(P[after])]))[0][0]
t_m = t[idx]
d = t - t_m
sel = (d >= -2) & (d <= 58)

fig, axs = plt.subplots(3, 1, figsize=(10.5, 8.2), sharex=True)
cols = dict(LH="#c0392b", FSH="#2c6fbb", E="#8e44ad", P="#2e8b57", F="#d68910", L="0.45")
axs[0].plot(d[sel], y[2][sel], color=cols["LH"], lw=2, label="LH")
axs[0].plot(d[sel], y[0][sel], color=cols["FSH"], lw=2, label="FSH")
axs[0].set_ylabel("Serum level\n(relative)")
axs[0].legend(frameon=False, fontsize=9, loc="upper right")
axs[0].set_title("A  Gonadotropins: intercycle FSH rise and the LH surge", loc="left", fontsize=11, fontweight="bold")
axs[1].plot(d[sel], E[sel], color=cols["E"], lw=2, label="estradiol")
axs[1].plot(d[sel], P[sel], color=cols["P"], lw=2, label="progesterone")
E_on = E[np.searchsorted(t, ovs[3]) - 1]
axs[1].axhline(E_on, color="0.6", lw=0.8, ls="--")
axs[1].text(57.5, E_on + 0.06, "estradiol at surge onset", ha="right", fontsize=8, color="0.4")
axs[1].set_ylabel("Ovarian steroid\n(relative)")
axs[1].legend(frameon=False, fontsize=9, loc="upper left")
axs[1].set_title("B  Ovarian steroids", loc="left", fontsize=11, fontweight="bold")
axs[2].plot(d[sel], y[3][sel], color=cols["F"], lw=2, label="growing follicles")
axs[2].plot(d[sel], (y[4] + y[5] + y[6] + y[7])[sel], color=cols["L"], lw=2, label="corpus luteum")
axs[2].set_ylabel("Tissue mass\n(relative)")
axs[2].legend(frameon=False, fontsize=9, loc="upper left")
axs[2].set_title("C  Follicle and corpus luteum", loc="left", fontsize=11, fontweight="bold")
axs[2].set_xlabel("Day of cycle (day 0 = onset of menses)")
for ax in axs:
    for ov in ovs:
        if -2 <= ov - t_m <= 58:
            ax.axvline(ov - t_m, color="0.7", lw=0.8, ls=":")
axs[0].text(ovs[3] - t_m + 0.4, axs[0].get_ylim()[1] * 0.9, "ovulation", fontsize=8, color="0.4")
axs[2].set_xlim(-2, 58)
fig.tight_layout()
