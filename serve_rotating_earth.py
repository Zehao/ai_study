"""Quickly serve the rotating Earth web demo on localhost."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os


def main() -> None:
    root = Path(__file__).resolve().parent
    port = 8000

    os.chdir(root)

    handler = SimpleHTTPRequestHandler
    httpd = ThreadingHTTPServer(("0.0.0.0", port), handler)

    print("Serving rotating_earth_web.html at:")
    print(f"  http://localhost:{port}/rotating_earth_web.html")
    print("Press Ctrl+C to stop.")

    try:
        # Serve files out of the repo root so the HTML can load textures from the CDN.
        httpd.serve_forever()
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
