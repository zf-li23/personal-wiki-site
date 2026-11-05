"""The fern sporangium as a catapult (after Noblin et al. 2012). A: leptosporangium closed, open (the drying
annulus bends back and the capsule tears at the stomium) and after ejection (cavitation, the annulus snaps
back). B: a two-time-scale model of the annulus angle after cavitation: an inertial snap with time scale
tau_in ~ 10 us, arrested about halfway, then poroelastic relaxation with tau_p ~ 1 ms. Dashed: an
unbraked snap back to the rest position, for comparison."""
import numpy as np

import wikibio as bio
from wikibio import charts, plant

P = bio.P
fig, ax = bio.canvas(31, 10.5)

bio.panel(ax, "A", (0.2, 10.3))
for i, (st, t) in enumerate([("closed", "Closed"), ("open", "Open: annulus bent back"), ("ejected", "Ejected")]):
    an = plant.leptosporangium(ax, (2.6 + i * 5.4, 5.4), 2.6, stage=st)
    bio.label(ax, (2.6 + i * 5.4, 2.4), t, size="small")
bio.callout(ax, an["annulus"], (15.2, 8.6), "Annulus")
bio.callout(ax, an["stomium"], (15.2, 3.6), "Stomium")

# --- B: model
tin, tp, th0, ths = 10e-6, 1e-3, 1.0, 0.5
t = np.logspace(-7, -1, 600)
snap = np.where(t < tin, ths + (th0 - ths) * np.cos(np.pi / 2 * t / tin), ths * np.exp(-(t - tin) / tp))
free_t = tin / np.arccos(ths / th0) * (np.pi / 2) / (np.pi / 2)  # time to reach 0 without the brake
free = np.where(t < 2 * tin, th0 * np.cos(np.pi / 2 * np.minimum(t / (2 * tin), 1.0)), 0.0)
bx = charts.axes_at(ax, (20.4, 1.9, 9.8, 7.0))
bx.plot(t, snap, color=charts.line("plant"), lw=2.0, label="with brake (cavitation catapult)")
bx.plot(t, free, color=charts.line("neutral"), lw=1.4, ls="--", label="without brake")
bx.set_xscale("log")
bx.set_xlim(1e-7, 1e-1)
bx.set_ylim(-0.05, 1.12)
bx.axvline(tin, color=P.muted(), lw=0.7, ls=":")
bx.axvline(tp, color=P.muted(), lw=0.7, ls=":")
bx.text(tin * 1.15, 1.04, r"$\tau_{\mathrm{in}} \approx 10\ \mu\mathrm{s}$", fontsize=8, color=P.ink())
bx.text(tp * 1.15, 1.04, r"$\tau_{\mathrm{p}} \approx 1\ \mathrm{ms}$", fontsize=8, color=P.ink())
bx.annotate("spores leave\nthe cup", xy=(tin, ths), xytext=(1.2e-7, 0.25), fontsize=8, color=P.ink(),
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
charts.style_axes(bx, xlabel="time after cavitation / s", ylabel="annulus opening (relative)")
bx.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.92))
bio.panel(ax, "B", (18.4, 10.3))
