import unittest
from matcher import contains_phrase, extract_skills, match


class MatcherTests(unittest.TestCase):
    def test_word_boundaries(self):
        self.assertFalse(contains_phrase("pytorch", "torch"))
        self.assertTrue(contains_phrase("SQL and Python", "sql"))

    def test_aliases(self):
        self.assertIn("data visualization", extract_skills("Built Power BI reports"))

    def test_coverage(self):
        result = match("Python and SQL", "Python, SQL, Pandas")
        self.assertEqual(result["coverage_percent"], 66.7)
        self.assertEqual(result["missing_skills"], ["pandas"])

    def test_no_known_requirements(self):
        self.assertIsNone(match("Python", "Enjoys teamwork")["coverage_percent"])


if __name__ == "__main__":
    unittest.main()
