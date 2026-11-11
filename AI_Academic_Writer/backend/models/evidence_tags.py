"""Evidence-tag check for 27ACADEMY papers.

House rule: every factual claim carries exactly one of three tags.
This check works at paragraph level: each body paragraph must contain at
least one tag. Headings, list-free blank lines, citations-only lines and
paragraphs that start with a skip marker are ignored. It cannot tell whether
the tag is the right one for the claim; that stays with the reviewer.
"""
import re

TAGS = {
    "measured": re.compile(r"\[\s*נמדד\s*/\s*מוכח[^\]]*\]"),
    "plausible": re.compile(r"\[\s*סביר עם מקור[^\]]*\]"),
    "speculation": re.compile(r"\[\s*ספקולציה[^\]]*\]"),
}
SKIP_PREFIXES = ("#", "|", "```", "---", "status:", "נכתב:", "מעמד:")
MIN_WORDS = 6  # shorter fragments are titles or labels, not claims


def check_evidence_tags(paper: str) -> dict:
    counts = {k: 0 for k in TAGS}
    untagged, checked = [], 0
    for i, para in enumerate(re.split(r"\n\s*\n", paper), start=1):
        p = para.strip()
        if not p or p.startswith(SKIP_PREFIXES) or len(p.split()) < MIN_WORDS:
            continue
        checked += 1
        hits = {k: len(rx.findall(p)) for k, rx in TAGS.items()}
        for k, n in hits.items():
            counts[k] += n
        if not any(hits.values()):
            untagged.append({"paragraph": i, "preview": p[:80]})
    return {"paragraphs_checked": checked, "tag_counts": counts,
            "untagged": untagged, "ok": checked > 0 and not untagged}
