# Conduction velocity in a chain of coupled cardiac cells against gap-junction coupling.
# Each cell obeys the Aliev-Panfilov model of cardiac excitation (dimensionless u, v):
#   du_i/dt = g (u_{i+1} - 2 u_i + u_{i-1}) + k u (1 - u)(u - a) - u v
#   dv_i/dt = (eps + mu1 v / (u + mu2)) (-v - k u (u - a - 1)),  k = 8, a = 0.15, eps = 0.002, mu1 = 0.2, mu2 = 0.3
# g is the intercellular (gap-junction) coupling. Velocities are scaled so that normal coupling (g = 10)
# gives 0.5 m/s with 100-um cells (one model time unit = 0.88 ms). A continuous cable predicts
# velocity proportional to sqrt(g), that is to 1/sqrt(r_i) (dashed); in the discrete chain conduction slows
# further and finally fails at about 1 % of normal coupling (source-sink mismatch). B: activation time along
# the chain for three couplings; at low coupling the delay is concentrated at the junctions (staircase).
import matplotlib.pyplot as plt
import numpy as np

K, A, EPS, MU1, MU2 = 8.0, 0.15, 0.002, 0.2, 0.3
G0, CELL_UM, V0 = 10.0, 100.0, 0.5


def activation_times(g, N=80, dt=0.002, tmax=2500.0):
    u = np.zeros(N)
    v = np.zeros(N)
    u[:3] = 1.0
    tact = np.full(N, np.nan)
    t = 0.0
    lap = np.empty(N)
    while t < tmax:
        lap[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
        lap[0] = u[1] - u[0]
        lap[-1] = u[-2] - u[-1]
        du = g * lap + K * u * (1 - u) * (u - A) - u * v
        dv = (EPS + MU1 * v / (u + MU2)) * (-v - K * u * (u - A - 1))
        u += dt * du
        v += dt * dv
        t += dt
        new = (u > 0.5) & np.isnan(tact)
        tact[new] = t
        if not np.isnan(tact[N - 15]) or (t > 60 and u.max() < 0.3):
            break
    return tact


def velocity(tact, i0=25, i1=-15):
    if np.isnan(tact[i1]):
        return 0.0
    return (len(tact) + i1 - i0) / (tact[i1] - tact[i0])


v_norm = velocity(activation_times(G0))
tunit = v_norm / (V0 * 1e3 / CELL_UM)  # ms per model time unit
gs = G0 * np.logspace(0.3, -2.3, 24)
cv = np.array([velocity(activation_times(g)) for g in gs]) / v_norm * V0

fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.2))
rel = gs / G0
ok = cv > 0
axa.loglog(rel[ok], cv[ok], "o-", color="#c0392b", lw=2, ms=4, label="discrete chain (simulation)")
axa.loglog(rel, V0 * np.sqrt(rel), "--", color="0.45", lw=1.2, label="continuous cable: $\\theta \\propto 1/\\sqrt{r_i}$")
fail = rel[~ok].max() if (~ok).any() else None
if fail is not None:
    axa.axvline(fail, color="#2f6fb5", lw=0.9, ls=":")
    axa.text(fail * 1.15, 0.012, "block", color="#2f6fb5", fontsize=8.5)
axa.axvline(1, color="0.6", lw=0.8, ls=":")
axa.axvline(0.5, color="0.6", lw=0.8, ls=":")
axa.text(0.52, 1.1, "Cx43 +/-", fontsize=8, color="0.4", ha="right")
axa.set_xlabel("Gap-junction coupling (normal = 1)")
axa.set_ylabel("Conduction velocity / (m/s)")
axa.set_ylim(0.01, 1.5)
axa.set_title("A  Velocity against coupling", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="lower right")

for g, c in ((G0, "0.2"), (G0 * 0.1, "#d9822b"), (G0 * 0.012, "#c0392b")):
    ta = activation_times(g)
    x = np.arange(len(ta)) * CELL_UM / 1000.0
    k = np.arange(len(ta)) >= 20
    axb.plot(x[k] - x[20], (ta[k] - ta[20]) * tunit, color=c, lw=1.8, drawstyle="steps-post",
             label=f"coupling {g / G0:g}")
axb.set_xlim(0, 4)
axb.set_ylim(0, 120)
axb.set_xlabel("Distance / mm")
axb.set_ylabel("Activation time / ms")
axb.set_title("B  Delay moves into the junctions", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left")
for a in (axa, axb):
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)
fig.tight_layout()
