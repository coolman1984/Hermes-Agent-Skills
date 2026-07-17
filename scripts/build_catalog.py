#!/usr/bin/env python3
"""Rebuild catalog.json from the on-disk skills tree + taxonomy.yaml.

Single source of truth for the machine catalog. Walks every
`skills/<domain>/<skill>/SKILL.md`, reads its YAML frontmatter, records which
bundled resource folders exist, and emits `catalog.json` in the repo root.

Domain titles, summaries, ordering, and membership come from `taxonomy.yaml`.
`original_category` is not stored on disk, so it is preserved from the existing
`catalog.json` when present.

Usage:
    python3 scripts/build_catalog.py            # rebuild catalog.json
    python3 scripts/build_catalog.py --check     # verify only, write nothing (CI-friendly)

Exit codes: 0 = clean, 1 = drift detected (missing/extra skills, or --check found
the catalog out of date). No third-party deps beyond PyYAML.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"
TAXONOMY = REPO / "taxonomy.yaml"
CATALOG = REPO / "catalog.json"
INDEX_HTML = REPO / "docs" / "index.html"
INDEX_MARKER = "/*__CATALOG_DATA__*/"
SOURCE_LABEL = "Hermes Agent skills library (live export)"


def parse_frontmatter(skill_md: Path) -> dict:
    """Return the YAML frontmatter block of a SKILL.md as a dict (empty if none)."""
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    # Split on the frontmatter fences: text is "---\n<yaml>\n---\n<body>".
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}
    block = parts[0][len("---"):]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def collect_disk_skills() -> dict[str, set[str]]:
    """Map domain-id -> set of skill folder names that contain a SKILL.md."""
    found: dict[str, set[str]] = {}
    for domain_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        names = {
            skill_dir.name
            for skill_dir in domain_dir.iterdir()
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").is_file()
        }
        found[domain_dir.name] = names
    return found


def build_skill_entry(domain_id: str, name: str, prev: dict) -> dict:
    skill_dir = SKILLS_DIR / domain_id / name
    fm = parse_frontmatter(skill_dir / "SKILL.md")

    # Tags live either at the top level (`tags: [...]`) or nested under
    # `metadata.hermes.tags`. Accept whichever the author used.
    hermes_meta = ((fm.get("metadata") or {}).get("hermes")) or {}
    tags = hermes_meta.get("tags")
    if tags is None:
        tags = fm.get("tags")
    if tags is None:
        tags = []
    if not isinstance(tags, list):
        tags = [str(tags)]

    # Descriptions may be folded across lines in YAML; collapse to one line.
    description = re.sub(r"\s+", " ", (fm.get("description") or "")).strip()

    return {
        "name": name,
        "domain": domain_id,
        "original_category": prev.get(name, {}).get("original_category", ""),
        "description": description,
        "path": f"skills/{domain_id}/{name}",
        "tags": tags,
        "version": str(fm.get("version") or ""),
        "author": str(fm.get("author") or ""),
        "license": str(fm.get("license") or ""),
        "has_references": (skill_dir / "references").is_dir(),
        "has_templates": (skill_dir / "templates").is_dir(),
        "has_scripts": (skill_dir / "scripts").is_dir(),
        "has_assets": (skill_dir / "assets").is_dir(),
    }


def build_catalog() -> tuple[dict, list[str]]:
    """Return (catalog_dict, warnings)."""
    taxonomy = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    prev_skills: dict[str, dict] = {}
    if CATALOG.is_file():
        try:
            prev = json.loads(CATALOG.read_text(encoding="utf-8"))
            prev_skills = {s["name"]: s for s in prev.get("skills", [])}
        except (json.JSONDecodeError, KeyError):
            pass

    disk = collect_disk_skills()
    warnings: list[str] = []
    domains_out: list[dict] = []
    skills_out: list[dict] = []

    tax_domains = sorted(taxonomy["domains"], key=lambda d: d.get("order", 0))
    for d in tax_domains:
        did = d["id"]
        listed = list(d.get("skills") or [])
        on_disk = disk.get(did, set())

        missing = [s for s in listed if s not in on_disk]
        extra = sorted(on_disk - set(listed))
        for s in missing:
            warnings.append(f"[{did}] listed in taxonomy but no SKILL.md on disk: {s}")
        for s in extra:
            warnings.append(f"[{did}] on disk but missing from taxonomy: {s}")

        present = [s for s in listed if s in on_disk]
        for name in present:
            skills_out.append(build_skill_entry(did, name, prev_skills))

        domains_out.append({
            "id": did,
            "title": d["title"],
            "summary": d.get("summary", ""),
            "order": d.get("order", 0),
            "count": len(present),
        })

    unlisted_domains = sorted(set(disk) - {d["id"] for d in tax_domains})
    for did in unlisted_domains:
        warnings.append(f"domain folder not in taxonomy.yaml: {did}")

    catalog = {
        "generated_at": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": SOURCE_LABEL,
        "skill_count": len(skills_out),
        "domains": domains_out,
        "skills": skills_out,
    }
    return catalog, warnings


def dumps(catalog: dict) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"


_SCRIPT_RE = re.compile(
    r'(<script id="catalog-data"[^>]*>)(.*?)(</script>)', re.DOTALL)


def render_index(catalog: dict) -> str | None:
    """Return docs/index.html with the catalog JSON injected, or None if absent."""
    if not INDEX_HTML.is_file():
        return None
    html = INDEX_HTML.read_text(encoding="utf-8")
    # Escape "</" so a description containing "</script>" can't close the block.
    payload = json.dumps(catalog, ensure_ascii=False).replace("</", "<\\/")
    body = "\n" + payload + "\n"
    if _SCRIPT_RE.search(html):
        return _SCRIPT_RE.sub(lambda m: m.group(1) + body + m.group(3), html, count=1)
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="verify only; write nothing. Exit 1 if catalog.json is stale or drift exists.")
    args = ap.parse_args()

    catalog, warnings = build_catalog()
    new_text = dumps(catalog)

    for w in warnings:
        print(f"WARN  {w}", file=sys.stderr)

    print(f"Domains: {len(catalog['domains'])}  Skills: {catalog['skill_count']}")

    new_index = render_index(catalog)

    if args.check:
        current = CATALOG.read_text(encoding="utf-8") if CATALOG.is_file() else ""
        # Ignore the generated_at timestamp when comparing content.
        def strip_ts(t: str) -> str:
            try:
                obj = json.loads(t)
                obj.pop("generated_at", None)
                return json.dumps(obj, sort_keys=True)
            except json.JSONDecodeError:
                return t
        stale = strip_ts(current) != strip_ts(new_text)
        if stale:
            print("catalog.json is OUT OF DATE — run: python3 scripts/build_catalog.py", file=sys.stderr)
        index_stale = False
        if new_index is not None:
            cur_html = INDEX_HTML.read_text(encoding="utf-8")
            # Compare the injected data blocks, ignoring the timestamp.
            def block(html: str) -> str:
                m = _SCRIPT_RE.search(html)
                if not m:
                    return ""
                try:
                    obj = json.loads(m.group(2).strip().replace("<\\/", "</"))
                    obj.pop("generated_at", None)
                    return json.dumps(obj, sort_keys=True)
                except json.JSONDecodeError:
                    return m.group(2)
            index_stale = block(cur_html) != block(new_index)
            if index_stale:
                print("docs/index.html data is OUT OF DATE — run: python3 scripts/build_catalog.py", file=sys.stderr)
        if warnings or stale or index_stale:
            return 1
        print("catalog.json and docs/index.html are up to date.")
        return 0

    CATALOG.write_text(new_text, encoding="utf-8")
    print(f"Wrote {CATALOG.relative_to(REPO)}")
    if new_index is not None:
        INDEX_HTML.write_text(new_index, encoding="utf-8")
        print(f"Wrote {INDEX_HTML.relative_to(REPO)}")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
