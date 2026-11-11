"""Citation checking against the Sefaria API.

A citation in a paper is written as:

    [מקור: Pirkei_Avot.1.12 | הלל ושמאי קבלו מהם]

The part before the bar is a Sefaria reference in API form; the part after it
is a quote of at least three words that must appear in that text. Comparison
ignores nikud, cantillation, punctuation and plene/defective spelling.
The matching logic is the same one used by esh27-core/graph/tools/kg.py.
"""
import json
import re
import unicodedata
import urllib.parse
import urllib.request

CITATION_RE = re.compile(r"\[מקור:\s*([^|\]]+?)\s*\|\s*([^\]]+?)\s*\]")
MIN_QUOTE_WORDS = 3
API = "https://www.sefaria.org/api/texts/{ref}?context=0&commentary=0"


def _norm(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s).replace("־", " ")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
    s = re.sub(r"[^א-ת ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _loose(s: str) -> str:
    return re.sub(r"[וי]", "", _norm(s))


def _flat(x) -> str:
    return x if isinstance(x, str) else " ".join(_flat(i) for i in x)


def fetch_hebrew(ref: str, timeout: int = 30) -> str:
    url = API.format(ref=urllib.parse.quote(ref, safe=".,_-:'()"))
    with urllib.request.urlopen(url, timeout=timeout) as f:
        return _flat(json.load(f).get("he", ""))


def find_citations(paper: str) -> list:
    return [{"ref": m.group(1).strip(), "quote": m.group(2).strip()} for m in CITATION_RE.finditer(paper)]


def citation_report(paper: str, fetch=fetch_hebrew) -> dict:
    """Check every citation. Returns {"total", "verified", "problems": [...]}."""
    cache, problems, verified = {}, [], 0
    citations = find_citations(paper)
    for c in citations:
        ref, quote = c["ref"], c["quote"]
        if len(_norm(quote).split()) < MIN_QUOTE_WORDS:
            problems.append({**c, "problem": "quote_too_short"})
            continue
        if ref not in cache:
            try:
                cache[ref] = fetch(ref)
            except Exception as ex:  # network error or unknown reference
                cache[ref] = None
                problems.append({**c, "problem": "source_not_fetched", "detail": str(ex)})
                continue
        text = cache[ref]
        if text is None:
            problems.append({**c, "problem": "source_not_fetched"})
        elif not text.strip():
            problems.append({**c, "problem": "source_empty"})
        elif _loose(quote) not in _loose(text):
            problems.append({**c, "problem": "quote_not_in_source"})
        else:
            verified += 1
    return {"total": len(citations), "verified": verified, "problems": problems}


def check_citations(paper: str) -> bool:
    """True only when the paper has at least one citation and all of them verify."""
    r = citation_report(paper)
    return r["total"] > 0 and not r["problems"]
