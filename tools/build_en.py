"""Erzeugt die englischen Seiten unter en/ aus den deutschen Seiten.

    python tools/build_en.py

Quelle der Übersetzungen ist assets/translations.js (deutscher Text -> englischer Text,
Leerräume werden beim Nachschlagen zusammengefasst). Das Skript

- übersetzt Texte, alt/aria-label/title/placeholder, <title> und die Meta-Beschreibungen,
- stellt interne Links auf /en/… um und macht relative Pfade (assets/…) absolut,
- setzt lang="en", Canonical, og:url und og:locale,
- trägt in beide Sprachversionen hreflang-Verweise ein (de-AT, en, x-default),
- schreibt die Sitemap mit beiden Sprachen neu.

Fehlt eine Übersetzung, bleibt der deutsche Text stehen und das Skript listet ihn auf
(Rückgabewert 1). Dann den Text in assets/translations.js ergänzen und neu starten.
Braucht Node.js (liest translations.js).
"""

import html
import json
import re
import subprocess
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://cansat-swash.org"
PAGES = ["index", "ueber-uns", "team", "flugergebnisse", "simulation", "foto-der-woche",
         "news", "unterstuetzen", "kontakt", "impressum", "datenschutz"]
TRANSLATED_ATTRS = {"alt", "aria-label", "title", "placeholder"}
META_TRANSLATED = {"description", "og:title", "og:description", "og:image:alt"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
# Texte, die in beiden Sprachen gleich sind (Namen, Zahlen, Marken)
SAME = re.compile(r"^[\d\s.,:;/%°·–—()+\-@#&→↗›☰☾☼✦|]*$|^(Team SWASH|CanSat|Instagram|E-Mail:?|Home|Team)$")


def load_translations():
    js = (ROOT / "assets/translations.js").read_text(encoding="utf-8")
    script = "const window={};" + js + ";process.stdout.write(JSON.stringify(window.swashTranslations))"
    out = subprocess.run(["node"], input=script, capture_output=True, text=True, encoding="utf-8",
                         check=True).stdout
    return {norm(k): v for k, v in json.loads(out).items()}


def norm(text):
    return " ".join(text.split())


def page_url(name, lang):
    slug = "" if name == "index" else name
    return f"{SITE}/{slug}" if lang == "de" else f"{SITE}/en/{slug}"


def en_href(value):
    """Interne Seitenlinks auf die englische Version umbiegen, relative Pfade absolut machen."""
    if value.startswith(("assets/", "favicon")):
        return "/" + value
    m = re.fullmatch(r"/([a-z-]*)(#.*)?", value)
    if m and (m.group(1) in PAGES or m.group(1) == ""):
        slug = "" if m.group(1) in ("", "index") else m.group(1)
        return f"/en/{slug}" + (m.group(2) or "")
    return value


class Translator(HTMLParser):
    def __init__(self, tr, name):
        super().__init__(convert_charrefs=True)
        self.tr, self.name = tr, name
        self.out, self.missing = [], []
        self.raw = 0  # innerhalb von <script>/<style>

    def t(self, text):
        key = norm(text)
        if not key or SAME.match(key):
            return text
        if key in self.tr:
            lead = text[: len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            return lead + self.tr[key] + trail
        self.missing.append(key)
        return text

    def tag(self, tag, attrs, close=""):
        a = dict(attrs)
        if tag == "html":
            a["lang"] = "en"
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key in META_TRANSLATED and a.get("content"):
                a["content"] = self.t(a["content"])
            if key == "og:url":
                a["content"] = page_url(self.name, "en")
            if key == "og:locale":
                a["content"] = "en_GB"
            if key == "og:locale:alternate":
                a["content"] = "de_AT"
        if tag == "link" and a.get("rel") == "canonical":
            a["href"] = page_url(self.name, "en")
        for k in list(a):
            if k in TRANSLATED_ATTRS and a[k]:
                a[k] = self.t(a[k])
            if k in ("href", "src") and a[k] and not (tag == "link" and a.get("rel") in ("canonical", "alternate")):
                a[k] = en_href(a[k])
        parts = [tag] + [k if v is None else f'{k}="{html.escape(v, quote=True)}"' for k, v in a.items()]
        return "<" + " ".join(parts) + close + ">"

    def handle_starttag(self, tag, attrs):
        self.out.append(self.tag(tag, attrs))
        if tag in ("script", "style"):
            self.raw += 1

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.tag(tag, attrs, " /"))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.raw -= 1
        if tag not in VOID:
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        self.out.append(data if self.raw else html.escape(self.t(data), quote=False))

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")


def alternates(name, indent):
    de, en = page_url(name, "de"), page_url(name, "en")
    return (f'{indent}<link rel="alternate" hreflang="de-AT" href="{de}">\n'
            f'{indent}<link rel="alternate" hreflang="en" href="{en}">\n'
            f'{indent}<link rel="alternate" hreflang="x-default" href="{de}">\n')


def ensure_alternates(src, name):
    """hreflang-Verweise direkt nach dem Canonical-Link, idempotent."""
    src = re.sub(r'[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*" ?/?>\n', "", src)
    m = re.search(r'^([ \t]*)<link rel="canonical"[^>]*>\n', src, re.M)
    if not m:
        raise SystemExit(f"{name}.html: kein Canonical-Link")
    return src[: m.end()] + alternates(name, m.group(1)) + src[m.end():]


def write_sitemap():
    today = date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for name in PAGES:
        for lang in ("de", "en"):
            lines.append(f"  <url><loc>{page_url(name, lang)}</loc><lastmod>{today}</lastmod>"
                         f'<xhtml:link rel="alternate" hreflang="de-AT" href="{page_url(name, "de")}"/>'
                         f'<xhtml:link rel="alternate" hreflang="en" href="{page_url(name, "en")}"/></url>')
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tr = load_translations()
    (ROOT / "en").mkdir(exist_ok=True)
    missing = {}
    for name in PAGES:
        path = ROOT / f"{name}.html"
        src = ensure_alternates(path.read_text(encoding="utf-8"), name)
        path.write_text(src, encoding="utf-8", newline="")
        p = Translator(tr, name)
        p.feed(src)
        p.close()
        (ROOT / "en" / f"{name}.html").write_text("".join(p.out), encoding="utf-8", newline="")
        if p.missing:
            missing[name] = sorted(set(p.missing))
    write_sitemap()
    print(f"{len(PAGES)} englische Seiten in en/, Sitemap mit {2 * len(PAGES)} Adressen.")
    if missing:
        print("\nOhne Übersetzung (bleibt deutsch), bitte in assets/translations.js ergänzen:")
        for name, texts in missing.items():
            for t in texts:
                print(f"  {name}: {t[:110]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
