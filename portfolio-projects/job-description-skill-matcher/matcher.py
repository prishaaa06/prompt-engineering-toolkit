"""Explainable keyword-based job description / CV skill matcher."""
import argparse
import json
import re
from pathlib import Path

SKILLS = {
    "python": ["python"],
    "sql": ["sql", "postgresql", "mysql"],
    "machine learning": ["machine learning", "ml models"],
    "data visualization": ["data visualization", "power bi", "tableau"],
    "statistics": ["statistics", "statistical analysis"],
    "excel": ["excel", "spreadsheets"],
    "git": ["git", "github"],
    "communication": ["communication", "presentations"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "tensorflow": ["tensorflow"],
    "scikit-learn": ["scikit-learn", "sklearn"],
}


def contains_phrase(text, phrase):
    return re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, flags=re.I) is not None


def extract_skills(text):
    return {skill for skill, phrases in SKILLS.items() if any(contains_phrase(text, p) for p in phrases)}


def match(cv_text, job_text):
    cv = extract_skills(cv_text)
    required = extract_skills(job_text)
    matched = cv & required
    missing = required - cv
    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "cv_skills_detected": sorted(cv),
        "job_skills_detected": sorted(required),
        "coverage_percent": round(100 * len(matched) / len(required), 1) if required else None,
        "note": "Keyword coverage only; not an ATS score or hiring prediction.",
    }


def main():
    parser = argparse.ArgumentParser(description="Transparent CV-to-JD skill matcher")
    parser.add_argument("resume", type=Path, help="Plain-text resume")
    parser.add_argument("job_description", type=Path, help="Plain-text job description")
    args = parser.parse_args()
    output = match(
        args.resume.read_text(encoding="utf-8"),
        args.job_description.read_text(encoding="utf-8"),
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
