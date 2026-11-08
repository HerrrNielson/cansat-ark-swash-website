"""Foto der Woche: Instagram-Post und Website aus einer Datenquelle.

Ablauf jede Woche (Details in social/DESIGN-FOTO-DER-WOCHE.md):
    1. Bilder nach social/fotos/ legen, z. B. 2026-kw46.jpg und 2026-kw46-2.jpg
    2. Neuen Eintrag oben in social/wochenfotos.json ergänzen
    3. python social/foto_der_woche.py

Ergebnis für die neueste Woche (oder --kw/--jahr):
    social/posts/<jahr>-kw<kw>-1.png, -2.png …  Instagram-Karussell, 1080 x 1350
    social/posts/<jahr>-kw<kw>.txt              Bildunterschrift mit Hashtags
Und für alle Wochen:
    assets/wochenfoto/<jahr>-kw<kw>.jpg         Website-Bild (erstes Bild, 4:3)
    index.html, foto-der-woche.html             Blöcke zwischen den WOCHENFOTO-/ARCHIV-Markierungen
    assets/translations.js                      englische Texte zwischen den WOCHENFOTO-Markierungen

Braucht Python 3 mit Pillow und die Windows-Schriften Bahnschrift und Segoe UI.
"""

import argparse
import html
import json
import re
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "social/wochenfotos.json"
FONTS = Path("C:/Windows/Fonts")

# Markenfarben aus DESIGN.md (--logo-*), keine anderen Farben verwenden
NAVY = (11, 31, 58)
ORANGE = (255, 107, 26)
PURPLE = (77, 16, 86)
LIGHT = (245, 247, 250)
GRAY = (169, 180, 194)
DOTS = [(44, 85, 162), (181, 33, 58), (199, 114, 20), (42, 138, 58)]

HASHTAGS = "#TeamSWASH #CanSat #CanSatAustria #ESEROAustria #HTLKaindorf #Raumfahrt #Technik"

W, H = 1080, 1350
M = 72  # Außenrand
PHOTO_W = W - 2 * M
PHOTO_H = PHOTO_W * 3 // 4
PHOTO_Y = 236
SHADOW = 14


# ---------- Bild ----------

def display_font(size, weight="Bold"):
    font = ImageFont.truetype(str(FONTS / "bahnschrift.ttf"), size)
    font.set_variation_by_name(weight)
    return font


def body_font(size):
    return ImageFont.truetype(str(FONTS / "segoeui.ttf"), size)


def spaced_text(draw, xy, text, font, fill, tracking):
    """Text mit Sperrung (tracking in Pixeln), wie die Labels auf der Website."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x


def spaced_width(draw, text, font, tracking):
    return sum(draw.textlength(ch, font=font) for ch in text) + tracking * (len(text) - 1)


def wrap_px(draw, text, font, max_width, max_lines, what):
    """Bricht nach Pixelbreite um; bricht ab statt still abzuschneiden."""
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        raise SystemExit(f"{what} ist zu lang: {len(lines)} Zeilen, erlaubt sind {max_lines}. Bitte kürzen.")
    return lines


def crop_4_3(img, box=None):
    """Schneidet 4:3 zu. Ohne box: Motiv vor glattem Hintergrund suchen, sonst mittig."""
    w, h = img.size
    if box:
        x, y, bw, bh = box
    else:
        bg = Image.new("RGB", img.size, img.getpixel((4, 4)))
        diff = ImageChops.difference(img, bg).convert("L").point(lambda v: 255 if v > 28 else 0)
        diff = diff.filter(ImageFilter.MedianFilter(5))
        found = diff.getbbox()
        if found and (found[2] - found[0]) * (found[3] - found[1]) < 0.8 * w * h:
            x0, y0, x1, y1 = found
            pad = 0.09 * max(x1 - x0, y1 - y0)
            x, y, bw, bh = x0 - pad, y0 - pad, x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
        else:
            x, y, bw, bh = 0, 0, w, h
    cx, cy = x + bw / 2, y + bh / 2
    if bw / bh > 4 / 3:
        bh = bw * 3 / 4
    else:
        bw = bh * 4 / 3
    bw, bh = min(bw, w, h * 4 / 3), min(bh, h, w * 3 / 4)
    x0 = min(max(cx - bw / 2, 0), w - bw)
    y0 = min(max(cy - bh / 2, 0), h - bh)
    return img.crop((round(x0), round(y0), round(x0 + bw), round(y0 + bh)))


def rounded_mask(size, radius=10):
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def dashed_rect(draw, box, color, dash=14, gap=10, width=3):
    x0, y0, x1, y1 = box
    for sx, sy, ex, ey in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x0, y1, x1, y1), (x0, y0, x0, y1)):
        length = abs(ex - sx) + abs(ey - sy)
        pos = 0
        while pos < length:
            end = min(pos + dash, length)
            if sx == ex:
                draw.line((sx, sy + pos, sx, sy + end), fill=color, width=width)
            else:
                draw.line((sx + pos, sy, sx + end, sy), fill=color, width=width)
            pos += dash + gap


def grain(img, strength=3):
    """Feine Papierkörnung wie auf der Website, nur für den Hintergrund."""
    noise = Image.effect_noise(img.size, 40).point(lambda v: 128 + (v - 128) * strength // 40)
    return ImageChops.add(img, Image.merge("RGB", (noise, noise, noise)), 1, -128)


def build_slide(photo, kw, jahr, titel, text, page=None):
    post = grain(Image.new("RGB", (W, H), NAVY))
    d = ImageDraw.Draw(post, "RGBA")

    # Orange Kante oben, wie die Header-Unterkante der Website
    d.rectangle((0, 0, W, 8), fill=ORANGE)

    # Kopfzeile: Label links, Logo rechts
    spaced_text(d, (M, 78), "FOTO DER WOCHE", display_font(30, "Bold"), ORANGE, 6)
    spaced_text(d, (M, 124), f"KW {kw} · {jahr}", display_font(30, "SemiBold"), LIGHT, 5)
    logo = Image.open(ROOT / "assets/swash-logo.png").convert("RGBA").resize((128, 128), Image.LANCZOS)
    d.ellipse((W - M - 134, 58, W - M + 6, 198), outline=ORANGE, width=2)
    post.paste(logo, (W - M - 128, 64), logo)

    # Foto mit hartem Schatten (Lila), gestricheltem Innenrahmen und Klebeband
    x0, y0 = M, PHOTO_Y
    d.rounded_rectangle((x0 + SHADOW, y0 + SHADOW, x0 + PHOTO_W + SHADOW, y0 + PHOTO_H + SHADOW), radius=10, fill=PURPLE)
    pic = photo.resize((PHOTO_W, PHOTO_H), Image.LANCZOS)
    post.paste(pic, (x0, y0), rounded_mask(pic.size))
    d = ImageDraw.Draw(post, "RGBA")
    dashed_rect(d, (x0 + 14, y0 + 14, x0 + PHOTO_W - 14, y0 + PHOTO_H - 14), (245, 247, 250, 115))
    tape = Image.new("RGBA", (190, 46), (0, 0, 0, 0))
    ImageDraw.Draw(tape).polygon([(4, 4), (186, 0), (190, 40), (182, 46), (8, 43), (0, 8)], fill=ORANGE + (210,))
    tape = tape.rotate(4, expand=True, resample=Image.BICUBIC)
    post.paste(tape, (W // 2 - tape.width // 2, y0 - 24), tape)

    # Titel und Text
    ty = y0 + PHOTO_H + SHADOW + 44
    title_font = display_font(64, "Bold")
    for line in wrap_px(d, titel, title_font, W - 2 * M, 2, "Titel"):
        d.text((M, ty), line, font=title_font, fill=LIGHT)
        ty += 70
    ty += 10
    bf = body_font(29)
    for line in wrap_px(d, text, bf, W - 2 * M, 3, "Text"):
        d.text((M, ty), line, font=bf, fill=GRAY)
        ty += 41

    # Fußzeile: Website links, Seitenzahl und Signalpunkte rechts
    fy = H - M - 22
    small = display_font(24, "SemiBold")
    spaced_text(d, (M, fy - 4), "CANSAT-SWASH.ORG", small, GRAY, 5)
    dots_left = W - M - 12 - 3 * 30 - 10
    for i, c in enumerate(DOTS):
        cx = W - M - 12 - (3 - i) * 30
        d.ellipse((cx - 10, fy + 2, cx + 10, fy + 22), fill=c)
    if page:
        label = f"{page[0]} / {page[1]}"
        spaced_text(d, (dots_left - 28 - spaced_width(d, label, small, 4), fy - 4), label, small, LIGHT, 4)
    return post


# ---------- Daten ----------

def name_of(e):
    return f"{e['jahr']}-kw{e['kw']:02d}"


def load_entries():
    entries = json.loads(DATA.read_text(encoding="utf-8"))
    for e in entries:
        for key in ("jahr", "kw", "bilder", "titel", "text", "alt", "titel_en", "text_en", "alt_en"):
            if not e.get(key):
                raise SystemExit(f"KW {e.get('kw')}: Feld '{key}' fehlt in {DATA.name}.")
    return sorted(entries, key=lambda e: (e["jahr"], e["kw"]), reverse=True)


def open_cropped(e, i):
    boxes = e.get("ausschnitte") or []
    box = boxes[i] if i < len(boxes) and boxes[i] else None
    if isinstance(box, str):
        box = tuple(int(v) for v in box.split(","))
    return crop_4_3(Image.open(ROOT / e["bilder"][i]).convert("RGB"), box)


def web_image(e):
    path = ROOT / "assets/wochenfoto" / f"{name_of(e)}.jpg"
    photo = open_cropped(e, 0)
    if photo.width > 1600:
        photo = photo.resize((1600, 1200), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    photo.save(path, quality=86, optimize=True, progressive=True)
    return path, photo.size


def build_instagram(e):
    out = ROOT / "social/posts"
    out.mkdir(parents=True, exist_ok=True)
    missing = [b for b in e["bilder"][1:] if not (ROOT / b).exists()]
    for b in missing:
        print(f"WARNUNG: {b} fehlt, diese Folie wird ausgelassen.")
    images = [i for i, b in enumerate(e["bilder"]) if i == 0 or b not in missing]
    n = len(images)
    subs = e.get("unterschriften") or []
    files = []
    for slot, i in enumerate(images):
        text = e["text"] if i == 0 else (subs[i - 1] if i - 1 < len(subs) else "")
        slide = build_slide(open_cropped(e, i), e["kw"], e["jahr"], e["titel"], text, (slot + 1, n) if n > 1 else None)
        path = out / f"{name_of(e)}-{slot + 1}.png"
        slide.save(path, optimize=True)
        files.append(path)
    caption = (
        f"Foto der Woche · KW {e['kw']}\n{e['titel']}\n\n{e['text']}\n\n"
        f"Alle Wochenfotos auf unserer Website, Link in der Bio.\n\n{HASHTAGS}\n"
    )
    cap_path = out / f"{name_of(e)}.txt"
    cap_path.write_text(caption, encoding="utf-8")
    return files, cap_path


# ---------- Website ----------

def esc(text):
    return html.escape(text, quote=True)


def replace_block(path, start, end, content):
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(rf"([ \t]*{re.escape(start)}\n).*?([ \t]*{re.escape(end)})", re.S)
    if not pattern.search(text):
        raise SystemExit(f"Markierung {start} fehlt in {path.name}.")
    text = pattern.sub(lambda m: m.group(1) + content + m.group(2), text, count=1)
    path.write_text(text, encoding="utf-8", newline="")


def update_website(entries, sizes):
    latest = entries[0]
    w, h = sizes[name_of(latest)]
    ind = " " * 10
    home = (
        f'{ind}<a class="weekly-link" href="foto-der-woche.html">\n'
        f'{ind}  <figure class="mission-image weekly-photo">\n'
        f'{ind}    <div class="mission-image-frame"><img src="assets/wochenfoto/{name_of(latest)}.jpg" alt="{esc(latest["alt"])}" width="{w}" height="{h}"></div>\n'
        f'{ind}    <figcaption><strong class="weekly-label">Foto der Woche · KW {latest["kw"]}</strong> {esc(latest["titel"])}<span class="weekly-more">Alle Wochenfotos</span></figcaption>\n'
        f'{ind}  </figure>\n'
        f'{ind}</a>\n'
    )
    replace_block(ROOT / "index.html", "<!-- WOCHENFOTO:START -->", "<!-- WOCHENFOTO:END -->", home)

    items = []
    for i, e in enumerate(entries):
        w, h = sizes[name_of(e)]
        lazy = "" if i == 0 else ' loading="lazy"'
        items.append(
            f'{ind}<article class="weekly-entry" id="{name_of(e)}">\n'
            f'{ind}  <figure class="mission-image weekly-photo">\n'
            f'{ind}    <div class="mission-image-frame"><img src="assets/wochenfoto/{name_of(e)}.jpg" alt="{esc(e["alt"])}" width="{w}" height="{h}"{lazy}></div>\n'
            f'{ind}  </figure>\n'
            f'{ind}  <div class="weekly-entry-text">\n'
            f'{ind}    <p class="eyebrow">KW {e["kw"]} · {e["jahr"]}</p>\n'
            f'{ind}    <h2>{esc(e["titel"])}</h2>\n'
            f'{ind}    <p>{esc(e["text"])}</p>\n'
            f'{ind}  </div>\n'
            f'{ind}</article>\n'
        )
    replace_block(ROOT / "foto-der-woche.html", "<!-- ARCHIV:START -->", "<!-- ARCHIV:END -->", "".join(items))

    pairs = {}
    for e in entries:
        pairs[f"Foto der Woche · KW {e['kw']}"] = f"Photo of the week · Week {e['kw']}"
        pairs[f"KW {e['kw']} · {e['jahr']}"] = f"Week {e['kw']} · {e['jahr']}"
        pairs[e["titel"]] = e["titel_en"]
        pairs[e["text"]] = e["text_en"]
        pairs[e["alt"]] = e["alt_en"]
    lines = "".join(f"  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},\n" for k, v in pairs.items())
    replace_block(ROOT / "assets/translations.js", "// WOCHENFOTO:START", "// WOCHENFOTO:END", lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kw", type=int, help="Woche für den Instagram-Post (Standard: neueste)")
    ap.add_argument("--jahr", type=int)
    ap.add_argument("--nur-instagram", action="store_true", help="Website nicht anfassen")
    args = ap.parse_args()

    entries = load_entries()
    target = entries[0]
    if args.kw:
        match = [e for e in entries if e["kw"] == args.kw and (not args.jahr or e["jahr"] == args.jahr)]
        if not match:
            raise SystemExit(f"KW {args.kw} steht nicht in {DATA.name}.")
        target = match[0]

    files, caption = build_instagram(target)
    print(f"Instagram KW {target['kw']}: " + ", ".join(str(f.relative_to(ROOT)) for f in files))
    print(f"Bildunterschrift:  {caption.relative_to(ROOT)}")

    if not args.nur_instagram:
        sizes = {}
        for e in entries:
            _, size = web_image(e)
            sizes[name_of(e)] = size
        update_website(entries, sizes)
        print(f"Website: {len(entries)} Wochenfoto(s), Startseite zeigt KW {entries[0]['kw']}")


if __name__ == "__main__":
    main()
