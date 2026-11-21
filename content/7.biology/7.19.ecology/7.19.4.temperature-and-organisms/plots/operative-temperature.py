# Operative temperature and behavioral thermoregulation of a small lizard (simplified heat-budget model,
# illustrative parameters).
# Air temperature Ta(t) = 25 - 7 cos(2 pi (t - 3) / 24) C (minimum 18 C at 03:00, maximum 32 C at 15:00);
# solar irradiance S(t) = 1000 sin(pi (t - 6) / 12) W m^-2 between 06:00 and 18:00.
# Operative temperature in the sun on open ground: Te = Ta + 0.008 S + a f S / (h_r + h_c), with absorptivity
# a = 0.9, fraction of the body surface facing direct sun f = 0.3, linearized radiative coefficient
# h_r = 4 eps sigma Ta^3 and convective coefficient h_c = 3.9 sqrt(u / D) (u = 1 m s^-1, D = 0.02 m);
# the term 0.008 S approximates the warming of air near sunlit ground. In shade Te = Ta.
# A: Te in sun and shade and the body temperature of a lizard (time constant tau = 10 min) that shuttles
#    between them, moving into the sun when Tb < 33 C and into shade when Tb > 36 C, active 07:00-19:00 and
#    in a burrow at 22 C otherwise; dTb/dt = (Te - Tb) / tau.
# B: heating in full sun at noon from 22 C for animals with time constants scaling as tau ~ m^0.5
#    (10 g: 10 min; 1 kg: 1.7 h; 100 kg: 17 h).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
sigma, eps = 5.67e-8, 0.95
t = np.linspace(0, 24, 24 * 60 + 1)
Ta = 25 - 7 * np.cos(2 * np.pi * (t - 3) / 24)
S = np.clip(1000 * np.sin(np.pi * (t - 6) / 12), 0, None)
hr = 4 * eps * sigma * (Ta + 273.15) ** 3
hc = 3.9 * np.sqrt(1.0 / 0.02)
Te_sun = Ta + 0.008 * S + 0.9 * 0.3 * S / (hr + hc)
Te_shade = Ta

tau = 10.0 / 60.0
Tb = np.empty_like(t)
Tb[0] = 22.0
in_sun = True
for i in range(1, t.size):
    dt = t[i] - t[i - 1]
    if 7 <= t[i] <= 19:
        if Tb[i - 1] < 33:
            in_sun = True
        elif Tb[i - 1] > 36:
            in_sun = False
        Te = Te_sun[i] if in_sun else Te_shade[i]
    else:
        Te = 22.0
    Tb[i] = Tb[i - 1] + dt * (Te - Tb[i - 1]) / tau

fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3), gridspec_kw={"width_ratios": [1.35, 1]})
a.axhspan(33, 36, color=P.light("positive"), lw=0)
a.text(0.5, 34.5, "preferred range", fontsize=7.5, color=P.edge("positive"), va="center")
a.plot(t, Te_sun, color=P.edge("negative"), lw=1.8, label="operative temperature, sun")
a.plot(t, Te_shade, color=P.edge("dna"), lw=1.8, label="operative temperature, shade (= air)")
a.plot(t, Tb, color=P.ink(), lw=1.2, label="body temperature, shuttling lizard")
a.set_xlim(0, 24)
a.set_xticks([0, 6, 12, 18, 24])
a.set_xlabel("Time of day / h")
a.set_ylabel("Temperature / °C")
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_ylim(15, 58)
a.set_title("A  Thermal environment and behavior", loc="left", fontweight="bold")

tt = np.linspace(0, 8, 801)
Te_noon = Te_sun[t.searchsorted(13.0)]
for tau_h, tok, name in ((10 / 60, "rna", "10 g"), (1.7, "atp", "1 kg"), (17.0, "metabolite", "100 kg")):
    b.plot(tt, Te_noon - (Te_noon - 22) * np.exp(-tt / tau_h), color=P.edge(tok), lw=2,
           label="%s, tau = %s" % (name, ("%.0f min" % (tau_h * 60)) if tau_h < 1 else ("%.1f h" % tau_h)))
b.axhline(Te_noon, color=P.muted(), lw=0.8, ls="--")
b.text(8, Te_noon + 0.6, "Te = %.0f °C" % Te_noon, ha="right", fontsize=7.5, color=P.muted())
b.set_xlim(0, 8)
b.set_ylim(20, Te_noon + 4)
b.set_xlabel("Time in the sun / h")
b.set_ylabel("Body temperature / °C")
b.legend(frameon=False, fontsize=7.5, loc="lower right")
b.set_title("B  Thermal inertia", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
