# Design-System – Team SWASH

Dieses Dokument beschreibt die visuelle Sprache der Website, so wie sie in `assets/styles.css` umgesetzt ist. Wer eine neue Seite, einen neuen Abschnitt oder eine neue Komponente baut, orientiert sich daran. Für Texte gilt zusätzlich [`content-guide.md`](content-guide.md).

## Leitidee

**Ein Missions-Patch auf Papier.** Die Website übernimmt Farben und Motive aus dem SWASH-Logo (Rakete, Flugbahn, Signalpunkte) und kombiniert sie mit einer handgemachten, technischen Werkstatt-Ästhetik:

- **Klare Fläche, harte Kanten:** Marineblau und Weiß, 2-px-Rahmen, Schatten ohne Unschärfe, die wie versetzt aufgeklebt wirken.
- **Handgezeichnete Akzente:** leicht unregelmäßige Ecken, gemalte Pinselstriche, Unterstreichungen, Klebeband, leicht gedrehte Etiketten.
- **Technischer Unterton:** Großbuchstaben mit Sperrung, nummerierte Abschnitte `[01]`, eckige Klammern um Kennzahlen, gestrichelte Hilfslinien wie auf einer Konstruktionszeichnung.
- **Papierkörnung:** ein feines Rauschen liegt über der ganzen Seite.

Die Seite soll nach Schülerteam mit Ingenieursanspruch aussehen: sorgfältig, aber nicht glatt.

---

## Farben

### Markenfarben (fix)

Die `--logo-*`-Variablen ändern sich im Dunkelmodus **nicht**. Sie werden für Flächen verwendet, die immer gleich aussehen sollen (Header, Footer, Panels).

| Token | Wert | Herkunft im Logo | Verwendung |
|---|---|---|---|
| `--logo-navy` | `#0b1f3a` | Hintergrund des Patches | Header, Footer, dunkle Panels, Tabellenkopf |
| `--logo-orange` | `#ff6b1a` | Flugbahn | Hauptakzent: Linien, Schatten, Kontakt-Button, Hervorhebungen auf Dunkel |
| `--logo-purple` | `#4d1056` | Raketenstreifen | Feature-Kachel, Schatten von Bild und Formular |
| `--logo-blue` | `#1e5aa8` | Erdbogen | Links, Schatten im Dunkelmodus |
| `--logo-light` | `#f5f7fa` | Schrift / Stern | Logo-Rahmen, Play-Button, Platzhalter-Etikett |
| `--logo-gray` | `#a9b4c2` | Orbit-Ellipse | Sekundäre Linien |

### Signalpunkte

Die vier Punkte aus dem Logo bilden eine eigene Farbfamilie. Sie erscheinen als Punktreihe (`--logo-dots`) und als rotierende Kartenfarbe.

| Token | Hell | Dunkel |
|---|---|---|
| `--dot-blue` | `#2c55a2` | `#7fa6e8` |
| `--dot-red` | `#b5213a` | `#ef6b80` |
| `--dot-amber` | `#c77214` | `#f0a050` |
| `--dot-green` | `#005300` | `#5fb36a` |

`--logo-dots` ist ein `background` aus vier Kreisen (46 × 10 px). Es wird als Ornament in dunklen Panels und im Footer-Kicker eingesetzt.

### Semantische Tokens (wechseln mit dem Theme)

| Token | Hell | Dunkel | Bedeutung |
|---|---|---|---|
| `--paper` | `#ffffff` | `#0b1f3a` | Seitenhintergrund, Kartenfläche |
| `--wash` | `#f5f7fa` | `#0f2747` | Abgesetzte Abschnitte (`.section.soft`), Hinweise, Tabellen-Hover |
| `--ink` | `#000000` | `#ffffff` | Fließtext |
| `--navy` | `#0b1f3a` | `#ffffff` | **Überschriftenfarbe** (nicht für Flächen verwenden) |
| `--brand` | `#0b1f3a` | `#ff6b1a` | Füllung des Primär-Buttons |
| `--rule` | `#0b1f3a` | `#a9b4c2` | Rahmen von Karten, Feldern, Tabellen |
| `--line` | `#c9ced6` | `#2b4062` | Feine, gestrichelte Trennlinien |
| `--accent` | `#ff6b1a` | `#ff6b1a` | Orange für Flächen, Linien, Schatten |
| `--accent-dark` | `#c2500f` | `#ff8c4d` | **Orange als Textfarbe** auf hellem Grund |
| `--link` | `#1e5aa8` | `#8db4f0` | Links im Fließtext |
| `--deep` / `--deep-2` | `#0b1f3a` / `#071528` | `#071528` / `#040e1c` | Hero, Footer, Footer-Leiste |
| `--header-bg` | `#0b1f3a` | `#071528` | Sticky Header |
| `--button-shadow` | `#ff6b1a` | `#1e5aa8` | Schatten des Primär-Buttons |

> **Wichtig:** `--navy` heißt nur aus historischen Gründen so. Im Dunkelmodus ist es Weiß. Für eine Fläche, die immer marineblau sein soll, `--logo-navy` oder `--deep` verwenden.

### Kontrastregeln

- **Orange als Text:** auf Weiß nur `--accent-dark` (`#c2500f`, Kontrast ≈ 4,7 : 1). Das helle `#ff6b1a` erreicht auf Weiß nur ≈ 2,9 : 1 und ist dort nur für Linien, Flächen und Schatten erlaubt.
- **Auf Marineblau** ist `#ff6b1a` als Text in Ordnung (≈ 5,8 : 1), z. B. Kicker im Page-Hero, Footer-Titel.
- **Weiß auf Marineblau** ≈ 16 : 1, Standard für alle dunklen Flächen.
- **Text auf Orange** ist immer Marineblau (`--logo-navy`), nie Weiß.

### Platzhalter-Markierung

Noch zu ersetzende Angaben (z. B. in Impressum, Datenschutz, Teamnamen) werden mit `.placeholder` markiert: schwarzer Text auf `#ffe2a8` (dunkel `#ffc670`), fett. Diese Farbe kommt sonst nirgends vor.

---

## Typografie

Es werden **keine Webfonts geladen**. Das ist Absicht: Die Datenschutzerklärung sagt zu, dass keine Inhalte von fremden Servern kommen. Neue Schriften nur lokal einbinden und dann die Datenschutzerklärung prüfen.

| Rolle | Token / Stack |
|---|---|
| Display (Überschriften, Labels, Buttons) | `--font-display`: Bahnschrift, „DIN Alternate“, „Helvetica Neue“, „Segoe UI“, Inter, system-ui |
| Fließtext | Inter, ui-sans-serif, system-ui, -apple-system, „Segoe UI“, sans-serif |

Bahnschrift (Windows) und DIN Alternate (macOS) geben den technischen DIN-Charakter. Auf anderen Systemen greift eine neutrale Grotesk.

### Größen

| Element | Größe | Gewicht | Zeilenhöhe | Sperrung |
|---|---|---|---|---|
| Video-Titel (Startseite) | `clamp(2.4rem, 6vw, 4.6rem)` | 700 | 1.02 | −.015em |
| H1 (Standard) | `clamp(2.4rem, 4.6vw, 4rem)` | 700 | 1.06 | −.012em |
| H1 im Page-Hero | `clamp(2.4rem, 5vw, 4.2rem)` | 700 | 1.06 | −.012em |
| H1 Startseiten-Hero | `clamp(2.3rem, 4.2vw, 3.6rem)` | 700 | 1.06 | −.012em |
| H2 | `clamp(1.9rem, 3.2vw, 2.75rem)` | 700 | 1.12 | −.008em |
| H3 | `1.3rem` | 600 | 1.25 | – |
| Kennzahl (`.big-number`) | `clamp(3.4rem, 8vw, 6.5rem)` | 700 | 1 | −.03em |
| Kartennummer (`.icon`) | `2.4rem` | 700 | 1 | −.02em |
| Lead | `clamp(1.08rem, 2vw, 1.25rem)` | 400 | 1.65 | – |
| Fließtext | `16px` | 400 | 1.65 | – |
| Kleintext (Footer, Hinweise) | `.88–.93rem` | 400 | 1.65 | – |

Große Überschriften haben leicht **negative** Sperrung, kleine Labels **positive**.

### Label-Stil (Großbuchstaben)

Alle kleinen Beschriftungen nutzen dieselbe Formel: `--font-display`, Großbuchstaben, 600–700, `.72–.82rem`, Sperrung `.08–.16em`.

| Element | Größe | Sperrung | Farbe |
|---|---|---|---|
| `.eyebrow` (Kicker) | .78rem | .16em | `--accent-dark` (auf Dunkel `--logo-orange`) |
| Navigation | .8rem | .12em | Weiß |
| `.button` | .82rem | .1em | Weiß / Marineblau |
| `.text-link` | .8rem | .12em | `--navy` |
| Feldbeschriftung | .76rem | .12em | `--navy` |
| `.team-role` | .76rem | .12em | `--accent-dark` |
| Footer-Titel | .76rem | .14em | `--logo-orange` |
| Brotkrumen | .74rem | .14em | Weiß |
| Markenname im Header | 1rem | .16em | Weiß |

### Hervorhebung in Überschriften

`.scribble` legt eine handgemalte orange Doppel-Unterstreichung (`deco-underline.svg`) unter 2–4 Wörter einer Überschrift. Höchstens einmal pro Seite, nur in der H1.

```html
<h1>Wir bringen einen Satelliten im Dosenformat sicher <span class="scribble">zurück zur Erde</span>.</h1>
```

---

## Form, Rahmen und Tiefe

### Handgemachte Ecken

Statt gleichmäßiger Radien haben alle Flächen leicht unterschiedliche Eckradien, als wären sie von Hand ausgeschnitten.

| Token | Wert | Für |
|---|---|---|
| `--radius-hand` | `5px 9px 6px 10px / 9px 5px 10px 6px` | Karten, Panels, Bilder, Tabellen, Dialog |
| `--radius-hand-sm` | `3px 6px 4px 7px / 6px 3px 7px 4px` | Buttons, Felder, Etiketten, Toggles, Chips |
| `50 %` | – | nur Logo und Play-Button |

### Harte Schatten

Schatten haben **nie Unschärfe** und sind immer gleich weit nach rechts unten versetzt. Sie wirken wie eine zweite, darunterliegende Papierlage in einer Markenfarbe.

| Komponente | Ruhe | Hover | Farbe hell | Farbe dunkel |
|---|---|---|---|---|
| `.button` | 4 px | 6 px, `translate(-2px,-2px)` | Orange | Blau |
| `.button.secondary` | 4 px | 6 px | `--rule` | `--rule` |
| `.card` | – | 7 px, `translate(-3px,-3px)` | Kartenfarbe | Kartenfarbe |
| `.feature-tile` | 7 px | 10 px | Marineblau | Blau |
| `.visual-panel` | 7 px | – | Orange | Orange |
| `.mission-image` | 7 px | – | Lila | Orange |
| `.form-card` | 7 px | – | Lila | Blau |
| `.table-wrap` | 6 px | – | Orange | Orange |
| `.privacy-dialog` | 8 px | – | Orange | Orange |
| `.video-play` | 4 px | – | Orange | Orange |

Beim Drücken (`:active`) schrumpft der Button-Schatten auf 1 px und das Element rutscht um 3 px nach rechts unten: ein spürbares „Eindrücken“.

### Rahmen und Linien

- **Standardrahmen:** `2px solid var(--rule)` für Karten, Felder, Tabellen, Hinweise.
- **Trennlinien:** `1.5px dashed var(--line)` zwischen Tabellenzeilen und Kontaktpersonen, `2px dashed var(--line)` vor H2 in Rechtstexten.
- **Innenrahmen auf dunklen Flächen:** `2px dashed rgba(245,247,250,.45)`, 12 px eingerückt (10 px beim Mitgliederfoto). Erzeugt den „Patch“-Eindruck. Immer `pointer-events: none`.
- **Kanten des Rahmens:** Header unten 2 px Orange, Footer oben 4 px Orange.
- **Hinweis-Box:** links ein 8 px breiter oranger Balken.

---

## Ornamente

Alle Dekor-Dateien liegen in `assets/`. Sie sind rein dekorativ und werden über CSS (Pseudo-Elemente, Masken, Hintergründe) eingesetzt, nicht als `<img>`.

| Ornament | Datei / Technik | Wo |
|---|---|---|
| Papierkörnung | `deco-grain.svg`, `body::after`, fixiert über allem | Ganze Seite. Hell: Deckkraft .13, `multiply`. Dunkel: .5, `soft-light` |
| Pinselstrich | `deco-stroke.svg` als `mask`, Farbe über `background` | Unter Navigationspunkten, hinter Abschnitts-Labels, hinter Kartennummern, im Footer-Kicker |
| Doppel-Unterstreichung | `deco-underline.svg` | `.scribble` in der H1 |
| Missionsgrafik | `deco-mission.svg` (Rakete, Flugbahn, Orbit, Punkte, aufgeraut per SVG-Filter) | Rechts im Video-Hero und im Page-Hero, 4–8° gedreht |
| Signalpunkte | `--logo-dots` | Ecke rechts oben in `.visual-panel` und Bildrahmen, Footer-Kicker |
| Klebeband | orange (82 %), unregelmäßiges `clip-path`-Polygon, −4° gedreht | Oben mittig auf `.mission-image` |
| Vierzackiger Stern | Orange, `clip-path`-Polygon, 14° gedreht | Ecke rechts oben in `.feature-tile` |
| Funkel-Zeichen `✦` | Text in Orange | In Platzhalter-Etiketten |

### Typografische Zeichen

- `→` hinter Button- und Text-Link-Beschriftungen (per CSS, nicht im HTML), wandert bei Hover 4 px nach rechts.
- `↗` am Ende externer Links (im HTML).
- `›` als Pfeil in der mobilen Navigation.
- `[01]`, `[02]` … vor Abschnitts-Labels, automatisch per CSS-Zähler.
- `[ ` und ` ]` in Orange um große Kennzahlen.
- `✓` in einem leicht gedrehten Kästchen bei `.check-list`.

### Drehungen

Kleine Drehungen geben den Eindruck von aufgeklebtem Material. Sie bleiben dezent:

| Element | Drehung |
|---|---|
| Video-Etikett „Video folgt“ | −3° |
| Platzhalter-Etikett | −2° |
| Häkchen-Kästchen | −3° |
| Klebeband | −4° |
| Missionsgrafik | +4° bis +8° |
| Stern | +14° |

Text in Fließtext, Überschriften, Buttons und Karten wird **nie** gedreht.

---

## Layout

### Container

```css
.container { width: min(calc(100% - 2.5rem), 1240px); margin-inline: auto; }
```

Seitenrand 1,25 rem, unter 560 px 1 rem. Maximale Inhaltsbreite `--width: 1240px`.

### Lesebreiten

| Element | max-width |
|---|---|
| H1 | 840 px (Page-Hero 760 px) |
| Lead | 680 px (Page-Hero 640 px) |
| `.section-heading` | 780 px |
| Rechtstexte (`.legal-content`) | 880 px |

### Abschnitte

| Klasse | Abstand oben/unten | Hintergrund |
|---|---|---|
| `.section` | `clamp(4rem, 8vw, 6.5rem)` | `--paper` |
| `.section.soft` | wie oben | `--wash`, oben und unten 2 px `--rule` |
| `.page-hero` | `clamp(4.5rem, 9vw, 7.5rem)` / `clamp(3.5rem, 7vw, 5.5rem)` | `--deep` |
| `.hero` / `.home-hero` | `clamp(4rem, 8vw, 7rem)` / `clamp(3.5rem, 7vw, 6rem)` | `--paper` |

Normale und `.soft`-Abschnitte wechseln sich ab. Zwei `.soft` hintereinander vermeiden.

### Raster

| Klasse | Spalten | Abstand |
|---|---|---|
| `.grid-3` | 3 | 1.5rem |
| `.grid-2` | 2 | 1.5rem |
| `.split` | 2 (Text links, Visual rechts) | `clamp(2rem, 6vw, 5rem)` |
| `.hero-grid` | 2 | `clamp(2rem, 5vw, 5rem)` |
| `.contact-grid` | `1fr .82fr` | 1.75rem |
| `.footer-grid` | `1.4fr 1fr 1fr` | 2.5rem |

### Breakpoints

| Breite | Änderung |
|---|---|
| ≤ 1060 px | Navigationspunkte enger |
| ≤ 940 px | Header 72 px hoch, Hamburger-Menü, Navigation als Ausklapp-Liste |
| ≤ 820 px | `.hero-grid`, `.split`, `.contact-grid` einspaltig; `.grid-3` zweispaltig (einzelne letzte Karte über volle Breite); Footer zweispaltig |
| ≤ 560 px | Alles einspaltig; Hero-Buttons volle Breite; Abschnittsleiste untereinander |

Die Seite wird ab 560 px abwärts als Mobilansicht behandelt. Neue Komponenten müssen bei 360 px Breite ohne horizontales Scrollen funktionieren (Ausnahme: `.table-wrap` scrollt bewusst horizontal).

---

## Komponenten

### Header

- Sticky, `--header-bg`, unten 2 px Orange, Höhe 84 px (mobil 72 px).
- Links: Logo im runden Rahmen (`.logo-frame`: heller Hintergrund, 1,5 px gestrichelter oranger Umriss mit 3 px Abstand) und der Name „Team SWASH“ in Label-Schrift.
- Navigation: weiße Großbuchstaben. Hover und aktive Seite (`aria-current="page"`) bekommen einen orangen Pinselstrich, der von links aufgezogen wird.
- „Kontakt“ ist immer der letzte Punkt und als oranger Button (`.nav-contact`) mit marineblauer Schrift hervorgehoben.
- Rechts davon, durch eine gestrichelte Linie getrennt: Hell/Dunkel-Schalter und Sprachschalter DE/EN (38 × 38 px, Umriss, Hover in Orange).

### Buttons

```html
<a class="button" href="…">Unsere Mission</a>
<a class="button secondary" href="…">Flugergebnisse</a>
```

| Variante | Fläche | Schrift | Schatten |
|---|---|---|---|
| Primär | `--brand` | Weiß (dunkel: Marineblau) | `--button-shadow` |
| Sekundär | `--paper` | `--navy` | `--rule` |

Mindesthöhe 50 px. Beschriftung 2–4 Wörter, nennt das Ziel. Der Pfeil `→` wird bei Links und Submit-Buttons automatisch angehängt. Pro Bereich höchstens ein Primär-Button; ein zweiter Button daneben ist sekundär.

### Text-Link

```html
<a class="text-link" href="…">Mission im Detail</a>
```

Für weniger wichtige Verweise, z. B. rechts in einer `.section-bar`. Label-Stil mit orangem Pfeil.

### Kicker und Abschnitts-Label

```html
<p class="eyebrow section-label">Unser CanSat</p>
<h2>Was wir an Bord haben.</h2>
```

- `.eyebrow` allein: kleine orange Zeile über einer Überschrift (z. B. im Page-Hero, im Dialog).
- `.eyebrow.section-label`: zusätzlich automatische Nummer `[01]` davor und ein Pinselstrich dahinter. Wird beim Hereinscrollen wie getippt eingeblendet (siehe [Bewegung](#bewegung)). Für jeden Inhaltsabschnitt in `<main>` verwenden; die Zählung beginnt auf jeder Seite neu.

### Abschnittskopf

```html
<div class="section-bar">            <!-- Kicker links, Text-Link rechts, Linie darunter -->
  <p class="eyebrow section-label">Unser CanSat</p>
  <a class="text-link" href="…">Mission im Detail</a>
</div>
<div class="section-heading">        <!-- H2 + ein Satz Einleitung -->
  <h2>Was wir an Bord haben.</h2>
  <p>Wir verbinden Messinstrumente, Flugsteuerung und Bildauswertung …</p>
</div>
```

### Karte

```html
<article class="card">
  <span class="icon" aria-hidden="true">01</span>
  <h3>Messdaten</h3>
  <p>Temperatur und Luftdruck werden während des Sinkflugs erfasst …</p>
</article>
```

- Weiße Fläche, 2 px Rahmen, handgemachte Ecken.
- Bei Hover hebt sich die Karte 3 px an und zeigt einen 7 px Schatten in ihrer **Kartenfarbe**.
- Die Kartenfarbe rotiert in `.grid-2` und `.grid-3` automatisch: Blau → Rot → Amber → Grün (die Signalpunkte des Logos). Sie färbt auch die Nummer `.icon` und die Rollen-Chips.
- `.icon` ist eine zweistellige Nummer (`01`, `02` …) mit Pinselstrich, keine Grafik.

Varianten:

| Klasse | Zweck |
|---|---|
| `.member-card` | Teammitglied: quadratisches Foto (`.member-photo`), Name, `.team-role`, Rollen-Chips (`.member-roles`) |
| `.contact-people-card` | Liste von Ansprechpersonen, getrennt durch gestrichelte Linien |

### Feature-Kachel

```html
<div class="card feature-tile">
  <h3>Wir sind bei CanSat Austria dabei</h3>
  <p>…</p>
</div>
```

Lila Fläche, weiße Schrift, gestrichelter Innenrahmen, oranger Stern oben rechts, Inhalt unten ausgerichtet, 7 px marineblauer Schatten. Für **einen** herausgehobenen Hinweis pro Seite, typischerweise rechts in einem `.split`.

### Kennzahl-Panel

```html
<div class="visual-panel">
  <span class="eyebrow">Messung · Funk · Auswertung</span>
  <span class="big-number">1 Hz</span>
  <p>Mindestens eine Messung pro Sekunde während des Sinkflugs.</p>
</div>
```

Marineblaue Fläche, gestrichelter Innenrahmen, Signalpunkte oben rechts, oranger Schatten. Eine einzige große Zahl in orangen eckigen Klammern, darunter ein erklärender Satz.

### Bild mit Rahmen

`.mission-image` → `.mission-image-frame` + `figcaption`. Marineblaue Fläche, Klebeband oben, Signalpunkte, gestrichelter Innenrahmen, lila Schatten. Die Bildunterschrift liegt unten im Bild, abgetrennt durch eine gestrichelte Linie.

### Platzhalter für Medien

Solange echte Fotos oder Videos fehlen:

```html
<span class="image-placeholder-label"><span aria-hidden="true">✦</span> CanSat-Foto folgt</span>
```

Helles Etikett, −2° gedreht, auf marineblauer Fläche. Der Container trägt `role="img"` und ein `aria-label`, das den Platzhalter beschreibt. Sobald ein Bild da ist, entfällt das Etikett; bei `.member-photo` verschwindet der Innenrahmen automatisch (`:has(img)`).

### Häkchen-Liste

```html
<ul class="check-list"><li>Versuchsbedingungen und Messwerte festhalten.</li></ul>
```

Häkchen in einem gerahmten, −3° gedrehten Kästchen. Für kurze Arbeitsschritte oder Grundsätze, 3–5 Punkte.

### Page-Hero (Unterseiten)

Marineblau, Brotkrumen (`Home / Seite`), oranger Kicker, weiße H1 und Lead, Missionsgrafik rechts. Jede Unterseite beginnt damit. Die Startseite hat stattdessen den Video-Bereich und einen hellen Hero mit Bild.

### Tabelle

```html
<div class="table-wrap"><table class="results-table">…</table></div>
```

Rahmen, oranger Schatten, marineblauer Kopf mit Label-Schrift. Die erste Spalte (`tbody th`) ist eine orange Kennung in Display-Schrift. Zeilen getrennt durch gestrichelte Linien, Hover in `--wash`. Zellen brechen nicht um, die Tabelle scrollt auf kleinen Bildschirmen horizontal. Einheiten gehören in die Kopfzeile.

### Hinweis

```html
<div class="notice">…</div>
```

`--wash`-Fläche, Rahmen, 8 px oranger Balken links. Für Einordnungen, Vorbehalte und Hinweise auf Platzhalter.

### Formular

- `.form-card` mit lila Schatten, Felder im zweispaltigen `.form-grid` (`.field.full` für volle Breite).
- Beschriftung im Label-Stil über dem Feld, Pflichtfelder mit `*`.
- Felder: 2 px Rahmen, kleine Handecken. Fokus: 3 px orangener Umriss mit 2 px Abstand.
- Statusmeldung (`.form-status.is-visible`): gestrichelter oranger Rahmen auf `--wash`.

### Footer

Marineblau, oben 4 px Orange. Beginnt mit einem Kicker („Hilfreiche Links“) zwischen Signalpunkten und Pinselstrich. Drei Spalten: Marke mit Kurzbeschreibung, Seiten, CanSat Austria + Rechtliches. Spaltentitel orange im Label-Stil. Unten eine dunklere Leiste (`--deep-2`) über die volle Breite mit Copyright und Schlusszeile.

### Datenschutz-Dialog

Natives `<dialog>`, max. 560 px breit, Rahmen und 8 px oranger Schatten, Hintergrund abgedunkelt mit Marineblau (72 %). Kicker, H2, Text, ein Primär-Button.

---

## Bewegung

Bewegung ist kurz, mechanisch und dient der Rückmeldung. Keine weichen Fades, kein Parallax.

| Was | Dauer | Effekt |
|---|---|---|
| Button | .15s ease | Anheben + Schatten wachsen; beim Drücken eindrücken |
| Karte | .18s ease | Anheben 3 px + farbiger Schatten |
| Pfeile `→` | .2s ease | 4 px nach rechts |
| Toggles | .2s ease | Rahmen und Symbol werden orange |
| Navigation | .25s ease | Pinselstrich wird von links aufgezogen (`scaleX`) |
| Abschnitts-Label | 1.1s `steps(26)` | Schreibmaschinen-Effekt per `clip-path`, einmalig beim Hereinscrollen |

Bewegungsrichtung ist immer gleich: Elemente heben sich nach **links oben**, ihr Schatten liegt rechts unten. `prefers-reduced-motion: reduce` schaltet alle Übergänge und Animationen ab; der Schreibmaschinen-Effekt wird dann gar nicht vorbereitet.

---

## Dunkelmodus

- Gesteuert über `data-theme="dark"` am `<html>`-Element. Standard ist Hell; die Systemeinstellung wird nicht automatisch übernommen. Die Wahl wird erst gespeichert, wenn jemand umschaltet (`team-swash-theme` im `localStorage`).
- Hintergrund wird Marineblau, Text und Überschriften Weiß, Rahmen hellgrau.
- **Primär-Buttons werden orange** mit marineblauer Schrift und blauem Schatten.
- Lila und marineblaue Schatten werden durch Blau oder Orange ersetzt, weil sie auf Marineblau nicht sichtbar wären.
- Dunkle Panels (`.visual-panel`, `.mission-image`, `.member-photo`) wechseln auf das noch dunklere `--deep`, damit sie sich vom Seitenhintergrund abheben.
- Die Signalpunkte werden aufgehellt.
- Die Körnung wird stärker (`opacity: .5`, `soft-light`).

Neue Komponenten nur mit den semantischen Tokens bauen; dann funktionieren sie in beiden Modi. Wer `--logo-*` oder feste Farben verwendet, muss die Komponente im Dunkelmodus prüfen und bei Bedarf eine Regel im Abschnitt `/* Dark mode */` ergänzen.

---

## Barrierefreiheit

- Sprunglink „Zum Inhalt springen“ als erstes Element jeder Seite.
- Aktive Seite in der Navigation per `aria-current="page"` (setzt `site.js`).
- Schalter für Menü, Theme und Sprache haben `aria-label`, `aria-expanded` bzw. `aria-pressed`.
- Dekorative Elemente (Kartennummern, Ornamente, Sternzeichen) sind `aria-hidden="true"` oder reine Pseudo-Elemente.
- Medien-Platzhalter haben `role="img"` und eine Beschreibung.
- Formularfelder haben einen sichtbaren Fokus. Bei anderen Elementen gilt der Browser-Fokus; er darf nicht per `outline: none` entfernt werden.
- Mindestgröße von Klickzielen: 38 px (Toggles), 44 px (Hamburger), 50 px (Buttons).
- Kontrastregeln siehe [Farben](#kontrastregeln).

---

## Mehrsprachigkeit

Die Seite ist zweisprachig (DE/EN). `site.js` sucht jeden deutschen Text wortgleich in `assets/translations.js`. Neue oder geänderte Texte, auch `aria-label` und `alt`, brauchen dort einen Eintrag. Englische Texte sind oft länger: Buttons, Labels und Überschriften in beiden Sprachen bei schmaler Breite prüfen.

---

## Checkliste für neue Inhalte

- [ ] Abschnitt mit `.section` oder `.section.soft`, darin `.container`.
- [ ] Kicker als `.eyebrow.section-label`, danach H2.
- [ ] Nur Tokens aus `:root` verwenden, keine neuen Hex-Werte.
- [ ] Ecken mit `--radius-hand` bzw. `--radius-hand-sm`.
- [ ] Schatten hart, rechts unten, in einer Markenfarbe.
- [ ] Orange als Text nur `--accent-dark` auf Hell bzw. `--logo-orange` auf Dunkel.
- [ ] Im Dunkelmodus und bei 360 px Breite geprüft.
- [ ] Übersetzung in `assets/translations.js` ergänzt.
- [ ] Dekoratives ist `aria-hidden` oder ein Pseudo-Element.

## Nicht machen

- Weiche, verschwommene Schatten oder Verläufe.
- Gleichmäßig runde Ecken (`border-radius: 8px` o. Ä.) auf Flächen.
- Neue Akzentfarben außerhalb von Logo- und Signalfarben.
- Helles Orange `#ff6b1a` als Textfarbe auf Weiß.
- Weiße Schrift auf Orange.
- Webfonts oder Bilder von fremden Servern.
- Mehr als einen Primär-Button oder mehr als eine `.feature-tile` pro Bereich.
- Gedrehten Fließtext oder gedrehte Überschriften.
