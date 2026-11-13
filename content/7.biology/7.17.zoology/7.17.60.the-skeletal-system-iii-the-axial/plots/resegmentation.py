# Resegmentation, schematic frontal section (anterior up), after Christ et al. (2000) and Kardong (2019).
# Left: somites with myotome (dermomyotome) and sclerotome halves (loose anterior, dense posterior); spinal nerves
# through the anterior halves. Right: vertebrae formed from the posterior half of one sclerotome and the anterior
# half of the next, alternating with the myotomes; nerves between vertebrae.
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(20, 12)
H = 3.0
for side, x0 in (("before", 1.0), ("after", 11.0)):
    bio.shape(ax, [(x0 + 1.6, 0.6), (x0 + 2.2, 0.6), (x0 + 2.2, 11.0), (x0 + 1.6, 11.0)], token="neutral", lw=0.5, zorder=2)
    for k in range(3):
        top = 10.4 - k * H
        mid = top - H / 2
        bio.shape(ax, [(x0 + 4.2, top - 0.05), (x0 + 6.2, top - 0.05), (x0 + 6.2, top - H + 0.05), (x0 + 4.2, top - H + 0.05)],
                  token="muscle", lw=0.6, zorder=3)
        if side == "before":
            vs.bone(ax, "centrum", vs.poly([(x0 + 2.3, top - 0.05), (x0 + 4.1, top - 0.05), (x0 + 4.1, mid), (x0 + 2.3, mid)]), state="cartilage")
            vs.bone(ax, "centrum", vs.poly([(x0 + 2.3, mid), (x0 + 4.1, mid), (x0 + 4.1, top - H + 0.05), (x0 + 2.3, top - H + 0.05)]))
            ax.plot([x0 + 1.9, x0 + 7.2], [top - 0.75, top - 0.75], color=P.fill("neuron"), lw=2.0, zorder=6)
        else:
            bot = mid - H + 0.05 if k < 2 else top - H + 0.05
            vs.bone(ax, "centrum", vs.poly([(x0 + 2.3, mid - 0.05), (x0 + 4.1, mid - 0.05), (x0 + 4.1, bot), (x0 + 2.3, bot)]))
            if k == 0:
                vs.bone(ax, "centrum", vs.poly([(x0 + 2.3, top - 0.05), (x0 + 4.1, top - 0.05), (x0 + 4.1, mid + 0.05), (x0 + 2.3, mid + 0.05)]))
            ax.plot([x0 + 1.9, x0 + 7.2], [mid, mid], color=P.fill("neuron"), lw=2.0, zorder=6)
        bio.label(ax, (x0 + 5.2, mid), "myotome %d" % (k + 1), size="tiny", color=P.on_fill())
bio.label(ax, (4.8, 11.6), "Somites: sclerotome halves", size="small", bold=True)
bio.label(ax, (14.8, 11.6), "After resegmentation", size="small", bold=True)
bio.label(ax, (2.9, 0.2), "notochord", size="tiny", color=P.muted())
bio.label(ax, (12.9, 0.2), "notochord", size="tiny", color=P.muted())
bio.callout(ax, (4.2, 9.6), (7.0, 11.0), "anterior (loose) half", size="tiny")
bio.callout(ax, (4.2, 8.2), (8.2, 9.9), "posterior (dense) half", size="tiny")
bio.callout(ax, (17.8, 8.9), (19.0, 10.6), "spinal nerve", size="tiny")
bio.callout(ax, (14.2, 7.2), (19.2, 0.6), "vertebra", size="tiny")
bio.arrow(ax, (8.6, 6.0), (10.4, 6.0), kind="process")
