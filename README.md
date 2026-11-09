# Team SWASH – Website

Website von Team SWASH, dem CanSat-Team der HTL Kaindorf bei CanSat Austria 2026/27: **[cansat-swash.org](https://cansat-swash.org)** (Deutsch, Englisch unter [/en/](https://cansat-swash.org/en/)).

Statische Mehrseiten-Website aus HTML, CSS und JavaScript, ohne Framework und ohne Webfonts. Kleine Python-Skripte erzeugen die englischen Seiten und das Foto der Woche; gehostet wird auf Cloudflare (Workers mit statischen Dateien).

Instagram: [@cansat.swash27](https://www.instagram.com/cansat.swash27/) · Haupt-Repo mit Firmware, Elektronik und CAD: [cansat-ark-swash](https://github.com/HerrrNielson/cansat-ark-swash)

## Lokal ansehen

Die Links nutzen saubere URLs wie auf der Live-Seite (`/team` statt `team.html`). Deshalb die Vorschau mit dem kleinen Server im Projekt starten:

    python tools/serve.py

und http://localhost:8000 öffnen. Der normale `python -m http.server` findet `/team` nicht.

## Veröffentlichen

Jeder Push auf `main` geht nach etwa einer Minute live. Cloudflare führt dabei `sh tools/build-dist.sh` aus (Build command im Cloudflare-Dashboard); das Skript legt fest, was veröffentlicht wird. README, Guides, `social/` und `tools/` werden nicht veröffentlicht. Ein neuer Ordner, der auf die Website soll, muss dort ergänzt werden.

## Texte ändern und englische Seiten

Die englischen Seiten unter `en/` werden aus den deutschen erzeugt, nicht von Hand bearbeitet:

    python tools/build_en.py

Die Übersetzungen stehen in `assets/translations.js` (deutscher Text → englischer Text). Nach jeder Textänderung an einer deutschen Seite den neuen Text dort mit Übersetzung eintragen und das Skript starten. Es listet fehlende Übersetzungen auf, setzt `hreflang`-Verweise in beide Sprachversionen und schreibt die `sitemap.xml` neu. Der DE/EN-Schalter im Kopf ist ein Link zur jeweils anderen Version.

Was auf welche Seite gehört und wie lang Texte sein sollen: [`content-guide.md`](content-guide.md). Farben, Schrift, Komponenten und Hover-Regeln: [`DESIGN.md`](DESIGN.md).

## Foto der Woche

Startseite, die Seite Foto der Woche und die Instagram-Posts entstehen jede Woche mit einem Befehl aus `social/wochenfotos.json`:

    python social/foto_der_woche.py

Das Skript baut auch die englischen Seiten neu. Ablauf, Regeln für Fotos und Texte und das Layout der Posts: [`social/DESIGN-FOTO-DER-WOCHE.md`](social/DESIGN-FOTO-DER-WOCHE.md).

## Simulationsdiagramme

Die Diagramme auf der Seite Flugergebnisse erzeugt das Haupt-Repo aus der Simulation der Firmware (`firmware/tools/website_charts.py`, Anleitung dort). Die Zahlen im Seitentext werden von Hand nachgezogen.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `index.html` | Startseite: Teamfoto, Mission, Foto der Woche |
| `ueber-uns.html` | Mission und technischer Aufbau |
| `team.html` | Teammitglieder und Aufgaben |
| `flugergebnisse.html` | Vorversuche und Simulationsergebnisse, später Flugdaten |
| `simulation.html` | Bodenstation als Simulation zum Ausprobieren (`assets/simulation/launch-day-simulation.html`, Kopie aus dem Haupt-Repo, `ground-station/web-sim/`) |
| `foto-der-woche.html` | Alle Fotos der Woche |
| `news.html` | Neuigkeiten aus dem Projekt |
| `unterstuetzen.html` | Unterstützung und Sponsoring |
| `kontakt.html` | Kontakt und Formular (Versand über Web3Forms) |
| `impressum.html`, `datenschutz.html` | Rechtliches |
| `en/` | Englische Seiten, erzeugt von `tools/build_en.py` |
| `assets/` | `styles.css`, `site.js` (Menü, Hell-/Dunkelmodus, Sprachschalter, Formular, Datenschutz-Hinweis), `translations.js`, Logo, Fotos, Grafiken |
| `social/` | Foto der Woche: Daten, Originalfotos, Instagram-Folien, Skript, Design-Guide |
| `tools/` | `serve.py` (Vorschau), `build_en.py` (englische Seiten, Sitemap), `build-dist.sh` (Veröffentlichung) |

## Dienste

| Dienst | Wofür |
|---|---|
| Cloudflare | Hosting, Weiterleitung www → Hauptdomain, Besucherstatistik (Web Analytics, ohne Cookies) |
| Web3Forms | Versand des Kontaktformulars per E-Mail (Access Key in `kontakt.html`, öffentlich) |
| Google Search Console | Sitemap und Suchergebnisse |

Wer einen weiteren Dienst einbindet (Schriften, Videos, Karten …), muss ihn in der Datenschutzerklärung ergänzen.

## Lizenz

Der **Quellcode** dieser Website (HTML-Struktur, CSS, JavaScript, Skripte) steht unter der **MIT-Lizenz**, siehe [`LICENSE`](LICENSE).

**Ausgenommen** und nur mit unserer Erlaubnis verwendbar sind Texte und Inhalte der Seiten, Fotos (vor allem die Teamfotos, wegen der Persönlichkeitsrechte der Abgebildeten), das SWASH-Logo, Grafiken und Diagramme sowie die Bodenstation-Simulation, die aus dem Haupt-Repo stammt. Die genaue Liste steht am Anfang von [`LICENSE`](LICENSE). Anfragen über [cansat-swash.org/kontakt](https://cansat-swash.org/kontakt).
