"""Saccades by a pulse-step command and the oculomotor neural integrator.

Eye plant (Robinson): tau_p dtheta/dt = -theta + u, tau_p = 0.2 s, with the motor neuron command u
in degrees of equivalent eye position. Burst neurons fire B(t) = B_max (1 - exp(-|e|/e0)) sign(e)
during a saccade, e = target - eye position as estimated from an efference copy (local feedback
model of Robinson, 1975), B_max = 600 deg/s, e0 = 8 deg; omnipause neurons release a saccade when
|e| > 1 deg and end
it when |e| < 0.3 deg or after 150 ms (minimum intersaccadic interval 150 ms). The neural integrator holds the eye
position command: dP/dt = B - (1 - w) P / tau_n, tau_n = 0.1 s (a recurrent network with feedback
gain w). Motor neurons: u = P + tau_p B (the step plus the pulse), so that dtheta/dt = B when P is
a perfect integral.
A: one 15 deg saccade: burst (pulse), integrator output (step), motor neuron command, eye position.
B: a sequence of targets with a well-tuned (w = 1), leaky (w = 0.9, time constant 1 s) and
unstable (w = 1.03) integrator: the leaky eye drifts back toward the center and corrective saccades
recur (gaze-evoked nystagmus), the unstable eye drifts away from the center.
C: main sequence of the model: peak velocity and duration against saccade amplitude.
D: time constant of the integrator tau_n / |1 - w| against the mistuning |1 - w|; the observed
time constant of about 20 s requires |1 - w| < 0.005.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt, tau_p, tau_n, Bmax, e0 = 0.0005, 0.2, 0.1, 600.0, 8.0


def run(targets, w, T):
    n = int(T / dt)
    th = Pint = 0.0
    sacc, last_end = False, -1.0
    out = np.zeros((n, 5))
    for i in range(n):
        t = i * dt
        tgt = targets(t)
        err = tgt - th                         # motor error from an efference copy of eye position
        if not sacc and abs(err) > 1.0 and t - last_end > 0.15:
            sacc, start = True, t
        if sacc and (abs(err) < 0.3 or t - start > 0.15):
            sacc, last_end = False, t
        B = Bmax * (1 - np.exp(-abs(err) / e0)) * np.sign(err) if sacc else 0.0
        Pint += dt * (B - (1 - w) * Pint / tau_n)
        u = Pint + tau_p * B
        th += dt / tau_p * (u - th)
        out[i] = (t, B, Pint, u, th)
    return out


fig, axs = plt.subplots(1, 4, figsize=(15, 3.7), gridspec_kw={"width_ratios": [1, 1.6, 1, 1]})
ax = axs[0]
o = run(lambda t: 15.0 if t > 0.05 else 0.0, 1.0, 0.25)
ms = o[:, 0] * 1e3
ax.plot(ms, o[:, 1] / 40, color=P.edge("negative"), lw=1.4, label="burst neurons /40 (pulse)")
ax.plot(ms, o[:, 2], color=P.edge("dna"), lw=1.4, label="integrator (step)")
ax.plot(ms, o[:, 3] / 2, color=P.edge("neuron"), lw=1.2, ls="--", label="motor neurons /2")
ax.plot(ms, o[:, 4], color=P.ink(), lw=2.0, label="eye position")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("deg, or scaled rate")
ax.set_title("A  Pulse and step", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7, loc="center right")

ax = axs[1]
tg = lambda t: 0.0 if t < 0.2 else (15.0 if t < 2.2 else (-20.0 if t < 4.2 else 0.0))
for w, lab, tok in ((1.0, "tuned, $w = 1$", "neutral"), (0.9, "leaky, $w = 0.9$", "dna"),
                    (1.03, "unstable, $w = 1.03$", "negative")):
    o = run(tg, w, 5.0)
    ax.plot(o[:, 0], o[:, 4], color=P.edge(tok) if tok != "neutral" else P.ink(), lw=1.5, label=lab)
tt = np.linspace(0, 5, 500)
ax.plot(tt, [tg(x) for x in tt], color=P.muted(), lw=0.8, ls=":", label="target")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Eye position (deg)")
ax.set_title("B  Integrator tuning", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7, ncol=2, loc="center", bbox_to_anchor=(0.62, 0.55))

ax = axs[2]
amps = np.array([2, 4, 6, 8, 10, 15, 20, 25, 30, 40])
pv, du = [], []
for A in amps:
    o = run(lambda t, A=A: A if t > 0.01 else 0.0, 1.0, 0.25)
    v = np.gradient(o[:, 4], dt)
    pv.append(v.max())
    act = o[:, 1] > 0
    du.append(act.sum() * dt * 1e3)
ax.plot(amps, pv, "o-", color=P.edge("negative"), lw=1.5, ms=3.5)
ax.set_xlabel("Amplitude (deg)")
ax.set_ylabel("Peak velocity (deg/s)", color=P.edge("negative"))
ax2 = ax.twinx()
ax2.plot(amps, du, "s-", color=P.edge("dna"), lw=1.5, ms=3.5)
ax2.set_ylabel("Duration (ms)", color=P.edge("dna"))
ax.set_title("C  Main sequence", loc="left", fontsize=10)

ax = axs[3]
mis = np.logspace(-4, -0.5, 50)
ax.loglog(mis, tau_n / mis, color=P.ink(), lw=1.8)
ax.axhline(20, color=P.edge("negative"), lw=0.8, ls="--")
ax.text(1.2e-4, 32, "observed, about 20 s", fontsize=7, color=P.edge("negative"))
ax.axhline(tau_n, color=P.muted(), lw=0.8, ls=":")
ax.text(1.2e-4, 0.12, "single-neuron $\\tau_n$", fontsize=7, color=P.muted())
ax.set_xlabel("Mistuning $|1 - w|$")
ax.set_ylabel("Integrator time constant (s)")
ax.set_title("D  Fine tuning", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
