import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from models.citation_handler import citation_report, find_citations
from models.evidence_tags import check_evidence_tags

AVOT = "הִלֵּל וְשַׁמַּאי קִבְּלוּ מֵהֶם. הִלֵּל אוֹמֵר, הֱוֵי מִתַּלְמִידָיו שֶׁל אַהֲרֹן"
fake = lambda ref: {"Pirkei_Avot.1.12": AVOT}[ref]


class Citations(unittest.TestCase):
    def test_verified_ignores_nikud_and_spelling(self):
        r = citation_report("טענה [מקור: Pirkei_Avot.1.12 | הלל ושמאי קיבלו מהם]", fetch=fake)
        self.assertEqual((r["total"], r["verified"], r["problems"]), (1, 1, []))

    def test_wrong_quote(self):
        r = citation_report("[מקור: Pirkei_Avot.1.12 | שמעיה ואבטליון קבלו מהם]", fetch=fake)
        self.assertEqual(r["problems"][0]["problem"], "quote_not_in_source")

    def test_short_quote_and_unknown_ref(self):
        r = citation_report("[מקור: Pirkei_Avot.1.12 | הלל ושמאי] [מקור: No_Such.1 | אחת שתיים שלוש]", fetch=fake)
        self.assertEqual([p["problem"] for p in r["problems"]], ["quote_too_short", "source_not_fetched"])

    def test_no_citations(self):
        self.assertEqual(find_citations("טקסט בלי מקורות"), [])

    @unittest.skipUnless(os.environ.get("LIVE_SEFARIA"), "set LIVE_SEFARIA=1 for the network test")
    def test_live(self):
        r = citation_report("[מקור: Pirkei_Avot.1.12 | הלל ושמאי קבלו מהם]")
        self.assertEqual(r["verified"], 1)


class Tags(unittest.TestCase):
    def test_tagged_and_untagged(self):
        paper = ("# כותרת\n\nהמודל הורץ שמונה עשרה פעמים והתוצאה נשמרה. [נמדד / מוכח: קובץ התוצאות]\n\n"
                 "השוק הזה צפוי לגדול מאוד בשנים הקרובות לפי כל ההערכות.\n\n"
                 "ייתכן שהקשר הזה סיבתי ולא מקרי בלבד. [ספקולציה]")
        r = check_evidence_tags(paper)
        self.assertEqual(r["paragraphs_checked"], 3)
        self.assertEqual(r["tag_counts"], {"measured": 1, "plausible": 0, "speculation": 1})
        self.assertEqual([u["paragraph"] for u in r["untagged"]], [3])
        self.assertFalse(r["ok"])


if __name__ == "__main__":
    unittest.main()
