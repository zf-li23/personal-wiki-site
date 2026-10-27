"""A minimal model of the spindle assembly checkpoint (after the Mad2 template model; De Antoni et al. 2005).

I is the fraction of Cdc20 sequestered in the mitotic checkpoint complex (MCC) and U the number of unattached
kinetochores. Each unattached kinetochore acts as a catalytic template (Mad1-C-Mad2 converting O-Mad2 to
C-Mad2) at rate k_u; MCC can also promote its own formation in solution (k_amp); MCC is disassembled by
p31comet-TRIP13 and APC/C-dependent turnover (k_off):
    dI/dt = (k_u U + k_amp I)(1 - I) - k_off I,      A = 1 - I (active APC/C-Cdc20)
    dS/dt = k_s - (k_d0 + k_d A) S                   (securin; anaphase when S < 10% of its initial level)
k_u = 5, k_amp = 0.3, k_off = 0.5 per min; k_s = 0.0125, k_d0 = 0.01, k_d = 0.25 per min (S in units of its
prometaphase level). Because k_amp < k_off, MCC cannot sustain itself once the last kinetochore attaches.
(A) A simulated prometaphase: 92 kinetochores attach at random times (exponential, mean 5 min, none later than 25 min)
except one that attaches late at 30 min. The single unattached kinetochore holds APC/C-Cdc20 activity near 10% and
securin stays high; after it attaches, MCC disassembles and securin is destroyed, and anaphase begins about
15 minutes later.
(B) Steady-state APC/C-Cdc20 activity as a function of the number of unattached kinetochores, for a strong
(k_u = 5) and a weak (k_u = 0.5 per min) template: with a strong catalytic template one kinetochore suffices to
keep the checkpoint on, which is the observed behaviour.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)

KU, KAMP, KOFF = 5.0, 0.3, 0.5
KS, KD0, KD = 0.0125, 0.01, 0.25

att = np.sort(np.append(np.minimum(rng.exponential(5.0, 91), 25.0 * rng.uniform(0.6, 1.0, 91)), 30.0))


def U(t):
    return np.sum(att > t)


def rhs(t, y, ku=KU):
    I, S = y
    A = 1 - I
    return [(ku * U(t) + KAMP * I) * (1 - I) - KOFF * I, KS - (KD0 + KD * A) * S]


I0 = 0.99
s = solve_ivp(rhs, (0, 70), [I0, 1.0], max_step=0.05)
t, (I, S) = s.t, s.y
Ut = np.array([U(x) for x in t])
ana = t[np.argmax((S < 0.1) & (t > 30))]

fig, ax = bio.canvas(24.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a = charts.axes_at(ax, (1.8, 1.5, 10.0, 6.6))
a2 = a.twinx()
a2.set_facecolor("none")
a2.step(t, Ut, where="post", color=charts.line("neutral"), lw=1.2)
a2.set_ylim(0, 100)
a2.set_ylabel("unattached kinetochores", fontsize=FT["small"], color=P.muted())
a2.tick_params(colors=P.muted(), labelsize=FT["tiny"])
for sp in a2.spines.values():
    sp.set_visible(False)
a.plot(t, 1 - I, color=charts.line("enzyme"), lw=1.8, label="APC/C–Cdc20 activity, 1 − I")
a.plot(t, S, color=charts.line("negative"), lw=1.8, label="securin (relative)")
a.axvline(30, color=P.muted(), ls=":", lw=0.9)
a.axvline(ana, color=charts.line("negative"), ls="--", lw=0.9)
a.text(30.5, 1.02, "last kinetochore\nattaches", fontsize=FT["tiny"], color=P.muted(), va="bottom")
a.text(ana + 0.5, 0.55, "anaphase", fontsize=FT["tiny"], color=charts.line("negative"))
a.set_xlim(0, 70)
a.set_ylim(0, 1.25)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "time after nuclear envelope breakdown / min", "activity, level")
a.text(12, 0.5, "grey: unattached\nkinetochores (right axis)", fontsize=FT["tiny"], color=P.muted())

bio.panel(ax, "B", (13.8, 8.8))
b = charts.axes_at(ax, (15.4, 1.5, 8.0, 6.6))
n = np.arange(0, 11)
for ku, tok, lab in ((KU, "enzyme", "strong template (k_u = 5)"), (0.5, "channel", "weak template (k_u = 0.5)")):
    act = []
    for u in n:
        f = lambda I: (ku * u + KAMP * I) * (1 - I) - KOFF * I
        act.append(1 - brentq(f, 0, 1))
    b.plot(n, act, "o-", color=charts.line(tok), lw=1.6, ms=4, label=lab)
b.set_xlim(-0.3, 10.3)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "number of unattached kinetochores U", "steady-state APC/C–Cdc20 activity")
