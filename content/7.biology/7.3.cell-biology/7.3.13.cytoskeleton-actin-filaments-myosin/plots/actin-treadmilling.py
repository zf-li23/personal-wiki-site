"""Critical concentrations at the two ends of an actin filament, and treadmilling.

Rate constants (Pollard 1986, Mg-ATP-actin; the pointed end of a filament at steady state is taken to
carry ADP-actin): barbed (plus) end k_on = 11.6 per uM per s, k_off = 1.4 per s (C_c+ = 0.12 uM);
pointed (minus) end k_on = 1.3 per uM per s, k_off(ADP) = 0.27 per s (C_c- = 0.21 uM).
A: net elongation rate J = k_on c - k_off at each end and of the whole filament; between the two critical
concentrations (shaded) the plus end grows while the minus end shrinks. At c_tm = 0.13 uM the two
rates cancel: steady-state treadmilling with a flux of about 0.1 subunits per second.
B: a stochastic simulation (Gillespie) of one filament at c_tm: positions of the plus and minus ends over
an hour, and marked subunits (speckles: three present at the start, two added later), which stay where they were added until they reach the
minus end and leave. The filament moves while its subunits do not.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
kpb, kmb, kpp, kmp = 11.6, 1.4, 1.3, 0.27
ctm = (kmb + kmp) / (kpb + kpp)

fig, ax = bio.canvas(22.0, 8.0)
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.8, 1.3, 8.4, 5.8))
c = np.linspace(0, 0.4, 200)
pa.axhline(0, color=P.muted(), lw=0.7)
pa.plot(c, kpb * c - kmb, color=quant.line_color("actin"), lw=1.8, label="plus (barbed) end")
pa.plot(c, kpp * c - kmp, color=quant.line_color("channel"), lw=1.8, label="minus (pointed) end")
pa.plot(c, (kpb + kpp) * c - kmb - kmp, color=quant.line_color("ink"), lw=1.2, ls=(0, (4, 2)), label="whole filament")
pa.axvspan(kmb / kpb, kmp / kpp, color=P.fill("highlight"), alpha=0.35, lw=0)
pa.plot([ctm], [0], "o", color=quant.line_color("ink"), ms=5)
pa.annotate("treadmilling\n$c_{\\mathrm{tm}}$", (ctm, 0), (0.24, -1.0), fontsize=bio.core.FONT["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pa.set_xlim(0, 0.4)
pa.set_ylim(-1.6, 3.4)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "free ATP-actin / µM", "net rate J / (subunits s⁻¹)")
charts.title(pa, "Two ends, two critical concentrations")

bio.panel(ax, "B", (11.6, 7.8))
pb = charts.axes_at(ax, (13.4, 1.3, 7.8, 5.8))
rng = np.random.default_rng(5)
plus, minus = 150, 0  # positions in subunits (2.7 nm)
rates = np.array([kpb * ctm, kmb, kpp * ctm, kmp])
t, T = 0.0, 3600.0
ts, ps, ms = [0.0], [plus], [minus]
marks = {40: [0.0, None], 90: [0.0, None], 140: [0.0, None]}
next_mark = [900.0, 1800.0]
while t < T:
    tot = rates.sum()
    t += rng.exponential(1 / tot)
    k = rng.choice(4, p=rates / tot)
    if k == 0:
        plus += 1
        if next_mark and t > next_mark[0]:
            marks[plus] = [t, None]
            next_mark.pop(0)
    elif k == 1:
        if plus in marks and marks[plus][1] is None:
            # a marked subunit lost again at the plus end: mark a later one instead
            next_mark.insert(0, marks.pop(plus)[0])
        plus -= 1
    elif k == 2:
        minus -= 1
    else:
        if minus in marks and marks[minus][1] is None:
            marks[minus][1] = t
        minus += 1
    ts.append(t); ps.append(plus); ms.append(minus)
ts = np.array(ts) / 60
nm = 2.7e-3
pb.fill_between(ts, np.array(ms) * nm, np.array(ps) * nm, step="post", color=P.fill("actin"), alpha=0.45, lw=0)
pb.step(ts, np.array(ps) * nm, where="post", color=quant.line_color("actin"), lw=1.2, label="plus end")
pb.step(ts, np.array(ms) * nm, where="post", color=quant.line_color("channel"), lw=1.2, label="minus end")
for pos, (t0, t1) in marks.items():
    t1 = t1 or T
    pb.plot([t0 / 60, t1 / 60], [pos * nm] * 2, color=quant.line_color("ink"), lw=1.8, zorder=5)
pb.plot([], [], color=quant.line_color("ink"), lw=1.6, label="marked subunit")
pb.set_xlim(0, 60)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "time / min", "position / µm")
charts.title(pb, "One filament at c_tm (simulation)")
