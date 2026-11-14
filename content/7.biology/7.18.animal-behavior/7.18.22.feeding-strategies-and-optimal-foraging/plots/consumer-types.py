# Four kinds of consumer arranged by two properties of their interaction with the victims (after Thompson 1982
# and Begon, Townsend and Harper): lethality, the probability that the victim is killed, and intimacy, how long
# and how closely a consumer is associated with a single victim (the inverse of the number of victims attacked
# in a lifetime). Predators kill many victims briefly; grazers take parts of many victims without killing them;
# parasites live on or in one or a few hosts, usually without killing them; parasitoids live in one host and kill it.
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(18.0, 12.0)
X0, Y0, W, H = 2.2, 1.6, 14.6, 9.4
ax.plot([X0, X0 + W], [Y0, Y0], color=P.muted(), lw=0.9)
ax.plot([X0, X0], [Y0, Y0 + H], color=P.muted(), lw=0.9)
bio.arrow(ax, (X0, Y0), (X0 + W + 0.3, Y0), kind="process", color=P.muted(), lw=0.9)
bio.arrow(ax, (X0, Y0), (X0, Y0 + H + 0.3), kind="process", color=P.muted(), lw=0.9)
bio.label(ax, (X0 + W / 2, Y0 - 0.55), "Lethality: probability that an attacked victim is killed", size="small")
bio.label(ax, (X0 - 0.55, Y0 + H / 2), "Intimacy: time spent with one victim", size="small", rotation=90)
bio.label(ax, (X0 + 0.15, Y0 - 0.2), "low", size="tiny", color=P.muted(), ha="left", va="top")
bio.label(ax, (X0 + W - 0.1, Y0 - 0.2), "high", size="tiny", color=P.muted(), ha="right", va="top")
bio.label(ax, (X0 - 0.15, Y0 + 0.25), "low", size="tiny", color=P.muted(), ha="right", rotation=90)
bio.label(ax, (X0 - 0.15, Y0 + H - 0.3), "high", size="tiny", color=P.muted(), ha="right", rotation=90)
# quadrant guides
ax.plot([X0 + W / 2] * 2, [Y0 + 0.2, Y0 + H], color=P.mix(P.muted(), P.surface(), 0.6), lw=0.7, ls=(0, (3, 3)))
ax.plot([X0 + 0.2, X0 + W], [Y0 + H / 2] * 2, color=P.mix(P.muted(), P.surface(), 0.6), lw=0.7, ls=(0, (3, 3)))

CELLS = [
    # (centre, title, subtitle, token)
    ((X0 + W * 0.25, Y0 + H * 0.25), "Grazers and browsers", "many victims, part of each,\nrarely lethal", "plant"),
    ((X0 + W * 0.75, Y0 + H * 0.25), "Predators", "many victims, each killed\nand (mostly) eaten whole", "negative"),
    ((X0 + W * 0.25, Y0 + H * 0.75), "Parasites", "one or few hosts, lives on\nor in them, rarely lethal", "rna"),
    ((X0 + W * 0.75, Y0 + H * 0.75), "Parasitoids", "one host per larva,\nalways killed", "atp"),
]
for (cx, cy), title, sub, tok in CELLS:
    bio.label(ax, (cx, cy + 1.55), title, size="normal", bold=True, color=quant.line_color(tok))
    bio.label(ax, (cx, cy - 1.45), sub, size="tiny", color=P.muted())

# icons inside the quadrants (the consumer, then a victim)
gx, gy = CELLS[0][0]
bio.icon(ax, "phylopic/cattle", at=(gx - 1.3, gy + 0.1), height=1.3, color="plant")
bio.icon(ax, "phylopic/deer", at=(gx + 1.3, gy + 0.15), height=1.5, color="plant")
px, py = CELLS[1][0]
bio.icon(ax, "phylopic/wolf", at=(px - 1.0, py + 0.1), height=1.3, color="negative")
bio.icon(ax, "phylopic/rabbit", at=(px + 1.6, py - 0.05), height=0.85, color="neutral")
bio.arrow(ax, (px + 0.05, py + 0.05), (px + 0.95, py + 0.0), kind="process", color=P.muted(), lw=1.0)
qx, qy = CELLS[2][0]
bio.icon(ax, "phylopic/tick", at=(qx - 1.2, qy + 0.05), height=0.95, color="rna")
bio.icon(ax, "phylopic/leech", at=(qx + 1.2, qy + 0.05), height=0.8, color="rna")
rx, ry = CELLS[3][0]
bio.icon(ax, "phylopic/ichneumon", at=(rx - 1.1, ry + 0.15), height=1.2, color="atp")
bio.icon(ax, "phylopic/moth", at=(rx + 1.4, ry + 0.0), height=0.8, color="neutral")
bio.arrow(ax, (rx - 0.15, ry + 0.05), (rx + 0.75, ry + 0.0), kind="process", color=P.muted(), lw=1.0)

# intermediate cases along the edges
bio.label(ax, (X0 + W * 0.5, Y0 + 0.45), "seed predators", size="tiny", color=P.muted(), italic=True)
bio.label(ax, (X0 + W * 0.5, Y0 + H - 0.2), "castrating parasites", size="tiny", color=P.muted(), italic=True)
