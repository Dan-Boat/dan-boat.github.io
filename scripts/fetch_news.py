#!/usr/bin/env python3
"""Pull physical-climate-risk / storm-peril news into _data/news.yml.

Sources are public RSS/Atom feeds only — scientific journals (Copernicus,
Nature), agency bulletins (NOAA), and (re)insurance/ILS trade press (Artemis,
Reinsurance News). This deliberately does NOT touch LinkedIn: LinkedIn's
Terms of Service prohibit automated scraping/collection, so LinkedIn items
are out of scope for this script by design — add anything from LinkedIn to
_data/news.yml by hand instead. See CONTENT-GUIDE.md.

Usage:
    pip install feedparser pyyaml
    python scripts/fetch_news.py

The script is idempotent: it skips URLs already present in _data/news.yml
and only appends new, keyword-matched items. It never deletes existing
entries, so manual edits/curation are preserved. It also writes
digest.md (a human-readable summary of what it found) which
.github/workflows/fetch-news.yml uses as the pull request description —
that PR is the weekly report for you to review before anything is published
to the site.
"""
from __future__ import annotations

import datetime as dt
import html
import re
import sys
from pathlib import Path

try:
    import feedparser
    import yaml
except ImportError:
    sys.exit("Missing deps. Run: pip install feedparser pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_FILE = REPO_ROOT / "_data" / "news.yml"
DIGEST_FILE = REPO_ROOT / "digest.md"

# Public RSS/Atom feeds to poll, grouped by type. Add/remove/prune as you
# find sources — a feed that 404s or times out is skipped with a warning,
# it won't fail the whole run.
FEEDS = [
    # NOAA NHC/SPC operational bulletins (active-storm advisories, severe
    # thunderstorm watches, hourly outlooks) are deliberately NOT included
    # here: they're live warnings that go stale within hours, which doesn't
    # fit a curated news/publications digest reviewed weekly. If you want a
    # live storm tracker, that's a separate widget, not this feed. Re-add
    # them below if you decide you do want raw bulletins in the mix:
    #   {"url": "https://www.nhc.noaa.gov/index-at.xml", "source": "NOAA National Hurricane Center", "category": "Tropical Cyclone"},
    #   {"url": "https://www.spc.noaa.gov/products/spcrss.xml", "source": "NOAA Storm Prediction Center", "category": "Severe Convective Storm"},

    # --- Scientific journals (Copernicus EGU journals publish per-article RSS) --
    {"url": "https://nhess.copernicus.org/xml/rss2_0.xml", "source": "Natural Hazards and Earth System Sciences (NHESS)", "category": "Climate Modelling"},
    {"url": "https://esd.copernicus.org/xml/rss2_0.xml", "source": "Earth System Dynamics (ESD)", "category": "Climate Modelling"},
    {"url": "https://gmd.copernicus.org/xml/rss2_0.xml", "source": "Geoscientific Model Development (GMD)", "category": "Climate Modelling"},
    {"url": "https://www.nature.com/nclimate.rss", "source": "Nature Climate Change", "category": "Climate Modelling"},

    # --- (Re)insurance / ILS / parametric trade press ----------------------
    {"url": "https://www.artemis.bm/feed/", "source": "Artemis.bm (ILS & Parametric)", "category": "Parametric Insurance"},
    {"url": "https://www.reinsurancene.ws/feed/", "source": "Reinsurance News", "category": "General"},

    # --- Climate/science journalism -----------------------------------------
    {"url": "https://www.carbonbrief.org/feed/", "source": "Carbon Brief", "category": "Climate Modelling"},
]

# Only keep items whose title/summary mention one of these (case-insensitive).
# Journal/trade feeds are broad, so this filter keeps the digest focused on
# physical climate risk & storm perils specifically.
KEYWORDS = [
    "cyclone", "hurricane", "typhoon", "storm", "flood", "wildfire", "drought",
    "parametric", "reinsurance", "catastrophe", "cat bond", "cat-bond",
    "climate risk", "severe weather", "climate model", "extreme weather",
    "sea level", "heatwave", "heat wave", "precipitation", "monsoon",
]

KEYWORD_RE = re.compile("|".join(re.escape(k) for k in KEYWORDS), re.IGNORECASE)

# Agency bulletin feeds are already curated/on-topic by nature — don't
# keyword-filter them or near everything gets dropped.
NO_FILTER_SOURCES = {"NOAA National Hurricane Center", "NOAA Storm Prediction Center"}

# Cap how many new items a single feed can contribute per run, so one prolific
# journal doesn't drown out the rest of the digest.
MAX_PER_FEED = 6


def load_existing() -> list[dict]:
    if not NEWS_FILE.exists():
        return []
    items = yaml.safe_load(NEWS_FILE.read_text()) or []
    # YAML auto-parses unquoted dates (YYYY-MM-DD) into datetime.date objects;
    # normalize to strings so sorting/comparison against freshly fetched
    # items (which use ISO date strings) doesn't blow up.
    for item in items:
        if isinstance(item.get("date"), (dt.date, dt.datetime)):
            item["date"] = item["date"].isoformat()
    return items


# Boilerplate prefixes some feeds prepend to every summary — stripped so the
# digest reads as an actual summary instead of a copyright notice.
BOILERPLATE_PREFIXES = [
    r"^This content is copyright to \S+\s+and should not appear anywhere else,?\s*or an infringement has occurred\.\s*",
]


def strip_boilerplate(summary: str) -> str:
    for pattern in BOILERPLATE_PREFIXES:
        summary = re.sub(pattern, "", summary, flags=re.IGNORECASE)
    return summary.strip()


def matches(entry, feed_source: str) -> bool:
    if feed_source in NO_FILTER_SOURCES:
        return True
    text = f"{entry.get('title', '')} {entry.get('summary', '')}"
    return bool(KEYWORD_RE.search(text))


def fetch_feed(feed: dict) -> list[dict]:
    try:
        parsed = feedparser.parse(feed["url"])
    except Exception as exc:  # pragma: no cover - network dependent
        print(f"WARN: failed to fetch {feed['url']}: {exc}", file=sys.stderr)
        return []
    if parsed.bozo and not parsed.entries:
        print(f"WARN: could not parse {feed['url']}: {parsed.bozo_exception}", file=sys.stderr)
        return []
    return parsed.entries


def main() -> None:
    existing = load_existing()
    known_urls = {item.get("url") for item in existing}
    new_items = []

    for feed in FEEDS:
        added_from_feed = 0
        for entry in fetch_feed(feed):
            if added_from_feed >= MAX_PER_FEED:
                break
            url = entry.get("link")
            if not url or url in known_urls:
                continue
            if not matches(entry, feed["source"]):
                continue

            published = entry.get("published_parsed") or entry.get("updated_parsed")
            date = (
                dt.date(*published[:3]).isoformat()
                if published
                else dt.date.today().isoformat()
            )
            summary = re.sub("<[^<]+?>", "", entry.get("summary", ""))
            summary = html.unescape(summary)
            summary = re.sub(r"\s+", " ", summary).strip()
            summary = strip_boilerplate(summary)

            title = html.unescape(entry.get("title", "Untitled").strip())

            new_items.append(
                {
                    "title": title,
                    "url": url,
                    "source": feed["source"],
                    "date": date,
                    "category": feed["category"],
                    "summary": summary[:300],
                }
            )
            known_urls.add(url)
            added_from_feed += 1

    write_digest(new_items)

    if not new_items:
        print("No new items found.")
        return

    combined = new_items + existing
    combined.sort(key=lambda item: item["date"], reverse=True)
    NEWS_FILE.write_text(
        "# Industry / physical-climate-risk news feed shown on /news/.\n"
        "# Auto-updated by scripts/fetch_news.py via .github/workflows/fetch-news.yml\n"
        "# Feel free to hand-edit; the script only appends new, deduplicated items.\n\n"
        + yaml.dump(combined, sort_keys=False, allow_unicode=True, width=100)
    )
    print(f"Added {len(new_items)} new item(s) to {NEWS_FILE}")


def write_digest(new_items: list[dict]) -> None:
    """Write a human-readable weekly report used as the PR body."""
    today = dt.date.today().isoformat()
    lines = [f"# Weekly climate-risk news digest — {today}", ""]

    if not new_items:
        lines.append("No new items matched this week. Nothing to review.")
    else:
        lines.append(
            f"Found **{len(new_items)}** new item(s) from journals, NOAA bulletins, "
            "and (re)insurance/ILS trade press. Review below, then edit "
            "`_data/news.yml` directly in this PR if you want to trim summaries, "
            "recategorize, or drop an item, before merging.\n"
        )
        by_category: dict[str, list[dict]] = {}
        for item in new_items:
            by_category.setdefault(item["category"], []).append(item)

        for category, items in sorted(by_category.items()):
            lines.append(f"## {category} ({len(items)})")
            for item in items:
                lines.append(f"- **[{item['title']}]({item['url']})** — {item['source']}, {item['date']}")
                if item["summary"]:
                    lines.append(f"  > {item['summary'][:220]}")
            lines.append("")

        lines.append(
            "\n---\n_Note: LinkedIn is intentionally not covered by this automation "
            "(their Terms of Service prohibit scraping) — add LinkedIn-sourced items "
            "to `_data/news.yml` by hand._"
        )

    DIGEST_FILE.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
