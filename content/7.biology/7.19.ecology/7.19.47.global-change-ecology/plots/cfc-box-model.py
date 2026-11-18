# One-box models of the two main chlorofluorocarbons, dB/dt = E(t) - B/tau, with lifetimes of 52 years
# (CFC-11) and 102 years (CFC-12). Stylized emissions: growth from 1950, a plateau in the 1970s-1980s,
# phase-out after the Montreal Protocol (1987) to small residual emissions from banks (declining with
# a time constant of 30 years), and a counterfactual
# "world avoided" in which emissions kept growing by 3% per year.
# A: emissions. B: tropospheric mixing ratios (1 ppt = 24.3 kt CFC-11, 21.4 kt CFC-12).
# C: equivalent chlorine 3 x CFC-11 + 2 x CFC-12 (chlorine atoms) relative to its 1980 value.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
yr = np.arange(1940, 2151)

def emissions(peak, residual, avoided=False):
    e = np.where(yr < 1950, 0.0, peak / (1 + np.exp(-(yr - 1965) / 4.0)))
    if avoided:
        return np.where(yr <= 1987, e, e[yr == 1987][0] * 1.03 ** (yr - 1987))
    decline = np.clip((yr - 1988) / 8.0, 0, 1)
    resid = residual * np.exp(-np.clip(yr - 1996, 0, None) / 30.0)   # leakage from banks declines
    return np.where(yr <= 1988, e, e * (1 - decline) + resid * decline)

def burden(E, tau):
    B = np.zeros(yr.size)
    for i in range(1, yr.size):
        B[i] = B[i - 1] + E[i - 1] - B[i - 1] / tau
    return B

fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.4, 4.1))
gases = [("CFC-11", 340, 60, 52, 24.3, "dna"), ("CFC-12", 430, 25, 102, 21.4, "negative")]
cl = {}
for name, pk, res, tau, kt, tok in gases:
    for avoided, ls in ((False, "-"), (True, ":")):
        E = emissions(pk, res, avoided)
        B = burden(E, tau) / kt
        lab = name if not avoided else None
        a.plot(yr, E, color=P.fill(tok), lw=1.8, ls=ls, label=lab)
        b.plot(yr, B, color=P.fill(tok), lw=1.8, ls=ls, label=lab)
        cl[(name, avoided)] = B
a.plot([], [], color=P.muted(), ls=":", label="world avoided")
a.axvline(1987, color=P.muted(), lw=0.8, ls="--")
a.text(1991, 760, "Montreal\nProtocol", fontsize=7.5, color=P.muted(), va="top")
a.set_ylim(0, 1200)
a.set_ylabel("Emissions / kt yr$^{-1}$")
a.legend(frameon=False, fontsize=7.5, loc="center right")
a.set_title("A  Emissions", loc="left", fontweight="bold")
b.set_ylim(0, 1500)
b.set_ylabel("Mixing ratio / ppt")
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_title("B  Atmospheric abundance", loc="left", fontweight="bold")
for avoided, ls in ((False, "-"), (True, ":")):
    eq = 3 * cl[("CFC-11", avoided)] + 2 * cl[("CFC-12", avoided)]
    rel = eq / eq[yr == 1980][0]
    c.plot(yr, rel, color=P.ink(), lw=2, ls=ls, label="world avoided" if avoided else "with the Protocol")
    if not avoided:
        peak = yr[np.argmax(rel)]
        back = yr[(yr > peak) & (rel <= 1.0)]
        c.plot([peak], [rel.max()], "o", color=P.ink(), ms=4)
        c.text(peak + 3, rel.max() + 0.06, f"peak {peak}", fontsize=7.5)
        if back.size:
            c.plot([back[0]], [1.0], "o", color=P.edge("negative"), ms=4)
            c.text(back[0] - 3, 0.82, f"back to 1980 level: {back[0]}", fontsize=7.5, ha="right",
                   color=P.edge("negative"))
c.axhline(1, color=P.muted(), lw=0.8, ls="--")
c.set_ylim(0, 4)
c.set_ylabel("Equivalent chlorine / 1980 value")
c.legend(frameon=False, fontsize=7.5, loc="upper left")
c.set_title("C  Chlorine from the two CFCs", loc="left", fontweight="bold")
for ax in (a, b, c):
    ax.set_xlim(1940, 2150)
    ax.set_xlabel("Year")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
