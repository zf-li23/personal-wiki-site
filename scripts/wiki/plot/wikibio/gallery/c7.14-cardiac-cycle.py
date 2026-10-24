# The cardiac cycle from a lumped model of the left heart (time-varying elastance ventricle and atrium,
# valves, three-element Windkessel aorta): a Wiggers diagram (pressures, ventricular volume, ECG and heart
# sounds on one time axis, with valve events and phases) and the pressure-volume loop.
import numpy as np

import wikibio as bio
from wikibio import physiology as phys
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 13.4)

r = phys.cardiac_cycle(hr=75)
t, T = r["t"], r["T"]
mc, ao, ac, mo = r["mitral_close"], r["aortic_open"], r["aortic_close"], r["mitral_open"]
tok_ao, tok_lv, tok_la = "blood", "protein", "dna"

# ---- A: Wiggers diagram -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 13.3))
X0, W = 2.2, 12.6
xt = [(v, "") for v in (0, 0.2, 0.4, 0.6, 0.8)]
pp = quant.Plot(ax, (X0, 7.0, W, 4.6), (0, T), (0, 140), ylabel="Pressure / mmHg", yticks=[0, 40, 80, 120], xticks=xt)
pv = quant.Plot(ax, (X0, 4.25, W, 2.2), (0, T), (40, 140), ylabel="LV volume / mL", yticks=[50, 90, 130], xticks=xt,
                ylabel_offset=0.85)
pe = quant.Plot(ax, (X0, 2.15, W, 1.5), (0, T), (-0.4, 1.2), ylabel="ECG", xticks=xt, frame=None, ylabel_offset=0.35)
ps = quant.Plot(ax, (X0, 0.95, W, 0.75), (0, T), (-1, 1), xlabel="$t$ / s", ylabel="Sounds",
                xticks=[0, 0.2, 0.4, 0.6, 0.8], frame=None, ylabel_offset=0.35)
ax.plot([X0, X0 + W], [0.95, 0.95], color=P.muted(), lw=0.8, zorder=6)
# phases
phases = [(0, mc, "Atrial\nsystole", "neutral"), (mc, ao, "IVC", "highlight"), (ao, ac, "Ejection", "blood"),
          (ac, mo, "IVR", "highlight"), (mo, T, "Filling", "dna")]
for a, b, text, tok in phases:
    for p in (pp, pv, pe, ps):
        p.span(a, b, tok, strength=0.86)
    bio.label(ax, ((pp.X(a) + pp.X(b)) / 2, 12.35), text, size="tiny", va="center")
# valve events
events = [(mc, "MV closes"), (ao, "AV opens"), (ac, "AV closes"), (mo, "MV opens")]
for k, (te, text) in enumerate(events):
    x = float(pp.X(te))
    ax.plot([x, x], [0.95, 11.6], color=P.muted(), lw=0.7, ls=(0, (2, 2)), zorder=5)
pp.line(t, r["p_ao"], tok_ao, lw=2.0, text="Aorta", at=0.85, dx=0.0, dy=0.25, ha="center", va="bottom", size="small")
pp.line(t, r["p_lv"], tok_lv, lw=2.0, text="Left ventricle", at=0.37, dx=-0.15, dy=0.0, ha="right", size="small")
pp.line(t, r["p_la"], tok_la, lw=2.0, text="Left atrium", at=0.93, dx=0.0, dy=0.18, ha="right", va="bottom", size="small")
pv.line(t, r["v_lv"], tok_lv, lw=2.0)
edv, esv = r["v_lv"].max(), r["v_lv"].min()
pv.text(0.02, edv + 3, f"EDV {edv:.0f} mL", ha="left", va="bottom")
pv.text(ac - 0.01, esv + 4, f"ESV {esv:.0f} mL", ha="right", va="bottom")
pv.text(ao + 0.02, 75, f"stroke volume {edv - esv:.0f} mL", ha="left", va="center", color=P.muted())
te = np.linspace(0, T, 1600)
pe.line(te, phys.ecg(te, r["t_qrs"], T), "ink", lw=1.2)
for xw, text in ((r["t_qrs"] - 0.08, "P"), (r["t_qrs"] + 0.015, "QRS"), (r["t_qrs"] + 0.30, "T")):
    pe.text(xw + 0.012, 0.8 if text != "QRS" else 1.12, text, ha="left", va="bottom" if text == "QRS" else "center",
            size="tiny")
for te0, name, amp in ((mc, "S1", 0.9), (ac, "S2", 0.7)):
    ts = np.linspace(te0, te0 + 0.06, 200)
    burst = amp * np.sin(2 * np.pi * 60 * (ts - te0)) * np.exp(-((ts - te0 - 0.02) / 0.015) ** 2)
    ps.line(ts, burst, "ink", lw=0.9)
    ps.text(te0 + 0.065, 0.0, name, ha="left", va="center", size="tiny")
bio.label(ax, (21.4, 0.25), "IVC / IVR: isovolumic contraction / relaxation\nMV: mitral valve;  AV: aortic valve", size="tiny",
          color=P.muted(), va="bottom")

# ---- B: pressure-volume loop ---------------------------------------------------------------------------
X1, W1 = 18.4, 6.0
pl = quant.Plot(ax, (X1, 4.6, W1, 7.0), (0, 150), (0, 150), xlabel="LV volume / mL", ylabel="LV pressure / mmHg",
                xticks=[0, 50, 100, 150], yticks=[0, 50, 100, 150], grid=True)
bio.panel(ax, "B", (X1 - 1.6, 13.3))
V = np.linspace(10, 150, 100)
pl.line(V, 3.0 * (V - 10), "muted", lw=1.0, dashed=True)
pl.text(62, 140, "ESPVR", ha="left", va="center", color=P.muted())
pl.line(V, 0.07 * (V - 10), "muted", lw=1.0, dashed=True)
pl.text(148, 1.2, "EDPVR", ha="right", va="bottom", color=P.muted())
pl.line(r["v_lv"], r["p_lv"], tok_lv, lw=2.2)
for k, (te0, text) in enumerate(events):
    i = int(np.argmin(np.abs(t - te0)))
    pl.points([r["v_lv"][i]], [r["p_lv"][i]], "ink", r=0.09, zorder=14)
    dx, dy, ha = [(3, 12, "left"), (3, 3, "left"), (-3, 4, "right"), (-3, -5, "right")][k]
    pl.text(r["v_lv"][i] + dx, r["p_lv"][i] + dy, text, ha=ha, va="center")
for (vx, py, text) in ((88, 18, "filling"), (131, 48, "IVC"), (90, 133, "ejection"), (45, 50, "IVR")):
    pl.text(vx, py, text, ha="center", va="center", token=tok_lv, italic=True)
pl.text(88, 70, f"SV {edv - esv:.0f} mL\nEF {100 * (edv - esv) / edv:.0f} %", ha="center", va="center", size="small")
bio.icon(ax, "servier/heart-interior", at=(X1 + W1 / 2, 2.35), height=2.3)
