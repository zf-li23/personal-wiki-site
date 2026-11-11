"""Gamma oscillations in a spiking E-I network: PING and ING.

400 excitatory (E) and 100 inhibitory (I) leaky integrate-and-fire neurons (tau_m = 20 and 10 ms,
V_rest = -70, threshold -50, reset -60 mV), conductance-based synapses (reversal 0 mV for AMPA,
tau = 2 ms; -75 mV for GABA_A, tau = 8 ms), random connectivity with probability 0.5, a constant
drive that would bring the cells about 20 mV above rest (E: 22 mV, I: given per case) plus
independent white noise (sigma = 3 mV). Each spike adds w to the postsynaptic conductance in units
of the leak conductance. 1 s of simulated time, dt = 0.1 ms.
PING: E -> I (w = 0.08), I -> E (0.06), I -> I (0.04); the E cells drive the I cells and the I cells
silence the E cells for a few milliseconds.
No E -> I: the PING network with the E -> I connection removed (control).
A: raster of the PING network over 200 ms (E cells below, I cells above; 100 E and all I cells shown).
B: population rate of E and I cells (2 ms bins) over the same 200 ms.
C: power spectra of the E population rate with and without the E -> I connection.
D: frequency of the spectral peak against the decay time constant of the GABA_A conductance
   (5, 8, 12, 20 ms): slower inhibition gives a slower rhythm.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
NE, NI = 400, 100
dt, T = 0.1, 1000.0
n = int(T / dt)
VL, Vth, Vr = -70.0, -50.0, -60.0
tmE, tmI = 20.0, 10.0
Eexc, Einh = 0.0, -75.0
tAMPA = 2.0
CIE = (rng.random((NI, NE)) < 0.5) * 1.0
CEI = (rng.random((NE, NI)) < 0.5) * 1.0
CII = (rng.random((NI, NI)) < 0.5) * 1.0


def simulate(muE, muI, wIE, wEI, wII, sig=3.0, seed=1, tG=8.0):
    r = np.random.default_rng(seed)
    VE = VL + r.random(NE) * 20
    VI = VL + r.random(NI) * 20
    gA = np.zeros(NI)
    gGE = np.zeros(NE)
    gGI = np.zeros(NI)
    sE, sI = [], []
    dA, dG = np.exp(-dt / tAMPA), np.exp(-dt / tG)
    for k in range(n):
        VE += dt / tmE * (-(VE - VL) + muE - gGE * (VE - Einh)) + sig * np.sqrt(2 * dt / tmE) * r.standard_normal(NE)
        VI += dt / tmI * (-(VI - VL) + muI - gA * (VI - Eexc) - gGI * (VI - Einh)) + sig * np.sqrt(2 * dt / tmI) * r.standard_normal(NI)
        fe, fi = VE >= Vth, VI >= Vth
        VE[fe] = Vr
        VI[fi] = Vr
        gA *= dA
        gGE *= dG
        gGI *= dG
        if fe.any():
            gA += wIE * CIE[:, fe].sum(axis=1)
            sE.append((k * dt, np.flatnonzero(fe)))
        if fi.any():
            gGE += wEI * CEI[:, fi].sum(axis=1)
            gGI += wII * CII[:, fi].sum(axis=1)
            sI.append((k * dt, np.flatnonzero(fi)))
    return sE, sI


def times_ids(sp):
    if not sp:
        return np.array([]), np.array([], int)
    return np.concatenate([[a] * len(b) for a, b in sp]), np.concatenate([b for _, b in sp])


def pop_rate(sp, N, bin_ms=2.0):
    t, _ = times_ids(sp)
    h, _ = np.histogram(t, bins=np.arange(0, T + 1, bin_ms))
    return h / N / (bin_ms / 1000.0)


def spectrum(rate, bin_ms=2.0, seg=128):
    x = rate[50:]  # drop the first 100 ms
    ps = []
    for i in range(0, len(x) - seg + 1, seg // 2):
        s = x[i:i + seg] - x[i:i + seg].mean()
        ps.append(np.abs(np.fft.rfft(s * np.hanning(seg))) ** 2)
    f = np.fft.rfftfreq(seg, bin_ms / 1000.0)
    return f, np.mean(ps, axis=0)


spE, spI = simulate(22.0, 0.0, 0.08, 0.06, 0.04)
ctlE, ctlI = simulate(22.0, 0.0, 0.0, 0.06, 0.04)

fig = plt.figure(figsize=(13, 4.2))
gs = fig.add_gridspec(2, 3, width_ratios=[1.3, 1.3, 1], height_ratios=[1.4, 1])
ax = fig.add_subplot(gs[:, 0])
tE, iE = times_ids(spE)
tI, iI = times_ids(spI)
m = (tE >= 400) & (tE < 600) & (iE < 100)
ax.plot(tE[m] - 400, iE[m], "|", ms=3, color=P.edge("dna"), mew=0.8)
m = (tI >= 400) & (tI < 600)
ax.plot(tI[m] - 400, iI[m] + 110, "|", ms=3, color=P.edge("negative"), mew=0.8)
ax.set_xlim(0, 200)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Neuron (E: 0-99, I: 110-209)")
ax.set_title("A  PING raster", loc="left", fontsize=10)
ax = fig.add_subplot(gs[:, 1])
rE, rI = pop_rate(spE, NE), pop_rate(spI, NI)
tb = np.arange(len(rE)) * 2.0
sl = (tb >= 400) & (tb < 600)
ax.plot(tb[sl] - 400, rE[sl], color=P.edge("dna"), lw=1.4, label="E")
ax.plot(tb[sl] - 400, rI[sl], color=P.edge("negative"), lw=1.4, label="I")
ax.set_xlim(0, 200)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Population rate / Hz")
ax.set_title("B  Population rates", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax = fig.add_subplot(gs[0, 2])
for lab, rate, col in (("PING", rE, P.edge("dna")), ("no E to I", pop_rate(ctlE, NE), P.muted())):
    f, ps = spectrum(rate)
    sel = (f > 4) & (f < 120)
    ax.semilogy(f[sel], ps[sel] / ps[sel].sum(), color=col, lw=1.5, label=lab)
ax.set_xlabel("Frequency / Hz")
ax.set_ylabel("Relative power")
ax.set_title("C  Spectrum of the E rate", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5)
ax = fig.add_subplot(gs[1, 2])
taus, fpk = [5.0, 8.0, 12.0, 20.0], []
for tg in taus:
    e, _ = simulate(22.0, 0.0, 0.08, 0.06, 0.04, tG=tg)
    f, ps = spectrum(pop_rate(e, NE))
    sel = (f > 10) & (f < 100)
    fpk.append(f[sel][ps[sel].argmax()])
ax.plot(taus, fpk, "o-", color=P.edge("positive"), lw=1.6)
ax.set_xlabel("GABA$_{\\mathrm{A}}$ decay time / ms")
ax.set_ylabel("Peak frequency / Hz")
ax.set_title("D  Rhythm and inhibition", loc="left", fontsize=10)
for a in fig.axes[:4]:
    a.grid(True, alpha=0.3)
fig.tight_layout()
