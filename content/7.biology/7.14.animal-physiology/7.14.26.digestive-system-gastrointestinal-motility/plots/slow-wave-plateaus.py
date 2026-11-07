# Frequency plateaus of intestinal slow waves as a chain of coupled phase oscillators.
#   d(theta_i)/dt = omega_i + K [sin(theta_{i+1} - theta_i) + sin(theta_{i-1} - theta_i)]
# 40 oscillators represent ICC segments from the duodenum (0 m) to the terminal ileum (5 m).
# Intrinsic frequencies omega_i/2pi fall linearly from 12 to 8 cycles/min (isolated segments).
# K is the nearest-neighbour coupling (gap junctions in the ICC-smooth muscle syncytium), in 1/min.
# A: realised frequency along the gut for three couplings; moderate coupling breaks the gradient into
# plateaus of locked segments separated by jumps. B: cos(theta) at six sites for the moderate
# coupling (cos(theta) at six sites, 30 s): waves lag aborally within a plateau; distal sites skip cycles.
import matplotlib.pyplot as plt
import numpy as np

N, L = 40, 5.0
x = np.linspace(0, L, N)
f_int = 12.0 - 4.0 * x / L
omega = 2 * np.pi * f_int


def run(K, T=80.0, dt=0.002, T0=30.0, keep=False):
    th = np.zeros(N)
    steps = int(T / dt)
    rec, t_rec = [], []
    th0 = None
    for s in range(steps):
        t = s * dt
        d = np.zeros(N)
        d[:-1] += np.sin(th[1:] - th[:-1])
        d[1:] += np.sin(th[:-1] - th[1:])
        th = th + dt * (omega + K * d)
        if th0 is None and t >= T0:
            th0 = th.copy()
        if keep and t >= T - 1.0:
            rec.append(np.cos(th))
            t_rec.append(t - (T - 1.0))
    f = (th - th0) / (2 * np.pi * (T - T0))
    return f, np.array(rec), np.array(t_rec)


fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.3))
axa.plot(x, f_int, "--", color="0.5", lw=1.2, label="intrinsic (uncoupled)")
for K, c in ((20.0, "#d9822b"), (80.0, "#c0392b")):
    f, _, _ = run(K)
    axa.plot(x, f, color=c, lw=2, label=f"coupled, K = {K:g} /min")
axa.set_xlabel("Distance from pylorus / m")
axa.set_ylabel("Slow-wave frequency / (cycles/min)")
axa.set_ylim(7.5, 12.5)
axa.set_title("A  Frequency plateaus", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right")

f, rec, tr = run(20.0, keep=True)
for k, i in enumerate(np.linspace(0, N - 1, 6).astype(int)):
    axb.plot(tr * 60, 0.4 * rec[:, i] - 1.2 * k, color="#2f6fb5", lw=1.3)
    axb.text(-1.0, -1.2 * k, f"{x[i]:.1f} m", ha="right", va="center", fontsize=8.5)
axb.set_xlim(0, 30)
axb.set_yticks([])
axb.set_xlabel("Time / s")
axb.set_title("B  Slow waves at six sites (K = 20 /min)", loc="left", fontsize=11, fontweight="bold")
for side in ("left", "right", "top"):
    axb.spines[side].set_visible(False)
fig.tight_layout()
