# Ripening of climacteric fruit as an autocatalytic ethylene switch (minimal model, illustrative
# parameters, relative units).
#   dE/dt = k0(t) + k1 E^4 / (1 + E^4) - k2 E,   k1 = 2, k2 = 1 /d
# k0 is the basal (System 1) ethylene production, which rises slowly as the fruit matures (here
# k0 = 0.05 + 0.07 t, at most 0.6); the Hill
# term is autocatalytic System 2 production (ethylene induces ACS and ACO). Respiration follows ethylene
# with a lag and is limited by depletion of respiratory substrate S:
#   dQ/dt = (S (Q0 + a E^2 / (1 + E^2)) - Q) / 1.5 d,  dS/dt = -(0.02 + 0.12 E) S,  Q0 = 1, a = 5.
# A: after harvest, a climacteric fruit (k1 = 2) shows a burst of ethylene followed by the respiratory
#    climacteric; a non-climacteric fruit (k1 = 0) does not; 1-MCP applied on day 2 (blocks the
#    receptors: k1 -> 0) prevents the switch.
# B: steady states of E against k0 (bifurcation diagram): a fold at k0 = 0.38 turns System 2 on; the
#    return fold lies at k0 < 0, so the switch cannot be reversed by removing the stimulus (hysteresis).
import matplotlib.pyplot as plt
import numpy as np

k2, Q0, a = 1.0, 1.0, 5.0
dt = 0.005
t = np.arange(0, 16, dt)


def run(k1_of_t):
    E = np.zeros_like(t)
    Q = np.zeros_like(t)
    S = np.ones_like(t)
    E[0], Q[0] = 0.05, Q0
    for i in range(len(t) - 1):
        k0 = min(0.6, 0.05 + 0.07 * t[i])
        k1 = k1_of_t(t[i])
        E[i + 1] = E[i] + dt * (k0 + k1 * E[i] ** 4 / (1 + E[i] ** 4) - k2 * E[i])
        S[i + 1] = S[i] - dt * (0.02 + 0.12 * E[i]) * S[i]
        target = S[i] * (Q0 + a * E[i] ** 2 / (1 + E[i] ** 2))
        Q[i + 1] = Q[i] + dt * (target - Q[i]) / 1.5
    return E, Q


clim = run(lambda s: 2.0)
non = run(lambda s: 0.0)
mcp = run(lambda s: 2.0 if s < 2 else 0.0)

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.4, 1]})
ax.plot(t, clim[0], color="#d9822b", lw=2.2, label="ethylene, climacteric")
ax.plot(t, clim[1], color="#2f6fb5", lw=2.2, label="respiration, climacteric")
ax.plot(t, non[0], color="#d9822b", lw=1.4, ls=":", label="ethylene, non-climacteric")
ax.plot(t, non[1], color="#2f6fb5", lw=1.4, ls=":", label="respiration, non-climacteric")
ax.plot(t, mcp[1], color="#7a7a7a", lw=1.4, ls="--", label="respiration, 1-MCP on day 2")
ax.set_xlabel("Days after harvest / d")
ax.set_ylabel("Relative level")
ax.set_xlim(0, 16)
ax.set_ylim(0, 3.6)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)

E = np.linspace(0, 2.6, 2000)
k0 = k2 * E - 2 * E**4 / (1 + E**4)
slope = np.gradient(k0, E)
stable = slope > 0
for mask, ls in ((stable, "-"), (~stable, "--")):
    kk = np.where(mask, k0, np.nan)
    bx.plot(kk, np.where(mask, E, np.nan), color="#d9822b", lw=2.2, ls=ls)
bx.axvline(0.384, color="0.5", lw=0.8, ls=":")
bx.text(0.39, 0.15, "fold\nk0 = 0.38", fontsize=8, color="0.35")
bx.annotate("", (0.384, 2.05), (0.384, 0.6), arrowprops=dict(arrowstyle="->", color="0.3", lw=1))
bx.annotate("", (0.02, 1.75), (0.32, 1.95), arrowprops=dict(arrowstyle="->", color="0.3", lw=1))
bx.text(0.03, 2.25, "stays on when k0 falls", fontsize=8, color="0.35")
bx.set_xlim(0, 0.8)
bx.set_ylim(0, 2.6)
bx.set_xlabel("Basal (System 1) production k0")
bx.set_ylabel("Steady-state ethylene E")
bx.spines[["top", "right"]].set_visible(False)
for a_, letter in zip((ax, bx), "AB"):
    a_.text(-0.12, 1.03, letter, transform=a_.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
