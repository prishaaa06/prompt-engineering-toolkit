# Offline Expense Tracker (Python + SQLite)

A command-line expense manager that stores personal expenses locally, groups monthly totals by category, and exports transactions to CSV.

## Skills demonstrated
SQLite, SQL queries, parameterized inserts, Python argparse, decimal-safe money representation, data validation, tests.

## Run
Python 3.9+, standard library only.

```bash
cd portfolio-projects/expense-tracker
python tracker.py add 249.50 Food --note "Lunch"
python tracker.py add 60 Travel --date 2026-11-10
python tracker.py report 2026-11
python tracker.py export expenses_export.csv
python -m unittest discover -p "test_*.py"
```

By default, data is stored in `expenses.db` in the current working directory. Use `--db myfile.db` **before** the command to select another local database.

## Privacy
No accounts, internet requests or cloud sync. The database and exports contain your personal spending information; do not commit them to GitHub. Amounts are represented as integer paise (minor currency units) to avoid binary floating-point errors.
