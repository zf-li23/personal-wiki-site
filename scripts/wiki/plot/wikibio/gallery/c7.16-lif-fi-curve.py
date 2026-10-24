# Leaky integrate-and-fire neuron: the point-neuron abstraction and its RC circuit, membrane-potential
# traces for three input currents, and f-I curves: LIF (type I, continuous onset; with and without noise)
# versus the Hodgkin-Huxley model (type II, discontinuous onset).
import numpy as np

import wikibio as bio
from wikibio import neuro, quant

P = bio.P
fig, ax = bio.canvas(25, 11.4)

# ---- LIF model: tau dV/dt = -(V - E_L) + R I; spike and reset when V reaches V_th ------------
tau, R, EL, Vth, Vreset, tref = 20.0, 10.0, -70.0, -55.0, -75.0, 2.0  # ms, MOhm, mV, mV, mV, ms


def lif(I, T, dt=0.05, sigma=0.0, seed=0):
    """Euler(-Maruyama) LIF runs for a vector of currents I (nA); returns t, V (mV) and spike times per run."""
    rng = np.random.default_rng(seed)
    I = np.atleast_1d(np.asarray(I, float))
    n = int(T / dt)
    V = np.full(len(I), EL)
    ref = np.zeros(len(I))
    Vs = np.empty((n, len(I)))
    spikes = [[] for _ in I]
    for k in range(n):
        noise = sigma * np.sqrt(2 * dt / tau) * rng.standard_normal(len(I)) if sigma else 0.0
        dV = (-(V - EL) + R * I) * dt / tau + noise
        V = np.where(ref > 0, Vreset, V + dV)
        ref = np.maximum(ref - dt, 0)
        fired = V >= Vth
        for j in np.flatnonzero(fired):
            spikes[j].append(k * dt)
        Vs[k] = np.where(fired, 20.0, V)  # draw the spike as a brief upstroke to +20 mV
        V = np.where(fired, Vreset, V)
        ref = np.where(fired, tref, ref)
    return np.arange(n) * dt, Vs, spikes


# ---- A: point neuron and its circuit -----------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.3))
bio.neuron(ax, (2.9, 9.3), (7.0, 9.3), soma_r=0.42, dendrites=4, myelin=False, terminals=2)
neuro.electrode(ax, (3.05, 9.42), angle=55, length=1.3, width=0.22, wire=False)
bio.label(ax, (4.0, 10.75), "$I(t)$", size="small", ha="left")
bio.label(ax, (7.5, 9.3), "spikes", size="small", ha="left", color=P.muted())
bio.arrow(ax, (3.9, 8.25), (3.9, 7.25), kind="process", color=P.muted())
bio.label(ax, (4.1, 7.75), "point-neuron model", size="small", ha="left", color=P.muted())

top, bot = 6.35, 3.2
x_i, x_r, x_c = 1.1, 3.0, 4.9
neuro.wire(ax, (x_i, top), (x_c + 1.3, top))
neuro.wire(ax, (x_i, bot), (x_c, bot))
neuro.current_source(ax, (x_i, bot), (x_i, top), text="$I$", text_side=1)
mid = (top + bot) / 2
neuro.resistor(ax, (x_r, top), (x_r, mid + 0.05), length=0.75, text="$R$", text_side=-1)
neuro.battery(ax, (x_r, mid + 0.05), (x_r, bot), text="$E_{\\mathrm{L}}$", text_side=-1)
neuro.capacitor(ax, (x_c, top), (x_c, bot), text="$C$", text_side=-1)
for x in (x_r, x_c):
    neuro.node(ax, (x, top))
neuro.node(ax, (x_r, bot))
neuro.ground(ax, (x_c, bot))
neuro.wire(ax, (x_c, bot), (x_c, bot))
bio.label(ax, (x_c + 1.45, top), "$V$", size="normal", ha="left")
bio.box(ax, (3.9, 1.55), 7.0, 1.45, "neuron")
bio.label(ax, (3.9, 1.95), "$\\tau\\,\\mathrm{d}V/\\mathrm{d}t = -(V - E_{\\mathrm{L}}) + RI$", size="small", color=P.on_fill())
bio.label(ax, (3.9, 1.2), "if $V \\geq V_{\\mathrm{th}}$: spike, $V \\to V_{\\mathrm{reset}}$", size="small", color=P.on_fill())

# ---- B: membrane potential for three currents ---------------------------------------------------
currents = [(1.4, "receptor"), (1.9, "enzyme"), (2.8, "channel")]
t, Vs, _ = lif([c for c, _ in currents], 200.0)
X0, W = 10.0, 7.0
for k, (Iv, tok) in enumerate(currents):
    y0 = 7.9 - k * 3.3
    last = k == len(currents) - 1
    p = quant.Plot(ax, (X0, y0, W, 2.6), (0, 200), (-80, 25), yticks=[-75, -55, 20],
                   xticks=[0, 50, 100, 150, 200] if last else [(v, "") for v in (0, 50, 100, 150, 200)],
                   xlabel="$t$ / ms" if last else None, ylabel="$V$ / mV" if k == 1 else None)
    p.hline(Vth, "negative", text="$V_{\\mathrm{th}}$")
    p.line(t, Vs[:, k], tok, lw=1.4)
    rate = neuro.lif_rate(Iv, tau, R, Vth - EL, Vreset - EL, tref)
    p.text(200, 26, f"$I$ = {Iv:g} nA   ({rate:.0f} Hz)", ha="right", va="bottom", token=tok, size="small")
bio.panel(ax, "B", (X0 - 1.4, 11.3))

# ---- C: LIF f-I curve, analytic and with membrane noise --------------------------------------------
Ifi = np.linspace(0, 4, 201)
r = neuro.lif_rate(Ifi, tau, R, Vth - EL, Vreset - EL, tref)
In = np.linspace(0, 4, 33)
_, _, sp = lif(In, 2000.0, dt=0.1, sigma=3.0, seed=1)
rn = np.array([len(s) / 2.0 for s in sp])
X1, W1 = 20.2, 4.4
pf = quant.Plot(ax, (X1, 6.4, W1, 4.2), (0, 4), (0, 120), xlabel="$I$ / nA", ylabel="$f$ / Hz",
                xticks=[0, 1, 2, 3, 4], yticks=[0, 40, 80, 120])
bio.panel(ax, "C", (X1 - 1.4, 11.3))
pf.line(In, rn, "channel", lw=1.2, dashed=True)
pf.points(In, rn, "channel", r=0.06)
pf.line(Ifi, r, "neuron", lw=2.0)
pf.vline((Vth - EL) / R, "muted", text="rheobase")
pf.legend([("LIF", "neuron", "-"), ("LIF + noise", "channel", "--")], (X1 + 0.25, 10.25))
bio.label(ax, (X1 + W1 / 2, 11.25), "Type I: continuous onset", size="small", bold=True)

# ---- D: Hodgkin-Huxley f-I curve (from rest) --------------------------------------------------------
Ihh = np.r_[np.arange(0, 6.0, 0.5), np.arange(6.0, 7.0, 0.1), np.arange(7, 41, 1.5)]
dt = 0.025
th = np.arange(0, 400 + dt / 2, dt)
Vh, *_ = neuro.hh_simulate(lambda tt: Ihh, th)
fh = []
for j in range(len(Ihh)):
    up = th[1:][(Vh[:-1, j] < 0) & (Vh[1:, j] >= 0) & (th[1:] > 100)]
    fh.append((len(up) - 1) / (up[-1] - up[0]) * 1000 if len(up) > 2 else 0.0)
fh = np.array(fh)
ph = quant.Plot(ax, (X1, 0.95, W1, 3.6), (0, 40), (0, 120), xlabel="$I$ / (µA cm$^{-2}$)", ylabel="$f$ / Hz",
                xticks=[0, 10, 20, 30, 40], yticks=[0, 40, 80, 120])
bio.panel(ax, "D", (X1 - 1.4, 5.3))
on = fh > 0
ph.line(Ihh[~on], fh[~on], "k", lw=2.0)
ph.line(Ihh[on], fh[on], "k", lw=2.0)
ph.points([Ihh[on][0]], [fh[on][0]], "k", r=0.07)
ph.points([Ihh[~on][-1]], [0], "k", r=0.07, hollow=True)
ph.line([Ihh[~on][-1], Ihh[on][0]], [0, fh[on][0]], "k", lw=0.8, dotted=True)
ph.text(Ihh[on][0] + 1.5, fh[on][0] - 6, f"jumps to {fh[on][0]:.0f} Hz", ha="left", va="top", token="k")
bio.label(ax, (X1 + W1 / 2, 5.25), "Type II (Hodgkin–Huxley)", size="small", bold=True)
