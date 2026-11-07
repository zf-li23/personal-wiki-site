# Thrombin generation as a threshold switch (minimal model, illustrative parameters).
# T: thrombin (nM); a: fraction of activated cofactors and platelets (Va, VIIIa, activated platelet surface);
# p: fraction of prothrombin remaining (plasma prothrombin P0 = 1.4 uM).
#   dT/dt = (s(t) + V a) p - k_AT T          initiation by tissue factor-VIIa, propagation by tenase/prothrombinase,
#                                             inhibition by antithrombin
#   da/dt = k_a T^2/(K^2 + T^2) (1 - a) - k_d a   thrombin activates V, VIII, XI and platelets (cooperative),
#                                                 activated protein C inactivates Va and VIIIa
#   dp/dt = -(s + V a) p / P0
# Initiation decays as TFPI shuts down the tissue factor-VIIa-Xa complex: s(t) = s0 exp(-t / tau).
# A: time courses for increasing tissue-factor stimuli s0. B: peak thrombin against s0; reducing the
# propagation rate V to 20 % (as when factor VIII or IX is missing) raises the threshold and lowers the burst.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

kAT, ka, kd, K, tau, P0 = 1.0, 2.0, 1.0, 20.0, 1.0, 1400.0


def run(s0, V=300.0, tmax=30.0):
    def f(t, y):
        th, a, p = y
        prod = (s0 * np.exp(-t / tau) + V * a) * p
        return [prod - kAT * th, ka * th ** 2 / (K ** 2 + th ** 2) * (1 - a) - kd * a, -prod / P0]

    return solve_ivp(f, (0, tmax), [0.0, 0.0, 1.0], max_step=0.02, rtol=1e-7, atol=1e-9)


fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.2))
colors = ["#9e9e9e", "#7f8fa6", "#2f6fb5", "#c0392b", "#7a1f1f"]
for s0, c in zip([1.0, 1.6, 2.5, 6.0, 20.0], colors):
    sol = run(s0)
    axa.plot(sol.t, sol.y[0], color=c, lw=2, label=f"$s_0$ = {s0:g} nM/min")
axa.set_xlim(0, 20)
axa.set_ylim(0, 160)
axa.set_xlabel("Time / min")
axa.set_ylabel("Thrombin / nM")
axa.set_title("A  Lag, then burst", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right")

s_grid = np.logspace(-0.5, 2, 60)
for V, c, lab in ((300.0, "#2f6fb5", "normal propagation"), (60.0, "#d9822b", "propagation 20 % (VIII or IX deficiency)")):
    peaks = [run(s, V=V).y[0].max() for s in s_grid]
    axb.semilogx(s_grid, peaks, color=c, lw=2, label=lab)
axb.set_xlabel("Initiation rate $s_0$ / (nM/min)")
axb.set_ylabel("Peak thrombin / nM")
axb.set_ylim(0, 160)
axb.set_title("B  Threshold", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="center right")
for ax in (axa, axb):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
