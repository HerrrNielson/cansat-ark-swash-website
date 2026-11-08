# Design-Guide: Foto der Woche

Jede Woche zeigt Team SWASH ein Foto davon, woran gerade gebaut wird: auf Instagram als Karussell und auf der Website (Startseite und Seite [Foto der Woche](../foto-der-woche.html)). Damit alle Posts gleich aussehen, entstehen sie **immer** mit dem Skript `social/foto_der_woche.py` aus einem Eintrag in `social/wochenfotos.json`. Nicht von Hand in Canva o. Ä. nachbauen.

Farben, Schriften und Formen kommen aus dem Design-System der Website ([`DESIGN.md`](../DESIGN.md)).

---

## Ablauf jede Woche

1. **Fotos ablegen** in `social/fotos/`, benannt nach Jahr und Kalenderwoche:
   `2026-kw46.jpg` (Hauptbild), `2026-kw46-2.jpg`, `2026-kw46-3.jpg` (weitere Karussell-Folien).
2. **Eintrag oben** in `social/wochenfotos.json` ergänzen (Vorlage unten).
3. **Skript starten** im Website-Ordner:
   ```
   python social/foto_der_woche.py
   ```
4. **Ergebnis prüfen:** `social/posts/2026-kw46-1.png`, `-2.png` … und die Bildunterschrift `social/posts/2026-kw46.txt` ansehen. Website lokal öffnen (Startseite und `foto-der-woche.html`), auch mit Umschaltung auf EN.
5. **Website veröffentlichen** (committen und pushen), **dann** auf Instagram posten: alle PNGs der Woche in der Reihenfolge `-1`, `-2` … als ein Karussell, Text aus der `.txt`-Datei.

Das Skript erneuert die Website immer aus der ganzen JSON-Datei. Ein Tippfehler in einer alten Woche wird also in der JSON korrigiert und das Skript neu gestartet.

### Vorlage für einen Eintrag

```json
{
  "jahr": 2026,
  "kw": 46,
  "suchzeile": "Suchbegriffe zuerst: was man sieht, in Worten, nach denen jemand sucht 🛰️",
  "bilder": ["social/fotos/2026-kw46.jpg", "social/fotos/2026-kw46-2.jpg"],
  "titel": "Kurzer Titel",
  "text": "Ein bis zwei Sätze, was man sieht und warum es wichtig ist.",
  "alt": "Bildbeschreibung für Screenreader: was ist auf dem Hauptbild zu sehen",
  "unterschriften": ["Ein Satz zur zweiten Folie."],
  "frage": "Eine Frage an euch, die zum Kommentieren einlädt? 👀",
  "thema_tag": "#elektronik",
  "titel_en": "Short title",
  "text_en": "One or two sentences …",
  "alt_en": "Image description …"
}
```

Optional: `"ausschnitte": ["x,y,breite,hoehe", null]` in Pixeln des Originalbilds, falls der automatische Zuschnitt nicht passt (`null` = automatisch).

---

## Fotos

| Regel | Warum |
|---|---|
| **Querformat**, Motiv in der Mitte, rundum etwas Platz | Das Skript schneidet auf **4:3** zu. Was am Rand liegt, kann wegfallen. |
| Mindestens **1600 × 1200 px** für echte Fotos | Wird auf 936 px (Instagram) und höchstens 1600 px (Website) skaliert. |
| **Renders** (KiCad, CAD) vor ruhigem, einfarbigem Hintergrund | Dann findet das Skript das Motiv automatisch und schneidet eng zu. |
| Echte Fotos: ruhiger Hintergrund, Tageslicht, nichts Privates im Bild | Bei Fotos vor unruhigem Hintergrund schneidet das Skript einfach mittig. |
| **Personen nur mit Einverständnis**, keine fremden Personen | Datenschutzerklärung, Abschnitt 6. |
| Keine Filter, keine Schrift im Foto | Text und Rahmen setzt das Skript. |
| Hauptbild = das Bild für die Website | Die Website zeigt nur das erste Bild, Instagram alle. |

## Texte

Für die Bildunterschrift gelten die Instagram-Regeln des Teams aus dem Haupt-Repo ([`outreach/video-guideline.md`](https://github.com/HerrrNielson/cansat-ark-swash/blob/main/outreach/video-guideline.md), Abschnitt 7, und [`outreach/DESIGN.md`](https://github.com/HerrrNielson/cansat-ark-swash/blob/main/outreach/DESIGN.md)). Fakten nur aus dem Repo oder vom Team bestätigt; ein 3D-Modell heißt „3D-Modell“, nicht „Foto“ oder „fertige Platine“.

**Anrede:** auf Instagram **„ihr“** (in `frage` und überall, wo die Leser angesprochen werden). Die Website-Texte (`titel`, `text`, `alt`) bleiben sachlich in der Wir-Form, weil sie auch auf der Website stehen, und dort gilt „Sie“.

| Feld | Länge | Beispiel |
|---|---|---|
| `suchzeile` | 1 Satz, erste Zeile der Bildunterschrift: **Suchbegriffe zuerst** (Instagram durchsucht Bildunterschriften wie eine Suchmaschine), ein Emoji am Ende | „CanSat-Elektronik im 3D-Modell: zwei runde Platinen für eine Getränkedose 🛰️“ |
| `titel` | 2–5 Wörter, höchstens 2 Zeilen im Post | „Zwei Platinen, eine Dose“ |
| `text` | 1–2 Sätze, höchstens 3 Zeilen im Post (ca. 170 Zeichen) | „Unsere Elektronik im 3D-Modell: …“ |
| `unterschriften` | je 1 Satz pro weitere Folie | „Die andere Seite: …“ |
| `frage` | eine Frage mit „ihr“, die zum Kommentieren einlädt | „Welche Bauteile erkennt ihr? 👀“ |
| `thema_tag` | genau **ein** Hashtag zum Thema der Woche, klein geschrieben | `#elektronik`, `#rotor`, `#test` |
| `alt` | was zu sehen ist, ohne „Bild von“ | „3D-Modell der zwei gestapelten runden Platinen unseres CanSat“ |

Ist ein Text zu lang, **bricht das Skript mit einer Meldung ab** statt ihn abzuschneiden. Dann kürzen. Fehlt `suchzeile`, `frage` oder `thema_tag`, bricht es ebenfalls ab.

Die Bildunterschrift für Instagram baut das Skript immer gleich (Kernaussagen mit Emoji-Ziffern, eine je Folie; bei nur einer Folie ohne Ziffer):

```
<suchzeile>

Foto der Woche · KW 46: <titel>
1️⃣ <text>
2️⃣ <unterschrift der Folie 2>

🔗 Alle Wochenfotos findet ihr auf unserer Website, Link in der Bio
💬 <frage>

#cansat #raumfahrt #physik #htlkaindorf <thema_tag>
```

**Höchstens 5 Hashtags:** die vier Standard-Tags des Teams stehen im Skript (`HASHTAGS`) und werden nur dort geändert, dazu kommt der `thema_tag` der Woche. Der Link in der Instagram-Bio zeigt auf `cansat-swash.org`; von der Startseite führt ein Klick aufs Wochenfoto zu allen Wochen.

Beim **Posten** gelten ebenfalls die Team-Regeln (`video-guideline.md`, Abschnitt 8), z. B. als Collab-Post mit dem Account der HTL Kaindorf und in der ersten Stunde auf Kommentare antworten.

---

## Aufbau des Instagram-Posts

Format **1080 × 1350 px (4:5)**, PNG. Alle Folien eines Karussells haben denselben Aufbau.

```
┌──────────────────────────────────────────┐ ← 8 px Orange (#ff6b1a)
│  FOTO DER WOCHE              ( Logo )     │   Label Orange, darunter KW · Jahr in Hell
│  KW 45 · 2026                             │   Logo 128 px mit orangem Ring
│            ▬▬▬ Klebeband ▬▬▬              │
│  ┌─────────────────────────────────┐      │   Foto 936 × 702 px (4:3), Rand 72 px
│  ┆                                 ┆▌     │   gestrichelter Innenrahmen (Hell, 45 %)
│  ┆            Foto 4:3             ┆▌     │   harter Schatten 14 px Lila (#4d1056)
│  └─────────────────────────────────┘▌     │
│   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     │
│  Titel (Bahnschrift Bold 64, Hell)        │   höchstens 2 Zeilen
│  Text (Segoe UI 29, Grau)                 │   höchstens 3 Zeilen
│                                           │
│  CANSAT-SWASH.ORG          1 / 2  ● ● ● ● │   Seitenzahl nur bei Karussell
└──────────────────────────────────────────┘
```

| Element | Wert |
|---|---|
| Hintergrund | Marineblau `#0b1f3a` mit feiner Papierkörnung (wie die Website) |
| Außenrand | 72 px links, rechts, unten |
| Label „FOTO DER WOCHE“ | Bahnschrift Bold 30 px, Sperrung 6 px, Orange `#ff6b1a` |
| KW · Jahr | Bahnschrift SemiBold 30 px, Sperrung 5 px, Hell `#f5f7fa` |
| Logo | `assets/swash-logo.png`, 128 px, oranger Ring 2 px |
| Foto | 936 × 702 px, Ecken 10 px, Innenrahmen gestrichelt 14 px eingerückt |
| Schatten | hart, 14 px nach rechts unten, Lila `#4d1056`; **nie** weich |
| Klebeband | Orange, 82 % deckend, um 4° gedreht, oben mittig |
| Titel | Bahnschrift Bold 64 px, Hell |
| Text | Segoe UI 29 px, Grau `#a9b4c2`, Zeilenabstand 41 px |
| Fußzeile | „CANSAT-SWASH.ORG“ Bahnschrift SemiBold 24 px, Grau; vier Signalpunkte in Blau, Rot, Bernstein, Grün |
| Seitenzahl | „1 / 2“ in Hell, nur wenn das Karussell mehr als eine Folie hat |

**Nicht machen:** andere Farben, weiche Schatten oder Verläufe, Emojis oder Sticker im Bild, Text ins Foto schreiben, Folien einzeln von Hand nachbearbeiten. Wer etwas am Aussehen ändern will, ändert das Skript, damit alle künftigen Posts mitziehen.

## Website

- **Startseite:** zeigt das Hauptbild der neuesten Woche rechts neben der Überschrift, mit Unterschrift „Foto der Woche · KW …“, Titel und „Alle Wochenfotos →“. Das ganze Bild ist ein Link auf `foto-der-woche.html` und hebt sich beim Überfahren an, wie alle klickbaren Elemente.
- **Seite Foto der Woche:** alle Wochen, neueste oben, jeweils Bild links und KW, Titel und Text rechts. Jede Woche hat einen Anker, z. B. `foto-der-woche.html#2026-kw45`.
- Beide Blöcke und die englischen Texte schreibt das Skript zwischen die Markierungen `WOCHENFOTO:START/END` bzw. `ARCHIV:START/END`. **Nichts zwischen den Markierungen von Hand ändern**, es wird beim nächsten Lauf überschrieben.
- Die Originalfotos in `social/fotos/` und die Instagram-Folien in `social/posts/` liefert die Website nicht aus (geprüft am 08.11.2026). Das GitHub-Repo ist aber **öffentlich**, also kann sie dort jeder sehen. Nichts in dieses Repo legen, was nicht öffentlich sein darf.
