# Student Performance Analyzer

A reproducible Python CLI project that reads student marks from CSV and computes subject averages, median scores, pass rates and an ordered leaderboard.

## Skills demonstrated
Python, CSV parsing, data validation, descriptive statistics, sorting, unit testing.

## Run
Requires Python 3.9+; no third-party libraries.

```bash
cd portfolio-projects/student-performance-analyzer
python analyzer.py sample_students.csv
python analyzer.py sample_students.csv --pass-mark 50
python -m unittest discover -p "test_*.py"
```

CSV columns: `student,math,programming,statistics`. All scores must be numeric and within 0–100. The default pass threshold is 40 **in every subject**.

## Extension ideas
Add additional subject columns, CSV output, and simple charts. Data is synthetic example data, not real student records.
