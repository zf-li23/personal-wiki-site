"""Photopinacol coupling of benzophenone in propan-2-ol. The n,pi* triplet, whose oxygen behaves like
an alkoxyl radical, abstracts the C-H hydrogen of the alcohol (fishhook arrows), giving the
diphenylketyl radical and the 2-hydroxy-2-propyl radical; the latter gives its O-H hydrogen to a
second benzophenone (forming acetone and another ketyl). Two diphenylketyl radicals then combine to
benzopinacol (1,1,2,2-tetraphenylethane-1,2-diol)."""

import numpy as np
from wikichem import Scheme


def shift(p, d):
    return np.asarray(p.xy, float) + np.asarray(d, float)


s = Scheme()
y = 0.0
b = s.molecule("[O][C](c1ccccc1)c1ccccc1", at=(0.0, y))
o = b.xy(0)
hx, hy = o[0] + 1.4, o[1]
cx = hx + 1.0
ip = s.molecule("[H]C(C)(C)O", coords=[(hx, hy), (cx, hy), (cx + 0.5, hy + 0.87), (cx + 0.5, hy - 0.87), (cx + 1.0, hy)])
mid = (o + ip.xy(0)) / 2
s.curly(b.atom(0), mid, bend=-0.6, single=True)
s.curly(shift(ip.bond(0, 1), (0.0, 0.12)), mid + [0.05, 0.1], bend=-0.8, single=True)
s.curly(shift(ip.bond(0, 1), (0.0, -0.12)), shift(ip.atom(1), (0.0, -0.3)), bend=-0.8, single=True)
s.text((1.0, y - 2.9), r"$^3$(n,$\pi^*$) + propan-2-ol")
s.arrow((5.4, y), (6.8, y))
s.molecule("O[C](c1ccccc1)c1ccccc1", at=(9.0, y))
s.plus((11.0, y))
s.molecule("C[C](C)O", at=(12.2, y))
s.text((10.4, y - 2.9), "ketyl radical + 2-hydroxy-2-propyl radical")
y2 = -6.0
k1 = s.molecule("O[C](c1ccccc1)c1ccccc1", at=(0.0, y2))
k2 = s.molecule("O[C](c1ccccc1)c1ccccc1", at=(4.8, y2), flip=True)
m = (k1.xy(1) + k2.xy(1)) / 2
s.curly(k1.atom(1), m, bend=-0.4, single=True)
s.curly(k2.atom(1), m, bend=0.4, single=True)
s.text((2.4, y2 - 2.9), "2 ketyl radicals")
s.arrow((7.2, y2), (8.6, y2))
s.molecule("OC(c1ccccc1)(c1ccccc1)C(O)(c1ccccc1)c1ccccc1", at=(11.2, y2))
s.text((11.2, y2 - 3.2), "benzopinacol")
s.draw()
