# Force-velocity, power and efficiency of slow and fast fibres (illustrative parameters).
# Hill's relation (F + a)(v + b) = b (F0 + a), written with f = F/F0, alpha = a/F0 and vmax = b/alpha:
#   v = vmax alpha (1 - f) / (f + alpha).
# Slow fibre: vmax = 2 L0/s, alpha = 0.18; fast fibre: vmax = 8 L0/s, alpha = 0.30; same F0 (equal specific
# tension). Energy liberation follows Hill (1938): rate = h0 + (F + a) v, where h0 is the isometric
# (maintenance) heat rate, taken proportional to the cross-bridge cycling speed, h0 = 0.1 F0 vmax.
# Efficiency = F v / (h0 + (F + a) v) (work over energy liberated during contraction).
# (A) force-velocity curves; (B) power F v against absolute shortening speed; (C) efficiency against speed
# (log axis); the dashed line marks the speed above which the fast fibre is the more efficient.
import matplotlib.pyplot as plt
import numpy as np

fib = [("slow (type I)", 2.0, 0.18, "#c0504d"), ("fast (type IIX)", 8.0, 0.30, "#2f6fb5")]
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))
f = np.linspace(0, 1, 500)
for name, vmax, al, col in fib:
    v = vmax * al * (1 - f) / (f + al)
    a.plot(v, f, color=col, lw=2.2, label=name)
    p = f * v
    i = np.argmax(p)
    b.plot(v, p, color=col, lw=2.2, label=name)
    b.plot(v[i], p[i], "o", color=col, ms=6)
    b.annotate(f"f = {f[i]:.2f}, v/vmax = {v[i] / vmax:.2f}", xy=(v[i], p[i]), xytext=(v[i] + 0.4, p[i] + 0.04),
               fontsize=8.5, color=col)
    h0 = 0.1 * vmax
    eta = f * v / (h0 + (f + al) * v)
    c.plot(v, eta, color=col, lw=2.2, label=name)
    j = np.argmax(eta)
    c.plot(v[j], eta[j], "o", color=col, ms=6)
a.set_xlabel("Shortening velocity v / (L₀ s⁻¹)")
a.set_ylabel("Force F / F₀")
a.legend(frameon=False, fontsize=8.5)
a.set_title("A   Force-velocity (Hill)", loc="left", fontsize=10)
b.set_xlabel("Shortening velocity v / (L₀ s⁻¹)")
b.set_ylabel("Power F v / (F₀ L₀ s⁻¹)")
b.set_ylim(0, 0.95)
b.set_title("B   Power", loc="left", fontsize=10)
c.set_xlabel("Shortening velocity v / (L₀ s⁻¹), log scale")
c.set_ylabel("Efficiency (work / energy liberated)")
c.set_ylim(0, 0.5)
vv = np.linspace(0.01, 1.99, 2000)
etas = []
for name, vmax, al, col in fib:
    ff = (vmax * al - al * vv) / (vmax * al + vv)
    etas.append(ff * vv / (0.1 * vmax + (ff + al) * vv))
vc = vv[np.argmin(np.abs(etas[0] - etas[1])[200:]) + 200]
c.axvline(vc, color="0.5", lw=0.9, ls="--")
c.text(vc - 0.1, 0.47, "slow fibre\nmore efficient", ha="right", va="top", fontsize=8.5, color="0.5")
c.text(vc + 0.1, 0.47, f"fast fibre\nmore efficient\n(v > {vc:.1f} L₀/s)", ha="left", va="top", fontsize=8.5, color="0.5")
c.legend(frameon=False, fontsize=8.5, loc="lower right")
c.set_title("C   Efficiency", loc="left", fontsize=10)
for x in (a, b):
    x.set_xlim(0, 8.2)
c.set_xscale("log")
c.set_xlim(0.05, 8.2)
for x in (a, b, c):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
