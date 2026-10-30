"""From cardiac crescent to four chambers (ventral views; the embryo's right is on the viewer's left), coloured
by origin. A: the first heart field (red) forms the cardiac crescent; the second heart field (orange anterior,
pink posterior) lies medial and dorsal to it in the pharyngeal mesoderm (mouse E7.5, human about day 18).
B: the crescent folds into a linear heart tube (mouse E8.0, human days 21-22), mostly left-ventricle
myocardium; second-field cells are added at the arterial pole (outflow tract, right ventricle) and the venous
pole (atria, inflow). C: the tube loops to the right (mouse E8.5, human day 23-28), bringing the atria dorsal
and anterior to the ventricles. D: the four-chambered heart (mouse E14.5, human week 7-8): the left ventricle
from the first field, the right ventricle and outflow tract from the anterior second field, most of the atria
from the posterior second field; cardiac neural crest (green) septates the outflow tract into the aorta and
pulmonary trunk, and the proepicardium gives the epicardium (purple) and coronary vessel wall."""
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(28, 10.5)
xs = (3.4, 10.2, 17.0, 23.8)
for k, (st, s, txt) in enumerate((("crescent", 2.4, "cardiac crescent\nE7.5 / day 18"), ("tube", 2.3, "linear heart tube\nE8.0 / day 21"),
                                  ("looping", 2.4, "looping\nE8.5 / day 23-28"), ("chambers", 2.4, "four chambers\nE14.5 / week 7-8"))):
    a = O.heart(ax, (xs[k], 5.2), s, st)
    bio.panel(ax, "ABCD"[k], (xs[k] - 3.2, 10.3))
    bio.label(ax, (xs[k], 0.7), txt, size="small")
    if st == "crescent":
        bio.callout(ax, a["fhf"], (0.6, 8.9), "First heart field")
        bio.callout(ax, a["shf"], (4.6, 9.6), "Second heart field")
        bio.callout(ax, a["foregut"], (3.4, 2.4), "Foregut portal")
    elif st == "tube":
        for key, xy, t in (("oft", (12.9, 8.9), "Outflow tract"), ("rv", (12.9, 7.6), "Right ventricle"), ("lv", (12.9, 5.6), "Left ventricle"),
                           ("atria", (12.9, 3.6), "Atria"), ("sinus", (12.9, 2.1), "Sinus venosus")):
            bio.callout(ax, a[key], xy, t)
    elif st == "looping":
        bio.callout(ax, a["rv"], (14.4, 2.6), "RV")
        bio.callout(ax, a["lv"], (19.6, 2.2), "LV")
        bio.callout(ax, a["atria"], (19.8, 8.8), "Atria")
    else:
        for key, xy, t in (("ra", (20.6, 9.5), "RA"), ("la", (27.4, 9.5), "LA"), ("rv", (20.6, 2.0), "RV"), ("lv", (27.4, 2.0), "LV"),
                           ("oft_septum", (26.0, 10.1), "Crest-derived septum"), ("epicardium", (24.6, 1.6), "Epicardium")):
            bio.callout(ax, a[key], xy, t)
for k in range(3):
    bio.arrow(ax, (xs[k] + 2.4, 5.2), (xs[k + 1] - 2.4, 5.2), kind="process", color=P.muted())
bio.label(ax, (xs[0] - 2.4, 1.6), "R", size="small", color=P.muted())
bio.label(ax, (xs[0] + 2.4, 1.6), "L", size="small", color=P.muted())
