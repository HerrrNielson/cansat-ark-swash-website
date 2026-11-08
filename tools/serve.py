"""Lokale Vorschau mit sauberen URLs wie auf Cloudflare (/team liefert team.html).

    python tools/serve.py          # http://localhost:8000
    python tools/serve.py 8765     # anderer Port
"""

import http.server
import sys
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = Path(super().translate_path(path))
        if not local.exists() and local.suffix == "" and local.with_suffix(".html").is_file():
            return str(local.with_suffix(".html"))
        return str(local)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = partial(CleanUrlHandler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"Vorschau: http://localhost:{port}")
        server.serve_forever()
