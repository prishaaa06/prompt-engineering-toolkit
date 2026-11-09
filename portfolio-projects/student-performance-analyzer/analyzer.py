"""Analyze student marks from a CSV using only Python's standard library."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

SUBJECTS = ("math", "programming", "statistics")


def load_records(path):
    records = []
    with open(path, newline="", encoding="utf-8") as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            try:
                name = row["student"].strip()
                if not name:
                    raise ValueError("student name cannot be empty")
                scores = {s: float(row[s]) for s in SUBJECTS}
                if any(not 0 <= score <= 100 for score in scores.values()):
                    raise ValueError("scores must be between 0 and 100")
                records.append({"student": name, **scores})
            except (KeyError, ValueError, TypeError) as exc:
                raise ValueError(f"Invalid CSV row {line}: {exc}") from exc
    if not records:
        raise ValueError("CSV has no student records")
    return records


def analyze(records, pass_mark=40):
    if not records:
        raise ValueError("At least one student record is required")
    if not 0 <= pass_mark <= 100:
        raise ValueError("pass_mark must be between 0 and 100")
    students = []
    for row in records:
        scores = [row[s] for s in SUBJECTS]
        students.append({
            "student": row["student"],
            "average": round(mean(scores), 2),
            "passed": all(score >= pass_mark for score in scores),
        })
    ranked = sorted(students, key=lambda r: (-r["average"], r["student"].lower()))
    return {
        "count": len(records),
        "subject_averages": {s: round(mean(r[s] for r in records), 2) for s in SUBJECTS},
        "class_median": round(median(s["average"] for s in students), 2),
        "pass_rate": round(100 * sum(s["passed"] for s in students) / len(students), 2),
        "ranking": ranked,
    }


def main():
    parser = argparse.ArgumentParser(description="Student score analytics")
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--pass-mark", type=float, default=40)
    args = parser.parse_args()
    result = analyze(load_records(args.csv_file), args.pass_mark)
    print(f"Students: {result['count']}; Pass rate: {result['pass_rate']}%")
    print(f"Median average: {result['class_median']}")
    for subject, average in result["subject_averages"].items():
        print(f"{subject}: {average}")
    print("\nLeaderboard:")
    for position, student in enumerate(result["ranking"], 1):
        outcome = "PASS" if student["passed"] else "REVIEW"
        print(f"{position}. {student['student']}: {student['average']:.2f} ({outcome})")


if __name__ == "__main__":
    main()
