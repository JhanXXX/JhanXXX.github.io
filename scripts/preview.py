"""Local preview of the shared Liquid templates; GitHub Pages builds with Jekyll.

Usage: python scripts/preview.py [--build-only] [--baseurl /example]
"""
from pathlib import Path
import argparse
import functools
import http.server
import re
import shutil
import markdown
import yaml
from liquid import Environment, DictLoader

ROOT = Path(__file__).resolve().parents[1]


def build(baseurl=""):
    site = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    site["baseurl"] = baseurl.rstrip("/")
    site["data"] = {p.stem: yaml.safe_load(p.read_text(encoding="utf-8")) for p in (ROOT / "_data").glob("*.yml")}
    site["static_files"] = [{"path": "/" + p.relative_to(ROOT).as_posix()} for p in (ROOT / "assets").rglob("*") if p.is_file()]
    # Jekyll permits unquoted include filenames; Python Liquid uses strings.
    def source(text):
        return re.sub(r"({%\s*include\s+)([\w./-]+)(\s*%})", r"\1'\2'\3", text)
    includes = {p.name: source(p.read_text(encoding="utf-8")) for p in (ROOT / "_includes").glob("*.html")}
    env = Environment(loader=DictLoader(includes))
    env.add_filter("relative_url", lambda value: site["baseurl"] + "/" + str(value).lstrip("/"))
    out = ROOT / "_preview"
    destination = out / baseurl.strip("/")
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "assets", destination / "assets", dirs_exist_ok=True)
    layout = env.from_string(source((ROOT / "_layouts/default.html").read_text(encoding="utf-8")))
    for name in ["about", "education", "publications", "experience", "steam"]:
        raw = (ROOT / (name + ".md")).read_text(encoding="utf-8")
        _, frontmatter, body = raw.split("---", 2)
        page = yaml.safe_load(frontmatter)
        page["url"] = page["permalink"]
        rendered = env.from_string(source(body)).render(site=site, page=page)
        content = markdown.markdown(rendered, extensions=["extra", "sane_lists"])
        html = layout.render(site=site, page=page, content=content)
        target = destination / page["url"].strip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
    print("Built five pages in", destination, flush=True)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--port", default=4000, type=int)
    args = parser.parse_args()
    out = build(args.baseurl)
    if not args.build_only:
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(out))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
        print(f"Local preview: http://127.0.0.1:{args.port}{args.baseurl}/", flush=True)
        server.serve_forever()
