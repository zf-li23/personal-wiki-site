"""Two-element Windkessel: C dP/dt = Q_in(t) - P/R.

Q_in: half-sine ejection lasting 0.3 s each beat, heart rate 75 /min, stroke volume 70 mL.
R = 1.0 mmHg s/mL (total peripheral resistance, about 1 PRU); C = 1.5 mL/mmHg (young, compliant aorta),
0.75 (stiffer) and 0.4 (stiff, elderly). Mean pressure = mean flow x R does not depend on C;
pulse pressure grows as C falls, and the diastolic decay has time constant tau = RC.
A: pressure waveforms at steady state. B: pulse pressure and systolic/diastolic pressure against C;
dashed line: the estimate SV/C when ejection is fast compared with tau.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P

HR, SV, Te, R = 75.0, 70.0, 0.3, 1.0
T = 60.0 / HR
Qpk = SV * np.pi / (2 * Te)


def qin(t):
    ph = t % T
    return np.where(ph < Te, Qpk * np.sin(np.pi * ph / Te), 0.0)


def run(C, n_beats=20, dt=1e-3):
    t = np.arange(0, n_beats * T, dt)
    p = np.empty_like(t)
    p[0] = 80.0
    q = qin(t)
    for i in range(1, len(t)):
        p[i] = p[i - 1] + dt * (q[i - 1] - p[i - 1] / R) / C
    return t, p, q


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.2), gridspec_kw={"width_ratios": [1.4, 1]})
cols = [P.edge("dna"), P.edge("protein"), P.edge("blood")]
for C, col, lab in zip([1.5, 0.75, 0.4], cols, ["C = 1.5 mL/mmHg (young)", "C = 0.75", "C = 0.4 (stiff)"]):
    t, p, q = run(C)
    m = t >= 17 * T
    ax.plot(t[m] - 17 * T, p[m], color=col, lw=2, label=lab)
t, p, q = run(1.5)
m = t >= 17 * T
ax2 = ax.twinx()
ax2.fill_between(t[m] - 17 * T, 0, q[m], color=P.fill("neutral"), alpha=0.3, lw=0)
ax2.set_ylim(0, 1500)
ax2.set_yticks([])
ax.text(0.15, 35, "ejection\n(inflow)", fontsize=8, color=P.muted(), ha="center")
ax.axhline(SV / T * R, color=P.muted(), ls=":", lw=1)
ax.text(0.62, SV / T * R - 7, "mean = Q R", fontsize=8, color=P.muted())
ax.set_xlim(0, 2.4)
ax.set_ylim(20, 170)
ax.set_zorder(ax2.get_zorder() + 1)
ax.patch.set_visible(False)
ax.set_xlabel("Time / s")
ax.set_ylabel("Aortic pressure / mmHg")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Same mean, larger swing when the aorta stiffens", loc="left", fontsize=10)

Cs = np.linspace(0.3, 2.5, 30)
pp, ps, pd = [], [], []
for C in Cs:
    t, p, q = run(C)
    w = p[t >= 15 * T]
    ps.append(w.max())
    pd.append(w.min())
    pp.append(w.max() - w.min())
bx.plot(Cs, ps, color=P.edge("blood"), lw=2, label="systolic")
bx.plot(Cs, pd, color=P.edge("dna"), lw=2, label="diastolic")
bx.plot(Cs, pp, color=P.ink(), lw=2, label="pulse pressure")
bx.plot(Cs, SV / Cs, color=P.ink(), lw=1, ls="--", label="SV / C")
bx.set_ylim(0, 220)
bx.set_xlabel("Arterial compliance C / mL mmHg$^{-1}$")
bx.set_ylabel("Pressure / mmHg")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Pulse pressure against compliance", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
