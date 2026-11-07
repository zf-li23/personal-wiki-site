# The length-tension relation computed from filament geometry.
# (A) Active isometric tension of frog muscle against sarcomere length: thick filament 1.6 um with a 0.2 um
#     bare zone, thin filaments 1.0 um from each Z disc (Z disc 0.05 um). Descending limb: tension is
#     proportional to the overlap of thin filaments with the head-bearing part of the thick filament (zero at
#     1.6 + 2 x 1.025 = 3.65 um); plateau 2.05-2.25 um; ascending limb: thin filaments overlap each other below
#     2.05 um and the thick filaments hit the Z discs at 1.65 um (shape after Gordon, Huxley & Julian 1966).
#     Dashed: the same geometry with the longer human thin filaments (about 1.27 um), plateau at 2.6-2.8 um.
#     Glyphs above: the filament configurations at the numbered points (frog).
# (B) Whole-muscle tension: active (frog curve) + passive tension of titin and connective tissue
#     (exponential above 2.4 um, illustrative); the total has a dip where active tension falls faster than
#     passive tension rises.
import numpy as np

import wikibio as bio
from wikibio import physiology as phys
from wikibio import quant

P = bio.P


def active(SL, thin=1.0, z=0.05, thick=1.6, bare=0.2):
    SL = np.asarray(SL, float)
    lt = thin + z / 2
    ov = np.clip(thick / 2 - np.maximum(SL / 2 - lt, bare / 2), 0, (thick - bare) / 2) / ((thick - bare) / 2)
    hit = thick + z
    asc = np.where(SL >= hit, 1 - 0.13 * (2 * lt - SL) / (2 * lt - hit),
                   np.clip(0.87 * (SL - 1.27) / (hit - 1.27), 0, None))
    return np.where(SL >= 2 * lt, ov, asc)


fig, ax = bio.canvas(26, 12.4)
X0, Y0, W, H = 1.6, 1.4, 11.0, 6.9
pl = quant.Plot(ax, (X0, Y0, W, H), (1.2, 4.4), (0, 1.15), xlabel="Sarcomere length / µm",
                ylabel="Active tension (relative)", xticks=[1.5, 2.0, 2.5, 3.0, 3.5, 4.0], yticks=[0, 0.5, 1.0], grid=True)
bio.panel(ax, "A", (0.1, 12.3))
SL = np.linspace(1.2, 4.4, 600)
pl.line(SL, active(SL), "muscle", lw=3.2, text="frog", at=0.62)
pl.line(SL, active(SL, thin=1.27), "protein", lw=1.6, dashed=True, text="human", at=0.83)
key = [(1.65, "1"), (2.05, "2"), (2.25, "3"), (3.65, "4")]
for sl, tag in key:
    tv = float(active(sl))
    pl.points([sl], [tv], "ink", r=0.11, zorder=14)
    pl.text(sl + 0.06, tv + 0.05, tag, ha="left", va="bottom", size="small", bold=True)
gs = 0.78
gy = 10.4
gap = (W + 0.4 - sum(s for s, _ in key) * gs) / (len(key) - 1)
notes = ["thick filaments\nhit the Z discs", "thin filaments\nmeet at the M line", "edge of the\nbare zone", "no overlap"]
gx = X0 - 0.2
for k, (sl, tag) in enumerate(key):
    cx = gx + sl * gs / 2
    phys.sarcomere(ax, gx, gy, sl, scale=gs, rows=2, spacing=0.32, labels=False, bands=False, detail=False)
    bio.label(ax, (cx, gy + 0.85), f"{tag}:  {sl:g} µm", size="tiny", bold=True)
    bio.label(ax, (cx, gy - 0.75), notes[k], size="tiny", color=P.muted(), va="top")
    gx += sl * gs + gap

X1 = 15.6
pb = quant.Plot(ax, (X1, Y0, 9.6, 8.6), (1.6, 3.8), (0, 1.6), xlabel="Sarcomere length / µm",
                ylabel="Tension (relative to maximal active)", xticks=[2.0, 2.5, 3.0, 3.5], yticks=[0, 0.5, 1.0, 1.5],
                grid=True)
bio.panel(ax, "B", (X1 - 1.5, 12.3))
S2 = np.linspace(1.6, 3.8, 500)
pas = np.where(S2 > 2.4, 0.06 * (np.exp((S2 - 2.4) / 0.5) - 1), 0.0)
act = active(S2)
pb.line(S2, act, "muscle", lw=2.2, text="active", at=0.2)
pb.line(S2, pas, "dna", lw=2.2, dashed=True, text="passive (titin)", at=0.8)
pb.line(S2, act + pas, "ink", lw=2.6, text="total", at=0.72)
