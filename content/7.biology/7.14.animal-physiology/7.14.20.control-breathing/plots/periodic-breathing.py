"""Periodic (Cheyne-Stokes) breathing as an instability of a delayed negative-feedback loop.

Plant: the lung CO2 store, V_L dP/dt = 863 VCO2 - VA P (V_L = 12 L: the effective CO2 store of lung gas, blood and rapidly exchanging tissue, VCO2 = 0.2 L/min, P in mmHg,
time in min), VA = 0.7 VE. Controller: VE(t) = G max(0, P(t - tau) - B), B = 37.5 mmHg, i.e. the chemoreceptors
see the alveolar PCO2 after the lung-to-chemoreceptor circulation delay tau. A brief sigh (VE doubled for 5 s)
perturbs the steady state at t = 20 s. With G = 2.4 L/(min mmHg) the loop is stable at the normal delay
(tau = 8 s) and oscillates with apnoeas when the delay is long (heart failure, tau = 30 s); at altitude the
gain is higher (G = 5) and even a moderate delay (tau = 12 s) destabilises the loop.
B: peak-to-peak amplitude of VE (late in the run) over the gain-delay plane; the boundary is where the
loop gain is large enough that the response to a disturbance returns in phase after the delay.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
VL, VCO2, B = 12.0, 0.2, 37.5


def simulate(G, tau_s, T_s=400.0, dt_s=0.05):
    n = int(T_s / dt_s)
    d = int(tau_s / dt_s)
    p0 = B + 863 * VCO2 / (0.7 * G * 1.0)  # rough start, refined by the steady state below
    # steady state: 863 VCO2 = 0.7 G (p - B) p
    a = 0.7 * G
    p0 = (a * B + np.sqrt((a * B) ** 2 + 4 * a * 863 * VCO2)) / (2 * a)
    p = np.full(n, p0)
    ve = np.zeros(n)
    dt = dt_s / 60
    for i in range(1, n):
        past = p[i - 1 - d] if i - 1 - d >= 0 else p0
        v = G * max(0.0, past - B)
        if 20 <= i * dt_s < 25:
            v *= 2
        ve[i] = v
        p[i] = p[i - 1] + dt * (863 * VCO2 - 0.7 * v * p[i - 1]) / VL
    return np.arange(n) * dt_s, ve, p


fig, axs = plt.subplots(1, 2, figsize=(13, 4.8), gridspec_kw={"width_ratios": [1.7, 1]})
ax = axs[0]
cases = [(2.4, 8, P.ink(), "normal: G = 2.4, delay 8 s", 0), (2.4, 30, P.edge("blood"), "heart failure: delay 30 s", 25),
         (5.0, 12, P.edge("dna"), "altitude: G = 5, delay 12 s", 50)]
for G, tau, c, lab, off in cases:
    t, ve, p = simulate(G, tau)
    ax.plot(t, ve + off, color=c, lw=1.6, label=lab)
    ax.axhline(off, color=P.muted(), lw=0.6, ls=":")
ax.set_xlabel("Time / s")
ax.set_ylabel("Ventilation / (L min$^{-1}$), traces offset")
ax.set_xlim(0, 400)
ax.legend(frameon=False, fontsize=8, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.32))
ax.set_title("A  Sigh at 20 s", loc="left", fontsize=10)

ax = axs[1]
Gs = np.linspace(0.5, 6, 23)
taus = np.linspace(2, 40, 20)
amp = np.zeros((len(taus), len(Gs)))
for i, tau in enumerate(taus):
    for j, G in enumerate(Gs):
        t, ve, p = simulate(G, tau, T_s=500, dt_s=0.1)
        late = ve[t > 350]
        amp[i, j] = late.max() - late.min()
im = ax.pcolormesh(Gs, taus, amp, shading="auto", cmap="magma")
fig.colorbar(im, ax=ax, label="Late VE oscillation, peak to peak / (L min$^{-1}$)")
for G, tau, c, lab, off in cases:
    ax.plot(G, tau, "o", mfc="none", mec="white", mew=1.6, ms=8)
ax.set_xlabel("Controller gain $G$ / (L min$^{-1}$ mmHg$^{-1}$)")
ax.set_ylabel("Circulation delay / s")
ax.set_title("B  Stable and unstable regions", loc="left", fontsize=10)
fig.tight_layout()
