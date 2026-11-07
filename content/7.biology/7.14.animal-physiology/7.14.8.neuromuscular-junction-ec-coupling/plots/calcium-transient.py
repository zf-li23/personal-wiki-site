# Myoplasmic Ca2+ transient of a fast-twitch fibre: a single-compartment model (units uM and ms; parameters
# after Baylor & Hollingworth's models of mouse fast fibres, rounded).
#   dc/dt = J_rel(t) + J_leak - J_SERCA - d[CaTn]/dt - d[CaPv]/dt
#   J_rel: an action potential releases 350 uM of Ca2+ from the SR (Gaussian flux, half-width ~1.6 ms); in a train
#   release is smaller, 350 (1 - 0.7 exp(-interval / 30 ms)) uM, as RyR1 inactivates and the SR runs down
#   J_SERCA = Vmax c^2 / (Km^2 + c^2), Vmax = 4.9 uM/ms, Km = 1 uM; a constant leak keeps rest at 0.05 uM
#   troponin C regulatory sites: 240 uM, kon = 0.0885 /uM/ms, koff = 0.4 /ms (fast, the Ca2+ switch)
#   parvalbumin: 1500 uM, effective kon = 0.004 /uM/ms, koff = 0.002 /ms (slow: Mg2+ must leave first)
# (A) one twitch; (B) relaxation of troponin occupancy with half the SERCA activity or without parvalbumin;
# (C) trains at 10, 30 and 80 Hz: occupancy summates and fuses as the stimulus interval falls below the
#     decay time of the transient (the basis of tetanus).
import matplotlib.pyplot as plt
import numpy as np

DT = 0.002


def run(tmax, spikes, vmax=4.9, pv=1500.0):
    n = int(tmax / DT)
    t = np.arange(n) * DT
    c0, km, ttot, kon, koff = 0.05, 1.0, 240.0, 0.0885, 0.4
    pkon, pkoff = 0.004, 0.002
    leak = vmax * c0**2 / (km**2 + c0**2)
    c = c0
    tn = ttot * kon * c0 / (kon * c0 + koff)
    pb = pv * pkon * c0 / (pkon * c0 + pkoff) if pv else 0.0
    sig = 0.7
    out = np.empty((n, 3))
    sp = np.asarray(spikes, float)
    isi = np.diff(sp, prepend=-1e9)
    amt = 350.0 * (1 - 0.7 * np.exp(-isi / 30.0))
    for i in range(n):
        rel = np.sum(amt * np.exp(-((t[i] - sp - 1.5) ** 2) / (2 * sig**2)) / (sig * np.sqrt(2 * np.pi)))
        dtn = kon * c * (ttot - tn) - koff * tn
        dpb = (pkon * c * (pv - pb) - pkoff * pb) if pv else 0.0
        dc = rel + leak - vmax * c**2 / (km**2 + c**2) - dtn - dpb
        c += DT * dc
        tn += DT * dtn
        pb += DT * dpb
        out[i] = c, tn / ttot, (pb / pv if pv else 0.0)
    return t, out


fig, (a, b, cax) = plt.subplots(1, 3, figsize=(13.5, 4.2))
t, o = run(60, [0.0])
a.plot(t, o[:, 0], color="#2f6fb5", lw=2.2, label="free [Ca²⁺]")
a.set_xlabel("Time after the action potential / ms")
a.set_ylabel("Free [Ca²⁺] / µM", color="#2f6fb5")
a.set_ylim(0, 18)
a2 = a.twinx()
a2.plot(t, o[:, 1], color="#c0504d", lw=2.0, label="troponin C occupied")
a2.plot(t, o[:, 2], color="#d9a03f", lw=2.0, ls="--", label="parvalbumin occupied")
a2.set_ylabel("Fraction of sites occupied")
a2.set_ylim(0, 1.05)
lines = a.get_lines() + a2.get_lines()
a.legend(lines, [l.get_label() for l in lines], frameon=False, fontsize=8.5, loc="upper right")
a.set_title("A   One twitch", loc="left", fontsize=10)
a.text(0.97, 0.55, f"peak free Ca²⁺ = {o[:, 0].max():.0f} µM", transform=a.transAxes, ha="right", fontsize=8.5)

for (name, kw, col, ls) in (("control", {}, "#c0504d", "-"), ("SERCA activity halved", {"vmax": 2.45}, "#7a5fb0", "--"),
                            ("no parvalbumin", {"pv": 0.0}, "#2f9e8f", ":")):
    t, o = run(150, [0.0], **kw)
    b.plot(t, o[:, 1], color=col, lw=2.2, ls=ls, label=name)
b.set_xlabel("Time / ms")
b.set_ylabel("Troponin C occupancy")
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=8.5, loc="upper right")
b.set_title("B   What ends the Ca²⁺ signal", loc="left", fontsize=10)

for f, col in ((10, "#8fb3d9"), (30, "#2f6fb5"), (80, "#1f3f73")):
    sp = np.arange(0, 300, 1000.0 / f)
    t, o = run(320, sp)
    cax.plot(t, o[:, 1], color=col, lw=1.8, label=f"{f} Hz")
cax.set_xlabel("Time / ms")
cax.set_ylabel("Troponin C occupancy")
cax.set_ylim(0, 1.18)
cax.legend(frameon=False, fontsize=8.5, loc="upper left", ncol=3)
cax.set_title("C   Trains of action potentials", loc="left", fontsize=10)
for x in (a, b, cax):
    x.spines[["top"]].set_visible(False)
for x in (b, cax):
    x.spines[["right"]].set_visible(False)
fig.tight_layout()
