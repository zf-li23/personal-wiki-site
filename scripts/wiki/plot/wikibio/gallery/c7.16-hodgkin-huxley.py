# Hodgkin-Huxley action potential: axon and membrane patch (channels, pump), the equivalent circuit,
# and the simulated membrane potential, gating variables and conductances (squid axon, 6.3 C).
import numpy as np

import wikibio as bio
from wikibio import neuro, quant

P = bio.P
fig, ax = bio.canvas(24.6, 12.6)

# ---- model: a 1 ms, 20 uA/cm2 current pulse at t = 1 ms -------------------------------------
t = np.arange(0, 14.0001, 0.01)
I_on, I_off, I_amp = 1.0, 2.0, 20.0
V, m, h, n = neuro.hh_simulate(lambda tt: I_amp if I_on <= tt < I_off else 0.0, t)
V, m, h, n = V[:, 0], m[:, 0], h[:, 0], n[:, 0]
gNa = neuro.HH["gNa"] * m**3 * h
gK = neuro.HH["gK"] * n**4
ipk = int(V.argmax())

# ---- A: neuron with electrodes ----------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.5))
ys = 10.6
bio.neuron(ax, (2.6, ys), (9.0, ys), soma_r=0.38, dendrites=4, myelin=False, terminals=3)
neuro.electrode(ax, (2.75, ys + 0.12), angle=55, length=1.45, width=0.24, wire=False)
bio.label(ax, (3.75, 11.85), "Stimulate", size="small", ha="left")
neuro.electrode(ax, (6.9, ys + 0.04), angle=55, length=1.45, width=0.24, wire=False)
bio.label(ax, (7.9, 11.85), "Record $V_{\\mathrm{m}}$", size="small", ha="left")
# zoom box on the axon, joined to panel B
zx0, zx1 = 4.3, 5.3
ax.plot([zx0, zx1, zx1, zx0, zx0], [ys - 0.32, ys - 0.32, ys + 0.32, ys + 0.32, ys - 0.32], color=P.muted(), lw=0.8,
        ls=(0, (2, 1.6)), zorder=20)
for xa, xb in ((zx0, 0.75), (zx1, 9.2)):
    ax.plot([xa, xb], [ys - 0.32, 8.25], color=P.muted(), lw=0.7, ls=(0, (2, 1.6)), zorder=1)
bio.label(ax, (9.3, ys - 0.55), "Unmyelinated axon", size="small", ha="right", va="top", color=P.muted())

# ---- B: membrane patch ------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 8.25))
my = 6.25
neuro.patch(ax, 0.75, 9.2, my, depth=2.0, labels=False)
bio.label(ax, (9.05, my + 1.85), "Outside", size="small", ha="right", va="top", color=P.muted())
bio.label(ax, (9.05, my - 1.85), "Inside", size="small", ha="right", va="bottom", color=P.muted())
for x, name in ((2.0, "Nav"), (4.1, "Kv"), (6.0, "Leak")):
    bio.label(ax, (x, my + 1.62), name, size="small", va="bottom")
neuro.channel(ax, 2.0, my, "na", open=True)
neuro.flux(ax, 2.0, my, "na", "in", reach=0.7, text=False)
neuro.channel(ax, 4.1, my, "k", open=True)
neuro.flux(ax, 4.1, my, "k", "out", reach=0.7, text=False)
neuro.channel(ax, 6.0, my, "leak", open=True)
neuro.pump(ax, 7.9, my, text="Pump")
bio.label(ax, (2.35, my + 1.15), "Na⁺", size="tiny", ha="left")
bio.label(ax, (4.45, my - 1.15), "K⁺", size="tiny", ha="left")

# ---- C: equivalent circuit (Hodgkin & Huxley 1952) --------------------------------------------
bio.panel(ax, "C", (0.1, 3.95))
top, bot = 3.45, 0.55
xs = [1.4, 3.4, 5.4, 7.4]
neuro.wire(ax, (xs[0], top), (xs[-1], top))
neuro.wire(ax, (xs[0], bot), (xs[-1], bot))
bio.label(ax, (8.0, top), "Outside", size="small", ha="left", color=P.muted())
bio.label(ax, (8.0, bot), "Inside", size="small", ha="left", color=P.muted())
neuro.capacitor(ax, (xs[0], top), (xs[0], bot), text="$C_{\\mathrm{m}}$", text_side=-1)
mid = (top + bot) / 2
for x, g, E, var, sign in ((xs[1], "Na", "Na", True, -1), (xs[2], "K", "K", True, 1), (xs[3], "L", "L", False, 1)):
    neuro.resistor(ax, (x, top), (x, mid + 0.05), length=0.7, variable=var, text=f"$g_{{\\mathrm{{{g}}}}}$", text_side=-1)
    # long plate (+) towards the inside for E_Na > 0, towards the outside for E_K, E_L < 0
    a, b = ((x, mid + 0.05), (x, bot)) if sign < 0 else ((x, bot), (x, mid + 0.05))
    neuro.battery(ax, a, b, text=f"$E_{{\\mathrm{{{E}}}}}$", text_side=1 if sign < 0 else -1)
for x in xs[1:-1]:
    neuro.node(ax, (x, top))
    neuro.node(ax, (x, bot))

# ---- D-F: simulated traces on a shared time axis -------------------------------------------------
X0, W = 12.6, 8.7
xt = [0, 2, 4, 6, 8, 10, 12, 14]
pv = quant.Plot(ax, (X0, 8.75, W, 3.35), (0, 14), (-90, 60), ylabel="$V_{\\mathrm{m}}$ / mV",
                yticks=[-80, -40, 0, 40], xticks=[(v, "") for v in xt])
bio.panel(ax, "D", (X0 - 1.6, 12.5))
pv.span(I_on, I_off, "highlight", text="$I_{\\mathrm{stim}}$", strength=0.45)
pv.hline(neuro.HH["ENa"], "na", text="$E_{\\mathrm{Na}}$")
pv.hline(neuro.HH["EK"], "k", text="$E_{\\mathrm{K}}$")
pv.hline(-65, "muted", text="rest")
pv.line(t, V, "neuron", lw=2.0)
pv.text(t[ipk] + 0.35, V[ipk] - 2, f"peak {V[ipk]:+.0f} mV", ha="left", va="top")
imin = int(V.argmin())
bio.callout(ax, pv.xy(t[imin] + 0.6, V[imin] + 0.3), pv.xy(7.2, -30), "after-hyperpolarization", size="tiny")

pg = quant.Plot(ax, (X0, 4.85, W, 3.0), (0, 14), (0, 1), ylabel="Gating variable", yticks=[0, 0.5, 1],
                xticks=[(v, "") for v in xt])
bio.panel(ax, "E", (X0 - 1.6, 8.05))
pg.span(I_on, I_off, "highlight", strength=0.45)
pg.line(t, m, "na", text="$m$  Na activation", at=1.0, dx=0.15, dy=0.0)
pg.line(t, h, "receptor", text="$h$  Na inactivation", at=1.0, dx=0.15, dy=0.0)
pg.line(t, n, "k", text="$n$  K activation", at=1.0, dx=0.15, dy=0.0)

pc = quant.Plot(ax, (X0, 0.95, W, 3.0), (0, 14), (0, 40), xlabel="$t$ / ms", ylabel="$g$ / (mS cm$^{-2}$)",
                yticks=[0, 20, 40], xticks=xt)
bio.panel(ax, "F", (X0 - 1.6, 4.15))
pc.span(I_on, I_off, "highlight", strength=0.45)
pc.line(t, gNa, "na", lw=2.0, text="$g_{\\mathrm{Na}} = \\bar g_{\\mathrm{Na}} m^3 h$", at=float(gNa.argmax()) / len(t),
        dx=0.2, dy=-0.1)
pc.line(t, gK, "k", lw=2.0, text="$g_{\\mathrm{K}} = \\bar g_{\\mathrm{K}} n^4$", at=0.42, dx=0.15, dy=0.2)
