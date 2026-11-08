#!/bin/sh
# Stellt zusammen, was Cloudflare veröffentlicht (Ordner dist/).
# Build command in Cloudflare: sh tools/build-dist.sh
#
# Nur was hier steht, kommt auf die Website. README, Guides, social/ und tools/
# bleiben bewusst draußen. Neue Ordner für die Website hier ergänzen.
set -e
rm -rf dist
mkdir -p dist
cp -r ./*.html ./*.ico ./*.txt ./*.xml assets en dist/
echo "dist/: $(find dist -type f | wc -l) Dateien"
