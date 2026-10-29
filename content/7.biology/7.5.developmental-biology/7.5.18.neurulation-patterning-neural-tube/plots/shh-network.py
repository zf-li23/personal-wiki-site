"""A model of how the ventral neural tube reads the Shh gradient (after Balaskas et al. 2012). Gli activity
G(x, t) follows the Shh gradient (decay length 0.15 of the ventral half) and adapts: it rises, then falls to 65%
of its peak as Patched accumulates. Pax6 (P), Olig2 (O) and Nkx2.2 (N) repress one another; Gli induces Olig2 at
a low threshold and Nkx2.2 only at a high one. (A) The domain with the highest factor at each position and time:
Olig2 appears first, Nkx2.2 later and only ventrally, displacing Olig2; the borders then stay put although
signalling declines. (B) Final levels across the ventral tube (0 = floor plate) and Gli activity at its peak
(dashed) and at the end (dotted). (C) Final fate of a single cell given a pulse of Gli activity of a given level and duration, followed
by 40% of that level: a ventral (Nkx2.2) fate needs both a high level and a long exposure; with a short pulse the
same level gives Olig2, as in explants exposed to Shh for different times (Dessaud et al. 2007)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
h = 4
aP, aO, aN = 4.0, 5.0, 8.0
nPN, nPO, nON, nOP, nNO, nNP = 0.4, 1.0, 0.8, 3.0, 2.0, 1.0


def rhs(P, O, N, G):
    dP = aP / (1 + (N / nPN) ** h + (O / nPO) ** h) - P
    dO = aO * G / (G + 0.25) / (1 + (N / nON) ** h + (P / nOP) ** h) - O
    dN = aN * G ** 4 / (G ** 4 + 0.5 ** 4) / (1 + (O / nNO) ** h + (P / nNP) ** h) - N
    return dP, dO, dN


def gli(S, t):
    amp = 1 - 0.35 * (1 - np.exp(-t / 10))
    return amp * S / (S + 0.3) * min(1.0, t / 2)


x = np.linspace(0, 1, 101)
S = np.exp(-x / 0.15)
P = np.zeros_like(x)
O = np.zeros_like(x)
N = np.zeros_like(x)
dt, T = 0.01, 40.0
times, dom = [], []
for k in range(int(T / dt)):
    t = k * dt
    G = gli(S, t)
    dP, dO, dN = rhs(P, O, N, G)
    P, O, N = P + dt * dP, O + dt * dO, N + dt * dN
    if k % 20 == 0:
        times.append(t)
        lvl = np.c_[P, O, N]
        d = np.argmax(lvl, 1).astype(float)
        d[lvl.max(1) < 0.5] = np.nan
        dom.append(d)
dom = np.array(dom)

fig, axs = plt.subplots(1, 3, figsize=(11.6, 3.8), gridspec_kw={"width_ratios": [1.1, 1, 1]})
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.34)
toks = ["neutral", "receptor", "drug"]       # Pax6 (p2 and dorsal), Olig2 (pMN), Nkx2.2 (p3)
cmap = ListedColormap([P_.fill(t) for t in toks])
a = axs[0]
a.imshow(dom.T, origin="lower", aspect="auto", extent=[0, T, 0, 1], cmap=cmap, vmin=-0.5, vmax=2.5, interpolation="nearest")
for name, tok, (tx, ty) in (("Pax6", "neutral", (30, 0.7)), ("Olig2", "receptor", (30, 0.3)), ("Nkx2.2", "drug", (30, 0.08))):
    a.text(tx, ty, name, fontsize=FT["small"], style="italic", color=P_.on_fill(), ha="center", va="center")
charts.style_axes(a, "time", "distance from floor plate", box=True)
charts.title(a, "A  Domains over time")

b = axs[1]
for v, name, tok in ((P, "Pax6", "neutral"), (O, "Olig2", "receptor"), (N, "Nkx2.2", "drug")):
    b.plot(x, v, color=charts.line(tok), lw=1.7, label=name)
b.plot(x, 8 * gli(S, 2.0), color=P_.muted(), lw=1.0, ls="--", label="Gli (x8), peak")
b.plot(x, 8 * gli(S, T), color=P_.muted(), lw=1.0, ls=":", label="Gli (x8), end")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(b, "distance from floor plate", "level")
charts.title(b, "B  Final pattern")

c = axs[2]
gl, du = np.meshgrid(np.linspace(0.1, 0.9, 60), np.linspace(0.0, 16.0, 60))
Pc, Oc, Nc = np.full(gl.shape, 4.0), np.zeros(gl.shape), np.zeros(gl.shape)
for k in range(int(60 / 0.02)):
    t = k * 0.02
    G = np.where(t < du, gl, 0.4 * gl)        # a pulse of Gli of a given level and duration, then a lower level
    dP, dO, dN = rhs(Pc, Oc, Nc, G)
    Pc, Oc, Nc = Pc + 0.02 * dP, Oc + 0.02 * dO, Nc + 0.02 * dN
fate = np.argmax(np.stack([Pc, Oc, Nc], -1), -1)
c.imshow(fate, origin="lower", aspect="auto", extent=[0.1, 0.9, 0, 16], cmap=cmap, vmin=-0.5, vmax=2.5, interpolation="nearest")
for name, (tx, ty) in (("Pax6", (0.16, 10)), ("Olig2", (0.5, 8)), ("Nkx2.2", (0.84, 10))):
    c.text(tx, ty, name, fontsize=FT["small"], style="italic", color=P_.on_fill(), ha="center", va="center")
charts.style_axes(c, "Gli level during the pulse", "pulse duration", box=True)
charts.title(c, "C  Level and duration")
