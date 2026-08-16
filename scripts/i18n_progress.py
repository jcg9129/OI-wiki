#!/usr/bin/env python3
"""Generate the English-translation progress tracker (i18n-progress.md).

Status is derived from the filesystem plus a small content manifest, so the
tracker can never drift from reality and a new session can resume simply by
re-running this and taking the next pending batch.

Freshness / staleness
---------------------
An article is **done** when a sibling ``*.en.md`` exists *and* the source has
not changed since it was translated. To detect the latter, ``i18n-manifest.json``
records, per source, the git blob SHA of the ``*.md`` at translation time. On
each run the current blob SHA is recomputed and compared:

* no ``*.en.md``                         -> ``pending``
* ``*.en.md`` exists, SHA matches        -> ``done``
* ``*.en.md`` exists, SHA differs        -> ``stale``  (source edited upstream;
                                            re-translate, then re-stamp)
* ``*.en.md`` exists, no manifest entry  -> ``done`` and the current SHA is
                                            recorded (bootstrap / brand-new
                                            translation — no re-stamp needed)

The default run never *overwrites* an existing manifest entry, so once a file is
flagged ``stale`` it stays flagged until the translation is refreshed. After
re-translating a stale file, stamp it back to the current source version:

    python3 scripts/i18n_progress.py --record docs/path/to/article.md ...

Run from the repo root: ``python3 scripts/i18n_progress.py``.
"""

import glob
import hashlib
import json
import os
import sys
from datetime import date

# Non-article or intentionally-Chinese pages (see the OI Wiki i18n memory).
SKIP = {"docs/edit-landing.md", "docs/intro/format.md"}
FIRST_BATCH = 5    # smaller first batch for testing
BATCH = 20         # subsequent batches
BASELINE_DONE = 9  # intro pages translated before the bulk effort began

TRACKER = "i18n-progress.md"
MANIFEST = "i18n-manifest.json"


def blob_sha(path):
    """Git blob SHA-1 of a file's current bytes.

    Matches ``git hash-object <path>`` for LF/UTF-8 sources, so a source that a
    pulled commit does not actually change keeps an identical SHA (not stale),
    while any real content edit changes it (stale). Computed over the working
    tree, so it works whether or not the files are committed yet.
    """
    with open(path, "rb") as fh:
        data = fh.read()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def load_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def write_manifest(manifest):
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")


def sources():
    for f in glob.glob("docs/**/*.md", recursive=True):
        if not f.endswith(".en.md"):
            yield f


def scan(manifest):
    """Return (rows, additions).

    ``rows`` is a sorted list of ``(path, status)``. ``additions`` maps sources
    whose translation exists but has no manifest entry yet to their current SHA
    (bootstrap / newly-translated files) — these are recorded, existing entries
    are left untouched so staleness survives across runs.
    """
    rows = []
    additions = {}
    for f in sources():
        if f in SKIP:
            rows.append((f, "skip"))
            continue
        if not os.path.exists(f[:-3] + ".en.md"):
            rows.append((f, "pending"))
            continue
        cur = blob_sha(f)
        recorded = manifest.get(f)
        if recorded is None:
            additions[f] = cur
            rows.append((f, "done"))
        elif recorded == cur:
            rows.append((f, "done"))
        else:
            rows.append((f, "stale"))
    rows.sort()
    return rows, additions


def record(paths):
    """Stamp the given sources to their current SHA (post-(re)translation)."""
    manifest = load_manifest()
    stamped = []
    for p in paths:
        if p.endswith(".en.md"):
            p = p[:-6] + ".md"
        if not os.path.exists(p):
            print(f"skip (no source): {p}")
            continue
        if not os.path.exists(p[:-3] + ".en.md"):
            print(f"skip (no .en.md): {p}")
            continue
        manifest[p] = blob_sha(p)
        stamped.append(p)
    write_manifest(manifest)
    print(f"recorded {len(stamped)} file(s) into {MANIFEST}")
    for p in stamped:
        print("  ", p)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--record":
        record(sys.argv[2:])
        return

    manifest = load_manifest()
    rows, additions = scan(manifest)
    if additions:
        manifest.update(additions)
        write_manifest(manifest)

    done = [f for f, s in rows if s == "done"]
    pending = [f for f, s in rows if s == "pending"]
    stale = [f for f, s in rows if s == "stale"]
    skipped = [f for f, s in rows if s == "skip"]

    # Re-translations (stale) come first so upstream drift is fixed promptly,
    # then new work (pending).
    todo = stale + pending

    # The first bulk batch is smaller (testing); afterwards use the full size.
    # Baseline off the pre-bulk count so the already-done intro pages don't
    # consume the testing allowance.
    bulk_done = len(done) - BASELINE_DONE
    batch_size = FIRST_BATCH if bulk_done < FIRST_BATCH else BATCH
    next_batch = todo[:batch_size]

    mark = {"done": "x", "pending": " ", "stale": "!", "skip": "-"}
    lines = []
    lines.append("# OI Wiki — English translation progress\n")
    lines.append(f"_Generated {date.today().isoformat()} by `scripts/i18n_progress.py`._\n")
    lines.append(
        f"**{len(done)} done · {len(pending)} pending · {len(stale)} stale · "
        f"{len(skipped)} skipped · {len(rows)} total.**\n"
    )
    lines.append(
        "## Rules\n\n"
        "- Sequential only — one article at a time, never in parallel.\n"
        f"- Batches of {BATCH} (first batch {FIRST_BATCH} for testing). "
        "Stop after each batch and wait for explicit permission to continue.\n"
        "- Resume by re-running this script and taking the next queued items "
        "(stale re-translations first, then pending).\n"
        "- `[!]` = source changed upstream since translation. After "
        "re-translating, stamp it: "
        "`python3 scripts/i18n_progress.py --record <source.md>`. New "
        "translations are recorded automatically on the next run.\n"
    )
    lines.append("## Next batch\n")
    if next_batch:
        lines.append(f"Next up ({len(next_batch)} of {len(todo)} to do — "
                     f"{len(stale)} stale, {len(pending)} pending):\n")
        for f in next_batch:
            box = "!" if f in stale else " "
            lines.append(f"- [{box}] {f}")
        lines.append("")
    else:
        lines.append("All articles translated and up to date. 🎉\n")

    lines.append("## Full checklist\n")
    section = None
    for f, s in rows:
        top = f.split("/")[1] if "/" in f[len("docs/"):] else "(root)"
        if top != section:
            section = top
            lines.append(f"\n### {section}\n")
        if s == "skip":
            suffix = "  _(Chinese fallback by design)_"
        elif s == "stale":
            suffix = "  _(source changed — re-translate)_"
        else:
            suffix = ""
        lines.append(f"- [{mark[s]}] {f}{suffix}")
    lines.append("")

    with open(TRACKER, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"{len(done)} done, {len(pending)} pending, {len(stale)} stale, "
          f"{len(skipped)} skip -> wrote {TRACKER}")
    if additions:
        print(f"recorded {len(additions)} new baseline SHA(s) into {MANIFEST}")
    print(f"Next batch ({len(next_batch)}):")
    for f in next_batch:
        print("  ", "[stale]" if f in stale else "[new]  ", f)


if __name__ == "__main__":
    main()
