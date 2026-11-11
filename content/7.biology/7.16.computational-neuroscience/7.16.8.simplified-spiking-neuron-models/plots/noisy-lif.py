"""The LIF neuron driven by noise: tau_m dV/dt = -(V - E_L) + mu + sigma sqrt(2 tau_m) xi(t), with xi
Gaussian white noise, so that without threshold V is an Ornstein-Uhlenbeck process with mean E_L + mu and
standard deviation sigma; E_L = V_reset = -65 mV, V_th = -50 mV (threshold at mu = 15 mV), tau_m = 10 ms,
tau_ref = 2 ms. Euler-Maruyama, dt = 0.1 ms, 200 neurons per condition, 5 s each. A: voltage traces for a
mean-driven (mu = 15.5 mV, sigma = 0.5 mV) and a fluctuation-driven neuron (mu = 12 mV, sigma = 4 mV)
firing at similar rates (about 30 Hz). B: their interspike-interval histograms: narrow (nearly periodic) versus broad and skewed,
with a roughly exponential tail. C: firing rate against the mean input mu for sigma = 0
(deterministic, analytic), 2 and 4 mV: noise smooths the threshold of the f-I curve. D: coefficient of
variation of the ISIs against mu: irregular firing (C_V near 1) below threshold, regular firing above."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
EL, Vth, tau, tref, dt = -65.0, -50.0, 10.0, 2.0, 0.1
rng = np.random.default_rng(0)


def run(mu, sigma, T=5000.0, record=None):
    """mu, sigma: arrays of the same shape (one entry per neuron). Returns spike-time lists and a trace."""
    mu = np.asarray(mu, float); sigma = np.asarray(sigma, float)
    V = np.full(mu.shape, EL); last = np.full(mu.shape, -1e9)
    spikes = [[] for _ in range(mu.size)]
    steps = int(T / dt)
    trace = np.empty((steps, len(record))) if record is not None else None
    amp = sigma * np.sqrt(2 * dt / tau)
    for k in range(steps):
        t = k * dt
        act = t - last >= tref
        V = np.where(act, V + dt / tau * (-(V - EL) + mu) + amp * rng.standard_normal(mu.shape), V)
        spk = V >= Vth
        if spk.any():
            for j in np.flatnonzero(spk):
                spikes[j].append(t)
            V = np.where(spk, EL, V); last = np.where(spk, t, last)
        if record is not None:
            trace[k] = np.where(spk[record], 0.0, V[record])
    return spikes, trace


fig, axs = plt.subplots(2, 2, figsize=(10.0, 5.8))
fig.subplots_adjust(wspace=0.28, hspace=0.5, left=0.07, right=0.99, bottom=0.09, top=0.93)

# A, B
conds = [(15.5, 0.5, "blood", "mean-driven: $\\mu = 15.5$, $\\sigma = 0.5$ mV"), (12.0, 4.0, "dna", "fluctuation-driven: $\\mu = 12$, $\\sigma = 4$ mV")]
mu = np.repeat([c[0] for c in conds], 100); sg = np.repeat([c[1] for c in conds], 100)
spikes, trace = run(mu, sg, T=5000.0, record=[0, 100])
ax = axs[0, 0]
tt = np.arange(trace.shape[0]) * dt
sel = tt < 300
for j, (m, s, tok, lab) in enumerate(conds):
    ax.plot(tt[sel], trace[sel, j] + 0 * j, color=charts.line(tok), lw=0.7, label=lab)
ax.axhline(Vth, color=P.muted(), lw=0.7, ls=":")
ax.set_ylim(-75, 25)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=1)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "A  Two ways to fire at about 30 Hz")
ax = axs[0, 1]
bins = np.arange(0, 200, 4)
for j, (m, s, tok, lab) in enumerate(conds):
    isi = np.concatenate([np.diff(spikes[i]) for i in range(100 * j, 100 * (j + 1))])
    cv = isi.std() / isi.mean()
    ax.hist(isi, bins=bins, density=True, histtype="step", lw=1.4, color=charts.line(tok),
            label=f"rate {1000 / isi.mean():.0f} Hz, $C_V$ = {cv:.2f}")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "interspike interval / ms", "density / ms$^{-1}$")
charts.title(ax, "B  ISI distributions")

# C, D: sweep the mean input
mus = np.linspace(0, 30, 16)
sigmas = [2.0, 4.0]
mu = np.tile(np.repeat(mus, 20), len(sigmas)); sg = np.repeat(sigmas, 20 * len(mus))
spikes, _ = run(mu, sg, T=4000.0)
ax_r, ax_c = axs[1, 0], axs[1, 1]
mg = np.linspace(0, 30, 400)
with np.errstate(divide="ignore", invalid="ignore"):
    r0 = np.where(mg > Vth - EL, 1000 / (tref + tau * np.log(mg / (mg - (Vth - EL)))), 0.0)
ax_r.plot(mg, r0, color=charts.line("neutral"), lw=1.5, label="$\\sigma = 0$")
for k, (s, tok) in enumerate(zip(sigmas, ["neuron", "dna"])):
    rate, cvs = [], []
    for i, m in enumerate(mus):
        idx = range((k * len(mus) + i) * 20, (k * len(mus) + i + 1) * 20)
        n = sum(len(spikes[j]) for j in idx)
        rate.append(n / (20 * 4.0))
        isi = np.concatenate([np.diff(spikes[j]) for j in idx if len(spikes[j]) > 1] or [np.array([])])
        cvs.append(isi.std() / isi.mean() if len(isi) > 30 else np.nan)
    ax_r.plot(mus, rate, "o-", ms=3, lw=1.2, color=charts.line(tok), label=f"$\\sigma = {s:g}$ mV")
    ax_c.plot(mus, cvs, "o-", ms=3, lw=1.2, color=charts.line(tok), label=f"$\\sigma = {s:g}$ mV")
for ax in (ax_r, ax_c):
    ax.axvline(Vth - EL, color=P.muted(), lw=0.7, ls=":")
ax_r.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax_r, "mean input $\\mu$ / mV", "firing rate / Hz")
charts.title(ax_r, "C  Noise smooths the f-I curve")
ax_c.axhline(1.0, color=P.muted(), lw=0.7, ls="--")
ax_c.set_ylim(0, 1.2)
ax_c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax_c, "mean input $\\mu$ / mV", "$C_V$ of ISIs")
charts.title(ax_c, "D  Irregularity below threshold")
