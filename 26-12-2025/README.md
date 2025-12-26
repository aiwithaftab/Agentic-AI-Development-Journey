# AI-Based Resume Screening - Learning Summary

## Overview
This project demonstrates a **basic AI-powered resume screening pipeline** using Python. The pipeline reads resumes in PDF format, extracts text, matches skills and experience keywords against a job description, computes a scoring metric, and ranks candidates based on their suitability.

---

## Tools & Libraries Used
- **Python 3.x**
- **pdfminer.six**: For extracting text from PDF resumes
- **Standard Python Libraries**: `os`, `pathlib`
- **Custom Scoring Module (`scorer.py`)**: Implements keyword matching and scoring logic

---

## Key Learning Points

### 1. Job Description Loading
- Loaded a job description from a file or string.
- Normalized text by converting to lowercase and standardizing spacing.
```python
job_description = load_job_description(job_description_path)
