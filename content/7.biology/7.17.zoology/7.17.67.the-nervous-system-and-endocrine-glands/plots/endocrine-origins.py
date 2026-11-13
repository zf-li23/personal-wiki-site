# Embryonic origins of the pituitary and pharyngeal endocrine glands, schematic median section of an embryo head
# (anterior left), with pouch derivatives shown on the pharynx. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(22, 10)
# neural tube (brain) dorsally
brain = vs.smooth([(2.5, 7.2), (4.5, 8.8), (9.0, 9.0), (14.0, 8.6), (20.5, 8.2), (20.5, 7.4), (14.0, 7.5), (9.0, 7.4),
                   (6.0, 6.6), (4.0, 6.2)])
bio.shape(ax, brain, token="neuron", zorder=3)
bio.label(ax, (10.5, 8.2), "brain (neural tube)", size="tiny")
# infundibulum and Rathke's pouch
inf = vs.smooth([(6.2, 6.7), (6.6, 5.7), (6.9, 5.4), (7.2, 5.7), (7.4, 6.6)])
bio.shape(ax, inf, token="neuron", zorder=4)
rp = vs.smooth([(5.4, 3.6), (5.6, 4.6), (6.2, 5.2), (6.9, 5.2), (7.0, 4.6), (6.6, 4.4), (6.3, 3.6)])
bio.shape(ax, rp, token="receptor", zorder=4)
# stomodeum and pharynx (endoderm tube)
ph = vs.smooth([(4.6, 3.5), (6.5, 3.9), (10.0, 4.0), (19.5, 3.8), (19.5, 2.4), (10.0, 2.2), (6.5, 2.4), (4.6, 2.8)])
bio.shape(ax, ph, token="enzyme", zorder=2)
bio.shape(ax, vs.oval((4.3, 3.1), 0.5, 0.55), token="receptor", zorder=3)
bio.label(ax, (3.2, 1.7), "stomodeum (ectoderm)", size="tiny")
# pouches 1-5 as dorsal bumps (ventral derivatives as dots)
pouch_x = [9.0, 11.0, 13.0, 15.0, 17.0]
names = ["1: middle ear, Eustachian tube", "2: tonsil", "3: parathyroid, thymus", "4: parathyroid, thymus",
         "last: ultimobranchial body"]
for i, (x, n) in enumerate(zip(pouch_x, names)):
    bio.shape(ax, vs.oval((x, 4.3), 0.5, 0.5), token="enzyme", zorder=3, lw=0.8)
    bio.callout(ax, (x, 4.6), (x + 0.4, 6.0 - 0.0 * i), n, size="tiny") if i in (0, 2, 4) else \
        bio.callout(ax, (x, 4.6), (x - 0.2, 5.4), n, size="tiny")
# thyroid from the floor between pouches 1 and 2
th = vs.smooth([(9.8, 2.3), (9.7, 1.3), (10.1, 0.9), (10.5, 1.3), (10.3, 2.3)])
bio.shape(ax, th, token="positive", zorder=4)
bio.callout(ax, (10.1, 1.2), (12.6, 0.6), "thyroid (from the pharyngeal floor; endostyle homologue)", size="tiny")
bio.callout(ax, (6.9, 5.5), (8.6, 6.8), "infundibulum: neurohypophysis", size="tiny")
bio.callout(ax, (5.7, 4.6), (2.4, 5.4), "Rathke's pouch: adenohypophysis", size="tiny")
bio.label(ax, (14.0, 3.1), "pharynx (endoderm)", size="tiny", color=P.on_fill())
