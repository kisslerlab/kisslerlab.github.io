#!/usr/bin/env python3
"""
Sync new publications from ORCID into _data/publications.yml.

What it does
------------
1. Reads your ORCID record's works (public API — no auth needed).
2. Collects the DOIs and skips any that already appear in _data/publications.yml.
3. For each genuinely new DOI, pulls clean metadata from Crossref (ordered author
   list, venue, year, type), falling back to the ORCID summary if Crossref has no
   record yet (common for brand-new preprints).
4. Inserts draft entries at the top of the `items:` list with `tags: []` and
   `senior: false` left as TODO placeholders for you to fill in.

It intentionally does NOT guess `tags` or `senior` — those are editorial calls.
Run it in CI (see .github/workflows/sync-publications.yml); it opens a pull
request so nothing changes on the live site until you review and merge.

Environment
-----------
ORCID_ID   your ORCID iD, e.g. 0000-0002-1825-0097   (required)
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ORCID = os.environ.get("ORCID_ID", "").strip()
HERE = os.path.dirname(os.path.abspath(__file__))
PUB_FILE = os.path.normpath(os.path.join(HERE, "..", "_data", "publications.yml"))
UA = "kisslerlab-site-sync (mailto:stephen.kissler@colorado.edu)"


def get_json(url, accept="application/json", tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    print(f"  ! request failed: {url} ({last})", file=sys.stderr)
    return None


def orcid_works(orcid):
    """Return [{doi, title, year, type}] for every work with a DOI."""
    data = get_json(f"https://pub.orcid.org/v3.0/{orcid}/works")
    if not data:
        return []
    works = []
    for group in data.get("group", []):
        summaries = group.get("work-summary", [])
        if not summaries:
            continue
        s = summaries[0]
        doi = None
        for e in ((s.get("external-ids") or {}).get("external-id") or []):
            if (e.get("external-id-type") or "").lower() == "doi":
                doi = (e.get("external-id-value") or "").strip().lower()
                break
        if not doi:
            continue
        title = (((s.get("title") or {}).get("title") or {}).get("value") or "").strip()
        year = (((s.get("publication-date") or {}).get("year") or {}).get("value") or "").strip()
        works.append({"doi": doi, "title": title, "year": year, "type": (s.get("type") or "").lower()})
    return works


def existing_dois(text):
    return {m.group(0).lower() for m in re.finditer(r"10\.\d{4,9}/[^\s\"']+", text)}


def crossref(doi):
    d = get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    if not d or "message" not in d:
        return None
    m = d["message"]
    authors = []
    for a in m.get("author", []):
        name = (a.get("given", "") + " " + a.get("family", "")).strip()
        if name:
            authors.append(name)
    container = (m.get("container-title") or m.get("group-title") or [])
    venue = container[0] if container else (m.get("publisher") or "")
    dp = (m.get("issued", {}).get("date-parts") or [[None]])[0]
    year = dp[0] if dp and dp[0] else None
    cr_type = (m.get("type") or "").lower()
    return {"authors": authors, "venue": venue, "year": year, "type": cr_type}


def is_preprint(orcid_type, cr_type):
    t = (cr_type or orcid_type or "")
    return "posted-content" in t or "preprint" in t


def yaml_escape(s):
    return (s or "").replace("\\", "\\\\").replace('"', '\\"')


def format_entry(work):
    doi = work["doi"]
    cr = crossref(doi)
    title = work.get("title") or "TODO — verify title"
    authors = ", ".join(cr["authors"]) if (cr and cr["authors"]) else "TODO — verify author list"
    venue = (cr and cr["venue"]) or ""
    year = (cr and cr["year"]) or work.get("year") or ""
    ptype = "preprint" if is_preprint(work.get("type"), cr and cr["type"]) else "paper"
    if not venue:
        venue = "Preprint" if ptype == "preprint" else "TODO — venue"
    return (
        f"  # TODO: set tags + confirm `senior` (added by ORCID sync)\n"
        f'  - title: "{yaml_escape(title)}"\n'
        f'    authors: "{yaml_escape(authors)}"\n'
        f'    venue: "{yaml_escape(str(venue))}"\n'
        f"    year: {year}\n"
        f"    type: {ptype}\n"
        f"    tags: []          # TODO: e.g. [viral-kinetics, surveillance]\n"
        f"    senior: false     # TODO: true if Stephen is first/last/co-senior\n"
        f'    doi: "{doi}"\n'
        f'    url: "https://doi.org/{doi}"\n'
    )


def main():
    if not ORCID:
        print("ERROR: set the ORCID_ID environment variable (repo variable).", file=sys.stderr)
        sys.exit(1)

    text = open(PUB_FILE, encoding="utf-8").read()
    have = existing_dois(text)

    works = orcid_works(ORCID)
    if not works:
        print("No works returned from ORCID (check the ORCID_ID). Nothing to do.")
        return

    new = [w for w in works if w["doi"] not in have]
    if not new:
        print(f"Up to date — {len(works)} ORCID works, none new.")
        return

    # newest first
    new.sort(key=lambda w: (w.get("year") or ""), reverse=True)
    print(f"Found {len(new)} new publication(s):")
    for w in new:
        print(f"  + {w['doi']}  {w.get('title','')[:70]}")

    block = "\n".join(format_entry(w) for w in new)
    # insert right after the `items:` line
    marker = re.search(r"^items:\s*$", text, re.M)
    if not marker:
        print("ERROR: could not find `items:` in publications.yml", file=sys.stderr)
        sys.exit(1)
    insert_at = marker.end()
    updated = text[:insert_at] + "\n" + block + text[insert_at:]
    open(PUB_FILE, "w", encoding="utf-8").write(updated)
    print(f"Wrote {len(new)} draft entr{'y' if len(new)==1 else 'ies'} to {PUB_FILE}.")


if __name__ == "__main__":
    main()
