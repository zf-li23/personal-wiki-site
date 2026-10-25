# A minimal model of the SOS response (Eq. 8.1). LexA level L (units of its basal level) is made from an
# autorepressed promoter and lost by dilution and by RecA*-stimulated cleavage; RecA* activity R(t)
# appears at t = 0 and decays as the damage is repaired. Each SOS gene's promoter activity is
# 1/(1 + L/K_i). B: fold induction a/a_basal; C: (a - a_basal)/(a_max - a_basal). Illustrative parameters.
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26, 7.6)

gamma, kc, tauR, tauU, KL = 0.03, 0.6, 40.0, 5.0, 0.3
beta = gamma * 1.0 * (1 + 1.0 / KL)          # basal steady state L = 1
t = np.linspace(-20, 180, 2001)


def rhs(tt, y):
    R = (1 - np.exp(-tt / tauU)) * np.exp(-tt / tauR) if tt >= 0 else 0.0
    return np.array([beta / (1 + y[0] / KL) - (gamma + kc * R) * y[0]])


L = quant.odeint_rk4(rhs, np.array([1.0]), t)[:, 0]
tp = np.clip(t, 0, None)
R = np.where(t >= 0, (1 - np.exp(-tp / tauU)) * np.exp(-tp / tauR), 0.0)
R = R / R.max()

a = C.axes_at(ax, (1.6, 1.4, 7.0, 5.2))
a.plot(t, L, color=P.ink(), lw=1.8, label="LexA, L")
a.plot(t, R, color=P.muted(), lw=1.3, ls="--", label="RecA* activity, R (scaled)")
a.set_xlim(t[0], t[-1])
a.set_ylim(0, 1.1)
C.style_axes(a, "Time after damage / min", "Relative level")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="upper center", labelcolor=P.ink())
bio.panel(ax, "A", (0.4, 7.2))
bio.label(ax, (1.0, 7.2), "Repressor and signal", size="normal", bold=True, ha="left")

genes = [("uvrA (K = 0.5)", 0.5, "positive", "-"), ("recA (K = 0.2)", 0.2, "enzyme", "--"),
         ("sulA (K = 0.06)", 0.06, "protein", "-."), ("umuDC (K = 0.02)", 0.02, "negative", ":")]
b = C.axes_at(ax, (10.8, 1.4, 6.0, 5.2))
c = C.axes_at(ax, (19.4, 1.4, 6.0, 5.2))
for name, K, tok, ls in genes:
    act = 1 / (1 + L / K)
    a0 = 1 / (1 + 1 / K)
    b.plot(t, act / a0, color=C.line(tok), lw=1.8, ls=ls, label=name)
    c.plot(t, (act - a0) / (act.max() - a0), color=C.line(tok), lw=1.8, ls=ls, label=name)
b.set_yscale("log")
b.set_yticks([1, 2, 5], ["1", "2", "5"])
b.minorticks_off()
b.set_ylim(0.9, 7)
c.set_ylim(-0.02, 1.08)
for q in (b, c):
    q.set_xlim(t[0], t[-1])
C.style_axes(b, "Time after damage / min", "Fold induction")
C.style_axes(c, "Time after damage / min", "Induction / maximum")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="upper right", labelcolor=P.ink())
bio.panel(ax, "B", (9.6, 7.2))
bio.label(ax, (10.2, 7.2), "Fold induction", size="normal", bold=True, ha="left")
bio.panel(ax, "C", (18.2, 7.2))
bio.label(ax, (18.8, 7.2), "Normalized time course", size="normal", bold=True, ha="left")
