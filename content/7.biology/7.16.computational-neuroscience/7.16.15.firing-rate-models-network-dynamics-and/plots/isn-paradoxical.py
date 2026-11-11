"""The paradoxical effect in an inhibition-stabilized network (threshold-linear E-I model).

tau_E dr_E/dt = -r_E + [w_EE r_E - w_EI r_I + h_E]_+,  tau_I dr_I/dt = -r_I + [w_IE r_E - w_II r_I + h_I]_+,
tau_E = 20 ms, tau_I = 10 ms; w_EI is the strength of the I -> E connection, w_IE that of E -> I.
ISN: w_EE = 1.5, w_EI = 2, w_IE = 4, w_II = 2 (w_EE > 1; Jacobian eigenvalues -1.25 +- 2.2i in units
of 1/tau for tau_E = tau_I). Non-ISN: w_EE = 0.5, w_EI = 1.5, w_IE = 3, w_II = 1.
Drive h_E = 10; h_I steps from 1 to 5 at t = 0.
A: ISN phase plane: E nullcline (blue) and I nullcline (red) before (solid) and after (dashed) the
   step; dots are the fixed points: raising the drive to I moves the fixed point to lower r_I.
B: time courses in the ISN (damped oscillation of both rates, final r_I below its initial value).
C: time courses in the non-ISN (r_I rises, r_E falls).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tE, tI = 20.0, 10.0
relu = lambda x: np.maximum(x, 0.0)


def simulate(w, hI0, hI1, T=300.0, dt=0.05):
    wEE, wEI, wIE, wII = w
    hE = 10.0
    # fixed point of the linear regime before the step
    A = np.array([[1 - wEE, wEI], [-wIE, 1 + wII]])
    r = np.linalg.solve(A, [hE, hI0])
    n = int(T / dt)
    out = np.empty((n, 2))
    for k in range(n):
        out[k] = r
        hI = hI1 if k * dt >= 50.0 else hI0
        dE = (-r[0] + relu(wEE * r[0] - wEI * r[1] + hE)) / tE
        dI = (-r[1] + relu(wIE * r[0] - wII * r[1] + hI)) / tI
        r = r + dt * np.array([dE, dI])
    return np.arange(n) * dt - 50.0, out


isn = (1.5, 2.0, 4.0, 2.0)
non = (0.5, 1.5, 3.0, 1.0)
fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
wEE, wEI, wIE, wII = isn
rE = np.linspace(0, 8, 100)
ax.plot(rE, (10 - (1 - wEE) * rE) / wEI, color=P.edge("dna"), lw=2.2, label="E nullcline")
for h, ls in ((1, "-"), (5, "--")):
    ax.plot(rE, (wIE * rE + h) / (1 + wII), color=P.edge("negative"), lw=2.0, ls=ls, label=f"I nullcline, $h_I$ = {h}")
    e = (15 - h) / 3.25
    ax.plot(e, (wIE * e + h) / (1 + wII), "o", ms=7, color=P.ink(), zorder=5)
ax.annotate("", xy=((15 - 5) / 3.25 + 0.05, (4 * (10 / 3.25) + 5) / 3 + 0.0), xytext=((15 - 1) / 3.25, (4 * (14 / 3.25) + 1) / 3),
            arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.3))
ax.set_xlim(0, 8)
ax.set_ylim(0, 12)
ax.set_xlabel("$r_E$ / Hz")
ax.set_ylabel("$r_I$ / Hz")
ax.set_title("A  ISN phase plane", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for ax, w, ttl in ((axs[1], isn, "B  ISN: $r_I$ falls"), (axs[2], non, "C  Non-ISN: $r_I$ rises")):
    t, r = simulate(w, 1.0, 5.0)
    ax.plot(t, r[:, 0], color=P.edge("dna"), lw=2.0, label="$r_E$")
    ax.plot(t, r[:, 1], color=P.edge("negative"), lw=2.0, label="$r_I$")
    ax.axvline(0, color=P.muted(), lw=0.8, ls=":")
    ax.set_xlim(-50, 250)
    ax.set_xlabel("Time from step in $h_I$ / ms")
    ax.set_ylabel("Rate / Hz")
    ax.set_title(ttl, loc="left", fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc="center right")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
