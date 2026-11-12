# Discontinuous growth of a crustacean (schematic model, illustrative parameters). Body length increases
# only at molts and stays constant between them. The size after a molt is a linear function of the size
# before it (a Hiatt growth diagram): L' = a + b L, here a = 1.2 mm, b = 1.05, so the relative molt
# increment falls from over 50 % in the smallest juveniles toward 5 % in large animals; the intermolt period
# lengthens with size, T = c L^k (c = 3 d, k = 1.1). A constant ratio L'/L (Brooks' rule, b > 1, a = 0)
# would give geometric growth; the dashed line is the smooth envelope through the post-molt sizes.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 9)
a, b, c, k = 1.2, 1.05, 3.0, 1.1
L, t = [2.0], [0.0]
while t[-1] < 400:
    T = c * L[-1] ** k
    t.append(t[-1] + T)
    L.append(a + b * L[-1])
L, t = np.array(L), np.array(t)
p = quant.Plot(ax, (1.6, 1.4, 12.0, 6.8), xlim=(0, 400), ylim=(0, 25), xlabel="Age / d", ylabel="Body length / mm",
               xticks=[0, 100, 200, 300, 400], yticks=[0, 5, 10, 15, 20, 25])
xs, ys = [], []
for i in range(len(L) - 1):
    xs += [t[i], t[i + 1]]
    ys += [L[i], L[i]]
xs, ys = np.array(xs), np.array(ys)
m = xs <= 400
p.line(xs[m], ys[m], "dna", lw=1.8)
p.line(t[t <= 400], L[t <= 400], "muted", dashed=True)
bio.label(ax, p.xy(40, 21), "Size constant between molts;\njump at each molt", size="small", ha="left")
# Hiatt diagram
q = quant.Plot(ax, (16.2, 1.4, 6.8, 6.8), xlim=(0, 40), ylim=(0, 40), xlabel="Pre-molt length / mm",
               ylabel="Post-molt length / mm", xticks=[0, 20, 40], yticks=[0, 20, 40])
x = np.linspace(0, 38, 50)
q.line(x, x, "muted", dashed=True)
q.line(x, a + b * x, "rna")
q.points(L[:-1][L[:-1] < 38], L[1:][L[:-1] < 38], "rna", r=0.08)
bio.label(ax, q.xy(4, 36), "Hiatt diagram:\nL' = a + bL", size="small", ha="left")
bio.label(ax, q.xy(26, 18), "no growth\n(L' = L)", size="tiny", color=P.muted())
