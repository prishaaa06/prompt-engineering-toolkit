import unittest
from analyzer import analyze


class AnalyzerTests(unittest.TestCase):
    def test_rank_and_pass_rate(self):
        records = [
            {"student": "A", "math": 90, "programming": 80, "statistics": 70},
            {"student": "B", "math": 20, "programming": 70, "statistics": 60},
        ]
        result = analyze(records)
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["pass_rate"], 50)
        self.assertEqual(result["ranking"][0]["student"], "A")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            analyze([])

    def test_invalid_pass_mark(self):
        with self.assertRaises(ValueError):
            analyze([{"student": "A", "math": 50, "programming": 50, "statistics": 50}], 120)


if __name__ == "__main__":
    unittest.main()
