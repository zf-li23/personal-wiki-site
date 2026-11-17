# Oxygen methods for aquatic primary production.
# A: light-dark bottle example (Example 42.3.1): c_I = 8.20, c_D = 7.40, c_L = 9.50 mg O2 L^-1 after 12 h.
# B: diel oxygen curve in a simulated stream: dc/dt = GPP(t) - R + K (c_sat - c), GPP a half-sine over
#    06:00-18:00 with a daily total of 4.8 mg O2 L^-1, R = 0.25 mg L^-1 h^-1, K = 0.5 h^-1, c_sat = 9 mg L^-1.
#    The method: corrected rate = dc/dt - K (c_sat - c); night mean = -R; GPP = corrected rate + R.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio

P = bio.P
fig = plt.figure(figsize=(11.0, 4.8))
gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.5], height_ratios=[1, 1])
a = fig.add_subplot(gs[:, 0])
cI, cD, cL = 8.20, 7.40, 9.50
bars = [("initial", cI, "neutral"), ("dark", cD, "animal"), ("light", cL, "plant")]
for i, (n, v, tok) in enumerate(bars):
    a.bar(i, v, color=P.fill(tok), edgecolor=P.edge(tok), width=0.6)
    a.text(i, v + 0.05, f"{v:.2f}", ha="center", va="bottom", fontsize=8, color=P.ink())
a.set_xticks(range(3), [b[0] + "\nbottle" for b in bars])
a.set_ylim(6.5, 10.3)
a.set_ylabel("Dissolved O₂ / mg L⁻¹")


def brace(x, y0, y1, text, tok, left=False):
    a.annotate("", (x, y1), (x, y0), arrowprops=dict(arrowstyle="<->", color=P.edge(tok), lw=1.3))
    a.text(x - 0.08 if left else x + 0.08, (y0 + y1) / 2, text, fontsize=7.5, va="center",
           ha="right" if left else "left", color=P.edge(tok))


brace(0.45, cD, cI, f"R = {cI - cD:.2f}", "animal")
brace(1.6, cI, cL, f"NP = {cL - cI:.2f}", "plant", left=True)
brace(2.4, cD, cL, f"GP = {cL - cD:.2f}", "positive")
a.plot([-0.3, 2.35], [cI, cI], color=P.muted(), lw=0.7, ls=":")
a.plot([0.7, 2.35], [cD, cD], color=P.muted(), lw=0.7, ls=":")
a.set_xlim(-0.5, 3.0)
a.set_title("A  Light–dark bottles (12 h)", loc="left", fontweight="bold")

# diel curve
Gday = 4.8
Gmax = Gday * np.pi / 24.0
R, K, cs = 0.25, 0.5, 9.0


def gpp(t):
    h = t % 24
    return np.where((h > 6) & (h < 18), Gmax * np.sin(np.pi * (h - 6) / 12), 0.0)


def rhs(t, c):
    return gpp(t) - R + K * (cs - c)


t = np.linspace(0, 72, 72 * 60 + 1)
c = solve_ivp(rhs, (0, 72), [8.5], t_eval=t, max_step=0.05).y[0]
sel = t >= 48
tt, cc = t[sel] - 48, c[sel]
dcdt = np.gradient(cc, tt)
corr = dcdt - K * (cs - cc)
night = (tt < 5) | (tt > 19)
Rest = -corr[night].mean()
gest = np.trapezoid(np.clip(corr + Rest, 0, None)[(tt > 6) & (tt < 18)], tt[(tt > 6) & (tt < 18)])
b1 = fig.add_subplot(gs[0, 1])
b1.plot(tt, cc, color=P.ink(), lw=2)
b1.axhline(cs, color=P.edge("dna"), lw=0.8, ls="--")
b1.text(0.3, cs + 0.03, "saturation", fontsize=7.5, color=P.edge("dna"), va="bottom")
b1.axvspan(0, 6, color=P.fill("neutral"), alpha=0.4, lw=0)
b1.axvspan(18, 24, color=P.fill("neutral"), alpha=0.4, lw=0)
b1.set_ylabel("O₂ / mg L⁻¹")
b1.set_xlim(0, 24)
b1.tick_params(labelbottom=False)
b1.set_title("B  Diel oxygen curve", loc="left", fontweight="bold")
b2 = fig.add_subplot(gs[1, 1], sharex=b1)
b2.axhline(0, color=P.muted(), lw=0.7)
b2.plot(tt, corr, color=P.ink(), lw=2, label="rate corrected for reaeration")
b2.axhline(-Rest, color=P.edge("animal"), lw=1.2, ls="--", label=f"respiration (from night) = {Rest:.2f} mg L⁻¹ h⁻¹")
b2.fill_between(tt, -Rest, corr, where=(corr > -Rest + 1e-6), color=P.fill("plant"), alpha=0.6, lw=0,
                label=f"GPP, integrated = {gest:.1f} mg L⁻¹ d⁻¹")
b2.axvspan(0, 6, color=P.fill("neutral"), alpha=0.4, lw=0)
b2.axvspan(18, 24, color=P.fill("neutral"), alpha=0.4, lw=0)
b2.set_xlabel("Time of day / h")
b2.set_ylabel("mg O₂ L⁻¹ h⁻¹")
b2.set_xticks(range(0, 25, 6))
b2.legend(frameon=False, fontsize=7, loc="upper left")
for ax in (a, b1, b2):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
