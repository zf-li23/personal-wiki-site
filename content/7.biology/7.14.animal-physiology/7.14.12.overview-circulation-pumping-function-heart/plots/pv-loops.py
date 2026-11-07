# Pressure-volume loops of the left ventricle and the Frank-Starling relation (lumped model, illustrative).
# The ventricle is a time-varying elastance: P = a(t) Emax (V - V0) + (1 - a(t)) Pd(V), with activation a(t)
# a raised-cosine twitch (rise 0.30 s, relaxation 0.12 s; heart rate 75 /min) and an exponential end-diastolic
# pressure-volume relation Pd(V) = Emin (exp(k (V - V0)) - 1) / k. It fills from a left atrium held at the
# filling pressure Pla (preload) through the mitral valve and ejects through the aortic valve into a
# three-element Windkessel (characteristic impedance Zc, compliance C, peripheral resistance R: afterload).
# Units: mL, mmHg, s. A: preload (Pla); B: afterload (R); C: contractility (Emax, the slope of the ESPVR);
# D: stroke volume against filling pressure Pla (Starling's ventricular function curve), normal and with
# Emax increased by sympathetic stimulation; the curve flattens because the stiff EDPVR limits filling.
import matplotlib.pyplot as plt
import numpy as np

BASE = dict(Pla=10.0, Emax=2.5, R=1.0, C=1.7, Zc=0.05, Emin=0.015, V0=10.0, k=0.026)


def act(tc, tp=0.30, tr=0.12):
    return np.where(tc < tp, 0.5 * (1 - np.cos(np.pi * tc / tp)),
                    np.where(tc < tp + tr, 0.5 * (1 + np.cos(np.pi * (tc - tp) / tr)), 0.0))


def beat(hr=75.0, beats=10, dt=2e-4, Rmv=0.01, Rav=0.005, **kw):
    p = dict(BASE)
    p.update(kw)
    T = 60.0 / hr
    n = int(beats * T / dt)
    a = act(np.mod(np.arange(n) * dt, T))
    V, Pa = 120.0, 85.0
    out = np.empty((n, 2))
    for i in range(n):
        Pd = p["Emin"] * (np.exp(p["k"] * (V - p["V0"])) - 1) / p["k"]
        P = a[i] * p["Emax"] * (V - p["V0"]) + (1 - a[i]) * Pd
        qin = max(0.0, (p["Pla"] - P) / Rmv)
        qout = max(0.0, (P - Pa) / (Rav + p["Zc"]))
        out[i] = (V, P)
        V += dt * (qin - qout)
        Pa += dt * (qout - Pa / p["R"]) / p["C"]
    last = out[int((beats - 1) * T / dt):]
    return last[:, 0], last[:, 1]


Vg = np.linspace(10, 170, 200)
fig, axs = plt.subplots(1, 4, figsize=(15, 4.0))
cases = [
    ("A  Preload", "Pla", [(6.0, "low"), (10.0, "normal"), (15.0, "high")]),
    ("B  Afterload", "R", [(0.7, "low"), (1.0, "normal"), (1.6, "high")]),
    ("C  Contractility", "Emax", [(1.6, "low"), (2.5, "normal"), (4.0, "high")]),
]
colors = ["#2f6fb5", "0.25", "#c0392b"]
for ax, (title, key, vals) in zip(axs[:3], cases):
    ed = BASE["Emin"] * (np.exp(BASE["k"] * (Vg - BASE["V0"])) - 1) / BASE["k"]
    ax.plot(Vg, ed, color="0.6", lw=1, ls="--")
    for (v, lab), c in zip(vals, colors):
        V, P = beat(**{key: v})
        ax.plot(V, P, color=c, lw=2, label=f"{lab} ({key} = {v:g})")
        if key == "Emax":
            ax.plot(Vg, v * (Vg - BASE["V0"]), color=c, lw=0.9, ls=":")
    if key != "Emax":
        ax.plot(Vg, BASE["Emax"] * (Vg - BASE["V0"]), color="0.6", lw=1, ls=":")
    ax.text(165, 6, "EDPVR", ha="right", fontsize=8, color="0.45")
    ax.set_xlim(0, 170)
    ax.set_ylim(0, 160)
    ax.set_xlabel("LV volume / mL")
    ax.set_title(title, loc="left", fontsize=11, fontweight="bold")
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
axs[0].set_ylabel("LV pressure / mmHg")
axs[1].text(76, 155, "ESPVR", fontsize=8, color="0.45")

ax = axs[3]
for Emax, c, lab in ((2.5, "0.25", "normal"), (4.0, "#c0392b", "sympathetic (Emax x 1.6)")):
    plas, sv = np.linspace(1, 25, 13), []
    for pla in plas:
        V, P = beat(Pla=pla, Emax=Emax)
        sv.append(V.max() - V.min())
    ax.plot(plas, sv, "o-", color=c, lw=2, ms=3.5, label=lab)
ax.set_xlabel("Filling pressure (left atrium) / mmHg")
ax.set_ylabel("Stroke volume / mL")
ax.set_title("D  Starling curve", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
fig.tight_layout()
