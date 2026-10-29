# Maintenance of the parasegment boundary by the Wingless-Hedgehog loop (Formula 15.4.1). Each of 16 cells (four
# parasegments of four cells) can express engrailed (en, with hedgehog) and wingless (wg). Pair-rule inputs switch en
# on in the first cell of each parasegment and wg in the last for t < 5 and then vanish; Sloppy-paired keeps the wg
# cells competent. En is maintained by Wingless from the neighbouring cells, wg by Hedgehog from the neighbours.
# A: wild type, the pattern persists after the initiating inputs are gone. B: no Wingless: en fades once the
# pair-rule input ends. C: Hedgehog signalling blocked transiently (5 < t < 9): the loop collapses and does not recover,
# because the off state is also stable.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
n = 16
ps = np.arange(n) % 4
en_comp = (ps == 0).astype(float)
wg_comp = (ps == 3).astype(float)


def f(u, K=0.5, m=3):
    u = np.maximum(u, 0)
    return u ** m / (K ** m + u ** m)


def run(wg_on=True, block=None, T=30.0, dt=0.02):
    E = np.zeros(n); Wg = np.zeros(n)
    out_E, out_W = [], []
    for k in range(int(T / dt)):
        t = k * dt
        init = 1.0 if t < 5 else 0.0
        nbW = np.roll(Wg, 1) + np.roll(Wg, -1)
        nbH = np.roll(E, 1) + np.roll(E, -1)  # hh is expressed with en
        hfac = 0.0 if (block and block[0] < t < block[1]) else 1.0
        dE = f(1.6 * nbW + 2 * init * en_comp) * en_comp - E
        dW = (f(1.6 * hfac * nbH + 2 * init * wg_comp) * wg_comp - Wg) if wg_on else -Wg
        E += dt * dE
        Wg += dt * dW
        if k % 25 == 0:
            out_E.append(E.copy()); out_W.append(Wg.copy())
    return np.array(out_E), np.array(out_W)


fig, ax = bio.canvas(23.0, 8.6)
cases = [("A", "wild type", {}), ("B", "wingless mutant", {"wg_on": False}), ("C", "Hedgehog signalling blocked, 5 < t < 9",
                                                                             {"block": (5, 9)})]
for k, (letter, title, kw) in enumerate(cases):
    E, Wg = run(**kw)
    pa = C.axes_at(ax, (1.2 + k * 7.4, 1.4, 6.2, 5.4))
    img = np.zeros(E.shape + (3,))
    from matplotlib.colors import to_rgb
    bg = np.array(to_rgb(P.surface()))
    ce, cw = np.array(to_rgb(P.edge("channel"))), np.array(to_rgb(P.edge("positive")))
    img = bg + E[..., None] * (ce - bg) + Wg[..., None] * (cw - bg)
    pa.imshow(np.clip(img, 0, 1), aspect="auto", origin="lower", extent=(0.5, n + 0.5, 0, 30), interpolation="nearest")
    pa.axhline(5, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
    if "block" in kw:
        pa.axhspan(5, 9, color=P.fill("negative"), alpha=0.25, lw=0)
    pa.set_xticks([1, 4, 5, 8, 9, 12, 13, 16])
    C.style_axes(pa, "cell", "time" if k == 0 else None, box=True)
    bio.panel(ax, letter, (0.3 + k * 7.4, 8.4))
    bio.label(ax, (1.2 + k * 7.4, 7.25), title, size="small", bold=True, ha="left", italic=(k == 1 and False))
bio.label(ax, (1.2, 0.3), "blue: engrailed + hedgehog; green: wingless; dotted: pair-rule inputs end", size="tiny",
          color=P.muted(), ha="left")
