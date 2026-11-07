# External coincidence model of photoperiodic flowering (minimal ODE model, illustrative parameters).
# (K = 0.7, Kr = 0.3, g = 0.25 /h.) The clock drives CO mRNA m(t) with a peak 14 h after dawn (ZT 14). CO protein P is made in proportion
# to m and degraded quickly in darkness (COP1-SPA) and in the early morning (phyB), but is stable in
# the late afternoon light (phyA, cry2):
#   dP/dt = ks m(t) - kd(t) P,  kd = 0.12 /h (light, ZT >= 4), 0.8 /h (light, ZT < 4), 1.5 /h (dark)
#   dF/dt = v P^4 / (K^4 + P^4) - g F           (FT mRNA, Arabidopsis: CO activates FT)
#   dH/dt = v Kr^4 / (Kr^4 + Pl^4) - g H         (Hd3a mRNA, rice: light-active Hd1 represses Hd3a;
#                                              Pl = P during the light period, 0 in darkness)
# A, B: 16 h and 8 h photoperiods (grey bands = night; levels scaled to the 16 h maxima).
# C: daily mean FT and Hd3a against photoperiod.
import matplotlib.pyplot as plt
import numpy as np

ks, v, K, Kr, g, hill = 0.3, 1.0, 0.7, 0.3, 0.25, 4
dt = 0.02


def mrna(t):
    return 0.08 + 0.92 * ((1 + np.cos(2 * np.pi * (t - 14) / 24)) / 2) ** 2


def run(photo, days=6):
    n = int(days * 24 / dt)
    t = np.arange(n) * dt
    P = F = H = 0.0
    out = np.zeros((n, 4))
    for i, ti in enumerate(t):
        z = ti % 24
        light = z < photo
        kd = (0.8 if z < 4 else 0.12) if light else 1.5
        m = mrna(z)
        Pl = P if light else 0.0
        P += dt * (ks * m - kd * P)
        F += dt * (v * P**hill / (K**hill + P**hill) - g * F)
        H += dt * (v * Kr**hill / (Kr**hill + Pl**hill) - g * H)
        out[i] = (m, P, F, H)
    return t, out


fig = plt.figure(figsize=(11, 4.6))
gs = fig.add_gridspec(2, 2, width_ratios=[1.35, 1], hspace=0.35, wspace=0.28)
for row, photo in enumerate([16, 8]):
    ax = fig.add_subplot(gs[row, 0])
    t, o = run(photo)
    sel = t >= 96
    tt = t[sel] - 96
    for d0 in (0, 24):
        ax.axvspan(d0 + photo, d0 + 24, color="0.55", alpha=0.18, lw=0)
    ax.plot(tt, o[sel, 0], color="#d9822b", lw=1.6, label="CO mRNA")
    ax.plot(tt, o[sel, 1] / 1.4, color="#2f6fb5", lw=2.0, label="CO protein")
    ax.plot(tt, o[sel, 2] / 2.6, color="#3a9a5b", lw=2.0, label="FT mRNA")
    ax.set_xlim(0, 48)
    ax.set_ylim(0, 1.15)
    ax.set_xticks(range(0, 49, 8))
    ax.set_yticks([0, 0.5, 1])
    ax.set_ylabel("Relative level")
    ax.text(0.5, 1.03, f"{photo} h light : {24 - photo} h dark", fontsize=9, ha="left")
    ax.spines[["top", "right"]].set_visible(False)
    if row == 0:
        ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper right", bbox_to_anchor=(1.0, 1.25))
        ax.set_xticklabels([])
    else:
        ax.set_xlabel("Time from dawn / h")
    ax.text(-0.13, 1.08, "AB"[row], transform=ax.transAxes, fontsize=12, weight="bold")

cx = fig.add_subplot(gs[:, 1])
photos = np.arange(6, 20.01, 0.5)
ft, hd = [], []
for p in photos:
    t, o = run(p, days=5)
    last = t >= 96
    ft.append(o[last, 2].mean())
    hd.append(o[last, 3].mean())
ft = np.array(ft) / max(ft)
hd = np.array(hd) / max(hd)
cx.plot(photos, ft, color="#3a9a5b", lw=2.2, marker="o", ms=3, label="FT (Arabidopsis, LDP)")
cx.plot(photos, hd, color="#9c6bc4", lw=2.2, marker="s", ms=3, label="Hd3a (rice, SDP)")
cx.set_xlabel("Photoperiod / h")
cx.set_ylabel("Daily mean florigen mRNA (relative)")
cx.set_xlim(6, 20)
cx.set_ylim(0, 1.08)
cx.legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.42))
cx.spines[["top", "right"]].set_visible(False)
cx.text(-0.15, 1.02, "C", transform=cx.transAxes, fontsize=12, weight="bold")
