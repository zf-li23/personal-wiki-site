# Development of a feather (top row) and a hair (bottom row) from skin placodes, schematic sections, after
# Prum (1999), Chuong et al. (2013) and Kardong (2019). Feather: placode, bud, follicle with collar, growing
# feather with barb ridges around the dermal pulp. Hair: placode, hair peg, bulbous peg around the dermal papilla,
# mature follicle with shaft, sebaceous gland and arrector pili muscle. Epidermis and its keratinized products
# in one colour, dermis and dermal condensation/papilla in another.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 15)
EP, DE, CO = "ectoderm", "mesoderm", "highlight"


def skin(x0, y0, w=6.0):
    bio.shape(ax, [(x0, y0 - 2.6), (x0 + w, y0 - 2.6), (x0 + w, y0), (x0, y0)], token=DE, zorder=1, lw=0.5)
    bio.shape(ax, [(x0, y0), (x0 + w, y0), (x0 + w, y0 + 0.35), (x0, y0 + 0.35)], token=EP, zorder=2, lw=0.5)


labels_f = ["placode", "bud", "follicle and collar", "barb ridges; feather emerges"]
labels_h = ["placode", "hair peg", "bulbous peg", "follicle with hair"]
for i in range(4):
    x0 = 0.5 + i * 7.0
    yF, yH = 10.6, 3.6
    skin(x0, yF)
    skin(x0, yH)
    cx = x0 + 3.0
    bio.label(ax, (cx, 14.6), labels_f[i], size="tiny", bold=True)
    bio.label(ax, (cx, 7.4), labels_h[i], size="tiny", bold=True)
    # feather row
    if i == 0:
        bio.shape(ax, [(cx - 1.0, yF + 0.35), (cx + 1.0, yF + 0.35), (cx + 0.8, yF + 0.6), (cx - 0.8, yF + 0.6)], token=EP, zorder=3)
        bio.shape(ax, bio.smooth_closed([(cx - 1.2, yF - 0.1), (cx + 1.2, yF - 0.1), (cx + 0.8, yF - 0.9), (cx - 0.8, yF - 0.9)]), token=CO, zorder=3)
    elif i == 1:
        bio.shape(ax, bio.smooth_closed([(cx - 0.8, yF + 0.35), (cx + 0.8, yF + 0.35), (cx + 0.5, yF + 1.8), (cx, yF + 2.1), (cx - 0.5, yF + 1.8)]), token=EP, zorder=3)
        bio.shape(ax, bio.smooth_closed([(cx - 0.5, yF + 0.2), (cx + 0.5, yF + 0.2), (cx + 0.3, yF + 1.5), (cx - 0.3, yF + 1.5)]), token=CO, zorder=4)
    else:
        top = 2.4 if i == 2 else 2.6
        bio.shape(ax, [(cx - 0.9, yF + 0.35), (cx - 0.65, yF - 2.0), (cx + 0.65, yF - 2.0), (cx + 0.9, yF + 0.35)], token="neutral", zorder=3, lw=0.8)
        bio.shape(ax, bio.smooth_closed([(cx - 0.6, yF - 1.9), (cx + 0.6, yF - 1.9), (cx + 0.55, yF + top), (cx, yF + top + 0.3), (cx - 0.55, yF + top)]), token=EP, zorder=4)
        bio.shape(ax, bio.smooth_closed([(cx - 0.32, yF - 1.7), (cx + 0.32, yF - 1.7), (cx + 0.25, yF + top - 0.6), (cx - 0.25, yF + top - 0.6)]), token=CO, zorder=5)
        ax.plot([cx - 0.62, cx + 0.62], [yF - 1.85, yF - 1.85], color=P.ink(), lw=2.2, zorder=6)
        if i == 2:
            bio.callout(ax, (cx + 0.6, yF - 1.85), (cx + 1.8, yF - 2.3), "collar", size="tiny")
            bio.callout(ax, (cx, yF + 0.8), (cx + 1.8, yF + 1.6), "dermal pulp", size="tiny")
        else:
            for k in range(5):
                ax.plot([cx - 0.5 + 0.25 * k, cx - 0.35 + 0.25 * k], [yF + 0.4, yF + top - 0.3], color=P.edge(EP), lw=0.8, zorder=7)
            for k in range(6):
                ang = np.radians(65 + 10 * k)
                ax.plot([cx, cx + 1.1 * np.cos(ang)], [yF + top + 0.3, yF + top + 0.3 + 0.5 * np.sin(ang)], color=P.edge(EP), lw=1.0, zorder=7)
            bio.callout(ax, (cx + 0.3, yF + 1.5), (cx + 1.9, yF + 1.0), "barb ridges", size="tiny")
    # hair row
    if i == 0:
        bio.shape(ax, [(cx - 0.9, yH + 0.35), (cx + 0.9, yH + 0.35), (cx + 0.7, yH - 0.3), (cx - 0.7, yH - 0.3)], token=EP, zorder=3)
        bio.shape(ax, bio.smooth_closed([(cx - 1.0, yH - 0.35), (cx + 1.0, yH - 0.35), (cx + 0.7, yH - 1.0), (cx - 0.7, yH - 1.0)]), token=CO, zorder=3)
    elif i == 1:
        bio.shape(ax, bio.smooth_closed([(cx - 0.7, yH + 0.3), (cx + 0.7, yH + 0.3), (cx + 0.5, yH - 1.5), (cx - 0.5, yH - 1.5)]), token=EP, zorder=3)
        bio.shape(ax, bio.smooth_closed([(cx - 0.7, yH - 1.5), (cx + 0.7, yH - 1.5), (cx + 0.5, yH - 2.1), (cx - 0.5, yH - 2.1)]), token=CO, zorder=3)
    else:
        bio.shape(ax, bio.smooth_closed([(cx - 0.55, yH + 0.3), (cx + 0.55, yH + 0.3), (cx + 0.6, yH - 1.6), (cx + 0.95, yH - 2.1),
                                         (cx, yH - 2.45), (cx - 0.95, yH - 2.1), (cx - 0.6, yH - 1.6)]), token=EP, zorder=3)
        bio.shape(ax, bio.smooth_closed([(cx - 0.4, yH - 2.35), (cx + 0.4, yH - 2.35), (cx + 0.25, yH - 1.8), (cx - 0.25, yH - 1.8)]), token=CO, zorder=4)
        bio.callout(ax, (cx, yH - 2.1), (cx + 1.9, yH - 2.4), "dermal papilla", size="tiny")
        if i == 3:
            bio.shape(ax, [(cx - 0.12, yH - 1.8), (cx + 0.12, yH - 1.8), (cx + 0.3, yH + 2.6), (cx + 0.06, yH + 2.6)], token="metabolite", zorder=6)
            bio.shape(ax, bio.smooth_closed([(cx - 0.55, yH - 0.4), (cx - 1.3, yH - 0.2), (cx - 1.4, yH - 0.8), (cx - 0.6, yH - 0.9)]), token="vesicle", zorder=4)
            ax.plot([cx + 0.6, cx + 1.9], [yH - 1.2, yH - 0.1], color=P.edge("muscle"), lw=3.0, zorder=4)
            bio.callout(ax, (cx - 1.1, yH - 0.55), (cx - 2.0, yH + 1.2), "sebaceous gland", size="tiny")
            bio.callout(ax, (cx + 1.5, yH - 0.45), (cx + 2.2, yH + 1.0), "arrector pili", size="tiny")
            bio.callout(ax, (cx + 0.2, yH + 1.8), (cx + 1.8, yH + 2.4), "hair shaft", size="tiny")
bio.label(ax, (0.3, 14.6), "Feather", size="small", bold=True, ha="left")
bio.label(ax, (0.3, 7.4), "Hair", size="small", bold=True, ha="left")
for i, (tok, t) in enumerate(((EP, "epidermis and its products"), (DE, "dermis"), (CO, "dermal condensation, pulp, papilla"),
                              ("metabolite", "keratinized hair shaft"))):
    xx = 1 + i * 7
    bio.shape(ax, [(xx, -0.1), (xx + 0.5, -0.1), (xx + 0.5, 0.3), (xx, 0.3)], token=tok, lw=0.6)
    bio.label(ax, (xx + 0.7, 0.1), t, size="tiny", ha="left")
