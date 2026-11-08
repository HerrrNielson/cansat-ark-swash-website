# Team SWASH – Website-Muster

Statische, responsive Mehrseiten-Website mit HTML5, CSS3 und JavaScript. Es wird kein Build-Schritt benötigt.

## Lokal öffnen

index.html im Browser öffnen. Für eine Vorschau mit lokalem Webserver können Sie im Projektordner beispielsweise python -m http.server 8000 starten und http://localhost:8000 öffnen.

## Seiten

- index.html – kurze Vorstellung der Mission mit Video-Platzhalter
- ueber-uns.html – Mission und technischer Aufbau
- team.html – Aufgabenbereiche des Teams
- flugergebnisse.html – Vorversuche und spätere Flugmessungen
- simulation.html – Launch-Day-Simulation der Bodenstation zum Ausprobieren, eingebettet aus assets/simulation/launch-day-simulation.html (Kopie aus dem Haupt-Repo, ground-station/web-sim/). Beim ersten Besuch erscheint eine kurze Anleitung, danach nur über „Anleitung anzeigen“.
- kontakt.html – Kontaktangaben und Formular
- Header und Footer zeigen das lokale SWASH-Logo aus assets/swash-logo.png.
- impressum.html – österreichisches Impressum-Muster
- datenschutz.html – Datenschutz-Muster passend zur statischen Demo
- robots.txt und sitemap.xml – für Suchmaschinen; bei neuen Seiten die sitemap.xml ergänzen
- assets/styles.css – responsive Gestaltung mit zurückhaltenden Marineblau- und Sandtönen und sanften Verläufen
- assets/site.js – mobiles Menü, Hell-/Dunkelmodus, Datenschutz-Hinweis, Formularhinweis und dynamisches Jahr
- assets/translations.js – deutsche und englische Texte für die Sprachumschaltung
- Beim ersten Besuch erscheint ein Datenschutz- und Cookie-Hinweis; seine Bestätigung wird lokal im Browser gespeichert.

## Vor Veröffentlichung anpassen

Ersetzen Sie alle gelb markierten rechtlichen Platzhalter und ergänzen Sie echte Kontaktinformationen. Das Video auf der Startseite ist ein Platzhalter. Das Kontaktformular sendet über Web3Forms (https://web3forms.com). Dort mit der Team-Adresse einen Access Key anfordern und in kontakt.html beim Attribut data-access-key statt WEB3FORMS_ACCESS_KEY eintragen. Der Key ist öffentlich und darf im HTML stehen. Ohne Key zeigt das Formular nur einen Hinweis auf die E-Mail-Adressen.

Für Vorschauen beim Teilen (WhatsApp, Instagram, LinkedIn) hat jede Seite Open-Graph-Tags mit assets/og-image.jpg (1200 × 630). Bei neuen Seiten die Tags mitkopieren und og:title, og:description und og:url anpassen.

Datenschutz und Impressum sind Mustertexte und müssen auf das tatsächliche Unternehmen, Geschäftsmodell, Hosting und alle eingesetzten Dienste abgestimmt werden.

## Foto der Woche

Startseite, die Seite foto-der-woche.html und die Instagram-Posts entstehen jede Woche mit einem Befehl aus social/wochenfotos.json:

    python social/foto_der_woche.py

Ablauf, Regeln für Fotos und Texte und das Layout der Posts stehen in social/DESIGN-FOTO-DER-WOCHE.md.
