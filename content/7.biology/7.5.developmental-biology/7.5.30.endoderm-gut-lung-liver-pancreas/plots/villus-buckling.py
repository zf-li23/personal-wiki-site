"""Buckling of the gut lining under compression (Formula 30.5.1). A: the compressive force needed to buckle a
thin elastic layer (bending stiffness B) bonded to an elastic foundation (stiffness K) into a wave of wavenumber
k: P(k) = B k^2 + K / k^2; the minimum, P_c = 2 sqrt(BK) at k* = (K/B)^(1/4), selects the wavelength
2 pi (B/K)^(1/4). B: a simulation of the layer under a compression 20 % above threshold (gradient flow of the
elastic energy with a weak cubic stiffening, periodic domain, random initial roughness): folds with the
predicted wavelength (dashed marks) emerge from noise. C: the selected wavelength against the thickness h of
the layer (B proportional to h^3), lambda proportional to h^(3/4): thicker, stiffer layers fold into fewer,
wider folds."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
B, K = 1.0, 1.0
fig = plt.figure(figsize=(10.4, 5.2))
gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.3], hspace=0.55, wspace=0.25, left=0.08, right=0.98, bottom=0.11, top=0.92)
a = fig.add_subplot(gs[0, 0])
k = np.linspace(0.3, 3, 300)
a.plot(k, B * k**2 + K / k**2, color=charts.line("highlight"), lw=1.8)
a.axhline(2 * np.sqrt(B * K), color=P_.muted(), lw=0.7, ls=":")
a.plot([1], [2], "o", color=P_.ink(), ms=5)
a.set_ylim(0, 8)
charts.style_axes(a, r"wavenumber $k$ (units of $(K/B)^{1/4}$)", r"buckling force $P(k)$")
charts.title(a, "A  Wavelength selection")
c = fig.add_subplot(gs[1, 0])
h = np.linspace(0.2, 2, 100)
c.plot(h, 2 * np.pi * h**0.75, color=charts.line("enzyme"), lw=1.8)
charts.style_axes(c, r"layer thickness $h$ (scaled)", r"wavelength $\lambda$")
charts.title(c, r"C  $\lambda \propto h^{3/4}$")
b = fig.add_subplot(gs[:, 1])
L, n = 80.0, 512
x = np.linspace(0, L, n, endpoint=False)
q = 2 * np.pi * np.fft.rfftfreq(n, d=L / n)
Pc = 2 * np.sqrt(B * K)
Pf = 1.2 * Pc
lin = -(B * q**4 - Pf * q**2 + K)
w = 0.01 * np.random.default_rng(0).standard_normal(n)
dt = 0.05
snaps = {}
for step in range(1, 6001):
    nl = np.fft.rfft(-0.5 * w**3)
    wh = (np.fft.rfft(w) + dt * nl) / (1 - dt * lin)
    w = np.fft.irfft(wh, n)
    if step in (150, 400, 6000):
        snaps[step] = w.copy()
for j, (st, tk) in enumerate(zip(sorted(snaps), ("neutral", "drug", "highlight"))):
    off = 3.4 * j
    b.fill_between(x, off - 1.6, off + snaps[st], color=charts.line(tk), alpha=0.6, lw=0)
    b.plot(x, off + snaps[st], color=charts.line(tk), lw=1.4)
    b.text(L + 1, off, f"t = {st * dt:.0f}", fontsize=FT["tiny"], color=P_.ink(), va="center")
lam = 2 * np.pi * (B / K) ** 0.25
for m in np.arange(0, L, lam):
    b.plot([m, m], [8.4, 8.8], color=P_.muted(), lw=0.8)
b.text(0, 9.0, r"predicted wavelength $2\pi(B/K)^{1/4}$", fontsize=FT["tiny"], color=P_.muted())
b.set_xlim(0, L + 8)
b.set_yticks([])
charts.style_axes(b, "position along the gut wall", None)
charts.title(b, "B  Folds emerge from noise (P = 1.2 Pc)")
