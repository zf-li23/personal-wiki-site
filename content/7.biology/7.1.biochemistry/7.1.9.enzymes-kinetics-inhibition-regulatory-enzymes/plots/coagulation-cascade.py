"""The blood coagulation cascade and the amplification of a regulatory cascade.

A: SBGN process description of the coagulation cascade. Zymogens (left) are converted to active
serine proteases (right, "a") by proteolysis (process squares); catalysis arcs (open circles)
show which protease cleaves which zymogen. Initiation (extrinsic pathway): tissue factor with
factor VIIa cleaves X (and IX). Propagation: IXa with its cofactor VIIIa and Xa with its cofactor Va
generate thrombin (IIa), which cleaves fibrinogen to fibrin and activates XIII (cross-linking),
XI and the cofactors V and VIII (feedback, dashed). Inhibition arcs: tissue factor pathway
inhibitor (TFPI), antithrombin (enhanced by heparin) and activated protein C (with protein S,
inactivating Va and VIIIa).
B: a model regulatory cascade of four stages, dx_i/dt = k x_(i-1) - d x_i, driven by a brief
input pulse; with gain k/d = 10 per stage, each stage is amplified tenfold and delayed."""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts, network

P = bio.P
fig, ax = bio.canvas(24.0, 13.0, scale=0.42)

# --- A: cascade --------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.9))
d = network.Diagram(ax, size="small")
zx, ax_ = 4.2, 8.4  # x of zymogens and of active forms
rows = {"XI": 11.6, "IX": 9.9, "X": 8.2, "II": 6.5, "Fg": 4.8}
d.macromolecule("tf", (1.3, 8.2), "TF·VIIa", token="receptor")
for z, y in rows.items():
    zname = {"II": "prothrombin (II)", "Fg": "fibrinogen"}.get(z, z)
    aname = {"II": "thrombin (IIa)", "Fg": "fibrin"}.get(z, z + "a")
    d.macromolecule("z" + z, (zx, y), zname, token="neutral")
    d.macromolecule("a" + z, (ax_, y), aname, token="enzyme" if z != "Fg" else "protein")
    d.reaction(["z" + z], ["a" + z], id="p" + z)
d.macromolecule("xl", (13.0, 4.8), "cross-linked\nfibrin", token="protein")
d.reaction(["aFg"], ["xl"], id="pxl")
d.macromolecule("f13", (10.6 + 0.05, 2.9), "XIIIa", token="enzyme")
d.connect("f13", "pxl", "catalysis")
bio.label(ax, (12.2, 2.9), "(XIII activated\nby thrombin)", size="tiny", color=P.muted(), ha="left")
d.connect("tf", "pX", "catalysis", via=[(2.6, 8.2), (2.6, 7.55), (6.3, 7.55)])
d.connect("tf", "pIX", "catalysis", via=[(2.6, 8.2), (2.6, 9.25), (6.3, 9.25)])
d.connect("aXI", "pIX", "catalysis", via=[(ax_ + 1.6, 11.6), (ax_ + 1.6, 10.6), (6.3, 10.6)])
d.connect("aIX", "pX", "catalysis", via=[(ax_ + 1.6, 9.9), (ax_ + 1.6, 8.9), (6.3, 8.9)], text="+ VIIIa", text_at=0.35)
d.connect("aX", "pII", "catalysis", via=[(ax_ + 1.6, 8.2), (ax_ + 1.6, 7.2), (6.3, 7.2)], text="+ Va", text_at=0.35)
d.connect("aII", "pFg", "catalysis", via=[(ax_ + 1.6, 6.5), (ax_ + 1.6, 5.5), (6.3, 5.5)])
d.connect("aII", "pXI", "catalysis", dashed=True, via=[(ax_ + 3.0, 6.5), (ax_ + 3.0, 12.4), (6.3, 12.4)])
bio.label(ax, (ax_ + 3.15, 9.3), "feedback: thrombin also\nactivates V and VIII", size="tiny", color=P.muted(), ha="left")
d.macromolecule("tfpi", (1.3, 10.6), "TFPI", token="negative")
d.connect("tfpi", "tf", "inhibition")
d.macromolecule("at", (1.3, 5.2), "antithrombin", token="negative")
d.connect("at", "pII", "inhibition", via=[(2.6, 5.2), (2.6, 5.85), (6.3, 5.85)])
bio.label(ax, (1.3, 4.4), "(heparin enhances)", size="tiny", color=P.muted())
d.macromolecule("apc", (1.3, 2.9), "activated\nprotein C + S", token="negative")
bio.label(ax, (1.3, 2.1), "inactivates Va, VIIIa", size="tiny", color=P.muted())
bio.label(ax, (zx, 12.6), "zymogens", size="small", bold=True)
bio.label(ax, (ax_, 12.6), "active proteases", size="small", bold=True)

# --- B: amplification --------------------------------------------------------------------
bio.panel(ax, "B", (14.6, 12.9))
b = charts.axes_at(ax, (16.0, 1.6, 7.4, 10.0))
k, dd, nst = 1.0, 0.1, 4


def inp(t):
    return 1.0 if t < 1.0 else 0.0


def f(t, x):
    dx = np.empty(nst)
    prev = inp(t)
    for i in range(nst):
        dx[i] = k * prev - dd * x[i]
        prev = x[i]
    return dx


t = np.linspace(0, 80, 1600)
sol = solve_ivp(f, (0, 80), np.zeros(nst), t_eval=t, max_step=0.05)
b.plot(t, [inp(s) for s in t], color=P.muted(), lw=1.2, label="input pulse")
for i, tok in enumerate(("channel", "enzyme", "drug", "negative")):
    b.plot(t, sol.y[i], color=charts.line(tok), lw=2.0, label=f"stage {i + 1}")
b.set_yscale("log")
b.set_ylim(1e-2, 3e4)
b.set_xlim(0, 80)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "time (units of 1/k)", "active enzyme (relative)")
charts.title(b, "Amplification and delay ($k/d$ = 10)")
