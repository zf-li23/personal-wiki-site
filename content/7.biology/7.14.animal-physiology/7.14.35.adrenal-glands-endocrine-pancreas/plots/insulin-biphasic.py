# Biphasic insulin secretion: a two-pool (readily releasable pool + provisioning) model after Grodsky (1972).
#   dL/dt = p - m c L                 L: readily releasable granules (relative units)
#   dc/dt = (sigma(G) - c) / tau_c     c: Ca2+ trigger, lags glucose by about 1.5 min
#   dp/dt = (p_inf(G) - p) / tau_p     p: provisioning (refilling) rate, rises slowly with glucose
#   S = m c L                          secretion rate
# sigma(G) is the triggering signal (K_ATP closure, Ca2+), p_inf(G) the amplifying signal; both sigmoid in G.
# Parameters are illustrative. A: glucose step 5 -> 15 mmol/L at t = 10 min. B: secretion at 60 min of
# a clamp versus glucose (static dose-response), normal and with a 1.5 mmol/L right shift (MODY 2).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def hill(G, K, n):
    G = np.maximum(G, 0.0)
    return G**n / (K**n + G**n)


def sigma(G, shift=0.0):
    return hill(G - shift, 8.5, 8)


def p_inf(G, shift=0.0, gain=1.0):
    return gain * (0.02 + 1.0 * hill(G - shift, 8.5, 5))


m = 0.3  # per min at full trigger
tau_c = 1.5  # min, lag of the Ca2+ trigger behind glucose
tau_p = 15.0  # min, provisioning time constant


def simulate(G_of_t, L0_scale=1.0, gain=1.0, shift=0.0, t_end=70.0):
    G0 = G_of_t(0.0)
    p0 = p_inf(G0, shift, gain)
    c0 = sigma(G0, shift)
    L0 = p0 / (m * c0 + 1e-12) * L0_scale  # resting pool (smaller in early T2D)

    def rhs(t, y):
        L, p, c = y
        G = G_of_t(t)
        return [p - m * c * L, (p_inf(G, shift, gain) - p) / tau_p, (sigma(G, shift) - c) / tau_c]

    t = np.linspace(0, t_end, 2000)
    sol = solve_ivp(rhs, (0, t_end), [L0, p0, c0], t_eval=t, max_step=0.1)
    L, p, c = sol.y
    return t, m * c * L


step = lambda t: 5.0 if t < 10.0 else 15.0

fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 4.4))
for kw, col, ls, lab in (
    (dict(), "#2c6fbb", "-", "normal"),
    (dict(L0_scale=0.2), "#c0392b", "-", "releasable pool 20% (early T2D)"),
    (dict(L0_scale=0.2, gain=0.5), "0.45", "--", "pool 20% and refilling 50%"),
):
    t, S = simulate(step, **kw)
    axa.plot(t, S, color=col, ls=ls, lw=2, label=lab)
axa.axvline(10, color="0.6", lw=0.8, ls=":")
axa.text(20, 3.3, "glucose 5 -> 15 mmol/L at 10 min", fontsize=8.5, color="0.35")
axa.text(14.5, 2.6, "first phase", fontsize=8.5, color="0.3")
axa.text(45, 1.1, "second phase", fontsize=8.5, color="0.3")
axa.set_xlabel("Time / min")
axa.set_ylabel("Insulin secretion rate / relative units")
axa.set_title("A  Two pools give two phases", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.85))

Gs = np.linspace(2, 25, 60)
for shift, col, ls, lab in ((0.0, "#2c6fbb", "-", "normal"), (1.5, "#2c6fbb", "--", "glucokinase +/- (MODY 2)")):
    out = []
    for g in Gs:
        t, S = simulate(lambda x, g=g: g, shift=shift, t_end=60.0)
        out.append(S[-1])
    axb.plot(Gs, out, color=col, ls=ls, lw=2, label=lab)
axb.axvspan(3.9, 5.6, color="0.85", alpha=0.6, lw=0)
axb.text(4.75, 0.3, "fasting\nrange", ha="center", fontsize=8, color="0.35")
axb.set_xlabel("Glucose / (mmol/L)")
axb.set_ylabel("Secretion at 60 min / relative units")
axb.set_title("B  Static dose-response", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left")
fig.tight_layout()
