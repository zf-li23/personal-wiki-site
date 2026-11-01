"""Marker-controlled watershed segmentation of a synthetic nuclear stain. A: 'DAPI' image of 40
nuclei (disks of radius 5-9 px, many touching) with blur and noise. B: thresholding and connected
components merge touching nuclei into one object. C: the Euclidean distance transform of the
foreground; its local maxima (crosses) are the markers, one per nucleus. D: flooding the inverted
distance from the markers splits the clumps along the necks. Objects are matched to the true
nuclei at intersection over union (IoU) >= 0.5; precision, recall and F1 are given above B and D."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy import ndimage as ndi
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
H = W = 160
yy, xx = np.mgrid[0:H, 0:W]

# place nuclei with small overlaps allowed (touching clumps)
centers, radii = [], []
while len(centers) < 40:
    c = rng.uniform(10, H - 10, 2)
    r = rng.uniform(5, 9)
    ok = all(np.hypot(*(c - c2)) > 0.88 * (r + r2) for c2, r2 in zip(centers, radii))
    near = len(centers) == 0 or min(np.hypot(*(c - c2)) - r - r2 for c2, r2 in zip(centers, radii)) < 4
    if ok and (near or rng.random() < 0.25):
        centers.append(c)
        radii.append(r)
truth = np.zeros((H, W), int)
dist_to = np.full((H, W), np.inf)
for k, (c, r) in enumerate(zip(centers, radii), start=1):
    d = np.hypot(yy - c[0], xx - c[1]) / r
    inside = (d < 1) & (d < dist_to)
    truth[inside] = k
    dist_to[inside] = d[inside]
img = ndi.gaussian_filter((truth > 0).astype(float), 1.2) * rng.uniform(0.7, 1.0, 41)[truth]
img = img + rng.normal(0, 0.06, img.shape)

mask = ndi.gaussian_filter(img, 1.0) > 0.4
mask = ndi.binary_fill_holes(mask)
cc, ncc = ndi.label(mask)

dist = ndi.distance_transform_edt(mask)
smooth = ndi.gaussian_filter(dist, 1.0)
peaks = (smooth == ndi.maximum_filter(smooth, size=9)) & (smooth > 2.5)
markers, nm = ndi.label(peaks)


def watershed(elev, markers, mask):
    """Priority-flood watershed: grow the markers in order of increasing elevation (4-connectivity)."""
    import heapq
    lab = markers.copy()
    heap = [(elev[y, x], y, x) for y, x in zip(*np.nonzero(lab))]
    heapq.heapify(heap)
    while heap:
        _, y, x = heapq.heappop(heap)
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v, u = y + dy, x + dx
            if 0 <= v < H and 0 <= u < W and mask[v, u] and lab[v, u] == 0:
                lab[v, u] = lab[y, x]
                heapq.heappush(heap, (elev[v, u], v, u))
    return lab


ws = watershed(-smooth, markers, mask)


def match(pred, truth, thr=0.5):
    tp = 0
    for k in range(1, truth.max() + 1):
        t = truth == k
        labs, cnt = np.unique(pred[t], return_counts=True)
        for lab, c in zip(labs, cnt):
            if lab == 0:
                continue
            union = t.sum() + (pred == lab).sum() - c
            if c / union >= thr:
                tp += 1
                break
    npred = len(np.unique(pred[pred > 0]))
    prec, rec = tp / npred, tp / truth.max()
    return tp, npred, prec, rec, 2 * prec * rec / (prec + rec)


m_cc = match(cc, truth)
m_ws = match(ws, truth)
RESULT = {"components": m_cc, "watershed": m_ws, "markers": nm}

cols = [P.fill(t) for t in ("dna", "rna", "enzyme", "protein", "receptor", "antibody", "carbohydrate", "channel")]


def lab_cmap(lab):
    """Colour labels greedily so that touching objects get different colours."""
    n = lab.max()
    adj = {k: set() for k in range(1, n + 1)}
    for a, b in ((lab[1:, :], lab[:-1, :]), (lab[:, 1:], lab[:, :-1])):
        m = (a != b) & (a > 0) & (b > 0)
        for u, v in zip(a[m], b[m]):
            adj[u].add(v)
            adj[v].add(u)
    colour = {}
    for k in range(1, n + 1):
        used = {colour.get(j) for j in adj[k]}
        colour[k] = next(c for c in range((k * 3) % len(cols), (k * 3) % len(cols) + 2 * len(cols)) if c % len(cols) not in used) % len(cols)
    return ListedColormap([(0, 0, 0, 0)] + [cols[colour[k]] for k in range(1, n + 1)])


fig, axs = plt.subplots(1, 4, figsize=(11.6, 3.3))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.84, wspace=0.05)
axs[0].imshow(img, cmap="gray", vmin=0, vmax=1)
charts.title(axs[0], "A  Nuclear stain")
axs[1].imshow(cc, cmap=lab_cmap(cc), interpolation="nearest")
charts.title(axs[1], f"B  Threshold: {m_cc[1]} objects, F1 = {m_cc[4]:.2f}")
axs[2].imshow(smooth, cmap="magma")
py, px = np.nonzero(peaks)
axs[2].plot(px, py, "x", color=P.fill("dna"), ms=4, mew=1.2)
charts.title(axs[2], f"C  Distance transform, {nm} markers")
axs[3].imshow(ws, cmap=lab_cmap(ws), interpolation="nearest")
charts.title(axs[3], f"D  Watershed: {m_ws[1]} objects, F1 = {m_ws[4]:.2f}")
for a in axs:
    a.set_xticks([])
    a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color(P.muted())
