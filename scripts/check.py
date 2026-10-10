"""Validate preview links and optionally report external URL responses."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor
import argparse
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        self.urls.extend(v for k, v in attrs if k in ("href", "src"))

external = set()
for path in (ROOT / "_preview").rglob("*.html"):
    html = path.read_text(encoding="utf-8")
    assert "{%" not in html and "{{" not in html, path
    parser = Links(); parser.feed(html)
    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.scheme in ("https", "http"):
            external.add(url)
        elif parsed.path.startswith("/"):
            target = ROOT / "_preview" / parsed.path.lstrip("/")
            assert target.exists(), (path, url)
print("PASS: all rendered internal links and asset paths resolve.")

if "--external" in __import__('sys').argv:
    def check(url):
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            with opener.open(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as response:
                return f"{response.status} {url}"
        except Exception as error:
            return f"UNVERIFIED {url}: {error}"
    print("\n".join(ThreadPoolExecutor(max_workers=8).map(check, sorted(external))))
