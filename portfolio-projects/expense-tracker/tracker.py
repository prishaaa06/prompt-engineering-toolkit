"""SQLite-backed personal expense tracking CLI (standard library only)."""
import argparse
import csv
import sqlite3
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


def amount_to_cents(value):
    try:
        amount = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Amount must be a number") from exc
    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be positive and finite")
    cents = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) * 100
    return int(cents)


def connect(database):
    conn = sqlite3.connect(database)
    conn.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        spent_on TEXT NOT NULL,
        category TEXT NOT NULL,
        note TEXT NOT NULL,
        amount_cents INTEGER NOT NULL CHECK (amount_cents > 0)
    )""")
    conn.commit()
    return conn


def add_expense(conn, amount, category, note="", spent_on=None):
    when = spent_on or date.today().isoformat()
    date.fromisoformat(when)
    category = category.strip()
    if not category:
        raise ValueError("Category is required")
    conn.execute(
        "INSERT INTO expenses (spent_on, category, note, amount_cents) VALUES (?, ?, ?, ?)",
        (when, category, note, amount_to_cents(amount)),
    )
    conn.commit()


def report(conn, month):
    if len(month) != 7 or month[4] != "-":
        raise ValueError("Month format must be YYYY-MM")
    date.fromisoformat(month + "-01")
    rows = conn.execute(
        """SELECT category, SUM(amount_cents), COUNT(*)
           FROM expenses WHERE substr(spent_on, 1, 7) = ?
           GROUP BY category ORDER BY SUM(amount_cents) DESC, category""",
        (month,),
    ).fetchall()
    return rows


def export_csv(conn, destination):
    rows = conn.execute(
        "SELECT spent_on, category, note, amount_cents FROM expenses ORDER BY spent_on, id"
    ).fetchall()
    with open(destination, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["date", "category", "note", "amount"])
        for day, category, note, cents in rows:
            writer.writerow([day, category, note, f"{cents / 100:.2f}"])


def main():
    parser = argparse.ArgumentParser(description="Offline expense tracker")
    parser.add_argument("--db", type=Path, default=Path("expenses.db"))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("amount")
    add.add_argument("category")
    add.add_argument("--note", default="")
    add.add_argument("--date", dest="spent_on")
    summary = commands.add_parser("report")
    summary.add_argument("month", help="YYYY-MM")
    export = commands.add_parser("export")
    export.add_argument("destination", type=Path)
    args = parser.parse_args()
    with connect(args.db) as conn:
        if args.command == "add":
            add_expense(conn, args.amount, args.category, args.note, args.spent_on)
            print("Expense recorded.")
        elif args.command == "report":
            rows = report(conn, args.month)
            for category, cents, count in rows:
                print(f"{category}: INR {cents / 100:.2f} ({count} entries)")
            print(f"TOTAL: INR {sum(cents for _, cents, _ in rows) / 100:.2f}")
        else:
            export_csv(conn, args.destination)
            print(f"Exported to {args.destination}")


if __name__ == "__main__":
    main()
