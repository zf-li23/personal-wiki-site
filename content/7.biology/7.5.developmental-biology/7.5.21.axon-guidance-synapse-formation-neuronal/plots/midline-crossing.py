"""Crossing the midline of the spinal cord (transverse section, dorsal up). (A) Commissural neurons in the dorsal
spinal cord send axons ventrally towards the floor plate. Before crossing, they express the netrin receptor DCC and
Robo3, which silences the Slit receptors Robo1 and Robo2; netrin (from the floor plate and, deposited on the pial
surface, from ventricular progenitors) attracts them and Shh from the floor plate adds attraction through Boc.
After crossing they lose Robo3, Robo1/2 become active and Slit from the floor plate repels them, together with
semaphorin-3B acting through neuropilin-2 and plexin-A1, so they cannot recross and they turn longitudinally
(anteriorly, guided by a Wnt gradient). Motor neurons express Robo1/2 but neither DCC nor Robo3, are repelled by the
floor plate and leave the cord through the ventral root. (B) The receptor states before and after crossing."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N
from matplotlib.patches import Circle

fig, ax = bio.canvas(22, 10.5)
P = bio.P
ne = N.TISSUE["neural"]
bio.panel(ax, "A", (0.2, 10.3))
cx, cy, H = 5.2, 5.4, 8.0
t = np.linspace(0, 2 * np.pi, 16, endpoint=False)
outline = bio.smooth_closed(np.c_[cx + 0.31 * H * (1 + 0.05 * np.sin(t)) * np.cos(t), cy + H / 2 * np.sin(t)])
bio.shape(ax, outline, ne, lw=1.1, alpha=0.5)
ax.plot([cx, cx], [cy - 0.33 * H, cy + 0.33 * H], color=P.edge(ne), lw=1.0)
bio.shape(ax, bio.blob((cx, cy - 0.45 * H), 0.45, 0.3, wobble=0.04, seed=2, k=8), "drug", lw=1.0)
bio.label(ax, (cx, cy - 0.45 * H - 0.6), "floor plate: netrin, Slit, Shh", size="tiny", color=P.edge("drug"))
# commissural neuron: dorsal, axon to floor plate, crosses, turns
nb = (cx - 1.4, cy + 2.6)
ax.add_patch(Circle(nb, 0.28, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.0, zorder=6))
path = np.array([nb, (cx - 1.9, cy + 0.5), (cx - 1.2, cy - 2.6), (cx - 0.2, cy - 3.45), (cx + 0.8, cy - 3.2), (cx + 1.6, cy - 2.6)])
q, _, _ = bio.polyline(path, n=200)
ax.plot(q[:, 0], q[:, 1], color=P.edge("neuron"), lw=2.0, zorder=5)
ax.add_patch(Circle((cx + 1.6, cy - 2.6), 0.18, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=6))
bio.label(ax, (cx + 2.0, cy - 2.25), "turns anteriorly", size="tiny", ha="left", color=P.muted())
bio.callout(ax, nb, (0.4, cy + 4.1), "commissural neuron (dI1)")
# motor neuron: ventral, axon exits
mn = (cx + 1.3, cy - 1.4)
ax.add_patch(Circle(mn, 0.3, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=1.0, zorder=6))
ax.plot([mn[0], cx + 2.5, cx + 4.3], [mn[1], cy - 1.3, cy - 1.0], color=P.edge("receptor"), lw=2.0)
bio.label(ax, (cx + 4.3, cy - 1.4), "ventral root", size="tiny", color=P.muted())
bio.callout(ax, mn, (cx + 3.3, cy + 0.8), "motor neuron")
bio.label(ax, (cx + 2.3, cy - 4.1), "Slit repels after crossing", size="tiny", color=P.edge("negative"), ha="left")
bio.arrow(ax, (cx - 0.5, cy - 3.0), (cx - 1.4, cy - 1.6), kind="activation", lw=0.8, color=P.edge("positive"), head=0.12)
bio.label(ax, (cx - 2.6, cy - 1.1), "netrin attracts", size="tiny", color=P.edge("positive"))

# (B) receptor states
bio.panel(ax, "B", (11.5, 10.3))
cols = [("Pre-crossing commissural", 13.8), ("Post-crossing commissural", 17.2), ("Motor neuron", 20.4)]
rows = [("DCC (netrin)", ["on", "on (silenced by Robo1)", "off; Unc5c instead"]), ("Robo3", ["on", "off", "off"]),
        ("Robo1/2 (Slit)", ["silenced", "on", "on"]), ("PlexinA1 (Sema3B)", ["off (degraded)", "on", "-"]),
        ("Response to floor plate", ["attracted", "repelled", "repelled"])]
for name, x in cols:
    bio.label(ax, (x, 9.4), name, size="tiny", bold=True)
for k, (rname, vals) in enumerate(rows):
    y = 8.4 - k * 1.35
    bio.label(ax, (11.8, y), rname, size="small", ha="left")
    for (name, x), val in zip(cols, vals):
        tok = "positive" if val in ("on", "attracted") else "negative" if val in ("repelled",) else "neutral"
        bio.box(ax, (x, y - 0.5), 3.0, 0.62, token=tok, text=val, size="tiny")
