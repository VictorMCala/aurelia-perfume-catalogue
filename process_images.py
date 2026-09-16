"""
AURELIA - Notino bottle image pipeline
  download CDN image -> cut out white background -> feather -> autocrop -> pad -> save PNG
Fill CDN with the direct cdn.notinoimg.com URLs (detail_main_mq preferred).
Run:  python process_images.py
"""
import io, os, urllib.request
from collections import deque
from PIL import Image, ImageDraw, ImageFilter

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "images")
os.makedirs(OUT, exist_ok=True)

# name (matches catalogue <img src>) -> direct CDN image URL
# Paste the detail_main_mq/uhq URL for each. Empty entries fall back to artwork.
# Keys starting with "x-" are staged cut-outs with no matching page yet.
CDN = {
    "black-opium":       "https://cdn.notinoimg.com/detail_main_mq/yves-saint-laurent/3365440787971_01-o/black-opium___260721.jpg",
    "libre":             "https://cdn.notinoimg.com/detail_main_uhq/yves-saint-laurent/3614272648425_1-o/libre___190827.jpg",
    "paradoxe":          "https://cdn.notinoimg.com/detail_main_uhq/prada/3614273961707_01-o/paradoxe-intense___230825.jpg",
    "la-vie-est-belle":  "https://cdn.notinoimg.com/detail_main_mq/lancome/3605533286555_01-o/la-vie-est-belle___250312.jpg",
    "valentino-vendetta":"https://cdn.notinoimg.com/detail_main_mq/valentino/3614274798319_01-o/vendetta-donna___260716.jpg",
    "miss-dior":         "https://cdn.notinoimg.com/detail_main_uhq/dior/3348901708920_01/miss-dior___240131.jpg",
    "armani-power-of-you":"https://cdn.notinoimg.com/detail_main_mq/armani/3614274752717_01-o/power-of-you___260112.jpg",
    # --- latest batch ---
    "crystal-noir":      "https://cdn.notinoimg.com/detail_main_uhq/versace/8018365070462_01-o/crystal-noir___241108.jpg",
    "good-girl-blush":   "https://cdn.notinoimg.com/detail_main_uhq/carolina-herrera/8411061056752_01-o/good-girl-blush___231107.jpg",
    "sharaf-blend":      "https://cdn.notinoimg.com/detail_main_uhq/zimaya/6290171074205_01-o/sharaf-blend___231204.jpg",
    "hawas-ice":         "https://cdn.notinoimg.com/detail_main_uhq/rasasi/614514331040_01-o/hawas-ice___240509.jpg",
    "paradigme":         "https://cdn.notinoimg.com/detail_main_uhq/prada/3614274182897_01-o/paradigme___250708.jpg",
    "le-male-le-parfum": "https://cdn.notinoimg.com/detail_main_uhq/jean-paul-gaultier/8435415032278_01-o/le-male-le-parfum___200617.jpg",
    "born-in-roma-uomo": "https://cdn.notinoimg.com/detail_main_uhq/valentino/2800021659984_01-o/born-in-roma-uomo-set___260629.jpg",
}


def download(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def cut_white(img, thresh=36, feather=0.8):
    """Make the contiguous white studio background transparent (keeps white inside the bottle)."""
    w, h = img.size
    rgb = img.copy()
    seed = (255, 0, 255)  # sentinel colour not present in product photos
    # seed along every edge so reflections touching the bottom edge are removed too
    pts = []
    for t in range(0, 21):
        f = t / 20
        pts += [(int(f * (w - 1)), 0), (int(f * (w - 1)), h - 1),
                (0, int(f * (h - 1))), (w - 1, int(f * (h - 1)))]
    for p in pts:
        if rgb.getpixel(p) != seed:
            ImageDraw.floodfill(rgb, p, seed, thresh=thresh)
    rgba = img.convert("RGBA")
    sp = rgb.load()
    ap = rgba.load()
    for y in range(h):
        for x in range(w):
            if sp[x, y] == seed:
                r, g, b, _ = ap[x, y]
                ap[x, y] = (r, g, b, 0)
    # soften the cut edge
    alpha = rgba.split()[3].filter(ImageFilter.GaussianBlur(feather))
    rgba.putalpha(alpha)
    return rgba


def trim_reflection(im, lo_frac=0.58, hi_frac=0.96, min_jump=20, k=3, max_crop=0.32):
    """Crop the mirrored reflection at the floor line (row of sharpest brightness change)."""
    w, h = im.size
    px = im.convert("RGBA").load()
    bright = [None] * h
    cov = [0.0] * h
    for y in range(h):
        s = n = 0
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 24:
                s += (r + g + b) / 3
                n += 1
        cov[y] = n / w
        bright[y] = (s / n) if n else None
    lo, hi = int(h * lo_frac), int(h * hi_frac)
    best, best_grad = None, 0.0
    for y in range(lo, hi):
        if bright[y - k] is None or bright[y + k] is None:
            continue
        if cov[y] < 0.30:
            continue
        grad = abs(bright[y + k] - bright[y - k])
        if grad > best_grad:
            best_grad, best = grad, y
    if best is not None and best_grad >= min_jump and (h - best) <= max_crop * h:
        return im.crop((0, 0, w, max(1, best - 2)))
    return im


def autocrop(im, pad_ratio=0.05):
    bbox = im.split()[3].getbbox()
    if bbox:
        im = im.crop(bbox)
    w, h = im.size
    pad = int(max(w, h) * pad_ratio)
    canvas = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    canvas.paste(im, (pad, pad), im)
    return canvas


def despeckle(im, keep_frac=0.03):
    """Keep only the large object blobs (bottle/box); drop stray leftover noise."""
    import numpy as np
    from scipy import ndimage
    arr = np.array(im)
    mask = arr[:, :, 3] > 40
    lbl, n = ndimage.label(mask)
    if n <= 1:
        return im
    sizes = ndimage.sum(np.ones_like(lbl, dtype=np.uint8), lbl, range(1, n + 1))
    keep = {i + 1 for i, s in enumerate(sizes) if s >= keep_frac * sizes.max()}
    arr[:, :, 3] = np.where(np.isin(lbl, list(keep)), arr[:, :, 3], 0)
    return Image.fromarray(arr, "RGBA")


_SESSION = None

def matte(img):
    """AI foreground cut-out (ISNet). Conservative mask keeps whole glass bottles,
    while excluding the mirrored floor reflection."""
    global _SESSION
    from rembg import remove, new_session
    if _SESSION is None:
        _SESSION = new_session("isnet-general-use")
    out = remove(img.convert("RGB"), session=_SESSION, post_process_mask=True).convert("RGBA")
    # binarise soft haze: keep confident foreground, drop faint reflection ghosts
    px = out.load()
    w, h = out.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 90:
                px[x, y] = (r, g, b, 0)
    return out


def process(name, url):
    try:
        img = download(url)
    except Exception as e:
        print(f"FAIL  {name}  download: {e}")
        return False
    if img.height > 1200:  # keep processing fast; plenty for print at bottle size
        img = img.resize((round(img.width * 1200 / img.height), 1200), Image.LANCZOS)
    cut = cut_white(img)             # flood-fill white studio bg (keeps whole glass bottles)
    cut = despeckle(cut)             # drop small stray blobs (leftover text/box noise)
    cut = trim_reflection(cut)       # crop the mirrored floor reflection
    out = autocrop(cut)
    path = os.path.join(OUT, f"{name}.png")
    out.save(path)
    print(f"ok    {name}  ->  {out.size[0]}x{out.size[1]}  {os.path.basename(path)}")
    return True


if __name__ == "__main__":
    done = 0
    for name, url in CDN.items():
        if url and "cdn.notinoimg.com" in url:
            done += process(name, url)
        else:
            print(f"skip  {name} (no URL)")
    print(f"\nProcessed {done} image(s). Missing ones fall back to the drawn flacon automatically.")
