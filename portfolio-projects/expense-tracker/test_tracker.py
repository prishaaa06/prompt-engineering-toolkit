import sqlite3
import unittest
from tracker import add_expense, amount_to_cents, connect, report


class ExpenseTests(unittest.TestCase):
    def test_amount_conversion(self):
        self.assertEqual(amount_to_cents("10.50"), 1050)
        with self.assertRaises(ValueError):
            amount_to_cents("-4")

    def test_report_aggregation(self):
        with connect(":memory:") as db:
            add_expense(db, "12.50", "Food", spent_on="2026-10-01")
            add_expense(db, "7.50", "Food", spent_on="2026-10-02")
            add_expense(db, "3.00", "Travel", spent_on="2026-11-01")
            self.assertEqual(report(db, "2026-10"), [("Food", 2000, 2)])


if __name__ == "__main__":
    unittest.main()
