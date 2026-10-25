# Textreferenz der Website

Für jeden Text der Website steht hier, **was dort inhaltlich hinkommen soll**. Wer Texte schreibt oder überarbeitet, orientiert sich daran. Die Spalte „Aktuell“ zeigt den Anfang des heutigen Texts, damit man die Stelle findet.

Stand der Durchsicht: 20.10.2026.

Die Website zählt zur Öffentlichkeitsarbeit, die die Jury mit 10 % bewertet (CanSat-Handbuch, Abschnitt 5.2.4).

## Vor dem Schreiben

- **Englische Version mitpflegen.** Die Sprachumschaltung sucht jeden deutschen Text *wortgleich* in `assets/translations.js`. Wer einen deutschen Text im HTML ändert, muss denselben Text dort als Schlüssel ändern und die englische Übersetzung anpassen. Sonst bleibt der Text beim Umschalten auf EN deutsch.
- **Fakten aus dem Repo oder vom Team bestätigt.** Schätzungen immer als Schätzung kennzeichnen.
- **Anrede:** Das Team hat die höfliche Anrede „Sie“ bestätigt.
- **Richtwerte für die Länge** im aktuellen Layout:

| Elementtyp | Länge |
|---|---|
| Kicker (kleine Zeile über einer Überschrift) | 2–4 Wörter |
| Seitenüberschrift (H1) | ein Satz, höchstens ca. 10 Wörter |
| Einleitung unter der H1 | 1–2 Sätze, ca. 25–40 Wörter |
| Abschnittsüberschrift (H2) | ein kurzer Satz |
| Kartentitel | 1–3 Wörter |
| Kartentext | 1–2 Sätze, ca. 15–25 Wörter |
| Button | 2–4 Wörter, nennt das Ziel |

---

## Auf allen Seiten

### Kopfbereich

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Name neben dem Logo | „Team SWASH“ | Teamname. Bleibt. |
| Alternativtext des Logos | „SWASH – Arbeitsgruppe für Raumfahrt Kaindorf“ | Wird von Screenreadern vorgelesen: offizieller Name der Gruppe. Nur ändern, wenn sich der Name ändert. |
| Navigation | Home · Über uns · Team · Flugergebnisse · Kontakt | Ein bis zwei Wörter pro Seite, passend zum Seitentitel. |
| Sprunglink | „Zum Inhalt springen“ | Unsichtbar, für Tastatur und Screenreader. Nicht ändern. |
| Beschriftung von Menü, Hell/Dunkel, DE/EN | in `assets/site.js` | Nur für Screenreader. Nicht ändern. |

### Fußbereich

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Hilfreiche Links“ | Kurze Zeile über dem Fußbereich. |
| Kurzbeschreibung unter dem Logo | „Ein Team aus Kaindorf entwickelt …“ | Ein Satz: wer wir sind und was wir bauen. Hier passt der Schulname (HTL Kaindorf) hin. |
| Spaltentitel | „Seiten“, „CanSat Austria“, „Rechtliches“ | Bezeichnungen der Link-Spalten. Bleiben. |
| ESERO-Link | „Informationen bei ESERO Austria ↗“ | Linktext zur Wettbewerbsseite. Das ↗ zeigt, dass der Link die Website verlässt. |
| Copyright | „© 2026 Team SWASH · CanSat Austria“ | Das Jahr setzt sich automatisch. |
| Schlusszeile | „Mit Sorgfalt gestaltet in Österreich“ | Kurze persönliche Signatur, z. B. wer die Website gebaut hat oder ein Bezug zur Schule. Der heutige Satz ist austauschbar. |

### Datenschutz-Hinweis (Fenster beim ersten Besuch)

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Datenschutz“ | Bleibt. |
| Titel | „Datenschutz & Cookies“ | Bleibt. |
| Text | „Diese Website setzt derzeit keine …“ | Zählt genau auf, was im Browser gespeichert wird, und verlinkt die Datenschutzerklärung. **Gespeichert werden heute drei Dinge: Hell/Dunkel, Sprache und die Bestätigung dieses Hinweises. Die Sprache fehlt im Text.** Muss zu Abschnitt 5 der Datenschutzerklärung passen. |
| Button | „Verstanden“ | Bestätigung. Bleibt. |

### Unsichtbare Texte jeder Seite

| Element | Beispiel | Was dort hinkommen soll |
|---|---|---|
| Seitentitel (Browser-Tab, Suchergebnis) | „Über uns \| Team SWASH“ | Seitenname, dann „Team SWASH“. |
| Meta-Beschreibung | „Die CanSat-Mission und das technische System …“ | Ein Satz mit ca. 120–155 Zeichen, den Google unter dem Link anzeigt. Jede Seite hat ihre eigene. Bei Impressum und AGB steht noch Firmen- bzw. Mustertext. |

---

## Startseite (`index.html`)

### Video ganz oben

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Etikett | „Video folgt“ | Fällt weg, sobald ein echtes Video da ist. |
| Videotitel | „Unser CanSat in Aktion“ | 3–5 Wörter: was man im Video sieht. |
| Untertitel | „Hier ist Platz für ein kurzes Video …“ | Ein Satz zum Video (z. B. Falltest, Bau, Start). Heute nur Platzhalter. |
| Screenreader-Text des Platzhalters | „Platzhalter für ein kurzes Video …“ | Mit dem echten Video durch eine Beschreibung des Videos ersetzen. |

Das Video am besten lokal einbinden. Ein eingebettetes YouTube-Video verlangt eine Ergänzung der Datenschutzerklärung. Videos laufen über Git LFS, das Kontingent ist begrenzt.

### Einstieg

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Team SWASH · CanSat Austria“ | Wer wir sind und in welchem Rahmen. Bleibt. |
| Hauptüberschrift | „Wir bringen einen Satelliten im Dosenformat sicher zurück zur Erde.“ | Die Kernbotschaft des Projekts in einem Satz, das Erste, was man liest. Der unterstrichene Teil („zurück zur Erde“) hat 2–4 Wörter. Die Überschrift ist im HTML in zwei Teile geteilt, die Übersetzung braucht beide Teile. |
| Einleitung | „Unser CanSat misst Temperatur und Luftdruck …“ | 1–2 Sätze: was der CanSat tut (Primärmission) und was ihn besonders macht (Autorotation, zielgenaue Landung). Für Laien verständlich. |
| Buttons | „Unsere Mission“, „Flugergebnisse“ | Führen zu „Über uns“ und „Flugergebnisse“. |
| Foto | „CanSat-Foto folgt“ | Ein echtes Foto vom CanSat oder vom Testmodell. Der Platzhaltertext fällt dann weg. |
| Bildunterschrift | „Einblicke in Aufbau und Flug ergänzen wir hier.“ | Ein kurzer Satz, was das Foto zeigt, z. B. „Testmodell mit passivem Rotor beim Autofenster-Versuch“. |

### Abschnitt „Unser CanSat“

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Unser CanSat“ | Bleibt. |
| Link rechts | „Mission im Detail“ | Führt zu „Über uns“. |
| Überschrift | „Was wir an Bord haben.“ | Leitet die drei Karten ein. |
| Einleitung | „Wir verbinden Messinstrumente, Flugsteuerung …“ | Ein Satz Überblick über die Systeme an Bord. |
| Karte 01 | „Messdaten“ | Primärmission in 1–2 Sätzen: Temperatur und Luftdruck messen, per Funk zur Bodenstation senden. |
| Karte 02 | „Autorotation“ | Was der Rotor macht und warum: bremst den Sinkflug statt eines Fallschirms und soll eine zielgenaue Landung ermöglichen. Ein Bild für Laien hilft, z. B. der Ahornsamen. |
| Karte 03 | „Kamera & NDVI“ | Was die Kamera aufnimmt und **was NDVI ist** (Vegetationsindex: wie gesund Pflanzen sind, aus Bildern berechnet). Ohne Erklärung versteht kaum jemand den Begriff. |

### Abschnitt „Vom Test zum Flug“

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Vom Test zum Flug“ | Bleibt. |
| Überschrift | „Wir zeigen, was funktioniert – und was wir noch lernen.“ | Die Botschaft: Wir dokumentieren offen, auch was schiefgeht. |
| Text | „Auf der Ergebnisseite sammeln wir …“ | Ein Satz: was man auf der Ergebnisseite findet. |
| Button | „Zu den Ergebnissen“ | Führt zu „Flugergebnisse“. |
| Kasten: Titel | „Wir sind bei CanSat Austria dabei“ | Dass wir teilnehmen, gern mit Saison (z. B. 2026/27). |
| Kasten: Text und Link | „CanSat Austria ist der Wettbewerb …“ | Ein Satz, was CanSat Austria ist: Schulwettbewerb von ESERO Austria, Satellit in Getränkedosengröße. Dazu der Link zu ESERO. |

---

## Über uns (`ueber-uns.html`)

Die Seite heißt „Über uns“, beschreibt aber Mission und Technik. Die Motivation steht als eigener Abschnitt auf der Startseite. Der Endbericht verlangt eine Kurzvorstellung des Projekts, der Motivation und des Teams.

### Einstieg

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Brotkrumen | „Home / Über uns“ | Pfad zur Seite. Passt automatisch. |
| Kicker | „Mission & System“ | Bleibt. |
| Überschrift | „Ein CanSat sammelt Daten – und soll kontrolliert landen.“ | Die Mission in einem Satz. |
| Einleitung | „Team SWASH entwickelt einen Satelliten im Dosenformat …“ | 2 Sätze: was ein CanSat ist und was unseren Ansatz besonders macht. |

### Primärmission

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Primärmission“ | Bleibt. |
| Überschrift | „Temperatur und Luftdruck im Sinkflug messen.“ | Die vorgeschriebene Aufgabe in einem Satz. |
| Absatz 1 | „Unser CanSat soll Lufttemperatur und Luftdruck …“ | Was gemessen wird, wie oft (mindestens 1 Hz, Vorgabe aus dem Handbuch, Abschnitt 2.2.1), wohin übertragen und was ausgewertet wird. |
| Absatz 2 | „Die Flugsteuerung übernimmt ein ESP32-S3 …“ | Mikrocontroller festgelegt: ESP32-S3. |
| Infokasten | „Messung · Funk · Auswertung“, „1 Hz“, Satz darunter | Eine Kennzahl der Primärmission groß, darunter ein Satz, der die Zahl erklärt. |

### Das steckt im CanSat

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker und Überschrift | „Das steckt im CanSat“, „Ein kompaktes System mit mehreren Aufgaben.“ | Leiten die Karten ein. |
| Karte 01 | „Flugcomputer & Sensorik“ | ESP32-S3 und Sensoren: was gelesen und aufgezeichnet wird. |
| Karte 02 | „LoRa-Bodenstation“ | Wie die Daten zur Bodenstation kommen. Frequenz oder Reichweite ergänzen, sobald `protocol/telemetry.md` sie nennt. |
| Karte 03 | „Autorotationsrotor“ | Rotor, Taumelscheibe, Servos: wie gesteuert wird und wozu (stabiler Sinkflug, zielgenaue Landung). |
| Karte 04 | „Kamera & NDVI“ | Raspberry Pi CM0 (Compute Module Zero) mit Kamera: was aufgenommen wird, was NDVI ist, was wir auswerten. |

Kommt der Umgebungslicht-/UV-Sensor dazu, passt eine fünfte Karte mit demselben Aufbau.

### Entwicklungsstand

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Entwicklungsstand“ | Bleibt. |
| Überschrift | „Wir machen Fortschritte messbar.“ | Bleibt oder wird an den Stand angepasst. |
| Text | „In Rotor-Vorversuchen prüfen wir …“ | Der aktuelle Stand in 2–3 Sätzen: Rotorversuche, nächste Falltests und NDVI-Auswertung. Die Sekundärmission umfasst Rotorsteuerung und NDVI-Bildauswertung. Regelmäßig aktualisieren. |
| Button | „Zu den Test- und Flugergebnissen“ | Führt zu „Flugergebnisse“. |
| Karte | „Vom Versuch zur Auswertung“ mit drei Punkten | Unsere Arbeitsweise bei Versuchen in drei kurzen Punkten. Bleibt allgemein. |

---

## Team (`team.html`)

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Team SWASH“ | Bleibt. |
| Überschrift | „Vier Fachbereiche, ein gemeinsamer CanSat.“ | Wie das Team aufgebaut ist, in einem Satz. |
| Einleitung | „Wir sind ein sechsköpfiges Team des Jahrgangs 2023 an der HTL Kaindorf …“ | 1–2 Sätze. Schule, Jahrgang und Zahl der Mitglieder sind ergänzt. |
| Vier Karten: Titel | „Konstruktion“, „Elektronik“, „Programmierung“, „Wissenschaft“ | Name des Fachbereichs. |
| Vier Karten: Untertitel | „Mechanik & CAD“ usw. | Schwerpunkt in 2–3 Wörtern. |
| Vier Karten: Text | „Wir entwickeln Rotor, Gehäuse und Bauteile …“ | 1–2 Sätze, was der Bereich macht. Die Nachnamen von David, Felix und Gabriel wurden mit ihrer Freigabe ergänzt. |
| Abschnitt unten: Kicker und Überschrift | „Gemeinsam entwickeln“, „Vom ersten Entwurf bis zur Auswertung.“ | Leiten den Absatz ein. |
| Abschnitt unten: Text | „Die Fachbereiche arbeiten eng zusammen …“ | Wie die Bereiche zusammenarbeiten (Treffen, gegenseitige Prüfung). |
| Button | „Unsere Mission im Detail“ | Führt zu „Über uns“. |

Das Repo-`README.md` führt sieben Rollen, die Website nur vier Fachbereiche. Socials, Team Lead und Hardware fehlen.

---

## Flugergebnisse (`flugergebnisse.html`)

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Test & Flug“ | Bleibt. |
| Überschrift | „Was wir messen, teilen wir.“ | Bleibt. |
| Einleitung | „Hier dokumentieren wir Vorversuche …“ | Was auf der Seite steht, und klar gesagt: stammen die Daten aus einem Versuch oder aus dem Flug? Nach dem Flug neu schreiben. |
| Kicker | „Aktueller Stand“ | Bleibt. |
| Überschrift | „Rotor-Vorversuch am Autofenster“ | Name des Versuchs, wie er unter `tests/` heißt. |
| Beschreibung | „Ein früher Versuch mit einem 96,9-g-Testmodell …“ | Versuchsaufbau in 1–2 Sätzen: Testmodell und Masse, Blattwinkel, Art der Anströmung. Quelle: `tests/04-passive-rotor-car-window-test/`. |
| Tabelle | Lauf, Fahrgeschwindigkeit, Gemessene Kraft, Winkel | Messwerte aus `results.md` mit Einheiten. Die Kraftwerte sind bereits um den Nullwert der Federwaage (0,7 N ohne Last) bereinigt. Lauf 2 und 3 sind Wiederholungen. |
| Hinweisbox | „Einordnung: Für einen vollständigen CanSat …“ | Schätzung ca. 19–22 m/s für einen 300-g-CanSat; die Richtlinien 2026 (Punkt 11) verlangen 8–11 m/s, bei geplanter Zielandung 6 m/s. Nächste Schritte: kleinerer Blattwinkel, größerer Rotor, Falltests. |
| Abschnitt „Nach dem Start“: Kicker, Überschrift, Text | „Die Flugauswertung kommt hier dazu.“ | Platzhalter bis zum Flug. Danach: Diagramme zu Temperatur, Druck und Höhe, Flugphasen, Landegenauigkeit, was wir gelernt haben (wie im Endbericht unter „Flugauswertung“). |
| Button | „Mehr über unsere Mission“ | Führt zu „Über uns“. |
| Karte | „CanSat Austria“ mit Text und Link | Ein Satz zum Rahmen des Wettbewerbs, dazu der Link. |

Sobald weitere Versuche Ergebnisse haben (Falttest 01, Falltests 03), bekommt jeder einen eigenen Block mit Überschrift, Aufbau, Tabelle und Einordnung.

---

## Kontakt (`kontakt.html`)

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker | „Kontakt“ | Bleibt. |
| Überschrift | „Was möchten Sie gemeinsam möglich machen?“ | Eine Einladung an die, die uns schreiben sollen: Sponsoren, Schulen, Presse, Interessierte. Der heutige Satz klingt nach Agentur-Vorlage. |
| Einleitung | „Das Kontaktformular ist vorbereitet, wird derzeit aber …“ | 1–2 Sätze: wer sich wofür melden kann (Sponsoring, Fragen, Medienanfragen). Den Hinweis zum Formular hier streichen, er steht schon zweimal im Formular. |
| Formulartitel | „Nachricht vorbereiten“ | Titel des Formulars, z. B. „Nachricht senden“, sobald der Versand funktioniert. |
| Hinweis über den Feldern | „Alle Felder außer Telefonnummer sind erforderlich …“ | Welche Felder Pflicht sind. Den Satz zum fehlenden Versand streichen, sobald das Formular angebunden ist. |
| Feldbeschriftungen | „Name *“, „E-Mail *“, „Telefonnummer“, „Nachricht *“ | Kurze Feldnamen, * heißt Pflichtfeld. |
| Button | „Formular absenden“ | Kurz, z. B. „Nachricht senden“. |
| Hinweis unter dem Button | „Diese statische Demo übermittelt …“ | Kurze Datenschutz-Info: wohin die Daten gehen, Link zur Datenschutzerklärung. Den Demo-Satz streichen, sobald das Formular angebunden ist. |
| Meldung nach dem Absenden (in `assets/site.js`, DE und EN) | „Danke. Die Eingaben sind gültig; …“ | Bestätigung nach dem Senden, nach der Anbindung z. B. „Danke, wir melden uns.“ |
| Karte „Team SWASH“ | „Wir entwickeln unseren CanSat …“ mit ESERO-Link | 1–2 Sätze, wer wir sind. Schule und Schuladresse passen hierher. |
| Karte „Direkt Kontakt“: Titel | „Direkt Kontakt“ | Grammatisch richtig: „Direkter Kontakt“. |
| Ansprechpersonen | Name, Rolle, E-Mail (3 Personen) | Ansprechpersonen mit Rolle. „Team Leader“ ist auf der deutschen Seite englisch („Teamleitung“ wäre deutsch). Die Schreibweise der Adressen ist uneinheitlich (`HTL-Kaindorf.at` und `htl-kaindorf.at`). Eine gemeinsame Teamadresse wäre eine Alternative zu persönlichen Adressen. |

---

## Impressum (`impressum.html`)

Die Vorlage ist für ein **Unternehmen** geschrieben (Wirtschaftskammer, Firmenbuch, UID, Gewerbebehörde). Für ein Schulprojekt ist zuerst zu klären, wer Medieninhaber ist: die Schule, eine volljährige Betreuungsperson oder ein Verein. Davon hängt ab, welche Angaben nötig sind. Vor der Veröffentlichung von der Schule oder einer fachkundigen Person prüfen lassen.

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker und Überschrift | „Rechtliches“, „Impressum“ | Bleiben. |
| Einleitung | „Angaben gemäß § 5 ECG …“ | Auf welcher Rechtsgrundlage die Angaben stehen. An den tatsächlichen Fall anpassen. |
| Hinweisbox | „Platzhalter bitte vollständig ersetzen.“ | Fällt weg, wenn alle Angaben eingetragen sind. |
| Medieninhaber und Diensteanbieter | Platzhalter für Name, Adresse, Telefon, E-Mail, Domain | Wer für die Website verantwortlich ist, mit Anschrift und Kontakt. Dieselbe Stelle wie „Verantwortlicher“ in der Datenschutzerklärung. |
| Unternehmensangaben | Platzhalter für WKO, Gewerbebehörde, Firmenbuch, UID … | Nur nötig, wenn ein Unternehmen dahintersteht. Sonst fällt der Abschnitt weg. |
| Offenlegung nach § 25 Mediengesetz | Platzhalter für Medieninhaber, Gegenstand, Blattlinie | Medieninhaber, Gegenstand (z. B. „Schulprojekt im Rahmen von CanSat Austria“), Blattlinie (z. B. „Information über das CanSat-Projekt von Team SWASH“). |
| Online-Streitbeilegung | „Die frühere EU-Plattform …“ | Betrifft vor allem Verkäufe an Verbraucher. Prüfen, ob der Abschnitt für uns nötig ist. |
| Haftung für Inhalte, Haftung für Links | Standardtexte | Können bleiben. |
| Urheberrecht | Standardtext | Kann bleiben. Optional: von wem Fotos und Videos stammen. |

---

## Datenschutz (`datenschutz.html`)

Die Vorlage ist für eine **Unternehmenswebsite** geschrieben. Viele Angaben hängen vom Hosting ab und lassen sich erst ausfüllen, wenn feststeht, wo die Website liegt.

| Element | Aktuell | Was dort hinkommen soll |
|---|---|---|
| Kicker und Überschrift | „Datenschutz“, „Datenschutzerklärung“ | Bleiben. |
| Einleitung | „Muster für eine einfache österreichische Unternehmenswebsite · Stand: Oktober 2026“ | Nur noch „Stand: Monat Jahr“. |
| Hinweisbox | „Wichtig: Mustertext mit Platzhaltern.“ | Fällt weg, wenn alles ausgefüllt ist. |
| 1. Verantwortlicher | Platzhalter für Name, Adresse, E-Mail, Telefon, Datenschutzbeauftragten | Wer für die Daten verantwortlich ist, dieselbe Stelle wie der Medieninhaber im Impressum. Ob ein Datenschutzbeauftragter bestellt ist. |
| 2. Allgemeine Informationen | Grundsätze und Rechtsgrundlagen | Standardtext, kann bleiben. |
| 3. Server-Protokolle | Platzhalter für Hoster, Speicherfrist, Empfänger | Name und Anschrift des Hosters, wie lange er Zugriffsprotokolle speichert, wer die Daten verarbeitet. Steht im Vertrag bzw. Auftragsverarbeitungsvertrag des Hosters. |
| 4. Kontaktaufnahme und Kontaktformular | drei Absätze, Platzhalter für Löschfrist | Wie E-Mail-Anfragen verarbeitet werden. Den Formular-Absatz neu schreiben, sobald der Versand angebunden ist (wohin, welcher Dienst). Eine Löschfrist für Anfragen festlegen. „Vorvertragliche Maßnahmen“ ist Firmensprache. |
| 5. Cookies, Analyse und externe Inhalte | „Diese Website setzt derzeit keine …“ | Genau, was im Browser gespeichert wird: Hell/Dunkel, **Sprache (fehlt heute)** und die Bestätigung des Hinweises. **Den Satz über Wikimedia Commons streichen**, er ist ein Überbleibsel (das Logo liegt lokal). Mit Video oder anderen Einbettungen hier ergänzen. |
| 6. Empfänger und Drittländer | Platzhalter | Liste der Dienstleister (Hoster, ggf. Formulardienst) und ob Daten außerhalb der EU landen. Bei einem US-Hoster ist das der Fall. |
| 7. Speicherdauer | Platzhalter | Speicherfrist pro Verarbeitung (Server-Protokolle, Anfragen). |
| 8. Ihre Rechte | Rechte nach DSGVO, Datenschutzbehörde | Standardtext, bleibt. |
| 9. Pflicht zur Bereitstellung | „Beim bloßen Besuch …“ | Standardtext. Die Stelle zu „Vertrag“ und „Leistung“ passt nicht zu uns und kann einfacher werden. |
| 10. Automatisierte Entscheidungen | Platzhalter | Bei dieser Website gibt es keine, also „findet nicht statt“. |
| 11. Aktualisierung | Standardtext | Bleibt. |

---

## AGB (`agb.html`)

Das sind **Muster-AGB für Beratungs- und Kreativleistungen** eines Unternehmens. Team SWASH verkauft derzeit nichts, die Seite ist dann vermutlich überflüssig. Im Team (und mit der Schule) klären, ob sie wegfällt. Dann auch die AGB-Links im Fußbereich aller Seiten entfernen. Bleibt sie (z. B. für Merch oder Sponsorpakete), muss sie neu geschrieben werden.

| Element | Aktuell | Was dort hinkommen soll, falls die Seite bleibt |
|---|---|---|
| Kicker, Überschrift, Einleitung | „Rechtliches“, „Allgemeine Geschäftsbedingungen“, „Muster für Dienstleistungen …“ | Titel und „Stand: Monat Jahr“. |
| Hinweisbox | „Bitte vor Verwendung anpassen …“ | Fällt weg, wenn fertig. |
| 1. Geltungsbereich | Platzhalter für Firmenname | Wer anbietet und für welche Leistungen die Bedingungen gelten. |
| 2. Angebote und Vertragsabschluss | Platzhalter für Gültigkeit | Wann ein Kauf oder eine Vereinbarung zustande kommt. |
| 3. Leistungen und Mitwirkung | Standardtext | Was geliefert wird und was der Kunde beitragen muss. |
| 4. Entgelt und Zahlung | Platzhalter für Zahlungsfrist | Preise, Zahlungsart, Frist. |
| 5. Termine und höhere Gewalt | Standardtext | Lieferzeiten, Verzögerungen. |
| 6. Abnahme und Korrekturen | Platzhalter für Prüffrist | Nur bei Dienstleistungen, sonst streichen. |
| 7. Nutzungsrechte | Standardtext | Nur bei Dienstleistungen, sonst streichen. |
| 8. Rücktritt und Vertragsbeendigung | Platzhalter für Kündigungsfrist | Rücktrittsrecht für Verbraucher. |
| 9. Gewährleistung und Haftung | Standardtext | Gesetzliche Gewährleistung, Haftung. |
| 10. Vertraulichkeit und Datenschutz | Standardtext | Verweis auf die Datenschutzerklärung. |
| 11. Schlussbestimmungen | Platzhalter für Firma und Fassung | Anwendbares Recht, Gerichtsstand, Datum der Fassung. |

---

## Offene Punkte vor der Veröffentlichung

1. **Impressum und Datenschutz:** Medieninhaber bzw. Verantwortlicher und Hosting sind noch nicht festgelegt. Die bestehenden Rechtstexte bleiben bis dahin Vorlagen.
2. **AGB:** Entscheiden, ob die Musterseite gelöscht wird; bis dahin bleiben Seite und Footer-Link bestehen.
3. **Kontaktformular:** Entscheiden, ob ein Versanddienst angebunden oder das Formular entfernt wird. Bis dahin weist die Seite darauf hin, dass es nicht versendet.
4. **Sponsoren:** Entscheiden, ob ein eigener Abschnitt für Sponsoren und Unterstützer ergänzt wird.
5. **Datenschutzhinweis:** Sprache wird lokal gespeichert, ist dort aber noch nicht genannt. Der Verweis auf Wikimedia Commons in der Datenschutzerklärung ist ebenfalls zu prüfen.
6. **Fotos und Video:** Platzhalter auf der Startseite erst ersetzen, wenn echte Medien samt passenden Bildunterschriften vorliegen.
