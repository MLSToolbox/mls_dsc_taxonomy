#!/usr/bin/env python3
"""Keep the website consistent with data/taxonomy.yaml.

    python scripts/taxonomy.py generate   # rewrite generated blocks (docs/ and menu)
    python scripts/taxonomy.py check      # validate data, pages and navigation

Generated parts (never edit them by hand):
  * in Markdown:  <!-- BEGIN GENERATED:name --> ... <!-- END GENERATED:name -->
                  (blocks: types, tree, index)
  * in zensical.toml:  # BEGIN GENERATED:nav ... # END GENERATED:nav
"""
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TOML = ROOT / "zensical.toml"
INDEX = "taxonomy/index.md"


def load():
    d = yaml.safe_load((ROOT / "data/taxonomy.yaml").read_text())
    return d.get("root", "Dataset differences"), d["taxonomy"]


def walk(nodes, parents=()):
    for n in nodes:
        yield n, parents
        yield from walk(n.get("children", []), parents + (n,))


def leaves(tax):
    return [n for n, _ in walk(tax) if not n.get("children")]


def page_ancestors(parents):
    """Ancestors that have a page of their own (groupings are skipped)."""
    return [p for p in parents if p.get("page")]

def rel(page, from_page):
    """Relative link from one docs page to another."""
    return Path(os.path.relpath(DOCS / page, (DOCS / from_page).parent)).as_posix()

def site_url(page, from_page):
    """Relative URL of `page` as served by the built site (directory URLs, no .md).

    Mermaid `click` URLs are not rewritten by the Markdown processor, so they must be
    written in their final form: schema/columns-set/index.md -> schema/columns-set/
    """
    r = rel(page, from_page)
    if r == "index.md" or r.endswith("/index.md"):
        return r[: -len("index.md")]
    return r[: -len(".md")] + "/"

def replace_block(page, name, content):
    path = DOCS / page
    text = path.read_text()
    pat = re.compile(rf"(<!-- BEGIN GENERATED:{name} -->).*?(<!-- END GENERATED:{name} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"ERROR: {page} has no GENERATED:{name} block")
    path.write_text(pat.sub(lambda m: f"{m.group(1)}\n\n{content.strip()}\n\n{m.group(2)}", text))


def toml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def nav_items(nodes, depth):
    out, pad = [], "  " * depth
    for n in nodes:
        kids = n.get("children", [])
        if n.get("nav") is False:                      # hidden grouping: promote children
            out += nav_items(kids, depth)
        elif not kids:
            out.append(f"{pad}{toml_str(n['page'])},")
        else:
            out.append(f"{pad}{{ {toml_str(n['name'])} = [")
            if n.get("page"):
                out.append(f"{pad}  {toml_str(n['page'])},")
            out += nav_items(kids, depth + 1)
            out.append(f"{pad}] }},")
    return out


def check():
    _, tax = load()
    errors = []
    keys = [n["key"] for n, _ in walk(tax)]
    for k in sorted({k for k in keys if keys.count(k) > 1}):
        errors.append(f"duplicate key: {k}")

    toml = TOML.read_text()
    if "# BEGIN GENERATED:nav" not in toml:
        errors.append("zensical.toml has no '# BEGIN GENERATED:nav' / '# END GENERATED:nav' markers")

    pages = set()
    for n, parents in walk(tax):
        kids, page = n.get("children"), n.get("page")
        if not kids and not page:
            errors.append(f"{n['key']}: change types need a `page`")
        if not page:
            continue
        pages.add(page)
        path = DOCS / page
        if not path.exists():
            errors.append(f"{n['key']}: page {page} does not exist")
            continue
        body = path.read_text()
        if page not in toml:
            errors.append(f"{n['key']}: {page} is not in the menu (run `generate`)")
        if kids and "<!-- BEGIN GENERATED:types -->" not in body:
            errors.append(f"{page}: missing GENERATED:types block")

    for f in (DOCS / "taxonomy").rglob("*.md"):
        p = f.relative_to(DOCS).as_posix()
        if p != INDEX and p not in pages:
            errors.append(f"orphan page not in taxonomy.yaml: {p}")

    for e in errors:
        print("ERROR:", e)
    if not errors:
        print(f"OK: {len(leaves(tax))} change types, {len(pages)} pages.")
    return 1 if errors else 0


def generate():
    root, tax = load()

    # --- overview: tree diagram and index -------------------------------------------
    lines, ids = ["```mermaid", "flowchart LR", f'    root(["{root}"])'], {}
    for i, (n, parents) in enumerate(walk(tax)):
        ids[n["key"]] = f"n{i}"
        lines.append(f'    n{i}["{n["name"]}"]')
        lines.append(f"    {ids[parents[-1]['key']] if parents else 'root'} --> n{i}")
    for n, _ in walk(tax):                       # clickable nodes: those with a page
        if n.get("page"):
            lines.append(f'    click {ids[n["key"]]} "{site_url(n["page"], INDEX)}" "{n["name"]}"')
    lines.append("```")
    replace_block(INDEX, "tree", "\n".join(lines))

    rows = ["| Difference category | Location |", "|---|---|"]
    for n, parents in walk(tax):
        if n.get("children"):
            continue
        loc = " › ".join(f"[{a['name']}]({rel(a['page'], INDEX)})" for a in page_ancestors(parents)) or "—"
        rows.append(f"| [{n['name']}]({rel(n['page'], INDEX)}) | {loc} |")
    replace_block(INDEX, "index", "\n".join(rows))

    # --- non-leaf pages: list of contents ----------------------------------------------
    for n, parents in walk(tax):
        page = n.get("page")
        if not page:
            continue
        if n.get("children"):
            def bullets(nodes, depth=0):
                out = []
                for c in nodes:
                    label = f"[{c['name']}]({rel(c['page'], page)})" if c.get("page") else f"**{c['name']}**"
                    out.append("    " * depth + f"- {label}")
                    out += bullets(c.get("children", []), depth + 1)
                return out
            replace_block(page, "types", "\n".join(bullets(n["children"])))

    # --- menu ---------------------------------------------------------------------------
    items = [f"    {toml_str(INDEX)},"] + nav_items(tax, 2)
    toml = TOML.read_text()
    pat = re.compile(r"([ \t]*# BEGIN GENERATED:nav\n).*?([ \t]*# END GENERATED:nav)", re.S)
    if not pat.search(toml):
        raise SystemExit("ERROR: zensical.toml has no '# BEGIN GENERATED:nav' / '# END GENERATED:nav' markers")
    TOML.write_text(pat.sub(lambda m: m.group(1) + "\n".join(items) + "\n" + m.group(2), toml))

    print("Generated blocks and menu updated.")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"check": check, "generate": generate}.get(cmd, lambda: print(__doc__) or 2)())
