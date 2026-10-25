#!/usr/bin/env python3
"""Icon library for biology figures: find open-licence SVG icons and convert them for wikibio.

    uv run --with svgelements python scripts/icons.py search mitochondri          # search the catalogues
    uv run --with svgelements python scripts/icons.py add bioicons:Servier/mitochondrium-3 --id servier/mitochondrion
    uv run --with svgelements python scripts/icons.py add phylopic:"Mus musculus" --id phylopic/mouse
    uv run --with svgelements python scripts/icons.py add phylopic:"Pinus#2" --id phylopic/pine     # 2nd allowed image
    uv run --with svgelements python scripts/icons.py list

Specs: bioicons:Category/Author/name, phylopic:"Taxon[#n]", wikimedia:"File name.svg", or svg:<url> with
--license/--author/--page. Templates: `colors ID` lists fill colours, `name ID part=#hex|i-j …` names parts.

Sources (see BIO_FIGURES.md §licences): bioicons.com (Servier Medical Art CC BY 3.0/4.0, DBCLS CC BY 4.0,
CC0 and other CC BY sets; CC BY-SA is refused) and PhyloPic (CC0 / public domain / CC BY only).
Converted icons go to scripts/wiki/plot/icons/<id>.json and are recorded with author, licence and
source URL in icons/manifest.json, from which the site prints attributions under each figure.
"""

import argparse
import fcntl
import json
import os
import re
import sys
import urllib.parse
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_DIR = os.path.join(ROOT, "scripts", "wiki", "plot", "icons")
MANIFEST = os.path.join(ICON_DIR, "manifest.json")
CACHE = os.path.join(ROOT, ".cache", "icons")
BIOICONS_INDEX = "https://bioicons.com/icons/icons.json"
BIOICONS_FILE = "https://bioicons.com/icons/{license}/{category}/{author}/{name}.svg"
PHYLOPIC_API = "https://api.phylopic.org"

# Share-alike is allowed (the figure is then shared under CC BY-SA 4.0, BIO_FIGURES §5); non-commercial
# and no-derivatives licences are refused.
ALLOWED = {
    "cc-0": "CC0 1.0", "cc0": "CC0 1.0", "public-domain": "Public domain", "pd": "Public domain",
    "cc-by-3.0": "CC BY 3.0", "cc-by-4.0": "CC BY 4.0", "cc-by-sa-3.0": "CC BY-SA 3.0", "cc-by-sa-4.0": "CC BY-SA 4.0",
    "mit": "MIT", "bsd": "BSD",
}
WIKIMEDIA_API = "https://commons.wikimedia.org/w/api.php"
LICENSE_URL = {
    "CC0 1.0": "https://creativecommons.org/publicdomain/zero/1.0/",
    "CC BY 3.0": "https://creativecommons.org/licenses/by/3.0/",
    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/",
    "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/",
    "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
    "Public domain": "https://creativecommons.org/publicdomain/mark/1.0/",
}


def fetch(url, binary=False):
    os.makedirs(CACHE, exist_ok=True)
    key = os.path.join(CACHE, re.sub(r"[^\w.-]", "_", url)[-180:])
    if os.path.exists(key) and os.path.getsize(key) > 0:
        with open(key, "rb") as f:
            data = f.read()
    else:
        # Catalogue paths contain spaces and non-ASCII author names ("Helicase 11", "Simon Dürr").
        parts = urllib.parse.urlsplit(url)
        safe = urllib.parse.urlunsplit(parts._replace(path=urllib.parse.quote(urllib.parse.unquote(parts.path))))
        req = urllib.request.Request(safe, headers={"User-Agent": "personal-wiki-site icon tool"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if not data:
            raise SystemExit(f"empty response from {url}; try again later")
        with open(key, "wb") as f:
            f.write(data)
    return data if binary else data.decode("utf-8")


def bioicons_index():
    return json.loads(fetch(BIOICONS_INDEX))


def load_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as f:
            return json.load(f)
    return {}


def save_manifest(m):
    os.makedirs(ICON_DIR, exist_ok=True)
    with open(MANIFEST, "w") as f:
        json.dump(dict(sorted(m.items())), f, indent=1, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------- SVG → JSON


def _flatten_gradients(svg):
    """Replace url(#gradient) paint by the average colour of the gradient stops (flat, BioRender-like)."""
    stops = {}
    for m in re.finditer(r"<(linearGradient|radialGradient)\b([^>]*)>(.*?)</\1>", svg, re.S):
        attrs, body = m.group(2), m.group(3)
        gid = re.search(r'\bid="([^"]+)"', attrs)
        cols = re.findall(r'stop-color[:=]\s*"?\s*(#[0-9a-fA-F]{3,6})', body)
        if gid:
            stops[gid.group(1)] = (cols, re.search(r'xlink:href="#([^"]+)"', attrs))
    for m in re.finditer(r"<(linearGradient|radialGradient)\b([^>]*)/>", svg):
        gid = re.search(r'\bid="([^"]+)"', m.group(2))
        ref = re.search(r'xlink:href="#([^"]+)"', m.group(2))
        if gid:
            stops[gid.group(1)] = ([], ref)

    def colour(gid, depth=0):
        cols, ref = stops.get(gid, ([], None))
        if not cols and ref and depth < 5:
            return colour(ref.group(1), depth + 1)
        if not cols:
            return None
        rgb = [tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) if len(c) == 7 else tuple(int(ch * 2, 16) for ch in c[1:]) for c in cols]
        avg = [round(sum(v[k] for v in rgb) / len(rgb)) for k in range(3)]
        return "#%02x%02x%02x" % tuple(avg)

    def sub(m):
        c = colour(m.group(1))
        return c or "none"

    return re.sub(r"url\(\s*#([^)\s]+)\s*\)", sub, svg)


def _drop_backdrops(items):
    """Remove artboard backgrounds and frames: shapes spanning (nearly) the whole drawing with vertices in
    at least three of its corners (a rectangle, whatever its path commands), filled light or not at all, or
    a rectangular ring (a frame). They show as a light box on the dark theme and pad the bounding box."""
    if len(items) < 2:
        return items
    xs = [v[0] for i in items for v in i["v"]]
    ys = [v[1] for i in items for v in i["v"]]
    X0, X1, Y0, Y1 = min(xs), max(xs), min(ys), max(ys)
    W, H = X1 - X0, Y1 - Y0

    def light(c):
        return c is None or all(int(c[k:k + 2], 16) >= 0xDC for k in (1, 3, 5))

    keep = []
    for it in items:
        vx = [v[0] for v in it["v"]]
        vy = [v[1] for v in it["v"]]
        x0, x1, y0, y1 = min(vx), max(vx), min(vy), max(vy)
        span = (x1 - x0) >= 0.9 * W and (y1 - y0) >= 0.9 * H
        tol = 0.02 * max(x1 - x0, y1 - y0)
        corners = sum(any(abs(a - cx) <= tol and abs(b - cy) <= tol for a, b in it["v"])
                      for cx in (x0, x1) for cy in (y0, y1))
        ring = it["c"].count(1) >= 2
        if span and corners >= 3 and (light(it.get("f")) or ring):
            continue
        keep.append(it)
    return keep


def _keep_dark_fills(items, res=400, band=0.012):
    """Lift solid near-black regions just above the dark-theme ink threshold.

    In the dark theme wikibio and the renderer turn opaque near-black (max channel < 0.22) into the light
    ink colour: right for outlines and line work, wrong for solid dark areas (an instrument's black panel,
    a dark shell), which would turn into light blobs. The drawing is rasterised (``res`` px) to find what
    of each near-black shape is actually visible; if a visible part survives erosion by ``band`` of the
    icon size it is a solid area, and the shape is shifted to a dark grey of the same hue (max channel
    0x3a), which both themes leave alone. Outlines (thin, or an underlay mostly covered by the fills
    above it) stay black and become ink. Coordinates must already be normalised to the 1000-unit box."""
    try:
        import numpy as np
        from PIL import Image, ImageDraw
    except ImportError:  # optional refinement
        return
    dark = []
    for k, it in enumerate(items):
        f = it.get("f")
        if f and it.get("o", 1) >= 0.85 and max(int(f[j:j + 2], 16) for j in (1, 3, 5)) < 0x38:
            dark.append(k)
    if not dark:
        return
    sc = res / 1000.0
    img = Image.new("I", (res + 2, res + 2), -1)
    draw = ImageDraw.Draw(img)
    for k, it in enumerate(items):
        if not it.get("f"):
            continue
        sub = []
        for (x, y), c in zip(it["v"] + [[0, 0]], it["c"] + [1]):
            if c == 1 and len(sub) > 2:
                draw.polygon(sub, fill=k)
            if c == 1:
                sub = []
            sub.append((x * sc, y * sc))
    top = np.asarray(img)
    r = max(1, round(band * res))
    for k in dark:
        m = top == k
        if not m.any():
            continue
        e = m.copy()
        for dx, dy in ((r, 0), (-r, 0), (0, r), (0, -r), (r, r), (-r, -r), (r, -r), (-r, r)):
            e &= np.roll(np.roll(m, dx, 0), dy, 1)
        if e.sum() > 0.05 * m.sum() and e.sum() > 4:
            f = items[k]["f"]
            rgb = [int(f[j:j + 2], 16) for j in (1, 3, 5)]
            d = 0x3a - max(rgb)
            items[k]["f"] = "#%02x%02x%02x" % tuple(v + d for v in rgb)


def _num(x):
    x = round(x, 1)
    return int(x) if x == int(x) else x


# group ids that editors generate (g123, path456, layer1, svg_2…) carry no meaning
_AUTO_ID = re.compile(r"^(g|path|layer|svg|rect|circle|ellipse|polygon|polyline|use|text|tspan|defs|clip|mask|"
                      r"group|shape|object|_x[0-9a-f]+_|[a-z]{0,3})[-_\d.]*$", re.I)


def _part_name(el):
    for key in ("{http://www.inkscape.org/namespaces/inkscape}label", "inkscape:label", "id"):
        v = el.values.get(key) if key != "id" else el.id
        if v and not _AUTO_ID.match(str(v)):
            return re.sub(r"[^a-z0-9]+", "-", str(v).lower()).strip("-")
    return None


def _shapes(node, part=None):
    """Shapes in document order with the name of their innermost named group (the anatomical part)."""
    import svgelements as se

    for child in node:
        if isinstance(child, se.Group):
            yield from _shapes(child, _part_name(child) or part)
        elif isinstance(child, se.Shape) and not isinstance(child, se.Image):
            yield child, _part_name(child) or part


def convert(svg_text, drop=None, keep=None):
    """SVG → {box, items, mono, parts}. Items keep their part name ("p") when the SVG names its groups;
    ``drop`` / ``keep`` are regexes on part names (leave out labels and leader lines, keep one organ…)."""
    import svgelements as se

    svg_text = _flatten_gradients(svg_text)
    import io

    doc = se.SVG.parse(io.StringIO(svg_text), reify=True)
    items = []
    xs, ys = [], []
    for el, part in _shapes(doc):
        if drop and part and re.search(drop, part):
            continue
        if keep and not (part and re.search(keep, part)):
            continue
        if getattr(el, "values", {}).get("visibility") == "hidden" or el.values.get("display") == "none":
            continue
        path = se.Path(el) if not isinstance(el, se.Path) else el
        verts, codes = [], []
        for seg in path:
            if isinstance(seg, se.Move):
                verts.append((seg.end.x, seg.end.y)); codes.append(1)
            elif isinstance(seg, se.Close):
                if verts:
                    verts.append(verts[-1]); codes.append(79)
            elif isinstance(seg, se.Line):
                verts.append((seg.end.x, seg.end.y)); codes.append(2)
            elif isinstance(seg, se.QuadraticBezier):
                verts += [(seg.control.x, seg.control.y), (seg.end.x, seg.end.y)]; codes += [3, 3]
            elif isinstance(seg, se.CubicBezier):
                verts += [(seg.control1.x, seg.control1.y), (seg.control2.x, seg.control2.y), (seg.end.x, seg.end.y)]; codes += [4, 4, 4]
            elif isinstance(seg, se.Arc):
                for cub in seg.as_cubic_curves():
                    verts += [(cub.control1.x, cub.control1.y), (cub.control2.x, cub.control2.y), (cub.end.x, cub.end.y)]; codes += [4, 4, 4]
        if not verts or codes[0] != 1:
            continue
        fill = el.fill if el.fill is not None and el.fill.value is not None and el.fill.alpha > 0 else None
        stroke = el.stroke if el.stroke is not None and el.stroke.value is not None and el.stroke.alpha > 0 else None
        if fill is None and stroke is None:
            continue
        item = {"v": verts, "c": codes}
        if part:
            item["p"] = part
        if fill is not None:
            item["f"] = fill.hex[:7]
        if stroke is not None:
            item["s"] = stroke.hex[:7]
            item["w"] = round(float(el.stroke_width or 1.0), 3)
        op = (fill.opacity if fill is not None else 1.0) * float(el.values.get("opacity", 1) or 1)
        if op < 0.999:
            item["o"] = round(op, 3)
        items.append(item)
        xs += [v[0] for v in verts]
        ys += [v[1] for v in verts]
    items = _drop_backdrops(items)
    if not items:
        raise ValueError("no drawable shapes found in the SVG (embedded raster images are skipped)")
    xs = [v[0] for i in items for v in i["v"]]
    ys = [v[1] for i in items for v in i["v"]]
    # Normalise to a box whose longer side is 1000 units and round to 0.1 unit (0.01 % of the icon):
    # keeps the JSON small without visible loss. Stroke widths scale with the coordinates.
    x0, y0 = min(xs), min(ys)
    k = 1000.0 / max(max(xs) - x0, max(ys) - y0, 1e-9)
    for item in items:
        item["v"] = [[_num((x - x0) * k), _num((y - y0) * k)] for x, y in item["v"]]
        if "w" in item:
            item["w"] = round(item["w"] * k, 2)
    colours = {i.get("f") for i in items if i.get("f")} | {i.get("s") for i in items if i.get("s")}
    if len(colours) > 1:  # silhouettes stay pure black: the dark theme shows them in the ink colour
        _keep_dark_fills(items)
    box = [0, 0, _num((max(xs) - x0) * k), _num((max(ys) - y0) * k)]
    parts = sorted({i["p"] for i in items if "p" in i})
    data = {"box": box, "items": items, "mono": len(colours) <= 1}
    if parts:
        data["parts"] = parts
    return data


# ------------------------------------------------------------------ sources


def resolve_bioicons(spec):
    """spec = "Author/name" or "Category/Author/name"; returns (svg_url, meta)."""
    parts = spec.split("/")
    for e in bioicons_index():
        if e["name"] == parts[-1] and e["author"] == parts[-2] and (len(parts) < 3 or e["category"] == parts[-3]):
            lic = e["license"]
            if lic not in ALLOWED:
                raise SystemExit(f"licence {lic} is not allowed (non-commercial and no-derivatives licences are refused)")
            # bioicons.com serves spaces in catalogue names as underscores ("Helicase 11" → Helicase_11)
            u = {k: e[k].replace(" ", "_") for k in ("category", "author", "name")}
            url = BIOICONS_FILE.format(license=lic, **u)
            author = {"Servier": "Servier Medical Art", "DBCLS": "DBCLS TogoTV"}.get(e["author"], e["author"].replace("-", " "))
            return url, {"source": "bioicons", "name": e["name"], "category": e["category"], "author": author,
                         "license": ALLOWED[lic], "url": url}
    raise SystemExit(f"no bioicons entry {spec!r}; try: scripts/icons.py search {parts[-1]}")


def _phylopic_licence(lic_url):
    if "-nc" in lic_url or "-nd" in lic_url:
        return None
    m = re.search(r"/licenses/(by(?:-sa)?)/(\d\.\d)", lic_url)
    if m:
        return f"CC {m.group(1).upper()} {m.group(2)}"
    return "CC0 1.0" if "zero" in lic_url else "Public domain" if "mark" in lic_url else None


def resolve_phylopic(taxon):
    """taxon = "Mus musculus", optionally "Mus musculus#2" for the 2nd image with an allowed licence.

    The node's primary image is used when its licence is allowed; otherwise (or with #n) the images of
    the node, then of its whole clade, are searched with non-commercial and share-alike licences excluded."""
    taxon, _, nth = taxon.partition("#")
    nth = int(nth or 1)
    build = _phylopic_build()
    q = urllib.parse.quote(taxon.lower())
    data = json.loads(fetch(f"{PHYLOPIC_API}/nodes?build={build}&filter_name={q}&embed_items=true&embed_primaryImage=true&page=0"))
    nodes = data.get("_embedded", {}).get("items", [])
    if not nodes:
        raise SystemExit(f"PhyloPic has no node named {taxon!r}")
    node = nodes[0]
    candidates = []
    img = node.get("_embedded", {}).get("primaryImage")
    if img and _phylopic_licence(img["_links"]["license"]["href"]):
        candidates.append(img)
    uuid = node["_links"]["self"]["href"].split("/")[2].split("?")[0]
    for filt in ("filter_node", "filter_clade"):
        if len(candidates) >= nth:
            break
        try:
            page = json.loads(fetch(f"{PHYLOPIC_API}/images?build={build}&{filt}={uuid}&filter_license_nc=false"
                                    f"&embed_items=true&embed_contributor=true&page=0"))
        except urllib.error.HTTPError as e:  # the API answers 404 when no image matches
            if e.code != 404:
                raise
            continue
        for im in page.get("_embedded", {}).get("items", []):
            if _phylopic_licence(im["_links"]["license"]["href"]) and im["uuid"] not in {c["uuid"] for c in candidates}:
                candidates.append(im)
    if len(candidates) < nth:
        raise SystemExit(f"PhyloPic has no image for {taxon!r} under CC0, public domain or CC BY"
                         + (f" (only {len(candidates)} found)" if candidates else ""))
    img = candidates[nth - 1]
    links = img["_links"]
    lic = _phylopic_licence(links["license"]["href"])
    svg = links["vectorFile"]["href"]
    contributor = img.get("_embedded", {}).get("contributor", {}).get("name") or links.get("contributor", {}).get("title")
    author = img.get("attribution") or contributor or "PhyloPic contributor"
    return svg, {"source": "phylopic", "name": taxon, "author": author, "license": lic,
                 "url": f"https://www.phylopic.org/images/{img['uuid']}"}


def _plain(html_text):
    """Commons metadata fields are HTML: keep the text."""
    t = re.sub(r"<[^>]+>", "", html_text or "")
    return re.sub(r"\s+", " ", urllib.parse.unquote(t).replace("&amp;", "&")).strip()


def _wikimedia_licence(short, url):
    s = (short or "").strip().lower().replace("_", " ")
    if "nc" in s.split() or "-nc" in s or "nd" in s.split() or "-nd" in s:
        return None
    if s.startswith("public domain") or s in ("pd", "pdm") or "pd-" in s:
        return "Public domain"
    if s.startswith("cc0") or s.startswith("cc-zero"):
        return "CC0 1.0"
    m = re.match(r"cc[ -](by(?:-sa)?)[ -](\d\.\d)", s)
    if m:
        return f"CC {m.group(1).upper()} {m.group(2)}"
    return None  # GFDL-only, Free Art, unclear: refused


def resolve_wikimedia(title):
    """title = "Flower anatomy.svg" (with or without "File:"); the file must be an SVG with an allowed licence."""
    title = title if title.startswith("File:") else "File:" + title
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|extmetadata|mime",
                                "format": "json"})
    pages = json.loads(fetch(f"{WIKIMEDIA_API}?{q}"))["query"]["pages"]
    page = next(iter(pages.values()))
    if "imageinfo" not in page:
        raise SystemExit(f"no Commons file {title!r}")
    info = page["imageinfo"][0]
    if info.get("mime") != "image/svg+xml":
        raise SystemExit(f"{title} is {info.get('mime')}, not an SVG")
    md = info.get("extmetadata", {})
    lic = _wikimedia_licence(md.get("LicenseShortName", {}).get("value"), md.get("LicenseUrl", {}).get("value"))
    if lic is None:
        raise SystemExit(f"licence {md.get('LicenseShortName', {}).get('value')!r} of {title} is not allowed")
    author = _plain(md.get("Artist", {}).get("value")) or "Wikimedia Commons contributor"
    return info["url"], {"source": "wikimedia", "name": title[5:], "author": author, "license": lic,
                         "url": info.get("descriptionurl") or info["url"]}


def _phylopic_build():
    req = urllib.request.Request(PHYLOPIC_API + "/", headers={"User-Agent": "personal-wiki-site icon tool"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["build"]


# --------------------------------------------------------------------- CLI


def cmd_search(args):
    q = args.query.lower()
    hits = [e for e in bioicons_index() if q in e["name"].lower() or q in e["category"].lower()]
    for e in hits[: args.limit]:
        ok = "" if e["license"] in ALLOWED else "  [licence not allowed]"
        print(f"bioicons:{e['category']}/{e['author']}/{e['name']}  ({e['license']}){ok}")
    print(f"{len(hits)} bioicons match", file=sys.stderr)


def cmd_add(args):
    src, _, spec = args.spec.partition(":")
    if src == "bioicons":
        url, meta = resolve_bioicons(spec)
    elif src == "phylopic":
        url, meta = resolve_phylopic(spec)
    elif src == "wikimedia":
        url, meta = resolve_wikimedia(spec)
    elif src == "svg":
        # any other library (SciDraw, NIH BioArt, Reactome…): the caller states the licence it read on the page
        lic = args.license
        if lic not in set(ALLOWED.values()) | {"CC BY 2.0", "CC BY 2.5", "CC BY-SA 2.0", "CC BY-SA 2.5"}:
            raise SystemExit("svg: needs --license (e.g. 'CC BY 4.0', 'CC BY-SA 4.0', 'CC0 1.0', 'Public domain')")
        if not args.author or not args.page:
            raise SystemExit("svg: needs --author and --page (the page that states the licence)")
        url = spec
        meta = {"source": args.id.split("/")[0], "name": os.path.basename(urllib.parse.urlsplit(spec).path),
                "author": args.author, "license": lic, "url": args.page}
    else:
        raise SystemExit("spec must start with bioicons:, phylopic:, wikimedia: or svg:")
    data = convert(fetch(url), drop=args.drop, keep=args.keep)
    icon_id = args.id
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*", icon_id):
        raise SystemExit("--id must look like 'servier/mitochondrion' (lower case, one slash)")
    if args.mono is not None:
        data["mono"] = args.mono
    data["id"] = icon_id
    out = os.path.join(ICON_DIR, icon_id + ".json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump(data, f, separators=(",", ":"))
    meta = {**meta, "tags": args.tags.split(",") if args.tags else []}
    # lock the read-modify-write so parallel `add` runs do not drop each other's entries
    with open(MANIFEST + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        m = load_manifest()
        m[icon_id] = meta
        save_manifest(m)
    print(f"added {icon_id}: {len(data['items'])} shapes, {meta['license']}, {meta['author']}")
    if data.get("parts"):
        print(f"  parts: {', '.join(data['parts'])}")
    size = os.path.getsize(out)
    if size > 600_000:
        print(f"  warning: {size // 1000} kB; prefer a simpler drawing or --keep the parts you need", file=sys.stderr)


def _load_icon(icon_id):
    path = os.path.join(ICON_DIR, icon_id + ".json")
    if not os.path.exists(path):
        raise SystemExit(f"no icon {icon_id}")
    with open(path) as f:
        return path, json.load(f)


def cmd_colors(args):
    """List the fill colours of an icon with their item indices and extent: the basis for naming parts."""
    _, data = _load_icon(args.id)
    groups = {}
    for k, it in enumerate(data["items"]):
        groups.setdefault(it.get("f") or ("stroke " + str(it.get("s"))), []).append(k)
    for colour, ks in sorted(groups.items(), key=lambda g: -len(g[1])):
        v = [p for k in ks for p in data["items"][k]["v"]]
        xs, ys = [p[0] for p in v], [p[1] for p in v]
        parts = sorted({data["items"][k].get("p", "") for k in ks} - {""})
        print(f"{colour:16s} {len(ks):4d} items  x {min(xs):6.0f}-{max(xs):6.0f}  y {min(ys):6.0f}-{max(ys):6.0f}  "
              f"items {ks[0]}..{ks[-1]}  {','.join(parts)}")


def cmd_name(args):
    """Assign part names: `name ID petal=#f4a9c4 sepal=#8bc34a stamen=12-30,41` (colours or item ranges)."""
    path, data = _load_icon(args.id)
    for rule in args.rules:
        name, _, sel = rule.partition("=")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            raise SystemExit(f"part names are lower case with hyphens: {name!r}")
        idx = set()
        for term in sel.split(","):
            if term.startswith("#"):
                idx |= {k for k, it in enumerate(data["items"]) if (it.get("f") or "").lower() == term.lower()}
            elif "-" in term:
                a, b = map(int, term.split("-"))
                idx |= set(range(a, b + 1))
            elif term:
                idx.add(int(term))
        for k in idx:
            data["items"][k]["p"] = name
        print(f"{name}: {len(idx)} items")
    data["parts"] = sorted({i["p"] for i in data["items"] if "p" in i})
    with open(path, "w") as f:
        json.dump(data, f, separators=(",", ":"))


def cmd_list(_args):
    for k, v in load_manifest().items():
        print(f"{k:40s} {v['license']:10s} {v['author']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--limit", type=int, default=40); s.set_defaults(fn=cmd_search)
    a = sub.add_parser("add"); a.add_argument("spec"); a.add_argument("--id", required=True); a.add_argument("--tags", default="")
    a.add_argument("--drop", default=None, help="regex: leave out parts whose name matches (labels, leader lines)")
    a.add_argument("--keep", default=None, help="regex: keep only parts whose name matches")
    a.add_argument("--license", default=None, help="svg: sources only: licence stated on --page")
    a.add_argument("--author", default=None, help="svg: sources only")
    a.add_argument("--page", default=None, help="svg: sources only: page that states author and licence")
    a.add_argument("--mono", type=lambda v: v.lower() in ("1", "true", "yes"), default=None); a.set_defaults(fn=cmd_add)
    l = sub.add_parser("list"); l.set_defaults(fn=cmd_list)
    c = sub.add_parser("colors"); c.add_argument("id"); c.set_defaults(fn=cmd_colors)
    n = sub.add_parser("name"); n.add_argument("id"); n.add_argument("rules", nargs="+"); n.set_defaults(fn=cmd_name)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
