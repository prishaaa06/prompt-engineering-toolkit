# Explainable Job Description Skill Matcher

Compare a plain-text CV against a job description and receive an explainable report of matched skills, missing skills and keyword coverage.

## Skills demonstrated
Python regular expressions, text processing, information extraction, JSON, unit tests and simple explainable scoring.

## Run
Python 3.9+, no external dependencies.

```bash
cd portfolio-projects/job-description-skill-matcher
python matcher.py sample_resume.txt sample_job.txt
python -m unittest discover -p "test_*.py"
```

## How it works
1. Read both text files.
2. Detect known skills using a configurable `SKILLS` dictionary with aliases.
3. Match whole phrases case-insensitively, avoiding many substring false positives.
4. Report the overlap and skills listed in the job description but not detected in the CV.

**Important:** This is an educational rule-based demonstration, **not** a machine learning model, semantic similarity system, ATS score or hiring prediction. It does not judge whether somebody actually possesses a skill and may miss unfamiliar synonyms. Do not upload private CVs to a public repository.
