#!/usr/bin/env python3
"""Keep the website consistent with data/*.yaml.

    python scripts/taxonomy.py check      # validate data, pages and navigation
    python scripts/taxonomy.py generate   # rewrite the generated blocks in docs/

Generated blocks are delimited in the Markdown files by
`<!-- BEGIN GENERATED:name -->` ... `<!-- END GENERATED:name -->`.
Never edit what is inside them by hand.
"""
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = "taxonomy/index.md"
VALIDATION = "validation/census-income.md"
# Expected totals reported in Table 1 of the paper (version -> number of change types).
REPORTED_TOTALS = {"D1": 3, "D2": 3, "D3": 7, "D4": 7, "D5": 4, "D6": 4, "D7": 5, "D8": 9, "D9": 6}


def load():
    tax = yaml.safe_load((ROOT / "data/taxonomy.yaml").read_text())["taxonomy"]
    ver = yaml.safe_load((ROOT / "data/census-income-versions.yaml").read_text())
    return tax, ver


def walk(nodes, parents=()):
    for n in nodes:
        yield n, parents
        yield from walk(n.get("children", []), parents + (n,))


def leaves(tax):
    return [n for n, _ in walk(tax) if not n.get("children")]


def rel(page, from_page):
    """Relative link from one docs page to another."""
    return Path(os.path.relpath(DOCS / page, (DOCS / from_page).parent)).as_posix()


def replace_block(page, name, content):
    path = DOCS / page
    text = path.read_text()
    pat = re.compile(rf"(<!-- BEGIN GENERATED:{name} -->).*?(<!-- END GENERATED:{name} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"ERROR: {page} has no GENERATED:{name} block")
    path.write_text(pat.sub(lambda m: f"{m.group(1)}\n\n{content.strip()}\n\n{m.group(2)}", text))


def check():
    tax, ver = load()
    errors = []
    keys = [n["key"] for n, _ in walk(tax)]
    for k in {k for k in keys if keys.count(k) > 1}:
        errors.append(f"duplicate key: {k}")

    nav_text = (ROOT / "zensical.toml").read_text()
    pages = set()
    for n, _ in walk(tax):
        is_leaf = not n.get("children")
        is_dim = n in tax
        if is_leaf or is_dim:
            page = n.get("page")
            if not page:
                errors.append(f"{n['key']}: missing `page`")
                continue
            pages.add(page)
            if not (DOCS / page).exists():
                errors.append(f"{n['key']}: page {page} does not exist")
            if page not in nav_text:
                errors.append(f"{n['key']}: page {page} is not in `nav` of zensical.toml")
            elif (DOCS / page).exists():
                body = (DOCS / page).read_text()
                block = "observed" if is_leaf else "types"
                if f"<!-- BEGIN GENERATED:{block} -->" not in body:
                    errors.append(f"{page}: missing GENERATED:{block} block")

    for f in (DOCS / "taxonomy").rglob("*.md"):
        p = f.relative_to(DOCS).as_posix()
        if p != INDEX and p not in pages:
            errors.append(f"orphan page not in taxonomy.yaml: {p}")

    leaf_keys = {n["key"] for n in leaves(tax)}
    for v in ver["versions"]:
        unknown = set(v["changes"]) - leaf_keys
        if unknown:
            errors.append(f"{v['id']}: unknown change types {sorted(unknown)}")
        if v["id"] in REPORTED_TOTALS and len(set(v["changes"])) != REPORTED_TOTALS[v["id"]]:
            errors.append(f"{v['id']}: {len(set(v['changes']))} changes, paper reports {REPORTED_TOTALS[v['id']]}")

    for e in errors:
        print("ERROR:", e)
    if not errors:
        print(f"OK: {len(leaf_keys)} change types, {len(tax)} dimensions, {len(ver['versions'])} dataset versions.")
    return 1 if errors else 0


def generate():
    tax, ver = load()
    versions = ver["versions"]
    n_ver = len(versions)

    # --- taxonomy overview: tree diagram and index ---------------------------------
    lines, ids = ["```mermaid", "flowchart LR", '    root(["Dataset changes"])'], {}
    for i, (n, parents) in enumerate(walk(tax)):
        ids[n["key"]] = f"n{i}"
        lines.append(f'    n{i}["{n["name"]}"]')
        lines.append(f"    {ids[parents[-1]['key']] if parents else 'root'} --> n{i}")
    lines.append("```")
    replace_block(INDEX, "tree", "\n".join(lines))

    rows = ["| Change type | Dimension |", "|---|---|"]
    for dim in tax:
        for leaf in ([dim] if not dim.get("children") else [n for n, _ in walk(dim["children"]) if not n.get("children")]):
            rows.append(f"| [{leaf['name']}]({rel(leaf['page'], INDEX)}) | [{dim['name']}]({rel(dim['page'], INDEX)}) |")
    replace_block(INDEX, "index", "\n".join(rows))

    # --- dimension pages: list of their change types ---------------------------------
    for dim in tax:
        if not dim.get("children"):
            continue

        def bullets(nodes, depth=0):
            out = []
            for n in nodes:
                label = f"[{n['name']}]({rel(n['page'], dim['page'])})" if n.get("page") else f"**{n['name']}**"
                out.append("  " * depth + f"- {label}")
                out += bullets(n.get("children", []), depth + 1)
            return out

        replace_block(dim["page"], "types", "\n".join(bullets(dim["children"])))

    # --- change type pages: where it was observed ------------------------------------
    for leaf in leaves(tax):
        seen = [v["id"] for v in versions if leaf["key"] in v["changes"]]
        link = rel(VALIDATION, leaf["page"])
        if seen:
            txt = (f"Observed in **{len(seen)} of {n_ver}** analysed versions of the "
                   f"[Census Income dataset]({link}): {', '.join(seen)}.")
        else:
            txt = f"Not observed in the {n_ver} analysed versions of the [Census Income dataset]({link})."
        replace_block(leaf["page"], "observed", txt)

    # --- validation page ---------------------------------------------------------------
    vrows = ["| ID | Version |", "|---|---|"] + [f"| {v['id']} | [{v['name']}]({v['url']}) |" for v in versions]
    replace_block(VALIDATION, "versions", "\n".join(vrows))

    head = ["Change type", *[v["id"] for v in versions], "Total"]
    m = ["| " + " | ".join(head) + " |", "|---|" + "---|" * (len(head) - 1)]
    for leaf in leaves(tax):
        marks = ["✔" if leaf["key"] in v["changes"] else "" for v in versions]
        total = sum(1 for x in marks if x)
        m.append(f"| [{leaf['name']}]({rel(leaf['page'], VALIDATION)}) | " + " | ".join(marks) + f" | {total} |")
    m.append("| **Total** | " + " | ".join(f"**{len(set(v['changes']))}**" for v in versions) + " | |")
    replace_block(VALIDATION, "matrix", "\n".join(m))
    print("Generated blocks updated.")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"check": check, "generate": generate}.get(cmd, lambda: print(__doc__) or 2)())
